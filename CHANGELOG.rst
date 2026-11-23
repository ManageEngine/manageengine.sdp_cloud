=====================================
manageengine.sdp\_cloud Release Notes
=====================================

.. contents:: Topics

v1.2.0
======

Release Summary
---------------

Security release. Validates user-supplied URL components, stops forwarding the OAuth token on redirects, and redacts the ``oauth_token`` access token from task output and ansible-runner/navigator artifacts.

Security Fixes
--------------

- api_util - the user-supplied ``domain`` parameter was interpolated into the API base URL without validation, so a tampered playbook variable (shared role, imported playbook, AWX survey or inventory) could point every module at an attacker-controlled host and receive the live OAuth access token in the ``Authorization`` header. ``domain`` is now checked against a fail-closed allowlist of official ServiceDesk Plus Cloud hosts before any request is made, and all modules using ``base_argument_spec()`` are covered.
- api_util - ``portal_name`` and ``parent_id`` are also interpolated into the request path and are now validated (slug and numeric respectively), and every constructed URL is checked so it cannot escape the API base path. This blocks redirecting an authenticated request to an arbitrary endpoint via values such as ``parent_id: "../../other-endpoint"``.
- api_util - the OAuth token is no longer re-attached when a request is redirected. ``ansible.module_utils.urls`` follows redirects by default and preserves the original headers across hosts, so an open redirect on an allowlisted host could otherwise still forward the token. ``Authorization`` is now passed via ``unredirected_headers``.
- oauth_token - the returned ``access_token`` is now redacted from callback output and ansible-runner/ansible-navigator artifacts through a new action plugin that flags successful results as ``no_log``. The registered variable still holds the real token for later tasks.

v1.1.0
======

Release Summary
---------------

Added entity-specific modules for request, problem, change, and release management. Improved argument validation, documentation, and API consistency.

Minor Changes
-------------

- Added RETURN sample values to all modules.
- Added ``required_if`` validation to write modules for ``state=absent`` requiring an entity ID.
- Documented environment variable fallbacks (``SDP_CLOUD_AUTH_TOKEN``, ``SDP_CLOUD_CLIENT_ID``, ``SDP_CLOUD_CLIENT_SECRET``, ``SDP_CLOUD_REFRESH_TOKEN``) in doc fragments.
- Flattened ``list_options`` into top-level parameters (``row_count``, ``sort_field``, ``sort_order``, ``start_index``, ``get_total_count``) for all info modules.
- Removed internal debugging fields (``payload``, ``endpoint``, ``method``) from module return values.
- change - new module for managing changes (create, update, delete).
- change_info - new module for listing or retrieving change details.
- problem - new module for managing problems (create, update, delete).
- problem_info - new module for listing or retrieving problem details.
- release - new module for managing releases (create, update, delete).
- release_info - new module for listing or retrieving release details.
- request - new module for managing requests (create, update, delete).
- request_info - new module for listing or retrieving request details.

Bugfixes
--------

- Added warning on JSON parse failure in ``fetch_existing_record`` instead of silently returning ``None``.
- Fixed inconsistent ``Accept`` header in ``fetch_existing_record`` to use ``application/vnd.manageengine.sdp.v3+json``.

v1.0.0
======

Release Summary
---------------

Initial release of the ManageEngine ServiceDesk Plus Cloud Ansible Collection.

New Modules
-----------

Manageengine
~~~~~~~~~~~~

sdp_cloud
^^^^^^^^^

- manageengine.sdp_cloud.manageengine.sdp_cloud.oauth_token - Generate ManageEngine SDP Cloud OAuth Access Token
- manageengine.sdp_cloud.manageengine.sdp_cloud.read_record - Read API module for ManageEngine ServiceDesk Plus Cloud
- manageengine.sdp_cloud.manageengine.sdp_cloud.write_record - Write API module for ManageEngine ServiceDesk Plus Cloud
