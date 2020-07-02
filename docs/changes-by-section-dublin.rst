.. Modifications Copyright © 2017-2018 AT&T Intellectual Property.

.. Licensed under the Creative Commons License, Attribution 4.0 Intl.
   (the "License"); you may not use this documentation except in compliance
   with the License. You may obtain a copy of the License at

.. https://creativecommons.org/licenses/by/4.0/

.. Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


Requirement Changes Introduced in Dublin
----------------------------------------

This document summarizes the requirement changes by section that were
introduced between the Casablanca release and
Dublin release. Click on the requirement number to
navigate to the

.. contents::
    :depth: 2

Summary of Changes
^^^^^^^^^^^^^^^^^^

* **Requirements Added:** 64
* **Requirements Changed:** 275
* **Requirements Removed:** 40


Configuration Management > Ansible Standards and Capabilities > VNF or PNF Configuration via Ansible Requirements > Ansible Client Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-94567`

    The VNF or PNF **MUST** provide Ansible playbooks that are designed to run
    using an inventory hosts file in a supported format with only IP addresses
    or IP addresses and VM/VNF or PNF names.


.. container:: note

    :need:`R-82018`

    The VNF or PNF **MUST** load the Ansible Server SSH public key onto VNF or
    PNF VM(s) /root/.ssh/authorized_keys as part of instantiation. Alternative,
    is for Ansible Server SSH public key to be loaded onto VNF or PNF VM(s)
    under /home/<Mechanized user ID>/.ssh/authorized_keys as part of
    instantiation, when a Mechanized user ID is created during instantiation,
    and Configure and all playbooks are designed to use a mechanized user ID
    only for authentication (never using root authentication during Configure
    playbook run). This will allow the Ansible Server to authenticate to
    perform post-instantiation configuration without manual intervention and
    without requiring specific VNF or PNF login IDs and passwords.

    *CAUTION*: For VNFs or PNFs configured using Ansible, to eliminate the need
    for manual steps, post-instantiation and pre-configuration, to
    upload of SSH public keys, SSH public keys loaded during (heat)
    instantiation shall be preserved and not removed by (heat) embedded
    (userdata) scripts.


.. container:: note

    :need:`R-35401`

    The VNF or PNF **MUST** support SSH and allow SSH access by the
    Ansible server to the endpoint VM(s) and comply with the Network
    Cloud Service Provider guidelines for authentication and access.


.. container:: note

    :need:`R-97451`

    The VNF or PNF **MUST** provide the ability to remove root access once
    post-instantiation configuration (Configure) is completed.


.. container:: note

    :need:`R-45197`

    The VNF or PNF **MUST** define the "from=" clause to provide the list of IP
    addresses of the Ansible Servers in the Cluster, separated by coma, to
    restrict use of the SSH key pair to elements that are part of the Ansible
    Cluster owner of the issued and assigned mechanized user ID.


.. container:: note

    :need:`R-73459`

    The VNF or PNF **MUST** provide the ability to include a "from=" clause in
    SSH public keys associated with mechanized user IDs created for an Ansible
    Server cluster to use for VNF or PNF VM authentication.


.. container:: note

    :need:`R-97345`

    The VNF or PNF **MUST** permit authentication, using root account, only
    right after instantiation and until post-instantiation configuration is
    completed.


.. container:: note

    :need:`R-92866`

    The VNF or PNF **MUST** include as part of post-instantiation configuration
    done by Ansible Playbooks the removal/update of the SSH public key from
    /root/.ssh/authorized_keys, and update of SSH keys loaded through
    instantiation to support Ansible. This may include creating Mechanized user
    ID(s) used by the Ansible Server(s) on VNF VM(s) and uploading and
    installing new SSH keys used by the mechanized use ID(s).


.. container:: note

    :need:`R-67124`

    The VNF or PNF **MUST** provide Ansible playbooks that are designed to run
    using an inventory hosts file in a supported format; with group names
    matching VNFC 3-character string adding "vip" for groups with virtual IP
    addresses shared by multiple VMs as seen in examples provided in Appendix.


.. container:: note

    :need:`R-32217`

    The VNF or PNF **MUST** have routable management IP addresses or FQDNs that
    are reachable via the Ansible Server for the endpoints (VMs) of a
    VNF or PNF that playbooks will target. ONAP will initiate requests to the
    Ansible Server for invocation of playbooks against these end
    points [#7.3.3]_.


.. container:: note

    :need:`R-54373`

    The VNF or PNF **MUST** have Python >= 2.6 on the endpoint VM(s)
    of a VNF or PNF on which an Ansible playbook will be executed.


.. container:: note

    :need:`R-24482`

    The VNF or PNF **MUST** provide Ansible playbooks that are designed to run
    using an inventory hosts file in a supported format; with site group that
    shall be used to add site specific configurations to the target VNF or PNF
    VM(s) as needed.


.. container:: note

    :need:`R-91745`

    The VNF or PNF **MUST** update the Ansible Server and other entities
    storing and using the SSH keys for authentication when the SSH
    keys used by Ansible are regenerated/updated.

    **Note**: Ansible Server itself may be used to upload new SSH public
    keys onto supported VNFs or PNFs.


Configuration Management > Ansible Standards and Capabilities > VNF or PNF Configuration via Ansible Requirements > Ansible Playbook Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-49911`

    The VNF or PNF provider **MUST** assign a new point release to the updated
    playbook set. The functionality of a new playbook set must be tested before
    it is deployed to the production.


.. container:: note

    :need:`R-58301`

    The VNF or PNF **SHOULD NOT** use playbooks that make requests to
    Cloud resources e.g. Openstack (nova, neutron, glance, heat, etc.);
    therefore, there is no use for Cloud specific variables like Openstack
    UUIDs in Ansible Playbook related artifacts.

    **Rationale**: Flows that require interactions with Cloud services e.g.
    Openstack shall rely on workflows run by an Orchestrator
    (Change Management) or other capability (such as a control loop or
    Operations GUI) outside Ansible Server which can be executed by a
    APPC/SDN-C. There are policies, as part of Control Loop
    models, that send remediation action requests to an APPC/SDN-C; these
    are triggered as a response to an event or correlated events published
    to Event Bus.


.. container:: note

    :need:`R-24189`

    The VNF or PNF provider **MUST** deliver a new set of playbooks that
    includes all updated and unchanged playbooks for any new revision to an
    existing set of playbooks.


.. container:: note

    :need:`R-43353`

    The VNF or PNF **MUST** return control from Ansible Playbooks only after
    all tasks performed by playbook are fully complete, signaling that the
    playbook completed all tasks. When starting services, return control
    only after all services are up. This is critical for workflows where
    the next steps are dependent on prior tasks being fully completed.


.. container:: note

    :need:`R-51442`

    The VNF or PNF **SHOULD** use playbooks that are designed to
    automatically 'rollback' to the original state in case of any errors
    for actions that change state of the VNF or PNF (e.g., configure).

    **Note**: In case rollback at the playbook level is not supported or
    possible, the VNF or PNF provider shall provide alternative rollback
    mechanism (e.g., for a small VNF or PNF the rollback mechanism may rely
    on workflow to terminate and re-instantiate VNF VMs and then re-run
    playbook(s)). Backing up updated files is also recommended to support
    rollback when soft rollback is feasible.


.. container:: note

    :need:`R-48698`

    The VNF or PNF **MUST** utilize information from key value pairs that will
    be provided by the Ansible Server as "extra-vars" during invocation to
    execute the desired VNF or PNF action. The "extra-vars" attribute-value
    pairs are passed to the Ansible Server by an APPC/SDN-C as part of the
    Rest API request. If the playbook requires files, they must also be
    supplied using the methodology detailed in the Ansible Server API, unless
    they are bundled with playbooks, example, generic templates. Any files
    containing instance specific info (attribute-value pairs), not obtainable
    from any ONAP inventory databases or other sources, referenced and used an
    input by playbooks, shall be provisioned (and distributed) in advance of
    use, e.g., VNF or PNF instantiation. Recommendation is to avoid these
    instance specific, manually created in advance of instantiation, files.


.. container:: note

    :need:`R-43253`

    The VNF or PNF **MUST** use playbooks designed to allow Ansible
    Server to infer failure or success based on the "PLAY_RECAP" capability.

    **Note**: There are cases where playbooks need to interpret results
    of a task and then determine success or failure and return result
    accordingly (failure for failed tasks).


.. container:: note

    :need:`R-50252`

    The VNF or PNF **MUST** write to a response file in JSON format that will
    be retrieved and made available by the Ansible Server if, as part of a VNF
    or PNF action (e.g., audit), a playbook is required to return any VNF or
    PNF information/response. The text files must be written in the main
    playbook home directory, in JSON format. The JSON file must be created for
    the VNF or PNF with the name '<VNF or PNF name>_results.txt'. All playbook
    output results, for all VNF or PNF VMs, to be provided as a response to the
    request, must be written to this response file.


.. container:: note

    :need:`R-49751`

    The VNF or PNF **MUST** support Ansible playbooks that are compatible with
    Ansible version 2.6 or later.


.. container:: note

    :need:`R-33280`

    The VNF or PNF **MUST NOT** use any instance specific parameters
    in a playbook.


.. container:: note

    :need:`R-40293`

    The VNF or PNF **MUST** make available playbooks that conform
    to the ONAP requirement.


.. container:: note

    :need:`R-02651`

    The VNF or PNF **SHOULD** use available backup capabilities to save a
    copy of configuration files before implementing changes to support
    operations such as backing out of software upgrades, configuration
    changes or other work as this will help backing out of configuration
    changes when needed.


