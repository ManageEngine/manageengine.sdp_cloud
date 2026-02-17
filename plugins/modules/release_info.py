# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: release_info
author:
  - Harish Kumar (@harishkumar-k-7052)
short_description: Retrieve release records from ManageEngine ServiceDesk Plus Cloud
description:
  - Fetches release data from ManageEngine ServiceDesk Plus Cloud via the V3 API.
  - If C(release_id) is provided, retrieves a single release by ID.
  - If C(release_id) is omitted, retrieves a list of releases with optional pagination and sorting.
  - This is a read-only module; it never modifies data.
  - See U(https://www.manageengine.com/products/service-desk/sdpod-v3-api/releases/release.html) for full API details.
extends_documentation_fragment:
  - manageengine.sdp_cloud.sdp_base
  - manageengine.sdp_cloud.auth
options:
  release_id:
    description:
      - The ID of a specific release to retrieve.
      - When provided, performs a C(GET /api/v3/releases/{id}) call and returns the single release.
      - When omitted, performs a list operation.
    type: str
  list_options:
    description:
      - Pagination and sorting options for list operations.
      - Ignored when C(release_id) is provided.
    type: dict
    suboptions:
      row_count:
        description: Number of records to return per page (1-100).
        type: int
        default: 10
      start_index:
        description: The starting index for pagination.
        type: int
      sort_field:
        description: The field to sort results by.
        type: str
        default: created_time
      sort_order:
        description: Sort direction.
        type: str
        default: asc
        choices: [asc, desc]
      get_total_count:
        description: Whether to include the total count of matching records.
        type: bool
        default: false
'''

EXAMPLES = r'''
- name: Get a single release by ID
  manageengine.sdp_cloud.release_info:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    release_id: "123456"
  register: single_release

- name: List releases with pagination
  manageengine.sdp_cloud.release_info:
    domain: "sdpondemand.manageengine.com"
    auth_token: "{{ auth_token }}"
    dc: "US"
    portal_name: "ithelpdesk"
    list_options:
      row_count: 10
      sort_field: "created_time"
      sort_order: "desc"
  register: release_list
'''

RETURN = r'''
response:
  description: The raw response from the SDP Cloud API.
  returned: always
  type: dict
release:
  description: The single release record (when release_id is provided).
  returned: when release_id is provided
  type: dict
releases:
  description: List of release records (when listing).
  returned: when release_id is omitted
  type: list
  elements: dict
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.api_util import (
    SDPClient, base_argument_spec, construct_endpoint,
    AUTH_MUTUALLY_EXCLUSIVE, AUTH_REQUIRED_TOGETHER
)
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.sdp_config import MODULE_CONFIG
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.read_helpers import construct_list_payload

ENTITY = 'release'


def run_module():
    config = MODULE_CONFIG[ENTITY]
    module_args = base_argument_spec()
    module_args.update(dict(
        release_id=dict(type='str'),
        list_options=dict(type='dict'),
    ))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=AUTH_MUTUALLY_EXCLUSIVE,
        required_together=AUTH_REQUIRED_TOGETHER
    )

    module.params['parent_module_name'] = ENTITY
    module.params['parent_id'] = module.params.get('release_id')

    client = SDPClient(module)
    endpoint = construct_endpoint(module)
    data = construct_list_payload(module)

    response = client.request(endpoint=endpoint, method='GET', data=data)

    result = dict(changed=False, response=response, payload=data)
    if module.params.get('release_id'):
        result[ENTITY] = response.get(ENTITY, {})
    else:
        result[config['endpoint']] = response.get(config['endpoint'], [])

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
