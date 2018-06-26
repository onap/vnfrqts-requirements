.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

Configuration Management
------------------------

Controller Interactions With VNF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP Controllers (such as APPC) expose a northbound API to clients
(such as SO) in order for the clients to initiate an activity
(aka command) on a VNF.   ONAP controllers interact with VNFs through
Network and Application Adapters to perform configuration and other
lifecycle management activities within NFV environment.
The standardized models, protocols and mechanisms by which network
functions are configured are equally applicable to VNFs and PNFs.

This section describes the list of commands that should be supported
by the VNF.   The following sections describe the standard protocols
that are supported (NETCONF, Chef, Ansible, and REST).

The commands below are expected to be supported on all VNF’s, unless
noted otherwise, either directly (via the NETCONF or REST interface)
or indirectly (via a Chef Cookbook or Ansible server).  Note that there
are additional commands offered to northbound clients that are not shown
below, as these commands either act internally on the Controller itself
or depend upon network cloud components for implementation (thus, these
actions do not put any special requirement on the VNF provider).

The commands allow for parametric data to be passed from the controller
to the VNF or Ansible/Chef server in the request.  The format of the
parameter data can be either xml (for NETCONF) or JSON (for Ansible,
Chef, or REST).

Configuration Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Configure**: The Controller client is requesting that a post-instantiation
configuration be applied to the target VNF instance. After the Configure
action is completed, the VNF instance should be ready for service.
Note that customer specific configurations may need to be applied using
the ConfigModify action.

**ConfigModify**: The Controller client is requesting a configuration
update to a subset of the total configuration parameters of a VNF or to
apply customer specific configurations. The configuration update is
typically done while the VNF is in service and should not disrupt traffic.

**ConfigBackup**: The Controller client is requesting a backup of the
configuration parameters where the parameters are stored on the VNF.
This command is typically requested as part of an orchestration flow
for scenarios such as a software upgrade. The ConfigBackup is typically
done while the VNF is not in service (i.e., in a maintenance state).
When the ConfigBackup command is executed, the current VNF configuration
parameters are saved in storage that is preserved (if there is an existing
set of backed up parameters, they are overwritten).

**ConfigRestore**: The Controller client is requesting a restore action of
the configuration parameters to the VNF that were saved by ConfigBackup
command. This command is typically requested as part of an orchestration
flow for scenarios such as a software upgrade where the software upgrade
may have failed and the VNF needs to be rolled back to the prior configuration.
When the ConfigRestore command is executed, the VNF configuration parameters
which were backed to persistent preserved storage are applied to the VNF
(replacing existing parameters). The ConfigRestore is typically done while
the VNF is not in service (i.e., in a maintenance state).

**ConfigScaleOut**: The Controller client is requesting that a configuration
be applied after the VNF instance has been scaled out (i.e., one or more
additional VM’s instantiated to increase capacity). For some VNF’s,
ConfigScaleOut is not needed because the VNF is auto-configured after
scale-out. This command is being introduced in the Beijing release.

**Audit**: The Controller client is requesting that the current (last known
configuration update) is audited against the running configuration on the VNF.

* R-20741 The xNF **MUST** support ONAP Controller’s **Configure** command.
* R-19366 The xNF **MUST** support ONAP Controller’s **ConfigModify** command.
* R-32981 The xNF **MUST** support ONAP Controller’s **ConfigBackup** command.
* R-48247 The xNF **MUST** support ONAP Controller’s **ConfigRestore** command.
* R-94084 The xNF **MUST** support ONAP Controller’s **ConfigScaleOut**
  command.
* R-56385 The xNF **MUST** support ONAP Controller’s **Audit** command.

LifeCycle Management Related Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**The following commands are needed to support various lifecycle management
flows where the VNF may need to be removed for service.**

**QuiesceTraffic**: The Controller client is requesting the VNF gracefully
stop traffic (aka block and drain traffic). The method for quiescing traffic
is specific to the VNF architecture. The action is completed when all
(in-flight transactions) traffic has stopped.   The VNF remains in an active
state where the VNF is able to process traffic (initiated using the
StartTraffic action).

**ResumeTraffic**: The Controller client is requesting the VNF resume
processing traffic. The method to resume traffic is specific to the VNF
architecture.

**StopApplication**: The Controller client is requesting that the application
running on the VNF is stopped gracefully (i.e., without traffic loss).
This is equivalent to quiescing the traffic and then stopping the application
processes. The processes can be restarted using the StartApplication command.

**StartApplication**: The Controller client is requesting that the application
running on the VNF is started. Get ready to process traffic.

**The following commands are needed to support software upgrades, in-place or
other type of software upgrade. The VNF instance may be removed from service
for the upgrade.**

**UpgradePrecheck**: The Controller client is requesting a confirmation that
the VNF can (and needs to) be upgraded to a specific software version
(specified in the request).

