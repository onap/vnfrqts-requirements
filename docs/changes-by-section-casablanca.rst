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


Requirement Changes Introduced in Casablanca
--------------------------------------------

This document summarizes the requirement changes by section that were
introduced between the Beijing release and
Casablanca release. Click on the requirement number to
navigate to the

.. contents::
    :depth: 2

Summary of Changes
^^^^^^^^^^^^^^^^^^

* **Requirements Added:** 102
* **Requirements Changed:** 232
* **Requirements Removed:** 63


Configuration Management > Ansible Standards and Capabilities > xNF Configuration via Ansible Requirements > Ansible Client Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~

.. container:: note

    :need:`R-24482`

    The xNF **MUST** provide Ansible playbooks that are designed to run using
    an inventory hosts file in a supported format; with site group that shall
    be used to add site specific configurations to the target xNF VM(s) as
    needed.


.. container:: note

    :need:`R-45197`

    The xNF **MUST** define the "from=" clause to provide the list of IP
    addresses of the Ansible Servers in the Cluster, separated by coma, to
    restrict use of the SSH key pair to elements that are part of the Ansible
    Cluster owner of the issued and assigned mechanized user ID.


.. container:: note

    :need:`R-67124`

    The xNF **MUST** provide Ansible playbooks that are designed to run using
    an inventory hosts file in a supported format; with group names matching
    VNFC 3-character string adding "vip" for groups with virtual IP addresses
    shared by multiple VMs as seen in examples provided in Appendix.


.. container:: note

    :need:`R-73459`

    The xNF **MUST** provide the ability to include a "from=" clause in SSH
    public keys associated with mechanized user IDs created for an Ansible
    Server cluster to use for xNF VM authentication.


.. container:: note

    :need:`R-94567`

    The xNF **MUST** provide Ansible playbooks that are designed to run using
    an inventory hosts file in a supported format with only IP addresses or
    IP addresses and VM/xNF names.


.. container:: note

    :need:`R-97345`

    The xNF **MUST** permit authentication, using root account, only right
    after instantiation and until post-instantiation configuration is
    completed.


.. container:: note

    :need:`R-97451`

    The xNF **MUST** provide the ability to remove root access once
    post-instantiation configuration (Configure) is completed.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-32217`

    The xNF **MUST** have routable management IP addresses or FQDNs that
    are reachable via the Ansible Server for the endpoints (VMs) of a
    xNF that playbooks will target. ONAP will initiate requests to the
    Ansible Server for invocation of playbooks against these end
    points [#7.3.3]_.


.. container:: note

    :need:`R-91745`

    The xNF **MUST** update the Ansible Server and other entities
    storing and using the SSH keys for authentication when the SSH
    keys used by Ansible are regenerated/updated.

    **Note**: Ansible Server itself may be used to upload new SSH public
    keys onto supported xNFs.


.. container:: note

    :need:`R-82018`

    The xNF **MUST** load the Ansible Server SSH public key onto xNF
    VM(s) /root/.ssh/authorized_keys as part of instantiation. Alternative,
    is for Ansible Server SSH public key to be loaded onto xNF VM(s) under
    /home/<Mechanized user ID>/.ssh/authorized_keys as part of instantiation,
    when a Mechanized user ID is created during instantiation, and Configure
    and all playbooks are designed to use a mechanized user ID only for
    authentication (never using root authentication during Configure playbook
    run). This will allow the Ansible Server to authenticate to perform
    post-instantiation configuration without manual intervention and without
    requiring specific xNF login IDs and passwords.

    *CAUTION*: For xNFs configured using Ansible, to eliminate the need
    for manual steps, post-instantiation and pre-configuration, to
    upload of SSH public keys, SSH public keys loaded during (heat)
    instantiation shall be preserved and not removed by (heat) embedded
    (userdata) scripts.


.. container:: note

    :need:`R-35401`

    The xNF **MUST** support SSH and allow SSH access by the
    Ansible server to the endpoint VM(s) and comply with the Network
    Cloud Service Provider guidelines for authentication and access.


.. container:: note

    :need:`R-92866`

    The xNF **MUST** include as part of post-instantiation configuration
    done by Ansible Playbooks the removal/update of the SSH public key from
    /root/.ssh/authorized_keys, and update of SSH keys loaded through
    instantiation to support Ansible. This may include creating Mechanized user
    ID(s) used by the Ansible Server(s) on VNF VM(s) and uploading and
    installing new SSH keys used by the mechanized use ID(s).


Configuration Management > Ansible Standards and Capabilities > xNF Configuration via Ansible Requirements > Ansible Playbook Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-24189`

    The xNF provider **MUST** deliver a new set of playbooks that includes
    all updated and unchanged playbooks for any new revision to an existing
    set of playbooks.


.. container:: note

    :need:`R-49751`

    The xNF **MUST** support Ansible playbooks that are compatible with
    Ansible version 2.6 or later.


.. container:: note

    :need:`R-49911`

    The xNF provider **MUST** assign a new point release to the updated
    playbook set. The functionality of a new playbook set must be tested before
    it is deployed to the production.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-48698`

    The xNF **MUST** utilize information from key value pairs that will be
    provided by the Ansible Server as "extra-vars" during invocation to
    execute the desired xNF action. The "extra-vars" attribute-value pairs
    are passed to the Ansible Server by an APPC/SDN-C as part of the
    Rest API request. If the playbook requires files, they must also be
    supplied using the methodology detailed in the Ansible Server API, unless
    they are bundled with playbooks, example, generic templates. Any files
    containing instance specific info (attribute-value pairs), not obtainable
    from any ONAP inventory databases or other sources, referenced and used an
    input by playbooks, shall be provisioned (and distributed) in advance of
    use, e.g., xNF instantiation. Recommendation is to avoid these instance
    specific, manually created in advance of instantiation, files.


.. container:: note

    :need:`R-43353`

    The xNF **MUST** return control from Ansible Playbooks only after all
    tasks performed by playbook are fully complete, signaling that the
    playbook completed all tasks. When starting services, return control
    only after all services are up. This is critical for workflows where
    the next steps are dependent on prior tasks being fully completed.


.. container:: note

    :need:`R-51442`

    The xNF **SHOULD** use playbooks that are designed to
    automatically 'rollback' to the original state in case of any errors
    for actions that change state of the xNF (e.g., configure).

    **Note**: In case rollback at the playbook level is not supported or
    possible, the xNF provider shall provide alternative rollback
    mechanism (e.g., for a small xNF the rollback mechanism may rely
    on workflow to terminate and re-instantiate VNF VMs and then re-run
    playbook(s)). Backing up updated files is also recommended to support
    rollback when soft rollback is feasible.


.. container:: note

    :need:`R-50252`

    The xNF **MUST** write to a response file in JSON format that will be
    retrieved and made available by the Ansible Server if, as part of a xNF
    action (e.g., audit), a playbook is required to return any xNF
    information/response. The text files must be written in the main playbook
    home directory, in JSON format. The JSON file must be created for the xNF
    with the name '<xNF name>_results.txt'. All playbook output results, for
    all xNF VMs, to be provided as a response to the request, must be written
    to this response file.


.. container:: note

    :need:`R-49396`

    The xNF **MUST** support each APPC/SDN-C xNF action
    by invocation of **one** playbook [#7.3.4]_. The playbook will be responsible
    for executing all necessary tasks (as well as calling other playbooks)
    to complete the request.


.. container:: note

    :need:`R-02651`

    The xNF **SHOULD** use available backup capabilities to save a
    copy of configuration files before implementing changes to support
    operations such as backing out of software upgrades, configuration
    changes or other work as this will help backing out of configuration
    changes when needed.


.. container:: note

    :need:`R-58301`

    The xNF **SHOULD NOT** use playbooks that make requests to
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


Configuration Management > Chef Standards and Capabilities > xNF Configuration via Chef Requirements > Chef Roles/Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-26567`

    The xNF Package **MUST** include a run list of
    roles/cookbooks/recipes, for each supported xNF action, that will
    perform the desired xNF action in its entirety as specified by ONAP
    (see Section 7.c, APPC/SDN-C APIs and Behavior, for list of xNF
    actions and requirements), when triggered by a chef-client run list
    in JSON file.


Configuration Management > Controller Interactions With xNF > Configuration Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-20741`

    The xNF **MUST** support APPC/SDN-C ``Configure`` command.


.. container:: note

    :need:`R-94084`

    The xNF **MUST** support APPC/SDN-C ``ConfigScaleOut`` command.


.. container:: note

    :need:`R-32981`

    The xNF **MUST** support APPC ``ConfigBackup`` command.


.. container:: note

    :need:`R-48247`

    The xNF **MUST** support APPC ``ConfigRestore`` command.


.. container:: note

    :need:`R-56385`

    The xNF **MUST** support APPC ``Audit`` command.


.. container:: note

    :need:`R-19366`

    The xNF **MUST** support APPC ``ConfigModify`` command.


Configuration Management > Controller Interactions With xNF > HealthCheck and Failure Related Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-41430`

    The xNF **MUST** support APPC/SDN-C ``HealthCheck`` command.


Configuration Management > Controller Interactions With xNF > Lifecycle Management Related Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-328086`

    The xNF **MUST**, if serving as a distribution point or anchor point for
    steering point from source to destination, support the ONAP Controller's
    ``DistributeTraffic`` command.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-12706`

    The xNF **MUST** support APPC/SDN-C ``QuiesceTraffic`` command.


.. container:: note

    :need:`R-49466`

    The xNF **MUST** support APPC/SDN-C ``UpgradeSoftware`` command.


.. container:: note

    :need:`R-82811`

    The xNF **MUST** support APPC ``StartApplication`` command.


.. container:: note

    :need:`R-07251`

    The xNF **MUST** support APPC/SDN-C ``ResumeTraffic`` command.


.. container:: note

    :need:`R-45856`

    The xNF **MUST** support APPC/SDN-C ``UpgradePostCheck`` command.


.. container:: note

    :need:`R-65641`

    The xNF **MUST** support APPC/SDN-C ``UpgradeBackOut`` command.


.. container:: note

    :need:`R-83146`

    The xNF **MUST** support APPC ``StopApplication`` command.


.. container:: note

    :need:`R-97343`

    The xNF **MUST** support APPC/SDN-C ``UpgradeBackup`` command.


.. container:: note

    :need:`R-19922`

    The xNF **MUST** support APPC/SDN-C ``UpgradePrecheck`` command.


