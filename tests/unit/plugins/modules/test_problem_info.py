# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest

from tests.unit.conftest import create_mock_module
from plugins.module_utils.read_helpers import construct_list_payload


# ---------------------------------------------------------------------------
# construct_list_payload — via list_options (entity-specific path)
# ---------------------------------------------------------------------------
class TestProblemInfoListPayload:
    def test_returns_none_when_problem_id_present(self):
        """When fetching by ID, no list payload is needed."""
        module = create_mock_module({
            'parent_id': '100',
            'parent_module_name': 'problem',
            'list_options': {'row_count': 10},
            'payload': None,
        })
        assert construct_list_payload(module) is None

    def test_returns_none_when_no_list_options(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'problem',
            'list_options': None,
            'payload': None,
        })
        assert construct_list_payload(module) is None

    def test_default_values(self):
        """When only row_count is specified, other fields get defaults."""
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'problem',
            'list_options': {'row_count': 10},
            'payload': None,
        })
        result = construct_list_payload(module)
        assert result == {
            'list_info': {
                'row_count': 10,
                'sort_field': 'created_time',
                'sort_order': 'asc',
                'get_total_count': False,
            }
        }

    def test_custom_values(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'problem',
            'list_options': {
                'row_count': 50,
                'sort_field': 'title',
                'sort_order': 'desc',
                'get_total_count': True,
                'start_index': 5,
            },
            'payload': None,
        })
        result = construct_list_payload(module)
        li = result['list_info']
        assert li['row_count'] == 50
        assert li['sort_field'] == 'title'
        assert li['sort_order'] == 'desc'
        assert li['get_total_count'] is True
        assert li['start_index'] == 5

    def test_invalid_sort_field(self):
        """Invalid sort_field not in problem's sortable_fields should fail."""
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'problem',
            'list_options': {'sort_field': 'nonexistent_field'},
            'payload': None,
        })
        with pytest.raises(SystemExit):
            construct_list_payload(module)
        module.fail_json.assert_called_once()