**UpgradeSoftware**: The Controller client is requesting that a (in-place)
software upgrade be performed on the VNF.  The software to be applied is
pre-loaded to a specified location.

**UpgradePostCheck**: The Controller client is requesting a confirmation that
the VNF software upgrade has been completed successfully (VNF upgraded to
the new software version).

**UpgradeBackup**: The Controller client is requesting that the VNF is backed
up prior to the UpgradeSoftware.

**UpgradeBackOut**: The Controller client is requesting that the VNF upgrade
is backed out (in the event that the SoftwareUpgrade or UpgradePostCheck
failed).

* R-12706 The xNF **MUST** support ONAP Controller’s **QuiesceTraffic**
  command.
* R-07251 The xNF **MUST** support ONAP Controller’s **ResumeTraffic**
  command.
* R-83146 The xNF **MUST** support ONAP Controller’s **StopApplication**
  command.
* R-82811 The xNF **MUST** support ONAP Controller’s **StartApplication**
  command.
* R-19922 The xNF **MUST** support ONAP Controller’s **UpgradePrecheck**
  command.
* R-49466 The xNF **MUST** support ONAP Controller’s **UpgradeSoftware**
  command.
* R-45856 The xNF **MUST** support ONAP Controller’s **UpgradePostCheck**
  command.
* R-97343 The xNF **MUST** support ONAP Controller’s **UpgradeBackup**
  command.
* R-65641 The xNF **MUST** support ONAP Controller’s **UpgradeBackOut**
  command.

Virtual Function - Container Recovery Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As part of life cycle management, for Cloud environment, VNFs need to
support a set of basic recovery capabilities to maintain the health
and extend the life of the VNF, eliminating and reducing the frequency
that an entire VNF needs to be rebuilt or re-instantiated to recover one
or more of its containers. For instance, a VNF in an Openstack environment
is composed of one or more containers called VMs (Virtual Machines). During
the life of a VNF it is expected that Cloud infrastructure hardware will
fail or they would need to be taken down for maintenance or hardware and
software upgrades (e.g. firmware upgrades, HostOS (Hypervisor), power
maintenance, power outages, etc.) To deal with such life cycle events
without having to rebuild entire VNFs or even entire sites these basic
recovery capabilities of individual containers, Virtual Machines or other,
must be supported.

* R-11790 The VNF **MUST** support ONAP Controller’s
  **Restart (stop/start or reboot)** command.
* R-56218 The VNF **MUST** support ONAP Controller’s Migrate command that
  moves container (VM) from a live Physical Server / Compute Node to
  another live Physical Server / Compute Node.

NOTE: Container migrations MUST be transparent to the VNF and no more
intrusive than a stop, followed by some down time for the migration to
be performed from one Compute Node / Physical Server to another, followed
by a start of the same VM with same configuration on the new Compute
Node / Physical Server.

* R-38001 The VNF MUST support ONAP Controller’s **Rebuild** command.
* R-76901 VNF MUST support a container rebuild mechanism based on existing
  image (e.g. Glance image in Openstack environment) or a snapshot.

HealthCheck and Failure Related Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**HealthCheck**: The Controller client is requesting a health check over the
entire scope of the VNF.  The VNF must be 100% healthy, ready to take requests
and provide services, with all VNF required capabilities ready to provide
services and with all active and standby resources fully ready with no open
MINOR, MAJOR or CRITICAL alarms.

Note: In addition to the commands above, the Controller supports a set of
Openstack failure recovery related commands that are executed on-demand or via
Control Loop at the VM level.  The VNF must support these commands in a fully
automated fashion.

* R-41430 The xNF **MUST** support ONAP Controller’s **HealthCheck**
  command.

Notes On Command Support Using Controller Southbound Protocols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ONAP Controllers are designed to support a standard set of protocols in
order to communicate with the VNF instance.  The supported protocols are
NETCONF, Ansible, Chef, and REST.

NETCONF and REST require the VNF to implement a server which supports the RPC
or REST calls.

Ansible and Chef require the use of a Ansible or Chef server which communicates
with the Controller (northbound) and the VNF VM’s (southbound).

The vendor must select which protocol to support for the commands listed above.
Notes:

* NETCONF is most suitable for configuration related commands

* Ansible and Chef are suitable for any command.
  Ansible has the advantage that it is agentless.

* REST is specified as an option only for the HealthCheck.


Additional details can be found in the `ONAP Application Controller (APPC) API Guide <http://onap.readthedocs.io/en/latest/submodules/appc.git/docs/APPC%20API%20Guide/APPC%20API%20Guide.html>`_, `ONAP VF-C project <http://onap.readthedocs.io/en/latest/submodules/vfc/nfvo/lcm.git/docs/index.html>`_ and the `ONAP SDNC project <http://onap.readthedocs.io/en/latest/submodules/sdnc/northbound.git/docs/index.html>`_.