Configuration Management > NETCONF Standards and Capabilities > xNF Configuration via NETCONF Requirements > NETCONF Server Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-18733`

    The xNF **MUST** implement the protocol operation:
    ``discard-changes()`` - Revert the candidate configuration
    data store to the running configuration.


.. container:: note

    :need:`R-29488`

    The xNF **MUST** implement the protocol operation:
    ``get-config(source, filter`` - Retrieve a (filtered subset of
    a) configuration from the configuration data store source.


.. container:: note

    :need:`R-70496`

    The xNF **MUST** implement the protocol operation:
    ``commit(confirmed, confirm-timeout)`` - Commit candidate
    configuration data store to the running configuration.


.. container:: note

    :need:`R-44281`

    The xNF **MUST** implement the protocol operation:
    ``edit-config(target, default-operation, test-option, error-option,
    config)`` - Edit the target configuration data store by merging,
    replacing, creating, or deleting new config elements.


.. container:: note

    :need:`R-02597`

    The xNF **MUST** implement the protocol operation:
    ``lock(target)`` - Lock the configuration data store target.


.. container:: note

    :need:`R-90007`

    The xNF **MUST** implement the protocol operation:
    ``close-session()`` - Gracefully close the current session.


.. container:: note

    :need:`R-11235`

    The xNF **MUST** implement the protocol operation:
    ``kill-session(session``- Force the termination of **session**.


.. container:: note

    :need:`R-96554`

    The xNF **MUST** implement the protocol operation:
    ``unlock(target)`` - Unlock the configuration data store target.


.. container:: note

    :need:`R-88031`

    The xNF **SHOULD** implement the protocol operation:
    ``delete-config(target)`` - Delete the named configuration
    data store target.


.. container:: note

    :need:`R-29324`

    The xNF **SHOULD** implement the protocol operation:
    ``copy-config(target, source)`` - Copy the content of the
    configuration data store source to the configuration data store target.


Contrail Resource Parameters > Contrail Network Parameters > External Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-02164`

    When a VNF's Heat Orchestration Template's Contrail resource
    has a property that
    references an external network that requires the network's
    Fully Qualified Domain Name (FQDN), the property parameter

    * **MUST** follow the format ``{network-role}_net_fqdn``
    * **MUST** be declared as type ``string``
    * **MUST NOT** be enumerated in the VNF's Heat Orchestration Template's
      Environment File


Heat > Cinder Volumes
^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-79531

    The VNF Heat Orchestration Template **MUST** define
    "outputs" in the volume template for each Cinder volume
    resource universally unique identifier (UUID) (i.e. ONAP
    Volume Template Output Parameters).


Heat > Heat Orchestration Template Format > Heat Orchestration Template Structure > resources > metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-97199

    A VNF's Heat Orchestration Template's OS::Nova::Server
    resource **MUST** contain the attribute "metadata".


Heat > Heat Template Constructs > Heat Files Support (get_file)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-62177

    When using the intrinsic function get_file, the included files
    **MUST** have unique file names within the scope of the VNF.


Heat > Heat Template Constructs > Nested Heat Template Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-89868

    The VNF Heat Orchestration Template **MUST** have unique
    file names within the scope of the VNF for a nested heat yaml file.


Heat > Networking > External Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-29865

    When a VNF connects to an external network, a network role,
    referred to as the '{network-role}' **MUST** be assigned to the
    external network for use in the VNF's Heat Orchestration Template.


Heat > Networking > Internal Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-34726

    If a VNF's port is connected to an internal network and the port
    is created in the same Heat Orchestration Template as the internal network,
    then the port resource **MUST** use a 'get_resource' to obtain
    the network UUID.


Heat > ONAP Resource ID and Parameter Naming Convention > Contrail Resource Parameters > Contrail Network Parameters > External Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-73228

    A VNF's Heat Orchestration Template's parameter
    '{network-role}_net_fqdn'
    **MUST** be declared as type 'string'.


Heat > ONAP Resource ID and Parameter Naming Convention > Resource: OS::Nova::Server – Metadata Parameters > vm_role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-46823

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vnf_name' **MUST** be
    either

     - enumerated in the VNF's Heat Orchestration
       Template's environment file.

     - hard coded in the VNF's Heat Orchestration
       Template's OS::Nova::Resource metadata property.


Heat > ONAP Support of Environment Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-22656

    The VNF Heat Orchestration Template **MUST** have a
    corresponding environment file for a Cinder Volume Module.


.. container:: note

    R-35727

    The VNF Heat Orchestration Template **MUST** have a
    corresponding environment file for an Incremental module.


.. container:: note

    R-67205

    The VNF Heat Orchestration Template **MUST** have a corresponding
    environment file for a Base Module.


Monitoring & Management > Data Structure Specification of the Event Record
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-120182`

    The xNF provider **MUST** indicate specific conditions that may arise, and
    recommend actions that may be taken at specific thresholds, or if specific
    conditions repeat within a specified time interval, using the semantics and
    syntax described by the :ref:`VES Event Registration specification <ves_event_registration_3_2>`.


.. container:: note

    :need:`R-123044`

    The xNF Provider **MAY** require that specific events, identified by their
    ``eventName``, require that certain fields, which are optional in the common
    event format, must be present when they are published.


.. container:: note

    :need:`R-520802`

    The xNF provider **MUST** provide a YAML file formatted in adherence with
    the :ref:`VES Event Registration specification <ves_event_registration_3_2>`
    that defines the following information for each event produced by the VNF:

    * ``eventName``
    * Required fields
    * Optional fields
    * Any special handling to be performed for that event


.. container:: note

    :need:`R-570134`

    The events produced by the xNF **MUST** must be compliant with the common
    event format defined in the
    :ref:`VES Event Listener <ves_event_listener_7_1>`
    specification.


Monitoring & Management > Event Records - Data Structure Description > Common Event Header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


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
       detecting a problem in another xNF
     * ``sequence`` - the ordering of events communicated by an event source
     * ``sourceName`` - name of the entity experiencing the event issue, which
       may be detected and reported by a separate reporting entity
     * ``startEpochMicrosec`` - the earliest unix time (aka epoch time)
       associated with the event
     * ``version`` - the version of the event header
     * ``vesEventListenerVersion`` - Version of the VES event listener API spec
       that this event is compliant with


Monitoring & Management > Event Records - Data Structure Description > Miscellaneous
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-283988`

    The VNF, when publishing events, **MUST NOT** send information through
    extensible structures if the event specification has explicitly defined
    fields for that information.


.. container:: note

    :need:`R-408813`

    The VNF, when publishing events, **MUST** pass all information it is
    able to collect even if the information field is identified as optional.
    However, if the data cannot be collected, then optional fields can be
    omitted.


.. container:: note

    :need:`R-470963`

    The VNF, when publishing events, **MUST** leverage camel case to separate
    words and acronyms used as keys that will be sent through extensible fields.
    When an acronym is used as the key, then only the first letter shall be
    capitalized.


Monitoring & Management > Monitoring & Management Requirements > Asynchronous and Synchronous Data Delivery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-332680`

    The xNF **SHOULD** deliver all syslog messages to the VES Collector per the
    specifications in Monitoring and Management chapter.


Monitoring & Management > Monitoring & Management Requirements > Bulk Performance Measurement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-440220`

    The xNF **SHOULD** support File transferring protocol, such as FTPES or SFTP,
    when supporting the event-driven bulk transfer of monitoring data.


.. container:: note

    :need:`R-75943`

    The xNF **SHOULD** support the data schema defined in 3GPP TS 32.435, when
    supporting the event-driven bulk transfer of monitoring data.


.. container:: note

    :need:`R-841740`

    The xNF **SHOULD** support FileReady VES event for event-driven bulk transfer
    of monitoring data.


Monitoring & Management > Monitoring & Management Requirements > Google Protocol Buffers (GPB)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-257367`

    The xNF, when leveraging Google Protocol Buffers for events, **MUST**
    serialize the events using native Google Protocol Buffers (GPB) according
    to the following guidelines:

       * The keys are represented as integers pointing to the system resources
         for the xNF being monitored
       * The values correspond to integers or strings that identify the
         operational state of the VNF resource, such a statistics counters and
         the state of an xNF resource.
       * The required Google Protocol Buffers (GPB) metadata is provided in the
         form of .proto files.


.. container:: note

    :need:`R-978752`

    The xNF providers **MUST** provide the Service Provider the following
    artifacts to support the delivery of high-volume xNF telemetry to
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

    The xNF, when leveraging JSON for events, **MUST** encode and serialize
    content delivered to ONAP using JSON (RFC 7159) plain text format.
    High-volume data is to be encoded and serialized using
    `Avro <http://avro.apache.org/>`_, where the Avro [#7.4.1]_ data
    format are described using JSON.


Monitoring & Management > Monitoring & Management Requirements > Reporting Frequency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-146931`

    The xNF **MUST** report exactly one Measurement event per period
    per source name.


Monitoring & Management > Monitoring & Management Requirements > VNF telemetry via standardized interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-821473`

    The xNF MUST produce heartbeat indicators consisting of events containing
    the common event header only per the VES Listener Specification.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-51910

    The xNF **MUST** provide all telemetry (e.g., fault event
    records, syslog records, performance records etc.) to ONAP using the
    model, format and mechanisms described in this section.


Monitoring & Management > Transports and Protocols Supporting Resource Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-798933`

    The xNF **SHOULD** deliver event records that fall into the event domains
    supported by VES.


.. container:: note

    :need:`R-821839`

    The xNF **MUST** deliver event records to ONAP using the common transport
    mechanisms and protocols defined in this document.


.. container:: note

    :need:`R-932071`

    The xNF provider **MUST** reach agreement with the Service Provider on
    the selected methods for encoding, serialization and data delivery
    prior to the on-boarding of the xNF into ONAP SDC Design Studio.


Monitoring & Management > Transports and Protocols Supporting Resource Interfaces > Bulk Telemetry Transmission
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-908291`

    The XNF **MAY** leverage bulk xNF telemetry transmission mechanism, as
    depicted in Figure 4, in instances where other transmission methods are not
    practical or advisable.


Monitoring & Management > Transports and Protocols Supporting Resource Interfaces > xNF Telemetry using Google Protocol Buffers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-697654`

    The xNF **MAY** leverage the Google Protocol Buffers (GPB) delivery model
    depicted in Figure 3 to support real-time performance management (PM) data.
    In this model the VES events are streamed as binary-encoded GBPs over via
    TCP sockets.


Monitoring & Management > Transports and Protocols Supporting Resource Interfaces > xNF Telemetry using VES/JSON Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-659655`

    The xNF **SHOULD** leverage the JSON-driven model, as depicted in Figure 2,
    for data delivery unless there are specific performance or operational
    concerns agreed upon by the Service Provider that would warrant using an
    alternate model.


ONAP Heat Cinder Volumes
^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-270358`

    A VNF's Heat Orchestration Template's Cinder Volume Template **MUST**
    contain either

    * An ``OS::Cinder::Volume`` resource
    * An ``OS::Heat::ResourceGroup`` resource that references a Nested YAML
      file that contains an ``OS::Cinder::Volume`` resource
    * A resource that defines the property ``type`` as a Nested YAML file
      (i.e., static nesting) and the Nested YAML contains
      an ``OS::Cinder::Volume`` resource


ONAP Heat Heat Template Constructs > Heat Files Support (get_file)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-05050`

    A VNF's Heat Orchestration Templates intrinsic function
    ``get_file`` <content key> **MAY** be used:

        * more than once in a VNF's Heat Orchestration Template
        * in two or more of a VNF's Heat Orchestration Templates
        * in a VNF's Heat Orchestration Templates nested YAML file


.. container:: note

    :need:`R-76718`

    If a VNF's Heat Orchestration Template uses the intrinsic function
    ``get_file``, the ``get_file`` target **MUST** be referenced in
    the Heat Orchestration Template by file name.


.. container:: note

    :need:`R-41888`

    A VNF's Heat Orchestration Template intrinsic function
    ``get_file`` **MUST NOT** utilize URL-based file retrieval.


.. container:: note

    :need:`R-87848`

    When using the intrinsic function get_file, ONAP does not support
    a directory hierarchy for included files. All files must be in a
    single, flat directory per VNF. A VNF's Heat Orchestration
    Template's ``get_file`` target files **MUST** be in the same
    directory hierarchy as the VNF's Heat Orchestration Templates.


ONAP Heat Heat Template Constructs > Nested Heat Templates > Nested Heat Template Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-70112`

    A VNF's Heat Orchestration Template **MUST** reference a Nested YAML
    file by name. The use of ``resource_registry`` in the VNF's Heat
    Orchestration Templates Environment File **MUST NOT** be used.


ONAP Heat Networking > External Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-00606`

    A VNF **MAY** be connected to zero, one or more than one external
    network.


