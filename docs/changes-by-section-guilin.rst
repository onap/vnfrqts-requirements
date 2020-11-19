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


Requirement Changes Introduced in Guilin
----------------------------------------

This document summarizes the requirement changes by section that were
introduced between the Frankfurt release and
Guilin release. Click on the requirement number to
navigate to the

.. contents::
    :depth: 2

Summary of Changes
^^^^^^^^^^^^^^^^^^

* **Requirements Added:** 30
* **Requirements Changed:** 51
* **Requirements Removed:** 37


Configuration Management > Ansible Standards and Capabilities > VNF or PNF Configuration via Ansible Requirements > Ansible Client Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-67124`

    The VNF or PNF Provider's Ansible playbooks **MUST** be designed to run
    using an inventory hosts file in a supported format; with group names
    matching VNFC 3-character string adding "vip" for groups with virtual IP
    addresses shared by multiple VMs as seen in examples provided in Appendix.
    

.. container:: note

    :need:`R-94567`

    The VNF or PNF Provider's Ansible playbooks **MUST** be designed to run
    using an inventory hosts file in a supported format with only IP addresses
    or IP addresses and VM/VNF or PNF names.
    

.. container:: note

    :need:`R-24482`

    The VNF or PNF Provider's Ansible playbooks **MUST** be designed to run
    using an inventory hosts file in a supported format; with site group that
    shall be used to add site specific configurations to the target VNF or PNF
    VM(s) as needed.
    

.. container:: note

    :need:`R-82018`

    The VNF or PNF **MUST** load the Ansible Server SSH public key onto VNF or
    PNF VM(s) /root/.ssh/authorized_keys as part of instantiation. Alternative,
    is for Ansible Server SSH public key to be loaded onto VNF or PNF
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

    :need:`R-92866`

    The VNF or PNF Provider **MUST** include as part of post-instantiation
    configuration done by Ansible Playbooks the removal/update of the SSH
    public key from ``/root/.ssh/authorized_keys``, and update of SSH keys
    loaded through instantiation to support Ansible. This may include creating
    Mechanized user ID(s) used by the Ansible Server(s) on VNF VM(s) and
    uploading and installing new SSH keys used by the mechanized use ID(s).
    

Configuration Management > Ansible Standards and Capabilities > VNF or PNF Configuration via Ansible Requirements > Ansible Playbook Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-195620`

    The VNF or PNF Provider's Ansible playbooks **SHOULD** compare the version(s)
    of Ansible that the VNF Provider developed and tested against to the
    ``ansible_version.full`` value during playbook execution, and issue a
    ``WARNING`` message if the operator version is not one of the tested
    versions.
    

.. container:: note

    :need:`R-444446`

    The VNF or PNF Provider's Ansible playbooks **SHOULD** issue log messages
    in the same format as Ansible's default messages:
    ``[<Log Level>]: <message>``

    Example:

       ``[WARNING]: Ansible version 2.9.3 does not match a known,
       tested version: 2.8.1, 2.8.2``
    