NETCONF Standards and Capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP Controllers and their Adapters utilize device YANG model and
NETCONF APIs to make the required changes in the VNF state and
configuration. The VNF providers must provide the Device YANG model and
NETCONF server supporting NETCONF APIs to comply with target ONAP and
industry standards.

VNF Configuration via NETCONF Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration Management
+++++++++++++++++++++++++++

* R-88026 The xNF **MUST** include a NETCONF server enabling
  runtime configuration and lifecycle management capabilities.
* R-95950 The xNF **MUST** provide a NETCONF interface fully defined
  by supplied YANG models for the embedded NETCONF server.

NETCONF Server Requirements
++++++++++++++++++++++++++++++

* R-73468 The xNF **MUST** allow the NETCONF server connection
  parameters to be configurable during virtual machine instantiation
  through Heat templates where SSH keys, usernames, passwords, SSH
  service and SSH port numbers are Heat template parameters.
* R-90007 The xNF **MUST** implement the protocol operation:
  **close-session()**- Gracefully close the current session.
* R-70496 The xNF **MUST** implement the protocol operation:
  **commit(confirmed, confirm-timeout)** - Commit candidate
  configuration datastore to the running configuration.
* R-18733 The xNF **MUST** implement the protocol operation:
  **discard-changes()** - Revert the candidate configuration
  datastore to the running configuration.
* R-44281 The xNF **MUST** implement the protocol operation:
  **edit-config(target, default-operation, test-option, error-option,
  config)** - Edit the target configuration datastore by merging,
  replacing, creating, or deleting new config elements.
* R-60106 The xNF **MUST** implement the protocol operation:
  **get(filter)** - Retrieve (a filtered subset of) the running
  configuration and device state information. This should include
  the list of xNF supported schemas.
* R-29488 The xNF **MUST** implement the protocol operation:
  **get-config(source, filter)** - Retrieve a (filtered subset of
  a) configuration from the configuration datastore source.
* R-11235 The xNF **MUST** implement the protocol operation:
  **kill-session(session)** - Force the termination of **session**.
* R-02597 The xNF **MUST** implement the protocol operation:
  **lock(target)** - Lock the configuration datastore target.
* R-96554 The xNF **MUST** implement the protocol operation:
  **unlock(target)** - Unlock the configuration datastore target.
* R-29324 The xNF **SHOULD** implement the protocol operation:
  **copy-config(target, source) -** Copy the content of the
  configuration datastore source to the configuration datastore target.
* R-88031 The xNF **SHOULD** implement the protocol operation:
  **delete-config(target) -** Delete the named configuration
  datastore target.
* R-97529 The xNF **SHOULD** implement the protocol operation:
  **get-schema(identifier, version, format) -** Retrieve the YANG schema.
* R-62468 The xNF **MUST** allow all configuration data to be
  edited through a NETCONF <edit-config> operation. Proprietary
  NETCONF RPCs that make configuration changes are not sufficient.
* R-01382 The xNF **MUST** allow the entire configuration of the
  xNF to be retrieved via NETCONF's <get-config> and <edit-config>,
  independently of whether it was configured via NETCONF or other
  mechanisms.
* R-28756 The xNF **MUST** support **:partial-lock** and
  **:partial-unlock** capabilities, defined in RFC 5717. This
  allows multiple independent clients to each write to a different
  part of the <running> configuration at the same time.
* R-83873 The xNF **MUST** support **:rollback-on-error** value for
  the <error-option> parameter to the <edit-config> operation. If any
  error occurs during the requested edit operation, then the target
  database (usually the running configuration) will be left unaffected.
  This provides an 'all-or-nothing' edit mode for a single <edit-config>
  request.
* R-68990 The xNF **MUST** support the **:startup** capability. It
  will allow the running configuration to be copied to this special
  database. It can also be locked and unlocked.
* R-68200 The xNF **MUST** support the **:url** value to specify
  protocol operation source and target parameters. The capability URI
  for this feature will indicate which schemes (e.g., file, https, sftp)
  that the server supports within a particular URL value. The 'file'
  scheme allows for editable local configuration databases. The other
  schemes allow for remote storage of configuration databases.
* R-20353 The xNF **MUST** implement both **:candidate** and
  **:writable-running** capabilities. When both **:candidate** and
  **:writable-running** are provided then two locks should be supported.
* R-11499 The xNF **MUST** fully support the XPath 1.0 specification
  for filtered retrieval of configuration and other database contents.
  The 'type' attribute within the <filter> parameter for <get> and
  <get-config> operations may be set to 'xpath'. The 'select' attribute
  (which contains the XPath expression) will also be supported by the
  server. A server may support partial XPath retrieval filtering, but
  it cannot advertise the **:xpath** capability unless the entire XPath
  1.0 specification is supported.
* R-83790 The xNF **MUST** implement the **:validate** capability
* R-49145 The xNF **MUST** implement **:confirmed-commit** If
  **:candidate** is supported.
* R-58358 The xNF **MUST** implement the **:with-defaults** capability
  [RFC6243].
