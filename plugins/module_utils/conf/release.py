# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

RELEASE_CONFIG = {
    'endpoint': 'releases',
    'id_param': 'release_id',
    'mandatory_field': 'title',
    'sortable_fields': [
        'created_time', 'completed_time', 'scheduled_start_time',
        'scheduled_end_time', 'id', 'title', 'priority', 'status', 'stage',
    ],
    'supported_system_field_meta': {
        'title': {'type': 'string'},
        'description': {'type': 'string'},
        'scheduled_start_time': {'type': 'datetime'},
        'scheduled_end_time': {'type': 'datetime'},
        'created_time': {'type': 'datetime'},
        'completed_time': {'type': 'datetime'},
        'next_review_on': {'type': 'datetime'},
        'template': {'type': 'lookup'},
        'stage': {'type': 'lookup'},
        'status': {'type': 'lookup'},
        'workflow': {'type': 'lookup'},
        'release_requester': {'type': 'user'},
        'release_engineer': {'type': 'user'},
        'release_manager': {'type': 'user'},
        'reason_for_release': {'type': 'lookup'},
        'impact': {'type': 'lookup'},
        'priority': {'type': 'lookup'},
        'category': {'type': 'lookup'},
        'subcategory': {'type': 'lookup'},
        'item': {'type': 'lookup'},
        'release_type': {'type': 'lookup'},
        'urgency': {'type': 'lookup'},
        'site': {'type': 'lookup'},
        'group': {'type': 'lookup'},
        'risk': {'type': 'lookup'},
        # Grouped fields
        'roll_out_plan_description': {'type': 'string', 'group_name': 'roll_out_plan'},
        'back_out_plan_description': {'type': 'string', 'group_name': 'back_out_plan'},
    },
}