.. container:: note

    :need:`R-918136`

    The VNF or PNF Provider's Ansible playbooks **MUST NOT** fail due to
    a mismatched version check as specified in R-918136. The warning message
    should be issued, and the playbook execution should continue as normal.
    

Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-49911`

    The VNF or PNF Provider **MUST** assign a new point release to the updated
    Ansible playbook set. The functionality of a new playbook set must be
    tested before it is deployed to the production.
    

.. container:: note

    :need:`R-24189`

    The VNF or PNF Provider **MUST** deliver a new set of Ansible playbooks that
    includes all updated and unchanged playbooks for any new revision to an
    existing set of playbooks.
    

.. container:: note

    :need:`R-53245`

    The VNF or PNF Provider's Ansible playbooks **MUST NOT** require
    passwords or secrets to be passed in clear text in the command line or
    Rest API request to run the playbook.
    

.. container:: note

    :need:`R-51442`

    The VNF or PNF Provider's Ansible playbooks **SHOULD** be designed to
    automatically 'rollback' to the original state in case of any errors
    for actions that change state of the VNF or PNF (e.g., configure).

    **Note**: In case rollback at the playbook level is not supported or
    possible, the VNF or PNF provider shall provide alternative rollback
    mechanism (e.g., for a small VNF or PNF the rollback mechanism may rely
    on workflow to terminate and re-instantiate VNF VMs and then re-run
    playbook(s)). Backing up updated files is also recommended to support
    rollback when soft rollback is feasible.
    

.. container:: note

    :need:`R-49396`

    The VNF or PNF Provider's Ansible playbooks **MUST** support each APPC/SDN-C
    VNF or PNF action by invocation of **one** playbook [#7.3.4]_. The playbook
    will be responsible for executing all necessary tasks (as well as calling
    other playbooks) to complete the request.
    

.. container:: note

    :need:`R-50252`

    The VNF or PNF Provider's Ansible playbooks **MUST** write to a response
    file in JSON format that will be retrieved and made available by the
    Ansible Server if, as part of a VNF or PNF action (e.g., audit), a playbook
    is required to return any VNF or PNF information/response. The text files
    must be written in the main playbook home directory, in JSON format. The
    JSON file must be created for the VNF or PNF with the name '<VNF or PNF name>_results.txt'. All playbook
    output results, for all VNF VMS or PNF Server/Blades, to be provided as a
    response to the request, must be written to this response file.
    

.. container:: note

    :need:`R-58301`

    The VNF or PNF Provider's Ansible playbooks **SHOULD NOT** make requests to
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

    :need:`R-09209`

    The VNF or PNF Provider's Ansible playbooks **MUST** store any playbook
    configuration data that requires encryption (passwords, secrets, etc.) in
    a JSON (.json), YAML (.yaml|.yml) or INI (.ini) file, which will be placed
    in ``<VNF type>/<Version>/ansible/vars`` directory.
    

.. container:: note

    :need:`R-46823`

    The VNF or PNF Provider's Ansible playbooks **MUST** store passwords and
    other attributes that must remain secret in JSON, YAML or INI with
    differentiated names when passwords and secrets vary from environment to
    environment. Example, name must include <Mechanized user ID>_...json or
    <Mechanized user ID>_...xml when labs and production use different passwords
    and/or secrets. The <Mechanized user ID> is discovered from the environment
    ``/etc/ansible/ansible.cfg`` where the playbook runs.
    

.. container:: note

    :need:`R-48698`

    The VNF or PNF Provider's Ansible playbooks **MUST** utilize information
    from key value pairs that will be provided by the Ansible Server as
    ``extra-vars`` during invocation to execute the desired VNF or PNF action.
    The "extra-vars" attribute-value pairs are passed to the Ansible Server by
    an APPC/SDN-C as part of the Rest API request. If the playbook requires
    files, they must also be supplied using the methodology detailed in the
    Ansible Server API, unless they are bundled with playbooks, example,
    generic templates. Any files containing instance specific info
    (attribute-value pairs), not obtainable
    from any ONAP inventory databases or other sources, referenced and used as
    input by playbooks, shall be provisioned (and distributed) in advance of
    use, e.g., VNF or PNF instantiation. Recommendation is to avoid these
    instance specific, manually created in advance of instantiation, files.
    

.. container:: note

    :need:`R-83092`

    The VNF or PNF Provider's Ansible playbooks **MUST** load passwords
    and other attributes that must remain secret from JSON, YAML or INI files
    that can be encrypted/decrypted using Ansible Vault capabilities.
    

.. container:: note

    :need:`R-39003`

    The VNF or PNF Provider's Ansible playbooks **MUST** store passwords and
    other attributes that must remain secret in JSON, YAML or INI files that
    can be encrypted/decrypted using Ansible Vault capabilities.
    

.. container:: note

    :need:`R-43253`

    The VNF or PNF Provider's Ansible playbooks **MUST** be designed to allow
    Ansible Server to infer failure or success based on the "PLAY_RECAP"
    capability.

    **Note**: There are cases where playbooks need to interpret results
    of a task and then determine success or failure and return result
    accordingly (failure for failed tasks).
    

.. container:: note

    :need:`R-78640`

    The VNF or PNF Provider's Ansible playbooks **SHOULD** provide a single
    YAML or JSON file with all the passwords and secrets to reduce the number
    of files to be decrypted/encrypted before on-boarding into the central
    repository.
    

.. container:: note

    :need:`R-20988`

    The VNF or PNF Provider's Ansible playbooks **MUST** not log or
    display passwords and other attributes that must remain secret when
    running playbook in debug mode.

    NOTE: Use ``no_log: True``
    

.. container:: note

    :need:`R-42333`

    The VNF or PNF Provider's Ansible playbooks that target a subset of VMs (or
    servers/blades) part of a VNF (or PNF) instance **MUST** be designed to use
    the VNF or PNF inventory host file and to use a parameter named
    ``target_vm_list`` to provide the subset of VMs in the VNF instance
    specifically targeted by the playbook.

    NOTE: Example of such playbooks would be playbooks used to configure VMs
    added to a VNF instance as part of a scale-out/up or scale-in/down
    operation. Such playbook is expected to also need to perform
    configuration/reconfiguration tasks part of the base VNF instance build.
    

.. container:: note

    :need:`R-43353`

    The VNF or PNF Provider's Ansible playbooks **MUST** return control only
    after all tasks performed by playbook are fully complete, signaling that the
    playbook completed all tasks. When starting services, return control
    only after all services are up. This is critical for workflows where
    the next steps are dependent on prior tasks being fully completed.
    

.. container:: note

    :need:`R-88786`

    The VNF or PNF Provider's Ansible playbooks **SHOULD** place the passwords
    and secrets to be edited at the top of the single YAML or JSON file with
    all the secrets, and the (default) ones that are to remain unchanged '
    towards the bottom, with commentary separating them.
    

.. container:: note

    :need:`R-33280`

    The VNF or PNF Provider's Ansible playbooks **MUST NOT** contain instance
    specific values that can not be provided by a parameter to the playbook.
    

.. container:: note

    :need:`R-56988`

    The VNF or PNF Provider's Ansible playbooks **MUST** load any configuration
    data that requires encryption (passwords, secrets, etc.) in a JSON (.json),
    YAML (.yaml|.yml) or INI (.ini) file, from the
    ``<VNF type>/<Version>/ansible/vars`` directory.
    

.. container:: note

    :need:`R-02651`

    The VNF or PNF Provider's Ansible playbooks **SHOULD** use available backup
    capabilities to save a copy of configuration files before implementing
    changes to support operations such as backing out of software upgrades,
    configuration changes or other work as this will help backing out of
    configuration changes when needed.
    

Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-40293

    The VNF or PNF **MUST** make available playbooks that conform
    to the ONAP requirement.
    

.. container:: note

    R-49751

    The VNF or PNF **MUST** support Ansible playbooks that are compatible with
    Ansible version 2.6 or later.
    

Monitoring & Management > Bulk Performance Measurement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-75943`

    The VNF or PNF **SHOULD** support the data schema defined in 3GPP TS 32.435 or 3GPP TS 28.532, when
    supporting the event-driven bulk transfer of monitoring data.
    

