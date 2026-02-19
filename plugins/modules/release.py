# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: release
author:
  - Harish Kumar (@harishkumar-k-7052)
short_description: Manage releases in ManageEngine ServiceDesk Plus Cloud
description:
  - Creates, updates, or deletes release records in ManageEngine ServiceDesk Plus Cloud.
  - When C(state=present) (default) and C(release_id) is omitted, creates a new release.
    The C(title) field inside C(payload) is mandatory for create operations.
  - When C(state=present) and C(release_id) is set, updates the existing release.
    Supports idempotency — skips the API call if no changes are detected.
  - When C(state=absent), deletes the release identified by C(release_id).
  - Supports check mode and diff mode.
  - See U(https://www.manageengine.com/products/service-desk/sdpod-v3-api/releases/release.html) for full API details.
extends_documentation_fragment:
  - manageengine.sdp_cloud.sdp_base
  - manageengine.sdp_cloud.auth
options:
  release_id:
    description:
      - The ID of an existing release record.
      - Required for update (C(state=present)) and delete (C(state=absent)) operations.
      - Omit when creating a new release.
    type: str
  state:
    description:
      - The desired state of the release.
      - C(present) ensures the release exists (create or update).
      - C(absent) ensures the release is deleted.
    type: str
    default: present
    choices: [present, absent]
  payload:
    description:
      - A dictionary of release attributes to set.
      - The C(title) field is B(mandatory) when creating a new release.
      - Supported fields include C(title), C(description), C(stage), C(status), C(template),
        C(priority), C(urgency), C(impact), C(category), C(subcategory), C(item),
        C(site), C(group), C(release_requester), C(release_engineer), C(release_manager),
        C(release_type), C(reason_for_release), C(risk), C(workflow),
        C(scheduled_start_time), C(scheduled_end_time), C(created_time), C(completed_time),
        C(next_review_on), and grouped fields C(roll_out_plan_description),
        C(back_out_plan_description).
      - For create, include all desired fields. For update, include only fields to change.
      - Not used when C(state=absent).
    type: dict
'''

EXAMPLES = r'''
- name: Create a Release (minimal)
  manageengine.sdp_cloud.release:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    payload:
      title: "Q1 2026 Production Release"

- name: Create a Release (with extra fields)
  manageengine.sdp_cloud.release:
    domain: "sdpondemand.manageengine.com"
    client_id: "{{ sdp_client_id }}"
    client_secret: "{{ sdp_client_secret }}"
    refresh_token: "{{ sdp_refresh_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    payload:
      title: "Q1 2026 Production Release"
      description: "Quarterly production deployment"
      priority: "High"
      release_engineer: "admin@example.com"
      group: "Release Management"

- name: Update a Release
  manageengine.sdp_cloud.release:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    release_id: "123456"
    payload:
      priority: "Low"
      status: "In Progress"

- name: Delete a Release
  manageengine.sdp_cloud.release:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    release_id: "123456"
    state: absent
'''

RETURN = r'''
response:
  description: The raw response from the SDP Cloud API.
  returned: always
  type: dict
release:
  description: The release record from the API response.
  returned: on create or update
  type: dict
  sample:
    id: "234567890123456"
    title: "Q1 2026 Production Release"
    status:
      name: "Open"
      id: "100000000000001"
    priority:
      name: "High"
      id: "100000000000002"
    stage:
      name: "Planning"
      id: "100000000000006"
    created_time:
      display_value: "Nov 10, 2025 10:00 AM"
      value: "1731234000000"
release_id:
  description: The ID of the created, updated, or deleted release.
  returned: on create or update
  type: str
  sample: "234567890123456"
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

ENTITY = 'release'


def run_module():
    config = MODULE_CONFIG[ENTITY]
    module_args = base_argument_spec()
    module_args.update(dict(
        release_id=dict(type='str'),
        state=dict(type='str', default='present', choices=['present', 'absent']),
        payload=dict(type='dict'),
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=AUTH_MUTUALLY_EXCLUSIVE,
        required_together=AUTH_REQUIRED_TOGETHER,
        required_if=[
            ('state', 'absent', ('release_id',)),
        ],
    )

    module.params['parent_module_name'] = ENTITY
    module.params['parent_id'] = module.params.get('release_id')

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