* R-59610 The xNF **MUST** implement the data model discovery and
  download as defined in [RFC6022].
* R-93443 The xNF **MUST** define all data models in YANG [RFC6020],
  and the mapping to NETCONF shall follow the rules defined in this RFC.
* R-26115 The xNF **MUST** follow the data model upgrade rules defined
  in [RFC6020] section 10. All deviations from section 10 rules shall
  be handled by a built-in automatic upgrade mechanism.
* R-10716 The xNF **MUST** support parallel and simultaneous
  configuration of separate objects within itself.
* R-29495 The xNF **MUST** support locking if a common object is
  being manipulated by two simultaneous NETCONF configuration operations
  on the same xNF within the context of the same writable running data
  store (e.g., if an interface parameter is being configured then it
  should be locked out for configuration by a simultaneous configuration
  operation on that same interface parameter).
* R-53015 The xNF **MUST** apply locking based on the sequence of
  NETCONF operations, with the first configuration operation locking
  out all others until completed.
* R-02616 The xNF **MUST** permit locking at the finest granularity
  if a xNF needs to lock an object for configuration to avoid blocking
  simultaneous configuration operations on unrelated objects (e.g., BGP
  configuration should not be locked out if an interface is being
  configured or entire Interface configuration should not be locked out
  if a non-overlapping parameter on the interface is being configured).
* R-41829 The xNF **MUST** be able to specify the granularity of the
  lock via a restricted or full XPath expression.
* R-66793 The xNF **MUST** guarantee the xNF configuration integrity
  for all simultaneous configuration operations (e.g., if a change is
  attempted to the BUM filter rate from multiple interfaces on the same
  EVC, then they need to be sequenced in the xNF without locking either
  configuration method out).
* R-54190 The xNF **MUST** release locks to prevent permanent lock-outs
  when/if a session applying the lock is terminated (e.g., SSH session
  is terminated).
* R-03465 The xNF **MUST** release locks to prevent permanent lock-outs
  when the corresponding <partial-unlock> operation succeeds.
* R-63935 The xNF **MUST** release locks to prevent permanent lock-outs
  when a user configured timer has expired forcing the NETCONF SSH Session
  termination (i.e., product must expose a configuration knob for a user
  setting of a lock expiration timer)
* R-10173 The xNF **MUST** allow another NETCONF session to be able to
  initiate the release of the lock by killing the session owning the lock,
  using the <kill-session> operation to guard against hung NETCONF sessions.
* R-88899 The xNF **MUST** support simultaneous <commit> operations
  within the context of this locking requirements framework.
* R-07545 The xNF **MUST** support all operations, administration and
  management (OAM) functions available from the supplier for xNFs using
  the supplied YANG code and associated NETCONF servers.
* R-60656 The xNF **MUST** support sub tree filtering.
* R-80898 The xNF **MUST** support heartbeat via a <get> with null filter.
* R-25238 The xNF PACKAGE **MUST** validated YANG code using the open
  source pyang [1]_ program using the following commands:

.. code-block:: python

 $ pyang --verbose --strict <YANG-file-name(s)>
 $ echo $!

* R-63953 The xNF **MUST** have the echo command return a zero value
  otherwise the validation has failed
* R-26508 The xNF **MUST** support a NETCONF server that can be mounted on
  OpenDaylight (client) and perform the operations of: modify, update,
  change, rollback configurations using each configuration data element,
  query each state (non-configuration) data element, execute each YANG
  RPC, and receive data through each notification statement.


The following requirements provides the Yang models that suppliers must
conform, and those where applicable, that suppliers need to use.

* R-28545 The xNF **MUST** conform its YANG model to RFC 6060,
  “YANG - A Data Modeling Language for the Network Configuration
  Protocol (NETCONF)”
* R-22700 The xNF **MUST** conform its YANG model to RFC 6470,
  “NETCONF Base Notifications”.
* R-10353 The xNF **MUST** conform its YANG model to RFC 6244,
  “An Architecture for Network Management Using NETCONF and YANG”.
* R-53317 The xNF **MUST** conform its YANG model to RFC 6087,
  “Guidelines for Authors and Reviewers of YANG Data Model Documents”.
* R-33955 The xNF **SHOULD** conform its YANG model to RFC 6991,
  “Common YANG Data Types”.
* R-22946 The xNF **SHOULD** conform its YANG model to RFC 6536,
  “NETCONF Access Control Model”.
* R-10129 The xNF **SHOULD** conform its YANG model to RFC 7223,
  “A YANG Data Model for Interface Management”.
* R-12271 The xNF **SHOULD** conform its YANG model to RFC 7223,
  “IANA Interface Type YANG Module”.
* R-49036 The xNF **SHOULD** conform its YANG model to RFC 7277,
  “A YANG Data Model for IP Management”.
* R-87564 The xNF **SHOULD** conform its YANG model to RFC 7317,
  “A YANG Data Model for System Management”.
