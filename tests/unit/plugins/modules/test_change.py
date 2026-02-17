# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest

from tests.unit.conftest import create_mock_module
from plugins.module_utils.sdp_config import MODULE_CONFIG
from plugins.module_utils.write_helpers import handle_present, handle_absent


CHANGE_CONFIG = MODULE_CONFIG['change']


def _merge_mandatory_field(module, config):
    """Simulate the mandatory field merge logic from handle_present."""
    field = config.get('mandatory_field')
    if field and module.params.get(field):
        if module.params.get('payload') is None:
            module.params['payload'] = {}
        module.params['payload'][field] = module.params[field]


# ---------------------------------------------------------------------------
# Title validation on create
# ---------------------------------------------------------------------------
class TestChangeTitleValidation:
    def test_create_requires_title(self):
        """Creating a change without title should fail."""
        module = create_mock_module({
            'parent_module_name': 'change',
            'parent_id': None,
            'title': None,
            'payload': {'description': 'No title provided'},
            'state': 'present',
        })
        with pytest.raises(SystemExit):
            handle_present(module, None, 'changes', CHANGE_CONFIG)
        module.fail_json.assert_called_once()
        assert 'title' in module.fail_json.call_args[1]['msg'].lower()

    def test_create_requires_title_empty_payload(self):
        """Creating with empty payload and no title should fail."""
        module = create_mock_module({
            'parent_module_name': 'change',
            'parent_id': None,
            'title': None,
            'payload': None,
            'state': 'present',
        })
        with pytest.raises(SystemExit):
            handle_present(module, None, 'changes', CHANGE_CONFIG)
        module.fail_json.assert_called_once()

    def test_create_with_title_option(self):
        """Title provided as top-level option should be merged into payload."""
        module = create_mock_module({
            'parent_module_name': 'change',
            'parent_id': None,
            'title': 'Test Title',
            'payload': {'priority': 'High'},
            'state': 'present',
        })
        _merge_mandatory_field(module, CHANGE_CONFIG)
        assert module.params['payload']['title'] == 'Test Title'
        assert module.params['payload']['priority'] == 'High'


# ---------------------------------------------------------------------------
# Delete validation
# ---------------------------------------------------------------------------
class TestChangeDeleteValidation:
    def test_delete_requires_change_id(self):
        """Deleting without change_id should fail."""
        module = create_mock_module({
            'parent_module_name': 'change',
            'parent_id': None,
            'state': 'absent',
        })
        with pytest.raises(SystemExit):
            handle_absent(module, None, 'changes', CHANGE_CONFIG)
        module.fail_json.assert_called_once()
        assert 'change_id' in module.fail_json.call_args[1]['msg']