Monitoring & Management > Monitoring & Management Requirements > Addressing and Delivery Protocol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-01033

    The VNF or PNF **MAY** use another option which is expected to include SFTP
    for asynchronous bulk files, such as bulk files that contain large volumes
    of data collected over a long time interval or data collected across many
    VNFs or PNFs. (Preferred is to reorganize the data into more frequent or more focused
    data sets, and deliver these by REST or TCP as appropriate.)
    

.. container:: note

    R-03070

    The VNF or PNF **MUST**, by ONAP Policy, provide the ONAP addresses
    as data destinations for each VNF or PNF, and may be changed by Policy while
    the VNF or PNF is in operation. We expect the VNF or PNF to be capable of redirecting
    traffic to changed destinations with no loss of data, for example from
    one REST URL to another, or from one TCP host and port to another.
    

.. container:: note

    R-08312

    The VNF or PNF **MAY** use another option which is expected to include REST
    delivery of binary encoded data sets.
    

.. container:: note

    R-63229

    The VNF or PNF **MAY** use another option which is expected to include REST
    for synchronous data, using RESTCONF (e.g., for VNF or PNF state polling).
    

.. container:: note

    R-79412

    The VNF or PNF **MAY** use another option which is expected to include TCP
    for high volume streaming asynchronous data sets and for other high volume
    data sets. TCP delivery can be used for either JSON or binary encoded data
    sets.
    

.. container:: note

    R-81777

    The VNF or PNF **MUST** be configured with initial address(es) to use
    at deployment time. Subsequently, address(es) may be changed through
    ONAP-defined policies delivered from ONAP to the VNF or PNF using PUTs to a
    RESTful API, in the same manner that other controls over data reporting
    will be controlled by policy.
    

.. container:: note

    R-84879

    The VNF or PNF **MUST** have the capability of maintaining a primary
    and backup DNS name (URL) for connecting to ONAP collectors, with the
    ability to switch between addresses based on conditions defined by policy
    such as time-outs, and buffering to store messages until they can be
    delivered. At its discretion, the service provider may choose to populate
    only one collector address for a VNF or PNF. In this case, the network will
    promptly resolve connectivity problems caused by a collector or network
    failure transparently to the VNF or PNF.
    

.. container:: note

    R-88482

    The VNF or PNF **SHOULD** use REST using HTTPS delivery of plain
    text JSON for moderate sized asynchronous data sets, and for high
    volume data sets when feasible.
    

