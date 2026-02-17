# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.sdp_config import MODULE_CONFIG


def construct_list_payload(module):
    """Validate and construct the list_info payload for GET list operations.

    Reads 'parent_module_name' from module.params to look up sortable_fields
    in MODULE_CONFIG. The payload source can be either module.params['payload']
    (for generic read_record) or module.params['list_options'] (for entity-specific
    info modules).

    Returns:
        A dict with {'list_info': {...}} or None if no list payload is needed.
    """
    if module.params.get('parent_id'):
        return None

    payload = module.params.get('list_options') or module.params.get('payload')
    if not payload:
        return None

    parent_module = module.params['parent_module_name']
    module_config = MODULE_CONFIG.get(parent_module)

    allowed_sort_fields = module_config.get('sortable_fields', [])

    validated_payload = {}

    allowed_keys = ['row_count', 'sort_field', 'sort_order', 'get_total_count', 'start_index']

    for key in payload.keys():
        if key not in allowed_keys:
            module.fail_json(msg="Invalid payload key '{0}'. Allowed keys: {1}".format(key, allowed_keys))

    # 1. row_count
    row_count = payload.get('row_count', 10)
    try:
        row_count = int(row_count)
    except ValueError:
        module.fail_json(msg="row_count must be an integer.")

    if not (1 <= row_count <= 100):
        module.fail_json(msg="row_count must be between 1 and 100.")
    validated_payload['row_count'] = row_count

    # 2. sort_field
    sort_field = payload.get('sort_field', 'created_time')

    if allowed_sort_fields and sort_field not in allowed_sort_fields:
        module.fail_json(msg="Invalid sort_field '{0}'. Allowed fields: {1}".format(sort_field, allowed_sort_fields))

    validated_payload['sort_field'] = sort_field

    # 3. sort_order
    sort_order = payload.get('sort_order', 'asc')
    if sort_order not in ['asc', 'desc']:
        module.fail_json(msg="Invalid sort_order '{0}'. Allowed values: ['asc', 'desc']".format(sort_order))
    validated_payload['sort_order'] = sort_order

    # 4. get_total_count
    get_total_count = payload.get('get_total_count', False)
    if isinstance(get_total_count, str):
        if get_total_count.lower() == 'true':
            get_total_count = True
        elif get_total_count.lower() == 'false':
            get_total_count = False
        else:
            module.fail_json(msg="get_total_count must be a boolean.")
    elif not isinstance(get_total_count, bool):
        module.fail_json(msg="get_total_count must be a boolean.")

    validated_payload['get_total_count'] = get_total_count

    # 5. start_index (pass through if provided)
    start_index = payload.get('start_index')
    if start_index is not None:
        try:
            validated_payload['start_index'] = int(start_index)
        except (ValueError, TypeError):
            module.fail_json(msg="start_index must be an integer.")

    return {"list_info": validated_payload}
