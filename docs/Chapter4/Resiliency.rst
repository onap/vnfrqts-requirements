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


VNF Resiliency
-------------------------

The VNF is responsible for meeting its resiliency goals and must factor
in expected availability of the targeted virtualization environment.
This is likely to be much lower than found in a traditional data center.
Resiliency is defined as the ability of the VNF to respond to error
conditions and continue to provide the service intended. A number of
software resiliency dimensions have been identified as areas that should
be addressed to increase resiliency. As VNFs are deployed into the
Network Cloud, resiliency must be designed into the VNF software to
provide high availability versus relying on the Network Cloud to achieve
that end.

Section 4.2 Resiliency in *VNF Guidelines* describes
the overall guidelines for designing VNFs to meet resiliency goals.
Below are more detailed resiliency requirements for VNFs.

All Layer Redundancy
^^^^^^^^^^^^^^^^^^^^^^

Design the VNF to be resilient to the failures of the underlying
virtualized infrastructure (Network Cloud). VNF design considerations
would include techniques such as multiple vLANs, multiple local and
geographic instances, multiple local and geographic data replication,
and virtualized services such as Load Balancers.

All Layer Redundancy Requirements


.. req::
    :id: R-52499
    :target: VNF
    :keyword: MUST

    The VNF **MUST** meet their own resiliency goals and not rely
    on the Network Cloud.

.. req::
    :id: R-42207
    :target: VNF
    :keyword: MUST

    The VNF **MUST** design resiliency into a VNF such that the
    resiliency deployment model (e.g., active-active) can be chosen at
    run-time.

.. req::
    :id: R-03954
    :target: VNF
    :keyword: MUST

    The VNF **MUST** survive any single points of failure within
    the Network Cloud (e.g., virtual NIC, VM, disk failure).

.. req::
    :id: R-89010
    :target: VNF
    :keyword: MUST

    The VNF **MUST** survive any single points of software failure
    internal to the VNF (e.g., in memory structures, JMS message queues).

.. req::
    :id: R-67709
    :target: VNF
    :keyword: MUST

    The VNF **MUST** be designed, built and packaged to enable
    deployment across multiple fault zones (e.g., VNFCs deployed in
    different servers, racks, OpenStack regions, geographies) so that
    in the event of a planned/unplanned downtime of a fault zone, the
    overall operation/throughput of the VNF is maintained.

.. req::
    :id: R-35291
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support the ability to failover a VNFC
    automatically to other geographically redundant sites if not
    deployed active-active to increase the overall resiliency of the VNF.

.. req::
    :id: R-36843
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support the ability of the VNFC to be deployable
    in multi-zoned cloud sites to allow for site support in the event of cloud
    zone failure or upgrades.

.. req::
    :id: R-00098
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** impact the ability of the VNF to provide
    service/function due to a single container restart.

.. req::
    :id: R-79952
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** support container snapshots if not for rebuild
    and evacuate for rollback or back out mechanism.

Minimize Cross Data-Center Traffic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Avoid performance-sapping data center-to-data center replication delay
by applying techniques such as caching and persistent transaction paths
- Eliminate replication delay impact between data centers by using a
concept of stickiness (i.e., once a client is routed to data center "A",
the client will stay with Data center "A" until the entire session is
completed).

Minimize Cross Data-Center Traffic Requirements


.. req::
    :id: R-92935
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** minimize the propagation of state information
    across multiple data centers to avoid cross data center traffic.

Application Resilient Error Handling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ensure an application communicating with a downstream peer is equipped
to intelligently handle all error conditions. Make sure code can handle
exceptions seamlessly - implement smart retry logic and implement
multi-point entry (multiple data centers) for back-end system
applications.

Application Resilient Error Handling Requirements


.. req::
    :id: R-26371
    :target: VNF
    :keyword: MUST

    The VNF **MUST** detect communication failure for inter VNFC
    instance and intra/inter VNF and re-establish communication
    automatically to maintain the VNF without manual intervention to
    provide service continuity.

.. req::
    :id: R-18725
    :target: VNF
    :keyword: MUST

    The VNF **MUST** handle the restart of a single VNFC instance
    without requiring all VNFC instances to be restarted.

