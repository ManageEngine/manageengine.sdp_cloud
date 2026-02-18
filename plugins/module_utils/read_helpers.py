# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.sdp_config import MODULE_CONFIG


def list_info_argument_spec():
    """Return the argument spec for list/pagination options.

    Used by *_info.py modules and read_record.py to define top-level params.
    """
    return dict(
        row_count=dict(type='int', default=10),
        start_index=dict(type='int'),
        sort_field=dict(type='str', default='created_time'),
        sort_order=dict(type='str', default='desc', choices=['asc', 'desc']),
        get_total_count=dict(type='bool', default=False),
    )


def construct_list_payload(module):
    """Validate and construct the list_info payload for GET list operations.

    Reads pagination/sorting params directly from module.params.

    Returns:
        A dict with {'list_info': {...}} or None if fetching by ID.
    """
    if module.params.get('parent_id'):
        return None

    parent_module = module.params['parent_module_name']
    module_config = MODULE_CONFIG.get(parent_module)
    allowed_sort_fields = module_config.get('sortable_fields', [])

    row_count = module.params.get('row_count', 10)
    sort_field = module.params.get('sort_field', 'created_time')
    sort_order = module.params.get('sort_order', 'desc')
    get_total_count = module.params.get('get_total_count', False)
    start_index = module.params.get('start_index')

    if not (1 <= row_count <= 100):
        module.fail_json(msg="row_count must be between 1 and 100.")

    if allowed_sort_fields and sort_field not in allowed_sort_fields:
        module.fail_json(msg="Invalid sort_field '{0}'. Allowed fields: {1}".format(sort_field, allowed_sort_fields))

    validated_payload = {
        'row_count': row_count,
        'sort_field': sort_field,
        'sort_order': sort_order,
        'get_total_count': get_total_count,
    }

    if start_index is not None:
        validated_payload['start_index'] = start_index

    return {"list_info": validated_payload}
