# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

CHANGE_CONFIG = {
    'endpoint': 'changes',
    'id_param': 'change_id',
    'mandatory_field': 'title',
    'sortable_fields': [
        'created_time', 'completed_time', 'scheduled_start_time',
        'scheduled_end_time', 'id', 'title', 'priority', 'status', 'stage',
    ],
    'supported_system_field_meta': {
        'title': {'type': 'string'},
        'description': {'type': 'string'},
        'comment': {'type': 'string'},
        'retrospective': {'type': 'bool'},
        'created_time': {'type': 'datetime'},
        'completed_time': {'type': 'datetime'},
        'scheduled_start_time': {'type': 'datetime'},
        'scheduled_end_time': {'type': 'datetime'},
        'stage': {'type': 'lookup'},
        'status': {'type': 'lookup'},
        'template': {'type': 'lookup'},
        'change_requester': {'type': 'user'},
        'change_manager': {'type': 'user'},
        'change_owner': {'type': 'user'},
        'reason_for_change': {'type': 'lookup'},
        'risk': {'type': 'lookup'},
        'impact': {'type': 'lookup'},
        'priority': {'type': 'lookup'},
        'category': {'type': 'lookup'},
        'subcategory': {'type': 'lookup'},
        'item': {'type': 'lookup'},
        'urgency': {'type': 'lookup'},
        'change_type': {'type': 'lookup'},
        'site': {'type': 'lookup'},
        'group': {'type': 'lookup'},
        'workflow': {'type': 'lookup'},
        # Grouped fields
        'roll_out_plan_description': {'type': 'string', 'group_name': 'roll_out_plan'},
        'back_out_plan_description': {'type': 'string', 'group_name': 'back_out_plan'},
    },
}