.. req::
    :id: R-06668
    :target: VNF
    :keyword: MUST

    The VNF **MUST** handle the start or restart of VNFC instances
    in any order with each VNFC instance establishing or re-establishing
    required connections or relationships with other VNFC instances and/or
    VNFs required to perform the VNF function/role without requiring VNFC
    instance(s) to be started/restarted in a particular order.

.. req::
    :id: R-80070
    :target: VNF
    :keyword: MUST

    The VNF **MUST** handle errors and exceptions so that they do
    not interrupt processing of incoming VNF requests to maintain service
    continuity (where the error is not directly impacting the software
    handling the incoming request).

.. req::
    :id: R-32695
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide the ability to modify the number of
    retries, the time between retries and the behavior/action taken after
    the retries have been exhausted for exception handling to allow the
    NCSP to control that behavior, where the interface and/or functional
    specification allows for altering behaviour.

.. req::
    :id: R-48356
    :target: VNF
    :keyword: MUST

    The VNF **MUST** fully exploit exception handling to the extent
    that resources (e.g., threads and memory) are released when no longer
    needed regardless of programming language.

.. req::
    :id: R-67918
    :target: VNF
    :keyword: MUST

    The VNF **MUST** handle replication race conditions both locally
    and geo-located in the event of a data base instance failure to maintain
    service continuity.

.. req::
    :id: R-36792
    :target: VNF
    :keyword: MUST

    The VNF **MUST** automatically retry/resubmit failed requests
    made by the software to its downstream system to increase the success rate.

.. req::
    :id: R-70013
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** require any manual steps to get it ready for
    service after a container rebuild.

.. req::
    :id: R-65515
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide a mechanism and tool to start VNF
    containers (VMs) without impacting service or service quality assuming
    another VNF in same or other geographical location is processing service
    requests.

.. req::
    :id: R-94978
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide a mechanism and tool to perform a graceful
    shutdown of all the containers (VMs) in the VNF without impacting service
    or service quality assuming another VNF in same or other geographical
    location can take over traffic and process service requests.

System Resource Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ensure an application is using appropriate system resources for the task
at hand; for example, do not use network or IO operations inside
critical sections, which could end up blocking other threads or
processes or eating memory if they are unable to complete. Critical
sections should only contain memory operation, and should not contain
any network or IO operation.

System Resource Optimization Requirements


.. req::
    :id: R-22059
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** execute long running tasks (e.g., IO,
    database, network operations, service calls) in a critical section
    of code, so as to minimize blocking of other operations and increase
    concurrent throughput.

.. req::
    :id: R-63473
    :target: VNF
    :keyword: MUST

    The VNF **MUST** automatically advertise newly scaled
    components so there is no manual intervention required.

.. req::
    :id: R-74712
    :target: VNF
    :keyword: MUST

    The VNF **MUST** utilize FQDNs (and not IP address) for
    both Service Chaining and scaling.

.. req::
    :id: R-41159
    :target: VNF
    :keyword: MUST

    The VNF **MUST** deliver any and all functionality from any
    VNFC in the pool (where pooling is the most suitable solution). The
    VNFC pool member should be transparent to the client. Upstream and
    downstream clients should only recognize the function being performed,
    not the member performing it.

.. req::
    :id: R-85959
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** automatically enable/disable added/removed
    sub-components or component so there is no manual intervention required.

.. req::
    :id: R-06885
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** support the ability to scale down a VNFC pool
    without jeopardizing active sessions. Ideally, an active session should
    not be tied to any particular VNFC instance.

.. req::
    :id: R-12538
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** support load balancing and discovery
    mechanisms in resource pools containing VNFC instances.

.. req::
    :id: R-98989
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** utilize resource pooling (threads,
    connections, etc.) within the VNF application so that resources
    are not being created and destroyed resulting in resource management
    overhead.

.. req::
    :id: R-55345
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** use techniques such as "lazy loading" when
    initialization includes loading catalogues and/or lists which can grow
    over time, so that the VNF startup time does not grow at a rate
    proportional to that of the list.