* R-24269 The xNF **SHOULD** conform its YANG model to RFC 7407,
  “A YANG Data Model for SNMP Configuration”, if Netconf used to
  configure SNMP engine.

The NETCONF server interface shall fully conform to the following
NETCONF RFCs.

* R-33946 The xNF **MUST** conform to the NETCONF RFC 4741,
  “NETCONF Configuration Protocol”.
* R-04158 The xNF **MUST** conform to the NETCONF RFC 4742,
  “Using the NETCONF Configuration Protocol over Secure Shell (SSH)”.
* R-13800 The xNF **MUST** conform to the NETCONF RFC 5277,
  “NETCONF Event Notification”.
* R-01334 The xNF **MUST** conform to the NETCONF RFC 5717,
  “Partial Lock Remote Procedure Call”.
* R-08134 The xNF **MUST** conform to the NETCONF RFC 6241,
  “NETCONF Configuration Protocol”.
* R-78282 The xNF **MUST** conform to the NETCONF RFC 6242,
  “Using the Network Configuration Protocol over Secure Shell”.

VNF REST APIs
^^^^^^^^^^^^^^^

HealthCheck is a command for which no NETCONF support exists.
Therefore, this must be supported using a RESTful interface
(defined in this section) or with a Chef cookbook/Ansible playbook
(defined in sections `Chef Standards and Capabilities`_ and
`Ansible Standards and Capabilities`_).

HealthCheck Definition: The VNF level HealthCheck is a check over
the entire scope of the VNF. The VNF must be 100% healthy, ready
to take requests and provide services, with all VNF required
capabilities ready to provide services and with all active and
standby resources fully ready with no open MINOR, MAJOR or CRITICAL
alarms.  NOTE: A switch may need to be turned on, but the VNF should
be ready to take service requests or be already processing service
requests successfully.

The VNF must provide a REST formatted GET RPCs to support HealthCheck
queries via the GET method over HTTP(s).

The port number, url, and other authentication information is provided
by the VNF provider.

REST APIs
~~~~~~~~~

* R-31809 The xNF **MUST** support the HealthCheck RPC. The HealthCheck
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

ONAP will support configuration of VNFs via Chef subject to the
requirements and guidelines defined in this section.

The Chef configuration management mechanism follows a client-server
model. It requires the presence of a Chef-Client on the VNF that will be
directly managed by a Chef Server. The Chef-client will register with
the appropriate Chef Server and are managed via ‘cookbooks’ and
configuration attributes loaded on the Chef Server which contain all
necessary information to execute the appropriate actions on the VNF via
the Chef-client.