ONAP Heat Networking > Internal Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-46461`

    A VNF's port connected to an internal network **MUST NOT** use the port
    for the purpose of reaching VMs in another VNF and/or an
    external gateway and/or
    external router.


.. container:: note

    :need:`R-52425`

    A VNF's port connected to an internal network **MUST**
    use the port for the purpose of reaching VMs in the same VNF.


.. container:: note

    :need:`R-87096`

    A VNF **MAY** contain zero, one or more than one internal network.


ONAP Heat Orchestration Template Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-92635`

    A VNF's Heat Orchestration Template **MUST** be compliant with the
    OpenStack Template Guide.


ONAP Heat Orchestration Template Format > Environment File Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-86285`

    A VNF's Heat Orchestration template **MUST** have a
    corresponding environment file.


.. container:: note

    :need:`R-68198`

    A VNF's Heat Orchestration template's Environment File's
    ``parameters:`` section **MAY** (or **MAY NOT**) enumerate parameters.


.. container:: note

    :need:`R-03324`

    A VNF's Heat Orchestration template's Environment File **MUST**
    contain the ``parameters:`` section.


ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-90279`

    A VNF Heat Orchestration's template's parameter **MUST** be used
    in a resource with the exception of the parameters for the
    ``OS::Nova::Server`` resource property ``availability_zone``.


.. container:: note

    :need:`R-91273`

    A VNF Heat Orchestration's template's parameter for the
    ``OS::Nova::Server`` resource property ``availability_zone``
    **MAY NOT** be used in any ``OS::Nova::Server``.


ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > parameters > constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-88863`

    A VNF's Heat Orchestration Template's parameter defined
    in a non-nested YAML file as type
    ``number`` **MUST** have a parameter constraint of ``range`` or
    ``allowed_values`` defined.


.. container:: note

    :need:`R-00011`

    A VNF's Heat Orchestration Template's parameter defined
    in a nested YAML file
    **MUST NOT** have a parameter constraint defined.


.. container:: note

    :need:`R-06613`

    A VNF's Heat Orchestration Template's parameter defined
    in a non-nested YAML file as type
    ``boolean`` **MAY** have a parameter constraint defined.


.. container:: note

    :need:`R-40518`

    A VNF's Heat Orchestration Template's parameter defined
    in a non-nested YAML file as type
    ``string`` **MAY** have a parameter constraint defined.


.. container:: note

    :need:`R-96227`

    A VNF's Heat Orchestration Template's parameter defined
    in a non-nested YAML file as type
    ``json`` **MAY** have a parameter constraint defined.


.. container:: note

    :need:`R-79817`

    A VNF's Heat Orchestration Template's parameter defined
    in a non-nested YAML file as
    type ``comma_delimited_list`` **MAY** have a parameter constraint defined.


ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > parameters > default
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-26124`

    If a VNF Heat Orchestration Template parameter has a default value,
    it **MUST** be enumerated in the environment file.


ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > parameters > type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-11441`

    A VNF's Heat Orchestration Template's parameter type **MUST** be one of
    the following values:

    * ``string``
    * ``number``
    * ``json``
    * ``comma_delimited_list``
    * ``boolean``


ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-40551`

    A VNF's Heat Orchestration Template's Nested YAML files **MAY**
    (or **MAY NOT**) contain the section ``resources:``.


ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > resources > deletion_policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-43740`

    VNF's Heat Orchestration Template's Resource **MAY** declare the
    attribute ``deletion_policy:``.


ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > resources > external_id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-78569`

    VNF's Heat Orchestration Template's Resource **MAY** declare the
    attribute ``external_id:``.


ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > resources > metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-67386`

    A VNF's Heat Orchestration Template's Resource **MAY** declare the
    attribute ``metadata``.


ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > resources > properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-10834`

    If a VNF's Heat Orchestration Template resource attribute
    ``property:`` uses a nested ``get_param``, the nested
    ``get_param`` **MUST** reference an index.


ONAP Heat Orchestration Templates Overview > ONAP Heat Orchestration Template Filenames > Base Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


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
    underscores '_' and **MUST NOT** contain the case insensitive word ``base``.


ONAP Heat Orchestration Templates Overview > ONAP Heat Orchestration Template Filenames > Cinder Volume Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-31141`

    VNF Heat Orchestration Template's Cinder Volume Module's Environment File
    **MUST** be named identical to the VNF Heat Orchestration Template's
    Cinder Volume Module with ``.y[a]ml`` replaced with ``.env``.


.. container:: note

    :need:`R-82732`

    A VNF Heat Orchestration Template's Cinder Volume Module **MUST**
    be named identical to the base or incremental module it is supporting with
    ``_volume`` appended.


ONAP Heat Orchestration Templates Overview > ONAP Heat Orchestration Template Filenames > Incremental Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-87247`

    VNF Heat Orchestration Template's Incremental Module file name
    **MUST** contain only alphanumeric characters and underscores
    '_' and **MUST NOT** contain the case insensitive word ``base``.


ONAP Heat Orchestration Templates Overview > ONAP Heat Orchestration Template Filenames > Nested Heat file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-76057`

    VNF Heat Orchestration Template's Nested YAML file name **MUST** contain
    only alphanumeric characters and underscores '_' and
    **MUST NOT** contain the case insensitive word ``base``.


ONAP Heat Orchestration Templates Overview > ONAP VNF Modularity Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-38474`

    A VNF's Base Module **MUST** have a corresponding Environment File.


.. container:: note

    :need:`R-20974`

    At orchestration time, the VNF's Base Module **MUST**
    be deployed first, prior to any incremental modules.


.. container:: note

    :need:`R-53433`

    A VNF's Cinder Volume Module **MUST** have a corresponding environment file


.. container:: note

    :need:`R-11200`

    A VNF's Cinder Volume Module, when it exists, **MUST** be 1:1
    with a Base module or Incremental module.


.. container:: note

    :need:`R-33132`

    A VNF's Heat Orchestration Template **MAY** be
     1.) Base Module Heat Orchestration Template (also referred to as a
         Base Module),
     2.) Incremental Module Heat Orchestration Template (referred to as
         an Incremental Module), or
     3.) a Cinder Volume Module Heat Orchestration Template (referred to as
         Cinder Volume  Module).


.. container:: note

    :need:`R-81725`

    A VNF's Incremental Module **MUST** have a corresponding Environment File


.. container:: note

    :need:`R-37028`

    A VNF **MUST** be composed of one Base Module


ONAP Heat Orchestration Templates Overview > Output Parameters > ONAP Volume Module Output Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-07443`

    A VNF's Heat Orchestration Templates' Cinder Volume Module Output
    Parameter's name and type **MUST** match the input parameter name and type
    in the corresponding Base Module or Incremental Module unless the Output
    Parameter is of the type ``comma_delimited_list``, then the corresponding
    input parameter **MUST** be declared as type ``json``.


.. container:: note

    :need:`R-89913`

    A VNF's Heat Orchestration Template's Cinder Volume Module Output
    Parameter(s)
    **MUST** include the
    UUID(s) of the Cinder Volumes created in template,
    while others **MAY** be included.


ONAP Heat VNF Modularity
^^^^^^^^^^^^^^^^^^^^^^^^


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

    For ECOMP to provided the UUID value of the shared resource to the
    incremental module, the parameter name defined in the ``outputs``
    section of the base module **MUST** be defined as a parameter
    in the ``parameters`` section of the incremental module.

    ECOMP will capture the output parameter name and value in the base module
    and provide the value to the corresponding parameter(s) in the
    incremental module(s).


ONAP Output Parameter Names > Predefined Output Parameters > OAM Management IP Addresses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-56287`

    If the VNF's OAM Management IP Address is assigned by ONAP SDN-C and
    assigned in the VNF's Heat Orchestration Template's via a heat resource
    ``OS::Neutron::Port`` property ``fixed_ips`` map property
    ``ip_adress`` parameter (e.g., ``{vm-type}_{network-role}_ip_{index}``,
    ``{vm-type}_{network-role}_v6_ip_{index}``)
    and the OAM IP Address is required to be inventoried in ONAP A&AI,
    then the parameter **MUST** be echoed in an output statement.

    .. code-block:: yaml

      outputs:
          oam_management_v4_address:
            value: {get_param: {vm-type}_{network-role}_ip_{index} }
          oam_management_v6_address:
            value: {get_param: {vm-type}_{network-role}_v6_ip_{index} }


.. container:: note

    :need:`R-48987`

    If the VNF's OAM Management IP Address is cloud assigned and
    and the OAM IP Address is required to be inventoried in ONAP A&AI,
    then the parameter **MUST** be obtained by the
    resource ``OS::Neutron::Port``
    attribute ``ip_address``.


.. container:: note

    :need:`R-94669`

    If a VNF has one IPv6 OAM Management IP Address and the
    IP Address needs to be inventoried in ONAP's A&AI
    database, an output parameter **MUST** be declared in only one of the
    VNF's Heat Orchestration Templates and the parameter **MUST** be named
    ``oam_management_v6_address``.


ONAP TOSCA VNFD Requirements > TOSCA VNF Descriptor > Capability Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-67895`

    The VNFD provided by VNF vendor may use the below described TOSCA
    capabilities. An on-boarding entity (ONAP SDC) **MUST** support them.

      **tosca.capabilities.nfv.VirtualBindable**

        A node type that includes the VirtualBindable capability indicates
        that it can be pointed by **tosca.relationships.nfv.VirtualBindsTo**
        relationship type.

      **tosca.capabilities.nfv.VirtualLinkable**

        A node type that includes the VirtualLinkable capability indicates
        that it can be pointed by **tosca.relationships.nfv.VirtualLinksTo**
        relationship.

      **tosca.capabilities.nfv.ExtVirtualLinkable**

        A node type that includes the ExtVirtualLinkable capability
        indicates that it can be pointed by
        **tosca.relationships.nfv.VirtualLinksTo** relationship.

      **Note**: This capability type is used in Casablanca how it does
      not exist in the last SOL001 draft

      **tosca.capabilities.nfv.VirtualCompute** and
      **tosca.capabilities.nfv.VirtualStorage** includes flavours of VDU


ONAP TOSCA VNFD Requirements > TOSCA VNF Descriptor > Data Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-54356`

    The below table includes the data types used by NFV node and is based
    on TOSCA/YAML constructs specified in draft GS NFV-SOL 001. The node
    data definitions/attributes used in VNFD **MUST** comply with the below
    table.


.. container:: note

    :need:`R-54876`

    The below table describes the data types used for LCM configuration
    and is based on TOSCA constructs specified in draft GS NFV-SOL 001.
    The LCM configuration data elements used in VNFD **MUST** comply
    with the below table.