.. req::
    :id: R-35532
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** release and clear all shared assets (memory,
    database operations, connections, locks, etc.) as soon as possible,
    especially before long running sync and asynchronous operations, so as
    to not prevent use of these assets by other entities.

Application Configuration Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Leverage configuration management audit capability to drive conformity
to develop gold configurations for technologies like Java, Python, etc.

Application Configuration Management Requirements


.. req::
    :id: R-77334
    :target: VNF
    :keyword: MUST

    The VNF **MUST** allow configurations and configuration parameters
    to be managed under version control to ensure consistent configuration
    deployment, traceability and rollback.

.. req::
    :id: R-99766
    :target: VNF
    :keyword: MUST

    The VNF **MUST** allow configurations and configuration parameters
    to be managed under version control to ensure the ability to rollback to
    a known valid configuration.

.. req::
    :id: R-73583
    :target: VNF
    :keyword: MUST

    The VNF **MUST** allow changes of configuration parameters
    to be consumed by the VNF without requiring the VNF or its sub-components
    to be bounced so that the VNF availability is not effected.

Intelligent Transaction Distribution & Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Leverage Intelligent Load Balancing and redundant components (hardware
and modules) for all transactions, such that at any point in the
transaction: front end, middleware, back end -- a failure in any one
component does not result in a failure of the application or system;
i.e., transactions will continue to flow, albeit at a possibly reduced
capacity until the failed component restores itself. Create redundancy
in all layers (software and hardware) at local and remote data centers;
minimizing interdependencies of components (i.e. data replication,
deploying non-related elements in the same container).

Intelligent Transaction Distribution & Management Requirements


.. req::
    :id: R-21558
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** use intelligent routing by having knowledge
    of multiple downstream/upstream endpoints that are exposed to it, to
    ensure there is no dependency on external services (such as load balancers)
    to switch to alternate endpoints.

.. req::
    :id: R-08315
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** use redundant connection pooling to connect
    to any backend data source that can be switched between pools in an
    automated/scripted fashion to ensure high availability of the connection
    to the data source.

.. req::
    :id: R-27995
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** include control loop mechanisms to notify
    the consumer of the VNF of their exceeding SLA thresholds so the consumer
    is able to control its load against the VNF.

Deployment Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^

Reduce opportunity for failure, by human or by machine, through smarter
deployment practices and automation. This can include rolling code
deployments, additional testing strategies, and smarter deployment
automation (remove the human from the mix).

Deployment Optimization Requirements


.. req::
    :id: R-73364
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support at least two major versions of the
    VNF software and/or sub-components to co-exist within production
    environments at any time so that upgrades can be applied across
    multiple systems in a staggered manner.

.. req::
    :id: R-02454
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support the existence of multiple major/minor
    versions of the VNF software and/or sub-components and interfaces that
    support both forward and backward compatibility to be transparent to
    the Service Provider usage.

.. req::
    :id: R-57855
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support hitless staggered/rolling deployments
    between its redundant instances to allow "soak-time/burn in/slow roll"
    which can enable the support of low traffic loads to validate the
    deployment prior to supporting full traffic loads.

.. req::
    :id: R-64445
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support the ability of a requestor of the
    service to determine the version (and therefore capabilities) of the
    service so that Network Cloud Service Provider can understand the
    capabilities of the service.

.. req::
    :id: R-56793
    :target: VNF
    :keyword: MUST

    The VNF **MUST** test for adherence to the defined performance
    budgets at each layer, during each delivery cycle with delivered
    results, so that the performance budget is measured and the code
    is adjusted to meet performance budget.

.. req::
    :id: R-77667
    :target: VNF
    :keyword: MUST

    The VNF **MUST** test for adherence to the defined performance
    budget at each layer, during each delivery cycle so that the performance
    budget is measured and feedback is provided where the performance budget
    is not met.

.. req::
    :id: R-49308
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** test for adherence to the defined resiliency
    rating recommendation at each layer, during each delivery cycle with
    delivered results, so that the resiliency rating is measured and the
    code is adjusted to meet software resiliency requirements.

.. req::
    :id: R-16039
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** test for adherence to the defined
    resiliency rating recommendation at each layer, during each
    delivery cycle so that the resiliency rating is measured and
    feedback is provided where software resiliency requirements are
    not met.

