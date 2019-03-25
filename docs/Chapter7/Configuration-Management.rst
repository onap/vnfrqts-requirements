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

Controller Interactions With xNF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

APPC/SDN-C expose a northbound API to clients (such as SO) in order for
the clients to initiate an activity (aka command) on a xNF. APPC/SDN-C
interact with xNFs through Network and Application Adapters to perform
configuration and other lifecycle management activities within NFV environment.
The standardized models, protocols and mechanisms by which network functions
are configured are equally applicable to VNFs and PNFs.

This section describes the list of commands that should be supported
by the xNF. The following sections describe the standard protocols
that are supported (NETCONF, Chef, Ansible, and REST).

The commands below are expected to be supported on all xNF's, unless
The commands below are expected to be supported on all xNF's, unless
noted otherwise, either directly (via the NETCONF or REST interface)
or indirectly (via a Chef Cookbook or Ansible server).

**Note that there are additional commands offered to northbound clients that
are not shown below, as these commands either act internally on APPC/SDN-C
itself or depend upon network cloud components for implementation (thus, these
actions do not put any special requirement on the xNF provider).**

The commands allow for parametric data to be passed from APPC/SDN-C
to the xNF or Ansible/Chef server in the request. The format of the
parameter data can be either xml (for NETCONF) or JSON (for Ansible,
Chef, or REST).

Configuration Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Configure``: The APPC/SDN-C client is requesting that a post-instantiation
configuration be applied to the target xNF. After the Configure
action is completed, the xNF instance should be ready for service.
Note that customer specific configurations may need to be applied using
the ConfigModify action. This command requires exclusive access rights of
the xNF.

``ConfigModify``: The APPC client is requesting a configuration
update to a subset of the total configuration parameters of an xNF or to
apply customer specific configurations. The configuration update is
typically done while the xNF is in service and should not disrupt traffic.
This command requires exclusive access rights of the xNF.

``ConfigBackup``: The APPC client is requesting a backup of the
configuration parameters where the parameters are stored on the xNF.
This command is typically requested as part of an orchestration flow
for scenarios such as a software upgrade. The ConfigBackup is typically
done while the xNF is not in service (i.e., in a maintenance state).
When the ConfigBackup command is executed, the current xNF configuration
parameters are saved in storage that is preserved (if there is an existing
set of backed up parameters, they are overwritten). This command requires
exclusive access rights of the xNF.

``ConfigRestore``: The APPC client is requesting a restore action of
the configuration parameters to the xNF that were saved by ConfigBackup
command. This command is typically requested as part of an orchestration
flow for scenarios such as a software upgrade where the software upgrade
may have failed and the xNF needs to be rolled back to the prior configuration.
When the ConfigRestore command is executed, the xNF configuration parameters
which were backed to persistent preserved storage are applied to the xNF
(replacing existing parameters). The ConfigRestore is typically done while
the xNF is not in service (i.e., in a maintenance state). This command
requires exclusive access rights of the xNF.

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
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC/SDN-C ``Configure`` command.

.. req::
    :id: R-19366
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC ``ConfigModify`` command.

.. req::
    :id: R-32981
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC ``ConfigBackup`` command.

.. req::
    :id: R-48247
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC ``ConfigRestore`` command.

.. req::
    :id: R-94084
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC/SDN-C ``ConfigScaleOut`` command.

.. req::
    :id: R-56385
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC ``Audit`` command.

Lifecycle Management Related Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**The following commands are needed to support various lifecycle management
flows where the VNF may need to be removed for service.**

Full details on the APIs can be found in the :doc:`APPC LCM API Guide <../../../../appc.git/docs/APPC LCM API Guide/APPC LCM API Guide>`

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

``QuiesceTraffic`` The APPC/SDN-C client is requesting the xNF gracefully
stop traffic (aka block and drain traffic). The method for quiescing traffic
is specific to the xNF architecture. The action is completed when all
(in-flight transactions) traffic has stopped. The xNF remains in an active
state where the xNF is able to process traffic (initiated using the
ResumeTraffic action).

``ResumeTraffic``: The APPC/SDN-C client is requesting the xNF resume
processing traffic. The method to resume traffic is specific to the xNF
architecture.

``StopApplication``: The APPC client is requesting that the application
running on the xNF is stopped gracefully (i.e., without traffic loss).
This is equivalent to quiescing the traffic and then stopping the application
processes. The processes can be restarted using the StartApplication command.

``StartApplication``: The APPC client is requesting that the application
running on the xNF is started. Get ready to process traffic. Traffic processing
can be resumed using the ResumeTraffic command.

**The following commands are needed to support software upgrades, in-place or
other type of software upgrade. The xNF instance may be removed from service
for the upgrade.**

``UpgradePrecheck``: The APPC/SDN-C client is requesting a confirmation that
the xNF can (and needs to) be upgraded to a specific software version
(specified in the request). Checking software installed and running on
the xNF matches software version, intended to be upgraded, is one of the
recommended checks.

``UpgradeSoftware``: The APPC/SDN-C client is requesting that a (in-place)
software upgrade be performed on the xNF.  The software to be applied is
pre-loaded to a specified location.

``UpgradePostCheck``: The APPC/SDN-C client is requesting a confirmation that
the xNF software upgrade has been completed successfully (xNF upgraded to
the new software version). Checking software installed and running on the xNF
matches software version, of the newly upgraded software, is one of the
recommended checks.

