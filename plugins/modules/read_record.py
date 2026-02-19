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
  row_count:
    description:
      - Number of records to return per page (1-100).
      - Ignored when C(parent_id) is provided.
    type: int
    default: 10
  start_index:
    description:
      - The starting index for pagination.
      - Ignored when C(parent_id) is provided.
    type: int
  sort_field:
    description:
      - The field to sort results by.
      - Ignored when C(parent_id) is provided.
    type: str
    default: created_time
  sort_order:
    description:
      - Sort direction.
      - Ignored when C(parent_id) is provided.
    type: str
    default: desc
    choices: [asc, desc]
  get_total_count:
    description:
      - Whether to include the total count of matching records.
      - Ignored when C(parent_id) is provided.
    type: bool
    default: false
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
    row_count: 10
    start_index: 1
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
    requests:
      - id: "234567890123456"
        subject: "Server down in DC-2"
        status:
          name: "Open"
          id: "100000000000001"
    list_info:
      has_more_rows: true
      row_count: 10
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.api_util import (
    SDPClient, common_argument_spec, check_module_config, construct_endpoint,
    AUTH_MUTUALLY_EXCLUSIVE, AUTH_REQUIRED_TOGETHER
)
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.read_helpers import (
    construct_list_payload, list_info_argument_spec,
)

# Re-export for backward compatibility with existing tests
construct_payload = construct_list_payload  # noqa: F841


def run_module():
    """Main execution entry point for read module."""
    module_args = common_argument_spec()
    module_args.update(list_info_argument_spec())

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=AUTH_MUTUALLY_EXCLUSIVE,
        required_together=AUTH_REQUIRED_TOGETHER
    )

    check_module_config(module)

    client = SDPClient(module)
    endpoint = construct_endpoint(module)

    data = construct_list_payload(module)

    response = client.request(
        endpoint=endpoint,
        method='GET',
        data=data
    )

    module.exit_json(changed=False, response=response)


def main():
    run_module()


if __name__ == '__main__':
    main()
