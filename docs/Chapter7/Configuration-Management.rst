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

.. _vnf_configuration_management:

Configuration Management
------------------------
The protocol used to communicate with VNF or PNF for life cycle management (LCM) operations is NETCONF, Ansible or Chef.
A VNF or PNF shall support at least one of communication protocols as specified in the requirement R-305645.

.. req::
    :id: R-305645
    :target: VNF or PNF
    :keyword: MUST
    :introduced: Frankfurt

    The VNF or PNF MUST supports configuration management including
    life cycle management (LCM) using at least one of the following
    protocols a)NETCONF/YANG, b)Ansible and c)Chef.

Since Frankfurt release, SO building blocks can use either APPC or CDS API path
for life cycle management (LCM) operations. The associated API is either APPC/SDN-C LCM API or CDS self-service API.
A VNF or PNF must supports LCM operations that using either of two APIs.
The selection of which API to use for LCM operations for a given PNF/VNF type is defined in design time by the service designer.

The requirements for supporting of SDN-C/APPC LCM API for LCM operations are documented in section 7.3.1.

Controller Interactions With VNF or PNF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This section is not applicable to LCM operations using CDS self-service API.

APPC/SDN-C expose a northbound API to clients (such as SO) in order for
the clients to initiate an activity (aka command) on a VNF or PNF. APPC/SDN-C
interact with VNFs or PNFs through Network and Application Adapters to perform
configuration and other lifecycle management activities within NFV environment.
The standardized models, protocols and mechanisms by which network functions
are configured are equally applicable to VNFs and PNFs.

This section describes the list of commands that should be supported
by the VNF or PNF. The following sections describe the standard protocols
that are supported (NETCONF, Chef, Ansible, and REST).

The commands below are expected to be supported on all VNF or PNF's, unless
The commands below are expected to be supported on all VNF or PNF's, unless
noted otherwise, either directly (via the NETCONF or REST interface)
or indirectly (via a Chef Cookbook or Ansible server).

**Note that there are additional commands offered to northbound clients that
are not shown below, as these commands either act internally on APPC/SDN-C
itself or depend upon network cloud components for implementation (thus, these
actions do not put any special requirement on the VNF or PNF provider).**

The commands allow for parametric data to be passed from APPC/SDN-C
to the VNF or PNF or Ansible/Chef server in the request. The format of the
parameter data can be either xml (for NETCONF) or JSON (for Ansible,
Chef, or REST).

Configuration Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Configure``: The APPC/SDN-C client is requesting that a post-instantiation
configuration be applied to the target VNF or PNF. After the Configure
action is completed, the VNF or PNF instance should be ready for service.
Note that customer specific configurations may need to be applied using
the ConfigModify action. This command requires exclusive access rights of
the VNF or PNF.

``ConfigModify``: The APPC client is requesting a configuration
update to a subset of the total configuration parameters of an VNF or PNF or to
apply customer specific configurations. The configuration update is
typically done while the VNF or PNF is in service and should not disrupt
traffic. This command requires exclusive access rights of the VNF or PNF.

``ConfigBackup``: The APPC client is requesting a backup of the
configuration parameters where the parameters are stored on the VNF or PNF.
This command is typically requested as part of an orchestration flow
for scenarios such as a software upgrade. The ConfigBackup is typically
done while the VNF or PNF is not in service (i.e., in a maintenance state).
When the ConfigBackup command is executed, the current VNF or PNF configuration
parameters are saved in storage that is preserved (if there is an existing
set of backed up parameters, they are overwritten). This command requires
exclusive access rights of the VNF or PNF.

``ConfigRestore``: The APPC client is requesting a restore action of
the configuration parameters to the VNF or PNF that were saved by ConfigBackup
command. This command is typically requested as part of an orchestration
flow for scenarios such as a software upgrade where the software upgrade
may have failed and the VNF or PNF needs to be rolled back to the prior
configuration.
When the ConfigRestore command is executed, the VNF or PNF configuration
parameters which were backed to persistent preserved storage are applied to the
VNF or PNF (replacing existing parameters). The ConfigRestore is typically done
while the VNF or PNF is not in service (i.e., in a maintenance state). This
command requires exclusive access rights of the VNF or PNF.