ONAP TOSCA VNFD Requirements > TOSCA VNF Descriptor > General
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-15837`

    The following table defines the major TOSCA  Types specified in
    ETSI NFV-SOL001 standard draft. The VNFD provided by a VNF vendor
    **MUST** comply with the below definitions:


.. container:: note

    :need:`R-17852`

    The VNFD **MAY** include TOSCA/YAML definitions that are not part of
    NFV Profile. If provided, these definitions MUST comply with TOSCA
    Simple Profile in YAML v.1.2.


.. container:: note

    :need:`R-35854`

    The VNF Descriptor (VNFD) provided by VNF vendor **MUST** comply with
    TOSCA/YAML based Service template for VNF descriptor specified in
    ETSI NFV-SOL001.

    **Note**: As the ETSI NFV-SOL001 is work in progress the below tables
    summarizes the TOSCA definitions agreed to be part of current version
    of NFV profile and that VNFD MUST comply with in ONAP Release 2+
    Requirements.


.. container:: note

    :need:`R-46527`

    A VNFD is a deployment template which describes a VNF in terms of
    deployment and operational behavior requirements. It contains
    virtualized resources (nodes) requirements as well as connectivity
    and interfaces requirements and **MUST** comply with info elements
    specified in ETSI GS NFV-IFA 011. The main parts of the VNFD are
    the following:

      - VNF topology: it is modeled in a cloud agnostic way using virtualized
        containers and their connectivity. Virtual Deployment Units (VDU)
        describe the capabilities of the virtualized containers, such as
        virtual CPU, RAM, disks; their connectivity is modeled with VDU
        Connection Point Descriptors (VduCpd), Virtual Link Descriptors
        (VnfVld) and VNF External Connection Point Descriptors
        (VnfExternalCpd);

      - VNF deployment aspects: they are described in one or more
        deployment flavours, including configurable parameters, instantiation
        levels, placement constraints (affinity / antiaffinity), minimum and
        maximum VDU instance numbers. Horizontal scaling is modeled with
        scaling aspects and the respective scaling levels in the deployment
        flavours;

    **Note**: The deployment aspects (deployment flavour etc.) are postponed
    for future ONAP releases.

      - VNF lifecycle management (LCM) operations: describes the LCM operations
        supported per deployment flavour, and their input parameters;
        Note, thatthe actual LCM implementation resides in a different layer,
        namely referring to additional template artifacts.


.. container:: note

    :need:`R-65486`

    The VNFD **MUST** comply with ETSI GS NFV-SOL001 document endorsing
    the above mentioned NFV Profile and maintaining the gaps with the
    requirements specified in ETSI GS NFV-IFA011 standard.


ONAP TOSCA VNFD Requirements > TOSCA VNF Descriptor > Interface Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-32155`

    The VNFD provided by VNF vendor may use the below described TOSCA
    interface types. An on-boarding entity (ONAP SDC) **MUST** support them.

      **tosca.interfaces.nfv.vnf.lifecycle.Nfv** supports LCM operations


ONAP TOSCA VNFD Requirements > TOSCA VNF Descriptor > Relationship Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-95321`

    The VNFD provided by VNF vendor may use the below described TOSCA
    relationships. An on-boarding entity (ONAP SDC) **MUST** support them.

      **tosca.relationships.nfv.VirtualBindsTo**

        This relationship type represents an association relationship between
        VDU and CP node types.

      **tosca.relationships.nfv.VirtualLinksTo**

        This relationship type represents an association relationship between
        the VduCpd's and VirtualLinkDesc node types.


ONAP TOSCA VNFD Requirements > VNF CSAR Package > VNF Package Contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-01123`

    The VNF package Manifest file **MUST** contain: VNF package meta-data, a
    list of all artifacts (both internal and external) entry's including
    their respected URI's, an algorithm to calculate a digest and a digest
    result calculated on the content of each artifacts, as specified in
    ETSI GS NFV-SOL004. The VNF Package MUST include VNF Identification
    Data to uniquely identify the resource for a given VNF provider. The
    identification data must include: an identifier for the VNF, the name
    of the VNF as was given by the VNF provider, VNF description, VNF
    provider, and version.


.. container:: note

    :need:`R-10087`

    The VNF package **MUST** contain all standard artifacts as specified in
    ETSI GS NFV-SOL004 including Manifest file, VNFD (or Main TOSCA/YAML
    based Service Template) and other optional artifacts. CSAR Manifest
    file as per SOL004 - for example ROOT\\ **MainServiceTemplate.mf**


.. container:: note

    :need:`R-21322`

    The VNF provider **MUST** provide their testing scripts to support
    testing as specified in ETSI NFV-SOL004 - Testing directory in CSAR


.. container:: note

    :need:`R-26885`

    The VNF provider **MUST** provide the binaries and images needed to
    instantiate the VNF (VNF and VNFC images) either as:

      - Local artifact in CSAR: ROOT\\Artifacts\\ **VNF_Image.bin**

      - externally referred (by URI) artifact in Manifest file (also may be
        referred by VNF Descriptor)

    Note: Currently, ONAP doesn't have the capability of Image management,
    we upload the image into VIM/VNFM manually.


.. container:: note

    :need:`R-40820`

    The VNF provider MUST enumerate all of the open source licenses
    their VNF(s) incorporate. CSAR License directory as per ETSI SOL004.

    for example ROOT\\Licenses\\ **License_term.txt**


ONAP TOSCA VNFD Requirements > VNF CSAR Package > VNF Package Structure and Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-51347`

    The VNF package **MUST** be arranged as a CSAR archive as specified in
    TOSCA Simple Profile in YAML 1.2.


.. container:: note

    :need:`R-87234`

    The VNF package provided by a VNF vendor **MAY** be either with
    TOSCA-Metadata directory (CSAR Option 1) or without TOSCA-Metadata
    directory (CSAR Option 2) as specified in ETSI GS NFV-SOL004. On-boarding
    entity (ONAP SDC) must support both options.

    **Note:** SDC supports only the CSAR Option 1 in Casablanca. The Option 2
    will be considered in future ONAP releases,


PNF Plug and Play > PNF Plug and Play
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-01427`

    The PNF **MUST** support the provisioning of security and authentication
    parameters (HTTP username and password) in order to be able to authenticate
    with DCAE (in ONAP).

    Note: In R3, a username and password are used with the DCAE VES Event
    Listener which are used for HTTP Basic Authentication.

    Note: The configuration management and provisioning software are specific
    to a vendor architecture.


.. container:: note

    :need:`R-106240`

    The following VES Events **MUST** be supported by the PNF: pnfRegistration
    VES Event, HVol VES Event, and Fault VES Event. These are onboarded via
    he SDC Design Studio.

    Note: these VES Events are emitted from the PNF to support PNF Plug and
    Play, High Volume Measurements, and Fault events respectively.


.. container:: note

    :need:`R-17624`

    The PNF **MAY** support the optional parameters for Service
    Configuration Parameters.

    Note: These are detailed in the Stage 5 PnP

    Note: These parameters are optional, and not all PNFs will support any
    or all of these parameters, it is up to the vendor and service provider
    to ascertain which ones are supported up to an including all of the ones
    that have been defined. Note: It is expected that there will be a growing
    list of supported configuration parameters in future releases of ONAP.


.. container:: note

    :need:`R-256347`

    The PNF **MUST** support the Ansible protocol for a Service Configuration
    message exchange between the PNF and PNF Controller (in ONAP).

    Note: this exchange may be either Ansible, Chef, or NetConf depending on
    the PNF. Note: The PNF Controller may be VF-C, APP-C or SDN-C based on the
    PNF and PNF domain. Note: for R3 (Casablanca) only Ansible is supported.


.. container:: note

    :need:`R-258352`

    The PNF **MUST** support & accept the provisioning of an ONAP contact IP
    address (in IPv4 or IPv6 format).

    Note: For example, it a possibility is that an external EMS would configure
    & provision the ONAP contact IP address to the PNF (in either IPv4 or
    IPv6 format). For the PNF Plug and Play Use Case, this IP address is the
    service provider's "point of entry" to the DCAE VES Listener.

    Note: different service provider's network architecture may also require
    special setup to allow an external PNF to contact the ONAP installation.
    For example, in the AT&T network, a maintenance tunnel is used to access
    ONAP.


.. container:: note

    :need:`R-284934`

    If the PNF encounters an error authenticating, reaching the ONAP DCAE VES
    Event listener or recieves an error response from sending the pnfRegistration
    VES Event, it **MAY** log the error, and notify the operator.

    Note: the design of how errors are logged, retrieved and reported
    will be a vendor-specific architecture. Reporting faults and errors
    is also a vendor specific design. It is expected that the PNF shall
    have a means to log an error and notify a user when a fault condition
    occurs in trying to contact ONAP, authenticate or send a pnfRegistration
    event.


.. container:: note

    :need:`R-378131`

    (Error Case) - If an error is encountered by the PNF during a
    Service Configuration exchange with ONAP, the PNF **MAY** log the
    error and notify an operator.


.. container:: note

    :need:`R-56718`

    The PNF Vendor **MAY** provide software version(s) to be supported by PNF
    for SDC Design Studio PNF Model. This is set in the PNF Model property
    software_versions.


.. container:: note

    :need:`R-579051`

    The PNF **MAY** support a HTTP connection to the DCAE VES Event Listener.

    Note: HTTP is allowed but not recommended.


.. container:: note

    :need:`R-638216`

    (Error Case) - The PNF **MUST** support a configurable timer to stop the
    periodicity sending of the pnfRegistration VES event. If this timer expires
    during a Service Configuration exchange between the PNF and ONAP, it
    MAY log a time-out error and notify an operator.

    Note: It is expected that each vendor will enforce and define a PNF
    service configuration timeout period. This is because the PNF cannot
    wait indefinitely as there may also be a technician on-site trying to
    complete installation & commissioning. The management of the VES event
    exchange is also a requirement on the PNF to be developed by the PNF
    vendor.


.. container:: note

    :need:`R-686466`

    The PNF **MUST** support sending a pnfRegistration VES event.


.. container:: note

    :need:`R-707977`

    When the PNF receives a Service configuration from ONAP, the PNF **MUST**
    cease sending the pnfRegistration VES Event.


.. container:: note

    :need:`R-763774`

    The PNF **MUST** support a HTTPS connection to the DCAE VES Event
    Listener.


.. container:: note

    :need:`R-793716`

    The PNF **MUST** have "ONAP Aware" software which is capable of performing
    PNF PnP registration with ONAP. The "ONAP Aware" software is capable of
    performing the PNF PnP Registration with ONAP MUST either be loaded
    separately or integrated into the PNF software upon physical delivery
    and installation of the PNF.

    Note: It is up to the specific vendor to design the software management
    functions.


.. container:: note

    :need:`R-809261`

    The PNF **MUST** use a IP address to contact ONAP.

    Note: it is expected that an ONAP operator can ascertain the ONAP IP
    address or the security gateway to reach ONAP on the VID or ONAP portal
    GUI.

    Note: The ONAP contact IP address has been previously configured and
    provisioned prior to this step.

    Note: The ONAP IP address could be provisioned or resolved through
    FQDN & DNS.


.. container:: note

    :need:`R-894004`

    When the PNF sets up a HTTP or HTTPS connection, it **MUST** provide a
    username and password to the DCAE VES Collector for HTTP Basic
    Authentication.

    Note: HTTP Basic Authentication has 4 steps: Request, Authenticate,
    Authorization with Username/Password Credentials, and Authentication Status
    as per RFC7617 and RFC 2617.


.. container:: note

    :need:`R-952314`

    If the PNF set up a TLS connection and mutual (two-way) authentication is
    being used, then the PNF **MUST** provide its own X.509v3 Certificate to
    the DCAE VES Collector for authentication.

    Note: This allows TLS authentication by DCAE VES Collector.

    Note: The PNF got its X.509 certificate through Enrollment with an
    operator certificate authority or a X.509 vendor certificate from the
    vendor factory CA.

    Note: In R3 three authentication options are supported:

    (1) HTTP with Username & Password and no TLS.

    (2) HTTP with Username & Password & TLS with two-way certificate
        authentication.

    (3) HTTP with Username & Password & TLS with server-side
        certificate authentication.


