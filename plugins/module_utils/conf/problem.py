# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

PROBLEM_CONFIG = {
    'endpoint': 'problems',
    'id_param': 'problem_id',
    'mandatory_field': 'title',
    'sortable_fields': [
        'reported_time', 'due_by_time', 'closed_time', 'created_time',
        'id', 'title', 'priority', 'status',
    ],
    'supported_system_field_meta': {
        'title': {'type': 'string'},
        'description': {'type': 'string'},
        'impact_details': {'type': 'string'},
        'reported_time': {'type': 'datetime'},
        'due_by_time': {'type': 'datetime'},
        'closed_time': {'type': 'datetime'},
        'reported_by': {'type': 'user'},
        'technician': {'type': 'user'},
        'requester': {'type': 'user'},
        'category': {'type': 'lookup'},
        'impact': {'type': 'lookup'},
        'priority': {'type': 'lookup'},
        'subcategory': {'type': 'lookup'},
        'item': {'type': 'lookup'},
        'urgency': {'type': 'lookup'},
        'site': {'type': 'lookup'},
        'group': {'type': 'lookup'},
        'status': {'type': 'lookup'},
        'template': {'type': 'lookup'},
        'impact_details_description': {'type': 'string', 'group_name': 'impact_details'},
        'root_cause_description': {'type': 'string', 'group_name': 'root_cause'},
        'symptoms_description': {'type': 'string', 'group_name': 'symptoms'},
        'known_error_comments': {'type': 'string', 'group_name': 'known_error_details'},
        'is_known_error': {'type': 'bool', 'group_name': 'known_error_details'},
        'close_details_comments': {'type': 'string', 'group_name': 'close_details'},
        'closure_code': {'type': 'lookup', 'group_name': 'close_details'},
        'resolution_details_description': {'type': 'string', 'group_name': 'resolution_details'},
        'workaround_details_description': {'type': 'string', 'group_name': 'workaround_details'},
    },
}
