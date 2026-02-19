.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.manageengine.sdp_cloud.change_module:

.. Anchors: short name for ansible.builtin

.. Title

manageengine.sdp_cloud.change module -- Manage changes in ManageEngine ServiceDesk Plus Cloud
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `manageengine.sdp_cloud collection <https://galaxy.ansible.com/ui/repo/published/manageengine/sdp_cloud/>`_ (version 1.1.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install manageengine.sdp\_cloud`.

    To use it in a playbook, specify: :code:`manageengine.sdp_cloud.change`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates, updates, or deletes change records in ManageEngine ServiceDesk Plus Cloud.
- When :literal:`state=present` (default) and :literal:`change\_id` is omitted, creates a new change. The :literal:`title` option is mandatory for create operations.
- When :literal:`state=present` and :literal:`change\_id` is set, updates the existing change. Supports idempotency — skips the API call if no changes are detected.
- When :literal:`state=absent`\ , deletes the change identified by :literal:`change\_id`.
- Supports check mode and diff mode.
- See \ `https://www.manageengine.com/products/service\-desk/sdpod\-v3\-api/changes/change.html <https://www.manageengine.com/products/service-desk/sdpod-v3-api/changes/change.html>`__ for full API details.


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

      .. _ansible_collections.manageengine.sdp_cloud.change_module__parameter-auth_token:

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
        <div class="ansibleOptionAnchor" id="parameter-change_id"></div>

      .. _ansible_collections.manageengine.sdp_cloud.change_module__parameter-change_id:

      .. rst-class:: ansible-option-title

      **change_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-change_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The ID of an existing change record.

      Required for update (\ :literal:`state=present`\ ) and delete (\ :literal:`state=absent`\ ) operations.

      Omit when creating a new change.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client_id"></div>

      .. _ansible_collections.manageengine.sdp_cloud.change_module__parameter-client_id:

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

      .. _ansible_collections.manageengine.sdp_cloud.change_module__parameter-client_secret:

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

      .. _ansible_collections.manageengine.sdp_cloud.change_module__parameter-dc:

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

      .. _ansible_collections.manageengine.sdp_cloud.change_module__parameter-domain:

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
        <div class="ansibleOptionAnchor" id="parameter-payload"></div>

      .. _ansible_collections.manageengine.sdp_cloud.change_module__parameter-payload:

      .. rst-class:: ansible-option-title

      **payload**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-payload" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A dictionary of additional change attributes to set.

      Supported fields include :literal:`description`\ , :literal:`comment`\ , :literal:`retrospective`\ , :literal:`stage`\ , :literal:`status`\ , :literal:`template`\ , :literal:`priority`\ , :literal:`urgency`\ , :literal:`impact`\ , :literal:`category`\ , :literal:`subcategory`\ , :literal:`item`\ , :literal:`site`\ , :literal:`group`\ , :literal:`change\_requester`\ , :literal:`change\_manager`\ , :literal:`change\_owner`\ , :literal:`change\_type`\ , :literal:`reason\_for\_change`\ , :literal:`risk`\ , :literal:`workflow`\ , :literal:`scheduled\_start\_time`\ , :literal:`scheduled\_end\_time`\ , :literal:`created\_time`\ , :literal:`completed\_time`\ , and grouped fields :literal:`roll\_out\_plan\_description`\ , :literal:`back\_out\_plan\_description`.

      For create, include all desired fields. For update, include only fields to change.

      Not used when :literal:`state=absent`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-portal_name"></div>

      .. _ansible_collections.manageengine.sdp_cloud.change_module__parameter-portal_name:

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

      .. _ansible_collections.manageengine.sdp_cloud.change_module__parameter-refresh_token:

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
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.manageengine.sdp_cloud.change_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The desired state of the change.

      :literal:`present` ensures the change exists (create or update).

      :literal:`absent` ensures the change is deleted.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-title"></div>

      .. _ansible_collections.manageengine.sdp_cloud.change_module__parameter-title:

      .. rst-class:: ansible-option-title

      **title**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-title" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The title of the change.

      :strong:`Mandatory` when creating a new change (\ :literal:`state=present` without :literal:`change\_id`\ ).

      Optional when updating (only include to change it).


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    - name: Create a Change (minimal)
      manageengine.sdp_cloud.change:
        domain: "sdpondemand.manageengine.com"
        auth_token: "{{ auth_token }}"
        dc: "US"
        portal_name: "ithelpdesk"
        title: "Upgrade database server"

    - name: Create a Change (with extra fields)
      manageengine.sdp_cloud.change:
        domain: "sdpondemand.manageengine.com"
        client_id: "your_client_id"
        client_secret: "your_client_secret"
        refresh_token: "your_refresh_token"
        dc: "US"
        portal_name: "ithelpdesk"
        title: "Upgrade database server"
        payload:
          description: "Upgrade PostgreSQL from 14 to 16"
          priority: "High"
          change_requester: "admin@example.com"
          group: "Infrastructure"

    - name: Update a Change
      manageengine.sdp_cloud.change:
        domain: "sdpondemand.manageengine.com"
        auth_token: "{{ auth_token }}"
        dc: "US"
        portal_name: "ithelpdesk"
        change_id: "123456"
        payload:
          priority: "Low"
          status: "In Progress"

    - name: Delete a Change
      manageengine.sdp_cloud.change:
        domain: "sdpondemand.manageengine.com"
        auth_token: "{{ auth_token }}"
        dc: "US"
        portal_name: "ithelpdesk"
        change_id: "123456"
        state: absent



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
        <div class="ansibleOptionAnchor" id="return-change"></div>

      .. _ansible_collections.manageengine.sdp_cloud.change_module__return-change:

      .. rst-class:: ansible-option-title

      **change**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-change" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The change record from the API response.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create or update

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"change\_type": {"id": "100000000000005", "name": "Standard"}, "created\_time": {"display\_value": "Nov 10, 2025 10:00 AM", "value": "1731234000000"}, "id": "234567890123456", "priority": {"id": "100000000000002", "name": "High"}, "status": {"id": "100000000000001", "name": "Requested"}, "title": "Upgrade database server"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-change_id"></div>

      .. _ansible_collections.manageengine.sdp_cloud.change_module__return-change_id:

      .. rst-class:: ansible-option-title

      **change_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-change_id" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The ID of the created, updated, or deleted change.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create or update

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"234567890123456"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-response"></div>

      .. _ansible_collections.manageengine.sdp_cloud.change_module__return-response:

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
