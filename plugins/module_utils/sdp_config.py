# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.conf.request import REQUEST_CONFIG
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.conf.problem import PROBLEM_CONFIG
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.conf.change import CHANGE_CONFIG
from ansible_collections.manageengine.sdp_cloud.plugins.module_utils.conf.release import RELEASE_CONFIG

DC_MAP = {
    'US': 'https://accounts.zoho.com',
    'EU': 'https://accounts.zoho.eu',
    'IN': 'https://accounts.zoho.in',
    'AU': 'https://accounts.zoho.com.au',
    'CN': 'https://accounts.zoho.com.cn',
    'JP': 'https://accounts.zoho.jp',
    'CA': 'https://accounts.zoho.ca',
    'SA': 'https://accounts.zoho.sa',
}

DC_CHOICES = list(DC_MAP.keys())

MODULE_CONFIG = {
    'request': REQUEST_CONFIG,
    'problem': PROBLEM_CONFIG,
    'change': CHANGE_CONFIG,
    'release': RELEASE_CONFIG,
}


# ---------------------------------------------------------------------------
# Security: fail-closed allowlists for user-supplied connection parameters.
#
# The OAuth access token is attached to every request made against the host
# built from the `domain` parameter, so an unvalidated `domain` lets anyone who
# can influence playbook variables (shared role, imported playbook, AWX survey)
# exfiltrate a live token. `domain`, `portal_name` and `parent_id` all feed the
# request URL and are therefore validated before use.
# ---------------------------------------------------------------------------

# Only ServiceDesk Plus Cloud / Zoho-operated hosts may receive the token.
# Leading dots are required so look-alikes such as "evilmanageengine.com" or
# "manageengine.com.attacker.io" cannot match.
ALLOWED_DOMAIN_SUFFIXES = (
    '.manageengine.com',
    '.manageengine.eu',
    '.manageengine.in',
    '.manageengine.com.au',
    '.manageengine.com.cn',
    '.manageengine.cn',
    '.manageengine.jp',
    '.manageengine.ca',
    '.manageengine.sa',
    '.servicedeskplus.com',
    '.servicedeskplus.eu',
    '.servicedeskplus.in',
    '.servicedeskplus.net.au',
    '.servicedeskplus.cn',
    '.servicedeskplus.jp',
    '.zoho.com',
    '.zoho.eu',
    '.zoho.in',
    '.zoho.com.au',
    '.zoho.com.cn',
    '.zoho.jp',
    '.zoho.ca',
    '.zoho.sa',
)

# A plain DNS host name: labels of alphanumerics/hyphens, at least two labels.
HOSTNAME_PATTERN = r'^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?(\.[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?)+$'

# Portal names are simple slugs (e.g. "ithelpdesk"); no path separators.
PORTAL_NAME_PATTERN = r'^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$'

# SDP record ids are numeric strings; blocks "../" path traversal.
PARENT_ID_PATTERN = r'^[0-9]{1,20}$'