Monitoring & Management > Monitoring & Management Requirements > Asynchronous and Synchronous Data Delivery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-11240

    The VNF or PNF **MUST** respond with content encoded in JSON, as
    described in the RESTCONF specification. This way the encoding of a
    synchronous communication will be consistent with Avro.
    

.. container:: note

    R-34660

    The VNF or PNF **MUST** use the RESTCONF/NETCONF framework used by
    the ONAP configuration subsystem for synchronous communication.
    

.. container:: note

    R-42140

    The VNF or PNF **MUST** respond to data requests from ONAP as soon
    as those requests are received, as a synchronous response.
    

.. container:: note

    R-43327

    The VNF or PNF **SHOULD** use `Modeling JSON text with YANG
    <https://tools.ietf.org/html/rfc7951>`_, If YANG models need to be
    translated to and from JSON{RFC7951]. YANG configuration and content can
    be represented via JSON, consistent with Avro, as described in "Encoding
    and Serialization" section.
    

.. container:: note

    R-46290

    The VNF or PNF **MUST** respond to an ONAP request to deliver granular
    data on device or subsystem status or performance, referencing the YANG
    configuration model for the VNF or PNF by returning the requested data elements.
    

.. container:: note

    R-70266

    The VNF or PNF **MUST** respond to an ONAP request to deliver the
    current data for any of the record types defined in
    `Event Records - Data Structure Description`_ by returning the requested
    record, populated with the current field values. (Currently the defined
    record types include fault fields, mobile flow fields, measurements for
    VNF or PNF scaling fields, and syslog fields. Other record types will be added
    in the future as they become standardized and are made available.)
    

.. container:: note

    R-73285

    The VNF or PNF **MUST** must encode, address and deliver the data
    as described in the previous paragraphs.
    