``ConfigScaleOut``: The APPC/SDN-C client is requesting that a configuration
be applied after the VNF instance has been scaled out (i.e., one or more
additional VM's instantiated to increase capacity). For some VNF's,
ConfigScaleOut is not needed because the VNF is auto-configured after
scale-out. This command is being introduced in the Beijing release to support
manual Scale Out and will be extended to support Auto ScaleOut in Casablanca
release. This command requires exclusive access rights of the VNF.

``Audit``: The APPC client is requesting that the current (last known
configuration update) is audited against the running configuration on the VNF
(Openstack).

.. req::
    :id: R-20741
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC/SDN-C ``Configure`` command.

.. req::
    :id: R-19366
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC ``ConfigModify`` command.

.. req::
    :id: R-32981
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC ``ConfigBackup`` command.

.. req::
    :id: R-48247
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC ``ConfigRestore`` command.

.. req::
    :id: R-94084
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC/SDN-C ``ConfigScaleOut`` command.

.. req::
    :id: R-56385
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC ``Audit`` command.

Lifecycle Management Related Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**The following commands are needed to support various lifecycle management
flows where the VNF may need to be removed for service.**

Full details on the APIs can be found in the
:doc:`APPC LCM API Guide <../../../../appc.git/docs/APPC LCM API Guide/APPC LCM API Guide>`

``DistributeTraffic`` The APPC/SDN-C client is requesting a change to
traffic distribution (redistribution) done by a traffic balancing/distribution
entity (aka anchor point) or mechanism. This action targets the traffic
balancing/distribution entity, in some cases DNS, other cases a load balancer
external to the VNF instance, as examples. Traffic distribution (weight)
changes intended to take a VNF instance out of service are completed only
when all in-flight traffic/transactions have been completed. To complete
the traffic redistribution process, gracefully taking a VNF instance
out-of-service, without dropping in-flight calls or sessions, QuiesceTraffic
command may need to follow traffic distribution changes (assigning weight 0
or very low weight to VNF instance). The VNF application remains in an active
state.

``QuiesceTraffic`` The APPC/SDN-C client is requesting the VNF or PNF
gracefully stop traffic (aka block and drain traffic). The method for quiescing
traffic is specific to the VNF or PNF architecture. The action is completed
when all (in-flight transactions) traffic has stopped. The VNF or PNF remains
in an active state where the VNF or PNF is able to process traffic (initiated
using the ResumeTraffic action).

``ResumeTraffic``: The APPC/SDN-C client is requesting the VNF or PNF resume
processing traffic. The method to resume traffic is specific to the VNF or PNF
architecture.

``StopApplication``: The APPC client is requesting that the application
running on the VNF or PNF is stopped gracefully (i.e., without traffic loss).
This is equivalent to quiescing the traffic and then stopping the application
processes. The processes can be restarted using the StartApplication command.

``StartApplication``: The APPC client is requesting that the application
running on the VNF or PNF is started. Get ready to process traffic.
Traffic processing can be resumed using the ResumeTraffic command.

**The following commands are needed to support software upgrades, in-place or
other type of software upgrade. The VNF or PNF instance may be removed from
service for the upgrade.**

``UpgradePrecheck``: The APPC/SDN-C client is requesting a confirmation that
the VNF or PNF can (and needs to) be upgraded to a specific software version
(specified in the request). Checking software installed and running on
the VNF or PNF matches software version, intended to be upgraded, is one of the
recommended checks.

``UpgradeSoftware``: The APPC/SDN-C client is requesting that a (in-place)
software upgrade be performed on the VNF or PNF.  The software to be applied is
pre-loaded to a specified location.

``UpgradePostCheck``: The APPC/SDN-C client is requesting a confirmation that
the VNF or PNF software upgrade has been completed successfully (VNF or PNF
upgraded to the new software version). Checking software installed and running
on the VNF or PNF matches software version, of the newly upgraded software, is
one of the recommended checks.

``UpgradeBackup``: The APPC/SDN-C client is requesting that the VNF or PNF is
backed up prior to the UpgradeSoftware.

``UpgradeBackOut``: The APPC/SDN-C client is requesting that the VNF or PNF
upgrade is backed out (in the event that the SoftwareUpgrade or
UpgradePostCheck failed).

.. req::
    :id: R-328086
    :target: VNF or PNF
    :keyword: MUST
    :introduced: casablanca
    :updated: dublin

    The VNF or PNF **MUST**, if serving as a distribution point or anchor point for
    steering point from source to destination, support the ONAP Controller's
    ``DistributeTraffic`` command.

.. req::
    :id: R-12706
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC/SDN-C ``QuiesceTraffic`` command.

.. req::
    :id: R-07251
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC/SDN-C ``ResumeTraffic`` command.

.. req::
    :id: R-83146
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC ``StopApplication`` command.

.. req::
    :id: R-82811
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC ``StartApplication`` command.

.. req::
    :id: R-19922
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC/SDN-C ``UpgradePrecheck`` command.

.. req::
    :id: R-49466
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC/SDN-C ``UpgradeSoftware`` command.

.. req::
    :id: R-45856
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC/SDN-C ``UpgradePostCheck`` command.

.. req::
    :id: R-97343
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC/SDN-C ``UpgradeBackup`` command.

.. req::
    :id: R-65641
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC/SDN-C ``UpgradeBackOut`` command.


HealthCheck and Failure Related Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``HealthCheck`` The APPC/SDN-C client is requesting a health check over the
entire scope of the VNF or PNF. The VNF or PNF must be 100% healthy, ready to
take requests and provide services, with all VNF or PNF required capabilities
ready to provide services and with all active and standby resources fully ready
with no open MINOR, MAJOR or CRITICAL alarms. This is expected to be the
default in the event that no parameter is passed to the Healthcheck playbook,
cookbook, etc.

Some VNFs or PNFs may support and desire to run partial healthchecks and
receive a successful response when partial health check completes without
errors. The parameter name used by HealthCheck playbook to request non-default
partial health check is healthcheck_type. Example of health check types
could be healthcheck_type=GuestOS, healthcheck_type=noDB,
healthcheck_type=noConnections, healthcheck_type=IgnoreAlarms, etc..
This attribute-value pair may be passed by the Orchestrator or Workflow
or other (northbound) APPC/SDN-C clients to the APPC/SDN-C as part of the
request.

**Note**: In addition to the commands above, the APPC/SDN-C supports a set of
Openstack failure recovery related commands that are executed on-demand or via
Control Loop at the VM level. The VNF must support these commands in a fully
automated fashion.

.. req::
    :id: R-41430
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support APPC/SDN-C ``HealthCheck`` command.

Notes On Command Support Using APPC/SDN-C Southbound Protocols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

APPC/SDN-C are designed to support a standard set of protocols in
order to communicate with the VNF or PNF instance. The supported protocols are
NETCONF, Ansible, Chef, and REST.

NETCONF and REST require the VNF or PNF to implement a server which supports
the RPC or REST calls.

Ansible and Chef require the use of a Ansible or Chef server which communicates
with the APPC/SDN-C (northbound) and the VNF or PNF VM's (southbound).

The vendor must select which protocol to support for the commands listed above.
Notes:

* NETCONF is most suitable for configuration related commands.

* Ansible and Chef are suitable for any command.
  Ansible has the advantage that it is agentless.

* REST is specified as an option only for the HealthCheck.


Additional details can be found in the
`ONAP Application Controller (APPC) API Guide <https://onap.readthedocs.io/en/latest/submodules/appc.git/docs/index.html>`_,
`ONAP VF-C project <https://onap.readthedocs.io/en/latest/submodules/vfc/nfvo/lcm.git/docs/index.html>`_ and
the `ONAP SDNC project <https://onap.readthedocs.io/en/latest/submodules/sdnc/oam.git/docs/index.html>`_.

NETCONF Standards and Capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

APPC/SDN-C and their Adapters utilize device YANG model and
NETCONF APIs to make the required changes in the VNF or PNF state and
configuration. The VNF or PNF providers must provide the Device YANG model and
NETCONF server supporting NETCONF APIs to comply with target ONAP and
industry standards.

VNF or PNF Configuration via NETCONF Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration Management
+++++++++++++++++++++++++++


.. req::
    :id: R-88026
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** include a NETCONF server enabling
    runtime configuration and lifecycle management capabilities.

.. req::
    :id: R-95950
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** provide a NETCONF interface fully defined
    by supplied YANG models for the embedded NETCONF server.

NETCONF Server Requirements
++++++++++++++++++++++++++++++


.. req::
    :id: R-73468
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** allow the NETCONF server connection
    parameters to be configurable during virtual machine instantiation
    through Heat templates where SSH keys, usernames, passwords, SSH
    service and SSH port numbers are Heat template parameters.

.. req::
    :id: R-90007
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement the protocol operation:
    ``close-session()`` - Gracefully close the current session.

.. req::
    :id: R-70496
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement the protocol operation:
    ``commit(confirmed, confirm-timeout)`` - Commit candidate
    configuration data store to the running configuration.

.. req::
    :id: R-18733
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement the protocol operation:
    ``discard-changes()`` - Revert the candidate configuration
    data store to the running configuration.

.. req::
    :id: R-44281
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement the protocol operation:
    ``edit-config(target, default-operation, test-option, error-option,
    config)`` - Edit the target configuration data store by merging,
    replacing, creating, or deleting new config elements.

.. req::
    :id: R-60106
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement the protocol operation:
    ``get(filter)`` - Retrieve (a filtered subset of) the running
    configuration and device state information. This should include
    the list of VNF or PNF supported schemas.

.. req::
    :id: R-29488
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement the protocol operation:
    ``get-config(source, filter`` - Retrieve a (filtered subset of
    a) configuration from the configuration data store source.

.. req::
    :id: R-11235
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement the protocol operation:
    ``kill-session(session``- Force the termination of **session**.

.. req::
    :id: R-02597
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement the protocol operation:
    ``lock(target)`` - Lock the configuration data store target.

.. req::
    :id: R-96554
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement the protocol operation:
    ``unlock(target)`` - Unlock the configuration data store target.

.. req::
    :id: R-29324
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** implement the protocol operation:
    ``copy-config(target, source)`` - Copy the content of the
    configuration data store source to the configuration data store target.

.. req::
    :id: R-88031
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** implement the protocol operation:
    ``delete-config(target)`` - Delete the named configuration
    data store target.

.. req::
    :id: R-97529
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** implement the protocol operation:
    ``get-schema(identifier, version, format)`` - Retrieve the YANG schema.

.. req::
    :id: R-62468
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** allow all configuration data to be
    edited through a NETCONF <edit-config> operation. Proprietary
    NETCONF RPCs that make configuration changes are not sufficient.

.. req::
    :id: R-01382
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** allow the entire configuration of the VNF or PNF to be
    retrieved via NETCONF's <get-config> and <edit-config>, independently
    of whether it was configured via NETCONF or other mechanisms.

.. req::
    :id: R-28756
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support ``:partial-lock`` and
    ``:partial-unlock`` capabilities, defined in RFC 5717. This
    allows multiple independent clients to each write to a different
    part of the <running> configuration at the same time.

.. req::
    :id: R-83873
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support ``:rollback-on-error`` value for
    the <error-option> parameter to the <edit-config> operation. If any
    error occurs during the requested edit operation, then the target
    database (usually the running configuration) will be left unaffected.
    This provides an 'all-or-nothing' edit mode for a single <edit-config>
    request.

.. req::
    :id: R-68990
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support the ``:startup`` capability. It
    will allow the running configuration to be copied to this special
    database. It can also be locked and unlocked.

.. req::
    :id: R-68200
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support the ``:url`` value to specify
    protocol operation source and target parameters. The capability URI
    for this feature will indicate which schemes (e.g., file, https, sftp)
    that the server supports within a particular URL value. The 'file'
    scheme allows for editable local configuration databases. The other
    schemes allow for remote storage of configuration databases.

.. req::
    :id: R-20353
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement both ``:candidate`` and
    ``:writable-running`` capabilities. When both ``:candidate`` and
    ``:writable-running`` are provided then two locks should be supported.

.. req::
    :id: R-11499
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** fully support the XPath 1.0 specification
    for filtered retrieval of configuration and other database contents.
    The 'type' attribute within the <filter> parameter for <get> and
    <get-config> operations may be set to 'xpath'. The 'select' attribute
    (which contains the XPath expression) will also be supported by the
    server. A server may support partial XPath retrieval filtering, but
    it cannot advertise the ``:xpath`` capability unless the entire XPath
    1.0 specification is supported.

.. req::
    :id: R-83790
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement the ``:validate`` capability.

.. req::
    :id: R-49145
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement ``:confirmed-commit`` If
    ``:candidate`` is supported.

.. req::
    :id: R-58358
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement the ``:with-defaults`` capability
    [RFC6243].

.. req::
    :id: R-59610
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** implement the data model discovery and
    download as defined in [RFC6022].

.. req::
    :id: R-93443
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** define all data models in YANG 1.0 [RFC6020] or
    YANG 1.1 [RFC7950]. A combination of YANG 1.0 and YANG 1.1 modules is
    allowed subject to the rules in [RFC7950] section 12. The mapping to
    NETCONF shall follow the rules defined in this RFC.

.. req::
    :id: R-26115
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** follow the data model update rules defined in
    [RFC6020] section 10 for YANG 1.0 modules, and [RFC7950] section 11
    for YANG 1.1 modules. All deviations from the aforementioned update
    rules shall be handled by a built-in  automatic upgrade mechanism.

.. req::
    :id: R-10716
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support parallel and simultaneous
    configuration of separate objects within itself.

.. req::
    :id: R-29495
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support locking if a common object is
    being manipulated by two simultaneous NETCONF configuration operations
    on the same VNF or PNF within the context of the same writable running data
    store (e.g., if an interface parameter is being configured then it
    should be locked out for configuration by a simultaneous configuration
    operation on that same interface parameter).

.. req::
    :id: R-53015
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** apply locking based on the sequence of
    NETCONF operations, with the first configuration operation locking
    out all others until completed.

.. req::
    :id: R-02616
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** permit locking at the finest granularity
    if a VNF or PNF needs to lock an object for configuration to avoid blocking
    simultaneous configuration operations on unrelated objects (e.g., BGP
    configuration should not be locked out if an interface is being
    configured or entire Interface configuration should not be locked out
    if a non-overlapping parameter on the interface is being configured).

.. req::
    :id: R-41829
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** be able to specify the granularity of the
    lock via a restricted or full XPath expression.

.. req::
    :id: R-66793
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** guarantee the VNF or PNF configuration integrity
    for all simultaneous configuration operations (e.g., if a change is
    attempted to the BUM filter rate from multiple interfaces on the same
    EVC, then they need to be sequenced in the VNF or PNF without locking either
    configuration method out).

.. req::
    :id: R-54190
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** release locks to prevent permanent lock-outs
    when/if a session applying the lock is terminated (e.g., SSH session
    is terminated).

.. req::
    :id: R-03465
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** release locks to prevent permanent lock-outs
    when the corresponding <partial-unlock> operation succeeds.

.. req::
    :id: R-63935
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** release locks to prevent permanent lock-outs
    when a user configured timer has expired forcing the NETCONF SSH Session
    termination (i.e., product must expose a configuration knob for a user
    setting of a lock expiration timer).

.. req::
    :id: R-10173
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** allow another NETCONF session to be able to
    initiate the release of the lock by killing the session owning the lock,
    using the <kill-session> operation to guard against hung NETCONF sessions.

.. req::
    :id: R-88899
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support simultaneous <commit> operations
    within the context of this locking requirements framework.

.. req::
    :id: R-07545
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support all operations, administration and
    management (OAM) functions available from the supplier for VNFs or PNFs
    using the supplied YANG code and associated NETCONF servers.

.. req::
    :id: R-60656
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support sub tree filtering.

.. req::
    :id: R-80898
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    TThe VNF or PNF **MUST** support heartbeat via a <get> with null filter.

.. req::
    :id: R-25238
    :target: VNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF PACKAGE **MUST** validated YANG code using the open
    source pyang [#7.3.1]_ program using the following commands:

    .. code-block:: text

      $ pyang --verbose --strict <YANG-file-name(s)> $ echo $!

.. req::
    :id: R-63953
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** have the echo command return a zero value
    otherwise the validation has failed.

.. req::
    :id: R-26508
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support a NETCONF server that can be mounted on
    OpenDaylight (client) and perform the operations of: modify, update,
    change, rollback configurations using each configuration data element,
    query each state (non-configuration) data element, execute each YANG
    RPC, and receive data through each notification statement.

The following requirements provides the Yang models that suppliers must
conform, and those where applicable, that suppliers need to use.


.. req::
    :id: R-22700
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** conform its YANG model to RFC 6470,
    "NETCONF Base Notifications".

.. req::
    :id: R-10353
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** conform its YANG model to RFC 6244,
    "An Architecture for Network Management Using NETCONF and YANG".

.. req::
    :id: R-53317
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** conform its YANG model to RFC 6087,
    "Guidelines for Authors and Reviewers of YANG Data Model specification".

.. req::
    :id: R-33955
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** conform its YANG model to RFC 6991,
    "Common YANG Data Types".

.. req::
    :id: R-22946
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** conform its YANG model to RFC 6536,
    "NETCONF Access Control Model".

.. req::
    :id: R-10129
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** conform its YANG model to RFC 7223,
    "A YANG Data Model for Interface Management".

.. req::
    :id: R-12271
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** conform its YANG model to RFC 7223,
    "IANA Interface Type YANG Module".

.. req::
    :id: R-49036
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** conform its YANG model to RFC 7277,
    "A YANG Data Model for IP Management".

.. req::
    :id: R-87564
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** conform its YANG model to RFC 7317,
    "A YANG Data Model for System Management".

.. req::
    :id: R-24269
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** conform its YANG model to RFC 7407,
    "A YANG Data Model for SNMP Configuration", if Netconf used to
    configure SNMP engine.

The NETCONF server interface shall fully conform to the following
NETCONF RFCs.


.. req::
    :id: R-33946
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** conform to the NETCONF RFC 4741,
    "NETCONF Configuration Protocol".

.. req::
    :id: R-04158
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** conform to the NETCONF RFC 4742,
    "Using the NETCONF Configuration Protocol over Secure Shell (SSH)".

.. req::
    :id: R-13800
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** conform to the NETCONF RFC 5277,
    "NETCONF Event Notification".

.. req::
    :id: R-01334
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** conform to the NETCONF RFC 5717,
    "Partial Lock Remote Procedure Call".

.. req::
    :id: R-08134
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** conform to the NETCONF RFC 6241,
    "NETCONF Configuration Protocol".

.. req::
    :id: R-78282
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** conform to the NETCONF RFC 6242,
    "Using the Network Configuration Protocol over Secure Shell".

.. req::
    :id: R-997907
    :target: VNF or PNF
    :keyword: SHOULD
    :introduced: dublin

    The VNF or PNF **SHOULD** support TLS as secure transport for the NETCONF
    protocol according to [RFC7589].


.. _xnf_rest_apis:

VNF or PNF REST APIs
^^^^^^^^^^^^^^^^^^^^

HealthCheck is a command for which no NETCONF support exists.
Therefore, this must be supported using a RESTful interface
(defined in this section) or with a Chef cookbook/Ansible playbook
(defined in sections `Chef Standards and Capabilities`_ and
`Ansible Standards and Capabilities`_).

See section 7.3.1.4 for the definition of Full Healthcheck and Partial
Healthchecks.

The VNF or PNF must provide a REST formatted GET RPCs to support HealthCheck
queries via the GET method over HTTP(s).

The port number, url, and other authentication information is provided
by the VNF or PNF provider.

REST APIs
~~~~~~~~~

.. req::
    :id: R-31809
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support the HealthCheck RPC. The HealthCheck
    RPC executes a VNF or PNF Provider-defined VNF or PNF HealthCheck over the
    scope of the entire VNF or PNF (e.g., if there are multiple VNFCs, then
    run a health check, as appropriate, for all VNFCs). It returns a 200 OK if
    the test completes. A JSON object is returned indicating state (healthy,
    unhealthy), scope identifier, time-stamp and one or more blocks containing
    info and fault information. If the VNF or PNF is unable to run the
    HealthCheck, return a standard http error code and message.

Examples of responses when HealthCheck runs and is able to provide a healthy
or unhealthy response:

.. code-block:: java

  {
    "identifier":"VNF",
    "state":"healthy",
    "time":"2018-11-28 22:39:00.809466"
  },

  {
    "identifier":"VNF",
    "state":"unhealthy",
    "info":"There are stopped processes or VNF is not ready, may be quiesced or frozen.",
    "fault":"VNF mtn23comx8000v not ready for service.",
    "time":"2018-11-30 05:47:48.655959"
  }


Chef Standards and Capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: note

    **ATTENTION**: Chef is supported by ONAP, but it is not currently used by
    any of the official ONAP use cases and is not part of standard release
    testing like REST, Ansible, and Netconf.  For this reason, the other
    options are generally favored over Chef at this time.


ONAP will support configuration of VNFs or PNFs via Chef subject to the
requirements and guidelines defined in this section.

The Chef configuration management mechanism follows a client-server
model. It requires the presence of a Chef-Client on the VNF or PNF that will be
directly managed by a Chef Server. The Chef-client will register with
the appropriate Chef Server and are managed via 'cookbooks' and
configuration attributes loaded on the Chef Server which contain all
necessary information to execute the appropriate actions on the VNF or PNF via
the Chef-client.

ONAP will utilize the open source Chef Server, invoke the documented
Chef REST APIs to manage the VNF or PNF and requires the use of open source
Chef-Client and Push Jobs Client on the VNF or PNF
(https://downloads.chef.io/).

VNF or PNF Configuration via Chef Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chef Client Requirements
+++++++++++++++++++++++++


.. req::
    :id: R-79224
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** have the chef-client be preloaded with
    validator keys and configuration to register with the designated
    Chef Server as part of the installation process.

.. req::
    :id: R-72184
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** have routable FQDNs for all the endpoints
    (VMs) of a VNF or PNF that contain chef-clients which are used to register
    with the Chef Server.  As part of invoking VNF or PNF actions, ONAP will
    trigger push jobs against FQDNs of endpoints for a VNF or PNF, if required.

.. req::
    :id: R-47068
    :target: VNF or PNF
    :keyword: MAY
    :updated: dublin

    The VNF or PNF **MAY** expose a single endpoint that is
    responsible for all functionality.

.. req::
    :id: R-67114
    :target: VNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** be installed with Chef-Client >= 12.0 and Chef
    push jobs client >= 2.0.

Chef Roles/Requirements
++++++++++++++++++++++++++

.. req::
    :id: R-27310
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF Package **MUST** include all relevant Chef artifacts
    (roles/cookbooks/recipes) required to execute VNF or PNF actions requested
    by ONAP for loading on appropriate Chef Server.

.. req::
    :id: R-26567
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF Package **MUST** include a run list of
    roles/cookbooks/recipes, for each supported VNF or PNF action, that will
    perform the desired VNF or PNF action in its entirety as specified by ONAP
    (see Section 7.c, APPC/SDN-C APIs and Behavior, for list of VNF or PNF
    actions and requirements), when triggered by a chef-client run list
    in JSON file.

.. req::
    :id: R-98911
    :target: VNF or PNF
    :keyword: MUST NOT
    :updated: dublin

    The VNF or PNF **MUST NOT** use any instance specific parameters
    for the VNF or PNF in roles/cookbooks/recipes invoked for a VNF or PNF
    action.

.. req::
    :id: R-37929
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** accept all necessary instance specific
    data from the environment or node object attributes for the VNF or PNF
    in roles/cookbooks/recipes invoked for a VNF or PNF action.

.. req::
    :id: R-62170
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** over-ride any default values for
    configurable parameters that can be set by ONAP in the roles,
    cookbooks and recipes.

.. req::
    :id: R-78116
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** update status on the Chef Server
    appropriately (e.g., via a fail or raise an exception) if the
    chef-client run encounters any critical errors/failures when
    executing a VNF or PNF action.

.. req::
    :id: R-44013
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** populate an attribute, defined as node
    ['PushJobOutput'] with the desired output on all nodes in the push job
    that execute chef-client run if the VNF or PNF action requires the output
    of a chef-client run be made available (e.g., get running configuration).

.. req::
    :id: R-30654
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF Package **MUST** have appropriate cookbooks that are
    designed to automatically 'rollback' to the original state in case of
    any errors for actions that change state of the VNF or PNF (e.g.,
    configure).

.. req::
    :id: R-65755
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** support callback URLs to return information
    to ONAP upon completion of the chef-client run for any chef-client run
    associated with a VNF or PNF action.

    -  As part of the push job, ONAP will provide two parameters in the
       environment of the push job JSON object:

        -  "RequestId" a unique Id to be used to identify the request,
        -  "CallbackUrl", the URL to post response back.

    -  If the CallbackUrl field is empty or missing in the push job, then
       the chef-client run need not post the results back via callback.

.. req::
    :id: R-15885
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** Upon completion of the chef-client run,
    POST back on the callback URL, a JSON object as described in Table
    A2 if the chef-client run list includes a cookbook/recipe that is
    callback capable. Failure to POST on the Callback Url should not be
    considered a critical error. That is, if the chef-client successfully
    completes the VNF or PNF action, it should reflect this status on the Chef
    Server regardless of whether the Callback succeeded or not.

ONAP Chef API Usage
~~~~~~~~~~~~~~~~~~~

This section outlines the workflow that ONAP invokes when it receives an
action request against a Chef managed VNF or PNF.

1. When ONAP receives a request for an action for a Chef Managed VNF or PNF, it
   retrieves the corresponding template (based on **action** and
   **VNF or PNF**) from its database and sets necessary values in the
   "Environment", "Node" and "NodeList" keys (if present) from either
   the payload of the received action or internal data.

2. If "Environment" key is present in the updated template, it posts the
   corresponding JSON dictionary to the appropriate Environment object
   REST endpoint on the Chef Server thus updating the Environment
   attributes on the Chef Server.

3. Next, it creates a Node Object from the "Node" JSON dictionary for
   all elements listed in the NodeList (using the FQDN to construct the
   endpoint) by replicating it  [#7.3.2]_. As part of this process, it will
   set the name field in each Node Object to the corresponding FQDN.
   These node objects are then posted on the Chef Server to
   corresponding Node Object REST endpoints to update the corresponding
   node attributes.

4. If PushJobFlag is set to "True" in the template, ONAP requests a push
   job against all the nodes in the NodeList to trigger
   chef-client. It will not invoke any other command via the push
   job. ONAP will include a callback URL in the push job request and a
   unique Request Id. An example push job posted by ONAP is listed
   below:

.. code-block:: java

  {
   "command": "chef-client"
   "run_timeout": 300
   "nodes": ["node1.vnf_a.onap.com", "node2.vnf_a.onap.com"]
     "env": {
              "RequestId":"8279-abcd-aksdj-19231"
              "CallbackUrl":"<callback>"
            }
  }


5. If CallbackCapable field in the template is not present or set to
   "False" ONAP will poll the Chef Server to check completion status of
   the push job.

6. If "GetOutputFlag" is set to "True" in the template and
   CallbackCapable is not set to "True", ONAP will retrieve any output
   from each node where the push job has finished by accessing the Node
   Object attribute node['PushJobOutput'].

.. _ansible_playbook_requirements:

Ansible Standards and Capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP will support configuration of VNFs or PNFs via Ansible subject to the
requirements and guidelines defined in this section.

Ansible allows agentless management of VNFs or PNFs/VMs/VNFCs via execution
of 'playbooks' over ssh. The 'playbooks' are a structured set of
tasks which contain all the necessary resources and execution capabilities
to take the necessary action on one or more target VMs (and/or VNFCs)
of the VNF. ONAP will utilize the framework of an Ansible Server that
will host all Ansible artifacts and run playbooks to manage VNFs or PNFs that
support Ansible.

VNF or PNF Configuration via Ansible Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ansible Client Requirements
+++++++++++++++++++++++++++++


.. req::
    :id: R-32217
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** have routable management IP addresses or FQDNs that
    are reachable via the Ansible Server for the endpoints (VMs) of a
    VNF or PNF that playbooks will target. ONAP will initiate requests to the
    Ansible Server for invocation of playbooks against these end
    points [#7.3.3]_.

.. req::
    :id: R-54373
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** have Python >= 2.6 on the endpoint VM(s)
    of a VNF or PNF on which an Ansible playbook will be executed.

.. req::
    :id: R-35401
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support SSH and allow SSH access by the
    Ansible server to the endpoint VM(s) and comply with the Network
    Cloud Service Provider guidelines for authentication and access.

.. req::
    :id: R-82018
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

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

.. req::
    :id: R-92866
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** include as part of post-instantiation configuration
    done by Ansible Playbooks the removal/update of the SSH public key from
    /root/.ssh/authorized_keys, and update of SSH keys loaded through
    instantiation to support Ansible. This may include creating Mechanized user
    ID(s) used by the Ansible Server(s) on VNF VM(s) and uploading and
    installing new SSH keys used by the mechanized use ID(s).

.. req::
    :id: R-97345
    :target: VNF or PNF
    :keyword: MUST
    :introduced: casablanca
    :updated: dublin

    The VNF or PNF **MUST** permit authentication, using root account, only
    right after instantiation and until post-instantiation configuration is
    completed.

.. req::
    :id: R-97451
    :target: VNF or PNF
    :keyword: MUST
    :introduced: casablanca
    :updated: dublin

    The VNF or PNF **MUST** provide the ability to remove root access once
    post-instantiation configuration (Configure) is completed.

.. req::
    :id: R-91745
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** update the Ansible Server and other entities
    storing and using the SSH keys for authentication when the SSH
    keys used by Ansible are regenerated/updated.

    **Note**: Ansible Server itself may be used to upload new SSH public
    keys onto supported VNFs or PNFs.

.. req::
    :id: R-73459
    :target: VNF or PNF
    :keyword: MUST
    :introduced: casablanca
    :updated: dublin

    The VNF or PNF **MUST** provide the ability to include a "from=" clause in
    SSH public keys associated with mechanized user IDs created for an Ansible
    Server cluster to use for VNF or PNF VM authentication.

.. req::
    :id: R-45197
    :target: VNF or PNF
    :keyword: MUST
    :introduced: casablanca
    :updated: dublin

    The VNF or PNF **MUST** define the "from=" clause to provide the list of IP
    addresses of the Ansible Servers in the Cluster, separated by coma, to
    restrict use of the SSH key pair to elements that are part of the Ansible
    Cluster owner of the issued and assigned mechanized user ID.

.. req::
    :id: R-94567
    :target: VNF or PNF
    :keyword: MUST
    :introduced: casablanca
    :updated: dublin

    The VNF or PNF **MUST** provide Ansible playbooks that are designed to run
    using an inventory hosts file in a supported format with only IP addresses
    or IP addresses and VM/VNF or PNF names.

.. req::
    :id: R-67124
    :target: VNF or PNF
    :keyword: MUST
    :introduced: casablanca
    :updated: dublin

    The VNF or PNF **MUST** provide Ansible playbooks that are designed to run
    using an inventory hosts file in a supported format; with group names
    matching VNFC 3-character string adding "vip" for groups with virtual IP
    addresses shared by multiple VMs as seen in examples provided in Appendix.

.. req::
    :id: R-24482
    :target: VNF or PNF
    :keyword: MUST
    :introduced: casablanca
    :updated: dublin

    The VNF or PNF **MUST** provide Ansible playbooks that are designed to run
    using an inventory hosts file in a supported format; with site group that
    shall be used to add site specific configurations to the target VNF or PNF
    VM(s) as needed.

Ansible Playbook Requirements
+++++++++++++++++++++++++++++++

An Ansible playbook is a collection of tasks that is executed on the
Ansible server (local host) and/or the target VM (s) in order to
complete the desired action.

.. req::
    :id: R-49751
    :target: VNF or PNF
    :keyword: MUST
    :introduced: casablanca
    :updated: dublin

    The VNF or PNF **MUST** support Ansible playbooks that are compatible with
    Ansible version 2.6 or later.

.. req::
    :id: R-40293
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** make available playbooks that conform
    to the ONAP requirement.

.. req::
    :id: R-49396
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** support each APPC/SDN-C VNF or PNF action
    by invocation of **one** playbook [#7.3.4]_. The playbook will be
    responsible for executing all necessary tasks (as well as calling other
    playbooks) to complete the request.

.. req::
    :id: R-33280
    :target: VNF or PNF
    :keyword: MUST NOT
    :updated: dublin

    The VNF or PNF **MUST NOT** use any instance specific parameters
    in a playbook.

.. req::
    :id: R-48698
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

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

The Ansible Server will determine if a playbook invoked to execute an
VNF or PNF action finished successfully or not using the "PLAY_RECAP" summary
in Ansible log.  The playbook will be considered to successfully finish
only if the "PLAY RECAP" section at the end of playbook execution output
has no unreachable hosts and no failed tasks. Otherwise, the playbook
will be considered to have failed.


.. req::
    :id: R-43253
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** use playbooks designed to allow Ansible
    Server to infer failure or success based on the "PLAY_RECAP" capability.

    **Note**: There are cases where playbooks need to interpret results
    of a task and then determine success or failure and return result
    accordingly (failure for failed tasks).

.. req::
    :id: R-50252
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** write to a response file in JSON format that will
    be retrieved and made available by the Ansible Server if, as part of a VNF
    or PNF action (e.g., audit), a playbook is required to return any VNF or
    PNF information/response. The text files must be written in the main
    playbook home directory, in JSON format. The JSON file must be created for
    the VNF or PNF with the name '<VNF or PNF name>_results.txt'. All playbook
    output results, for all VNF or PNF VMs, to be provided as a response to the
    request, must be written to this response file.

.. req::
    :id: R-51442
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** use playbooks that are designed to
    automatically 'rollback' to the original state in case of any errors
    for actions that change state of the VNF or PNF (e.g., configure).

    **Note**: In case rollback at the playbook level is not supported or
    possible, the VNF or PNF provider shall provide alternative rollback
    mechanism (e.g., for a small VNF or PNF the rollback mechanism may rely
    on workflow to terminate and re-instantiate VNF VMs and then re-run
    playbook(s)). Backing up updated files is also recommended to support
    rollback when soft rollback is feasible.

.. req::
    :id: R-58301
    :target: VNF or PNF
    :keyword: SHOULD NOT
    :updated: dublin

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

.. req::
    :id: R-02651
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin

    The VNF or PNF **SHOULD** use available backup capabilities to save a
    copy of configuration files before implementing changes to support
    operations such as backing out of software upgrades, configuration
    changes or other work as this will help backing out of configuration
    changes when needed.

.. req::
    :id: R-43353
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** return control from Ansible Playbooks only after
    all tasks performed by playbook are fully complete, signaling that the
    playbook completed all tasks. When starting services, return control
    only after all services are up. This is critical for workflows where
    the next steps are dependent on prior tasks being fully completed.

Detailed examples:

``StopApplication Playbook`` – StopApplication Playbook shall return control
and a completion status response only after VNF or PNF application is fully
stopped, all processes/services stopped.

``StartApplication Playbook`` – StartApplication Playbook shall return control
and a completion status only after all VNF or PNF application services are
fully up, all processes/services started and ready to provide services.

**NOTE**: Start Playbook should not be declared complete/done after starting
one or several processes that start the other processes.

HealthCheck Playbook:

SUCCESS – HealthCheck success shall be returned (return code 0) by a
Playbook or Cookbook only when VNF or PNF is 100% healthy, ready to take
requests and provide services, with all VNF or PNF required capabilities ready
to provide services and with all active and standby resources fully ready with
no open MINOR, MAJOR or CRITICAL alarms.

NOTE: In some cases, a switch may need to be turned on, but a VNF or PNF
reported as healthy, should be ready to take service requests or be
already processing service requests successfully.

A successful execution of a health-check playbook shall create one response
file (per VNF or PNF) in JSON format, named after the VNF or PNF instance,
followed by "_results.txt" (<VNF or PNF instance name>_results.txt) to be
provided as a response to the requestor, indicating  health-check was executed
and completed successfully, example: vfdb9904v_results.txt, with the following
contents:

.. code-block:: java

  {
   "identifier": "VNF",
   "state": "healthy",
   "time": "2018-03-16:1139"
  }

Example:

.. code-block:: java

  $ cat vfdb9904v_results.txt
  {
   "identifier": "VNF",
   "state": "healthy",
   "time": "2018-03-16:1139"
  }


**NOTE**: See section 7.3.1.4 for comments on support of partial health checks.

FAILURE – A health check playbook shall return a non-zero return code in
case VNF or PNF is not 100% healthy because one or more VNF or PNF application
processes are stopped or not ready to take service requests or because critical
or non-critical resources are not ready or because there are open MINOR, MAJOR
or CRITICAL traps/alarms or because there are issues with the VNF or PNF that
need attention even if they do not impact services provided by the VNF or PNF.

A failed health-check playbook shall also create one file (per VNF or PNF), in
JSON format, named after the VNF or PNF instance name, followed by
"_results.txt" to indicate health-check was executed and found issues in the
health of the VNF or PNF. This is to differentiate from failure to run
health-check playbook or playbook tasks to verify the health of the VNF or
PNF, example: vfdb9904v_results.txt, with the following contents:

.. code-block:: java

 {
  "identifier": "VNF",
  "state": "unhealthy",
  "info": "Error in following VM(s). Check hcstatus files
  under /tmp/ccfx9901v for details",
  "fault": [
    "vfdb9904vm001",
    "vfdb9904vm002"
  ],
  "time": "2018-03-16:4044"
 }


Example:

.. code-block:: java

 $ cat vfdb9904v_results.txt
 {
  "identifier": "VNF",
  "state": "unhealthy",
  "info": "Error in following VM(s). Check hcstatus files
  under /tmp/ccfx9901v for details",
  "fault": [
    "vfdb9904vm001",
    "vfdb9904vm002"
  ],
  "time": "2018-03-16:4044"
 }


See `VNF or PNF REST APIs`_ for additional details on HealthCheck.

Some VNFs or PNFs may support and desire to run partial health checks and
receive a successful response when partial health check completes without
errors. The parameter name used by HealthCheck playbook to request non-default
partial health check is healthcheck_type. Example of health check types
could be healthcheck_type=GuestOS, healthcheck_type=noDB,
healthcheck_type=noConnections, healthcheck_type=IgnoreAlarms, etc.. This
attribute-value pair may be passed by Orchestrator or Workflow or other
(northbound) APPC/SDN-C clients to APPC/SDN-C as part of the request.

By default, when no argument/parameter is passed, healthcheck playbook
performs a full VNF or PNF health check.

.. req::
    :id: R-24189
    :target: VNF or PNF
    :keyword: SHOULD
    :introduced: casablanca
    :updated: dublin

    The VNF or PNF provider **MUST** deliver a new set of playbooks that
    includes all updated and unchanged playbooks for any new revision to an
    existing set of playbooks.

.. req::
    :id: R-49911
    :target: VNF or PNF
    :keyword: SHOULD
    :updated: dublin
    :introduced: casablanca

    The VNF or PNF provider **MUST** assign a new point release to the updated
    playbook set. The functionality of a new playbook set must be tested before
    it is deployed to the production.


Ansible API Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section outlines the workflow that APPC/SDN-C invokes when
it receives an action request against an Ansible managed VNF or PNF.

 #. When APPC/SDN-C receives a request for an action for an
    Ansible managed VNF or PNF, it retrieves the corresponding template (based
    on **action** and **VNF or PNF Type**) from its database and sets necessary
    values (such as an Id, NodeList, and EnvParameters) from either
    information either in the request or data obtained from other sources,
    inventory database, is an example of such sources.
    This is referred to as the payload that is sent as a JSON object
    to the Ansible server as part of the Rest API request.
 #. The APPC/SDN-C sends a request to the Ansible server to
    execute the action.
 #. The APPC/SDN-C, after sending a request to the Ansible server,
    polls it to get results(success or failure). The APPC/SDN-C has a
    timeout value which is contained in the action request template. Different
    actions can set different timeout values (default setting is 600 seconds).
    If the result is not available when the timeout is reached, the APPC/SDN-C
    stops polling and returns a timeout error to the requester.
    The Ansible Server continues to process the request.


Support of APPC/SDN-C Commands And Southbound Protocols
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table summarizes the commands and possible protocols selected.
Note that the HealthCheck can also be supported via REST.

Table 8. APPC/SDN-C APIs and NETCONF Commands

+-------------+--------------------+--------------------+--------------------+
|**Command**  |**NETCONF Support** |**Chef Support**    |**Ansible**         |
+=============+====================+====================+====================+
|General      |For each RPC, the   |VNF or PNF Vendor   |VNF Vendor must     |
|Comments     |appropriate RPC     |must provide any    |provide an Ansible  |
|             |operation is listed.|necessary roles,    |playbook to retrieve|
|             |                    |cookbooks, recipes  |the running         |
|             |                    |to retrieve the     |configuration from a|
|             |                    |running             |VNF and place the   |
|             |                    |configuration from  |output on the       |
|             |                    |a VNF or PNF and    |Ansible server in   |
|             |                    |place it in the     |a manner aligned    |
|             |                    |respective Node     |with playbook       |
|             |                    |Objects             |requirements listed |
|             |                    |'PushJobOutput'     |in this document.   |
|             |                    |attribute of all    |                    |
|             |                    |nodes in NodeList   |The PlaybookName    |
|             |                    |when triggered by a |must be provided    |
|             |                    |chef-client run.    |in the JSON file.   |
|             |                    |                    |                    |
|             |                    |The JSON file for   |NodeList must list  |
|             |                    |this VNF or PNF     |IP addresses or DNS |
|             |                    |action is required  |supported FQDNs of  |
|             |                    |to set "PushJobFlag"|an example VNF      |
|             |                    |to "True" and       |on which to         |
|             |                    |"GetOutputFlag" to  |execute playbook.   |
|             |                    |"True". The "Node"  |                    |
|             |                    |JSON dictionary     |                    |
|             |                    |must have the run   |                    |
|             |                    |list populated      |                    |
|             |                    |with the necessary  |                    |
|             |                    |sequence of roles,  |                    |
|             |                    |cookbooks, recipes. |                    |
|             |                    |                    |                    |
|             |                    |The Environment     |                    |
|             |                    |and Node values     |                    |
|             |                    |should contain all  |                    |
|             |                    |appropriate         |                    |
|             |                    |configuration       |                    |
|             |                    |attributes.         |                    |
|             |                    |                    |                    |
|             |                    |NodeList must       |                    |
|             |                    |list sample FQDNs   |                    |
|             |                    |that are required to|                    |
|             |                    |conduct a           |                    |
|             |                    |chef-client run for |                    |
|             |                    |this VNF Action.    |                    |
+-------------+--------------------+--------------------+--------------------+
|Audit        |The <get-config> is |Supported via a     |Supported via a     |
|             |used to return the  |cookbook that       |playbook that       |
|             |running             |returns the running |returns the running |
|             |configuration.      |configuration.      |configuration.      |
+-------------+--------------------+--------------------+--------------------+
|Configure,   |The <edit-config>   |Supported via a     |Supported via a     |
|ModifyConfig |operation loads all |cookbook that       |playbook that       |
|             |or part of a        |updates the VNF or  |updates the VNF     |
|             |specified data set  |PNF configuration.  |configuration.      |
|             |to the specified    |                    |                    |
|             |target database. If |                    |                    |
|             |there is no         |                    |                    |
|             |<candidate/>        |                    |                    |
|             |database, then the  |                    |                    |
|             |target is the       |                    |                    |
|             |<running/> database.|                    |                    |
|             |A <commit> follows. |                    |                    |
+-------------+--------------------+--------------------+--------------------+
|Other        |This command has no |Supported via a     |Supported via a     |
|Configuration|existing NETCONF RPC|cookbook that       |playbook that       |
|Commands     |action.             |performs            |performs            |
|             |                    |the action.         |the action.         |
+-------------+--------------------+--------------------+--------------------+
|Lifecycle    |This command has no |Supported via a     |Supported via a     |
|Management   |existing NETCONF RPC|cookbook that       |playbook that       |
|Commands     |action.             |performs            |performs            |
|             |                    |the action.         |the action.         |
+-------------+--------------------+--------------------+--------------------+
|Health Check |This command has no |Supported via a     |Supported           |
|             |existing NETCONF RPC|cookbook            |via a               |
|             |action.             |that                |playbook            |
|             |                    |performs            |that                |
|             |                    |a HealthCheck and   |performs            |
|             |                    |returns the results.|the                 |
|             |                    |                    |HealthCheck         |
|             |                    |                    |and returns         |
|             |                    |                    |the                 |
|             |                    |                    |results.            |
+-------------+--------------------+--------------------+--------------------+

.. [#7.3.1]
   https://github.com/mbj4668/pyang

.. [#7.3.2]
   Recall that the Node Object **is required** to be identical across
   all VMs of a VNF or PNF invoked as part of the action except for the "name".

.. [#7.3.3]
   Upstream elements must provide the appropriate FQDN in the request to
   ONAP for the desired action.

.. [#7.3.4]
   Multiple ONAP actions may map to one playbook.