.. container:: note

    :need:`R-980039`

    The PNF **MUST** send the pnfRegistration VES event periodically.


.. container:: note

    :need:`R-981585`

    The pnfRegistration VES event periodicity **MUST** be configurable.

    Note: The PNF uses the service configuration request as a semaphore to
    stop sending the pnfRegistration sent. See the requirement PNP-5360
    requirement.


Resource IDs
^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-98138`

    When a VNF's Heat Orchestration Template's resource is associated with a
    single internal network, the Resource ID **MUST** contain the text
    ``int_{network-role}``.


.. container:: note

    :need:`R-67793`

    When a VNF's Heat Orchestration Template's resource is associated
    with more than one ``{vm-type}`` and/or more than one internal and/or
    external network, the Resource ID **MUST** not contain the ``{vm-type}``
    and/or ``{network-role}``/``int_{network-role}``. It also should contain the
    term ``shared`` and/or contain text that identifies the VNF.


.. container:: note

    :need:`R-82115`

    When a VNF's Heat Orchestration Template's resource is associated with a
    single ``{vm-type}``
    and a single external network, the Resource ID text **MUST** contain both
    the ``{vm-type}``
    and the ``{network-role}``

    - the ``{vm-type}`` **MUST** appear before the ``{network-role}`` and
      **MUST** be separated by an underscore '_'


      - e.g., ``{vm-type}_{network-role}``, ``{vm-type}_{index}_{network-role}``


    - note that an ``{index}`` value **MAY** separate the ``{vm-type}`` and the
      ``{network-role}`` and when this occurs underscores **MUST** separate the
      three values.  (e.g., ``{vm-type}_{index}_{network-role}``).


.. container:: note

    :need:`R-82551`

    When a VNF's Heat Orchestration Template's resource is associated with a
    single ``{vm-type}`` and a single internal network, the Resource ID **MUST**
    contain both the ``{vm-type}`` and the ``int_{network-role}`` and

    - the ``{vm-type}`` **MUST** appear before the ``int_{network-role}`` and
      **MUST** be separated by an underscore '_'

      - (e.g., ``{vm-type}_int_{network-role}``,
        ``{vm-type}_{index}_int_{network-role}``)

    - note that an ``{index}`` value **MAY** separate the
      ``{vm-type}`` and the ``int_{network-role}`` and when this occurs
      underscores **MUST** separate the three values.
      (e.g., ``{vm-type}_{index}_int_{network-role}``).


Resource IDs > Contrail Heat Resources Resource ID Naming Convention > OS::ContrailV2::VirtualNetwork
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-99110`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualNetwork`` Resource ID **MUST** use the naming convention

    1) ``int_{network-role}_network``

    or

    2) ``int_{network-role}_RVN`` where RVN represents Resource Virtual
       Network

    VNF Heat Orchestration Templates can only create internal networks.
    There is no ``{index}`` after ``{network-role}`` because ``{network-role}``
    **MUST** be unique in the scope of the VNF's
    Heat Orchestration Template.

    Note that option 1 is preferred.


Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Neutron::Net
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-25720`

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Net``
    Resource ID **MUST** use the naming convention

    * ``int_{network-role}_network``

    VNF Heat Orchestration Templates can only create internal networks.
    There is no ``{index}`` after ``{network-role}`` because ``{network-role}``
    **MUST** be unique in the scope of the VNF's
    Heat Orchestration Template.


Resource: OS::Neutron::Port - Parameters > Introduction > Items to Note
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-48880`

    If a VNF's Port is attached to an external network and the port's
    IP addresses are assigned by ONAP's SDN-Controller,
    the ``OS::Neutron::Port`` Resource's

    * property ``fixed_ips`` map property ``ip_address`` **MUST** be used
    * property ``fixed_ips`` map property ``subnet``
      **MUST NOT** be used


.. container:: note

    :need:`R-45602`

    If a VNF's Port is attached to a network (internal or external)
    and the port's IP addresses are cloud assigned by OpenStack's DHCP
    Service, the ``OS::Neutron::Port`` Resource's

    * property ``fixed_ips`` map property ``ip_address`` **MUST NOT** be used
    * property ``fixed_ips`` map property ``subnet``
      **MAY** be used


.. container:: note

    :need:`R-70964`

    If a VNF's Port is attached to an internal network and the port's
    IP addresses are statically assigned by the VNF's Heat Orchestration\
    Template (i.e., enumerated in the Heat Orchestration Template's
    environment file), the ``OS::Neutron::Port`` Resource's

    * property ``fixed_ips`` map property ``ip_address`` **MUST** be used
    * property ``fixed_ips`` map property ``subnet``
      **MUST NOT** be used


Resource: OS::Neutron::Port - Parameters > Property: allowed_address_pairs, Map Property: ip_address > VIP Assignment, External Networks, Supported by Automation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-35735`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv6 Virtual IP (VIP)
    address is assigned via ONAP automation
    using the property ``allowed_address_pairs``
    map property ``ip_address``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_{network-role}_floating_v6_ip``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as type ``string``.


.. container:: note

    :need:`R-41492`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv4 Virtual IP (VIP)
    address is assigned via ONAP automation
    using the property ``allowed_address_pairs``
    map property ``ip_address`` and
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_{network-role}_floating_ip``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as type ``string``.


Resource: OS::Neutron::Port - Parameters > Property: fixed_ips, Map Property: ip_address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-28795`

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_int_{network-role}_ip_{index}``
    **MUST** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-39841`

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_{network-role}_ip_{index}``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-85235`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv4 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
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
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the internal
        network
      * the value for ``{index`` must start at zero (0) and increment by one


.. container:: note

    :need:`R-90206`

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_int_{network-role}_int_ips``
    **MUST** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-23503`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
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

    :need:`R-87123`

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_{network-role}_v6_ip_{index}``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-98569`

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_int_{network-role}_v6_ips``
    **MUST** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-93496`

    The VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    property ``fixed_ips``
    map property ``ip_address``
    parameter associated with an internal network, i.e.,

     * ``{vm-type}_int_{network-role}_ip_{index}``
     * ``{vm-type}_int_{network-role}_v6_ip_{index}``
     * ``{vm-type}_int_{network-role}_ips``
     * ``{vm-type}_int_{network-role}_v6_ips``


    **MUST** be enumerated in the Heat Orchestration
    Template's Environment File and IP addresses **MUST** be
    assigned.


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

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the external
        network
      * the value for ``{index}`` must start at zero (0) and increment by one


.. container:: note

    :need:`R-29765`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
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
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network
      * the value for ``{index}`` must start at zero (0) and increment by one


.. container:: note

    :need:`R-62590`

    The VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    property ``fixed_ips``
    map property ``ip_address``
    parameter associated with an external network, i.e.,

     * ``{vm-type}_{network-role}_ip_{index}``
     * ``{vm-type}_{network-role}_v6_ip_{index}``
     * ``{vm-type}_{network-role}_ips``
     * ``{vm-type}_{network-role}_v6_ips``


    **MUST NOT** be enumerated in the Heat Orchestration
    Template's Environment File.  ONAP provides the IP address
    assignments at orchestration time.


.. container:: note

    :need:`R-04697`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv4 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
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

    :need:`R-97201`

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_int_{network-role}_v6_ip_{index}``
    **MUST** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-27818`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see RRequirements R-52425 and R-46461),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
    ``string``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_v6_ip_{index}``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the internal
        network
      * the value for ``{index}`` must start at zero (0) and increment by one


Resource: OS::Neutron::Port - Parameters > Property: fixed_ips, Map Property: subnet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-84123`

    When

      * the VNF's Heat Orchestration Template's
        resource ``OS::Neutron::Port`` in an Incremental Module is attaching
        to an internal network (per the ONAP definition, see
        Requirements R-52425 and R-46461)
        that is created in the Base Module, AND
      * an IPv4 address is being cloud assigned by OpenStack's DHCP Service AND
      * the internal network IPv4 subnet is to be specified
        using the property ``fixed_ips`` map property ``subnet``,

    the parameter **MUST** follow the naming convention

      * ``int_{network-role}_subnet_id``

    where

      * ``{network-role}`` is the network role of the internal network

    Note that the parameter **MUST** be defined as an ``output`` parameter in
    the base module.


.. container:: note

    :need:`R-62802`

    When the VNF's Heat Orchestration Template's
    resource ``OS::Neutron::Port`` is attaching
    to an external network (per the ONAP definition, see
    Requirement R-57424),
    and an IPv4 address is being cloud assigned by OpenStack's DHCP Service
    and the external network IPv4 subnet is to be specified
    using the property ``fixed_ips``
    map property ``subnet``, the parameter
    **MUST** follow the naming convention

      * ``{network-role}_subnet_id``

    where

      * ``{network-role}`` is the network role of the network.


.. container:: note

    :need:`R-22288`

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``subnet`` parameter
    ``int_{network-role}_v6_subnet_id``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-76160`

    When

      * the VNF's Heat Orchestration Template's
        resource ``OS::Neutron::Port`` in an Incremental Module is attaching
        to an internal network (per the ONAP definition, see Requirements
        R-52425 and R-46461)
        that is created in the Base Module, AND
      * an IPv6 address is being cloud assigned by OpenStack's DHCP Service AND
      * the internal network IPv6 subnet is to be specified
        using the property ``fixed_ips`` map property ``subnet``,

    the parameter **MUST** follow the naming convention
    ``int_{network-role}_v6_subnet_id``,
    where ``{network-role}`` is the network role of the internal network.

    Note that the parameter **MUST** be defined as an ``output`` parameter in
    the base module.


.. container:: note

    :need:`R-15287`

    When the VNF's Heat Orchestration Template's
    resource ``OS::Neutron::Port`` is attaching
    to an external network (per the ONAP definition, see
    Requirement R-57424),
    and an IPv6 address is being cloud assigned by OpenStack's DHCP Service
    and the external network IPv6 subnet is to be specified
    using the property ``fixed_ips``
    map property ``subnet``, the parameter
    **MUST** follow the naming convention

      * ``{network-role}_v6_subnet_id``

    where

      * ``{network-role}`` is the network role of the network.


.. container:: note

    :need:`R-83677`

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``subnet`` parameter
    ``{network-role}_subnet_id``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-80829`

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``subnet`` parameter
    ``{network-role}_v6_subnet_id``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


.. container:: note

    :need:`R-38236`

    The VNF's Heat Orchestration Template's
    resource ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``subnet`` parameter
    **MUST** be declared type ``string``.


.. container:: note

    :need:`R-69634`

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``subnet`` parameter
    ``int_{network-role}_subnet_id``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


Resource: OS::Neutron::Port - Parameters > Property: network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-29872`

    The VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    property ``network``
    parameter **MUST NOT** be enumerated in the Heat Orchestration
    Template's Environment File.


.. container:: note

    :need:`R-62983`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424), the
    ``network`` parameter name **MUST**

      * follow the naming convention ``{network-role}_net_id`` if the Neutron
        network UUID value is used to reference the network
      * follow the naming convention ``{network-role}_net_name`` if the
        OpenStack network name is used to reference the network.

    where ``{network-role}`` is the network-role of the external network
    and a ``get_param`` **MUST** be used as the intrinsic function.


.. container:: note

    :need:`R-93177`

    When the VNF's Heat Orchestration Template's resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and the internal network is created in the
    same Heat Orchestration Template as the ``OS::Neutron::Port``,
    the ``network`` property value **MUST** obtain the UUID
    of the internal network by using the intrinsic function
    ``get_resource``
    and referencing the Resource ID of the internal network.


