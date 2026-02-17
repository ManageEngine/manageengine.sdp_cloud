# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

REQUEST_CONFIG = {
    'endpoint': 'requests',
    'id_param': 'request_id',
    'mandatory_field': 'subject',
    'sortable_fields': [
        'created_time', 'due_by_time', 'first_response_due_by_time', 'last_updated_time',
        'scheduled_start_time', 'scheduled_end_time', 'subject', 'id', 'priority', 'status',
    ],
    'supported_system_field_meta': {
        'subject': {'type': 'string'},
        'description': {'type': 'string'},
        'impact_details': {'type': 'string'},
        'update_reason': {'type': 'string'},
        'status_change_comments': {'type': 'string'},
        'status': {'type': 'lookup'},
        'template': {'type': 'lookup'},
        'priority': {'type': 'lookup'},
        'urgency': {'type': 'lookup'},
        'impact': {'type': 'lookup'},
        'mode': {'type': 'lookup'},
        'level': {'type': 'lookup'},
        'site': {'type': 'lookup'},
        'group': {'type': 'lookup'},
        'category': {'type': 'lookup'},
        'subcategory': {'type': 'lookup'},
        'item': {'type': 'lookup'},
        'requester': {'type': 'user'},
        'technician': {'type': 'user'},
        'on_behalf_of': {'type': 'user'},
        'editor': {'type': 'user'},
        'due_by_time': {'type': 'datetime'},
        'first_response_due_by_time': {'type': 'datetime'},
        'scheduled_start_time': {'type': 'datetime'},
        'scheduled_end_time': {'type': 'datetime'},
    },
}
