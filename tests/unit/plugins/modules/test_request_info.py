# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest

from tests.unit.conftest import create_mock_module
from plugins.module_utils.read_helpers import construct_list_payload


# ---------------------------------------------------------------------------
# construct_list_payload — top-level params (entity-specific and generic path)
# ---------------------------------------------------------------------------
class TestRequestInfoListPayload:
    def test_returns_none_when_request_id_present(self):
        """When fetching by ID, no list payload is needed."""
        module = create_mock_module({
            'parent_id': '100',
            'parent_module_name': 'request',
            'row_count': 10,
            'start_index': None,
            'sort_field': 'created_time',
            'sort_order': 'asc',
            'get_total_count': False,
        })
        assert construct_list_payload(module) is None

    def test_default_values(self):
        """When defaults are used, the payload reflects them."""
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'row_count': 10,
            'start_index': None,
            'sort_field': 'created_time',
            'sort_order': 'asc',
            'get_total_count': False,
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
            'parent_module_name': 'request',
            'row_count': 50,
            'start_index': 5,
            'sort_field': 'subject',
            'sort_order': 'desc',
            'get_total_count': True,
        })
        result = construct_list_payload(module)
        li = result['list_info']
        assert li['row_count'] == 50
        assert li['sort_field'] == 'subject'
        assert li['sort_order'] == 'desc'
        assert li['get_total_count'] is True
        assert li['start_index'] == 5

    def test_row_count_out_of_range(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'row_count': 200,
            'start_index': None,
            'sort_field': 'created_time',
            'sort_order': 'asc',
            'get_total_count': False,
        })
        with pytest.raises(SystemExit):
            construct_list_payload(module)

    def test_invalid_sort_field(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'row_count': 10,
            'start_index': None,
            'sort_field': 'nonexistent_field',
            'sort_order': 'asc',
            'get_total_count': False,
        })
        with pytest.raises(SystemExit):
            construct_list_payload(module)

    def test_start_index_included_when_set(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'row_count': 10,
            'start_index': 20,
            'sort_field': 'created_time',
            'sort_order': 'asc',
            'get_total_count': False,
        })
        result = construct_list_payload(module)
        assert result['list_info']['start_index'] == 20

    def test_start_index_omitted_when_none(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'row_count': 10,
            'start_index': None,
            'sort_field': 'created_time',
            'sort_order': 'asc',
            'get_total_count': False,
        })
        result = construct_list_payload(module)
        assert 'start_index' not in result['list_info']