.. container:: note

    R-86586

    The VNF or PNF **MUST** use the YANG configuration models and RESTCONF
    [RFC8040] (https://tools.ietf.org/html/rfc8040).
    

Monitoring & Management > Monitoring & Management Requirements > Google Protocol Buffers (GPB)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-257367

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

    R-978752

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


Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-19624

    The VNF or PNF, when leveraging JSON for events, **MUST** encode and serialize
    content delivered to ONAP using JSON (RFC 7159) plain text format.
    High-volume data is to be encoded and serialized using
    `Avro <http://avro.apache.org/>`_, where the Avro data
    format are described using JSON.
    

Monitoring & Management > Monitoring & Management Requirements > Reporting Frequency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-146931

    The VNF or PNF **MUST** report exactly one Measurement event per period
    per source name.
    

.. container:: note

    R-98191

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
    

Monitoring & Management > Monitoring & Management Requirements > Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-01427

    If the VNF or PNF is using Basic Authentication, then the VNF or
    PNF **MUST** support the provisioning of security and authentication
    parameters (HTTP username and password) in order to be able to
    authenticate with DCAE VES Event Listener.

    Note: The configuration management and provisioning software
    are specific to a vendor architecture.
    

.. container:: note

    R-42366

    The VNF or PNF **MUST** support secure connections and transports such as
    Transport Layer Security (TLS) protocol
    [`RFC5246 <https://tools.ietf.org/html/rfc5246>`_] and should adhere to
    the best current practices outlined in
    `RFC7525 <https://tools.ietf.org/html/rfc7525>`_.
    

.. container:: note

    R-43387

    If the VNF or PNF is using Certificate Authentication, the
    VNF or PNF **MUST** support mutual TLS authentication and the Subject
    Name in the end-entity certificate MUST be used according to
    `RFC5280 <https://tools.ietf.org/html/rfc5280>`_.

    Note: In mutual TLS authentication, the client (VNF or PNF) must
    authenticate the server (DCAE) certificate and must provide its own
    X.509v3 end-entity certificate to the server for authentication.
    

.. container:: note

    R-44290

    The VNF or PNF **MUST** control access to ONAP and to VNFs or PNFs, and creation
    of connections, through secure credentials, log-on and exchange mechanisms.
    

.. container:: note

    R-47597

    The VNF or PNF **MUST** carry data in motion only over secure connections.
    

.. container:: note

    R-55634

    If VNF or PNF is using Basic Authentication, then the VNF or PNF
    **MUST** be in compliance with
    `RFC7617 <https://tools.ietf.org/html/rfc7617>`_ for authenticating HTTPS
    connections to the DCAE VES Event Listener.
    

.. container:: note

    R-894004

    If the VNF or PNF is using Basic Authentication, then when the VNF
    or PNF sets up a HTTPS connection to the DCAE VES Event Listener,
    the VNF or PNF **MUST** provide a username and password to the
    DCAE VES Event Listener in the Authorization header and the VNF
    or PNF MUST support one-way TLS authentication.

    Note: In one-way TLS authentication, the client (VNF or PNF)
    must authentication the server (DCAE) certificate.
    

Monitoring & Management > Monitoring & Management Requirements > VNF telemetry via standardized interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-821473

    The VNF or PNF MUST produce heartbeat indicators consisting of events containing
    the common event header only per the VES Listener Specification.
    

Monitoring & Management > Monitoring and Fault Protocol Selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-209104`

    The VNF or PNF producing VES syslog events **SHOULD** restrict these
    events to those that convey significant errors or warnings needed to support
    the operation or troubleshooting of the VNF or PNF. It is expected the
    volume of such events would be lower (e.g. less than 2000 per day) than
    more detailed events produced in the course of normal operations.
    

.. container:: note

    :need:`R-554966`

    The VNF or PNF **MUST** report performance metrics using
    :ref:`Virtual Function Event Streaming (VES) <ves_monitoring_requirements>`
    or :ref:`bulk_performance_measurement`.
    

.. container:: note

    :need:`R-63105`

    The VNF or PNF **MAY** produce telemetry data using the
    :doc:`RESTConf Collector <dcae:sections/services/restconf/index>`, but this
    requires additional coordination with the operator to appropriately
    map the data internally to a VES-like structure used within ONAP. If this
    option is needed, then the VNF or PNF Provider must coordinate with with the
    Operator for the data to be successfully collected and processed by DCAE.
    

.. container:: note

    :need:`R-69111`

    The VNF or PNF **MUST** report application logs using either
    :ref:`Virtual Function Event Streaming (VES) <ves_monitoring_requirements>`
    or Syslog in compliance with
    `RFC 5424 <https://tools.ietf.org/html/rfc5424>`__ .
    

.. container:: note

    :need:`R-82909`

    The VNF or PNF **MUST** report faults and alarms using either
    :ref:`Virtual Function Event Streaming (VES) <ves_monitoring_requirements>`
    or :ref:`SNMP <snmp_monitoring_requirements>`. (NOTE: See relevant sections
    for more detailed requirements)
    

.. container:: note

    :need:`R-857511`

    VNF or PNF Provider **MUST** have agreement with the Service Provider before
    utilizing the :doc:`HV-VES option <dcae:sections/services/ves-hv/index>`
    for monitoring as this option does not fully integrate with the ONAP's DCAE
    event processing capabilities.
    

.. container:: note

    :need:`R-935717`

    The VNF or PNF **MUST** report heartbeats using
    :ref:`Virtual Function Event Streaming (VES) <ves_monitoring_requirements>`.
    

Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-697654`

    The VNF or PNF **MAY** leverage ONAP's High Volume VNF Event Streaming
    (HV-VES) when there is a need to deliver large volumes of real-time
    performance management metrics. See
    :doc:`HV-VES collector <dcae:sections/services/ves-hv/index>`
    service details for more information.
    

.. container:: note

    :need:`R-332680`

    The VNF or PNF producing VES events **SHOULD** deliver syslog messages
    that meet the criteria in R-209104 to the VES Event Listener using the
    ``syslog`` VES domain.
    

.. container:: note

    :need:`R-908291`

    The VNF or PNF **MAY** leverage a bulk VNF or PNF telemetry transmission
    mechanism in instances where other transmission
    methods are not practical or advisable.

    NOTE: For additional information and use cases for the Bulk Telemetry
    Transmission Mechanism, please refer to
    the :ref:`bulk_performance_measurement` requirements and the
    `5G - Bulk PM ONAP Development <https://wiki.onap.org/display/DW/5G+-+Bulk+PM>`__
    Wiki page.
    

Monitoring & Management > SNMP Monitoring Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-233922`

    If the VNF or PNF is using SNMP, then the VNF or PNF Provider **SHOULD**
    provide examples of all SNMP alarms.
    

.. container:: note

    :need:`R-261501`

    If the VNF or PNF is using SNMP, then the VNF or PNF Provider **MUST**
    provide a Management Information Base (MIB) file that uniquely identifies
    and describes all SNMP events exposed by the network function.
    

Monitoring & Management > Transports and Protocols Supporting Resource Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-798933

    The VNF or PNF **SHOULD** deliver event records that fall into the event domains
    supported by VES.
    

.. container:: note

    R-821839

    The VNF or PNF **MUST** deliver event records to ONAP using the common
    transport mechanisms and protocols defined in this specification.
    

.. container:: note

    R-932071

    The VNF or PNF provider **MUST** reach agreement with the Service Provider on
    the selected methods for encoding, serialization and data delivery
    prior to the on-boarding of the VNF or PNF into ONAP SDC Design Studio.
    

Monitoring & Management > Transports and Protocols Supporting Resource Interfaces > VNF or PNF Telemetry using VES/JSON Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-659655

    The VNF or PNF **SHOULD** leverage the JSON-driven model, as depicted in Figure 2,
    for data delivery unless there are specific performance or operational
    concerns agreed upon by the Service Provider that would warrant using an
    alternate model.
    

Monitoring & Management > Virtual Function Event Streaming (VES) Client Requirements > Buffering and Redelivery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-103464`

    A VNF or PNF producing VES events that is buffering events due to an
    unavailable VES Event Listener **MAY** leverage to ``publishEventBatch``
    operation to redeliver buffered events. Please note this can only be
    used when all buffered events belong to the same domain due to the
    restrictions in place for the operation.
    

.. container:: note

    :need:`R-346137`

    A VNF or PNF producing VES events that is buffering events per R-658596
    **MUST** store in-scope events even when the maximum capacity of the
    buffer (defined in R-636251) has been reached. To make room for new events
    in this situation, hte oldest event in the buffer shall be removed
    as necessary. (i.e. First In First Out)
    

.. container:: note

    :need:`R-379523`

    A VNF or PNF producing VES events that is buffering events due to an
    unavailable VES Event Listener **MUST** redeliver all buffered events
    according to the following rules when the VNF or PNF detects the VES Event
    Listener has become available:

    * Deliver all previously buffered events before sending new events
    * Deliver buffered events in the order they were received
    

.. container:: note

    :need:`R-498679`

    A VNF or PNF producing VES events **MAY** discard buffered events older
    than a maximum retention period, not less than 1 hour, even if the event
    was never successfully delivered to the event listener. While discarding
    based on this retention period is supported for backwards compatibility, it
    is recommended to retain events until the maximum buffer size is reached per
    R-346137 as that will maximize the number of events delivered.
    

.. container:: note

    :need:`R-636251`

    A VNF or PNF producing VES events **MUST** size the event buffer
    referenced in R-658596 such that it can buffer a minimum of 1 hours of
    events under nominal load.
    

.. container:: note

    :need:`R-658596`

    A VNF or PNF producing VES events **MUST** buffer events that meet the
    following criteria if the VES Event Listener is unreachable or the request
    encounters a timeout.

    * Faults with eventSeverity of ``MINOR``, ``MAJOR``, ``NORMAL``, or
      ``CRITICAL``
    * Syslog with syslogSev of ``Emergency``, ``Alert``, ``Critical``,
      ``Error``, or ``Warning``
    * All measurement events
    

.. container:: note

    :need:`R-818859`

    The VNF or PNF producing VES events **MUST** not allow an unavailable or
    timing out VES Event Listener to impact the performance, stability, or
    correct execution of network function.
    

Monitoring & Management > Virtual Function Event Streaming (VES) Client Requirements > Configuration Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-460012`

    The VNF or PNF producing VES events **MUST** allow the configuration of
    the attributes defined in Table 1 and utilize the provided default value
    (where applicable) when the configuration value is not provided by the
    Service Provider.
    

.. container:: note

    :need:`R-940591`

    A VNF or PNF producing VES events **SHOULD** use the recommended parameter
    name for the configurable value from Table 1.
    

Monitoring & Management > Virtual Function Event Streaming (VES) Client Requirements > Configuration Requirements > VES Listener Endpoint and DNS Resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-130645`

    The VNF or PNF **MUST** respect the Time To Live provided by the DNS for
    the VES Event Listener FQDN.
    

.. container:: note

    :need:`R-70492`

    The VNF or PNF **MUST** support DNS resolution of the VES Listener Endpoint
    if a Fully Qualified Domain Name (FQDN) is provided.
    

Monitoring & Management > Virtual Function Event Streaming (VES) Client Requirements > Event Definition and Registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-120182`

    A VNF or PNF Provider utilizing VES **MUST** indicate specific conditions
    that may arise, and recommend actions that may be taken at specific
    thresholds, or if specific conditions repeat within a specified time
    interval, using the semantics and syntax described by the
    :ref:`VES Event Registration specification <ves_event_registration_3_2>`.

    **NOTE:** The Service Provider may override VNF or PNF provider Event
    Registrations using the ONAP SDC Design Studio to finalizes Service
    Provider engineering rules for the processing of the VNF or PNF events.
    These changes may modify any of the following:

    * Threshold levels
    * Specified actions related to conditions
    

.. container:: note

    :need:`R-520802`

    If the VNF or PNF is using VES, then the VNF or PNF Provider **MUST** provide
    a YAML file formatted in adherence with the
    :ref:`VES Event Registration specification <ves_event_registration_3_2>`
    that defines the following information for each event produced by the VNF:

    * ``eventName``
    * Required fields
    * Optional fields
    * Any special handling to be performed for that event
    

Monitoring & Management > Virtual Function Event Streaming (VES) Client Requirements > Event Delivery Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-176945`

    The VNF or PNF producing VES events **SHOULD NOT** send syslog events to the
    VES Event Listener during debug mode, but rather store syslog events locally
    for access or possible file transfer.
    

.. container:: note

    :need:`R-655209`

    The VNF or PNF producing VES events **MUST** respect the configured
    VES Timeout Value when delivering VES events, and abort any call where
    the VES Event Listener does not successfully acknowledge the delivery of
    event(s) within the Timeout Value. These failed transactions should be
    buffered and retried in accordance with the
    :ref:`ves_buffering_requirements` Requirements.
    

Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-06924`

    The VNF or PNF producing VES events **MUST** deliver VES events as it
    becomes available or according to the configured measurement interval.
    

Monitoring & Management > Virtual Function Event Streaming (VES) Client Requirements > Event Formatting and Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-408814`

    The VNF or a PNF producing VES stndDefined domain events to report
    standards-organization defined events to ONAP, **MUST** set the
    event.stndDefinedNamespace property. By default, ONAP ships with support
    for the following:

    * 3GPP-Provisioning
    * 3GPP-Heartbeat
    * 3GPP-FaultSupervision
    * 3GPP-PerformanceAssurance

    Another namespace, outside of the list provided, needs to registered in ONAP in coordination
    with the operator before it can be used.
    

.. container:: note

    :need:`R-408815`

    If the VNF or PNF producing VES stndDefined domain events provides
    the event.stndDefinedFields.schemaReference then it **MUST** set its value
    to the publicUrl value in DCAE's VES Collector `etc/externalRepo/schema-map.json <https://github.com/onap/dcaegen2-collectors-ves/blob/guilin/etc/externalRepo/schema-map.json/>`_
    that describes the data being sent in event.stndDefinedFields.data.
    

.. container:: note

    :need:`R-408816`

    If the VNF or PNF producing VES stndDefined domain events provides
    the event.stndDefinedFields.schemaReference then it **MUST** only pass events
    that conform to schema references previously registered with DCAE otherwise
    the event will be rejected. By default, ONAP ships with support for schemas
    found in DCAE's VES Collector `etc/externalRepo/schema-map.json <https://github.com/onap/dcaegen2-collectors-ves/blob/guilin/etc/externalRepo/schema-map.json/>`_.
    

.. container:: note

    :need:`R-408817`

    The VNF or PNF Provider producing stndDefined events **MUST** coordinate with
    the operator, willing to validate stndDefined events, to configure DCAE to
    accept any new event schema prior to sending those events or the events
    will be rejected.
    

.. container:: note

    :need:`R-408818`

    If the VNF or PNF producing VES stndDefined domain events provides
    the event.stndDefinedFields.schemaReference then it **MUST** set the
    event.stndDefined.schemaReference property to an exact structure,
    from supported schemaReference, describing the notification within
    an openAPI specification, using JSON Pointer as URI fragment  e.g.
    “https://forge.3gpp.org/.../faultMnS.yaml#/components/schemas/notifyNewAlarm"
    

Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-408813`

    A VNF or PNF producing VES events **MUST** pass all information it is
    able to collect even if the information field is identified as optional.
    However, if the data cannot be collected, then optional fields can be
    omitted.
    

.. container:: note

    :need:`R-570134`

    The VES events produced by the VNF or PNF **MUST** be compliant with the
    common event formats defined in one of the following specifications:

    * :ref:`VES Event Listener 5.4.1<ves_event_listener_5_4_1>`
    * :ref:`VES Event Listener 7.1.1<ves_event_listener_7_1>`
    * :ref:`VES Event Listener 7.2<ves_event_listener_7_2>`

    The latest version (7.2) should be preferred. Earlier versions are
    provided for backwards compatibility.
    

.. container:: note

    :need:`R-283988`

    A VNF or PNF producing VES events **MUST NOT** send information through
    extensible structures if the event specification has explicitly defined
    fields for that information.
    

.. container:: note

    :need:`R-528866`

    The VES events produced by the VNF or PNF **MUST** conform to the schema and
    other formatting requirements specified in the relevant VES Event Listener
    specification.
    

.. container:: note

    :need:`R-470963`

    A VNF or PNF producing VES events **SHOULD** leverage camel case to
    separate words and acronyms used as keys that will be sent through extensible
    fields. When an acronym is used as the key, then only the first letter shall
    be capitalized.
    

Monitoring & Management > Virtual Function Event Streaming (VES) Client Requirements > Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-33878`

    The VNF or PNF **MUST** utilize one of the authentication methods
    prescribed by the relevant VES Event Listener specification.
    

ONAP Heat VNF Modularity
^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-610030`

    A VNF's Heat Orchestration Template's Incremental Module **MUST**
    declare

    - one or more ``OS::Nova::Server`` resources OR
    - one or more ``OS::Cinder::Volume`` resources.

    An ``OS::Nova::Server``
    **MAY** be created in the incremental module or a nested yaml file invoked
    by the incremental module.

    An ``OS::Cinder::Volume``
    **MAY** be created in the incremental module or a nested yaml file invoked
    by the incremental module.
    

PNF Plug and Play > PNF Plug and Play
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-106240`

    A PNF MUST support the pnfRegistration VES event which is required to integrate with ONAP’s PNF Plug and Play capabilities.
    

TOSCA PNF Descriptor > Capability Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-177937`

    The PNFD provided by a PNF vendor **MUST** comply with the following
    Capabilities Types as specified in ETSI NFV-SOL001 standard:

      - tosca.capabilities.nfv.VirtualLinkable
    

TOSCA PNF Descriptor > Policy Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-596064`

    The PNFD provided by a PNF vendor **MUST** comply with the following Policy
    Types as specified in ETSI NFV-SOL001 standard:

      - tosca.policies.nfv.SecurityGroupRule
    

TOSCA PNF Descriptor > Relationship Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-64064`

    The PNFD provided by a PNF vendor **MUST** comply with the following
    Relationship Types as specified in ETSI NFV-SOL001 standard:

      - tosca.relations.nfv.VirtualLinksTo
    

VNF and PNF On-boarding and package management > Licensing Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-85991`

    If the VNF or PNF requires a license then the VNF or PNF provider **MUST** provide a universal license key
    per VNF or PNF to be used as needed by services (i.e., not tied to a VM
    instance) as the recommended solution. The VNF or PNF provider may provide
    pools of Unique VNF or PNF License Keys, where there is a unique key for
    each VNF or PNF instance as an alternate solution. In all cases, licensing issues should
    be resolved without interrupting in-service VNFs or PNFs.
    

.. container:: note

    :need:`R-44569`

    If ONAP licensing management solution is used, then the VNF or PNF provider **MUST NOT** require additional
    infrastructure such as a VNF or PNF provider license server for VNF or PNF provider
    functions and metrics.
    

.. container:: note

    :need:`R-13613`

    The VNF **MUST** provide clear measurements for licensing
    purposes if needed to allow automated scale up/down by the management system.
    

.. container:: note

    :need:`R-47849`

    If ONAP licensing management solution is used, then the VNF or PNF provider
    **MUST** support the metadata about licenses (and their applicable
    entitlements) as defined in the
    `ONAP License Management Information Model <https://docs.onap.org/projects/onap-modeling-modelspec/en/latest/ONAP%20Model%20Spec/im/License/LicenseModel.html>`__,
    and any license keys required to authorize use of the VNF or PNF software.
    This metadata will be used to facilitate onboarding the VNF or PNF into the
    ONAP environment and automating processes for putting the licenses into use
    and managing the full lifecycle of the licenses.
    

.. container:: note

    :need:`R-85653`

    If ONAP licensing management solution is used, then the VNF or PNF **MUST** provide metrics (e.g., number of sessions,
    number of subscribers, number of seats, etc.) to ONAP for tracking
    every license.
    

Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-44125

    The VNF or PNF provider **MUST** agree to the process that can
    be met by Service Provider reporting infrastructure. The Contract
    shall define the reporting process and the available reporting tools.
    

.. container:: note

    R-97293

    The VNF or PNF provider **MUST NOT** require audits
    of Service Provider's business.
    

VNF and PNF On-boarding and package management > Resource Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-22346`

    The VNF or PNF Provider **MUST** provide :ref:`VES Event Registration <ves_event_registration_3_2>`
    for all VES events provided by that VNF or PNF.
    

VNF or PNF CSAR Package > VNF or PNF Package Contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-40820`

    The VNF CSAR PACKAGE **MUST** enumerate all of the open source
    licenses their VNF(s) incorporate. CSAR License directory as per ETSI
    SOL004.

    for example ROOT\\Licenses\\ **License_term.txt**
    