``UpgradeBackup``: The APPC/SDN-C client is requesting that the xNF is backed
up prior to the UpgradeSoftware.

``UpgradeBackOut``: The APPC/SDN-C client is requesting that the xNF upgrade
is backed out (in the event that the SoftwareUpgrade or UpgradePostCheck
failed).

.. req::
    :id: R-328086
    :target: XNF
    :keyword: MUST
    :introduced: casablanca

    The xNF **MUST**, if serving as a distribution point or anchor point for
    steering point from source to destination, support the ONAP Controller's
    ``DistributeTraffic`` command.

.. req::
    :id: R-12706
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC/SDN-C ``QuiesceTraffic`` command.

.. req::
    :id: R-07251
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC/SDN-C ``ResumeTraffic`` command.

.. req::
    :id: R-83146
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC ``StopApplication`` command.

.. req::
    :id: R-82811
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC ``StartApplication`` command.

.. req::
    :id: R-19922
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC/SDN-C ``UpgradePrecheck`` command.

.. req::
    :id: R-49466
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC/SDN-C ``UpgradeSoftware`` command.

.. req::
    :id: R-45856
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC/SDN-C ``UpgradePostCheck`` command.

.. req::
    :id: R-97343
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC/SDN-C ``UpgradeBackup`` command.

.. req::
    :id: R-65641
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC/SDN-C ``UpgradeBackOut`` command.


HealthCheck and Failure Related Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``HealthCheck`` The APPC/SDN-C client is requesting a health check over the
entire scope of the xNF. The xNF must be 100% healthy, ready to take requests
and provide services, with all xNF required capabilities ready to provide
services and with all active and standby resources fully ready with no open
MINOR, MAJOR or CRITICAL alarms. This is expected to be the default in the
event that no parameter is passed to the Healthcheck playbook, cookbook, etc.

Some xNFs may support and desire to run partial healthchecks and receive a
successful response when partial health check completes without errors.
The parameter name used by HealthCheck playbook to request non-default
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
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support APPC/SDN-C ``HealthCheck`` command.

Notes On Command Support Using APPC/SDN-C Southbound Protocols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

APPC/SDN-C are designed to support a standard set of protocols in
order to communicate with the xNF instance. The supported protocols are
NETCONF, Ansible, Chef, and REST.

NETCONF and REST require the xNF to implement a server which supports the RPC
or REST calls.

Ansible and Chef require the use of a Ansible or Chef server which communicates
with the APPC/SDN-C (northbound) and the xNF VM's (southbound).

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
NETCONF APIs to make the required changes in the xNF state and
configuration. The xNF providers must provide the Device YANG model and
NETCONF server supporting NETCONF APIs to comply with target ONAP and
industry standards.

xNF Configuration via NETCONF Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration Management
+++++++++++++++++++++++++++


.. req::
    :id: R-88026
    :target: XNF
    :keyword: MUST

    The xNF **MUST** include a NETCONF server enabling
    runtime configuration and lifecycle management capabilities.

.. req::
    :id: R-95950
    :target: XNF
    :keyword: MUST

    The xNF **MUST** provide a NETCONF interface fully defined
    by supplied YANG models for the embedded NETCONF server.

NETCONF Server Requirements
++++++++++++++++++++++++++++++


.. req::
    :id: R-73468
    :target: XNF
    :keyword: MUST

    The xNF **MUST** allow the NETCONF server connection
    parameters to be configurable during virtual machine instantiation
    through Heat templates where SSH keys, usernames, passwords, SSH
    service and SSH port numbers are Heat template parameters.

.. req::
    :id: R-90007
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** implement the protocol operation:
    ``close-session()`` - Gracefully close the current session.

.. req::
    :id: R-70496
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** implement the protocol operation:
    ``commit(confirmed, confirm-timeout)`` - Commit candidate
    configuration data store to the running configuration.

.. req::
    :id: R-18733
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** implement the protocol operation:
    ``discard-changes()`` - Revert the candidate configuration
    data store to the running configuration.

.. req::
    :id: R-44281
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** implement the protocol operation:
    ``edit-config(target, default-operation, test-option, error-option,
    config)`` - Edit the target configuration data store by merging,
    replacing, creating, or deleting new config elements.

.. req::
    :id: R-60106
    :target: XNF
    :keyword: MUST

    The xNF **MUST** implement the protocol operation:
    ``get(filter)`` - Retrieve (a filtered subset of) the running
    configuration and device state information. This should include
    the list of xNF supported schemas.

