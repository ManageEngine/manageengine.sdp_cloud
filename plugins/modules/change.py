# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: change
author:
  - Harish Kumar (@harishkumar-k-7052)
short_description: Manage changes in ManageEngine ServiceDesk Plus Cloud
description:
  - Creates, updates, or deletes change records in ManageEngine ServiceDesk Plus Cloud.
  - When C(state=present) (default) and C(change_id) is omitted, creates a new change.
    The C(title) option is mandatory for create operations.
  - When C(state=present) and C(change_id) is set, updates the existing change.
    Supports idempotency — skips the API call if no changes are detected.
  - When C(state=absent), deletes the change identified by C(change_id).
  - Supports check mode and diff mode.
  - See U(https://www.manageengine.com/products/service-desk/sdpod-v3-api/changes/change.html) for full API details.
extends_documentation_fragment:
  - manageengine.sdp_cloud.sdp_base
  - manageengine.sdp_cloud.auth
options:
  change_id:
    description:
      - The ID of an existing change record.
      - Required for update (C(state=present)) and delete (C(state=absent)) operations.
      - Omit when creating a new change.
    type: str
  state:
    description:
      - The desired state of the change.
      - C(present) ensures the change exists (create or update).
      - C(absent) ensures the change is deleted.
    type: str
    default: present
    choices: [present, absent]
  title:
    description:
      - The title of the change.
      - B(Mandatory) when creating a new change (C(state=present) without C(change_id)).
      - Optional when updating (only include to change it).
    type: str
  payload:
    description:
      - A dictionary of additional change attributes to set.
      - Supported fields include C(description), C(comment), C(retrospective), C(stage),
        C(status), C(template), C(priority), C(urgency), C(impact), C(category),
        C(subcategory), C(item), C(site), C(group), C(change_requester), C(change_manager),
        C(change_owner), C(change_type), C(reason_for_change), C(risk), C(workflow),
        C(scheduled_start_time), C(scheduled_end_time), C(created_time), C(completed_time),
        and grouped fields C(roll_out_plan_description), C(back_out_plan_description).
      - For create, include all desired fields. For update, include only fields to change.
      - Not used when C(state=absent).
    type: dict
'''

EXAMPLES = r'''
- name: Create a Change (minimal)
  manageengine.sdp_cloud.change:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    title: "Upgrade database server"

- name: Create a Change (with extra fields)
  manageengine.sdp_cloud.change:
    domain: "sdpondemand.manageengine.com"
    client_id: "your_client_id"
    client_secret: "your_client_secret"
    refresh_token: "your_refresh_token"
    dc: "US"
    portal_name: "ithelpdesk"
    title: "Upgrade database server"
    payload:
      description: "Upgrade PostgreSQL from 14 to 16"
      priority: "High"
      change_requester: "admin@example.com"
      group: "Infrastructure"

- name: Update a Change
  manageengine.sdp_cloud.change:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    change_id: "123456"
    payload:
      priority: "Low"
      status: "In Progress"

- name: Delete a Change
  manageengine.sdp_cloud.change:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    change_id: "123456"
    state: absent
'''

RETURN = r'''
response:
  description: The raw response from the SDP Cloud API.
  returned: always
  type: dict
change:
  description: The change record from the API response (convenience accessor).
  returned: on create or update
  type: dict
change_id:
  description: The ID of the created, updated, or deleted change.
  returned: on create or update
  type: str
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.api_util import (
    SDPClient, base_argument_spec, construct_endpoint,
    AUTH_MUTUALLY_EXCLUSIVE, AUTH_REQUIRED_TOGETHER
)
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.sdp_config import MODULE_CONFIG
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.write_helpers import (
    handle_absent, handle_present,
)

ENTITY = 'change'


def run_module():
    config = MODULE_CONFIG[ENTITY]
    module_args = base_argument_spec()
    module_args.update(dict(
        change_id=dict(type='str'),
        state=dict(type='str', default='present', choices=['present', 'absent']),
        title=dict(type='str'),
        payload=dict(type='dict'),
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=AUTH_MUTUALLY_EXCLUSIVE,
        required_together=AUTH_REQUIRED_TOGETHER
    )

    module.params['parent_module_name'] = ENTITY
    module.params['parent_id'] = module.params.get('change_id')

    client = SDPClient(module)
    endpoint = construct_endpoint(module)

    if module.params['state'] == 'absent':
        handle_absent(module, client, endpoint, config)
    else:
        handle_present(module, client, endpoint, config)


def main():
    run_module()


if __name__ == '__main__':
    main()