Monitoring & Dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^

Promote dashboarding as a tool to monitor and support the general
operational health of a system. It is critical to the support of the
implementation of many resiliency patterns essential to the maintenance
of the system. It can help identify unusual conditions that might
indicate failure or the potential for failure. This would contribute to
improve Mean Time to Identify (MTTI), Mean Time to Repair (MTTR), and
post-incident diagnostics.

Monitoring & Dashboard Requirements


.. req::
    :id: R-34957
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide a method of metrics gathering for each
    layer's performance to identify variances in the allocations so
    they can be addressed.

.. req::
    :id: R-49224
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide unique traceability of a transaction
    through its life cycle to ensure quick and efficient troubleshooting.

.. req::
    :id: R-52870
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide a method of metrics gathering
    and analysis to evaluate the resiliency of the software from both
    a granular as well as a holistic standpoint. This includes, but is
    not limited to thread utilization, errors, timeouts, and retries.

.. req::
    :id: R-92571
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide operational instrumentation such as
    logging, so as to facilitate quick resolution of issues with the VNF to
    provide service continuity.

.. req::
    :id: R-48917
    :target: VNF
    :keyword: MUST

    The VNF **MUST** monitor for and alert on (both sender and
    receiver) errant, running longer than expected and missing file transfers,
    so as to minimize the impact due to file transfer errors.

.. req::
    :id: R-28168
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** use an appropriately configured logging
    level that can be changed dynamically, so as to not cause performance
    degradation of the VNF due to excessive logging.

.. req::
    :id: R-87352
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** utilize Cloud health checks, when available
    from the Network Cloud, from inside the application through APIs to check
    the network connectivity, dropped packets rate, injection, and auto failover
    to alternate sites if needed.

.. req::
    :id: R-16560
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** conduct a resiliency impact assessment for all
    inter/intra-connectivity points in the VNF to provide an overall resiliency
    rating for the VNF to be incorporated into the software design and
    development of the VNF.

Virtual Function - Container Recovery Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

**Evacuate(VM)**: The Controller client is requesting moving a specified
VM from its current AIC host to another (when the host is down). Moving
from a specified Host will be supported at in a later release (Openstack).

**Migrate (VM)**: The Controller client is requesting migrating a running
target VM from its current AIC host to another. Migrating a running target
VM from a specified Host will be supported at in a later release (Openstack).

**Reboot(VM)**: The Controller client is requesting to reboot the VM.
Options are soft (graceful) or hard (Openstack).

**Rebuild (VM)**: The Controller client is recreating a target VM instance
to a known (good) state (Openstack).

**Restart (VM)**: The Controller client is requesting to restart the VM
(Openstack).

**Snapshot (VM)**: The Controller client is requesting to create a snapshot
of a VNF or VM and store it (Openstack).

**Start (VM)**: The Controller client is requesting to start the VM
(Openstack).

**Stop (VM)**: The Controller client is requesting to stop the VM
(Openstack).

.. req::
    :id: R-11790
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support ONAP Controller's
    **Restart (stop/start or reboot)** command.

.. req::
    :id: R-56218
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support ONAP Controller's Migrate command that
    moves container (VM) from a live Physical Server / Compute Node to
    another live Physical Server / Compute Node.

        Note: Container migrations MUST be transparent to the VNF and no more intrusive than a stop,
        followed by some down time for the migration to be performed from one Compute Node / Physical
        Server to another, followed by a start of the same VM with same configuration on the new
        Compute Node / Physical Server.

.. req::
    :id: R-38001
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support ONAP Controller's **Rebuild** command.

.. req::
    :id: R-76901
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support a container rebuild mechanism based on existing
    image (e.g. Glance image in Openstack environment) or a snapshot.

.. req::
    :id: R-46851
    :target: VNF
    :keyword: MUST
    :introduced: casablanca

    The VNF **MUST** support ONAP Controller's Evacuate command.

.. req::
    :id: R-48761
    :target: VNF
    :keyword: MUST
    :introduced: casablanca

    The VNF **MUST** support ONAP Controller's Snapshot command.
