# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.sdp_config import MODULE_CONFIG
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.udf_utils import is_udf_field, get_udf_field_type


def _is_valid_email(value):
    """Return True if value looks like an email (local@domain.tld). Rejects e.g. 'hell@hi'."""
    if not isinstance(value, str) or not value:
        return False
    parts = value.split('@')
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    if '.' not in domain:
        return False
    return True


def resolve_field_metadata(module, client, module_config, field_name):
    """
    Determine if a field is System or UDF and return its metadata.
    Returns: (field_type, category, group_name)
    category: 'system' or 'udf'
    """
    system_fields = module_config.get('supported_system_field_meta', {})

    if field_name in system_fields:
        f_config = system_fields[field_name]
        return f_config.get('type'), 'system', f_config.get('group_name')

    if is_udf_field(field_name):
        if not client:
            module.warn("UDF field '{0}' found but no client available. Treating as string.".format(field_name))
            return 'string', 'udf', None

        parent_module = module.params['parent_module_name']
        udf_type = get_udf_field_type(module, client, parent_module, field_name)
        return udf_type, 'udf', None

    return None, None, None


def transform_field_value(module, field_name, value, ftype):
    """
    Transform the value based on the resolved field type.
    """
    if ftype == 'string':
        return value

    elif ftype == 'num':
        if isinstance(value, (int, float)):
            return value
        if isinstance(value, str):
            try:
                return int(value)
            except ValueError:
                try:
                    return float(value)
                except ValueError:
                    pass
        module.fail_json(
            msg="Numeric field '{0}' requires an integer or decimal value. Got: {1}".format(field_name, value)
        )

    elif ftype == 'bool':
        if isinstance(value, str):
            return value.lower() == 'true'
        return bool(value)

    elif ftype == 'datetime':
        if not isinstance(value, (int, float)):
            module.fail_json(msg="Invalid datetime format for field '{0}'. value must be a timestamp (int/float).".format(field_name))
        return {'value': value}

    elif ftype == 'lookup':
        return {'name': value}

    elif ftype == 'user':
        if not _is_valid_email(value):
            module.fail_json(
                msg="User field '{0}' accepts only a valid email address (e.g. user@example.com). Got: {1}".format(field_name, value)
            )
        return {'email_id': value}

    return value


def construct_payload(module, client=None):
    """
    Validate and construct the payload using a unified single-pass loop.
    """
    payload = module.params['payload']
    if not payload:
        return None

    parent_module = module.params['parent_module_name']

    module_config = MODULE_CONFIG.get(parent_module)

    root_key = parent_module

    constructed_data = {'udf_fields': {}}

    for key, value in payload.items():
        ftype, category, group_name = resolve_field_metadata(module, client, module_config, key)

        if not category:
            allowed_fields = list(module_config.get('supported_system_field_meta', {}).keys())
            module.fail_json(msg="Invalid field '{0}'. Allowed system fields: {1}".format(key, allowed_fields))

        final_value = transform_field_value(module, key, value, ftype)

        if category == 'system':
            if group_name:
                if group_name not in constructed_data:
                    constructed_data[group_name] = {}
                constructed_data[group_name][key] = final_value
            else:
                constructed_data[key] = final_value

        elif category == 'udf':
            constructed_data['udf_fields'][key] = final_value

    if not constructed_data['udf_fields']:
        del constructed_data['udf_fields']

    return {root_key: constructed_data}


def handle_absent(module, client, endpoint, entity_config):
    """Handle state=absent (delete) logic for any entity.

    Args:
        module: AnsibleModule instance.
        client: SDPClient instance.
        endpoint: Constructed API endpoint string.
        entity_config: Dict from MODULE_CONFIG for this entity, containing
                       'id_param' for error messages and other entity metadata.
    """
    from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.api_util import get_current_record

    parent_module = module.params['parent_module_name']
    parent_id = module.params.get('parent_id')

    current_record = get_current_record(client, module)

    if not current_record:
        module.exit_json(changed=False, msg="Record does not exist, nothing to delete.")

    if module.check_mode:
        result = dict(
            changed=True,
            msg="Would delete {0} record with id {1}.".format(parent_module, parent_id),
        )
        if module._diff:
            result['diff'] = {'before': current_record, 'after': {}}
        module.exit_json(**result)

    response = client.request(endpoint=endpoint, method='DELETE')

    result = dict(changed=True, response=response)
    if module._diff:
        result['diff'] = {'before': current_record, 'after': {}}
    module.exit_json(**result)


def handle_present(module, client, endpoint, entity_config):
    """Handle state=present (create/update) logic for any entity.

    Handles mandatory field merging, validation, idempotency, check mode,
    diff mode, and convenience return keys.

    Args:
        module: AnsibleModule instance.
        client: SDPClient instance.
        endpoint: Constructed API endpoint string.
        entity_config: Dict from MODULE_CONFIG for this entity, containing
                       'id_param', 'mandatory_field', and other entity metadata.
    """
    from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.api_util import (
        get_current_record, has_differences
    )

    parent_module = module.params['parent_module_name']
    parent_id = module.params.get('parent_id')
    id_param = entity_config.get('id_param', 'parent_id')
    mandatory_field = entity_config.get('mandatory_field')

    method = 'PUT' if parent_id else 'POST'

    # Merge top-level mandatory field into payload (entity modules expose it as a top-level option)
    if mandatory_field and module.params.get(mandatory_field):
        if module.params.get('payload') is None:
            module.params['payload'] = {}
        module.params['payload'][mandatory_field] = module.params[mandatory_field]

    # Enforce mandatory field on create
    if method == 'POST' and mandatory_field:
        payload = module.params.get('payload') or {}
        if not payload.get(mandatory_field):
            module.fail_json(msg="'{0}' is required when creating a new {1}.".format(
                mandatory_field, parent_module))

    data = construct_payload(module, client)

    # Idempotency for updates
    current_record = None
    if method == 'PUT' and data:
        current_record = get_current_record(client, module)

        if current_record and not has_differences(data, current_record, parent_module):
            result = dict(
                changed=False,
                response={parent_module: current_record},
            )
            result[parent_module] = current_record
            result[id_param] = parent_id
            module.exit_json(**result)

    if module.check_mode:
        result = dict(
            changed=True,
            msg="Would {0} a {1} record.".format('update' if method == 'PUT' else 'create', parent_module),
        )
        if module._diff and current_record:
            result['diff'] = {'before': current_record, 'after': data.get(parent_module, {})}
        module.exit_json(**result)

    response = client.request(endpoint=endpoint, method=method, data=data)

    entity_record = response.get(parent_module, {})
    result = dict(
        changed=True,
        response=response,
    )
    result[parent_module] = entity_record
    result[id_param] = entity_record.get('id')

    if module._diff:
        result['diff'] = {
            'before': current_record or {},
            'after': entity_record,
        }

    module.exit_json(**result)
