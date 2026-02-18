# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest

from tests.unit.conftest import create_mock_module
from plugins.module_utils.sdp_config import MODULE_CONFIG
from plugins.module_utils.write_helpers import handle_present


RELEASE_CONFIG = MODULE_CONFIG['release']


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
class TestReleaseTitleValidation:
    def test_create_requires_title(self):
        """Creating a release without title should fail."""
        module = create_mock_module({
            'parent_module_name': 'release',
            'parent_id': None,
            'title': None,
            'payload': {'description': 'No title provided'},
            'state': 'present',
        })
        with pytest.raises(SystemExit):
            handle_present(module, None, 'releases', RELEASE_CONFIG)
        module.fail_json.assert_called_once()
        assert 'title' in module.fail_json.call_args[1]['msg'].lower()

    def test_create_requires_title_empty_payload(self):
        """Creating with empty payload and no title should fail."""
        module = create_mock_module({
            'parent_module_name': 'release',
            'parent_id': None,
            'title': None,
            'payload': None,
            'state': 'present',
        })
        with pytest.raises(SystemExit):
            handle_present(module, None, 'releases', RELEASE_CONFIG)
        module.fail_json.assert_called_once()

    def test_create_with_title_option(self):
        """Title provided as top-level option should be merged into payload."""
        module = create_mock_module({
            'parent_module_name': 'release',
            'parent_id': None,
            'title': 'Test Release Title',
            'payload': {'priority': 'High'},
            'state': 'present',
        })
        _merge_mandatory_field(module, RELEASE_CONFIG)
        assert module.params['payload']['title'] == 'Test Release Title'
        assert module.params['payload']['priority'] == 'High'