ONAP will utilize the open source Chef Server, invoke the documented
Chef REST APIs to manage the VNF and requires the use of open source
Chef-Client and Push Jobs Client on the VNF
(https://downloads.chef.io/).

VNF Configuration via Chef Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chef Client Requirements
+++++++++++++++++++++++++

* R-79224 The xNF **MUST** have the chef-client be preloaded with
  validator keys and configuration to register with the designated
  Chef Server as part of the installation process.
* R-72184 The xNF **MUST** have routable FQDNs for all the endpoints
  (VMs) of a xNF that contain chef-clients which are used to register
  with the Chef Server.  As part of invoking xNF actions, ONAP will
  trigger push jobs against FQDNs of endpoints for a xNF, if required.
* R-47068 The xNF **MAY** expose a single endpoint that is
  responsible for all functionality.
* R-67114 The xNF **MUST** be installed with Chef-Client >= 12.0 and
  Chef push jobs client >= 2.0.

Chef Roles/Requirements
++++++++++++++++++++++++++

* R-27310 The xNF Package **MUST** include all relevant Chef artifacts
  (roles/cookbooks/recipes) required to execute xNF actions requested by
  ONAP for loading on appropriate Chef Server.
* R-26567 The xNF Package **MUST** include a run list of
  roles/cookbooks/recipes, for each supported xNF action, that will
  perform the desired xNF action in its entirety as specified by ONAP
  (see Section 7.c, ONAP Controller APIs and Behavior, for list of xNF
  actions and requirements), when triggered by a chef-client run list
  in JSON file.
* R-98911 The xNF **MUST NOT** use any instance specific parameters
  for the xNF in roles/cookbooks/recipes invoked for a xNF action.
* R-37929 The xNF **MUST** accept all necessary instance specific
  data from the environment or node object attributes for the xNF
  in roles/cookbooks/recipes invoked for a xNF action.
* R-62170 The xNF **MUST** over-ride any default values for
  configurable parameters that can be set by ONAP in the roles,
  cookbooks and recipes.
* R-78116 The xNF **MUST** update status on the Chef Server
  appropriately (e.g., via a fail or raise an exception) if the
  chef-client run encounters any critical errors/failures when
  executing a xNF action.
* R-44013 The xNF **MUST** populate an attribute, defined as node
  [‘PushJobOutput’] with the desired output on all nodes in the push job
  that execute chef-client run if the xNF action requires the output of a
  chef-client run be made available (e.g., get running configuration).
* R-30654 The xNF Package **MUST** have appropriate cookbooks that are
  designed to automatically ‘rollback’ to the original state in case of
  any errors for actions that change state of the xNF (e.g., configure).
* R-65755 The xNF **SHOULD** support callback URLs to return information
  to ONAP upon completion of the chef-client run for any chef-client run
  associated with a xNF action.

-  As part of the push job, ONAP will provide two parameters in the
   environment of the push job JSON object:

    -  ‘RequestId’ a unique Id to be used to identify the request,
    -  ‘CallbackUrl’, the URL to post response back.

-  If the CallbackUrl field is empty or missing in the push job, then
   the chef-client run need not post the results back via callback.

* R-15885 The xNF **MUST** Upon completion of the chef-client run,
  POST back on the callback URL, a JSON object as described in Table
  A2 if the chef-client run list includes a cookbook/recipe that is
  callback capable. Failure to POST on the Callback Url should not be
  considered a critical error. That is, if the chef-client successfully
  completes the xNF action, it should reflect this status on the Chef
  Server regardless of whether the Callback succeeded or not.

ONAP Chef API Usage
~~~~~~~~~~~~~~~~~~~

This section outlines the workflow that ONAP invokes when it receives an
action request against a Chef managed VNF.

1. When ONAP receives a request for an action for a Chef Managed VNF, it
   retrieves the corresponding template (based on **action** and
   **VNF)** from its database and sets necessary values in the
   “Environment”, “Node” and “NodeList” keys (if present) from either
   the payload of the received action or internal data.

2. If “Environment” key is present in the updated template, it posts the
   corresponding JSON dictionary to the appropriate Environment object
   REST endpoint on the Chef Server thus updating the Environment
   attributes on the Chef Server.

3. Next, it creates a Node Object from the “Node” JSON dictionary for
   all elements listed in the NodeList (using the FQDN to construct the
   endpoint) by replicating it  [2]_. As part of this process, it will
   set the name field in each Node Object to the corresponding FQDN.
   These node objects are then posted on the Chef Server to
   corresponding Node Object REST endpoints to update the corresponding
   node attributes.

4. If PushJobFlag is set to “True” in the template, ONAP requests a push
   job against all the nodes in the NodeList to trigger
   chef-client\ **.** It will not invoke any other command via the push
   job. ONAP will include a callback URL in the push job request and a
   unique Request Id. An example push job posted by ONAP is listed
   below:

.. code-block:: java

   {
     "command": "chef-client",
     "run\_timeout": 300,
     "nodes”: [“node1.vnf\_a.onap.com”, “node2.vnf\_a.onap.com”],
       "env": {
                “RequestId”:”8279-abcd-aksdj-19231”,
                “CallbackUrl”:”<callback>”
              },
   }

5. If CallbackCapable field in the template is not present or set to
   “False” ONAP will poll the Chef Server to check completion status of
   the push job.

6. If “GetOutputFlag” is set to “True” in the template and
   CallbackCapable is not set to “True”, ONAP will retrieve any output
   from each node where the push job has finished by accessing the Node
   Object attribute node[‘PushJobOutput’].

Ansible Standards and Capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP will support configuration of VNFs via Ansible subject to the
requirements and guidelines defined in this section.

Ansible allows agentless management of VNFs/VMs/VNFCs via execution
of ‘playbooks’ over ssh. The ‘playbooks’ are a structured set of
tasks which contain all the necessary resources and execution capabilities
to take the necessary action on one or more target VMs (and/or VNFCs)
of the VNF. ONAP will utilize the framework of an Ansible Server that
will host all Ansible artifacts and run playbooks to manage VNFs that support
Ansible.

VNF Configuration via Ansible Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ansible Client Requirements
+++++++++++++++++++++++++++++

* R-32217 The xNF **MUST** have routable FQDNs that are reachable via
  the Ansible Server for the endpoints (VMs) of a xNF on which playbooks
  will be executed. ONAP will initiate requests to the Ansible Server
  for invocation of playbooks against these end points [3]_.
* R-54373 The xNF **MUST** have Python >= 2.6 on the endpoint VM(s)
  of a xNF on which an Ansible playbook will be executed.
* R-35401 The xNF **MUST** support SSH and allow SSH access by the
  Ansible server for the endpoint VM(s) and comply with the Network
  Cloud Service Provider guidelines for authentication and access.
* R-82018 The xNF **MUST** load the Ansible Server SSH public key onto xNF
  VM(s) as part
  of instantiation. This will allow the Ansible Server to authenticate
  to perform post-instantiation configuration without manual intervention
  and without requiring specific xNF login IDs and passwords.

 CAUTION: For VNFs configured using Ansible, to eliminate the need
 for manual steps, post-instantiation and pre-configuration, to upload
 of SSH public keys, SSH public keys loaded during (heat) instantiation shall
 be preserved and not removed by (heat) embedded (userdata) scripts.

* R-92866 The xNF **MUST** include as part of post-instantiation configuration
  done by Ansible Playbooks the removal/update of the SSH public key from
  /root/.ssh/authorized_keys, and  update of SSH keys loaded through
  instantiation to support Ansible. This may include download and install of
  new SSH keys and new mechanized IDs.
* R-91745 The xNF **MUST** update the Ansible Server and other entities
  storing and using the SSH keys for authentication when the SSH keys used
  by Ansible are regenerated/updated.

  NOTE: Ansible Server itself may be used to upload new SSH public keys
  onto supported VNFs.

Ansible Playbook Requirements
+++++++++++++++++++++++++++++++

An Ansible playbook is a collection of tasks that is executed on the
Ansible server (local host) and/or the target VM (s) in order to
complete the desired action.

* R-40293 The xNF **MUST** make available playbooks that conform
  to the ONAP requirement.
* R-49396 The xNF **MUST** support each ONAP (APPC) xNF action
  by invocation of **one** playbook [4]_. The playbook will be responsible
  for executing
  all necessary tasks (as well as calling other playbooks) to complete
  the request.
* R-33280 The xNF **MUST NOT** use any instance specific parameters
  in a playbook.
* R-48698 The xNF **MUST** utilize information from key value pairs
  that will be provided by the Ansible Server as "extra-vars" during
  invocation to execute the desired xNF action. If the playbook requires
  files, they must also be supplied using the methodology detailed in
  the Ansible Server API, unless they are bundled with playbooks, example,
  generic templates.

The Ansible Server will determine if a playbook invoked to execute a
xNF action finished successfully or not using the “PLAY_RECAP” summary
in Ansible log.  The playbook will be considered to successfully finish
only if the “PLAY RECAP” section at the end of playbook execution output
has no unreachable hosts and no failed tasks. Otherwise, the playbook
will be considered to have failed.

* R-43253 The xNF **MUST** use playbooks designed to allow Ansible
  Server to infer failure or success based on the “PLAY_RECAP” capability.
  NOTE: There are cases where playbooks need to interpret results of a task
  and then determine success or failure and return result accordingly
  (failure for failed tasks).
* R-50252 The xNF **MUST** write to a specific one text files that
  will be retrieved and made available by the Ansible Server if, as part
  of a xNF action (e.g., audit), a playbook is required to return any
  xNF information. The text files must be written in the same directory as
  the one from which the playbook is being executed. A text file must be
  created for the xNF playbook run targets/affects, with the name
  ‘<VNFname>_results.txt’ into which any desired output from each
  respective VM/xNF must be written.
* R-51442 The xNF **SHOULD** use playbooks that are designed to
  automatically ‘rollback’ to the original state in case of any errors
  for actions that change state of the xNF (e.g., configure).

 NOTE: In case rollback at the playbook level is not supported or possible,
 the xNF provider shall provide alternative locking mechanism (e.g., for a
 small xNF the rollback mechanism may rely on workflow to terminate and
 re-instantiate VNF VMs and then re-run playbook(s)). Backing up updated
 files also recommended to support rollback when soft rollback is feasible.

* R-58301 The xNF **SHOULD NOT** use playbooks that make requests to
  Cloud resources e.g. Openstack (nova, neutron, glance, heat, etc.);
  therefore, there is no use for Cloud specific variables like Openstack
  UUIDs in Ansible Playbooks.

 Rationale: Flows that require interactions with Cloud services
 e.g. Openstack shall rely on workflows run by an Orchestrator
 (Change Management) or
 other capability (such as a control loop or Operations GUI) outside
 Ansible Server which can be executed by a Controller such as APPC.
 There are policies, as part of Control Loop models, that send remediation
 action requests to APPC; these are triggered as a response to an event
 or correlated events published to Event Bus.

* R-02651 The xNF **SHOULD** use the Ansible backup feature to save a
  copy of configuration files before implementing changes to support
  operations such as backing out of software upgrades, configuration
  changes or other work as this will help backing out of configuration
  changes when needed.
* R-43353 The xNF **MUST** return control from Ansible Playbooks only
  after tasks are fully complete, signaling that the playbook completed
  all tasks. When starting services, return control only after all services
  are up. This is critical for workflows where the next steps are dependent
  on prior tasks being fully completed.

 Detailed examples:

 StopApplication Playbook – StopApplication Playbook shall return control
 and a completion status only after VNF application is fully stopped, all
 processes/services stopped.
 StartApplication Playbook – StartApplication Playbook shall return control
 and a completion status only after all VNF application services are fully up,
 all processes/services started and ready to provide services. NOTE: Start
 Playbook should not be declared complete/done after starting one or several
 processes that start the other processes.

 HealthCheck Playbook:

 SUCCESS – HealthCheck success shall be returned (return code 0) by a
 Playbook or Cookbook only when VNF is 100% healthy, ready to take requests
 and provide services, with all VNF required capabilities ready to provide
 services and with all active and standby resources fully ready with no
 open MINOR, MAJOR or CRITICAL alarms.

 NOTE: In some cases, a switch may need to be turned on, but a VNF
 reported as healthy, should be ready to take service requests or be
 already processing service requests successfully.

 A successful execution of a health-check playbook shall also create one
 file per VNF VM, named after the VNF instance name followed by
 “_results.txt (<vnf_instance>_results.txt) to indicate health-check was
 executed and completed successfully, example: vfdb9904v_results.txt,
 with the following contents:

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
..

 FAILURE – A health check playbook shall return a non-zero return code in
 case VNF is not 100% healthy because one or more VNF application processes
 are stopped or not ready to take service requests or because critical or
 non-critical resources are not ready or because there are open MINOR, MAJOR
 or CRITICAL traps/alarms or because there are issues with the VNF that
 need attention even if they do not impact services provided by the VNF.

 A failed health-check playbook shall also create one file per VNF,
 named after the VNF instance name, followed by
 “_results.txt to indicate health-check was executed and found issues
 in the health of the VNF. This is to differentiate from failure to
 run health-check playbook or playbook tasks to verify the health of the VNF,
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
..

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
..

 See `VNF REST APIs`_ for additional details on HealthCheck.

ONAP Controller / Ansible API Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section outlines the workflow that ONAP Controller invokes when
it receives an action request against an Ansible managed VNF.

 #. When ONAP Controller receives a request for an action for an
    AnsibleManaged VNF, it retrieves the corresponding template (based
    on **action** and **VNF**) from its database and sets necessary
    values (such as an Id, NodeList, and EnvParameters) from either
    information in the request or data obtained from other sources.
    This is referred to as the payload that is sent as a JSON object
    to the Ansible server.
 #. The ONAP Controller sends a request to the Ansible server to
    execute the action.
 #. The ONAP Controller polls the Ansible Server for result (success
    or failure).  The ONAP Controllers has a timeout value which is
    contained in the template.   If the result is not available when the
    timeout is reached, the ONAP Controller stops polling and returns a
    timeout error to the requester.   The Ansible Server continues to
    process the request.


