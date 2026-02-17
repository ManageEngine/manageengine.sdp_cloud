# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: read_record
author:
  - Harish Kumar (@harishkumar-k-7052)
short_description: Read API module for ManageEngine ServiceDesk Plus Cloud
description:
  - Performs data retrieval API operations (GET) on ManageEngine ServiceDesk Plus Cloud entities.
  - Supports Requests, Problems, Changes, and Releases.
  - If C(parent_id) is provided, retrieves a single record. Otherwise, retrieves a list of records.
extends_documentation_fragment:
  - manageengine.sdp_cloud.sdp
  - manageengine.sdp_cloud.auth
options:
  payload:
    description:
      - The input data for the API request.
      - Used for list operations to control pagination and sorting.
      - Supported keys are C(row_count) (1-100, default 10), C(sort_field), C(sort_order) (asc/desc), C(get_total_count), and C(start_index).
      - Ignored when C(parent_id) is provided.
    type: dict
'''

EXAMPLES = r'''
- name: Get Request Details
  manageengine.sdp_cloud.read_record:
    domain: "sdpondemand.manageengine.com"
    parent_module_name: "request"
    parent_id: "100"
    client_id: "your_client_id"
    client_secret: "your_client_secret"
    refresh_token: "your_refresh_token"
    dc: "US"
    portal_name: "ithelpdesk"

- name: Get List of Requests
  manageengine.sdp_cloud.read_record:
    domain: "sdpondemand.manageengine.com"
    parent_module_name: "request"
    client_id: "your_client_id"
    client_secret: "your_client_secret"
    refresh_token: "your_refresh_token"
    dc: "US"
    portal_name: "ithelpdesk"
    payload:
      row_count: 10
      start_index: 1
'''

RETURN = r'''
response:
  description: The raw response from the SDP Cloud API.
  returned: always
  type: dict
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.api_util import (
    SDPClient, common_argument_spec, check_module_config, construct_endpoint,
    AUTH_MUTUALLY_EXCLUSIVE, AUTH_REQUIRED_TOGETHER
)

# Re-export so existing tests that import construct_payload from this module continue to work
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.read_helpers import (  # noqa: F401
    construct_list_payload as construct_payload,
)


def run_module():
    """Main execution entry point for read module."""
    module_args = common_argument_spec()
    module_args.update(dict(
        payload=dict(type='dict')
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=AUTH_MUTUALLY_EXCLUSIVE,
        required_together=AUTH_REQUIRED_TOGETHER
    )

    check_module_config(module)

    client = SDPClient(module)
    endpoint = construct_endpoint(module)

    # Construct Payload
    data = construct_payload(module)

    response = client.request(
        endpoint=endpoint,
        method='GET',
        data=data
    )

    module.exit_json(changed=False, response=response, payload=data)


def main():
    run_module()


if __name__ == '__main__':
    main()
