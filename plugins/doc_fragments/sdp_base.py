# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):

    # Base documentation fragment for entity-specific SDP Cloud modules.
    # Contains only connection options (domain, portal_name, auth_token)
    # without parent_module_name or parent_id.
    DOCUMENTATION = r'''
options:
  domain:
    description:
      - The host name of your ServiceDesk Plus Cloud instance.
      - For example, C(sdpondemand.manageengine.com) or C(sdp.zoho.eu).
      - Must be a bare host name (no scheme, port or path) under an official
        ServiceDesk Plus Cloud domain. Any other host is rejected before the
        OAuth token is sent, so a tampered value cannot leak credentials.
    type: str
    required: true
  portal_name:
    description:
      - The portal name of your ServiceDesk Plus Cloud instance (e.g., C(ithelpdesk)).
      - Only letters, digits, hyphen and underscore are allowed.
    type: str
    required: true
  auth_token:
    description:
      - The OAuth access token for authenticating API requests.
      - Mutually exclusive with I(client_id), I(client_secret), and I(refresh_token).
      - If not set, the value of the E(SDP_CLOUD_AUTH_TOKEN) environment variable is used.
    type: str
'''
