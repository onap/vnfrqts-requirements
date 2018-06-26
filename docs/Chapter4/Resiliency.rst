.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

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

Section 5.a Resiliency in *VNF Guidelines* describes
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

* R-52499 The VNF **MUST** meet their own resiliency goals and not rely
  on the Network Cloud.
* R-42207 The VNF **MUST** design resiliency into a VNF such that the
  resiliency deployment model (e.g., active-active) can be chosen at
  run-time.
* R-03954 The VNF **MUST** survive any single points of failure within
  the Network Cloud (e.g., virtual NIC, VM, disk failure).
* R-89010 The VNF **MUST** survive any single points of software failure
  internal to the VNF (e.g., in memory structures, JMS message queues).
* R-67709 The VNF **MUST** be designed, built and packaged to enable
  deployment across multiple fault zones (e.g., VNFCs deployed in
  different servers, racks, OpenStack regions, geographies) so that
  in the event of a planned/unplanned downtime of a fault zone, the
  overall operation/throughput of the VNF is maintained.
* R-35291 The VNF **MUST** support the ability to failover a VNFC
  automatically to other geographically redundant sites if not
  deployed active-active to increase the overall resiliency of the VNF.
* R-36843 The VNF **MUST** support the ability of the VNFC to be deployable
  in multi-zoned cloud sites to allow for site support in the event of cloud
  zone failure or upgrades.
* R-00098 The VNF **MUST NOT** impact the ability of the VNF to provide
  service/function due to a single container restart.
* R-79952 The VNF **SHOULD** support container snapshots if not for rebuild
  and evacuate for rollback or back out mechanism.

Minimize Cross Data-Center Traffic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Avoid performance-sapping data center-to-data center replication delay
by applying techniques such as caching and persistent transaction paths
- Eliminate replication delay impact between data centers by using a
concept of stickiness (i.e., once a client is routed to data center "A",
the client will stay with Data center “A” until the entire session is
completed).

Minimize Cross Data-Center Traffic Requirements

* R-92935 The VNF **SHOULD** minimize the propagation of state information
  across multiple data centers to avoid cross data center traffic.

Application Resilient Error Handling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ensure an application communicating with a downstream peer is equipped
to intelligently handle all error conditions. Make sure code can handle
exceptions seamlessly - implement smart retry logic and implement
multi-point entry (multiple data centers) for back-end system
applications.

Application Resilient Error Handling Requirements

* R-26371 The VNF **MUST** detect communication failure for inter VNFC
  instance and intra/inter VNF and re-establish communication
  automatically to maintain the VNF without manual intervention to
  provide service continuity.
* R-18725 The VNF **MUST** handle the restart of a single VNFC instance
  without requiring all VNFC instances to be restarted.
* R-06668 The VNF **MUST** handle the start or restart of VNFC instances
  in any order with each VNFC instance establishing or re-establishing
  required connections or relationships with other VNFC instances and/or
  VNFs required to perform the VNF function/role without requiring VNFC
  instance(s) to be started/restarted in a particular order.
* R-80070 The VNF **MUST** handle errors and exceptions so that they do
  not interrupt processing of incoming VNF requests to maintain service
  continuity (where the error is not directly impacting the software
  handling the incoming request).
* R-32695 The VNF **MUST** provide the ability to modify the number of
  retries, the time between retries and the behavior/action taken after
  the retries have been exhausted for exception handling to allow the
  NCSP to control that behavior, where the interface and/or functional
  specification allows for altering behaviour.
* R-48356 The VNF **MUST** fully exploit exception handling to the extent
  that resources (e.g., threads and memory) are released when no longer
  needed regardless of programming language.
* R-67918 The VNF **MUST** handle replication race conditions both locally
  and geo-located in the event of a data base instance failure to maintain
  service continuity.
* R-36792 The VNF **MUST** automatically retry/resubmit failed requests
  made by the software to its downstream system to increase the success rate.
* R-70013 The VNF **MUST NOT** require any manual steps to get it ready for
  service after a container rebuild.
* R-65515 The VNF **MUST** provide a mechanism and tool to start VNF
  containers (VMs) without impacting service or service quality assuming
  another VNF in same or other geographical location is processing service
  requests.
* R-94978 The VNF **MUST** provide a mechanism and tool to perform a graceful
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

* R-22059 The VNF **MUST NOT** execute long running tasks (e.g., IO,
  database, network operations, service calls) in a critical section
  of code, so as to minimize blocking of other operations and increase
  concurrent throughput.
* R-63473 The VNF **MUST** automatically advertise newly scaled
  components so there is no manual intervention required.
* R-74712 The VNF **MUST** utilize FQDNs (and not IP address) for
  both Service Chaining and scaling.
* R-41159 The VNF **MUST** deliver any and all functionality from any
  VNFC in the pool (where pooling is the most suitable solution). The
  VNFC pool member should be transparent to the client. Upstream and
  downstream clients should only recognize the function being performed,
  not the member performing it.
* R-85959 The VNF **SHOULD** automatically enable/disable added/removed
  sub-components or component so there is no manual intervention required.
* R-06885 The VNF **SHOULD** support the ability to scale down a VNFC pool
  without jeopardizing active sessions. Ideally, an active session should
  not be tied to any particular VNFC instance.
