# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: request_info
author:
  - Harish Kumar (@harishkumar-k-7052)
short_description: Retrieve request records from ManageEngine ServiceDesk Plus Cloud
description:
  - Fetches request data from ManageEngine ServiceDesk Plus Cloud via the V3 API.
  - If C(request_id) is provided, retrieves a single request by ID.
  - If C(request_id) is omitted, retrieves a list of requests with optional pagination and sorting.
  - This is a read-only module; it never modifies data.
  - See U(https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request.html) for full API details.
extends_documentation_fragment:
  - manageengine.sdp_cloud.sdp_base
  - manageengine.sdp_cloud.auth
options:
  request_id:
    description:
      - The ID of a specific request to retrieve.
      - When provided, performs a C(GET /api/v3/requests/{id}) call and returns the single request.
      - When omitted, performs a list operation.
    type: str
  row_count:
    description:
      - Number of records to return per page (1-100).
      - Ignored when C(request_id) is provided.
    type: int
    default: 10
  start_index:
    description:
      - The starting index for pagination.
      - Ignored when C(request_id) is provided.
    type: int
  sort_field:
    description:
      - The field to sort results by.
      - Ignored when C(request_id) is provided.
    type: str
    default: created_time
  sort_order:
    description:
      - Sort direction.
      - Ignored when C(request_id) is provided.
    type: str
    default: asc
    choices: [asc, desc]
  get_total_count:
    description:
      - Whether to include the total count of matching records.
      - Ignored when C(request_id) is provided.
    type: bool
    default: false
'''

EXAMPLES = r'''
- name: Get a single request by ID
  manageengine.sdp_cloud.request_info:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    request_id: "123456"
  register: single_request

- name: List requests with pagination
  manageengine.sdp_cloud.request_info:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    row_count: 10
    sort_field: "created_time"
    sort_order: "desc"
  register: request_list
'''

RETURN = r'''
response:
  description: The raw response from the SDP Cloud API.
  returned: always
  type: dict
request:
  description: The single request record (when request_id is provided).
  returned: when request_id is provided
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
requests:
  description: List of request records (when listing).
  returned: when request_id is omitted
  type: list
  elements: dict
  sample:
    - id: "234567890123456"
      subject: "Server down in DC-2"
      status:
        name: "Open"
        id: "100000000000001"
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.api_util import (
    SDPClient, base_argument_spec, construct_endpoint,
    AUTH_MUTUALLY_EXCLUSIVE, AUTH_REQUIRED_TOGETHER
)
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.sdp_config import MODULE_CONFIG
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.read_helpers import (
    construct_list_payload, list_info_argument_spec
)

ENTITY = 'request'


def run_module():
    config = MODULE_CONFIG[ENTITY]
    module_args = base_argument_spec()
    module_args.update(list_info_argument_spec())
    module_args.update(dict(
        request_id=dict(type='str'),
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=AUTH_MUTUALLY_EXCLUSIVE,
        required_together=AUTH_REQUIRED_TOGETHER
    )

    module.params['parent_module_name'] = ENTITY
    module.params['parent_id'] = module.params.get('request_id')

    client = SDPClient(module)
    endpoint = construct_endpoint(module)
    data = construct_list_payload(module)

    response = client.request(endpoint=endpoint, method='GET', data=data)

    result = dict(changed=False, response=response)
    if module.params.get('request_id'):
        result[ENTITY] = response.get(ENTITY, {})
    else:
        result[config['endpoint']] = response.get(config['endpoint'], [])

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