.. container:: note

    :need:`R-49396`

    The VNF or PNF **MUST** support each APPC/SDN-C VNF or PNF action
    by invocation of **one** playbook [#7.3.4]_. The playbook will be
    responsible for executing all necessary tasks (as well as calling other
    playbooks) to complete the request.


Configuration Management > Chef Standards and Capabilities > VNF or PNF Configuration via Chef Requirements > Chef Client Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-47068`

    The VNF or PNF **MAY** expose a single endpoint that is
    responsible for all functionality.


.. container:: note

    :need:`R-79224`

    The VNF or PNF **MUST** have the chef-client be preloaded with
    validator keys and configuration to register with the designated
    Chef Server as part of the installation process.


.. container:: note

    :need:`R-67114`

    The VNF or PNF **MUST** be installed with Chef-Client >= 12.0 and Chef
    push jobs client >= 2.0.


.. container:: note

    :need:`R-72184`

    The VNF or PNF **MUST** have routable FQDNs for all the endpoints
    (VMs) of a VNF or PNF that contain chef-clients which are used to register
    with the Chef Server.  As part of invoking VNF or PNF actions, ONAP will
    trigger push jobs against FQDNs of endpoints for a VNF or PNF, if required.


Configuration Management > Chef Standards and Capabilities > VNF or PNF Configuration via Chef Requirements > Chef Roles/Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-37929`

    The VNF or PNF **MUST** accept all necessary instance specific
    data from the environment or node object attributes for the VNF or PNF
    in roles/cookbooks/recipes invoked for a VNF or PNF action.


.. container:: note

    :need:`R-62170`

    The VNF or PNF **MUST** over-ride any default values for
    configurable parameters that can be set by ONAP in the roles,
    cookbooks and recipes.


.. container:: note

    :need:`R-30654`

    The VNF or PNF Package **MUST** have appropriate cookbooks that are
    designed to automatically 'rollback' to the original state in case of
    any errors for actions that change state of the VNF or PNF (e.g.,
    configure).


.. container:: note

    :need:`R-26567`

    The VNF or PNF Package **MUST** include a run list of
    roles/cookbooks/recipes, for each supported VNF or PNF action, that will
    perform the desired VNF or PNF action in its entirety as specified by ONAP
    (see Section 7.c, APPC/SDN-C APIs and Behavior, for list of VNF or PNF
    actions and requirements), when triggered by a chef-client run list
    in JSON file.


.. container:: note

    :need:`R-27310`

    The VNF or PNF Package **MUST** include all relevant Chef artifacts
    (roles/cookbooks/recipes) required to execute VNF or PNF actions requested
    by ONAP for loading on appropriate Chef Server.


.. container:: note

    :need:`R-44013`

    The VNF or PNF **MUST** populate an attribute, defined as node
    ['PushJobOutput'] with the desired output on all nodes in the push job
    that execute chef-client run if the VNF or PNF action requires the output
    of a chef-client run be made available (e.g., get running configuration).


.. container:: note

    :need:`R-15885`

    The VNF or PNF **MUST** Upon completion of the chef-client run,
    POST back on the callback URL, a JSON object as described in Table
    A2 if the chef-client run list includes a cookbook/recipe that is
    callback capable. Failure to POST on the Callback Url should not be
    considered a critical error. That is, if the chef-client successfully
    completes the VNF or PNF action, it should reflect this status on the Chef
    Server regardless of whether the Callback succeeded or not.


.. container:: note

    :need:`R-65755`

    The VNF or PNF **SHOULD** support callback URLs to return information
    to ONAP upon completion of the chef-client run for any chef-client run
    associated with a VNF or PNF action.

    -  As part of the push job, ONAP will provide two parameters in the
       environment of the push job JSON object:

        -  "RequestId" a unique Id to be used to identify the request,
        -  "CallbackUrl", the URL to post response back.

    -  If the CallbackUrl field is empty or missing in the push job, then
       the chef-client run need not post the results back via callback.


.. container:: note

    :need:`R-98911`

    The VNF or PNF **MUST NOT** use any instance specific parameters
    for the VNF or PNF in roles/cookbooks/recipes invoked for a VNF or PNF
    action.


.. container:: note

    :need:`R-78116`

    The VNF or PNF **MUST** update status on the Chef Server
    appropriately (e.g., via a fail or raise an exception) if the
    chef-client run encounters any critical errors/failures when
    executing a VNF or PNF action.


Configuration Management > Controller Interactions With VNF or PNF > Configuration Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-20741`

    The VNF or PNF **MUST** support APPC/SDN-C ``Configure`` command.


.. container:: note

    :need:`R-56385`

    The VNF or PNF **MUST** support APPC ``Audit`` command.


.. container:: note

    :need:`R-48247`

    The VNF or PNF **MUST** support APPC ``ConfigRestore`` command.


.. container:: note

    :need:`R-94084`

    The VNF or PNF **MUST** support APPC/SDN-C ``ConfigScaleOut`` command.


.. container:: note

    :need:`R-19366`

    The VNF or PNF **MUST** support APPC ``ConfigModify`` command.


.. container:: note

    :need:`R-32981`

    The VNF or PNF **MUST** support APPC ``ConfigBackup`` command.


Configuration Management > Controller Interactions With VNF or PNF > HealthCheck and Failure Related Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-41430`

    The VNF or PNF **MUST** support APPC/SDN-C ``HealthCheck`` command.


Configuration Management > Controller Interactions With VNF or PNF > Lifecycle Management Related Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-65641`

    The VNF or PNF **MUST** support APPC/SDN-C ``UpgradeBackOut`` command.


.. container:: note

    :need:`R-97343`

    The VNF or PNF **MUST** support APPC/SDN-C ``UpgradeBackup`` command.


.. container:: note

    :need:`R-45856`

    The VNF or PNF **MUST** support APPC/SDN-C ``UpgradePostCheck`` command.


.. container:: note

    :need:`R-07251`

    The VNF or PNF **MUST** support APPC/SDN-C ``ResumeTraffic`` command.


.. container:: note

    :need:`R-19922`

    The VNF or PNF **MUST** support APPC/SDN-C ``UpgradePrecheck`` command.


.. container:: note

    :need:`R-49466`

    The VNF or PNF **MUST** support APPC/SDN-C ``UpgradeSoftware`` command.


.. container:: note

    :need:`R-82811`

    The VNF or PNF **MUST** support APPC ``StartApplication`` command.


.. container:: note

    :need:`R-12706`

    The VNF or PNF **MUST** support APPC/SDN-C ``QuiesceTraffic`` command.


.. container:: note

    :need:`R-328086`

    The VNF or PNF **MUST**, if serving as a distribution point or anchor point for
    steering point from source to destination, support the ONAP Controller's
    ``DistributeTraffic`` command.


.. container:: note

    :need:`R-83146`

    The VNF or PNF **MUST** support APPC ``StopApplication`` command.


Configuration Management > NETCONF Standards and Capabilities > VNF or PNF Configuration via NETCONF Requirements > Configuration Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-95950`

    The VNF or PNF **MUST** provide a NETCONF interface fully defined
    by supplied YANG models for the embedded NETCONF server.


.. container:: note

    :need:`R-88026`

    The VNF or PNF **MUST** include a NETCONF server enabling
    runtime configuration and lifecycle management capabilities.


Configuration Management > NETCONF Standards and Capabilities > VNF or PNF Configuration via NETCONF Requirements > NETCONF Server Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-997907`

    The VNF or PNF **SHOULD** support TLS as secure transport for the NETCONF
    protocol according to [RFC7589].


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-26115`

    The VNF or PNF **MUST** follow the data model update rules defined in
    [RFC6020] section 10 for YANG 1.0 modules, and [RFC7950] section 11
    for YANG 1.1 modules. All deviations from the aforementioned update
    rules shall be handled by a built-in  automatic upgrade mechanism.


.. container:: note

    :need:`R-10716`

    The VNF or PNF **MUST** support parallel and simultaneous
    configuration of separate objects within itself.


.. container:: note

    :need:`R-59610`

    The VNF or PNF **MUST** implement the data model discovery and
    download as defined in [RFC6022].


.. container:: note

    :need:`R-83790`

    The VNF or PNF **MUST** implement the ``:validate`` capability.


.. container:: note

    :need:`R-62468`

    The VNF or PNF **MUST** allow all configuration data to be
    edited through a NETCONF <edit-config> operation. Proprietary
    NETCONF RPCs that make configuration changes are not sufficient.


.. container:: note

    :need:`R-29495`

    The VNF or PNF **MUST** support locking if a common object is
    being manipulated by two simultaneous NETCONF configuration operations
    on the same VNF or PNF within the context of the same writable running data
    store (e.g., if an interface parameter is being configured then it
    should be locked out for configuration by a simultaneous configuration
    operation on that same interface parameter).


.. container:: note

    :need:`R-88031`

    The VNF or PNF **SHOULD** implement the protocol operation:
    ``delete-config(target)`` - Delete the named configuration
    data store target.


.. container:: note

    :need:`R-54190`

    The VNF or PNF **MUST** release locks to prevent permanent lock-outs
    when/if a session applying the lock is terminated (e.g., SSH session
    is terminated).


.. container:: note

    :need:`R-49145`

    The VNF or PNF **MUST** implement ``:confirmed-commit`` If
    ``:candidate`` is supported.


.. container:: note

    :need:`R-96554`

    The VNF or PNF **MUST** implement the protocol operation:
    ``unlock(target)`` - Unlock the configuration data store target.


.. container:: note

    :need:`R-22946`

    The VNF or PNF **SHOULD** conform its YANG model to RFC 6536,
    "NETCONF Access Control Model".


.. container:: note

    :need:`R-01382`

    The VNF or PNF **MUST** allow the entire configuration of the VNF or PNF to be
    retrieved via NETCONF's <get-config> and <edit-config>, independently
    of whether it was configured via NETCONF or other mechanisms.


.. container:: note

    :need:`R-10173`

    The VNF or PNF **MUST** allow another NETCONF session to be able to
    initiate the release of the lock by killing the session owning the lock,
    using the <kill-session> operation to guard against hung NETCONF sessions.


.. container:: note

    :need:`R-08134`

    The VNF or PNF **MUST** conform to the NETCONF RFC 6241,
    "NETCONF Configuration Protocol".


.. container:: note

    :need:`R-60656`

    The VNF or PNF **MUST** support sub tree filtering.


.. container:: note

    :need:`R-29488`

    The VNF or PNF **MUST** implement the protocol operation:
    ``get-config(source, filter`` - Retrieve a (filtered subset of
    a) configuration from the configuration data store source.


.. container:: note

    :need:`R-01334`

    The VNF or PNF **MUST** conform to the NETCONF RFC 5717,
    "Partial Lock Remote Procedure Call".


.. container:: note

    :need:`R-33946`

    The VNF or PNF **MUST** conform to the NETCONF RFC 4741,
    "NETCONF Configuration Protocol".


.. container:: note

    :need:`R-25238`

    The VNF or PNF PACKAGE **MUST** validated YANG code using the open
    source pyang [#7.3.1]_ program using the following commands:

    .. code-block:: text

      $ pyang --verbose --strict <YANG-file-name(s)> $ echo $!


.. container:: note

    :need:`R-10129`

    The VNF or PNF **SHOULD** conform its YANG model to RFC 7223,
    "A YANG Data Model for Interface Management".


.. container:: note

    :need:`R-33955`

    The VNF or PNF **SHOULD** conform its YANG model to RFC 6991,
    "Common YANG Data Types".


.. container:: note

    :need:`R-88899`

    The VNF or PNF **MUST** support simultaneous <commit> operations
    within the context of this locking requirements framework.


.. container:: note

    :need:`R-11235`

    The VNF or PNF **MUST** implement the protocol operation:
    ``kill-session(session``- Force the termination of **session**.


.. container:: note

    :need:`R-12271`

    The VNF or PNF **SHOULD** conform its YANG model to RFC 7223,
    "IANA Interface Type YANG Module".


.. container:: note

    :need:`R-90007`

    The VNF or PNF **MUST** implement the protocol operation:
    ``close-session()`` - Gracefully close the current session.


.. container:: note

    :need:`R-03465`

    The VNF or PNF **MUST** release locks to prevent permanent lock-outs
    when the corresponding <partial-unlock> operation succeeds.


.. container:: note

    :need:`R-93443`

    The VNF or PNF **MUST** define all data models in YANG 1.0 [RFC6020] or
    YANG 1.1 [RFC7950]. A combination of YANG 1.0 and YANG 1.1 modules is
    allowed subject to the rules in [RFC7950] section 12. The mapping to
    NETCONF shall follow the rules defined in this RFC.


.. container:: note

    :need:`R-29324`

    The VNF or PNF **SHOULD** implement the protocol operation:
    ``copy-config(target, source)`` - Copy the content of the
    configuration data store source to the configuration data store target.


.. container:: note

    :need:`R-68990`

    The VNF or PNF **MUST** support the ``:startup`` capability. It
    will allow the running configuration to be copied to this special
    database. It can also be locked and unlocked.


.. container:: note

    :need:`R-80898`

    TThe VNF or PNF **MUST** support heartbeat via a <get> with null filter.


.. container:: note

    :need:`R-66793`

    The VNF or PNF **MUST** guarantee the VNF or PNF configuration integrity
    for all simultaneous configuration operations (e.g., if a change is
    attempted to the BUM filter rate from multiple interfaces on the same
    EVC, then they need to be sequenced in the VNF or PNF without locking either
    configuration method out).


.. container:: note

    :need:`R-11499`

    The VNF or PNF **MUST** fully support the XPath 1.0 specification
    for filtered retrieval of configuration and other database contents.
    The 'type' attribute within the <filter> parameter for <get> and
    <get-config> operations may be set to 'xpath'. The 'select' attribute
    (which contains the XPath expression) will also be supported by the
    server. A server may support partial XPath retrieval filtering, but
    it cannot advertise the ``:xpath`` capability unless the entire XPath
    1.0 specification is supported.


.. container:: note

    :need:`R-63935`

    The VNF or PNF **MUST** release locks to prevent permanent lock-outs
    when a user configured timer has expired forcing the NETCONF SSH Session
    termination (i.e., product must expose a configuration knob for a user
    setting of a lock expiration timer).


.. container:: note

    :need:`R-63953`

    The VNF or PNF **MUST** have the echo command return a zero value
    otherwise the validation has failed.


.. container:: note

    :need:`R-26508`

    The VNF or PNF **MUST** support a NETCONF server that can be mounted on
    OpenDaylight (client) and perform the operations of: modify, update,
    change, rollback configurations using each configuration data element,
    query each state (non-configuration) data element, execute each YANG
    RPC, and receive data through each notification statement.


.. container:: note

    :need:`R-70496`

    The VNF or PNF **MUST** implement the protocol operation:
    ``commit(confirmed, confirm-timeout)`` - Commit candidate
    configuration data store to the running configuration.


.. container:: note

    :need:`R-24269`

    The VNF or PNF **SHOULD** conform its YANG model to RFC 7407,
    "A YANG Data Model for SNMP Configuration", if Netconf used to
    configure SNMP engine.


.. container:: note

    :need:`R-13800`

    The VNF or PNF **MUST** conform to the NETCONF RFC 5277,
    "NETCONF Event Notification".


.. container:: note

    :need:`R-22700`

    The VNF or PNF **MUST** conform its YANG model to RFC 6470,
    "NETCONF Base Notifications".


.. container:: note

    :need:`R-78282`

    The VNF or PNF **MUST** conform to the NETCONF RFC 6242,
    "Using the Network Configuration Protocol over Secure Shell".


.. container:: note

    :need:`R-53317`

    The VNF or PNF **MUST** conform its YANG model to RFC 6087,
    "Guidelines for Authors and Reviewers of YANG Data Model specification".


.. container:: note

    :need:`R-97529`

    The VNF or PNF **SHOULD** implement the protocol operation:
    ``get-schema(identifier, version, format)`` - Retrieve the YANG schema.


.. container:: note

    :need:`R-18733`

    The VNF or PNF **MUST** implement the protocol operation:
    ``discard-changes()`` - Revert the candidate configuration
    data store to the running configuration.


.. container:: note

    :need:`R-44281`

    The VNF or PNF **MUST** implement the protocol operation:
    ``edit-config(target, default-operation, test-option, error-option,
    config)`` - Edit the target configuration data store by merging,
    replacing, creating, or deleting new config elements.


.. container:: note

    :need:`R-02597`

    The VNF or PNF **MUST** implement the protocol operation:
    ``lock(target)`` - Lock the configuration data store target.


.. container:: note

    :need:`R-20353`

    The VNF or PNF **MUST** implement both ``:candidate`` and
    ``:writable-running`` capabilities. When both ``:candidate`` and
    ``:writable-running`` are provided then two locks should be supported.


.. container:: note

    :need:`R-10353`

    The VNF or PNF **MUST** conform its YANG model to RFC 6244,
    "An Architecture for Network Management Using NETCONF and YANG".


.. container:: note

    :need:`R-60106`

    The VNF or PNF **MUST** implement the protocol operation:
    ``get(filter)`` - Retrieve (a filtered subset of) the running
    configuration and device state information. This should include
    the list of VNF or PNF supported schemas.


.. container:: note

    :need:`R-87564`

    The VNF or PNF **SHOULD** conform its YANG model to RFC 7317,
    "A YANG Data Model for System Management".


.. container:: note

    :need:`R-83873`

    The VNF or PNF **MUST** support ``:rollback-on-error`` value for
    the <error-option> parameter to the <edit-config> operation. If any
    error occurs during the requested edit operation, then the target
    database (usually the running configuration) will be left unaffected.
    This provides an 'all-or-nothing' edit mode for a single <edit-config>
    request.


.. container:: note

    :need:`R-73468`

    The VNF or PNF **MUST** allow the NETCONF server connection
    parameters to be configurable during virtual machine instantiation
    through Heat templates where SSH keys, usernames, passwords, SSH
    service and SSH port numbers are Heat template parameters.


.. container:: note

    :need:`R-28756`

    The VNF or PNF **MUST** support ``:partial-lock`` and
    ``:partial-unlock`` capabilities, defined in RFC 5717. This
    allows multiple independent clients to each write to a different
    part of the <running> configuration at the same time.


.. container:: note

    :need:`R-68200`

    The VNF or PNF **MUST** support the ``:url`` value to specify
    protocol operation source and target parameters. The capability URI
    for this feature will indicate which schemes (e.g., file, https, sftp)
    that the server supports within a particular URL value. The 'file'
    scheme allows for editable local configuration databases. The other
    schemes allow for remote storage of configuration databases.


.. container:: note

    :need:`R-53015`

    The VNF or PNF **MUST** apply locking based on the sequence of
    NETCONF operations, with the first configuration operation locking
    out all others until completed.


.. container:: note

    :need:`R-07545`

    The VNF or PNF **MUST** support all operations, administration and
    management (OAM) functions available from the supplier for VNFs or PNFs
    using the supplied YANG code and associated NETCONF servers.


.. container:: note

    :need:`R-41829`

    The VNF or PNF **MUST** be able to specify the granularity of the
    lock via a restricted or full XPath expression.


.. container:: note

    :need:`R-49036`

    The VNF or PNF **SHOULD** conform its YANG model to RFC 7277,
    "A YANG Data Model for IP Management".


.. container:: note

    :need:`R-02616`

    The VNF or PNF **MUST** permit locking at the finest granularity
    if a VNF or PNF needs to lock an object for configuration to avoid blocking
    simultaneous configuration operations on unrelated objects (e.g., BGP
    configuration should not be locked out if an interface is being
    configured or entire Interface configuration should not be locked out
    if a non-overlapping parameter on the interface is being configured).


.. container:: note

    :need:`R-58358`

    The VNF or PNF **MUST** implement the ``:with-defaults`` capability
    [RFC6243].


.. container:: note

    :need:`R-04158`

    The VNF or PNF **MUST** conform to the NETCONF RFC 4742,
    "Using the NETCONF Configuration Protocol over Secure Shell (SSH)".


Configuration Management > NETCONF Standards and Capabilities > xNF Configuration via NETCONF Requirements > NETCONF Server Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-28545

    The xNF **MUST** conform its YANG model to RFC 6060,
    "YANG - A Data Modeling Language for the Network Configuration
    Protocol (NETCONF)".


Configuration Management > VNF or PNF REST APIs > REST APIs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-31809`

    The VNF or PNF **MUST** support the HealthCheck RPC. The HealthCheck
    RPC executes a VNF or PNF Provider-defined VNF or PNF HealthCheck over the
    scope of the entire VNF or PNF (e.g., if there are multiple VNFCs, then
    run a health check, as appropriate, for all VNFCs). It returns a 200 OK if
    the test completes. A JSON object is returned indicating state (healthy,
    unhealthy), scope identifier, time-stamp and one or more blocks containing
    info and fault information. If the VNF or PNF is unable to run the
    HealthCheck, return a standard http error code and message.


Contrail Resource Parameters > OS::ContrailV2::VirtualMachineInterface Property virtual_machine_interface_allowed_address_pairs > External Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-100280`

    If a VNF's Heat Orchestration Template's resource
    ``OS::ContrailV2::VirtualMachineInterface``
    is attaching to an external network (per the
    ONAP definition, see Requirement R-57424), the
    map property

    ``virtual_machine_interface_allowed_address_pairs``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``

    parameter
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-100310`

    When the VNF's Heat Orchestration Template's resource
    ``OS::ContrailV2::VirtualMachineInterface`` is attaching to an external
    network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv4 Virtual IP (VIP)
    is required to be supported by the ONAP data model,
    the map property

    ``virtual_machine_interface_allowed_address_pairs``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``

    parameter name **MUST** follow the naming convention

    * ``{vm-type}_{network-role}_floating_ip``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the external network

    And the parameter **MUST** be declared as type ``string``.

    The ONAP data model can only support one IPv4 VIP address.


.. container:: note

    :need:`R-100330`

    When the VNF's Heat Orchestration Template's resource
    ``OS::ContrailV2::VirtualMachineInterface`` is attaching to an external
    network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv6 Virtual IP (VIP)
    is required to be supported by the ONAP data model,
    the map property

    ``virtual_machine_interface_allowed_address_pairs``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``

    parameter name **MUST** follow the naming convention

    * ``{vm-type}_{network-role}_floating_v6_ip``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the external network

    And the parameter **MUST** be declared as type ``string``.

    The ONAP data model can only support one IPv6 VIP address.


.. container:: note

    :need:`R-100350`

    When the VNF's Heat Orchestration Template's resource
    ``OS::ContrailV2::VirtualMachineInterface`` is attaching to an
    external network
    (per the ONAP definition, see Requirement R-57424),
    and the IPv4 VIP address and/or IPv6 VIP address
    is **not** supported by the ONAP data model,
    the map property

    ``virtual_machine_interface_allowed_address_pairs``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``

    * Parameter name **MAY** use any naming convention.  That is, there is no
      ONAP mandatory parameter naming convention.
    * Parameter **MAY** be declared as type ``string`` or type
    ``comma_delimited_list``.

    And the ``OS::ContrailV2::VirtualMachineInterface`` resource
    **MUST** contain resource-level ``metadata`` (not property-level).

    And the ``metadata`` format **MUST**  must contain the
    key value ``aap_exempt`` with a list of all map property

    ``virtual_machine_interface_allowed_address_pairs``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``

    parameters **not** supported by the ONAP data model.


Contrail Resource Parameters > OS::ContrailV2::VirtualMachineInterface Property virtual_machine_interface_allowed_address_pairs > Internal Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-100360`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualMachineInterface`` is attaching to an
    internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv4 Virtual IP (VIP)
    address is assigned using the map property,
    ``virtual_machine_interface_allowed_address_pairs,
    virtual_machine_interface_allowed_address_pairs_allowed_address_pair,
    virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip,
    virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``
    , the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_ip``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as ``type: string``
    and **MUST** be enumerated in the environment file.

    OR

    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as ``type: comma_delimited_list``
    and **MUST** be enumerated in the environment file.


.. container:: note

    :need:`R-100370`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualMachineInterface`` is attaching to an
    internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv6 Virtual IP (VIP)
    address is assigned
    using the map property,
    ``virtual_machine_interface_allowed_address_pairs,
    virtual_machine_interface_allowed_address_pairs_allowed_address_pair,
    virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip,
    virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``
    , the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_v6_ip``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as ``type: string``
    and **MUST** be enumerated in the environment file

    OR

    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_v6_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as ``type: comma_delimited_list``
    and **MUST** be enumerated in the environment file.


Contrail Resource Parameters > Resource OS::ContrailV2::InstanceIp > Resource OS::ContrailV2::InstanceIp Property instance_ip_address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-100000`

    The VNF's Heat Orchestration Template's
    resource ``OS::ContrailV2::InstanceIp`` property ``instance_ip_address``
    parameter
    **MUST** be declared as either type ``string`` or type
    ``comma_delimited_list``.


.. container:: note

    :need:`R-100010`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an external network (per the ONAP definition, see Requirement R-57424),
    and an IPv4 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a string,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_{network-role}_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the external network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one


.. container:: note

    :need:`R-100020`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` property ``instance_ip_address``
    parameter
    ``{vm-type}_{network-role}_ip_{index}``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-100030`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv4 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_{network-role}_ips``

      where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the external
        network


.. container:: note

    :need:`R-100040`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` property ``instance_ip_address``
    parameter
    ``{vm-type}_{network-role}_ips``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-100050`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an external network
    (per the
    ONAP definition, see Requirement R-57424),
    and an IPv6 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a string,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_{network-role}_v6_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the
      ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the external network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one


.. container:: note

    :need:`R-100060`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` property ``instance_ip_address``
    parameter
    ``{vm-type}_{network-role}_v6_ip_{index}``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-100070`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv6 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_{network-role}_v6_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network


.. container:: note

    :need:`R-100080`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` property ``instance_ip_address``
    parameter
    ``{vm-type}_{network-role}_v6_ips``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-100090`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv4 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is
    defined as a ``string``,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_int_{network-role}_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the
      ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the internal network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one


.. container:: note

    :need:`R-100100`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` property ``instance_ip_address``
    parameter
    ``{vm-type}_int_{network-role}_ip_{index}``
    **MUST** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-100110`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv4 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the internal
        network


.. container:: note

    :need:`R-100120`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` property ``instance_ip_address``
    parameter
    ``{vm-type}_int_{network-role}_int_ips``
    **MUST** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-100130`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address to an
    internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv6 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a
    ``string``,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_int_{network-role}_v6_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the internal network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one


.. container:: note

    :need:`R-100140`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` property ``instance_ip_address``
    parameter
    ``{vm-type}_int_{network-role}_v6_ip_{index}``
    **MUST** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-100150`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address to an
    internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv6 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_v6_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the internal
        network


.. container:: note

    :need:`R-100160`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` property ``instance_ip_address``
    map property ``ip_address`` parameter
    ``{vm-type}_int_{network-role}_v6_ips``
    **MUST** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-100170`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp``
    property ``instance_ip_address``
    parameter associated with an external network, i.e.,

     * ``{vm-type}_{network-role}_ip_{index}``
     * ``{vm-type}_{network-role}_v6_ip_{index}``
     * ``{vm-type}_{network-role}_ips``
     * ``{vm-type}_{network-role}_v6_ips``


    **MUST NOT** be enumerated in the Heat Orchestration
    Template's Environment File.  ONAP provides the IP address
    assignments at orchestration time.


.. container:: note

    :need:`R-100180`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp``
    property ``instance_ip_address``
    parameter associated with an internal network, i.e.,

     * ``{vm-type}_int_{network-role}_ip_{index}``
     * ``{vm-type}_int_{network-role}_v6_ip_{index}``
     * ``{vm-type}_int_{network-role}_ips``
     * ``{vm-type}_int_{network-role}_v6_ips``


    **MUST** be enumerated in the Heat Orchestration
    Template's Environment File and IP addresses **MUST** be
    assigned.


Contrail Resource Parameters > Resource OS::ContrailV2::InstanceIp > Resource OS::ContrailV2::InstanceIp Property subnet_uuid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-100190`

    The VNF's Heat Orchestration Template's
    resource ``OS::ContrailV2::InstanceIp`` property ``subnet_uuid``
    parameter
    **MUST** be declared type ``string``.


.. container:: note

    :need:`R-100200`

    When the VNF's Heat Orchestration Template's
    resource ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an external network (per the ONAP definition, see
    Requirement R-57424),
    and an IPv4 address is being cloud assigned by OpenStack's DHCP Service
    and the external network IPv4 subnet is to be specified
    using the property ``subnet_uuid``, the parameter
    **MUST** follow the naming convention

      * ``{network-role}_subnet_id``

    where

      * ``{network-role}`` is the network role of the network.


.. container:: note

    :need:`R-100210`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` property ``subnet_uuid``
    parameter
    ``{network-role}_subnet_id``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-100220`

    When the VNF's Heat Orchestration Template's
    resource ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an external network (per the ONAP definition, see
    Requirement R-57424),
    and an IPv6 address is being cloud assigned by OpenStack's DHCP Service
    and the external network IPv6 subnet is to be specified
    using the property ``subnet_uuid``, the parameter
    **MUST** follow the naming convention

      * ``{network-role}_v6_subnet_id``

    where

      * ``{network-role}`` is the network role of the network.


.. container:: note

    :need:`R-100230`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` property ``subnet_uuid``
    parameter
    ``{network-role}_v6_subnet_id``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-100240`

    When

      * the VNF's Heat Orchestration Template's
        resource ``OS::ContrailV2::InstanceIp`` in an Incremental Module is
        assigning an IP address
        to an internal network (per the ONAP definition, see
        Requirements R-52425 and R-46461)
        that is created in the Base Module, AND
      * an IPv4 address is being cloud assigned by OpenStack's DHCP Service AND
      * the internal network IPv4 subnet is to be specified
        using the property ``subnet_uuid``,

    the parameter **MUST** follow the naming convention

      * ``int_{network-role}_subnet_id``

    where

      * ``{network-role}`` is the network role of the internal network

    Note that the parameter **MUST** be defined as an ``output`` parameter in
    the base module.


.. container:: note

    :need:`R-100250`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` property ``subnet_uuid``
    parameter
    ``int_{network-role}_subnet_id``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-100260`

    When

      * the VNF's Heat Orchestration Template's
        resource ``OS::ContrailV2::InstanceIp`` in an Incremental Module is
        attaching
        to an internal network (per the ONAP definition,
        see Requirements R-52425 and R-46461)
        that is created in the Base Module, AND
      * an IPv6 address is being cloud assigned by OpenStack's DHCP Service AND
      * the internal network IPv6 subnet is to be specified
        using the property ``subnet_uuid``,

    the parameter **MUST** follow the naming convention
    ``int_{network-role}_v6_subnet_id``,
    where ``{network-role}`` is the network role of the internal network.

    Note that the parameter **MUST** be defined as an ``output`` parameter in
    the base module.


.. container:: note

    :need:`R-100270`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` property ``subnet_uuid``
    parameter
    ``int_{network-role}_v6_subnet_id``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


Monitoring & Management > Data Structure Specification of the Event Record
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-120182`

    The VNF or PNF provider **MUST** indicate specific conditions that may arise, and
    recommend actions that may be taken at specific thresholds, or if specific
    conditions repeat within a specified time interval, using the semantics and
    syntax described by the :ref:`VES Event Registration specification <ves_event_registration_3_2>`.


.. container:: note

    :need:`R-570134`

    The events produced by the VNF or PNF **MUST** must be compliant with the common
    event format defined in the
    :ref:`VES Event Listener<ves_event_listener_7_1>`
    specification.


.. container:: note

    :need:`R-520802`

    The VNF or PNF provider **MUST** provide a YAML file formatted in adherence with
    the :ref:`VES Event Registration specification <ves_event_registration_3_2>`
    that defines the following information for each event produced by the VNF:

    * ``eventName``
    * Required fields
    * Optional fields
    * Any special handling to be performed for that event


.. container:: note

    :need:`R-123044`

    The VNF or PNF Provider **MAY** require that specific events, identified by their
    ``eventName``, require that certain fields, which are optional in the common
    event format, must be present when they are published.


Monitoring & Management > Event Records - Data Structure Description > Common Event Header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-528866`

    The VNF **MUST** produce VES events that include the following mandatory
    fields in the common event header.

     * ``domain`` - the event domain enumeration
     * ``eventId`` - the event key unique to the event source
     * ``eventName`` - the unique event name
     * ``lastEpochMicrosec`` - the latest unix time (aka epoch time) associated
       with the event
     * ``priority`` - the processing priority enumeration
     * ``reportingEntityName`` - name of the entity reporting the event or
       detecting a problem in another VNF or PNF
     * ``sequence`` - the ordering of events communicated by an event source
     * ``sourceName`` - name of the entity experiencing the event issue, which
       may be detected and reported by a separate reporting entity
     * ``startEpochMicrosec`` - the earliest unix time (aka epoch time)
       associated with the event
     * ``version`` - the version of the event header
     * ``vesEventListenerVersion`` - Version of the VES event listener API spec
       that this event is compliant with


Monitoring & Management > Monitoring & Management Requirements > Addressing and Delivery Protocol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-84879`

    The VNF or PNF **MUST** have the capability of maintaining a primary
    and backup DNS name (URL) for connecting to ONAP collectors, with the
    ability to switch between addresses based on conditions defined by policy
    such as time-outs, and buffering to store messages until they can be
    delivered. At its discretion, the service provider may choose to populate
    only one collector address for a VNF or PNF. In this case, the network will
    promptly resolve connectivity problems caused by a collector or network
    failure transparently to the VNF or PNF.


.. container:: note

    :need:`R-88482`

    The VNF or PNF **SHOULD** use REST using HTTPS delivery of plain
    text JSON for moderate sized asynchronous data sets, and for high
    volume data sets when feasible.


.. container:: note

    :need:`R-81777`

    The VNF or PNF **MUST** be configured with initial address(es) to use
    at deployment time. Subsequently, address(es) may be changed through
    ONAP-defined policies delivered from ONAP to the VNF or PNF using PUTs to a
    RESTful API, in the same manner that other controls over data reporting
    will be controlled by policy.


.. container:: note

    :need:`R-79412`

    The VNF or PNF **MAY** use another option which is expected to include TCP
    for high volume streaming asynchronous data sets and for other high volume
    data sets. TCP delivery can be used for either JSON or binary encoded data
    sets.


.. container:: note

    :need:`R-01033`

    The VNF or PNF **MAY** use another option which is expected to include SFTP
    for asynchronous bulk files, such as bulk files that contain large volumes
    of data collected over a long time interval or data collected across many
    VNFs or PNFs. (Preferred is to reorganize the data into more frequent or more focused
    data sets, and deliver these by REST or TCP as appropriate.)


.. container:: note

    :need:`R-03070`

    The VNF or PNF **MUST**, by ONAP Policy, provide the ONAP addresses
    as data destinations for each VNF or PNF, and may be changed by Policy while
    the VNF or PNF is in operation. We expect the VNF or PNF to be capable of redirecting
    traffic to changed destinations with no loss of data, for example from
    one REST URL to another, or from one TCP host and port to another.


.. container:: note

    :need:`R-08312`

    The VNF or PNF **MAY** use another option which is expected to include REST
    delivery of binary encoded data sets.


.. container:: note

    :need:`R-63229`

    The VNF or PNF **MAY** use another option which is expected to include REST
    for synchronous data, using RESTCONF (e.g., for VNF or PNF state polling).


Monitoring & Management > Monitoring & Management Requirements > Asynchronous and Synchronous Data Delivery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-73285`

    The VNF or PNF **MUST** must encode, address and deliver the data
    as described in the previous paragraphs.


.. container:: note

    :need:`R-06924`

    The VNF or PNF **MUST** deliver asynchronous data as data becomes
    available, or according to the configured frequency.


.. container:: note

    :need:`R-86586`

    The VNF or PNF **MUST** use the YANG configuration models and RESTCONF
    [RFC8040] (https://tools.ietf.org/html/rfc8040).


.. container:: note

    :need:`R-70266`

    The VNF or PNF **MUST** respond to an ONAP request to deliver the
    current data for any of the record types defined in
    `Event Records - Data Structure Description`_ by returning the requested
    record, populated with the current field values. (Currently the defined
    record types include fault fields, mobile flow fields, measurements for
    VNF or PNF scaling fields, and syslog fields. Other record types will be added
    in the future as they become standardized and are made available.)


.. container:: note

    :need:`R-34660`

    The VNF or PNF **MUST** use the RESTCONF/NETCONF framework used by
    the ONAP configuration subsystem for synchronous communication.


.. container:: note

    :need:`R-332680`

    The VNF or PNF **SHOULD** deliver all syslog messages to the VES Collector per the
    specifications in Monitoring and Management chapter.


.. container:: note

    :need:`R-46290`

    The VNF or PNF **MUST** respond to an ONAP request to deliver granular
    data on device or subsystem status or performance, referencing the YANG
    configuration model for the VNF or PNF by returning the requested data elements.


.. container:: note

    :need:`R-42140`

    The VNF or PNF **MUST** respond to data requests from ONAP as soon
    as those requests are received, as a synchronous response.


.. container:: note

    :need:`R-11240`

    The VNF or PNF **MUST** respond with content encoded in JSON, as
    described in the RESTCONF specification. This way the encoding of a
    synchronous communication will be consistent with Avro.


.. container:: note

    :need:`R-43327`

    The VNF or PNF **SHOULD** use `Modeling JSON text with YANG
    <https://tools.ietf.org/html/rfc7951>`_, If YANG models need to be
    translated to and from JSON{RFC7951]. YANG configuration and content can
    be represented via JSON, consistent with Avro, as described in "Encoding
    and Serialization" section.


Monitoring & Management > Monitoring & Management Requirements > Bulk Performance Measurement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-807129`

    The VNF or PNF **SHOULD** report the files in FileReady for as long as they are
    available at VNF or PNF.

    Note: Recommended period is at least 24 hours.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-841740`

    The VNF or PNF **SHOULD** support FileReady VES event for event-driven bulk transfer
    of monitoring data.


.. container:: note

    :need:`R-440220`

    The VNF or PNF **SHOULD** support File transferring protocol, such as FTPES or SFTP,
    when supporting the event-driven bulk transfer of monitoring data.


.. container:: note

    :need:`R-75943`

    The VNF or PNF **SHOULD** support the data schema defined in 3GPP TS 32.435, when
    supporting the event-driven bulk transfer of monitoring data.


Monitoring & Management > Monitoring & Management Requirements > Google Protocol Buffers (GPB)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-257367`

    The VNF or PNF, when leveraging Google Protocol Buffers for events, **MUST**
    serialize the events using native Google Protocol Buffers (GPB) according
    to the following guidelines:

       * The keys are represented as integers pointing to the system resources
         for the VNF or PNF being monitored
       * The values correspond to integers or strings that identify the
         operational state of the VNF resource, such a statistics counters and
         the state of an VNF or PNF resource.
       * The required Google Protocol Buffers (GPB) metadata is provided in the
         form of .proto files.


.. container:: note

    :need:`R-978752`

    The VNF or PNF providers **MUST** provide the Service Provider the following
    artifacts to support the delivery of high-volume VNF or PNF telemetry to
    DCAE via GPB over TLS/TCP:

       * A valid VES Event .proto definition file, to be used validate and
         decode an event
       * A valid high volume measurement .proto definition file, to be used for
         processing high volume events
       * A supporting PM content metadata file to be used by analytics
         applications to process high volume measurement events


Monitoring & Management > Monitoring & Management Requirements > JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-19624`

    The VNF or PNF, when leveraging JSON for events, **MUST** encode and serialize
    content delivered to ONAP using JSON (RFC 7159) plain text format.
    High-volume data is to be encoded and serialized using
    `Avro <http://avro.apache.org/>`_, where the Avro data
    format are described using JSON.


Monitoring & Management > Monitoring & Management Requirements > Reporting Frequency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-98191`

    The VNF or PNF **MUST** vary the frequency that asynchronous data
    is delivered based on the content and how data may be aggregated or
    grouped together.

        Note:

        - For example, alarms and alerts are expected to be delivered as
          soon as they appear. In contrast, other content, such as performance
          measurements, KPIs or reported network signaling may have various
          ways of packaging and delivering content. Some content should be
          streamed immediately; or content may be monitored over a time
          interval, then packaged as collection of records and delivered
          as block; or data may be collected until a package of a certain
          size has been collected; or content may be summarized statistically
          over a time interval, or computed as a KPI, with the summary or KPI
          being delivered.
        - We expect the reporting frequency to be configurable depending on
          the virtual network functions needs for management. For example,
          Service Provider may choose to vary the frequency of collection
          between normal and trouble-shooting scenarios.
        - Decisions about the frequency of data reporting will affect
          the size of delivered data sets, recommended delivery method,
          and how the data will be interpreted by ONAP. These considerations
          should not affect deserialization and decoding of the data, which
          will be guided by the accompanying JSON schema or GPB definition
          files.


.. container:: note

    :need:`R-146931`

    The VNF or PNF **MUST** report exactly one Measurement event per period
    per source name.


Monitoring & Management > Monitoring & Management Requirements > Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-42366`

    The VNF or PNF **MUST** support secure connections and transports such as
    Transport Layer Security (TLS) protocol
    [`RFC5246 <https://tools.ietf.org/html/rfc5246>`_] and should adhere to
    the best current practices outlined in
    `RFC7525 <https://tools.ietf.org/html/rfc7525>`_.


.. container:: note

    :need:`R-44290`

    The VNF or PNF **MUST** control access to ONAP and to VNFs or PNFs, and creation
    of connections, through secure credentials, log-on and exchange mechanisms.


.. container:: note

    :need:`R-894004`

    When the VNF or PNF sets up a HTTP or HTTPS connection to the collector, it **MUST**
    provide a username and password to the DCAE VES Collector for HTTP Basic
    Authentication.

    Note: HTTP Basic Authentication has 4 steps: Request, Authenticate,
    Authorization with Username/Password Credentials, and Authentication Status
    as per RFC7617 and RFC 2617.


.. container:: note

    :need:`R-01427`

    The VNF or PNF **MUST** support the provisioning of security and authentication
    parameters (HTTP username and password) in order to be able to authenticate
    with DCAE (in ONAP).

    Note: In R3, a username and password are used with the DCAE VES Event
    Listener which are used for HTTP Basic Authentication.

    Note: The configuration management and provisioning software are specific
    to a vendor architecture.


.. container:: note

    :need:`R-68165`

    The VNF or PNF **MUST** encrypt any content containing Sensitive Personal
    Information (SPI) or certain proprietary data, in addition to applying the
    regular procedures for securing access and delivery.


.. container:: note

    :need:`R-47597`

    The VNF or PNF **MUST** carry data in motion only over secure connections.


Monitoring & Management > Monitoring & Management Requirements > VNF telemetry via standardized interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-821473`

    The VNF or PNF MUST produce heartbeat indicators consisting of events containing
    the common event header only per the VES Listener Specification.


Monitoring & Management > Transports and Protocols Supporting Resource Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-821839`

    The VNF or PNF **MUST** deliver event records to ONAP using the common
    transport mechanisms and protocols defined in this specification.


.. container:: note

    :need:`R-798933`

    The VNF or PNF **SHOULD** deliver event records that fall into the event domains
    supported by VES.


.. container:: note

    :need:`R-932071`

    The VNF or PNF provider **MUST** reach agreement with the Service Provider on
    the selected methods for encoding, serialization and data delivery
    prior to the on-boarding of the VNF or PNF into ONAP SDC Design Studio.


Monitoring & Management > Transports and Protocols Supporting Resource Interfaces > Bulk Telemetry Transmission



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-908291`

    The VNF or PNF **MAY** leverage bulk VNF or PNF telemetry transmission mechanism, as
    depicted in Figure 4, in instances where other transmission methods are not
    practical or advisable.


Monitoring & Management > Transports and Protocols Supporting Resource Interfaces > VNF or PNF Telemetry using Google Protocol Buffers



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-697654`

    The VNF or PNF **MAY** leverage the Google Protocol Buffers (GPB) delivery model
    depicted in Figure 3 to support real-time performance management (PM) data.
    In this model the VES events are streamed as binary-encoded GBPs over via
    TCP sockets.


Monitoring & Management > Transports and Protocols Supporting Resource Interfaces > VNF or PNF Telemetry using VES/JSON Model



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-659655`

    The VNF or PNF **SHOULD** leverage the JSON-driven model, as depicted in Figure 2,
    for data delivery unless there are specific performance or operational
    concerns agreed upon by the Service Provider that would warrant using an
    alternate model.


ONAP Heat Heat Template Constructs > Heat Files Support (get_file)



Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-87848

    When using the intrinsic function get_file, ONAP does not support
    a directory hierarchy for included files. All files must be in a
    single, flat directory per VNF. A VNF's Heat Orchestration
    Template's ``get_file`` target files **MUST** be in the same
    directory hierarchy as the VNF's Heat Orchestration Templates.


ONAP Heat Heat Template Constructs > Key Pairs



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-100380`

    If a VNF requires the use of an SSH key created by OpenStack, the VNF
    Heat Orchestration Template **SHOULD** create the ``OS::Nova::Keypair``
    in the base module, and expose the public key as an output value.

    This allows re-use of the key by ONAP when triggering scale out, recovery,
    or other day 1 operations.


ONAP Heat Heat Template Constructs > Nested Heat Templates > Nested Heat Template Requirements



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-708564`

    If a VNF's Heat Orchestration Template's resource invokes a nested
    YAML file, either statically or dynamically
    (via ``OS::Heat::ResourceGroup``),
    the names of the parameters associated with the following resource
    properties **MUST NOT** change.

    * ``OS::Nova::Server`` property ``flavor``
    * ``OS::Nova::Server`` property ``image``
    * ``OS::Nova::Server`` property ``name``
    * ``OS::Nova::Server`` property metadata key value ``vnf_id``
    * ``OS::Nova::Server`` property metadata key value ``vf_module_id``
    * ``OS::Nova::Server`` property metadata key value ``vnf_name``
    * ``OS::Nova::Server`` property metadata key value ``vf_module_name``
    * ``OS::Nova::Server`` property metadata key value ``vm_role``
    * ``OS::Nova::Server`` property metadata key value ``vf_module_index``
    * ``OS::Nova::Server`` property metadata key value ``workload_context``
    * ``OS::Nova::Server`` property metadata key value ``environment_context``
    * ``OS::Neutron::Port`` property ``fixed_ips``, map property ``ip_address``
    * ``OS::Neutron::Port`` property ``fixed_ips``, map property ``subnet``
    * ``OS::Neutron::Port`` property ``allowed_address_pairs``, map property
      ``ip_address``
    * ``OS::Neutron::Port`` property ``network``
    * ``OS::ContrailV2::VirtualMachineInterface`` property
      ``virtual_network_refs``
    * ``OS::ContrailV2::VirtualMachineInterface`` property
      ``virtual_machine_interface_allowed_address_pairs``, map property
      ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair``,
      ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip``
      ,
      ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``
    * ``OS::ContrailV2::InstanceIP`` property ``instance_ip_address``
    * ``OS::ContrailV2::InstanceIP`` property ``subnet_uuid``


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-52530

    A VNF's Heat Orchestration Template's Nested YAML file
    **MUST** be in the same directory hierarchy as the VNF's Heat
    Orchestration Templates.


.. container:: note

    R-70112

    A VNF's Heat Orchestration Template **MUST** reference a Nested YAML
    file by name. The use of ``resource_registry`` in the VNF's Heat
    Orchestration Templates Environment File **MUST NOT** be used.


ONAP Heat Networking > External Networks



Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-83015

    A VNF's ``{network-role}`` assigned to an external network **MUST**
    be different than the ``{network-role}`` assigned to the VNF's
    internal networks, if internal networks exist.


ONAP Heat Networking > Internal Networks



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-35666`

    If a VNF has an internal network, the VNF Heat Orchestration Template
    **MUST** include the heat resources to create the internal network.

    A VNF's Internal Network is created using Neutron Heat Resources
    (i.e., ``OS::Neutron::Net``, ``OS::Neutron::Subnet``) and/or
    Contrail Heat Resources (i.e., ``OS::ContrailV2::VirtualNetwork``,
    ``ContrailV2::NetworkIpam``).


.. container:: note

    :need:`R-22688`

    When a VNF's Heat Orchestration Template creates an internal network
    (per the ONAP definition, see Requirements R-52425 and R-46461
    and R-35666) and the internal network needs to be shared between modules
    within a VNF,  the internal network **MUST** be created either in the

    * the base module
    * a nested YAML file invoked by the base module

    and the base module **MUST** contain an output parameter that provides
    either the network UUID or network name.

    * If the network UUID value is used to reference the network, the output
      parameter name in the base module **MUST** follow the naming convention
      ``int_{network-role}_net_id``
    * If the network name in is used to reference the network, the output
      parameter name in the base template **MUST** follow the naming convention
      ``int_{network-role}_net_name``

    ``{network-role}`` **MUST** be the network-role of the internal network
    created in the Base Module.

    The Base Module Output Parameter MUST be declared in the ``parameters:``
    section of the Incremental Module(s) where the ``OS::Neutron::Port``
    resource(s) is attaching to the internal network.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-32025

    When a VNF creates two or more internal networks, each internal
    network **MUST** be assigned a unique ``{network-role}`` in the context
    of the VNF for use in the VNF's Heat Orchestration Template.


.. container:: note

    R-68936

    When a VNF creates an internal network, a network role, referred to as
    the ``{network-role}`` **MUST** be assigned to the internal network
    for use in the VNF's Heat Orchestration Template.


.. container:: note

    R-69874

    A VNF's ``{network-role}`` assigned to an internal network **MUST**
    be different than the ``{network-role}`` assigned to the VNF's external
    networks.


ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > parameters > constraints



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-00011`

    A VNF's Heat Orchestration Template's parameter defined
    in a nested YAML file
    **SHOULD NOT** have a parameter constraint defined.


.. container:: note

    :need:`R-88863`

    A VNF's Heat Orchestration Template's parameter defined
    in a non-nested YAML file as type
    ``number`` **MAY** have a parameter constraint defined.


ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > resources > properties



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-10834`

    A VNF's Heat Orchestration Template resource attribute ``property:``
    **MUST NOT** use more than two levels of nested ``get_param`` intrinsic
    functions when deriving a property value.  SDC does not support nested
    ``get_param`` with recursive lists (i.e., a list inside list).
    The second ``get_param`` in a nested lookup must directly derive its value
    without further calls to ``get_param`` functions.

    * Example of valid nesting:

      * ``name: {get_param: [ {vm-type}_names, {get_param : index } ] }``

    * Examples of invalid nesting.  SDC will not support these examples since
      there is an array inside array.

      * ``name: {get_param: [ {vm-type}_names, { get_param: [ indexlist, 0 ] } ] }``
      * ``name: {get_param: [ {vm-type}_names, { get_param: [ indexlist1, { get_param: indexlist2 } ] } ] }``


ONAP Heat Orchestration Templates Overview > ONAP Heat Orchestration Template Filenames > Base Modules



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-81339`

    A VNF Heat Orchestration Template's Base Module file name **MUST** include
    case insensitive 'base' in the filename and
    **MUST** match one of the following four
    formats:

     1.) ``base_<text>.y[a]ml``

     2.) ``<text>_base.y[a]ml``

     3.) ``base.y[a]ml``

     4.) ``<text>_base_<text>``.y[a]ml

    where ``<text>`` **MUST** contain only alphanumeric characters and
    underscores '_' and **MUST NOT** contain the case insensitive string
    ``base`` or ``volume``.


ONAP Heat Orchestration Templates Overview > ONAP Heat Orchestration Template Filenames > Cinder Volume Modules



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-589037`

    A VNF Heat Orchestration Template's Cinder Volume Module ``resources:``
    section
    **MUST** only be defined using one of the following:

    * one of more ``OS::Cinder::Volume`` resources
    * one or more ``OS::Heat::ResourceGroup`` resources that call a nested YAML
      file that contains only ``OS::Cinder::Volume`` resources
    * a resource that calls a nested YAML file (static nesting) that contains
      only ``OS::Cinder::Volume`` resources


ONAP Heat Orchestration Templates Overview > ONAP Heat Orchestration Template Filenames > Incremental Modules



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-87247`

    VNF Heat Orchestration Template's Incremental Module file name
    **MUST** contain only alphanumeric characters and underscores
    '_' and **MUST NOT** contain the case insensitive string ``base``.


ONAP Heat Orchestration Templates Overview > ONAP Heat Orchestration Template Filenames > Nested Heat file



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-76057`

    VNF Heat Orchestration Template's Nested YAML file name **MUST** contain
    only alphanumeric characters and underscores '_' and
    **MUST NOT** contain the case insensitive string ``base``.


ONAP Heat Orchestration Templates Overview > ONAP VNF Modularity Overview



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-90748`

    A VNF's Heat Orchestration Template's Resource ``OS::Cinder::Volume``
    **MAY** be defined in an Incremental Module.


.. container:: note

    :need:`R-03251`

    A VNF's Heat Orchestration Template's Resource ``OS::Cinder::Volume``
    **MAY** be defined in a Cinder Volume Module.


.. container:: note

    :need:`R-46119`

    A VNF's Heat Orchestration Template's Resource ``OS::Cinder::Volume``
    **MAY** be defined in a Base Module.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-20974

    At orchestration time, the VNF's Base Module **MUST**
    be deployed first, prior to any incremental modules.


ONAP Heat Orchestration Templates Overview > ONAP VNF On-Boarding



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-348813`

    The VNF's Heat Orchestration Template's ZIP file **MUST NOT** include
    a binary image file.


.. container:: note

    :need:`R-511776`

    When a VNF's Heat Orchestration Template is ready
    to be on-boarded to ONAP,
    all files composing the VNF Heat Orchestration Template
    **MUST** be placed in a flat (i.e., non-hierarchical) directory and
    archived using ZIP.  The resulting ZIP file is uploaded into ONAP.


ONAP Heat Orchestration Templates Overview > Output Parameters > ONAP Base Module Output Parameters



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-52753`

    VNF's Heat Orchestration Template's Base Module's output parameter's
    name and type **MUST** match the VNF's Heat Orchestration Template's
    incremental Module's name and type.


.. container:: note

    :need:`R-22608`

    When a VNF's Heat Orchestration Template's Base Module's output
    parameter is declared as an input parameter in an Incremental Module,
    the parameter attribute ``constraints:`` **SHOULD NOT** be declared.


ONAP Heat Orchestration Templates Overview > Output Parameters > ONAP Volume Module Output Parameters



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-20547`

    When an ONAP Volume Module Output Parameter is declared as an input
    parameter in a base or an incremental module Heat Orchestration
    Template, parameter constraints **SHOULD NOT** be declared.


.. container:: note

    :need:`R-07443`

    A VNF's Heat Orchestration Templates' Cinder Volume Module Output
    Parameter's name and type **MUST** match the input parameter name and type
    in the corresponding Base Module or Incremental Module.


.. container:: note

    :need:`R-89913`

    A VNF's Heat Orchestration Template's Cinder Volume Module Output
    Parameter(s)
    **MUST** include the
    UUID(s) of the Cinder Volumes created in template.


ONAP Heat Support of Environment Files



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-599443`

    A parameter enumerated in a
    VNF's Heat Orchestration Template's environment file **MUST** be declared
    in the
    corresponding VNF's Heat Orchestration Template's YAML file's
    ``parameters:`` section.


ONAP Heat VNF Modularity



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-61001`

    A shared Heat Orchestration Template resource is a resource that **MUST**
    be defined in the base module and will be referenced by one or
    more resources in one or more incremental modules.

    The UUID of the shared resource (created in the base module) **MUST** be
    exposed by declaring a parameter in the
    ``outputs`` section of the base module.

    For ONAP to provided the UUID value of the shared resource to the
    incremental module, the parameter name defined in the ``outputs``
    section of the base module **MUST** be defined as a parameter
    in the ``parameters`` section of the incremental module.

    ONAP will capture the output parameter name and value in the base module
    and provide the value to the corresponding parameter(s) in the
    incremental module(s).


ONAP TOSCA VNFD Requirements > VNF CSAR Package > VNF Package Contents



Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-26885

    The VNF provider **MUST** provide the binaries and images needed to
    instantiate the VNF (VNF and VNFC images) either as:

      - Local artifact in CSAR: ROOT\\Artifacts\\ **VNF_Image.bin**

      - externally referred (by URI) artifact in Manifest file (also may be
        referred by VNF Descriptor)

    Note: Currently, ONAP doesn't have the capability of Image management,
    we upload the image into VIM/VNFM manually.


ONAP TOSCA VNFD or PNFD Requirements > TOSCA PNF Descriptor > Capability Types



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-177937`

    The PNFD provided by a PNF vendor **MUST** comply with the following
    Capabilities Types as specified in ETSI NFV-SOL001 standard:

      - tosca.datatypes.nfv.VirtualLinkable


ONAP TOSCA VNFD or PNFD Requirements > TOSCA PNF Descriptor > Data Types



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-484843`

    The PNFD provided by a PNF vendor **MUST** comply with the following Data
    Types as specified in ETSI NFV-SOL001 standard:

      - tosca.datatypes.nfv.CpProtocolData

      - tosca.datatypes.nfv.AddressData

      - tosca.datatypes.nfv.L2AddressData

      - tosca.datatypes.nfv.L3AddressData

      - tosca.datatypes.nfv.LocationInfo

      - tosca.datatypes.nfv.CivicAddressElement


ONAP TOSCA VNFD or PNFD Requirements > TOSCA PNF Descriptor > General



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-24632`

    The PNF Descriptor (PNFD) provided by PNF vendor **MUST** comply with
    TOSCA/YAML based Service template for PNF descriptor specified in ETSI
    NFV-SOL001.


ONAP TOSCA VNFD or PNFD Requirements > TOSCA PNF Descriptor > Node Types



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-535009`

    The PNFD provided by a PNF vendor **MUST** comply with the following Node
    Types as specified in ETSI NFV-SOL001 standard:

      - tosca.nodes.nfv.PNF

      - tosca.nodes.nfv.PnfExtCp

      - tosca.nodes.nfv.Cp


ONAP TOSCA VNFD or PNFD Requirements > TOSCA PNF Descriptor > Policy Types



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-596064`

    The PNFD provided by a PNF vendor **MUST** comply with the following Policy
    Types as specified in ETSI NFV-SOL001 standard:

      - tosca.datatypes.nfv.SecurityGroupRule


ONAP TOSCA VNFD or PNFD Requirements > TOSCA PNF Descriptor > Relationship Types



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-64064`

    The PNFD provided by a PNF vendor **MUST** comply with the following
    Relationship Types as specified in ETSI NFV-SOL001 standard:

      - tosca.datatypes.nfv.VirtualLinksTo


ONAP TOSCA VNFD or PNFD Requirements > TOSCA VNF Descriptor > General



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-65486`

    The VNFD **MUST** comply with ETSI GS NFV-SOL001 specification endorsing
    the above mentioned NFV Profile and maintaining the gaps with the
    requirements specified in ETSI GS NFV-IFA011 standard.


ONAP TOSCA VNFD or PNFD Requirements > VNF or PNF CSAR Package > VNF Package Contents



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-146092`

    If one or more non-MANO artifact(s) is included in the VNF or PNF TOSCA CSAR
    package, the Manifest file in this CSAR package **MUST** contain: non-MANO
    artifact set which MAY contain following ONAP public tag.

      - onap_ves_events: contains VES registration files

      - onap_pm_dictionary: contains the PM dictionary files

      - onap_yang_modules: contains Yang module files for configurations

      - onap_ansible_playbooks: contains any ansible_playbooks

      - onap_others: contains any other non_MANO artifacts, e.g. informational
        documents


.. container:: note

    :need:`R-221914`

    The VNF or PNF package **MUST** contain a a human-readable change log text
    file. The Change Log file keeps a history describing any changes in the VNF
    or PNF package. The Change Log file is kept up to date continuously from
    the creation of the CSAR package.


.. container:: note

    :need:`R-293901`

    The VNF or PNF CSAR PACKAGE with TOSCA-Metadata **MUST** include following
    additional keywords pointing to TOSCA files:

      - ETSI-Entry-Manifest

      - ETSI-Entry-Change-Log

    Note: For a CSAR containing a TOSCA-Metadata directory, which includes
    the TOSCA.meta metadata file. The TOSCA.meta metadata file includes block_0
    with the Entry-Definitions keyword pointing to a TOSCA definitions YAML
    file used as entry for parsing the contents of the overall CSAR archive.


.. container:: note

    :need:`R-57019`

    The PNF TOSCA CSAR PACKAGE Manifest file **MUST** start with the PNF
    package metadata in the form of a name-value pairs. Each pair shall appear
    on a different line. The name is specified as following:

      - pnfd_provider

      - pnfd_name

      - pnfd_release_date_time

      - pnfd_archive_version


.. container:: note

    :need:`R-795126`

    The VNF TOSCA CSAR package Manifest file **MUST** start with the VNF
    package metadata in the form of a name-value pairs. Each pair shall appear
    on a different line. The name is specified as following:

      - vnf_provider_id

      - vnf_product_name

      - vnf_release_date_time

      - vnf_package_version


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-10087`

    The VNF or PNF CSAR package **MUST** include all artifacts required by
    ETSI GS NFV-SOL004 including Manifest file, VNFD or PNFD (or Main
    TOSCA/YAML based Service Template) and other optional artifacts.


.. container:: note

    :need:`R-40820`

    The VNF or PNF TOSCA PACKAGE **MUST** enumerate all of the open source
    licenses their VNF(s) incorporate. CSAR License directory as per ETSI
    SOL004.

    for example ROOT\\Licenses\\ **License_term.txt**


.. container:: note

    :need:`R-01123`

    The VNF or PNF package Manifest file **MUST** contain: VNF or PNF package
    meta-data, a list of all artifacts (both internal and external) entry's
    including their respected URI's, an algorithm to calculate a digest and
    a digest result calculated on the content of each artifacts, as specified
    in ETSI GS NFV-SOL004.


ONAP TOSCA VNFD or PNFD Requirements > VNF or PNF CSAR Package > VNF Package Structure and Format



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-506221`

    The VNF or PNF TOSCA CSAR file **MUST** be a zip file with .csar extension.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-51347`

    The VNF or PNF CSAR package **MUST** be arranged as a CSAR archive as
    specified in TOSCA Simple Profile in YAML 1.2.


.. container:: note

    :need:`R-87234`

    The VNF or PNF package provided by a VNF or PNF vendor **MUST** be with
    TOSCA-Metadata directory (CSAR Option 1) as specified in
    ETSI GS NFV-SOL004.

    **Note:** SDC supports only the CSAR Option 1 in Dublin. The Option 2
    will be considered in future ONAP releases.


ONAP TOSCA VNFD or PNFD Requirements > VNF or PNF CSAR Package > VNF or PNF Package Authenticity and Integrity



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-130206`

    If the VNF or PNF CSAR Package utilizes Option 2 for package security, then
    the complete CSAR file **MUST** contain a Digest (a.k.a. hash) for each of
    the components of the VNF or PNF package. The table of hashes is included
    in the package manifest file, which is signed with the VNF or PNF provider
    private key. In addition, the VNF or PNF provider MUST include a signing
    certificate that includes the VNF or PNF provider public key, following a
    TOSCA pre-defined naming convention and located either at the root of the
    archive or in a predefined location specified by the TOSCA.meta file with
    the corresponding entry named "ETSI-Entry-Certificate".


.. container:: note

    :need:`R-787965`

    If the VNF or PNF CSAR Package utilizes Option 2 for package security, then
    the complete CSAR file **MUST** be digitally signed with the VNF or PNF
    provider private key. The VNF or PNF provider delivers one zip file
    consisting of the CSAR file, a signature file and a certificate file that
    includes the VNF or PNF provider public key. The certificate may also be
    included in the signature container, if the signature format allows that.
    The VNF or PNF provider creates a zip file consisting of the CSAR file with
    .csar extension, signature and certificate files. The signature and
    certificate files must be siblings of the CSAR file with extensions .cms
    and .cert respectively.


PNF Plug and Play > PNF Plug and Play



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-256347`

    The PNF **MUST** support one of the protocols for a Service Configuration
    message exchange between the PNF and PNF Controller (in ONAP):
    a) Netconf/YANG, b) Chef, or c) Ansible.

    Note: The PNF Controller may be VF-C, APP-C or SDN-C based on the
    PNF and PNF domain.


.. container:: note

    :need:`R-106240`

    The following VES Events **SHOULD** be supported by the PNF: pnfRegistration
    VES Event, HVol VES Event, and Fault VES Event. These are onboarded via
    he SDC Design Studio.

    Note: these VES Events are emitted from the PNF to support PNF Plug and
    Play, High Volume Measurements, and Fault events respectively.


Resource IDs



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-11690`

    When a VNF's Heat Orchestration Template's Resource ID contains an
    ``{index}``, the ``{index}`` is a numeric value that **MUST** start at
    zero and **MUST** increment by one.

    As stated in R-16447,
    *a VNF's <resource ID> MUST be unique across all Heat
    Orchestration Templates and all HEAT Orchestration Template
    Nested YAML files that are used to create the VNF*.  While the ``{index}``
    will start at zero in the VNF, the ``{index}`` may not start at zero
    in a given Heat Orchestration Template or HEAT Orchestration Template
    Nested YAML file.


Resource IDs > Contrail Heat Resources Resource ID Naming Convention > OS::ContrailV2::InstanceIp



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-53310`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` Resource ID
    that is configuring an IPv4 Address on a virtual machine interface
    (i.e., OS::ContrailV2::VirtualMachineInterface)
    attached to an external network
    **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_{network-role}_vmi_{vmi_index}_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the network that the
      virtual machine interface is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    * ``IP`` signifies that an IPv4 address is being configured
    * ``{index}`` references the instance of the IPv4 address configured
      on the virtual machine interface.  The ``{index}`` is a numeric value
      that **MUST** start at zero on an
      instance of a virtual machine interface and **MUST** increment by one
      each time a new IPv4 address is configured on the
      virtual machine interface.


.. container:: note

    :need:`R-87563`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` Resource ID
    that is configuring an IPv6 Address on a virtual machine interface
    (i.e., OS::ContrailV2::VirtualMachineInterface)
    attached to an internal network
    **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_int_{network-role}_vmi_{vmi_index}_v6_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the network
      that the port is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    * ``v6_IP`` signifies that an IPv6 address is being configured
    * ``{index}`` references the instance of the IPv6 address configured
      on the virtual machine interface.  The ``{index}`` is a numeric value
      that **MUST** start at zero on an
      instance of a virtual machine interface and **MUST** increment by one
      each time a new IPv6 address is configured on the
      virtual machine interface.


.. container:: note

    :need:`R-62187`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` Resource ID
    that is configuring an IPv4 Address on a virtual machine interface
    (i.e., OS::ContrailV2::VirtualMachineInterface)
    attached to an internal network
    **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_int_{network-role}_vmi_{vmi_index}_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the network
      that the port is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    * ``IP`` signifies that an IPv4 address is being configured
    * ``{index}`` references the instance of the IPv4 address configured
      on the virtual machine interface.  The ``{index}`` is a numeric value
      that **MUST** start at zero on an
      instance of a virtual machine interface and **MUST** increment by one
      each time a new IPv4 address is configured on the
      virtual machine interface.


.. container:: note

    :need:`R-46128`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` Resource ID
    that is configuring an IPv6 Address on a virtual machine interface
    (i.e., OS::ContrailV2::VirtualMachineInterface)
    attached to an external network
    **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_{network-role}_vmi_{vmi_index}_v6_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the network
      that the port is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    * ``v6_IP`` signifies that an IPv6 address is being configured
    * ``{index}`` references the instance of the IPv6 address configured
      on the virtual machine interface.  The ``{index}`` is a numeric value
      that **MUST** start at zero on an
      instance of a virtual machine interface and **MUST** increment by one
      each time a new IPv6 address is configured on the
      virtual machine interface.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-20947

    A VNF's Heat Orchestration Template's Resource ``OS::ContrailV2::InstanceIp``
    that is configuring an IPv4 Address on a sub-interface port attached to a
    sub-interface network Resource ID **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_subint_{network-role}_vmi_{vmi_index}_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` is the instance of the ``{vm-type}``
    * ``{network-role}`` is the network-role of the network
      that the port is attached to
    * ``{vmi_index}`` is the instance of the the virtual machine interface
      (e.g., port)  on the vm-type
      attached to the network of ``{network-role}``
    * ``IP`` signifies that an IPv4 address is being configured
    * ``{index}`` is the index of the IPv4 address


.. container:: note

    R-88540

    A VNF's Heat Orchestration Template's Resource ``OS::ContrailV2::InstanceIp``
    that is configuring an IPv6 Address on a sub-interface port attached to a
    sub-interface network Resource ID **MUST**
    use the naming convention

    *  ``{vm-type}_{vm-type_index}_subint_{network-role}_vmi_{vmi_index}_v6_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` is the instance of the ``{vm-type}``
    * ``{network-role}`` is the network-role of the network
      that the port is attached to
    * ``{vmi_index}`` is the instance of the the virtual machine interface
      (e.g., port)  on the vm-type
      attached to the network of ``{network-role}``
    * ``v6_IP`` signifies that an IPv6 address is being configured
    * ``{index}`` is the index of the IPv6 address


Resource IDs > Contrail Heat Resources Resource ID Naming Convention > OS::ContrailV2::ServiceTemplate



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-14447`

    A VNF's Heat Orchestration Template's Resource ``OS::ContrailV2::ServiceTemplate``
    Resource ID **MAY** use the naming convention

    * ``{vm-type}_RST_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``RST`` signifies that it is the Resource Service Template
    * ``{index}`` is the index.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).


Resource IDs > Contrail Heat Resources Resource ID Naming Convention > OS::ContrailV2::VirtualMachineInterface



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-50468`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualMachineInterface`` Resource ID
    that is attaching to an internal network
    **MUST** use the naming convention

    * ``{vm-type}_{vm-type_index}_int_{network-role}_vmi_{vmi_index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the network
      that the port (i.e. virtual machine interface) is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.


.. container:: note

    :need:`R-96253`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualMachineInterface`` Resource ID
    that is attaching to an external network
    **MUST** use the naming convention

    * ``{vm-type}_{vm-type_index}_{network-role}_vmi_{vmi_index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the network
      that the port (i.e. virtual machine interface) is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-54458

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualMachineInterface`` that is attaching to a sub-interface
    network Resource ID **MUST** use the naming convention

    * ``{vm-type}_{vm-type_index}_subint_{network-role}_vmi_{vmi_index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` is the instance of the ``{vm-type}``
    * ``{network-role}`` is the network-role of the network
      that the port (i.e. virtual machine interface) is attached to
    * ``{vmi_index}`` is the instance of the the vmi on the vm-type
      attached to the network of ``{network-role}``


Resource IDs > Contrail Heat Resources Resource ID Naming Convention > OS::ContrailV2::VirtualNetwork



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-99110`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualNetwork`` Resource ID **MUST** use the naming
    convention

    * ``int_{network-role}_network``

    VNF Heat Orchestration Templates can only create internal networks.
    There is no ``{index}`` after ``{network-role}`` because ``{network-role}``
    **MUST** be unique in the scope of the VNF's
    Heat Orchestration Template.


Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Cinder::Volume



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-87004`

    A VNF's Heat Orchestration Template's Resource
    ``OS::Cinder::Volume``
    Resource ID
    **SHOULD**
    use the naming convention

    * ``{vm-type}_volume_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{index}`` starts at zero and increments by one (as described in R-11690)


Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Cinder::VolumeAttachment



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-86497`

    A VNF's Heat Orchestration Template's Resource
    ``OS::Cinder::VolumeAttachment``
    Resource ID
    **SHOULD**
    use the naming convention

    * ``{vm-type}_volume_attachment_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{index}`` starts at zero and increments by one (as described in R-11690)


Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Heat::ResourceGroup



Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-64197

    A VNF's Heat Orchestration Template's Resource ``OS::Heat::ResourceGroup``
    Resource ID that creates sub-interfaces **MUST** use the naming convention

    * ``{vm-type}_{vm-type_index}_subint_{network-role}_port_{port-index}_subinterfaces``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` is the instance of the ``{vm-type}``
    * ``{network-role}`` is the network-role of the networks
      that the sub-interfaces attach to
    * ``{port-index}`` is the instance of the the port on the vm-type
      attached to the network of ``{network-role}``


Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Neutron::Port



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-68520`

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    that is creating a *Reserve Port* with an IPv6 address Resource ID
    **SHOULD** use the naming convention

    * ``reserve_port_{vm-type}_{network-role}_floating_v6_ip_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{network-role}`` is the network-role of the network
      that the port is attached to
    * ``{index}`` is the instance of the IPv6 *Reserve Port*
      for the vm-type attached to the network of ``{network-role}``.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).


.. container:: note

    :need:`R-27469`

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    that is creating a *Reserve Port* with an IPv4 address Resource ID
    **SHOULD** use the naming convention

    * ``reserve_port_{vm-type}_{network-role}_floating_ip_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{network-role}`` is the network-role of the network
      that the port is attached to
    * ``{index}`` is the instance of the IPv4 *Reserve Port*
      for the vm-type attached to the network of ``{network-role}``.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).


.. container:: note

    :need:`R-26351`

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    that is attaching to an internal network Resource ID **MUST**
    use the naming convention

    * ``{vm-type}_{vm-type_index}_int_{network-role}_port_{port-index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the network
      that the port is attached to
    * ``{port_index}`` references the instance of the port on the ``{vm-type}``
      attached to ``{network-role}`` network.  The
      ``{port_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new port is defined on the instance of the ``{vm-type}`` attached to
      ``{network-role}`` network.


.. container:: note

    :need:`R-20453`

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    that is attaching to an external network Resource ID
    **MUST** use the naming convention

    * ``{vm-type}_{vm-type_index}_{network-role}_port_{port-index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the network
      that the port is attached to
    * ``{port_index}`` references the instance of the port on the ``{vm-type}``
      attached to ``{network-role}`` network.  The
      ``{port_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new port is defined on the instance of the ``{vm-type}`` attached to
      ``{network-role}`` network.


Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Neutron::Subnet



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-59434`

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Subnet``
    Resource ID **SHOULD** use the naming convention

    * ``int_{network-role}_subnet_{index}``

    where

    * ``{network-role}`` is the network-role
    * ``{index}`` is the ``{index}`` of the subnet of the network.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).


Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Nova::Keypair



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-24997`

    A VNF's Heat Orchestration Template's Resource ``OS::Nova::Keypair`` applies to
    one ``{vm-type}`` Resource ID **SHOULD** use the naming convention

    * ``{vm-type}_keypair_{index}``

    where

    * ``{network-role}`` is the network-role
    * ``{index}`` is the ``{index}`` of the keypair.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).


.. container:: note

    :need:`R-65516`

    A VNF's Heat Orchestration Template's Resource ``OS::Nova::Keypair`` applies to
    all Virtual Machines in the VNF, the Resource ID **SHOULD** use the naming
    convention

    * ``{vnf-type}_keypair``

    where

    * ``{vnf-type}`` describes the VNF


Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Nova::Server



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-29751`

    A VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    Resource ID
    **MUST** use the naming convention

    * ``{vm-type}_server_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{index}`` is the index.
      The ``{index}`` **MUST** starts at zero and increment by one
      as described in R-11690.


Resource Property “name”



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-85734`

    If a VNF's Heat Orchestration Template contains the property ``name``
    for a non ``OS::Nova::Server`` resource, the intrinsic function
    ``str_replace`` **MUST** be used in conjunction with the ONAP
    supplied metadata parameter ``vnf_name`` to generate a unique value.
    Additional data **MAY** be used in the ``str_replace`` construct
    to generate a unique value.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-32408

    If a VNF's Heat Orchestration Template property ``name``
    for a non ``OS::Nova::Server`` resource uses the intrinsic function
    ``str_replace`` in conjunction with the ONAP
    supplied metadata parameter ``vnf_name`` and does not create
    a unique value, additional data **MUST** be used in the
    ``str_replace`` to create a unique value, such as ``OS::stack_name``
    and/or the ``OS::Heat::ResourceGroup`` ``index``.


Resource: OS::Neutron::Port - Parameters > Introduction > Items to Note



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-681859`

    A VNF's Heat Orchestration Template's ``OS::Neutron::Port`` resource's

    * Resource ID (defined in R-20453)
    * property ``network`` parameter name (defined in R-62983 and
      R-86182)
    * property ``fixed_ips``, map property ``ip_address`` parameter name
      (defined in R-40971, R-04697, R-71577, R-23503, R-78380, R-85235,
      R-27818, and R-29765)
    * property ``fixed_ips``, map property ``subnet`` parameter name
      (defined in R-62802, R-15287, R-84123, R-76160)
    * property ``allowed_address_pairs`` parameter name (defined in
      R-41492 and R-83418)

    **MUST** contain the identical ``{network-role}``.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-07577

    If the VNF's ports connected to a unique network (internal or external)
    and the port's IP addresses are cloud assigned IP Addresses,
    all the IPv4 Addresses **MUST** be from
    the same subnet and all the IPv6 Addresses **MUST** be from the
    same subnet.


.. container:: note

    R-13841

    A VNF **MAY** have one or more ports connected to a unique
    internal network. All VNF ports connected to the unique internal
    network **MUST** have cloud assigned IP Addresses
    or **MUST** have statically assigned IP addresses.


.. container:: note

    R-93272

    A VNF **MAY** have one or more ports connected to a unique
    external network. All VNF ports connected to the unique external
    network **MUST** have cloud assigned IP Addresses
    or **MUST** have ONAP SDN-C assigned IP addresses.


Resource: OS::Neutron::Port - Parameters > Property: allowed_address_pairs, Map Property: ip_address



Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-62300

    If a VNF has two or more ports that require a Virtual IP Address (VIP),
    a VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``allowed_address_pairs``
    map property ``ip_address`` parameter
    **MUST** be used.


Resource: OS::Neutron::Port - Parameters > Property: allowed_address_pairs, Map Property: ip_address > VIP Assignment, External Networks



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-41493`

    When the VNF's Heat Orchestration Template's resource
    ``OS::Neutron::Port`` is attaching to an external network
    (per the ONAP definition, see Requirement R-57424),
    and the IPv4 VIP address and/or IPv6 VIP address
    is **not** supported by the ONAP data model,
    the property ``allowed_address_pairs`` map property ``ip_address``

    * Parameter name **MAY** use any naming convention.  That is, there is no
      ONAP mandatory parameter naming convention.
    * Parameter **MAY** be declared as type ``string`` or type
    ``comma_delimited_list``.

    And the ``OS::Neutron::Port`` resource **MUST** contain
    resource-level ``metadata`` (not property-level).

    And the ``metadata`` format **MUST**  must contain the
    key value ``aap_exempt`` with a list of all
    ``allowed_address_pairs`` map property ``ip_address`` parameters
    **not** supported by the ONAP data model.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-35735`

    When the VNF's Heat Orchestration Template's resource
    ``OS::Neutron::Port`` is attaching to an external network
    (per the ONAP definition, see Requirement R-57424),
    and the IPv6 VIP is required to be supported by the ONAP data model,
    the property ``allowed_address_pairs`` map property ``ip_address``
    parameter name **MUST** follow the naming convention

    * ``{vm-type}_{network-role}_floating_v6_ip``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the external network

    And the parameter **MUST** be declared as type ``string``.

    As noted in the introduction to this section, the ONAP data model
    can only support one IPv6 VIP address.


.. container:: note

    :need:`R-83412`

    If a VNF's Heat Orchestration Template's resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424), the
    property ``allowed_address_pairs``
    map property ``ip_address`` parameter(s)
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-41492`

    When the VNF's Heat Orchestration Template's resource
    ``OS::Neutron::Port`` is attaching to an external network
    (per the ONAP definition, see Requirement R-57424),
    and the IPv4 VIP is required to be supported by the ONAP data model,
    the property ``allowed_address_pairs`` map property ``ip_address``
    parameter name **MUST** follow the naming convention

    * ``{vm-type}_{network-role}_floating_ip``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the external network

    And the parameter **MUST** be declared as type ``string``.

    As noted in the introduction to this section, the ONAP data model
    can only support one IPv4 VIP address.


Resource: OS::Neutron::Port - Parameters > Property: allowed_address_pairs, Map Property: ip_address > VIP Assignment, External Networks, Supported by Automation



Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-10754

    If a VNF has two or more ports that
    attach to an external network that require a Virtual IP Address (VIP),
    and the VNF requires ONAP automation to assign the IP address,
    all the Virtual Machines using the VIP address **MUST**
    be instantiated in the same Base Module Heat Orchestration Template
    or in the same Incremental Module Heat Orchestration Template.


.. container:: note

    R-41956

    If a VNF requires ONAP to assign a Virtual IP (VIP) Address to
    ports connected an external network, the port
    **MUST NOT** have more than one IPv6 VIP address.


.. container:: note

    R-83418

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``allowed_address_pairs``
    map property ``ip_address`` parameter
    ``{vm-type}_{network-role}_floating_v6_ip``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    R-91810

    If a VNF requires ONAP to assign a Virtual IP (VIP) Address to
    ports connected an external network, the port
    **MUST NOT** have more than one IPv4 VIP address.


.. container:: note

    R-98748

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``allowed_address_pairs``
    map property ``ip_address`` parameter
    **MUST** be declared as type ``string``.


Resource: OS::Neutron::Port - Parameters > Property: allowed_address_pairs, Map Property: ip_address > VIP Assignment, Internal Networks



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-717227`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv4 Virtual IP (VIP)
    address is assigned using the property ``allowed_address_pairs``
    map property ``ip_address``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_ip``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as ``type: string``
    and **MUST** be enumerated in the environment file.

    OR

    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as ``type: comma_delimited_list``
    and **MUST** be enumerated in the environment file.


.. container:: note

    :need:`R-805572`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv6 Virtual IP (VIP)
    address is assigned
    using the property ``allowed_address_pairs``
    map property ``ip_address``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_v6_ip``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as ``type: string``
    and **MUST** be enumerated in the environment file

    OR

    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_v6_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as ``type: comma_delimited_list``
    and **MUST** be enumerated in the environment file.


Resource: OS::Neutron::Port - Parameters > Property: fixed_ips, Map Property: ip_address



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-78380`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv4 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is
    defined as a ``string``,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_int_{network-role}_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the
      ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the internal network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one


.. container:: note

    :need:`R-71577`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a string,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_{network-role}_v6_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the
      ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the external network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one


.. container:: note

    :need:`R-40971`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv4 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a string,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_{network-role}_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the external network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one


.. container:: note

    :need:`R-27818`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
    ``string``,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_int_{network-role}_v6_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the internal network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one


Resource: OS::Neutron::Port - Parameters > Property: network



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-86182`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port``
    is in an incremental module and
    is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    the ``network`` parameter name **MUST**

      * follow the naming convention ``int_{network-role}_net_id`` if the
        network UUID value is used to reference the network
      * follow the naming convention ``int_{network-role}_net_name`` if the
        network name in is used to reference the network.

    where ``{network-role}`` is the network-role of the internal network and
    a ``get_param`` **MUST** be used as the intrinsic function.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-93177

    When the VNF's Heat Orchestration Template's resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and the internal network is created in the
    same Heat Orchestration Template as the ``OS::Neutron::Port``,
    the ``network`` property value **MUST** obtain the UUID
    of the internal network by using the intrinsic function
    ``get_resource``
    and referencing the Resource ID of the internal network.


Resource: OS::Nova::Server - Parameters



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-304011`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource's

    * Resource ID (defined in R-29751)
    * property ``image`` parameter name (defined in R-58670)
    * property ``flavor`` parameter name (defined in R-45188)
    * property ``name`` parameter name (defined in R-54171 & R-87817)
    * property ``networks`` map property ``port`` value which is a
      ``OS::Neutron::Port`` Resource ID (defined in R-20453)
      referenced using the intrinsic function ``get_attr``

    **MUST** contain the identical ``{vm-type}``
    and **MUST** follow the naming conventions defined
    in R-58670, R-45188, R-54171, R-87817, and R-29751.  And the ``{index}`` in
    the ``OS::Nova::Server`` Resource ID (defined in R-29751) **MUST** match
    the ``{vm-type_index}`` defined in
    the ``OS::Nova::Server`` property ``networks`` map property ``port``
    referenced ``OS::Neutron::Port`` Resource ID (defined in R-20453).


Resource: OS::Nova::Server - Parameters > Property: Name



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-54171`

    When the VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``name`` parameter is defined as a ``string``,
    the parameter name **MUST** follow the naming convention

    * ``{vm-type}_name_{index}``

    where ``{index}`` is a numeric value that **MUST** start at
    zero in a VNF's Heat Orchestration Template and **MUST** increment by one.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-40899

    When the VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``name`` parameter is defined as a ``string``, a parameter
    **MUST** be delcared for
    each ``OS::Nova::Server`` resource associated with the ``{vm-type}``.


.. container:: note

    R-85800

    When the VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``name`` parameter is defined as a ``comma_delimited_list``,
    a parameter **MUST** be delcared once for all ``OS::Nova::Server`` resources
    associated with the ``{vm-type}``.


Resource: OS::Nova::Server - Parameters > Property: availability_zone



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-98450`

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``availability_zone`` parameter name
    **MUST** follow the naming convention

    * ``availability_zone_{index}``

    where ``{index}`` is a numeric value that **MUST** start at zero
    in a VNF's Heat Orchestration Templates and **MUST**
    increment by one.


Resource: OS::Nova::Server Metadata Parameters > environment_context



Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-62954

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server Resource``
    ``metadata`` map value parameter ``environment_context`` is passed into a
    Nested YAML
    file, the parameter name ``environment_context`` **MUST NOT** change.


Resource: OS::Nova::Server Metadata Parameters > vf_module_id



Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-86237

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vf_module_id`` is passed into a
    Nested YAML
    file, the key/value pair name ``vf_module_id`` **MUST NOT** change.


Resource: OS::Nova::Server Metadata Parameters > vf_module_index



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-100410`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource  property ``metadata`` **MAY**
    contain the key/value pair ``vf_module_index``.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-50816`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource  property ``metadata``
    key/value pair ``vf_module_index``
    value **MUST** be obtained via a ``get_param``.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-22441

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vf_module_index`` is passed into a
    Nested YAML file, the key/value pair
    ``vf_module_index`` **MUST NOT** change.


Resource: OS::Nova::Server Metadata Parameters > vf_module_name



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-100400`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property metadata **SHOULD** contain the key/value pair ``vf_module_name``.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-68023`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vf_module_name``
    value **MUST**
    be obtained via a ``get_param``.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-49177

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vf_module_name`` is passed into a
    Nested YAML
    file, the key/value pair name ``vf_module_name`` **MUST NOT** change.


Resource: OS::Nova::Server Metadata Parameters > vm_role



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-95430`

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource property
    ``metadata`` key/value pair ``vm_role`` value is obtained via
    ``get_param``, the parameter **MAY** be declared as

    * ``vm_role`` and the parameter defined as ``type: string``.
    * ``vm_roles`` and the parameter defined as ``type: comma_delimited_list``.
    * ``{vm-type}_vm_role`` and the parameter defined as ``type: string``.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-70757

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vm_role`` is passed into a Nested
    YAML
    file, the key/value pair name ``vm_role`` **MUST NOT** change.


Resource: OS::Nova::Server Metadata Parameters > vnf_id



Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-44491

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vnf_id`` is passed into a Nested YAML
    file, the key/value pair name ``vnf_id`` **MUST NOT** change.


Resource: OS::Nova::Server Metadata Parameters > vnf_name



Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-16576

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vnf_name`` is passed into a Nested YAML
    file, the key/value pair name ``vnf_name`` **MUST NOT** change.


Resource: OS::Nova::Server Metadata Parameters > workload_context



Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-75202

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``workload_context``
    is passed into a Nested YAML
    file, the key/value pair name ``workload_context`` **MUST NOT** change.


VNF On-boarding and package management > Compute, Network, and Storage Requirements



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-96634`

    The VNF or PNF Provider **MUST** provide human readable documentation
    (not in the on-boarding package) to describe scaling capabilities to manage
    scaling characteristics of the VNF or PNF.


.. container:: note

    :need:`R-26881`

    The VNF provider **MUST** provide the binaries and images
    needed to instantiate the VNF (VNF and VNFC images).


.. container:: note

    :need:`R-35851`

    The VNF HEAT Package **MUST** include VNF topology that describes basic
    network and application connectivity internal and external to the VNF
    including Link type, KPIs, Bandwidth, latency, jitter, QoS (if applicable)
    for each interface.


VNF On-boarding and package management > Licensing Requirements



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-44569`

    The VNF or PNF provider **MUST NOT** require additional
    infrastructure such as a VNF or PNF provider license server for VNF or PNF provider
    functions and metrics.


.. container:: note

    :need:`R-40827`

    The VNF or PNF provider **MUST** enumerate all of the open
    source licenses their VNF or PNF(s) incorporate.


.. container:: note

    :need:`R-44125`

    The VNF or PNF provider **MUST** agree to the process that can
    be met by Service Provider reporting infrastructure. The Contract
    shall define the reporting process and the available reporting tools.


.. container:: note

    :need:`R-97293`

    The VNF or PNF provider **MUST NOT** require audits
    of Service Provider's business.


.. container:: note

    :need:`R-85991`

    The VNF or PNF provider **MUST** provide a universal license key
    per VNF or PNF to be used as needed by services (i.e., not tied to a VM
    instance) as the recommended solution. The VNF or PNF provider may provide
    pools of Unique VNF or PNF License Keys, where there is a unique key for
    each VNF or PNF instance as an alternate solution. Licensing issues should
    be resolved without interrupting in-service VNFs or PNFs.


.. container:: note

    :need:`R-47849`

    The VNF or PNF provider **MUST** support the metadata about
    licenses (and their applicable entitlements) as defined in this
    specification for VNF or PNF software, and any license keys required to authorize
    use of the VNF or PNF software.  This metadata will be used to facilitate
    onboarding the VNF or PNF into the ONAP environment and automating processes
    for putting the licenses into use and managing the full lifecycle of
    the licenses. The details of this license model are described in
    Tables C1 to C8 in the Appendix.

    Note: License metadata support in ONAP is not currently available
    and planned for 1Q 2018.


.. container:: note

    :need:`R-85653`

    The VNF or PNF **MUST** provide metrics (e.g., number of sessions,
    number of subscribers, number of seats, etc.) to ONAP for tracking
    every license.


VNF On-boarding and package management > Resource Configuration



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-89571`

    The VNF or PNF **MUST** support and provide artifacts for configuration
    management using at least one of the following technologies;
    a) Netconf/YANG, b) Chef, or c) Ansible.

    Note: The requirements for Netconf/YANG, Chef, and Ansible protocols
    are provided separately and must be supported only if the corresponding
    protocol option is provided by the VNF or PNF providor.


VNF On-boarding and package management > Resource Configuration > Configuration Management via Ansible



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-75608`

    The VNF or PNF provider **MUST** provide playbooks to be loaded
    on the appropriate Ansible Server.


.. container:: note

    :need:`R-16777`

    The VNF or PNF provider **MUST** provide a JSON file for each
    supported action for the VNF or PNF. The JSON file must contain key value
    pairs with all relevant values populated with sample data that illustrates
    its usage. The fields and their description are defined in Table B1
    in the Appendix.


.. container:: note

    :need:`R-46567`

    The VNF or PNF Package **MUST** include configuration scripts
    for boot sequence and configuration.


.. container:: note

    :need:`R-16065`

    The VNF or PNF provider **MUST** provide configurable parameters
    (if unable to conform to YANG model) including VNF or PNF attributes/parameters
    and valid values, dynamic attributes and cross parameter dependencies
    (e.g., customer provisioning data).


VNF On-boarding and package management > Resource Configuration > Configuration Management via Chef



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-18525`

    The VNF or PNF provider **MUST** provide a JSON file for each
    supported action for the VNF or PNF. The JSON file must contain key value
    pairs with all relevant values populated with sample data that illustrates
    its usage. The fields and their description are defined in Tables A1
    and A2 in the Appendix.

    Note: Chef support in ONAP is not currently available and planned for 4Q 2017.


.. container:: note

    :need:`R-13390`

    The VNF or PNF provider **MUST** provide cookbooks to be loaded
    on the appropriate Chef Server.


VNF On-boarding and package management > Resource Configuration > Configuration Management via NETCONF/YANG



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-30278`

    The VNF or PNF provider **SHOULD** provide a Resource/Device YANG model
    as a foundation for creating the YANG model for configuration.


VNF On-boarding and package management > Resource Control Loop



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-33904`

    The VNF or PNF Package **MUST** include documentation for each KPI, provide
    lower and upper limits.


.. container:: note

    :need:`R-69877`

    The VNF or PNF Package **MUST** include documentation for each KPI,
    identify the suggested actions that need to be performed when a
    threshold crossing alert event is recorded.


.. container:: note

    :need:`R-01556`

    The VNF or PNF Documentation Package **MUST** describe the
    fault, performance, capacity events/alarms and other event records
    that are made available by the VNF or PNF.


.. container:: note

    :need:`R-16875`

    The VNF or PNF Documentation Package **MUST** include documentation which must
    include a unique identification string for the specific VNF or PNF, a description
    of the problem that caused the error, and steps or procedures to perform
    Root Cause Analysis and resolve the issue.


.. container:: note

    :need:`R-22680`

    The VNF or PNF Documentation Package **MUST** describe
    any requirements for the monitoring component of tools for Network
    Cloud automation and management to provide these records to components
    of the VNF or PNF.


.. container:: note

    :need:`R-33694`

    The VNF or PNF Package **MUST** include documentation to when applicable,
    provide calculators needed to convert raw data into appropriate reporting
    artifacts.


.. container:: note

    :need:`R-86235`

    The VNF or PNF Package **MUST** include documentation about the monitoring
    parameters that must include latencies, success rates, retry rates, load
    and quality (e.g., DPM) for the key transactions/functions supported by
    the VNF or PNF and those that must be exercised by the VNF or PNF in order to perform
    its function.


.. container:: note

    :need:`R-73560`

    The VNF or PNF Package **MUST** include documentation about monitoring
    parameters/counters exposed for virtual resource management and VNF or PNF
    application management.


.. container:: note

    :need:`R-53598`

    The VNF or PNF Documentation Package **MUST**, when relevant,
    provide a threshold crossing alert point for each KPI and describe the
    significance of the threshold crossing.


.. container:: note

    :need:`R-48596`

    The VNF or PNF Documentation Package **MUST** describe
    the characteristics for the VNF or PNF reliability and high availability.


.. container:: note

    :need:`R-01478`

    The VNF or PNF Documentation Package **MUST** describe all
    parameters that are available to monitor the VNF or PNF after instantiation
    (includes all counters, OIDs, PM data, KPIs, etc.) that must be
    collected for reporting purposes.


.. container:: note

    :need:`R-90632`

    The VNF Package **MUST** include documentation about KPIs and
    metrics that need to be collected at each VM for capacity planning
    and performance management purposes.


.. container:: note

    :need:`R-22888`

    The VNF or PNF Documentation Package **MUST** provide the VNF or PNF
    Policy Description to manage the VNF or PNF runtime lifecycle. The document
    must include a description of how the policies (conditions and actions)
    are implemented in the VNF or PNF.


.. container:: note

    :need:`R-42018`

    The VNF or PNF Package **MUST** include documentation which must include
    all events (fault, measurement for VNF or PNF Scaling, Syslogs, State Change
    and Mobile Flow), that need to be collected at each VM, VNFC (defined in `VNF Guidelines <https://onap.readthedocs.io/en/latest/submodules/vnfrqts/guidelines.git/docs/vnf_guidelines.html>`__ ) and for the overall VNF or PNF.


.. container:: note

    :need:`R-35960`

    The VNF or PNF Package **MUST** include documentation which must include
    all events, severity level (e.g., informational, warning, error) and
    descriptions including causes/fixes if applicable for the event.


.. container:: note

    :need:`R-56815`

    The VNF or PNF Documentation Package **MUST** describe
    supported VNF or PNF scaling capabilities and capacity limits (e.g., number
    of users, bandwidth, throughput, concurrent calls).


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-27711

    The xNF provider **MUST** provide an XML file that contains a
    list of xNF error codes, descriptions of the error, and possible
    causes/corrective action.


.. container:: note

    R-74763

    The xNF provider **MUST** provide an artifact per xNF that contains
    all of the xNF Event Records supported. The artifact should include
    reference to the specific release of the xNF Event Stream Common Event
    Data Model document it is based on. (e.g.,
    `VES Event Listener <https://onap.readthedocs.io/en/latest/submodules/vnfsdk/model.git/docs/files/VESEventListener.html>`__)


VNF On-boarding and package management > Resource Description



Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-025941`

    The VNF or PNF PROVIDER **MUST** provide FM Meta Data to support the
    analysis of fault events delivered to DCAE. The Meta Data must be
    included in the VES Registration YAML file with each fault event
    supported by that NF at onboarding time and the Meta Data must follow
    the VES Event Listener and VES Event Registration Specifications.


.. container:: note

    :need:`R-816745`

    The VNF or PNF PROVIDER *MUST* provide the Service Provider with
    PM Meta Data (PM Dictionary) to support the analysis of PM events delivered
    to DCAE. The PM Dictionary is to be provided as a separate YAML artifact at
    onboarding and must follow the VES Event Listener Specification and VES
    Event Registration Specification which contain the format and content
    required.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-98617`

    The VNF Provider **MUST** provide documentation regarding any dependency
    (e.g. affinity, anti-affinity) the VNF has on other VNFs and resources.


.. container:: note

    :need:`R-36280`

    The VNF or PNF Documentation Package **MUST** describe the
    VNF or PNF Functional Capabilities that are utilized to operationalize the
    VNF or PNF and compose complex services.


.. container:: note

    :need:`R-00068`

    The VNF or PNF Documentation Package **MUST** include
    a description of parameters that can be monitored for the VNF or PNF
    and event records (status, fault, flow, session, call, control
    plane, etc.) generated by the VNF or PNF after instantiation.


.. container:: note

    :need:`R-69565`

    The VNF or PNF Documentation Package **MUST** describe the VNF or PNF
    Management APIs, which must include information and tools for ONAP to
    deploy and configure (initially and ongoing) the VNF or PNF application(s)
    (e.g., NETCONF APIs) which includes a description of configurable
    parameters for the VNF or PNF and whether the parameters can be configured
    after VNF or PNF instantiation.


.. container:: note

    :need:`R-22346`

    The VNF or PNF package **MUST** provide :ref:`VES Event Registration <ves_event_registration_3_2>`
    for all VES events provided by that VNF or PNF.


.. container:: note

    :need:`R-384337`

    The VNF Documentation Package **MUST** contain a list of the files within the VNF
    package that are static during the VNF's runtime.


.. container:: note

    :need:`R-84366`

    The VNF or PNF Documentation Package **MUST** describe the
    VNF or PNF Functional APIs that are utilized to build network and
    application services. This document describes the externally exposed
    functional inputs and outputs for the VNF or PNF, including interface
    format and protocols supported.


.. container:: note

    :need:`R-00156`

    The VNF or PNF Documentation Package **MUST** describe the VNF or PNF
    Management APIs, which must include information and tools for
    ONAP to monitor the health of the VNF or PNF (conditions that require
    healing and/or scaling responses).


.. container:: note

    :need:`R-12678`

    The VNF or PNF Documentation Package **MUST** include a
    description of runtime lifecycle events and related actions (e.g.,
    control responses, tests) which can be performed for the VNF or PNF.


.. container:: note

    :need:`R-66070`

    For HEAT package, the VNF Package **MUST** include VNF Identification Data to
    uniquely identify the resource for a given VNF provider. The identification
    data must include: an identifier for the VNF, the name of the VNF as was
    given by the VNF provider, VNF description, VNF provider, and version.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-77707

    The xNF provider **MUST** include a Manifest File that
    contains a list of all the components in the xNF package.


VNF On-boarding and package management > Testing



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-58775`

    The VNF provider **MUST** provide software components that
    can be packaged with/near the VNF, if needed, to simulate any functions
    or systems that connect to the VNF system under test. This component is
    necessary only if the existing testing environment does not have the
    necessary simulators.


.. container:: note

    :need:`R-43958`

    The VNF Documentation Package **MUST** describe
    the tests that were conducted by the VNF provider and the test results.


.. container:: note

    :need:`R-04298`

    The VNF provider **MUST** provide their testing scripts to
    support testing.


VNF Resiliency > Monitoring & Dashboard



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-34957`

    The VNF **MUST** provide a method of metrics gathering for each
    layer's performance to identify variances in the allocations so
    they can be addressed.


{network-role}



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-05201`

    When a VNF connects to two or more unique networks, each
    network **MUST** be assigned a unique ``{network-role}``
    in the context of the VNF for use in the VNF's Heat Orchestration
    Template.


.. container:: note

    :need:`R-69014`

    When a VNF's port connects to an internal network or external network,
    a network role, referred to
    as the ``{network-role}`` **MUST** be assigned to the network for
    use in the VNF's Heat Orchestration Template.  The ``{network-role}``
    is used in the VNF's Heat Orchestration Template resource IDs
    and resource property parameter names.


.. container:: note

    :need:`R-26506`

    A VNF's Heat Orchestration Template's ``{network-role}`` **MUST** contain
    only alphanumeric characters and/or underscores '_' and

    * **MUST NOT** contain any of the following strings: ``_int`` or ``int_``
      or ``_int_``
    * **MUST NOT** end in the string: ``_v6``
    * **MUST NOT** contain the strings ``_#_``,  where ``#`` is a number
    * **MUST NOT** end in the string: ``_#``, where ``#`` is a number


{vm-type}



Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-01455`

    When a VNF's Heat Orchestration Template creates a Virtual Machine
    (i.e., ``OS::Nova::Server``),
    each "class" of VMs **MUST** be assigned a VNF unique
    ``{vm-type}``; where "class" defines VMs that
    **MUST** have the following identical characteristics:

      1.) ``OS::Nova::Server`` resource property ``flavor`` value

      2.) ``OS::Nova::Server`` resource property ``image`` value

      3.) Cinder Volume attachments

        - Each VM in the "class" **MUST** have the identical Cinder Volume
          configuration

      4.) Network attachments and IP address requirements

        - Each VM in the "class" **MUST** have the identical number of
          ports connecting to the identical networks and requiring the identical
          IP address configuration.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-66729

    A VNF's Heat Orchestration Template's Resource that is associated with a
    unique Virtual Machine type **MUST** include ``{vm-type}`` as part of the
    resource ID.


.. container:: note

    R-82481

    A VNF's Heat Orchestration Template's Resource property parameter that is
    associated with a unique Virtual Machine type **MUST** include
    ``{vm-type}`` as part of the parameter name with two exceptions:

     1.) The Resource ``OS::Nova::Server`` property ``availability_zone``
     parameter **MUST NOT** be prefixed with a common ``{vm-type}`` identifier,

     2.) The Resource ``OS::Nova::Server`` eight mandatory and optional
     ``metadata``
     parameters (i.e., ``vnf_name``, ``vnf_id``, ``vf_module_id``,
     ``vf_module_name``, ``vm_role``,
     ``vf_module_index``, ``environment_context``, ``workload_context``)
     **MUST NOT** be prefixed with a common ``{vm-type}`` identifier.

