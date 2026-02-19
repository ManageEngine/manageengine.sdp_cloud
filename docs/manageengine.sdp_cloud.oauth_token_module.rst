.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.manageengine.sdp_cloud.oauth_token_module:

.. Anchors: short name for ansible.builtin

.. Title

manageengine.sdp_cloud.oauth_token module -- Generate ManageEngine SDP Cloud OAuth Access Token
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `manageengine.sdp_cloud collection <https://galaxy.ansible.com/ui/repo/published/manageengine/sdp_cloud/>`_ (version 1.1.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install manageengine.sdp\_cloud`.

    To use it in a playbook, specify: :code:`manageengine.sdp_cloud.oauth_token`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Generates a temporary OAuth access token using a refresh token.
- This token is required for authenticating against the ServiceDesk Plus Cloud API.
- The access token is valid for 1 hour.


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
        <div class="ansibleOptionAnchor" id="parameter-client_id"></div>

      .. _ansible_collections.manageengine.sdp_cloud.oauth_token_module__parameter-client_id:

      .. rst-class:: ansible-option-title

      **client_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The Client ID generated from the Zoho API Console.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client_secret"></div>

      .. _ansible_collections.manageengine.sdp_cloud.oauth_token_module__parameter-client_secret:

      .. rst-class:: ansible-option-title

      **client_secret**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client_secret" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The Client Secret generated from the Zoho API Console.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dc"></div>

      .. _ansible_collections.manageengine.sdp_cloud.oauth_token_module__parameter-dc:

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
        <div class="ansibleOptionAnchor" id="parameter-refresh_token"></div>

      .. _ansible_collections.manageengine.sdp_cloud.oauth_token_module__parameter-refresh_token:

      .. rst-class:: ansible-option-title

      **refresh_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-refresh_token" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The long\-lived refresh token.


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    - name: Generate Access Token using Vaulted Variables
      manageengine.sdp_cloud.oauth_token:
        client_id: "{{ sdp_client_id }}"
        client_secret: "{{ sdp_client_secret }}"
        refresh_token: "{{ sdp_refresh_token }}"
        dc: "US"
      register: auth_response
      no_log: true

    - name: Use the token in subsequent tasks
      manageengine.sdp_cloud.read_record:
        domain: "sdpondemand.manageengine.com"
        portal_name: "ithelpdesk"
        parent_module_name: "request"
        parent_id: "100"
        auth_token: "{{ auth_response.access_token }}"
        dc: "US"



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
        <div class="ansibleOptionAnchor" id="return-access_token"></div>

      .. _ansible_collections.manageengine.sdp_cloud.oauth_token_module__return-access_token:

      .. rst-class:: ansible-option-title

      **access_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-access_token" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The short\-lived OAuth access token.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-expires_in"></div>

      .. _ansible_collections.manageengine.sdp_cloud.oauth_token_module__return-expires_in:

      .. rst-class:: ansible-option-title

      **expires_in**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-expires_in" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The duration in seconds until the access token expires (usually 3600).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-token_type"></div>

      .. _ansible_collections.manageengine.sdp_cloud.oauth_token_module__return-token_type:

      .. rst-class:: ansible-option-title

      **token_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-token_type" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The type of token (e.g., Bearer).


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