.. container:: note

    :need:`R-86182`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and the internal network is created in a
    different Heat Orchestration Template than the ``OS::Neutron::Port``,
    the ``network`` parameter name **MUST**

      * follow the naming convention ``int_{network-role}_net_id`` if the Neutron
        network UUID value is used to reference the network
      * follow the naming convention ``int_{network-role}_net_name`` if the
        OpenStack network name in is used to reference the network.

    where ``{network-role}`` is the network-role of the internal network and
    a ``get_param`` **MUST** be used as the intrinsic function.


Resource: OS::Nova::Server - Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-304011`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource's

    * Resource ID
    * property ``image`` parameter name
    * property ``flavor`` parameter name
    * property ``name`` parameter name


    **MUST** contain the identical ``{vm-type}``
    and **MUST** follow the naming conventions defined
    in R-58670, R-45188, R-54171, R-87817, and R-29751.


Resource: OS::Nova::Server - Parameters > Property: Name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-663631`

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``name`` value **MUST** be be obtained via a ``get_param``.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-40899`

    When the VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``name`` parameter is defined as a ``string``, a parameter
    **MUST** be delcared for
    each ``OS::Nova::Server`` resource associated with the ``{vm-type}``.


.. container:: note

    :need:`R-54171`

    When the VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``name`` parameter is defined as a ``string``,
    the parameter name **MUST** follow the naming convention
    ``{vm-type}_name_{index}``, where ``{index}`` is a numeric
    value that starts at
    zero and increments by one.


.. container:: note

    :need:`R-51430`

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property
    ``name`` parameter **MUST** be declared as either type ``string``
    or type ``comma_delimited_list``.


Resource: OS::Nova::Server - Parameters > Property: Name > Contrail Issue with Values for OS::Nova::Server Property Name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-44271`

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property
    ``name`` parameter value **SHOULD NOT** contain special characters
    since the Contrail GUI has a limitation displaying special characters.

    However, if special characters must be used, the only special characters
    supported are: --- \" ! $ ' (\ \ ) = ~ ^ | @ ` { } [ ] > , . _


Resource: OS::Nova::Server - Parameters > Property: availability_zone
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-01359`

    A VNF's Heat Orchestration Template that contains an ``OS::Nova:Server``
    Resource **MAY** define a parameter for the property
    ``availability_zone`` that is not utilized in any ``OS::Nova::Server``
    resources in the Heat Orchestration Template.


.. container:: note

    :need:`R-98450`

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property
    ``availability_zone`` parameter name **MUST** follow the naming convention
    ``availability_zone_{index}`` where the ``{index}``
    **MUST** start at zero and
    increment by one.


Resource: OS::Nova::Server - Parameters > Property: flavor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-481670`

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``flavor`` value **MUST** be be obtained via a ``get_param``.


Resource: OS::Nova::Server - Parameters > Property: image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-901331`

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``image`` value **MUST** be be obtained via a ``get_param``.


Resource: OS::Nova::Server Metadata Parameters > environment_context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-13194`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``environment_context`` **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.


.. container:: note

    :need:`R-56183`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata``key/value pair ``environment_context``
    parameter ``environment_context`` **MUST NOT**
    have parameter constraints defined.


.. container:: note

    :need:`R-20308`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``environment_context``
    parameter **MUST** be declared as ``environment_context`` and the
    parameter type **MUST** be defined as type: ``string``.


Resource: OS::Nova::Server Metadata Parameters > vf_module_id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-86237`

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vf_module_id`` is passed into a
    Nested YAML
    file, the key/value pair name ``vf_module_id`` **MUST NOT** change.


.. container:: note

    :need:`R-71493`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` **MUST**
    contain the key/value pair ``vf_module_id``
    and the value MUST be obtained via a ``get_param``.


.. container:: note

    :need:`R-82134`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource property
    ``metadata`` key/value pair ``vf_module_id`` parameter **MUST**
    be declared as ``vf_module_id`` and the parameter **MUST**
    be defined as type: ``string``.


.. container:: note

    :need:`R-98374`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource property
    ``metadata`` key/value pair ``vf_module_id`` parameter ``vf_module_id``
    **MUST NOT**
    have parameter constraints defined.


.. container:: note

    :need:`R-72871`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource property
    ``metadata`` key/value pair ``vf_module_id`` parameter ``vf_module_id``
    **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.


Resource: OS::Nova::Server Metadata Parameters > vf_module_index
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-37039`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vf_module_index`` parameter
    ``vf_module_index`` **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.


.. container:: note

    :need:`R-09811`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vf_module_index`` **MUST NOT**
    have parameter constraints defined.


.. container:: note

    :need:`R-22441`

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vf_module_index`` is passed into a
    Nested YAML file, the key/value pair
    ``vf_module_index`` **MUST NOT** change.


.. container:: note

    :need:`R-50816`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource  property ``metadata`` **MAY**
    contain the key/value pair ``vf_module_index``
    and the value **MUST** be obtained via a ``get_param``.


.. container:: note

    :need:`R-55306`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vf_module_index`` **MUST NOT**
    be used in a ``OS::Cinder::Volume`` resource and **MUST NOT** be
    used in VNF's Volume template;
    it is not supported.


.. container:: note

    :need:`R-54340`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vf_module_index`` parameter **MUST**
    be declared as ``vf_module_index`` and the parameter **MUST** be
    defined as type: ``number``.


Resource: OS::Nova::Server Metadata Parameters > vf_module_name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-68023`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` **SHOULD**
    contain the key/value pair ``vf_module_name`` and the value **MUST**
    be obtained via a ``get_param``.


.. container:: note

    :need:`R-49177`

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vf_module_name`` is passed into a
    Nested YAML
    file, the key/value pair name ``vf_module_name`` **MUST NOT** change.


.. container:: note

    :need:`R-80374`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vf_module_name``
    parameter ``vf_module_name`` **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.


.. container:: note

    :need:`R-15480`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vf_module_name`` parameter ``vf_module_name``
    **MUST NOT** have parameter constraints defined.


.. container:: note

    :need:`R-39067`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vf_module_name`` parameter **MUST** be
    declared as ``vf_module_name`` and the parameter **MUST**
    be defined as type: ``string``.


Resource: OS::Nova::Server Metadata Parameters > vm_role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-67597`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vm_role`` parameter ``vm_role``
    **MUST NOT** have parameter constraints defined.


.. container:: note

    :need:`R-70757`

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vm_role`` is passed into a Nested
    YAML
    file, the key/value pair name ``vm_role`` **MUST NOT** change.


.. container:: note

    :need:`R-86476`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vm_role`` value **MUST**
    only contain alphanumeric characters and underscores (i.e., '_').


.. container:: note

    :need:`R-95430`

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource property
    ``metadata`` key/value pair ``vm_role`` value is obtained via
    ``get_param``, the parameter **MUST** be declared as ``vm_role``
    and the parameter **MUST** be defined as type: ``string``.


.. container:: note

    :need:`R-85328`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource property
    ``metadata`` **MAY**
    contain the key/value pair ``vm_role`` and the value **MUST** be
    obtained either via

    - ``get_param``
    - hard coded in the key/value pair ``vm_role``.


Resource: OS::Nova::Server Metadata Parameters > vnf_id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-44491`

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vnf_id`` is passed into a Nested YAML
    file, the key/value pair name ``vnf_id`` **MUST NOT** change.


.. container:: note

    :need:`R-20856`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource property
    ``metadata`` key/value pair ``vnf_id`` parameter ``vnf_id`` **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.


.. container:: note

    :need:`R-07507`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource property
    ``metadata`` key/value pair ``vnf_id`` parameter
    **MUST** be declared as ``vnf_id`` and the parameter **MUST**
    be defined as type: ``string``.


.. container:: note

    :need:`R-37437`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource property ``metadata`` **MUST**
    contain the  key/value pair ``vnf_id``
    and the value **MUST** be obtained via a ``get_param``.


.. container:: note

    :need:`R-55218`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource property
    ``metadata`` key/value pair ``vnf_id`` parameter ``vnf_id`` **MUST NOT**
    have parameter constraints defined.


Resource: OS::Nova::Server Metadata Parameters > vnf_name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-36542`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vnf_name`` parameter
    ``vnf_name`` **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.


.. container:: note

    :need:`R-72483`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource property
    ``metadata`` **MUST** contain the key/value pair ``vnf_name`` and the
    value **MUST** be obtained via a ``get_param``.


.. container:: note

    :need:`R-44318`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vnf_name``
    parameter ``vnf_name`` **MUST NOT**
    have parameter constraints defined.


.. container:: note

    :need:`R-62428`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vnf_name`` parameter **MUST**
    be declared as ``vnf_name`` and the parameter **MUST** be defined as
    type: ``string``.


.. container:: note

    :need:`R-16576`

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vnf_name`` is passed into a Nested YAML
    file, the key/value pair name ``vnf_name`` **MUST NOT** change.


Resource: OS::Nova::Server Metadata Parameters > workload_context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-74978`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``workload_context``
    parameter **MUST**
    be declared as ``workload_context`` and the parameter **MUST**
    be defined as type: ``string``.


.. container:: note

    :need:`R-02691`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``workload_context``
    parameter ``workload_context`` **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.


.. container:: note

    :need:`R-34055`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``workload_context``
    parameter ``workload_context`` **MUST NOT**
    have parameter constraints defined.


.. container:: note

    :need:`R-75202`

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``workload_context``
    is passed into a Nested YAML
    file, the key/value pair name ``workload_context`` **MUST NOT** change.


VNF On-boarding and package management > Resource Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-22346`

    The VNF package MUST provide :ref:`VES Event Registration <ves_event_registration_3_2>`
    for all VES events provided by that xNF.


.. container:: note

    :need:`R-384337`

    The VNF documentation **MUST** contain a list of the files within the VNF
    package that are static during the VNF's runtime.


VNF On-boarding and package management > Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-43958`

    The xNF Package **MUST** include documentation describing
    the tests that were conducted by the xNF provider and the test results.


VNF Resiliency > Virtual Function - Container Recovery Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-46851`

    The VNF **MUST** support ONAP Controller's Evacuate command.


.. container:: note

    :need:`R-48761`

    The VNF **MUST** support ONAP Controller's Snapshot command.


VNF Security > VNF API Security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-21210`

    The VNF **MUST** implement the following input validation control
    on APIs: Validate that any input file has a correct and valid
    Multipurpose Internet Mail Extensions (MIME) type. Input files
    should be tested for spoofed MIME types.


.. container:: note

    :need:`R-54930`

    The VNF **MUST** implement the following input validation controls:
    Do not permit input that contains content or characters inappropriate
    to the input expected by the design. Inappropriate input, such as
    SQL expressions, may cause the system to execute undesirable and
    unauthorized transactions against the database or allow other
    inappropriate access to the internal network (injection attacks).


.. container:: note

    :need:`R-43884`

    The VNF **SHOULD** integrate with the Operator's authentication and
    authorization services (e.g., IDAM).


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-02137

    The VNF **MUST** implement all monitoring and logging as
    described in the Security Analytics section.


.. container:: note

    R-15659

    The VNF **MUST** restrict changing the criticality level of
    a system security alarm to administrator(s).


.. container:: note

    R-19367

    The VNF **MUST** monitor API invocation patterns to detect
    anomalous access patterns that may represent fraudulent access or
    other types of attacks, or integrate with tools that implement anomaly
    and abuse detection.


.. container:: note

    R-19804

    The VNF **MUST** validate the CA signature on the certificate,
    ensure that the date is within the validity period of the certificate,
    check the Certificate Revocation List (CRL), and recognize the identity
    represented by the certificate where PKI-based authentication is used.


.. container:: note

    R-23772

    The VNF **MUST** validate input at all layers implementing VNF APIs.


.. container:: note

    R-25878

    The VNF **MUST** use certificates issued from publicly
    recognized Certificate Authorities (CA) for the authentication process
    where PKI-based authentication is used.


.. container:: note

    R-37608

    The VNF **MUST** provide a mechanism to restrict access based
    on the attributes of the VNF and the attributes of the subject.


.. container:: note

    R-78066

    The VNF **MUST** support requests for information from law
    enforcement and government agencies.


.. container:: note

    R-87135

    The VNF **MUST** comply with NIST standards and industry
    best practices for all implementations of cryptography.


VNF Security > VNF Cryptography Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-48080`

    The VNF **SHOULD** support an automated certificate management protocol
    such as CMPv2, Simple Certificate Enrollment Protocol (SCEP) or
    Automated Certificate Management Environment (ACME).


