# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: write_record
author:
  - Harish Kumar (@harishkumar-k-7052)
short_description: Manage records in ManageEngine ServiceDesk Plus Cloud
description:
  - Creates, updates, or deletes entities in ManageEngine ServiceDesk Plus Cloud.
  - When C(state=present) (default), automatically infers create vs update based on the presence of C(parent_id).
  - When C(state=absent), deletes the record identified by C(parent_id).
  - Supports idempotency, check mode, and diff mode.
extends_documentation_fragment:
  - manageengine.sdp_cloud.sdp
  - manageengine.sdp_cloud.auth
options:
  state:
    description:
      - The desired state of the record.
      - C(present) ensures the record exists (create or update).
      - C(absent) ensures the record is deleted.
    type: str
    default: present
    choices: [present, absent]
  payload:
    description:
      - The input data for the API request.
      - For create operations, this should contain the fields for the new record.
      - For update operations, this should contain only the fields to be modified.
      - Not used when C(state=absent).
    type: dict
'''

EXAMPLES = r'''
- name: Create a Request
  manageengine.sdp_cloud.write_record:
    domain: "sdpondemand.manageengine.com"
    parent_module_name: "request"
    state: present
    client_id: "your_client_id"
    client_secret: "your_client_secret"
    refresh_token: "your_refresh_token"
    dc: "US"
    portal_name: "ithelpdesk"
    payload:
      subject: "New Request from Ansible"
      description: "Created via sdp_api_write module"
      requester: "requester@example.com"

- name: Update a Problem
  manageengine.sdp_cloud.write_record:
    domain: "sdpondemand.manageengine.com"
    parent_module_name: "problem"
    parent_id: "100"
    state: present
    client_id: "your_client_id"
    client_secret: "your_client_secret"
    refresh_token: "your_refresh_token"
    dc: "US"
    portal_name: "ithelpdesk"
    payload:
      title: "Updated Title"

- name: Delete a Request
  manageengine.sdp_cloud.write_record:
    domain: "sdpondemand.manageengine.com"
    parent_module_name: "request"
    parent_id: "100"
    state: absent
    client_id: "your_client_id"
    client_secret: "your_client_secret"
    refresh_token: "your_refresh_token"
    dc: "US"
    portal_name: "ithelpdesk"
'''

RETURN = r'''
response:
  description: The raw response from the SDP Cloud API.
  returned: always
  type: dict
  sample:
    response_status:
      status_code: 2000
      status: "success"
    request:
      id: "234567890123456"
      subject: "Server down in DC-2"
      status:
        name: "Open"
        id: "100000000000001"
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.api_util import (
    SDPClient, common_argument_spec, check_module_config, construct_endpoint,
    AUTH_MUTUALLY_EXCLUSIVE, AUTH_REQUIRED_TOGETHER
)
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.sdp_config import MODULE_CONFIG

# Re-export helpers so existing tests that import from this module continue to work
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.write_helpers import (  # noqa: F401  pylint: disable=unused-import
    resolve_field_metadata, transform_field_value, construct_payload,
    handle_absent, handle_present,
)


def run_module():
    """Main execution entry point for write module."""
    module_args = common_argument_spec()
    module_args.update(dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        payload=dict(type='dict'),
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=AUTH_MUTUALLY_EXCLUSIVE,
        required_together=AUTH_REQUIRED_TOGETHER,
        required_if=[
            ('state', 'absent', ('parent_id',)),
        ],
    )

    # Validation
    check_module_config(module)

    client = SDPClient(module)
    endpoint = construct_endpoint(module)
    parent_module = module.params['parent_module_name']
    entity_config = MODULE_CONFIG[parent_module]
    state = module.params['state']

    if state == 'absent':
        handle_absent(module, client, endpoint, entity_config)
    else:
        handle_present(module, client, endpoint, entity_config)


def main():
    run_module()


if __name__ == '__main__':
    main()
