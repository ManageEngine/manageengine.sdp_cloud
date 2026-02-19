# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest

from tests.unit.conftest import create_mock_module
from plugins.module_utils.sdp_config import MODULE_CONFIG
from plugins.module_utils.write_helpers import handle_present


PROBLEM_CONFIG = MODULE_CONFIG['problem']


# ---------------------------------------------------------------------------
# Title validation on create
# ---------------------------------------------------------------------------
class TestProblemTitleValidation:
    def test_create_requires_title(self):
        """Creating a problem without title in payload should fail."""
        module = create_mock_module({
            'parent_module_name': 'problem',
            'parent_id': None,
            'payload': {'description': 'No title provided'},
            'state': 'present',
        })
        with pytest.raises(SystemExit):
            handle_present(module, None, 'problems', PROBLEM_CONFIG)
        module.fail_json.assert_called_once()
        assert 'title' in module.fail_json.call_args[1]['msg'].lower()

    def test_create_requires_title_empty_payload(self):
        """Creating with empty payload should fail."""
        module = create_mock_module({
            'parent_module_name': 'problem',
            'parent_id': None,
            'payload': None,
            'state': 'present',
        })
        with pytest.raises(SystemExit):
            handle_present(module, None, 'problems', PROBLEM_CONFIG)
        module.fail_json.assert_called_once()

    def test_create_with_title_in_payload(self):
        """Title provided inside payload dict should pass validation."""
        module = create_mock_module({
            'parent_module_name': 'problem',
            'parent_id': None,
            'payload': {'title': 'Test Title', 'priority': 'High'},
            'state': 'present',
        })
        payload = module.params.get('payload') or {}
        assert payload.get('title') == 'Test Title'
        assert payload.get('priority') == 'High'