.. container:: note

    :need:`R-93860`

    The VNF **SHOULD** provide the capability to integrate with an
    external encryption service.


.. container:: note

    :need:`R-41994`

    The VNF **MUST** support the use of X.509 certificates issued from any
    Certificate Authority (CA) that is compliant with RFC5280, e.g., a public
    CA such as DigiCert or Let's Encrypt, or an RFC5280  compliant Operator
    CA.

    Note: The VNF provider cannot require the use of self-signed certificates
    in an Operator's run time environment.


.. container:: note

    :need:`R-49109`

    The VNF **MUST** support HTTP/S using TLS v1.2 or higher
    with strong cryptographic ciphers.


VNF Security > VNF Data Protection Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-69610`

    The VNF **MUST** provide the capability of using X.509 certificates
    issued by an external Certificate Authority.


.. container:: note

    :need:`R-58964`

    The VNF **MUST** provide the capability to restrict read
    and write access to data handled by the VNF.


.. container:: note

    :need:`R-47204`

    The VNF **MUST** be capable of protecting the confidentiality and integrity
    of data at rest and in transit from unauthorized access and modification.


.. container:: note

    :need:`R-32641`

    The VNF **MUST** provide the capability to encrypt data on
    non-volatile memory.Non-volative memory is storage that is
    capable of retaining data without electrical power, e.g.
    Complementary metal-oxide-semiconductor (CMOS) or hard drives.


.. container:: note

    :need:`R-73067`

    The VNF **MUST** use NIST and industry standard cryptographic
    algorithms and standard modes of operations when implementing
    cryptography.


.. container:: note

    :need:`R-95864`

    The VNF **MUST** support digital certificates that comply with X.509
    standards.


.. container:: note

    :need:`R-02170`

    The VNF **MUST** use, whenever possible, standard implementations
    of security applications, protocols, and formats, e.g., S/MIME, TLS, SSH,
    IPSec, X.509 digital certificates for cryptographic implementations.
    These implementations must be purchased from reputable vendors or obtained
    from reputable open source communities and must not be developed in-house.


.. container:: note

    :need:`R-70933`

    The VNF **MUST** provide the ability to migrate to newer
    versions of cryptographic algorithms and protocols with minimal impact.


.. container:: note

    :need:`R-12467`

    The VNF **MUST NOT** use compromised encryption algorithms.
    For example, SHA, DSS, MD5, SHA-1 and Skipjack algorithms.
    Acceptable algorithms can be found in the NIST FIPS publications
    (https://csrc.nist.gov/publications/fips) and in the
    NIST Special Publications (https://csrc.nist.gov/publications/sp).


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-22645

    The VNF **SHOULD** use commercial algorithms only when there
    are no applicable governmental standards for specific cryptographic
    functions, e.g., public key cryptography, message digests.


.. container:: note

    R-99112

    The VNF **MUST** provide the capability to restrict access
    to data to specific users.


VNF Security > VNF General Security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-118669`

    Login access (e.g., shell access) to the operating system layer, whether
    interactive or as part of an automated process, **MUST** be through an
    encrypted protocol such as SSH or TLS.


.. container:: note

    :need:`R-240760`

    The VNF **MUST NOT** contain any backdoors.


.. container:: note

    :need:`R-256267`

    If SNMP is utilized, the VNF **MUST** support at least SNMPv3 with
    message authentication.


.. container:: note

    :need:`R-258686`

    The VNF application processes **MUST NOT** run as root.


.. container:: note

    :need:`R-343842`

    The VNF **MUST**, after a successful login at command line or a GUI,
    display the last valid login date and time and the number of unsuccessful
    attempts since then made with that user's ID. This requirement is only
    applicable when the user account is defined locally in the VNF.


.. container:: note

    :need:`R-638682`

    The VNF **MUST** log any security event required by the VNF Requirements to
    Syslog using LOG_AUTHPRIV for any event that would contain sensitive
    information and LOG_AUTH for all other relevant events.


.. container:: note

    :need:`R-756950`

    The VNF **MUST** be operable without the use of Network File System (NFS).


.. container:: note

    :need:`R-842258`

    The VNF **MUST** include a configuration, e.g., a heat template or CSAR
    package, that specifies the targetted parameters, e.g. a limited set of
    ports, over which the VNF will communicate (including internal, external
    and management communication).


.. container:: note

    :need:`R-872986`

    The VNF **MUST** store Authentication Credentials used to authenticate to
    other systems encrypted except where there is a technical need to store
    the password unencrypted in which case it must be protected using other
    security techniques that include the use of file and directory permissions.
    Ideally, credentials SHOULD rely on a HW Root of Trust, such as a
    TPM or HSM.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-62498`

    The VNF **MUST** support encrypted access protocols, e.g., TLS,
    SSH, SFTP.


.. container:: note

    :need:`R-23882`

    The VNF **SHOULD** provide the capability for the Operator to run security
    vulnerability scans of the operating system and all application layers.


.. container:: note

    :need:`R-61354`

    The VNF **MUST** provide a mechanism (e.g., access control list) to
    permit and/or restrict access to services on the VNF by source,
    destination, protocol, and/or port.


.. container:: note

    :need:`R-19768`

    The VNF **SHOULD** support network segregation, i.e., separation of OA&M
    traffic from signaling and payload traffic, using technologies such as
    VPN and VLAN.


.. container:: note

    :need:`R-19082`

    The VNF **MUST** allow the Operator to disable or remove any security
    testing tools or programs included in the VNF, e.g., password cracker,
    port scanner.


.. container:: note

    :need:`R-86261`

    The VNF **MUST** support the ability to prohibit remote access to the VNF
    via a host based security mechanism.


.. container:: note

    :need:`R-99771`

    The VNF **MUST** have all code (e.g., QCOW2) and configuration files
    (e.g., HEAT template, Ansible playbook, script) hardened, or with
    documented recommended configurations for hardening and interfaces that
    allow the Operator to harden the VNF. Actions taken to harden a system
    include disabling all unnecessary services, and changing default values
    such as default credentials and community strings.


.. container:: note

    :need:`R-80335`

    For all GUI and command-line interfaces, the VNF **MUST** provide the
    ability to present a warning notice that is set by the Operator. A warning
    notice is a formal statement of resource intent presented to everyone
    who accesses the system.


.. container:: note

    :need:`R-21819`

    The VNF **MUST** provide functionality that enables the Operator to comply
    with requests for information from law enforcement and government agencies.


.. container:: note

    :need:`R-23740`

    The VNF **MUST** implement and enforce the principle of least privilege
    on all protected interfaces.


.. container:: note

    :need:`R-40813`

    The VNF **SHOULD** support the use of virtual trusted platform
    module.


.. container:: note

    :need:`R-69649`

    The VNF Provider **MUST** have patches available for vulnerabilities
    in the VNF as soon as possible. Patching shall be controlled via change
    control process with vulnerabilities disclosed along with
    mitigation recommendations.


.. container:: note

    :need:`R-92207`

    The VNF **SHOULD** provide a mechanism that enables the operators to
    perform automated system configuration auditing at configurable time
    intervals.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-26586

    The VNF **SHOULD** support the ability to work with aliases
    (e.g., gateways, proxies) to protect and encapsulate resources.


.. container:: note

    R-33981

    The VNF **SHOULD** interoperate with various access control
    mechanisms for the Network Cloud execution environment (e.g.,
    Hypervisors, containers).


.. container:: note

    R-35144

    The VNF **MUST**, if not using the NCSP's IDAM API, comply
    with the NCSP's credential management policy.


.. container:: note

    R-39342

    The VNF **MUST**, if not using the NCSP's IDAM API, comply
    with "password changes (includes default passwords)" policy. Products
    will support password aging, syntax and other credential management
    practices on a configurable basis.


.. container:: note

    R-40521

    The VNF **MUST**, if not using the NCSP's IDAM API, support
    use of common third party authentication and authorization tools such
    as TACACS+, RADIUS.


.. container:: note

    R-42681

    The VNF **MUST** use the NCSP's IDAM API or comply with
    the requirements if not using the NCSP's IDAM API, for identification,
    authentication and access control of OA&M and other system level
    functions.


.. container:: note

    R-49956

    The VNF **MUST** pass all access to applications (Bearer,
    signaling and OA&M) through various security tools and platforms from
    ACLs, stateful firewalls and application layer gateways depending on
    manner of deployment. The application is expected to function (and in
    some cases, interwork) with these security tools.


.. container:: note

    R-52085

    The VNF **MUST**, if not using the NCSP's IDAM API, provide
    the ability to support Multi-Factor Authentication (e.g., 1st factor =
    Software token on device (RSA SecureID); 2nd factor = User Name+Password,
    etc.) for the users.


.. container:: note

    R-55830

    The VNF **MUST** distribute all production code from NCSP
    internal sources only. No production code, libraries, OS images, etc.
    shall be distributed from publically accessible depots.


.. container:: note

    R-63217

    The VNF **MUST**, if not using the NCSP's IDAM API, support
    logging via ONAP for a historical view of "who did what and when."


.. container:: note

    R-68589

    The VNF **MUST**, if not using the NCSP's IDAM API, support
    User-IDs and passwords to uniquely identify the user/application. VNF
    needs to have appropriate connectors to the Identity, Authentication
    and Authorization systems that enables access at OS, Database and
    Application levels as appropriate.


.. container:: note

    R-85633

    The VNF **MUST** implement Data Storage Encryption
    (database/disk encryption) for Sensitive Personal Information (SPI)
    and other subscriber identifiable data.

    Note: Subscribers SPI/data must be encrypted at rest, and other
    subscriber identifiable data should be encrypted at rest. Other
    data protection requirements exist and should be well understood
    by the developer.


VNF Security > VNF Identity and Access Management Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-231402`

    The VNF **MUST** provide a means for the user to explicitly logout, thus
    ending that session for that authenticated user.


.. container:: note

    :need:`R-45719`

    The VNF **MUST**, if not integrated with the Operator's Identity and Access
    Management system, or enforce a configurable "terminate idle sessions"
    policy by terminating the session after a configurable period of inactivity.


.. container:: note

    :need:`R-479386`

    The VNF **MUST NOT** display "Welcome" notices or messages that could
    be misinterpreted as extending an invitation to unauthorized users.


.. container:: note

    :need:`R-581188`

    A failed authentication attempt **MUST NOT** identify the reason for the
    failure to the user, only that the authentication failed.


