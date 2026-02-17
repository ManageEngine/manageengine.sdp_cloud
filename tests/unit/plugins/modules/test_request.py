# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest

from tests.unit.conftest import create_mock_module
from plugins.module_utils.sdp_config import MODULE_CONFIG
from plugins.module_utils.write_helpers import handle_present, handle_absent


REQUEST_CONFIG = MODULE_CONFIG['request']


# ---------------------------------------------------------------------------
# Subject validation on create
# ---------------------------------------------------------------------------
class TestRequestSubjectValidation:
    def test_create_requires_subject(self):
        """Creating a request without subject should fail."""
        module = create_mock_module({
            'parent_module_name': 'request',
            'parent_id': None,
            'subject': None,
            'payload': {'description': 'No subject provided'},
            'state': 'present',
        })
        with pytest.raises(SystemExit):
            handle_present(module, None, 'requests', REQUEST_CONFIG)
        module.fail_json.assert_called_once()
        assert 'subject' in module.fail_json.call_args[1]['msg'].lower()

    def test_create_requires_subject_empty_payload(self):
        """Creating with empty payload and no subject should fail."""
        module = create_mock_module({
            'parent_module_name': 'request',
            'parent_id': None,
            'subject': None,
            'payload': None,
            'state': 'present',
        })
        with pytest.raises(SystemExit):
            handle_present(module, None, 'requests', REQUEST_CONFIG)
        module.fail_json.assert_called_once()

    def test_create_with_subject_option(self):
        """Subject provided as top-level option should be merged into payload."""
        module = create_mock_module({
            'parent_module_name': 'request',
            'parent_id': None,
            'subject': 'Test Subject',
            'payload': {'priority': 'High'},
            'state': 'present',
        })
        # Simulate what handle_present does for subject merge
        _merge_mandatory_field(module, REQUEST_CONFIG)
        assert module.params['payload']['subject'] == 'Test Subject'
        assert module.params['payload']['priority'] == 'High'

    def test_create_with_subject_in_payload(self):
        """Subject can also be provided inside payload dict."""
        module = create_mock_module({
            'parent_module_name': 'request',
            'parent_id': None,
            'subject': None,
            'payload': {'subject': 'From Payload', 'priority': 'Low'},
            'state': 'present',
        })
        payload = module.params.get('payload') or {}
        assert payload.get('subject') == 'From Payload'

    def test_subject_option_overrides_payload(self):
        """Top-level subject option should override subject in payload."""
        module = create_mock_module({
            'parent_module_name': 'request',
            'parent_id': None,
            'subject': 'Top Level Subject',
            'payload': {'subject': 'Payload Subject'},
            'state': 'present',
        })
        _merge_mandatory_field(module, REQUEST_CONFIG)
        assert module.params['payload']['subject'] == 'Top Level Subject'


def _merge_mandatory_field(module, config):
    """Simulate the mandatory field merge logic from handle_present."""
    field = config.get('mandatory_field')
    if field and module.params.get(field):
        if module.params.get('payload') is None:
            module.params['payload'] = {}
        module.params['payload'][field] = module.params[field]


# ---------------------------------------------------------------------------
# Payload construction (via write_helpers)
# ---------------------------------------------------------------------------
class TestRequestConstructPayload:
    def test_simple_create_payload(self):
        from plugins.module_utils.write_helpers import construct_payload
        module = create_mock_module({
            'parent_module_name': 'request',
            'parent_id': None,
            'payload': {'subject': 'Test', 'description': 'A test request'},
        })
        result = construct_payload(module)
        assert result == {
            'request': {
                'subject': 'Test',
                'description': 'A test request',
            }
        }

    def test_payload_with_lookup_and_user(self):
        from plugins.module_utils.write_helpers import construct_payload
        module = create_mock_module({
            'parent_module_name': 'request',
            'parent_id': None,
            'payload': {
                'subject': 'Test',
                'priority': 'High',
                'requester': 'admin@example.com',
            },
        })
        result = construct_payload(module)
        assert result['request']['subject'] == 'Test'
        assert result['request']['priority'] == {'name': 'High'}
        assert result['request']['requester'] == {'email_id': 'admin@example.com'}

    def test_payload_with_datetime(self):
        from plugins.module_utils.write_helpers import construct_payload
        module = create_mock_module({
            'parent_module_name': 'request',
            'parent_id': None,
            'payload': {
                'subject': 'Test',
                'due_by_time': 1700000000,
            },
        })
        result = construct_payload(module)
        assert result['request']['due_by_time'] == {'value': 1700000000}

    def test_payload_none_returns_none(self):
        from plugins.module_utils.write_helpers import construct_payload
        module = create_mock_module({
            'parent_module_name': 'request',
            'parent_id': None,
            'payload': None,
        })
        assert construct_payload(module) is None

    def test_invalid_field_fails(self):
        from plugins.module_utils.write_helpers import construct_payload
        module = create_mock_module({
            'parent_module_name': 'request',
            'parent_id': None,
            'payload': {'invalid_field': 'value'},
        })
        with pytest.raises(SystemExit):
            construct_payload(module)
        module.fail_json.assert_called_once()


# ---------------------------------------------------------------------------
# Delete validation
# ---------------------------------------------------------------------------
class TestRequestDeleteValidation:
    def test_delete_requires_request_id(self):
        """Deleting without request_id should fail."""
        module = create_mock_module({
            'parent_module_name': 'request',
            'parent_id': None,
            'state': 'absent',
        })
        with pytest.raises(SystemExit):
            handle_absent(module, None, 'requests', REQUEST_CONFIG)
        module.fail_json.assert_called_once()
        assert 'request_id' in module.fail_json.call_args[1]['msg']
