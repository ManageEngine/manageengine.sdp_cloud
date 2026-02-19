# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: problem
author:
  - Harish Kumar (@harishkumar-k-7052)
short_description: Manage problems in ManageEngine ServiceDesk Plus Cloud
description:
  - Creates, updates, or deletes problem records in ManageEngine ServiceDesk Plus Cloud.
  - When C(state=present) (default) and C(problem_id) is omitted, creates a new problem.
    The C(title) field inside C(payload) is mandatory for create operations.
  - When C(state=present) and C(problem_id) is set, updates the existing problem.
    Supports idempotency — skips the API call if no changes are detected.
  - When C(state=absent), deletes the problem identified by C(problem_id).
  - Supports check mode and diff mode.
  - See U(https://www.manageengine.com/products/service-desk/sdpod-v3-api/problems/problem.html) for full API details.
extends_documentation_fragment:
  - manageengine.sdp_cloud.sdp_base
  - manageengine.sdp_cloud.auth
options:
  problem_id:
    description:
      - The ID of an existing problem record.
      - Required for update (C(state=present)) and delete (C(state=absent)) operations.
      - Omit when creating a new problem.
    type: str
  state:
    description:
      - The desired state of the problem.
      - C(present) ensures the problem exists (create or update).
      - C(absent) ensures the problem is deleted.
    type: str
    default: present
    choices: [present, absent]
  payload:
    description:
      - A dictionary of problem attributes to set.
      - The C(title) field is B(mandatory) when creating a new problem.
      - Supported fields include C(title), C(description), C(impact_details), C(priority), C(urgency),
        C(impact), C(status), C(template), C(category), C(subcategory), C(item), C(site),
        C(group), C(requester), C(technician), C(reported_by), C(due_by_time), C(reported_time),
        C(closed_time), and grouped fields (C(impact_details_description), C(root_cause_description),
        C(symptoms_description), C(known_error_comments), C(is_known_error), C(close_details_comments),
        C(closure_code), C(resolution_details_description), C(workaround_details_description)).
      - For create, include all desired fields. For update, include only fields to change.
      - Not used when C(state=absent).
    type: dict
'''

EXAMPLES = r'''
- name: Create a Problem (minimal)
  manageengine.sdp_cloud.problem:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    payload:
      title: "Server connectivity issues in DC-2"

- name: Create a Problem (with extra fields)
  manageengine.sdp_cloud.problem:
    domain: "sdpondemand.manageengine.com"
    client_id: "{{ sdp_client_id }}"
    client_secret: "{{ sdp_client_secret }}"
    refresh_token: "{{ sdp_refresh_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    payload:
      title: "Server connectivity issues in DC-2"
      description: "Web server unresponsive since 10:00 AM"
      priority: "High"
      requester: "admin@example.com"
      group: "Infrastructure"

- name: Update a Problem
  manageengine.sdp_cloud.problem:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    problem_id: "123456"
    payload:
      priority: "Low"
      status: "In Progress"

- name: Delete a Problem
  manageengine.sdp_cloud.problem:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    problem_id: "123456"
    state: absent
'''

RETURN = r'''
response:
  description: The raw response from the SDP Cloud API.
  returned: always
  type: dict
problem:
  description: The problem record from the API response.
  returned: on create or update
  type: dict
  sample:
    id: "234567890123456"
    title: "Server connectivity issues in DC-2"
    status:
      name: "Open"
      id: "100000000000001"
    priority:
      name: "High"
      id: "100000000000002"
    group:
      name: "Infrastructure"
      id: "100000000000004"
    created_time:
      display_value: "Nov 10, 2025 10:00 AM"
      value: "1731234000000"
problem_id:
  description: The ID of the created, updated, or deleted problem.
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

ENTITY = 'problem'


def run_module():
    config = MODULE_CONFIG[ENTITY]
    module_args = base_argument_spec()
    module_args.update(dict(
        problem_id=dict(type='str'),
        state=dict(type='str', default='present', choices=['present', 'absent']),
        payload=dict(type='dict'),
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=AUTH_MUTUALLY_EXCLUSIVE,
        required_together=AUTH_REQUIRED_TOGETHER,
        required_if=[
            ('state', 'absent', ('problem_id',)),
        ],
    )

    module.params['parent_module_name'] = ENTITY
    module.params['parent_id'] = module.params.get('problem_id')

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
