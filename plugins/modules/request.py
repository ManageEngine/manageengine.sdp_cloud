# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: request
author:
  - Harish Kumar (@harishkumar-k-7052)
short_description: Manage requests in ManageEngine ServiceDesk Plus Cloud
description:
  - Creates, updates, or deletes request records in ManageEngine ServiceDesk Plus Cloud.
  - When C(state=present) (default) and C(request_id) is omitted, creates a new request.
    The C(subject) field inside C(payload) is mandatory for create operations.
  - When C(state=present) and C(request_id) is set, updates the existing request.
    Supports idempotency — skips the API call if no changes are detected.
  - When C(state=absent), deletes the request identified by C(request_id).
  - Supports check mode and diff mode.
  - See U(https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request.html) for full API details.
extends_documentation_fragment:
  - manageengine.sdp_cloud.sdp_base
  - manageengine.sdp_cloud.auth
options:
  request_id:
    description:
      - The ID of an existing request record.
      - Required for update (C(state=present)) and delete (C(state=absent)) operations.
      - Omit when creating a new request.
    type: str
  state:
    description:
      - The desired state of the request.
      - C(present) ensures the request exists (create or update).
      - C(absent) ensures the request is deleted.
    type: str
    default: present
    choices: [present, absent]
  payload:
    description:
      - A dictionary of request attributes to set.
      - The C(subject) field is B(mandatory) when creating a new request.
      - Supported fields include C(subject), C(description), C(priority), C(urgency), C(impact),
        C(status), C(requester), C(technician), C(group), C(category), C(subcategory),
        C(item), C(due_by_time), C(template), C(mode), C(level), C(site),
        C(on_behalf_of), C(editor), C(udf_fields), and more.
      - For create, include all desired fields. For update, include only fields to change.
      - Not used when C(state=absent).
    type: dict
'''

EXAMPLES = r'''
- name: Create a Request (minimal)
  manageengine.sdp_cloud.request:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    payload:
      subject: "Server down in DC-2"

- name: Create a Request (with extra fields)
  manageengine.sdp_cloud.request:
    domain: "sdpondemand.manageengine.com"
    client_id: "{{ sdp_client_id }}"
    client_secret: "{{ sdp_client_secret }}"
    refresh_token: "{{ sdp_refresh_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    payload:
      subject: "Server down in DC-2"
      description: "Web server unresponsive since 10:00 AM"
      priority: "High"
      requester: "admin@example.com"
      group: "Infrastructure"

- name: Update a Request
  manageengine.sdp_cloud.request:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    request_id: "123456"
    payload:
      priority: "Low"
      status: "In Progress"

- name: Delete a Request
  manageengine.sdp_cloud.request:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    request_id: "123456"
    state: absent
'''

RETURN = r'''
response:
  description: The raw response from the SDP Cloud API.
  returned: always
  type: dict
request:
  description: The request record from the API response.
  returned: on create or update
  type: dict
  sample:
    id: "234567890123456"
    subject: "Server down in DC-2"
    status:
      name: "Open"
      id: "100000000000001"
    priority:
      name: "High"
      id: "100000000000002"
    requester:
      email_id: "user@example.com"
      name: "John Doe"
      id: "100000000000003"
    group:
      name: "Infrastructure"
      id: "100000000000004"
    created_time:
      display_value: "Nov 10, 2025 10:00 AM"
      value: "1731234000000"
request_id:
  description: The ID of the created, updated, or deleted request.
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

ENTITY = 'request'


def run_module():
    config = MODULE_CONFIG[ENTITY]
    module_args = base_argument_spec()
    module_args.update(dict(
        request_id=dict(type='str'),
        state=dict(type='str', default='present', choices=['present', 'absent']),
        payload=dict(type='dict'),
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=AUTH_MUTUALLY_EXCLUSIVE,
        required_together=AUTH_REQUIRED_TOGETHER,
        required_if=[
            ('state', 'absent', ('request_id',)),
        ],
    )

    module.params['parent_module_name'] = ENTITY
    module.params['parent_id'] = module.params.get('request_id')

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
