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
class TestRequestInfoListPayload:
    def test_returns_none_when_request_id_present(self):
        """When fetching by ID, no list payload is needed."""
        module = create_mock_module({
            'parent_id': '100',
            'parent_module_name': 'request',
            'list_options': {'row_count': 10},
            'payload': None,
        })
        assert construct_list_payload(module) is None

    def test_returns_none_when_no_list_options(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'list_options': None,
            'payload': None,
        })
        assert construct_list_payload(module) is None

    def test_default_values(self):
        """When only row_count is specified, other fields get defaults."""
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
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
            'parent_module_name': 'request',
            'list_options': {
                'row_count': 50,
                'sort_field': 'subject',
                'sort_order': 'desc',
                'get_total_count': True,
                'start_index': 5,
            },
            'payload': None,
        })
        result = construct_list_payload(module)
        li = result['list_info']
        assert li['row_count'] == 50
        assert li['sort_field'] == 'subject'
        assert li['sort_order'] == 'desc'
        assert li['get_total_count'] is True
        assert li['start_index'] == 5

    def test_invalid_key_fails(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'list_options': {'invalid_key': 'value'},
            'payload': None,
        })
        with pytest.raises(SystemExit):
            construct_list_payload(module)
        module.fail_json.assert_called_once()

    def test_row_count_out_of_range(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'list_options': {'row_count': 200},
            'payload': None,
        })
        with pytest.raises(SystemExit):
            construct_list_payload(module)

    def test_invalid_sort_order(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'list_options': {'sort_order': 'random'},
            'payload': None,
        })
        with pytest.raises(SystemExit):
            construct_list_payload(module)

    def test_invalid_sort_field(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'list_options': {'sort_field': 'nonexistent_field'},
            'payload': None,
        })
        with pytest.raises(SystemExit):
            construct_list_payload(module)

    def test_get_total_count_string_true(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'list_options': {'get_total_count': 'true'},
            'payload': None,
        })
        result = construct_list_payload(module)
        assert result['list_info']['get_total_count'] is True

    def test_get_total_count_invalid_string(self):
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'list_options': {'get_total_count': 'maybe'},
            'payload': None,
        })
        with pytest.raises(SystemExit):
            construct_list_payload(module)

    def test_empty_list_options_returns_none(self):
        """Empty dict {} is falsy — returns None."""
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'list_options': {},
            'payload': None,
        })
        assert construct_list_payload(module) is None


# ---------------------------------------------------------------------------
# construct_list_payload — backward compat via payload key (generic read_record path)
# ---------------------------------------------------------------------------
class TestRequestInfoPayloadCompat:
    def test_payload_key_works_for_generic_module(self):
        """The generic read_record uses 'payload' key — should still work."""
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'payload': {'row_count': 5},
            'list_options': None,
        })
        result = construct_list_payload(module)
        assert result['list_info']['row_count'] == 5

    def test_list_options_preferred_over_payload(self):
        """When both list_options and payload exist, list_options takes precedence."""
        module = create_mock_module({
            'parent_id': None,
            'parent_module_name': 'request',
            'list_options': {'row_count': 20},
            'payload': {'row_count': 5},
        })
        result = construct_list_payload(module)
        assert result['list_info']['row_count'] == 20