.. req::
    :id: R-29488
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** implement the protocol operation:
    ``get-config(source, filter`` - Retrieve a (filtered subset of
    a) configuration from the configuration data store source.

.. req::
    :id: R-11235
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** implement the protocol operation:
    ``kill-session(session``- Force the termination of **session**.

.. req::
    :id: R-02597
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** implement the protocol operation:
    ``lock(target)`` - Lock the configuration data store target.

.. req::
    :id: R-96554
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** implement the protocol operation:
    ``unlock(target)`` - Unlock the configuration data store target.

.. req::
    :id: R-29324
    :target: XNF
    :keyword: SHOULD
    :updated: casablanca

    The xNF **SHOULD** implement the protocol operation:
    ``copy-config(target, source)`` - Copy the content of the
    configuration data store source to the configuration data store target.

.. req::
    :id: R-88031
    :target: XNF
    :keyword: SHOULD
    :updated: casablanca

    The xNF **SHOULD** implement the protocol operation:
    ``delete-config(target)`` - Delete the named configuration
    data store target.

.. req::
    :id: R-97529
    :target: XNF
    :keyword: SHOULD

    The xNF **SHOULD** implement the protocol operation:
    ``get-schema(identifier, version, format)`` - Retrieve the YANG schema.

.. req::
    :id: R-62468
    :target: XNF
    :keyword: MUST

    The xNF **MUST** allow all configuration data to be
    edited through a NETCONF <edit-config> operation. Proprietary
    NETCONF RPCs that make configuration changes are not sufficient.

.. req::
    :id: R-01382
    :target: XNF
    :keyword: MUST

    The xNF **MUST** allow the entire configuration of the xNF to be
    retrieved via NETCONF's <get-config> and <edit-config>, independently
    of whether it was configured via NETCONF or other mechanisms.

.. req::
    :id: R-28756
    :target: XNF
    :keyword: MUST

    The xNF **MUST** support ``:partial-lock`` and
    ``:partial-unlock`` capabilities, defined in RFC 5717. This
    allows multiple independent clients to each write to a different
    part of the <running> configuration at the same time.

.. req::
    :id: R-83873
    :target: XNF
    :keyword: MUST

    The xNF **MUST** support ``:rollback-on-error`` value for
    the <error-option> parameter to the <edit-config> operation. If any
    error occurs during the requested edit operation, then the target
    database (usually the running configuration) will be left unaffected.
    This provides an 'all-or-nothing' edit mode for a single <edit-config>
    request.

.. req::
    :id: R-68990
    :target: XNF
    :keyword: MUST

    The xNF **MUST** support the ``:startup`` capability. It
    will allow the running configuration to be copied to this special
    database. It can also be locked and unlocked.

.. req::
    :id: R-68200
    :target: XNF
    :keyword: MUST

    The xNF **MUST** support the ``:url`` value to specify
    protocol operation source and target parameters. The capability URI
    for this feature will indicate which schemes (e.g., file, https, sftp)
    that the server supports within a particular URL value. The 'file'
    scheme allows for editable local configuration databases. The other
    schemes allow for remote storage of configuration databases.

.. req::
    :id: R-20353
    :target: XNF
    :keyword: MUST

    The xNF **MUST** implement both ``:candidate`` and
    ``:writable-running`` capabilities. When both ``:candidate`` and
    ``:writable-running`` are provided then two locks should be supported.

.. req::
    :id: R-11499
    :target: XNF
    :keyword: MUST

    The xNF **MUST** fully support the XPath 1.0 specification
    for filtered retrieval of configuration and other database contents.
    The 'type' attribute within the <filter> parameter for <get> and
    <get-config> operations may be set to 'xpath'. The 'select' attribute
    (which contains the XPath expression) will also be supported by the
    server. A server may support partial XPath retrieval filtering, but
    it cannot advertise the ``:xpath`` capability unless the entire XPath
    1.0 specification is supported.

.. req::
    :id: R-83790
    :target: XNF
    :keyword: MUST

    The xNF **MUST** implement the ``:validate`` capability.

.. req::
    :id: R-49145
    :target: XNF
    :keyword: MUST

    The xNF **MUST** implement ``:confirmed-commit`` If
    ``:candidate`` is supported.

.. req::
    :id: R-58358
    :target: XNF
    :keyword: MUST

    The xNF **MUST** implement the ``:with-defaults`` capability
    [RFC6243].

.. req::
    :id: R-59610
    :target: XNF
    :keyword: MUST

    The xNF **MUST** implement the data model discovery and
    download as defined in [RFC6022].

.. req::
    :id: R-93443
    :target: XNF
    :keyword: MUST

    The xNF **MUST** define all data models in YANG [RFC6020],
    and the mapping to NETCONF shall follow the rules defined in this RFC.

.. req::
    :id: R-26115
    :target: XNF
    :keyword: MUST

    The xNF **MUST** follow the data model upgrade rules defined
    in [RFC6020] section 10. All deviations from section 10 rules shall
    be handled by a built-in automatic upgrade mechanism.

.. req::
    :id: R-10716
    :target: XNF
    :keyword: MUST

    The xNF **MUST** support parallel and simultaneous
    configuration of separate objects within itself.

.. req::
    :id: R-29495
    :target: XNF
    :keyword: MUST

    The xNF **MUST** support locking if a common object is
    being manipulated by two simultaneous NETCONF configuration operations
    on the same xNF within the context of the same writable running data
    store (e.g., if an interface parameter is being configured then it
    should be locked out for configuration by a simultaneous configuration
    operation on that same interface parameter).

.. req::
    :id: R-53015
    :target: XNF
    :keyword: MUST

    The xNF **MUST** apply locking based on the sequence of
    NETCONF operations, with the first configuration operation locking
    out all others until completed.

.. req::
    :id: R-02616
    :target: XNF
    :keyword: MUST

    The xNF **MUST** permit locking at the finest granularity
    if a xNF needs to lock an object for configuration to avoid blocking
    simultaneous configuration operations on unrelated objects (e.g., BGP
    configuration should not be locked out if an interface is being
    configured or entire Interface configuration should not be locked out
    if a non-overlapping parameter on the interface is being configured).

.. req::
    :id: R-41829
    :target: XNF
    :keyword: MUST

    The xNF **MUST** be able to specify the granularity of the
    lock via a restricted or full XPath expression.

.. req::
    :id: R-66793
    :target: XNF
    :keyword: MUST

    The xNF **MUST** guarantee the xNF configuration integrity
    for all simultaneous configuration operations (e.g., if a change is
    attempted to the BUM filter rate from multiple interfaces on the same
    EVC, then they need to be sequenced in the xNF without locking either
    configuration method out).

.. req::
    :id: R-54190
    :target: XNF
    :keyword: MUST

    The xNF **MUST** release locks to prevent permanent lock-outs
    when/if a session applying the lock is terminated (e.g., SSH session
    is terminated).

.. req::
    :id: R-03465
    :target: XNF
    :keyword: MUST

    The xNF **MUST** release locks to prevent permanent lock-outs
    when the corresponding <partial-unlock> operation succeeds.

.. req::
    :id: R-63935
    :target: XNF
    :keyword: MUST

    The xNF **MUST** release locks to prevent permanent lock-outs
    when a user configured timer has expired forcing the NETCONF SSH Session
    termination (i.e., product must expose a configuration knob for a user
    setting of a lock expiration timer).

.. req::
    :id: R-10173
    :target: XNF
    :keyword: MUST

    The xNF **MUST** allow another NETCONF session to be able to
    initiate the release of the lock by killing the session owning the lock,
    using the <kill-session> operation to guard against hung NETCONF sessions.

.. req::
    :id: R-88899
    :target: XNF
    :keyword: MUST

    The xNF **MUST** support simultaneous <commit> operations
    within the context of this locking requirements framework.

.. req::
    :id: R-07545
    :target: XNF
    :keyword: MUST

    The xNF **MUST** support all operations, administration and
    management (OAM) functions available from the supplier for xNFs using
    the supplied YANG code and associated NETCONF servers.

.. req::
    :id: R-60656
    :target: XNF
    :keyword: MUST

    The xNF **MUST** support sub tree filtering.

.. req::
    :id: R-80898
    :target: XNF
    :keyword: MUST

    TThe xNF **MUST** support heartbeat via a <get> with null filter.

.. req::
    :id: R-25238
    :target: VNF
    :keyword: MUST

    The xNF PACKAGE **MUST** validated YANG code using the open
    source pyang [#7.3.1]_ program using the following commands:

    .. code-block:: text

      $ pyang --verbose --strict <YANG-file-name(s)> $ echo $!

.. req::
    :id: R-63953
    :target: XNF
    :keyword: MUST

    The xNF **MUST** have the echo command return a zero value
    otherwise the validation has failed.

.. req::
    :id: R-26508
    :target: XNF
    :keyword: MUST

    The xNF **MUST** support a NETCONF server that can be mounted on
    OpenDaylight (client) and perform the operations of: modify, update,
    change, rollback configurations using each configuration data element,
    query each state (non-configuration) data element, execute each YANG
    RPC, and receive data through each notification statement.

The following requirements provides the Yang models that suppliers must
conform, and those where applicable, that suppliers need to use.


.. req::
    :id: R-28545
    :target: XNF
    :keyword: MUST

    The xNF **MUST** conform its YANG model to RFC 6060,
    "YANG - A Data Modeling Language for the Network Configuration
    Protocol (NETCONF)".

.. req::
    :id: R-22700
    :target: XNF
    :keyword: MUST

    The xNF **MUST** conform its YANG model to RFC 6470,
    "NETCONF Base Notifications".

.. req::
    :id: R-10353
    :target: XNF
    :keyword: MUST

    The xNF **MUST** conform its YANG model to RFC 6244,
    "An Architecture for Network Management Using NETCONF and YANG".

.. req::
    :id: R-53317
    :target: XNF
    :keyword: MUST

    The xNF **MUST** conform its YANG model to RFC 6087,
    "Guidelines for Authors and Reviewers of YANG Data Model Documents".

.. req::
    :id: R-33955
    :target: XNF
    :keyword: SHOULD

    The xNF **SHOULD** conform its YANG model to RFC 6991,
    "Common YANG Data Types".

.. req::
    :id: R-22946
    :target: XNF
    :keyword: SHOULD

    The xNF **SHOULD** conform its YANG model to RFC 6536,
    "NETCONF Access Control Model".

.. req::
    :id: R-10129
    :target: XNF
    :keyword: SHOULD

    The xNF **SHOULD** conform its YANG model to RFC 7223,
    "A YANG Data Model for Interface Management".

.. req::
    :id: R-12271
    :target: XNF
    :keyword: SHOULD

    The xNF **SHOULD** conform its YANG model to RFC 7223,
    "IANA Interface Type YANG Module".

.. req::
    :id: R-49036
    :target: XNF
    :keyword: SHOULD

    The xNF **SHOULD** conform its YANG model to RFC 7277,
    "A YANG Data Model for IP Management".

.. req::
    :id: R-87564
    :target: XNF
    :keyword: SHOULD

    The xNF **SHOULD** conform its YANG model to RFC 7317,
    "A YANG Data Model for System Management".

.. req::
    :id: R-24269
    :target: XNF
    :keyword: SHOULD

    The xNF **SHOULD** conform its YANG model to RFC 7407,
    "A YANG Data Model for SNMP Configuration", if Netconf used to
    configure SNMP engine.

The NETCONF server interface shall fully conform to the following
NETCONF RFCs.


.. req::
    :id: R-33946
    :target: XNF
    :keyword: MUST

    The xNF **MUST** conform to the NETCONF RFC 4741,
    "NETCONF Configuration Protocol".

.. req::
    :id: R-04158
    :target: XNF
    :keyword: MUST

    The xNF **MUST** conform to the NETCONF RFC 4742,
    "Using the NETCONF Configuration Protocol over Secure Shell (SSH)".

.. req::
    :id: R-13800
    :target: XNF
    :keyword: MUST

    The xNF **MUST** conform to the NETCONF RFC 5277,
    "NETCONF Event Notification".

.. req::
    :id: R-01334
    :target: XNF
    :keyword: MUST

    The xNF **MUST** conform to the NETCONF RFC 5717,
    "Partial Lock Remote Procedure Call".

.. req::
    :id: R-08134
    :target: XNF
    :keyword: MUST

    The xNF **MUST** conform to the NETCONF RFC 6241,
    "NETCONF Configuration Protocol".

.. req::
    :id: R-78282
    :target: XNF
    :keyword: MUST

    The xNF **MUST** conform to the NETCONF RFC 6242,
    "Using the Network Configuration Protocol over Secure Shell".

.. req::
    :id: R-997907
    :target: VNF or PNF
    :keyword: SHOULD
    :introduced: dublin

    The VNF or PNF **SHOULD** support TLS as secure transport for the NETCONF
    rotocol according to [RFC7589].


.. _xnf_rest_apis:

xNF REST APIs
^^^^^^^^^^^^^^^

HealthCheck is a command for which no NETCONF support exists.
Therefore, this must be supported using a RESTful interface
(defined in this section) or with a Chef cookbook/Ansible playbook
(defined in sections `Chef Standards and Capabilities`_ and
`Ansible Standards and Capabilities`_).

See section 7.3.1.4 for the definition of Full Healthcheck and Partial
Healthchecks.

The xNF must provide a REST formatted GET RPCs to support HealthCheck
queries via the GET method over HTTP(s).

The port number, url, and other authentication information is provided
by the xNF provider.

REST APIs
~~~~~~~~~

.. req::
    :id: R-31809
    :target: XNF
    :keyword: MUST

    The xNF **MUST** support the HealthCheck RPC. The HealthCheck
    RPC executes a xNF Provider-defined xNF HealthCheck over the scope of
    the entire xNF (e.g., if there are multiple VNFCs, then run a health check,
    as appropriate, for all VNFCs). It returns a 200 OK if the test completes.
    A JSON object is returned indicating state (healthy, unhealthy), scope
    identifier, time-stamp and one or more blocks containing info and fault
    information. If the xNF is unable to run the HealthCheck, return a
    standard http error code and message.

Examples of responses when HealthCheck runs and is able to provide a healthy
or unhealthy response:

.. code-block:: java

 {
   "identifier": "scope represented",
   "state": "healthy",
   "time": "01-01-1000:0000"
 }

 {
   "identifier": "scope represented",
   "state": "unhealthy",
    {[
   "info": "System threshold exceeded details",
   "fault":
     {
       "cpuOverall": 0.80,
       "cpuThreshold": 0.45
     }
     ]},
   "time": "01-01-1000:0000"
 }


Chef Standards and Capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP will support configuration of xNFs via Chef subject to the
requirements and guidelines defined in this section.

The Chef configuration management mechanism follows a client-server
model. It requires the presence of a Chef-Client on the xNF that will be
directly managed by a Chef Server. The Chef-client will register with
the appropriate Chef Server and are managed via 'cookbooks' and
configuration attributes loaded on the Chef Server which contain all
necessary information to execute the appropriate actions on the xNF via
the Chef-client.

ONAP will utilize the open source Chef Server, invoke the documented
Chef REST APIs to manage the xNF and requires the use of open source
Chef-Client and Push Jobs Client on the xNF
(https://downloads.chef.io/).

xNF Configuration via Chef Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chef Client Requirements
+++++++++++++++++++++++++


.. req::
    :id: R-79224
    :target: XNF
    :keyword: MUST

    The xNF **MUST** have the chef-client be preloaded with
    validator keys and configuration to register with the designated
    Chef Server as part of the installation process.

.. req::
    :id: R-72184
    :target: XNF
    :keyword: MUST

    The xNF **MUST** have routable FQDNs for all the endpoints
    (VMs) of a xNF that contain chef-clients which are used to register
    with the Chef Server.  As part of invoking xNF actions, ONAP will
    trigger push jobs against FQDNs of endpoints for a xNF, if required.

.. req::
    :id: R-47068
    :target: XNF
    :keyword: MAY

    The xNF **MAY** expose a single endpoint that is
    responsible for all functionality.

.. req::
    :id: R-67114
    :target: VNF
    :keyword: MUST

    The xNF **MUST** be installed with Chef-Client >= 12.0 and Chef
    push jobs client >= 2.0.

Chef Roles/Requirements
++++++++++++++++++++++++++

.. req::
    :id: R-27310
    :target: XNF
    :keyword: MUST

    The xNF Package **MUST** include all relevant Chef artifacts
    (roles/cookbooks/recipes) required to execute xNF actions requested by
    ONAP for loading on appropriate Chef Server.

.. req::
    :id: R-26567
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF Package **MUST** include a run list of
    roles/cookbooks/recipes, for each supported xNF action, that will
    perform the desired xNF action in its entirety as specified by ONAP
    (see Section 7.c, APPC/SDN-C APIs and Behavior, for list of xNF
    actions and requirements), when triggered by a chef-client run list
    in JSON file.

.. req::
    :id: R-98911
    :target: XNF
    :keyword: MUST NOT

    The xNF **MUST NOT** use any instance specific parameters
    for the xNF in roles/cookbooks/recipes invoked for a xNF action.

.. req::
    :id: R-37929
    :target: XNF
    :keyword: MUST

    The xNF **MUST** accept all necessary instance specific
    data from the environment or node object attributes for the xNF
    in roles/cookbooks/recipes invoked for a xNF action.

.. req::
    :id: R-62170
    :target: XNF
    :keyword: MUST

    The xNF **MUST** over-ride any default values for
    configurable parameters that can be set by ONAP in the roles,
    cookbooks and recipes.

.. req::
    :id: R-78116
    :target: XNF
    :keyword: MUST

    The xNF **MUST** update status on the Chef Server
    appropriately (e.g., via a fail or raise an exception) if the
    chef-client run encounters any critical errors/failures when
    executing a xNF action.

.. req::
    :id: R-44013
    :target: XNF
    :keyword: MUST

    The xNF **MUST** populate an attribute, defined as node
    ['PushJobOutput'] with the desired output on all nodes in the push job
    that execute chef-client run if the xNF action requires the output of a
    chef-client run be made available (e.g., get running configuration).

.. req::
    :id: R-30654
    :target: XNF
    :keyword: MUST

    The xNF Package **MUST** have appropriate cookbooks that are
    designed to automatically 'rollback' to the original state in case of
    any errors for actions that change state of the xNF (e.g., configure).

.. req::
    :id: R-65755
    :target: XNF
    :keyword: SHOULD

    The xNF **SHOULD** support callback URLs to return information
    to ONAP upon completion of the chef-client run for any chef-client run
    associated with a xNF action.

    -  As part of the push job, ONAP will provide two parameters in the
       environment of the push job JSON object:

        -  "RequestId" a unique Id to be used to identify the request,
        -  "CallbackUrl", the URL to post response back.

    -  If the CallbackUrl field is empty or missing in the push job, then
       the chef-client run need not post the results back via callback.

.. req::
    :id: R-15885
    :target: XNF
    :keyword: MUST

    The xNF **MUST** Upon completion of the chef-client run,
    POST back on the callback URL, a JSON object as described in Table
    A2 if the chef-client run list includes a cookbook/recipe that is
    callback capable. Failure to POST on the Callback Url should not be
    considered a critical error. That is, if the chef-client successfully
    completes the xNF action, it should reflect this status on the Chef
    Server regardless of whether the Callback succeeded or not.

ONAP Chef API Usage
~~~~~~~~~~~~~~~~~~~

This section outlines the workflow that ONAP invokes when it receives an
action request against a Chef managed xNF.

1. When ONAP receives a request for an action for a Chef Managed xNF, it
   retrieves the corresponding template (based on **action** and
   **xNF**) from its database and sets necessary values in the
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

ONAP will support configuration of xNFs via Ansible subject to the
requirements and guidelines defined in this section.

Ansible allows agentless management of xNFs/VMs/VNFCs via execution
of 'playbooks' over ssh. The 'playbooks' are a structured set of
tasks which contain all the necessary resources and execution capabilities
to take the necessary action on one or more target VMs (and/or VNFCs)
of the VNF. ONAP will utilize the framework of an Ansible Server that
will host all Ansible artifacts and run playbooks to manage xNFs that support
Ansible.

xNF Configuration via Ansible Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ansible Client Requirements
+++++++++++++++++++++++++++++


.. req::
    :id: R-32217
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** have routable management IP addresses or FQDNs that
    are reachable via the Ansible Server for the endpoints (VMs) of a
    xNF that playbooks will target. ONAP will initiate requests to the
    Ansible Server for invocation of playbooks against these end
    points [#7.3.3]_.

.. req::
    :id: R-54373
    :target: XNF
    :keyword: MUST

    The xNF **MUST** have Python >= 2.6 on the endpoint VM(s)
    of a xNF on which an Ansible playbook will be executed.

.. req::
    :id: R-35401
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support SSH and allow SSH access by the
    Ansible server to the endpoint VM(s) and comply with the Network
    Cloud Service Provider guidelines for authentication and access.

.. req::
    :id: R-82018
    :target: XNF
    :keyword: MUST
    :updated: casablanca

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

.. req::
    :id: R-92866
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** include as part of post-instantiation configuration
    done by Ansible Playbooks the removal/update of the SSH public key from
    /root/.ssh/authorized_keys, and update of SSH keys loaded through
    instantiation to support Ansible. This may include creating Mechanized user
    ID(s) used by the Ansible Server(s) on VNF VM(s) and uploading and
    installing new SSH keys used by the mechanized use ID(s).

.. req::
    :id: R-97345
    :target: XNF
    :keyword: MUST
    :introduced: casablanca

    The xNF **MUST** permit authentication, using root account, only right
    after instantiation and until post-instantiation configuration is
    completed.

.. req::
    :id: R-97451
    :target: XNF
    :keyword: MUST
    :introduced: casablanca

    The xNF **MUST** provide the ability to remove root access once
    post-instantiation configuration (Configure) is completed. 

.. req::
    :id: R-91745
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** update the Ansible Server and other entities
    storing and using the SSH keys for authentication when the SSH
    keys used by Ansible are regenerated/updated.

    **Note**: Ansible Server itself may be used to upload new SSH public
    keys onto supported xNFs.

.. req::
    :id: R-73459
    :target: XNF
    :keyword: MUST
    :introduced: casablanca

    The xNF **MUST** provide the ability to include a "from=" clause in SSH
    public keys associated with mechanized user IDs created for an Ansible
    Server cluster to use for xNF VM authentication.

.. req::
    :id: R-45197
    :target: XNF
    :keyword: MUST
    :introduced: casablanca

    The xNF **MUST** define the "from=" clause to provide the list of IP
    addresses of the Ansible Servers in the Cluster, separated by coma, to
    restrict use of the SSH key pair to elements that are part of the Ansible
    Cluster owner of the issued and assigned mechanized user ID. 

.. req::
    :id: R-94567
    :target: XNF
    :keyword: MUST
    :introduced: casablanca

    The xNF **MUST** provide Ansible playbooks that are designed to run using
    an inventory hosts file in a supported format with only IP addresses or
    IP addresses and VM/xNF names.

.. req::
    :id: R-67124
    :target: XNF
    :keyword: MUST
    :introduced: casablanca

    The xNF **MUST** provide Ansible playbooks that are designed to run using
    an inventory hosts file in a supported format; with group names matching
    VNFC 3-character string adding "vip" for groups with virtual IP addresses
    shared by multiple VMs as seen in examples provided in Appendix.

.. req::
    :id: R-24482
    :target: XNF
    :keyword: MUST
    :introduced: casablanca

    The xNF **MUST** provide Ansible playbooks that are designed to run using
    an inventory hosts file in a supported format; with site group that shall
    be used to add site specific configurations to the target xNF VM(s) as
    needed.

Ansible Playbook Requirements
+++++++++++++++++++++++++++++++

An Ansible playbook is a collection of tasks that is executed on the
Ansible server (local host) and/or the target VM (s) in order to
complete the desired action.

.. req::
    :id: R-49751
    :target: XNF
    :keyword: MUST
    :introduced: casablanca

    The xNF **MUST** support Ansible playbooks that are compatible with
    Ansible version 2.6 or later. 

.. req::
    :id: R-40293
    :target: XNF
    :keyword: MUST

    The xNF **MUST** make available playbooks that conform
    to the ONAP requirement.

.. req::
    :id: R-49396
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** support each APPC/SDN-C xNF action
    by invocation of **one** playbook [#7.3.4]_. The playbook will be responsible
    for executing all necessary tasks (as well as calling other playbooks)
    to complete the request.

.. req::
    :id: R-33280
    :target: XNF
    :keyword: MUST NOT

    The xNF **MUST NOT** use any instance specific parameters
    in a playbook.

.. req::
    :id: R-48698
    :target: XNF
    :keyword: MUST
    :updated: casablanca

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

The Ansible Server will determine if a playbook invoked to execute an
xNF action finished successfully or not using the "PLAY_RECAP" summary
in Ansible log.  The playbook will be considered to successfully finish
only if the "PLAY RECAP" section at the end of playbook execution output
has no unreachable hosts and no failed tasks. Otherwise, the playbook
will be considered to have failed.


.. req::
    :id: R-43253
    :target: XNF
    :keyword: MUST

    The xNF **MUST** use playbooks designed to allow Ansible
    Server to infer failure or success based on the "PLAY_RECAP" capability.

    **Note**: There are cases where playbooks need to interpret results
    of a task and then determine success or failure and return result
    accordingly (failure for failed tasks).

.. req::
    :id: R-50252
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** write to a response file in JSON format that will be
    retrieved and made available by the Ansible Server if, as part of a xNF
    action (e.g., audit), a playbook is required to return any xNF
    information/response. The text files must be written in the main playbook
    home directory, in JSON format. The JSON file must be created for the xNF
    with the name '<xNF name>_results.txt'. All playbook output results, for
    all xNF VMs, to be provided as a response to the request, must be written
    to this response file. 

.. req::
    :id: R-51442
    :target: XNF
    :keyword: SHOULD
    :updated: casablanca

    The xNF **SHOULD** use playbooks that are designed to
    automatically 'rollback' to the original state in case of any errors
    for actions that change state of the xNF (e.g., configure).

    **Note**: In case rollback at the playbook level is not supported or
    possible, the xNF provider shall provide alternative rollback
    mechanism (e.g., for a small xNF the rollback mechanism may rely
    on workflow to terminate and re-instantiate VNF VMs and then re-run
    playbook(s)). Backing up updated files is also recommended to support
    rollback when soft rollback is feasible.

.. req::
    :id: R-58301
    :target: XNF
    :keyword: SHOULD NOT
    :updated: casablanca

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

.. req::
    :id: R-02651
    :target: XNF
    :keyword: SHOULD
    :updated: casablanca

    The xNF **SHOULD** use available backup capabilities to save a
    copy of configuration files before implementing changes to support
    operations such as backing out of software upgrades, configuration
    changes or other work as this will help backing out of configuration
    changes when needed.

.. req::
    :id: R-43353
    :target: XNF
    :keyword: MUST
    :updated: casablanca

    The xNF **MUST** return control from Ansible Playbooks only after all
    tasks performed by playbook are fully complete, signaling that the
    playbook completed all tasks. When starting services, return control
    only after all services are up. This is critical for workflows where
    the next steps are dependent on prior tasks being fully completed.

Detailed examples:

``StopApplication Playbook`` – StopApplication Playbook shall return control
and a completion status response only after xNF application is fully stopped,
all processes/services stopped.

``StartApplication Playbook`` – StartApplication Playbook shall return control
and a completion status only after all xNF application services are fully up,
all processes/services started and ready to provide services.

**NOTE**: Start Playbook should not be declared complete/done after starting
one or several processes that start the other processes.

HealthCheck Playbook:

SUCCESS – HealthCheck success shall be returned (return code 0) by a
Playbook or Cookbook only when xNF is 100% healthy, ready to take requests
and provide services, with all xNF required capabilities ready to provide
services and with all active and standby resources fully ready with no
open MINOR, MAJOR or CRITICAL alarms.

NOTE: In some cases, a switch may need to be turned on, but a xNF
reported as healthy, should be ready to take service requests or be
already processing service requests successfully.

A successful execution of a health-check playbook shall create one response
file (per xNF) in JSON format, named after the xNF instance, followed by
"_results.txt" (<xNF instance name>_results.txt) to be provided as a response
to the requestor, indicating  health-check was executed and completed
successfully, example: vfdb9904v_results.txt, with the following contents:

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
case xNF is not 100% healthy because one or more xNF application processes
are stopped or not ready to take service requests or because critical or
non-critical resources are not ready or because there are open MINOR, MAJOR
or CRITICAL traps/alarms or because there are issues with the xNF that
need attention even if they do not impact services provided by the xNF.

A failed health-check playbook shall also create one file (per xNF), in
JSON format, named after the xNF instance name, followed by "_results.txt"
to indicate health-check was executed and found issues in the health of
the xNF. This is to differentiate from failure to run health-check playbook
or playbook tasks to verify the health of the xNF,
example: vfdb9904v_results.txt, with the following contents:

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


See `xNF REST APIs`_ for additional details on HealthCheck.

Some xNFs may support and desire to run partial health checks and receive
a successful response when partial health check completes without errors.
The parameter name used by HealthCheck playbook to request non-default
partial health check is healthcheck_type. Example of health check types
could be healthcheck_type=GuestOS, healthcheck_type=noDB,
healthcheck_type=noConnections, healthcheck_type=IgnoreAlarms, etc.. This
attribute-value pair may be passed by Orchestrator or Workflow or other
(northbound) APPC/SDN-C clients to APPC/SDN-C as part of the request.

By default, when no argument/parameter is passed, healthcheck playbook
performs a full xNF health check.

.. req::
    :id: R-24189
    :target: XNF
    :keyword: SHOULD
    :introduced: casablanca

    The xNF provider **MUST** deliver a new set of playbooks that includes
    all updated and unchanged playbooks for any new revision to an existing
    set of playbooks.

.. req::
    :id: R-49911
    :target: XNF
    :keyword: SHOULD
    :updated: casablanca
    :introduced: casablanca

    The xNF provider **MUST** assign a new point release to the updated
    playbook set. The functionality of a new playbook set must be tested before
    it is deployed to the production.


Ansible API Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section outlines the workflow that APPC/SDN-C invokes when
it receives an action request against an Ansible managed xNF.

 #. When APPC/SDN-C receives a request for an action for an
    Ansible managed xNF, it retrieves the corresponding template (based
    on **action** and **xNF Type**) from its database and sets necessary
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
|General      |For each RPC, the   |xNF Vendor must     |VNF Vendor must     |
|Comments     |appropriate RPC     |provide any         |provide an Ansible  |
|             |operation is listed.|necessary roles,    |playbook to retrieve|
|             |                    |cookbooks, recipes  |the running         |
|             |                    |to retrieve the     |configuration from a|
|             |                    |running             |VNF and place the   |
|             |                    |configuration from  |output on the       |
|             |                    |a xNF and place it  |Ansible server in   |
|             |                    |in the respective   |a manner aligned    |
|             |                    |Node Objects        |with playbook       |
|             |                    |'PushJobOutput'     |requirements listed |
|             |                    |attribute of all    |in this document.   |
|             |                    |nodes in NodeList   |                    |
|             |                    |when triggered      |The PlaybookName    |
|             |                    |by a chef-client    |must be provided    |
|             |                    |run.                |in the JSON file.   |
|             |                    |                    |                    |
|             |                    |The JSON file for   |NodeList must list  |
|             |                    |this xNF action is  |IP addresses or DNS |
|             |                    |required to set     |supported FQDNs of  |
|             |                    |"PushJobFlag" to    |an example VNF      |
|             |                    |"True" and          |on which to         |
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
|             |or part of a        |updates the xNF     |updates the VNF     |
|             |specified data set  |configuration.      |configuration.      |
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
   all VMs of a xNF invoked as part of the action except for the "name".

.. [#7.3.3]
   Upstream elements must provide the appropriate FQDN in the request to
   ONAP for the desired action.

.. [#7.3.4]
   Multiple ONAP actions may map to one playbook.


