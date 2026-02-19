.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.manageengine.sdp_cloud.request_module:

.. Anchors: short name for ansible.builtin

.. Title

manageengine.sdp_cloud.request module -- Manage requests in ManageEngine ServiceDesk Plus Cloud
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `manageengine.sdp_cloud collection <https://galaxy.ansible.com/ui/repo/published/manageengine/sdp_cloud/>`_ (version 1.1.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install manageengine.sdp\_cloud`.

    To use it in a playbook, specify: :code:`manageengine.sdp_cloud.request`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Creates, updates, or deletes request records in ManageEngine ServiceDesk Plus Cloud.
- When :literal:`state=present` (default) and :literal:`request\_id` is omitted, creates a new request. The :literal:`subject` option is mandatory for create operations.
- When :literal:`state=present` and :literal:`request\_id` is set, updates the existing request. Supports idempotency — skips the API call if no changes are detected.
- When :literal:`state=absent`\ , deletes the request identified by :literal:`request\_id`.
- Supports check mode and diff mode.
- See \ `https://www.manageengine.com/products/service\-desk/sdpod\-v3\-api/requests/request.html <https://www.manageengine.com/products/service-desk/sdpod-v3-api/requests/request.html>`__ for full API details.


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

      .. _ansible_collections.manageengine.sdp_cloud.request_module__parameter-auth_token:

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

      .. _ansible_collections.manageengine.sdp_cloud.request_module__parameter-client_id:

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

      .. _ansible_collections.manageengine.sdp_cloud.request_module__parameter-client_secret:

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

      .. _ansible_collections.manageengine.sdp_cloud.request_module__parameter-dc:

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

      .. _ansible_collections.manageengine.sdp_cloud.request_module__parameter-domain:

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

      .. _ansible_collections.manageengine.sdp_cloud.request_module__parameter-payload:

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

      A dictionary of additional request attributes to set.

      Supported fields include :literal:`description`\ , :literal:`priority`\ , :literal:`urgency`\ , :literal:`impact`\ , :literal:`status`\ , :literal:`requester`\ , :literal:`technician`\ , :literal:`group`\ , :literal:`category`\ , :literal:`subcategory`\ , :literal:`item`\ , :literal:`due\_by\_time`\ , :literal:`template`\ , :literal:`mode`\ , :literal:`level`\ , :literal:`site`\ , :literal:`on\_behalf\_of`\ , :literal:`editor`\ , :literal:`udf\_fields`\ , and more.

      For create, include all desired fields. For update, include only fields to change.

      Not used when :literal:`state=absent`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-portal_name"></div>

      .. _ansible_collections.manageengine.sdp_cloud.request_module__parameter-portal_name:

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

      .. _ansible_collections.manageengine.sdp_cloud.request_module__parameter-refresh_token:

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
        <div class="ansibleOptionAnchor" id="parameter-request_id"></div>

      .. _ansible_collections.manageengine.sdp_cloud.request_module__parameter-request_id:

      .. rst-class:: ansible-option-title

      **request_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-request_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The ID of an existing request record.

      Required for update (\ :literal:`state=present`\ ) and delete (\ :literal:`state=absent`\ ) operations.

      Omit when creating a new request.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.manageengine.sdp_cloud.request_module__parameter-state:

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

      The desired state of the request.

      :literal:`present` ensures the request exists (create or update).

      :literal:`absent` ensures the request is deleted.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-subject"></div>

      .. _ansible_collections.manageengine.sdp_cloud.request_module__parameter-subject:

      .. rst-class:: ansible-option-title

      **subject**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-subject" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The subject / title of the request.

      :strong:`Mandatory` when creating a new request (\ :literal:`state=present` without :literal:`request\_id`\ ).

      Optional when updating (only include to change it).

      Maximum 250 characters.


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    - name: Create a Request (minimal)
      manageengine.sdp_cloud.request:
        domain: "sdpondemand.manageengine.com"
        auth_token: "{{ auth_token }}"
        dc: "US"
        portal_name: "ithelpdesk"
        subject: "Server down in DC-2"

    - name: Create a Request (with extra fields)
      manageengine.sdp_cloud.request:
        domain: "sdpondemand.manageengine.com"
        client_id: "your_client_id"
        client_secret: "your_client_secret"
        refresh_token: "your_refresh_token"
        dc: "US"
        portal_name: "ithelpdesk"
        subject: "Server down in DC-2"
        payload:
          description: "Web server unresponsive since 10:00 AM"
          priority: "High"
          requester: "admin@example.com"
          group: "Infrastructure"

    - name: Update a Request
      manageengine.sdp_cloud.request:
        domain: "sdpondemand.manageengine.com"
        auth_token: "{{ auth_token }}"
        dc: "US"
        portal_name: "ithelpdesk"
        request_id: "123456"
        payload:
          priority: "Low"
          status: "In Progress"

    - name: Delete a Request
      manageengine.sdp_cloud.request:
        domain: "sdpondemand.manageengine.com"
        auth_token: "{{ auth_token }}"
        dc: "US"
        portal_name: "ithelpdesk"
        request_id: "123456"
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
        <div class="ansibleOptionAnchor" id="return-request"></div>

      .. _ansible_collections.manageengine.sdp_cloud.request_module__return-request:

      .. rst-class:: ansible-option-title

      **request**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-request" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The request record from the API response.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on create or update

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"created\_time": {"display\_value": "Nov 10, 2025 10:00 AM", "value": "1731234000000"}, "group": {"id": "100000000000004", "name": "Infrastructure"}, "id": "234567890123456", "priority": {"id": "100000000000002", "name": "High"}, "requester": {"email\_id": "user@example.com", "id": "100000000000003", "name": "John Doe"}, "status": {"id": "100000000000001", "name": "Open"}, "subject": "Server down in DC\-2"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-request_id"></div>

      .. _ansible_collections.manageengine.sdp_cloud.request_module__return-request_id:

      .. rst-class:: ansible-option-title

      **request_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-request_id" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The ID of the created, updated, or deleted request.


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

      .. _ansible_collections.manageengine.sdp_cloud.request_module__return-response:

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