Support of Controller Commands And Southbound Protocols
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table summarizes the commands and possible protocols selected.
Note that the HealthCheck can also be supported via REST.

Table 8. ONAP Controller APIs and NETCONF Commands

+-------------+--------------------+--------------------+--------------------+
|**Command**  |**NETCONF Support** |**Chef Support**    |**Ansible**         |
+=============+====================+====================+====================+
|General      |For each RPC, the   |VNF Vendor must     |VNF Vendor must     |
|Comments     |appropriate RPC     |provide any         |provide an Ansible  |
|             |operation is listed.|necessary roles,    |playbook to retrieve|
|             |                    |cookbooks, recipes  |the running         |
|             |                    |to retrieve the     |configuration from a|
|             |                    |running             |VNF and place the   |
|             |                    |configuration from  |output on the       |
|             |                    |a VNF and place it  |Ansible server in   |
|             |                    |in the respective   |a manner aligned    |
|             |                    |Node Objects        |with playbook       |
|             |                    |‘PushJobOutput’     |requirements listed |
|             |                    |attribute of all    |in this document.   |
|             |                    |nodes in NodeList   |                    |
|             |                    |when triggered      |The PlaybookName    |
|             |                    |by a chef-client    |must be provided    |
|             |                    |run.                |in the JSON file.   |
|             |                    |                    |                    |
|             |                    |The JSON file for   |NodeList must list  |
|             |                    |this VNF action is  |IP addresses or DNS |
|             |                    |required to set     |supported FQDNs of  |
|             |                    |“PushJobFlag” to    |an example VNF      |
|             |                    |“True” and          |on which to         |
|             |                    |“GetOutputFlag” to  |execute playbook.   |
|             |                    |“True”. The “Node”  |                    |
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
|             |or part of a        |updates the VNF     |updates the VNF     |
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

.. [1]
   https://github.com/mbj4668/pyang

.. [2]
   Recall that the Node Object **is required** to be identical across
   all VMs of a VNF invoked as part of the action except for the “name”.

.. [3]
   Upstream elements must provide the appropriate FQDN in the request to
   ONAP for the desired action.

.. [4]
   Multiple ONAP actions may map to one playbook.

.. |image0| image:: Data_Model_For_Event_Records.png
      :width: 7in
      :height: 8in

.. |image1| image:: VES_JSON_Driven_Model.png
      :width: 5in
      :height: 3in

.. |image2| image:: YANG_Driven_Model.png
      :width: 5in
      :height: 3in

.. |image3| image:: Protocol_Buffers_Driven_Model.png
      :width: 4.74in
      :height: 3.3in

