.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.manageengine.sdp_cloud.read_record_module:

.. Anchors: short name for ansible.builtin

.. Title

manageengine.sdp_cloud.read_record module -- Read API module for ManageEngine ServiceDesk Plus Cloud
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `manageengine.sdp_cloud collection <https://galaxy.ansible.com/ui/repo/published/manageengine/sdp_cloud/>`_ (version 1.1.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install manageengine.sdp\_cloud`.

    To use it in a playbook, specify: :code:`manageengine.sdp_cloud.read_record`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Performs data retrieval API operations (GET) on ManageEngine ServiceDesk Plus Cloud entities.
- Supports Requests, Problems, Changes, and Releases.
- If :literal:`parent\_id` is provided, retrieves a single record. Otherwise, retrieves a list of records.


.. Aliases


.. Requirements






.. Options

Parameters
----------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auth_token"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-auth_token:

      .. rst-class:: ansible-option-title

      **auth_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auth_token" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The OAuth access token for authenticating API requests.

      Mutually exclusive with :emphasis:`client\_id`\ , :emphasis:`client\_secret`\ , and :emphasis:`refresh\_token`.

      If not set, the value of the :ansenvvar:`SDP\_CLOUD\_AUTH\_TOKEN` environment variable is used.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client_id"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-client_id:

      .. rst-class:: ansible-option-title

      **client_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The Client ID generated from the Zoho API Console.

      Required together with :emphasis:`client\_secret` and :emphasis:`refresh\_token` if :emphasis:`auth\_token` is not provided.

      If not set, the value of the :ansenvvar:`SDP\_CLOUD\_CLIENT\_ID` environment variable is used.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client_secret"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-client_secret:

      .. rst-class:: ansible-option-title

      **client_secret**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client_secret" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The Client Secret generated from the Zoho API Console.

      Required together with :emphasis:`client\_id` and :emphasis:`refresh\_token` if :emphasis:`auth\_token` is not provided.

      If not set, the value of the :ansenvvar:`SDP\_CLOUD\_CLIENT\_SECRET` environment variable is used.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dc"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-dc:

      .. rst-class:: ansible-option-title

      **dc**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dc" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The Data Center location of your ServiceDesk Plus Cloud instance.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"US"`
      - :ansible-option-choices-entry:`"EU"`
      - :ansible-option-choices-entry:`"IN"`
      - :ansible-option-choices-entry:`"AU"`
      - :ansible-option-choices-entry:`"CN"`
      - :ansible-option-choices-entry:`"JP"`
      - :ansible-option-choices-entry:`"CA"`
      - :ansible-option-choices-entry:`"SA"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-domain"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-domain:

      .. rst-class:: ansible-option-title

      **domain**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-domain" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The domain URL of your ServiceDesk Plus Cloud instance.

      For example, :literal:`sdpondemand.manageengine.com` or :literal:`sdp.zoho.eu`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-get_total_count"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-get_total_count:

      .. rst-class:: ansible-option-title

      **get_total_count**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-get_total_count" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Whether to include the total count of matching records.

      Ignored when :literal:`parent\_id` is provided.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-parent_id"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-parent_id:

      .. rst-class:: ansible-option-title

      **parent_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-parent_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The ID of the specific record to operate on.

      Required for update, get\-by\-id, and delete operations.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-parent_module_name"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-parent_module_name:

      .. rst-class:: ansible-option-title

      **parent_module_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-parent_module_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The ITSM module to operate on.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"request"`
      - :ansible-option-choices-entry:`"problem"`
      - :ansible-option-choices-entry:`"change"`
      - :ansible-option-choices-entry:`"release"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-portal_name"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-portal_name:

      .. rst-class:: ansible-option-title

      **portal_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-portal_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The portal name of your ServiceDesk Plus Cloud instance (e.g., :literal:`ithelpdesk`\ ).


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-refresh_token"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-refresh_token:

      .. rst-class:: ansible-option-title

      **refresh_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-refresh_token" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The long\-lived refresh token from the Zoho API Console.

      Required together with :emphasis:`client\_id` and :emphasis:`client\_secret` if :emphasis:`auth\_token` is not provided.

      If not set, the value of the :ansenvvar:`SDP\_CLOUD\_REFRESH\_TOKEN` environment variable is used.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-row_count"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-row_count:

      .. rst-class:: ansible-option-title

      **row_count**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-row_count" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of records to return per page (1\-100).

      Ignored when :literal:`parent\_id` is provided.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`10`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sort_field"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-sort_field:

      .. rst-class:: ansible-option-title

      **sort_field**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sort_field" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The field to sort results by.

      Ignored when :literal:`parent\_id` is provided.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"created\_time"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-sort_order"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-sort_order:

      .. rst-class:: ansible-option-title

      **sort_order**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-sort_order" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Sort direction.

      Ignored when :literal:`parent\_id` is provided.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"asc"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"desc"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-start_index"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__parameter-start_index:

      .. rst-class:: ansible-option-title

      **start_index**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-start_index" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The starting index for pagination.

      Ignored when :literal:`parent\_id` is provided.


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    - name: Get Request Details
      manageengine.sdp_cloud.read_record:
        domain: "sdpondemand.manageengine.com"
        parent_module_name: "request"
        parent_id: "100"
        client_id: "your_client_id"
        client_secret: "your_client_secret"
        refresh_token: "your_refresh_token"
        dc: "US"
        portal_name: "ithelpdesk"

    - name: Get List of Requests
      manageengine.sdp_cloud.read_record:
        domain: "sdpondemand.manageengine.com"
        parent_module_name: "request"
        client_id: "your_client_id"
        client_secret: "your_client_secret"
        refresh_token: "your_refresh_token"
        dc: "US"
        portal_name: "ithelpdesk"
        row_count: 10
        start_index: 1



.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response"></div>

      .. _ansible_collections.manageengine.sdp_cloud.read_record_module__return-response:

      .. rst-class:: ansible-option-title

      **response**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-response" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The raw response from the SDP Cloud API.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"list\_info": {"has\_more\_rows": true, "row\_count": 10}, "requests": [{"id": "234567890123456", "status": {"id": "100000000000001", "name": "Open"}, "subject": "Server down in DC\-2"}], "response\_status": {"status": "success", "status\_code": 2000}}`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Harish Kumar (@harishkumar-k-7052)


.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/ManageEngine/manageengine.sdp_cloud/issues"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/ManageEngine/manageengine.sdp_cloud"
    external: true


.. Parsing errors