* R-12538 The VNF **SHOULD** support load balancing and discovery
  mechanisms in resource pools containing VNFC instances.
* R-98989 The VNF **SHOULD** utilize resource pooling (threads,
  connections, etc.) within the VNF application so that resources
  are not being created and destroyed resulting in resource management
  overhead.
* R-55345 The VNF **SHOULD** use techniques such as “lazy loading” when
  initialization includes loading catalogues and/or lists which can grow
  over time, so that the VNF startup time does not grow at a rate
  proportional to that of the list.
* R-35532 The VNF **SHOULD** release and clear all shared assets (memory,
  database operations, connections, locks, etc.) as soon as possible,
  especially before long running sync and asynchronous operations, so as
  to not prevent use of these assets by other entities.


Application Configuration Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Leverage configuration management audit capability to drive conformity
to develop gold configurations for technologies like Java, Python, etc.

Application Configuration Management Requirements

* R-77334 The VNF **MUST** allow configurations and configuration parameters
  to be managed under version control to ensure consistent configuration
  deployment, traceability and rollback.
* R-99766 The VNF **MUST** allow configurations and configuration parameters
  to be managed under version control to ensure the ability to rollback to
  a known valid configuration.
* R-73583 The VNF **MUST** allow changes of configuration parameters
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

* R-21558 The VNF **SHOULD** use intelligent routing by having knowledge
  of multiple downstream/upstream endpoints that are exposed to it, to
  ensure there is no dependency on external services (such as load balancers)
  to switch to alternate endpoints.
* R-08315 The VNF **SHOULD** use redundant connection pooling to connect
  to any backend data source that can be switched between pools in an
  automated/scripted fashion to ensure high availability of the connection
  to the data source.
* R-27995 The VNF **SHOULD** include control loop mechanisms to notify
  the consumer of the VNF of their exceeding SLA thresholds so the consumer
  is able to control its load against the VNF.

Deployment Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^

Reduce opportunity for failure, by human or by machine, through smarter
deployment practices and automation. This can include rolling code
deployments, additional testing strategies, and smarter deployment
automation (remove the human from the mix).

Deployment Optimization Requirements

* R-73364 The VNF **MUST** support at least two major versions of the
  VNF software and/or sub-components to co-exist within production
  environments at any time so that upgrades can be applied across
  multiple systems in a staggered manner.
* R-02454 The VNF **MUST** support the existence of multiple major/minor
  versions of the VNF software and/or sub-components and interfaces that
  support both forward and backward compatibility to be transparent to
  the Service Provider usage.
* R-57855 The VNF **MUST** support hitless staggered/rolling deployments
  between its redundant instances to allow "soak-time/burn in/slow roll"
  which can enable the support of low traffic loads to validate the
  deployment prior to supporting full traffic loads.
* R-64445 The VNF **MUST** support the ability of a requestor of the
  service to determine the version (and therefore capabilities) of the
  service so that Network Cloud Service Provider can understand the
  capabilities of the service.
* R-56793 The VNF **MUST** test for adherence to the defined performance
  budgets at each layer, during each delivery cycle with delivered
  results, so that the performance budget is measured and the code
  is adjusted to meet performance budget.
* R-77667 The VNF **MUST** test for adherence to the defined performance
  budget at each layer, during each delivery cycle so that the performance
  budget is measured and feedback is provided where the performance budget
  is not met.
* R-49308 The VNF **SHOULD** test for adherence to the defined resiliency
  rating recommendation at each layer, during each delivery cycle with
  delivered results, so that the resiliency rating is measured and the
  code is adjusted to meet software resiliency requirements.
* R-16039 The VNF **SHOULD** test for adherence to the defined
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

* R-34957 The VNF **MUST** provide a method of metrics gathering for each
  layer's performance to identify/document variances in the allocations so
  they can be addressed.
* R-49224 The VNF **MUST** provide unique traceability of a transaction
  through its life cycle to ensure quick and efficient troubleshooting.
* R-52870 The VNF **MUST** provide a method of metrics gathering
  and analysis to evaluate the resiliency of the software from both
  a granular as well as a holistic standpoint. This includes, but is
  not limited to thread utilization, errors, timeouts, and retries.
* R-92571 The VNF **MUST** provide operational instrumentation such as
  logging, so as to facilitate quick resolution of issues with the VNF to
  provide service continuity.
* R-48917 The VNF **MUST** monitor for and alert on (both sender and
  receiver) errant, running longer than expected and missing file transfers,
  so as to minimize the impact due to file transfer errors.
* R-28168 The VNF **SHOULD** use an appropriately configured logging
  level that can be changed dynamically, so as to not cause performance
  degradation of the VNF due to excessive logging.
* R-87352 The VNF **SHOULD** utilize Cloud health checks, when available
  from the Network Cloud, from inside the application through APIs to check
  the network connectivity, dropped packets rate, injection, and auto failover
  to alternate sites if needed.
* R-16560 The VNF **SHOULD** conduct a resiliency impact assessment for all
  inter/intra-connectivity points in the VNF to provide an overall resiliency
  rating for the VNF to be incorporated into the software design and
  development of the VNF.