.. container:: note

    :need:`R-814377`

    The VNF **MUST** have the capability of allowing the Operator to create,
    manage, and automatically provision user accounts using an Operator
    approved identity lifecycle management tool using a standard protocol,
    e.g., NETCONF API.


.. container:: note

    :need:`R-844011`

    The VNF MUST not store authentication credentials to itself in clear
    text or any reversible form and must use salting.


.. container:: note

    :need:`R-931076`

    The VNF **MUST** support account names that contain at least A-Z, a-z,
    0-9 character sets and be at least 6 characters in length.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-23135`

    The VNF **MUST**, if not integrated with the Operator's identity and
    access management system, authenticate all access to protected GUIs, CLIs,
    and APIs.


.. container:: note

    :need:`R-15671`

    The VNF **MUST** provide access controls that allow the Operator
    to restrict access to VNF functions and data to authorized entities.


.. container:: note

    :need:`R-78010`

    The VNF **MUST** integrate with standard identity and access management
    protocols such as LDAP, TACACS+, Windows Integrated Authentication
    (Kerberos), SAML federation, or OAuth 2.0.


.. container:: note

    :need:`R-86835`

    The VNF **MUST** set the default settings for user access
    to deny authorization, except for a super user type of account.
    When a VNF is added to the network, nothing should be able to use
    it until the super user configures the VNF to allow other users
    (human and application)  have access.


.. container:: note

    :need:`R-59391`

    The VNF **MUST NOT** allow the assumption of the permissions of another
    account to mask individual accountability. For example, use SUDO when a
    user requires elevated permissions such as root or admin.


.. container:: note

    :need:`R-75041`

    The VNF **MUST**, if not integrated with the Operator's Identity and
    Access Management system, support configurable password expiration.


.. container:: note

    :need:`R-71787`

    Each architectural layer of the VNF (eg. operating system, network,
    application) **MUST** support access restriction independently of all
    other layers so that Segregation of Duties can be implemented.


.. container:: note

    :need:`R-79107`

    The VNF **MUST**, if not integrated with the Operator's Identity
    and Access Management system, support the ability to disable the
    userID after a configurable number of consecutive unsuccessful
    authentication attempts using the same userID.


.. container:: note

    :need:`R-46908`

    The VNF **MUST**, if not integrated with the Operator's Identity and
    Access Management system, comply with "password complexity" policy. When
    passwords are used, they shall be complex and shall at least meet the
    following password construction requirements: (1) be a minimum configurable
    number of characters in length, (2) include 3 of the 4 following types of
    characters: upper-case alphabetic, lower-case alphabetic, numeric, and
    special, (3) not be the same as the UserID with which they are associated
    or other common strings as specified by the environment, (4) not contain
    repeating or sequential characters or numbers, (5) not to use special
    characters that may have command functions, and (6) new passwords must
    not contain sequences of three or more characters from the previous
    password.


.. container:: note

    :need:`R-85419`

    The VNF **SHOULD** support OAuth 2.0 authorization using an external
    Authorization Server.


.. container:: note

    :need:`R-98391`

    The VNF **MUST**, if not integrated with the Operator's Identity and
    Access Management system, support Role-Based Access Control to enforce
    least privilege.


.. container:: note

    :need:`R-99174`

    The VNF **MUST**, if not integrated with the Operator's Identity and
    Access Management system, support the creation of multiple IDs so that
    individual accountability can be supported.


.. container:: note

    :need:`R-81147`

    The VNF **MUST** support strong authentication, also known as
    multifactor authentication, on all protected interfaces exposed by the
    VNF for use by human users. Strong authentication uses at least two of the
    three different types of authentication factors in order to prove the
    claimed identity of a user.


.. container:: note

    :need:`R-42874`

    The VNF **MUST** allow the Operator to restrict access based on
    the assigned permissions associated with an ID in order to support
    Least Privilege (no more privilege than required to perform job
    functions).


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-05470

    The VNF **MUST** host connectors for access to the database layer.


.. container:: note

    R-14025

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Session Hijacking.


.. container:: note

    R-19790

    The VNF **MUST NOT** include authentication credentials
    in security audit logs, even if encrypted.


.. container:: note

    R-24825

    The VNF **MUST** provide Context awareness data (device,
    location, time, etc.) and be able to integrate with threat detection system.


.. container:: note

    R-29301

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Password Attacks.


.. container:: note

    R-31412

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for XSS / CSRF.


.. container:: note

    R-31751

    The VNF **MUST** subject VNF provider access to privilege
    reconciliation tools to prevent access creep and ensure correct
    enforcement of access policies.


.. container:: note

    R-44032

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Man in the Middle (MITM).


.. container:: note

    R-45496

    The VNF **MUST** host connectors for access to the OS (Operating System) layer.


.. container:: note

    R-49945

    The VNF **MUST** authorize VNF provider access through a
    client application API by the client application owner and the resource
    owner of the VNF before provisioning authorization through Role Based
    Access Control (RBAC), Attribute Based Access Control (ABAC), or other
    policy based mechanism.


.. container:: note

    R-51883

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Replay.


.. container:: note

    R-58977

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Eavesdropping.


.. container:: note

    R-58998

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Malware (Key Logger).


.. container:: note

    R-64503

    The VNF **MUST** provide minimum privileges for initial
    and default settings for new user accounts.


.. container:: note

    R-72243

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Phishing / SMishing.


.. container:: note

    R-73541

    The VNF **MUST** use access controls for VNFs and their
    supporting computing systems at all times to restrict access to
    authorized personnel only, e.g., least privilege. These controls
    could include the use of system configuration or access control
    software.


.. container:: note

    R-77157

    The VNF **MUST** conform to approved request, workflow
    authorization, and authorization provisioning requirements when
    creating privileged users.


.. container:: note

    R-85028

    The VNF **MUST** authenticate system to system access and
    do not conceal a VNF provider user's individual accountability for
    transactions.


.. container:: note

    R-89753

    The VNF **MUST NOT** install or use systems, tools or
    utilities capable of capturing or logging data that was not created
    by them or sent specifically to them in production, without
    authorization of the VNF system owner.


.. container:: note

    R-95105

    The VNF **MUST** host connectors for access to the application layer.


VNF Security > VNF Security Analytics Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-303569`

    The VNF **MUST** log the Source IP address in the security audit logs.


.. container:: note

    :need:`R-465236`

    The VNF **SHOULD** provide the capability of maintaining the integrity of
    its static files using a cryptographic method.


.. container:: note

    :need:`R-629534`

    The VNF **MUST** be capable of automatically synchronizing the system clock
    daily with the Operator's trusted time source, to assure accurate time
    reporting in log files. It is recommended that Coordinated Universal Time
    (UTC) be used where possible, so as to eliminate ambiguity owing to daylight
    savings time.


.. container:: note

    :need:`R-703767`

    The VNF **MUST** have the capability to securely transmit the security logs
    and security events to a remote system before they are purged from the
    system.


.. container:: note

    :need:`R-859208`

    The VNF **MUST** log automated remote activities performed with
    elevated privileges.


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-07617`

    The VNF **MUST** log success and unsuccessful creation, removal, or
    change to the inherent privilege level of users.


.. container:: note

    :need:`R-22367`

    The VNF **MUST** support detection of malformed packets due to software
    misconfiguration or software vulnerability, and generate an error to the
    syslog console facility.


.. container:: note

    :need:`R-34552`

    The VNF **MUST** be implemented so that it is not vulnerable to OWASP
    Top 10 web application security risks.


.. container:: note

    :need:`R-54520`

    The VNF **MUST** log successful and unsuccessful authentication
    attempts, e.g., authentication associated with a transaction,
    authentication to create a session, authentication to assume elevated
    privilege.


.. container:: note

    :need:`R-58370`

    The VNF **SHOULD** operate with anti-virus software which produces alarms
    every time a virus is detected.


.. container:: note

    :need:`R-94525`

    The VNF **MUST** log connections to the network listeners of the
    resource.


.. container:: note

    :need:`R-43332`

    The VNF **MUST** activate security alarms automatically when
    it detects the successful modification of a critical system or
    application file.


.. container:: note

    :need:`R-41825`

    The VNF **MUST** activate security alarms automatically when
    a configurable number of consecutive unsuccessful login attempts
    is reached.


.. container:: note

    :need:`R-29705`

    The VNF **MUST** restrict changing the criticality level of a
    system security alarm to users with administrative privileges.


.. container:: note

    :need:`R-63330`

    The VNF **MUST** detect when its security audit log storage
    medium is approaching capacity (configurable) and issue an alarm.


.. container:: note

    :need:`R-30932`

    The VNF **MUST** log successful and unsuccessful access to VNF
    resources, including data.


.. container:: note

    :need:`R-04492`

    The VNF **MUST** generate security audit logs that can be sent
    to Security Analytics Tools for analysis.


.. container:: note

    :need:`R-74958`

    The VNF **MUST** activate security alarms automatically when
    it detects an unsuccessful attempt to gain permissions
    or assume the identity of another user.


.. container:: note

    :need:`R-54816`

    The VNF **MUST** support the storage of security audit logs for a
    configurable period of time.


Requirements Removed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    R-08598

    The VNF **MUST** log successful and unsuccessful changes to a privilege level.


.. container:: note

    R-19219

    The VNF **MUST** provide audit logs that include user ID, dates,
    times for log-on and log-off, and terminal location at minimum.


.. container:: note

    R-20912

    The VNF **MUST** support alternative monitoring capabilities
    when VNFs do not expose data or control traffic or use proprietary and
    optimized protocols for inter VNF communication.


.. container:: note

    R-25094

    The VNF **MUST** perform data capture for security functions.


.. container:: note

    R-31961

    The VNF **MUST** support integrated DPI/monitoring functionality
    as part of VNFs (e.g., PGW, MME).


.. container:: note

    R-56786

    The VNF **MUST** implement "Closed Loop" automatic implementation
    (without human intervention) for Known Threats with detection rate in low
    false positives.


.. container:: note

    R-57271

    The VNF **MUST** provide the capability of generating security
    audit logs by interacting with the operating system (OS) as appropriate.


.. container:: note

    R-61648

    The VNF **MUST** support event logging, formats, and delivery
    tools to provide the required degree of event data to ONAP.


{network-role}
^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-26506`

    A VNF's Heat Orchestration Template's ``{network-role}`` **MUST** contain
    only alphanumeric characters and/or underscores '_' and
    **MUST NOT** contain any of the following strings:
    ``_int`` or ``int_`` or ``_int_``.


.. container:: note

    :need:`R-84322`

    A VNF's Heat Orchestration Template's Resource property parameter that
    is associated with an internal network **MUST** include
    ``int_{network-role}`` as part of the parameter name,
    where ``int_`` is a hard coded string.


.. container:: note

    :need:`R-96983`

    A VNF's Heat Orchestration Template's Resource ID that is associated
    with an internal network **MUST** include ``int_{network-role}`` as part
    of the Resource ID, where ``int_`` is a hard coded string.


{vm-type}
^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~


.. container:: note

    :need:`R-82481`

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


.. container:: note

    :need:`R-98407`

    A VNF's Heat Orchestration Template's ``{vm-type}`` **MUST** contain only
    alphanumeric characters and/or underscores '_' and **MUST NOT**
    contain any of the following strings:
    ``_int`` or ``int_`` or ``_int_``.


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

        - Each VM in the "class" **MUST** have the the identical number of
          ports connecting to the identical networks and requiring the identical
          IP address configuration.

