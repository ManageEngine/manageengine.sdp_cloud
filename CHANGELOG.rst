=====================================
manageengine.sdp\_cloud Release Notes
=====================================

.. contents:: Topics

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
