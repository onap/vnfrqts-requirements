.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 ONAP

.. toctree::
   :maxdepth: 3

.. contents::
   :depth: 3
..

================
VNF Requirements
================


**1. Purpose**
==============
- The purpose of these requirements is to accelerate adoption of VNF best practices which will increase innovation, minimize customization needed to onboard VNFs as well as reduce implementation complexity, time and cost for all impacted stakeholders.
- This initial release consolidates the requirements from Open-O and OpenECOMP to provide common VNF requirements across the industry in order to drive interoperability, simplify management, and reduce cost to build, deploy and manage VNFs.
- These requirements serve multiple purposes:
    - Primarily it provides a detailed list of requirements for VNF providers to meet to be compatible with ONAP; VNF providers will use the VNF requirements to build VNFs that are compatible with ONAP
    - It can also serve as a list of requirements that service providers can use in RFPs for selecting VNFs
    - It will also be used as a basis for testing and certification of VNFs for compliance with ONAP; ONAP projects such as the VNF Validation Project will uses these VNFs requirements to build test cases to validate VNFs for compliance with ONAP.

**2. Scope**
============
- The audience for this document are VNF providers, NCSPs and other interested 3rd parties who need to know the design, build and lifecycle management requirements for VNFs to be compliant with ONAP.
- These requirements are strictly from a standpoint of what the VNF developer needs to know to operate and be compliant with ONAP.
- Requirements that are not applicable to VNF providers such as those that applicable to service providers are not included in this document.
- These requirements are applicable to the Amsterdam release of ONAP.
- Scope of the ONAP versions/release and future functionality

a. References
-------------
This section contains a list of normative and informative references along with information on acquiring the identified references.  Normative references are required to be implemented by this document. Informative references are for informational purposes only.

Normative References
--------------------
+---------------+---------------------------------------------------------------------------------------------------------------+
| Reference     | Description                                                                                                   |
+===============+===============================================================================================================+
| [RFC 2119]    | IETF RFC2119, Key words for use in RFCs to Indicate Requirement Levels, S. Bradner, March 1997.               |
+---------------+---------------------------------------------------------------------------------------------------------------+

Informative References
----------------------
+---------------+---------------------------------------------------------------------------------------------------------------+
| Reference     | Description                                                                                                   |
+===============+===============================================================================================================+
|               |                                                                                                               |
+---------------+---------------------------------------------------------------------------------------------------------------+

Reference Acquisition
---------------------
IETF Specifications:

- Internet Engineering Task Force (IETF) Secretariat, 48377 Fremont Blvd., Suite 117, Fremont, California 94538, USA; Phone: +1-510-492-4080, Fax: +1-510-492-4001.

**3. Introduction**
====================
- These requirements are specific to the Amsterdam release of ONAP. It is the initial release of requirements based on a merge of the Open-O and OpenECOMP requirements.
- Requirements are identified as either MUST, MUST NOT, SHOULD, SHOULD NOT, or MAY as defined in RFC 2119.
- Chapter 4 contains the VNF requirements involving the design and development of VNFs. These requirements help VNFs operate efficiently within a cloud environment. Requirements cover design, resiliency, security, modularity and DevOps.
- Chapter 5 describes the different data models the VNF provider needs to understand.  There are currently 2 models described in this document
    - The first model is the onboarding package data model. This is a TOSCA model that will describe how all the elements passed from the VNF Provider to the Service provider should be formatted and packaged.
    - The second model is HEAT template used for orchestrating and instantiating virtual resources in an OpenStack environment.  At this time the HEAT files will be passed to the Service provider as a data element within the TOSCA onboarding package.
- Chapter 6 details the requirements specific to an implementation. The current implementations documented are OpenStack and Azure.
- Chapter 7 provides the comprehensive set of requirements for VNFs to be on-boarded, configured and managed by ONAP.
- Chapter 8 is the appendix that provide a number of detailed data record formats.

**4. VNF Development Requirements**
====================================

a. VNF Design
-------------

Services are composed of VNFs and common components and are designed to
be agnostic of the location to leverage capacity where it exists in the
Network Cloud. VNFs can be instantiated in any location that meets the
performance and latency requirements of the service.

A key design principle for virtualizing services is decomposition of
network functions using NFV concepts into granular VNFs. This enables
instantiating and customizing only essential functions as needed for the
service, thereby making service delivery more nimble. It provides
flexibility of sizing and scaling and also provides flexibility with
packaging and deploying VNFs as needed for the service. It enables
grouping functions in a common cloud data center to minimize
inter-component latency. The VNFs should be designed with a goal of
being modular and reusable to enable using best-in-breed vendors.

Section 5.a VNF Design in *VNF Guidelines* describes
the overall guidelines for designing VNFs from VNF Components (VNFCs).
Below are more detailed requirements for composing VNFs.

VNF Design Requirements

* R-58421 The VNF **SHOULD** be decomposed into granular re-usable VNFCs.
* R-82223 The VNF **MUST** be decomposed if the functions have significantly different scaling characteristics (e.g., signaling versus media functions, control versus data plane functions).
* R-16496 The VNF **MUST** enable instantiating only the functionality that is needed for the decomposed VNF (e.g., if transcoding is not needed it should not be instantiated).
* R-02360 The VNFC **MUST** be designed as a standalone, executable process.
* R-34484 The VNF **SHOULD** create a single component VNF for VNFCs that can be used by other VNFs.
* R-23035 The VNF **MUST** be designed to scale horizontally (more instances of a VNF or VNFC) and not vertically (moving the existing instances to larger VMs or increasing the resources within a VM) to achieve effective utilization of cloud resources.
* R-30650 The VNF **MUST** utilize cloud provided infrastructure and VNFs (e.g., virtualized Local Load Balancer) as part of the VNF so that the cloud can manage and provide a consistent service resiliency and methods across all VNF's.
* R-12709 The VNFC **SHOULD** be independently deployed, configured, upgraded, scaled, monitored, and administered by ONAP.
* R-37692 The VNFC **MUST** provide API versioning to allow for independent upgrades of VNFC.
* R-86585 The VNFC **SHOULD** minimize the use of state within a VNFC to facilitate the movement of traffic from one instance to another.
* R-65134 The VNF **SHOULD** maintain state in a geographically redundant datastore that may, in fact, be its own VNFC.
* R-75850 The VNF **SHOULD** decouple persistent data from the VNFC and keep it in its own datastore that can be reached by all instances of the VNFC requiring the data.
* R-88199 The VNF **MUST** utilize virtualized, scalable open source database software that can meet the performance/latency requirements of the service for all datastores.
* R-99656 The VNF **MUST** NOT terminate stable sessions if a VNFC instance fails.
* R-84473 The VNF **MUST** enable DPDK in the guest OS for VNF’s requiring high packets/sec performance.  High packet throughput is defined as greater than 500K packets/sec.
* R-54430 The VNF **MUST** use the NCSP’s supported library and compute flavor that supports DPDK to optimize network efficiency if using DPDK. [1]_
* R-18864 The VNF **MUST** NOT use technologies that bypass virtualization layers (such as SR-IOV) unless approved by the NCSP (e.g., if necessary to meet functional or performance requirements).
* R-64768 The VNF **MUST** limit the size of application data packets to no larger than 9000 bytes for SDN network-based tunneling when guest data packets are transported between tunnel endpoints that support guest logical networks.
* R-74481 The VNF **MUST** NOT require the use of a dynamic routing protocol unless necessary to meet functional requirements.

b. VNF Resiliency
-----------------

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
^^^^^^^^^^^^^^^^^^^^

Design the VNF to be resilient to the failures of the underlying
virtualized infrastructure (Network Cloud). VNF design considerations
would include techniques such as multiple vLANs, multiple local and
geographic instances, multiple local and geographic data replication,
and virtualized services such as Load Balancers.


All Layer Redundancy Requirements

* R-52499 The VNF **MUST** meet their own resiliency goals and not rely on the Network Cloud.
* R-42207 The VNF **MUST** design resiliency into a VNF such that the resiliency deployment model (e.g., active-active) can be chosen at run-time.
* R-03954 The VNF **MUST** survive any single points of failure within the Network Cloud (e.g., virtual NIC, VM, disk failure).
* R-89010 The VNF **MUST** survive any single points of software failure internal to the VNF (e.g., in memory structures, JMS message queues).
* R-67709 The VNF **MUST** be designed, built and packaged to enable deployment across multiple fault zones (e.g., VNFCs deployed in different servers, racks, OpenStack regions, geographies) so that in the event of a planned/unplanned downtime of a fault zone, the overall operation/throughput of the VNF is maintained.
* R-35291 The VNF **MUST** support the ability to failover a VNFC automatically to other geographically redundant sites if not deployed active-active to increase the overall resiliency of the VNF.
* R-36843 The VNF **MUST** support the ability of the VNFC to be deployable in multi-zoned cloud sites to allow for site support in the event of cloud zone failure or upgrades.

Minimize Cross Data-Center Traffic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Avoid performance-sapping data center-to-data center replication delay
by applying techniques such as caching and persistent transaction paths
- Eliminate replication delay impact between data centers by using a
concept of stickiness (i.e., once a client is routed to data center "A",
the client will stay with Data center “A” until the entire session is
completed).

Minimize Cross Data-Center Traffic Requirements

* R-92935 The VNF **SHOULD** minimize the propagation of state information across multiple data centers to avoid cross data center traffic.

Application Resilient Error Handling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ensure an application communicating with a downstream peer is equipped
to intelligently handle all error conditions. Make sure code can handle
exceptions seamlessly - implement smart retry logic and implement
multi-point entry (multiple data centers) for back-end system
applications.

Application Resilient Error Handling Requirements

* R-26371 The VNF **MUST** detect connectivity failure for inter VNFC instance and intra/inter VNF and re-establish connectivity automatically to maintain the VNF without manual intervention to provide service continuity.
* R-18725 The VNF **MUST** handle the restart of a single VNFC instance without requiring all VNFC instances to be restarted.
* R-06668 The VNF **MUST** handle the start or restart of VNFC instances in any order with each VNFC instance establishing or re-establishing required connections or relationships with other VNFC instances and/or VNFs required to perform the VNF function/role without requiring VNFC instance(s) to be started/restarted in a particular order.
* R-80070 The VNF **MUST** handle errors and exceptions so that they do not interrupt processing of incoming VNF requests to maintain service continuity.
* R-32695 The VNF **MUST** provide the ability to modify the number of retries, the time between retries and the behavior/action taken after the retries have been exhausted for exception handling to allow the NCSP to control that behavior.
* R-48356 The VNF **MUST** fully exploit exception handling to the extent that resources (e.g., threads and memory) are released when no longer needed regardless of programming language.
* R-67918 The VNF **MUST** handle replication race conditions both locally and geo-located in the event of a data base instance failure to maintain service continuity.
* R-36792 The VNF **MUST** automatically retry/resubmit failed requests made by the software to its downstream system to increase the success rate.


System Resource Optimization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ensure an application is using appropriate system resources for the task
at hand; for example, do not use network or IO operations inside
critical sections, which could end up blocking other threads or
processes or eating memory if they are unable to complete. Critical
sections should only contain memory operation, and should not contain
any network or IO operation.


System Resource Optimization Requirements

* R-22059 The VNF **MUST NOT** execute long running tasks (e.g., IO, database, network operations, service calls) in a critical section of code, so as to minimize blocking of other operations and increase concurrent throughput.
* R-63473 The VNF **MUST** automatically advertise newly scaled components so there is no manual intervention required.
* R-74712 The VNF **MUST** utilize FQDNs (and not IP address) for both Service Chaining and scaling.
* R-41159 The VNF **MUST** deliver any and all functionality from any VNFC in the pool. The VNFC pool member should be transparent to the client. Upstream and downstream clients should only recognize the function being performed, not the member performing it.
* R-85959 The VNF **SHOULD** automatically enable/disable added/removed sub-components or component so there is no manual intervention required.
* R-06885 The VNF **SHOULD** support the ability to scale down a VNFC pool without jeopardizing active sessions. Ideally, an active session should not be tied to any particular VNFC instance.
* R-12538 The VNF **SHOULD** support load balancing and discovery mechanisms in resource pools containing VNFC instances.
* R-98989 The VNF **SHOULD** utilize resource pooling (threads, connections, etc.) within the VNF application so that resources are not being created and destroyed resulting in resource management overhead.
* R-55345 The VNF **SHOULD** use techniques such as “lazy loading” when initialization includes loading catalogues and/or lists which can grow over time, so that the VNF startup time does not grow at a rate proportional to that of the list.
* R-35532 The VNF **SHOULD** release and clear all shared assets (memory, database operations, connections, locks, etc.) as soon as possible, especially before long running sync and asynchronous operations, so as to not prevent use of these assets by other entities.


Application Configuration Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Leverage configuration management audit capability to drive conformity
to develop gold configurations for technologies like Java, Python, etc.

Application Configuration Management Requirements

* R-77334 The VNF **MUST** allow configurations and configuration parameters to be managed under version control to ensure consistent configuration deployment, traceability and rollback.
* R-99766 The VNF **MUST** allow configurations and configuration parameters to be managed under version control to ensure the ability to rollback to a known valid configuration.
* R-73583 The VNF **MUST** allow changes of configuration parameters to be consumed by the VNF without requiring the VNF or its sub-components to be bounced so that the VNF availability is not effected.


Intelligent Transaction Distribution & Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

* R-21558 The VNF **SHOULD** use intelligent routing by having knowledge of multiple downstream/upstream endpoints that are exposed to it, to ensure there is no dependency on external services (such as load balancers) to switch to alternate endpoints.
* R-08315 The VNF **SHOULD** use redundant connection pooling to connect to any backend data source that can be switched between pools in an automated/scripted fashion to ensure high availability of the connection to the data source.
* R-27995 The VNF **SHOULD** include control loop mechanisms to notify the consumer of the VNF of their exceeding SLA thresholds so the consumer is able to control its load against the VNF.

Deployment Optimization
^^^^^^^^^^^^^^^^^^^^^^^

Reduce opportunity for failure, by human or by machine, through smarter
deployment practices and automation. This can include rolling code
deployments, additional testing strategies, and smarter deployment
automation (remove the human from the mix).

Deployment Optimization Requirements

* R-73364 The VNF **MUST** support at least two major versions of the VNF software and/or sub-components to co-exist within production environments at any time so that upgrades can be applied across multiple systems in a staggered manner.
* R-02454 The VNF **MUST** support the existence of multiple major/minor versions of the VNF software and/or sub-components and interfaces that support both forward and backward compatibility to be transparent to the Service Provider usage.
* R-57855 The VNF **MUST** support hitless staggered/rolling deployments between its redundant instances to allow "soak-time/burn in/slow roll" which can enable the support of low traffic loads to validate the deployment prior to supporting full traffic loads.
* R-64445 The VNF **MUST** support the ability of a requestor of the service to determine the version (and therefore capabilities) of the service so that Network Cloud Service Provider can understand the capabilities of the service.
* R-56793 The VNF **MUST** test for adherence to the defined performance budgets at each layer, during each delivery cycle with delivered results, so that the performance budget is measured and the code is adjusted to meet performance budget.
* R-77667 The VNF **MUST** test for adherence to the defined performance budget at each layer, during each delivery cycle so that the performance budget is measured and feedback is provided where the performance budget is not met.
* R-49308 The VNF **SHOULD** test for adherence to the defined resiliency rating recommendation at each layer, during each delivery cycle with delivered results, so that the resiliency rating is measured and the code is adjusted to meet software resiliency requirements.
* R-16039 The VNF **SHOULD** test for adherence to the defined resiliency rating recommendation at each layer, during each delivery cycle so that the resiliency rating is measured and feedback is provided where software resiliency requirements are not met.

Monitoring & Dashboard
^^^^^^^^^^^^^^^^^^^^^^

Promote dashboarding as a tool to monitor and support the general
operational health of a system. It is critical to the support of the
implementation of many resiliency patterns essential to the maintenance
of the system. It can help identify unusual conditions that might
indicate failure or the potential for failure. This would contribute to
improve Mean Time to Identify (MTTI), Mean Time to Repair (MTTR), and
post-incident diagnostics.

Monitoring & Dashboard Requirements

* R-34957 The VNF **MUST** provide a method of metrics gathering for each layer's performance to identify/document variances in the allocations so they can be addressed.
* R-49224 The VNF **MUST** provide unique traceability of a transaction through its life cycle to ensure quick and efficient troubleshooting.
* R-52870 The VNF **MUST** provide a method of metrics gathering and analysis to evaluate the resiliency of the software from both a granular as well as a holistic standpoint. This includes, but is not limited to thread utilization, errors, timeouts, and retries.
* R-92571 The VNF **MUST** provide operational instrumentation such as logging, so as to facilitate quick resolution of issues with the VNF to provide service continuity.
* R-48917 The VNF **MUST** monitor for and alert on (both sender and receiver) errant, running longer than expected and missing file transfers, so as to minimize the impact due to file transfer errors.
* R-28168 The VNF **SHOULD** use an appropriately configured logging level that can be changed dynamically, so as to not cause performance degradation of the VNF due to excessive logging.
* R-87352 The VNF **SHOULD** utilize Cloud health checks, when available from the Network Cloud, from inside the application through APIs to check the network connectivity, dropped packets rate, injection, and auto failover to alternate sites if needed.
* R-16560 The VNF **MUST** conduct a resiliency impact assessment for all inter/intra-connectivity points in the VNF to provide an overall resiliency rating for the VNF to be incorporated into the software design and development of the VNF.

c. VNF Security
---------------

The objective of this section is to provide the key security
requirements that need to be met by VNFs. The security requirements are
grouped into five areas as listed below. Other security areas will be
addressed in future updates. These security requirements are applicable
to all VNFs. Additional security requirements for specific types of VNFs
will be applicable and are outside the scope of these general
requirements.

Section 5.a Security in *VNF Guidelines* outlines
the five broad security areas for VNFs that are detailed in the
following sections:

-  **VNF General Security**: This section addresses general security
   requirements for the VNFs that the VNF provider will need to address.

-  **VNF Identity and Access Management**: This section addresses
   security requirements with respect to Identity and Access Management
   as these pertain to generic VNFs.

-  **VNF API Security**: This section addresses the generic security
   requirements associated with APIs. These requirements are applicable
   to those VNFs that use standard APIs for communication and data
   exchange.

-  **VNF Security Analytics**: This section addresses the security
   requirements associated with analytics for VNFs that deal with
   monitoring, data collection and analysis.

-  **VNF Data Protection**: This section addresses the security
   requirements associated with data protection.

VNF General Security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section provides details on the VNF general security requirements
on various security areas such as user access control, network security,
ACLs, infrastructure security, and vulnerability management. These
requirements cover topics associated with compliance, security patching,
logging/accounting, authentication, encryption, role-based access
control, least privilege access/authorization. The following security
requirements need to be met by the solution in a virtual environment:

General Security Requirements

Integration and operation within a robust security environment is necessary and expected. The security architecture will include one or more of the following: IDAM (Identity and Access Management) for all system and applications access, Code scanning, network vulnerability scans, OS, Database and application patching, malware detection and cleaning, DDOS prevention, network security gateways (internal and external) operating at various layers, host and application based tools for security compliance validation, aggressive security patch application, tightly controlled software distribution and change control processes and other state of the art security solutions. The VNF is expected to function reliably within such an environment and the developer is expected to understand and accommodate such controls and can expected to supply responsive interoperability support and testing throughout the product’s lifecycle.

* R-23740 The VNF **MUST** accommodate the security principle of “least privilege” during development, implementation and operation. The importance of “least privilege” cannot be overstated and must be observed in all aspects of VNF development and not limited to security. This is applicable to all sections of this document.
* R-61354 The VNF **MUST** implement access control list for OA&M services (e.g., restricting access to certain ports or applications).
* R-85633 The VNF **MUST** implement Data Storage Encryption (database/disk encryption) for Sensitive Personal Information (SPI) and other subscriber identifiable data. Note: subscriber’s SPI/data must be encrypted at rest, and other subscriber identifiable data should be encrypted at rest. Other data protection requirements exist and should be well understood by the developer.
* R-92207 The VNF **SHOULD** implement a mechanism for automated and frequent "system configuration (automated provisioning / closed loop)" auditing.
* R-23882 The VNF **SHOULD** be scanned using both network scanning and application scanning security tools on all code, including underlying OS and related configuration. Scan reports shall be provided. Remediation roadmaps shall be made available for any findings.
* R-46986 The VNF **SHOULD** have source code scanned using scanning tools (e.g., Fortify) and provide reports.
* R-55830 The VNF **MUST** distribute all production code from NCSP internal sources only. No production code, libraries, OS images, etc. shall be distributed from publically accessible depots.
* R-99771 The VNF **MUST** provide all code/configuration files in a "Locked down" or hardened state or with documented recommendations for such hardening. All unnecessary services will be disabled. VNF provider default credentials, community strings and other such artifacts will be removed or disclosed so that they can be modified or removed during provisioning.
* R-19768 The VNF **SHOULD** support L3 VPNs that enable segregation of traffic by application (dropping packets not belonging to the VPN) (i.e., AVPN, IPSec VPN for Internet routes).
* R-33981 The VNF **SHOULD** interoperate with various access control mechanisms for the Network Cloud execution environment (e.g., Hypervisors, containers).
* R-40813 The VNF **SHOULD** support the use of virtual trusted platform module, hypervisor security testing and standards scanning tools.
* R-56904 The VNF **MUST** interoperate with the ONAP (SDN) Controller so that it can dynamically modify the firewall rules, ACL rules, QoS rules, virtual routing and forwarding rules.
* R-26586 The VNF **SHOULD** support the ability to work with aliases (e.g., gateways, proxies) to protect and encapsulate resources.
* R-49956 The VNF **MUST** pass all access to applications (Bearer, signaling and OA&M) through various security tools and platforms from ACLs, stateful firewalls and application layer gateways depending on manner of deployment. The application is expected to function (and in some cases, interwork) with these security tools.
* R-69649 The VNF **MUST** have all vulnerabilities patched as soon as possible. Patching shall be controlled via change control process with vulnerabilities disclosed along with mitigation recommendations.
* R-78010 The VNF **MUST** use the NCSP’s IDAM API for Identification, authentication and access control of customer or VNF application users.
* R-42681 The VNF **MUST** use the NCSP’s IDAM API or comply with the requirements if not using the NCSP’s IDAM API, for identification, authentication and access control of OA&M and other system level functions.
* R-68589 The VNF **MUST**, if not using the NCSP’s IDAM API, support User-IDs and passwords to uniquely identify the user/application. VNF needs to have appropriate connectors to the Identity, Authentication and Authorization systems that enables access at OS, Database and Application levels as appropriate.
* R-52085 The VNF **MUST**, if not using the NCSP’s IDAM API, provide the ability to support Multi-Factor Authentication (e.g., 1st factor = Software token on device (RSA SecureID); 2nd factor = User Name+Password, etc.) for the users.
* R-98391 The VNF **MUST**, if not using the NCSP’s IDAM API, support Role-Based Access Control to permit/limit the user/application to performing specific activities.
* R-63217 The VNF **MUST**, if not using the NCSP’s IDAM API, support logging via ONAP for a historical view of “who did what and when”.
* R-62498 The VNF **MUST**, if not using the NCSP’s IDAM API, encrypt OA&M access (e.g., SSH, SFTP).
* R-79107 The VNF **MUST**, if not using the NCSP’s IDAM API, enforce a configurable maximum number of Login attempts policy for the users. VNF provider must comply with "terminate idle sessions" policy. Interactive sessions must be terminated, or a secure, locking screensaver must be activated requiring authentication, after a configurable period of inactivity. The system-based inactivity timeout for the enterprise identity and access management system must also be configurable.
* R-35144 The VNF **MUST**, if not using the NCSP’s IDAM API, comply with the NCSP’s credential management policy.
* R-75041 The VNF **MUST**, if not using the NCSP’s IDAM API, expire passwords at regular configurable intervals.
* R-46908 The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "password complexity" policy. When passwords are used, they shall be complex and shall at least meet the following password construction requirements: (1) be a minimum configurable number of characters in length, (2) include 3 of the 4 following types of characters: upper-case alphabetic, lower-case alphabetic, numeric, and special, (3) not be the same as the UserID with which they are associated or other common strings as specified by the environment, (4) not contain repeating or sequential characters or numbers, (5) not to use special characters that may have command functions, and (6) new passwords must not contain sequences of three or more characters from the previous password.
* R-39342 The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "password changes (includes default passwords)" policy. Products will support password aging, syntax and other credential management practices on a configurable basis.
* R-40521 The VNF **MUST**, if not using the NCSP’s IDAM API, support use of common third party authentication and authorization tools such as TACACS+, RADIUS.
* R-41994 The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "No Self-Signed Certificates" policy. Self-signed certificates must be used for encryption only, using specified and approved encryption protocols such as LS 1.1 or higher or equivalent security protocols such as IPSec, AES.
* R-23135 The VNF **MUST**, if not using the NCSP’s IDAM API, authenticate system to system communications were one system accesses the resources of another system, and must never conceal individual accountability.

VNF Identity and Access Management Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following security requirements for logging, identity, and access
management need to be met by the solution in a virtual environment:


Identity and Access Management Requirements

* R-95105 The VNF **MUST** host connectors for access to the application layer.
* R-45496 The VNF **MUST** host connectors for access to the OS (Operating System) layer.
* R-05470 The VNF **MUST** host connectors for access to the database layer.
* R-99174 The VNF **MUST** comply with Individual Accountability (each person must be assigned a unique ID) when persons or non-person entities access VNFs.
* R-42874 The VNF **MUST** comply with Least Privilege (no more privilege than required to perform job functions) when persons or non-person entities access VNFs.
* R-71787 The VNF **MUST** comply with Segregation of Duties (access to a single layer and no developer may access production without special oversight) when persons or non-person entities access VNFs.
* R-86261 The VNF **MUST NOT** allow VNF provider access to VNFs remotely.
* R-49945 The VNF **MUST** authorize VNF provider access through a client application API by the client application owner and the resource owner of the VNF before provisioning authorization through Role Based Access Control (RBAC), Attribute Based Access Control (ABAC), or other policy based mechanism.
* R-31751 The VNF **MUST** subject VNF provider access to privilege reconciliation tools to prevent access creep and ensure correct enforcement of access policies.
* R-34552 The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for OWASP Top 10.
* R-29301 The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Password Attacks.
* R-72243 The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Phishing / SMishing.
* R-58998 The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Malware (Key Logger).
* R-14025 The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Session Hijacking.
* R-31412 The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for XSS / CSRF.
* R-51883 The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Replay.
* R-44032 The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Man in the Middle (MITM).
* R-58977 The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Eavesdropping.
* R-24825 The VNF **MUST** provide Context awareness data (device, location, time, etc.) and be able to integrate with threat detection system.
* R-59391 The VNF provider **MUST**, where a VNF provider requires the assumption of permissions, such as root or administrator, first log in under their individual user login ID then switch to the other higher level account; or where the individual user login is infeasible, must login with an account with admin privileges in a way that uniquely identifies the individual performing the function.
* R-85028 The VNF **MUST** authenticate system to system access and do not conceal a VNF provider user’s individual accountability for transactions.
* R-80335 The VNF **MUST** make visible a Warning Notices: A formal statement of resource intent, i.e., a warning notice, upon initial access to a VNF provider user who accesses private internal networks or Company computer resources, e.g., upon initial logon to an internal web site, system or application which requires authentication.
* R-73541 The VNF **MIST** use access controls for VNFs and their supporting computing systems at all times to restrict access to authorized personnel only, e.g., least privilege. These controls could include the use of system configuration or access control software.
* R-64503 The VNF **MUST** provide minimum privileges for initial and default settings for new user accounts.
* R-86835 The VNF **MUST** set the default settings for user access to sensitive commands and data to deny authorization.
* R-77157 The VNF **MUST** conform to approved request, workflow authorization, and authorization provisioning requirements when creating privileged users.
* R-81147 The VNF **MUST** have greater restrictions for access and execution, such as up to 3 factors of authentication and restricted authorization, for commands affecting network services, such as commands relating to VNFs, must.
* R-49109 The VNF **MUST** encrypt TCP/IP--HTTPS (e.g., TLS v1.2) transmission of data on internal and external networks.
* R-39562 The VNF **MUST** disable unnecessary or vulnerable cgi-bin programs.
* R-15671 The VNF **MUST NOT** provide public or unrestricted access to any data without the permission of the data owner. All data classification and access controls must be followed.
* R-89753 The VNF **MUST NOT** install or use systems, tools or utilities capable of capturing or logging data that was not created by them or sent specifically to them in production, without authorization of the VNF system owner.
* R-19082 The VNF **MUST NOT** run security testing tools and programs, e.g., password cracker, port scanners, hacking tools in production, without authorization of the VNF system owner.
* R-19790 The VNF **MUST NOT** include authentication credentials in security audit logs, even if encrypted.
* R-85419 The VNF **SHOULD** use REST APIs exposed to Client Applications for the implementation of OAuth 2.0 Authorization Code Grant and Client Credentials Grant, as the standard interface for a VNF.
* R-86455 The VNF **SHOULD** support hosting connectors for OS Level and Application Access.
* R-48080 The VNF **SHOULD** support SCEP (Simple Certificate Enrollment Protocol).


VNF API Security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section covers API security requirements when these are used by the
VNFs. Key security areas covered in API security are Access Control,
Authentication, Passwords, PKI Authentication Alarming, Anomaly
Detection, Lawful Intercept, Monitoring and Logging, Input Validation,
Cryptography, Business continuity, Biometric Authentication,
Identification, Confidentiality and Integrity, and Denial of Service.

The solution in a virtual environment needs to meet the following API
security requirements:


API Requirements

* R-37608 The VNF **MUST** provide a mechanism to restrict access based on the attributes of the VNF and the attributes of the subject.
* R-43884 The VNF **MUST** integrate with external authentication and authorization services (e.g., IDAM).
* R-25878 The VNF **MUST** use certificates issued from publicly recognized Certificate Authorities (CA) for the authentication process where PKI-based authentication is used.
* R-19804 The VNF **MUST** validate the CA signature on the certificate, ensure that the date is within the validity period of the certificate, check the Certificate Revocation List (CRL), and recognize the identity represented by the certificate where PKI-based authentication is used.
* R-47204 The VNF **MUST** protect the confidentiality and integrity of data at rest and in transit from unauthorized access and modification.
* R-33488 The VNF **MUST** protect against all denial of service attacks, both volumetric and non-volumetric, or integrate with external denial of service protection tools.
* R-21652 The VNF **MUST** implement the following input validation control: Check the size (length) of all input. Do not permit an amount of input so great that it would cause the VNF to fail. Where the input may be a file, the VNF API must enforce a size limit.
* R-54930 The VNF **MUST** implement the following input validation control: Do not permit input that contains content or characters inappropriate to the input expected by the design. Inappropriate input, such as SQL insertions, may cause the system to execute undesirable and unauthorized transactions against the database or allow other inappropriate access to the internal network.
* R-21210 The VNF **MUST** implement the following input validation control: Validate that any input file has a correct and valid Multipurpose Internet Mail Extensions (MIME) type. Input files should be tested for spoofed MIME types.
* R-23772 The VNF **MUST** validate input at all layers implementing VNF APIs.
* R-87135 The VNF **MUST** comply with NIST standards and industry best practices for all implementations of cryptography.
* R-02137 The VNF **MUST** implement all monitoring and logging as described in the Security Analytics section.
* R-15659 The VNF **MUST** restrict changing the criticality level of a system security alarm to administrator(s).
* R-19367 The VNF **MUST** monitor API invocation patterns to detect anomalous access patterns that may represent fraudulent access or other types of attacks, or integrate with tools that implement anomaly and abuse detection.
* R-78066 The VNF **MUST** support requests for information from law enforcement and government agencies.


VNF Security Analytics Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section covers VNF security analytics requirements that are mostly
applicable to security monitoring. The VNF Security Analytics cover the
collection and analysis of data following key areas of security
monitoring:

-  Anti-virus software

-  Logging

-  Data capture

-  Tasking

-  DPI

-  API based monitoring

-  Detection and notification

-  Resource exhaustion detection

-  Proactive and scalable monitoring

-  Mobility and guest VNF monitoring

-  Closed loop monitoring

-  Interfaces to management and orchestration

-  Malformed packet detections

-  Service chaining

-  Dynamic security control

-  Dynamic load balancing

-  Connection attempts to inactive ports (malicious port scanning)

The following requirements of security monitoring need to be met by the
solution in a virtual environment.

Security Analytics Requirements

* R-48470 The VNF **MUST** support Real-time detection and notification of security events.
* R-22286 The VNF **MUST** support Integration functionality via API/Syslog/SNMP to other functional modules in the network (e.g., PCRF, PCEF) that enable dynamic security control by blocking the malicious traffic or malicious end users
* R-32636 The VNF **MUST** support API-based monitoring to take care of the scenarios where the control interfaces are not exposed, or are optimized and proprietary in nature.
* R-61648 The VNF **MUST** support event logging, formats, and delivery tools to provide the required degree of event data to ONAP
* R-22367 The VNF **MUST** support detection of malformed packets due to software misconfiguration or software vulnerability.
* R-31961 The VNF **MUST** support integrated DPI/monitoring functionality as part of VNFs (e.g., PGW, MME).
* R-20912 The VNF **MUST** support alternative monitoring capabilities when VNFs do not expose data or control traffic or use proprietary and optimized protocols for inter VNF communication.
* R-73223 The VNF **MUST** support proactive monitoring to detect and report the attacks on resources so that the VNFs and associated VMs can be isolated, such as detection techniques for resource exhaustion, namely OS resource attacks, CPU attacks, consumption of kernel memory, local storage attacks.
* R-58370 The VNF **MUST** coexist and operate normally with commercial anti-virus software which shall produce alarms every time when there is a security incident.
* R-56920 The VNF **MUST** protect all security audit logs (including API, OS and application-generated logs), security audit software, data, and associated documentation from modification, or unauthorized viewing, by standard OS access control mechanisms, by sending to a remote system, or by encryption.
* R-54520 The VNF **MUST** log successful and unsuccessful login attempts.
* R-55478 The VNF **MUST** log logoffs.
* R-08598 The VNF **MUST** log successful and unsuccessful changes to a privilege level.
* R-13344 The VNF **MUST** log starting and stopping of security logging
* R-07617 The VNF **MUST** log creating, removing, or changing the inherent privilege level of users.
* R-94525 The VNF **MUST** log connections to a network listener of the resource.
* R-31614 The VNF **MUST** log the field “event type” in the security audit logs.
* R-97445 The VNF **MUST** log the field “date/time” in the security audit logs.
* R-25547 The VNF **MUST** log the field “protocol” in the security audit logs.
* R-06413 The VNF **MUST** log the field “service or program used for access” in the security audit logs.
* R-15325 The VNF **MUST** log the field “success/failure” in the security audit logs.
* R-89474 The VNF **MUST** log the field “Login ID” in the security audit logs.
* R-04982 The VNF **MUST NOT** include an authentication credential, e.g., password, in the security audit logs, even if encrypted.
* R-63330 The VNF **MUST** detect when the security audit log storage medium is approaching capacity (configurable) and issue an alarm via SMS or equivalent as to allow time for proper actions to be taken to pre-empt loss of audit data.
* R-41252 The VNF **MUST** support the capability of online storage of security audit logs.
* R-41825 The VNF **MUST** activate security alarms automatically when the following event is detected: configurable number of consecutive unsuccessful login attempts
* R-43332 The VNF **MUST** activate security alarms automatically when the following event is detected: successful modification of critical system or application files
* R-74958 The VNF **MUST** activate security alarms automatically when the following event is detected: unsuccessful attempts to gain permissions or assume the identity of another user
* R-15884 The VNF **MUST** include the field “date” in the Security alarms (where applicable and technically feasible).
* R-23957 The VNF **MUST** include the field “time” in the Security alarms (where applicable and technically feasible).
* R-71842 The VNF **MUST** include the field “service or program used for access” in the Security alarms (where applicable and technically feasible).
* R-57617 The VNF **MUST** include the field “success/failure” in the Security alarms (where applicable and technically feasible).
* R-99730 The VNF **MUST** include the field “Login ID” in the Security alarms (where applicable and technically feasible).
* R-29705 The VNF **MUST** restrict changing the criticality level of a system security alarm to administrator(s).
* R-13627 The VNF **MUST** monitor API invocation patterns to detect anomalous access patterns that may represent fraudulent access or other types of attacks, or integrate with tools that implement anomaly and abuse detection.
* R-21819 The VNF **MUST** support requests for information from law enforcement and government agencies.
* R-56786 The VNF **MUST** implement “Closed Loop” automatic implementation (without human intervention) for Known Threats with detection rate in low false positives.
* R-25094 The VNF **MUST** perform data capture for security functions.
* R-04492 The VNF **MUST** generate security audit logs that must be sent to Security Analytics Tools for analysis.
* R-19219 The VNF **MUST** provide audit logs that include user ID, dates, times for log-on and log-off, and terminal location at minimum.
* R-30932 The VNF **MUST** provide security audit logs including records of successful and rejected system access data and other resource access attempts.
* R-54816 The VNF **MUST** support the storage of security audit logs for agreed period of time for forensic analysis.
* R-57271 The VNF **MUST** provide the capability of generating security audit logs by interacting with the operating system (OS) as appropriate.
* R-84160 The VNF **MUST** have security logging for VNFs and their OSs be active from initialization. Audit logging includes automatic routines to maintain activity records and cleanup programs to ensure the integrity of the audit/logging systems.

VNF Data Protection Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section covers VNF data protection requirements that are mostly
applicable to security monitoring.


Data Protection Requirements

* R-58964 The VNF **MUST** provide the capability to restrict read and write access to data.
* R-99112 The VNF **MUST** provide the capability to restrict access to data to specific users.
* R-83227 The VNF **MUST** Provide the capability to encrypt data in transit on a physical or virtual network.
* R-32641 The VNF **MUST** provide the capability to encrypt data on non-volatile memory.
* R-13151 The VNF **SHOULD** disable the paging of the data requiring encryption, if possible, where the encryption of non-transient data is required on a device for which the operating system performs paging to virtual memory. If not possible to disable the paging of the data requiring encryption, the virtual memory should be encrypted.
* R-93860 The VNF **MUST** provide the capability to integrate with an external encryption service.
* R-73067 The VNF **MUST** use industry standard cryptographic algorithms and standard modes of operations when implementing cryptography.
* R-22645 The VNF **SHOULD** use commercial algorithms only when there are no applicable governmental standards for specific cryptographic functions, e.g., public key cryptography, message digests.
* R-12467 The VNF **MUST NOT** use the SHA, DSS, MD5, SHA-1 and Skipjack algorithms or other compromised encryption.
* R-02170 The VNF **MUST** use, whenever possible, standard implementations of security applications, protocols, and format, e.g., S/MIME, TLS, SSH, IPSec, X.509 digital certificates for cryptographic implementations. These implementations must be purchased from reputable vendors and must not be developed in-house.
* R-70933 The VNF **MUST** provide the ability to migrate to newer versions of cryptographic algorithms and protocols with no impact.
* R-44723 The VNF **MUST** use symmetric keys of at least 112 bits in length.
* R-25401 The VNF **MUST** use asymmetric keys of at least 2048 bits in length.
* R-95864 The VNF **MUST** use commercial tools that comply with X.509 standards and produce x.509 compliant keys for public/private key generation.
* R-12110 The VNF **MUST NOT** use keys generated or derived from predictable functions or values, e.g., values considered predictable include user identity information, time of day, stored/transmitted data.
* R-52060 The VNF **MUST** provide the capability to configure encryption algorithms or devices so that they comply with the laws of the jurisdiction in which there are plans to use data encryption.
* R-69610 The VNF **MUST** provide the capability of using certificates issued from a Certificate Authority not provided by the VNF provider.
* R-83500 The VNF **MUST** provide the capability of allowing certificate renewal and revocation.
* R-29977 The VNF **MUST** provide the capability of testing the validity of a digital certificate by validating the CA signature on the certificate.
* R-24359 The VNF **MUST** provide the capability of testing the validity of a digital certificate by validating the date the certificate is being used is within the validity period for the certificate.
* R-39604 The VNF **MUST** provide the capability of testing the validity of a digital certificate by checking the Certificate Revocation List (CRL) for the certificates of that type to ensure that the certificate has not been revoked.
* R-75343 The VNF **MUST** provide the capability of testing the validity of a digital certificate by recognizing the identity represented by the certificate — the "distinguished name".

d. VNF Modularity
-----------------

ONAP Heat Orchestration Templates: Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP supports a modular Heat Orchestration Template design pattern,
referred to as *VNF Modularity.*

ONAP VNF Modularity Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With VNF Modularity, a single VNF may be composed from one or more Heat
Orchestration Templates, each of which represents a subset of the
overall VNF. These component parts are referred to as “\ *VNF
Modules*\ ”. During orchestration, these modules are deployed
incrementally to create the complete VNF.

A modular Heat Orchestration Template can be either one of the following
types:

1. Base Module

2. Incremental Module

3. Cinder Volume Module

* R-37028 The VNF **MUST** be composed of one “base” module.
* R-41215 The VNF **MAY** have zero to many “incremental” modules.
* R-20974 The VNF **MUST** deploy the base module first, prior to the incremental modules.

ONAP also supports the concept of an optional, independently deployed
Cinder volume via a separate Heat Orchestration Templates, referred to
as a Cinder Volume Module. This allows the volume to persist after a
Virtual Machine (VM) (i.e., OS::Nova::Server) is deleted, allowing the
volume to be reused on another instance (e.g., during a failover
activity).

* R-11200 The VNF MUST keep the scope of a Cinder volume module, when it exists, to be 1:1 with the VNF Base Module or Incremental Module.

* R-nnnnn The VNF MUST have a corresponding environment file for a Base Module.
* R-nnnnn The VNF MUST have a corresponding environment file for an Incremental Module.
* R-nnnnn The VNF MUST have a corresponding environment file for a Cinder Volume Module.

These concepts will be described in more detail throughout the document.
This overview is provided to set the stage and help clarify the concepts
that will be introduced.


ONAP VNF Modularity
^^^^^^^^^^^^^^^^^^^

ONAP supports a modular Heat Orchestration Template design pattern,
referred to as *VNF Modularity.* With this approach, a single VNF may be
composed from one or more Heat Orchestration Templates, each of which
represents a subset of the overall VNF. These component parts are
referred to as “\ *VNF Modules*\ ”. During orchestration, these modules
are deployed incrementally to create the complete VNF.

A modular Heat Orchestration Template can be either one of the following
types:

1. Base Module

2. Incremental Module

3. Cinder Volume Module

A VNF must be composed of one “base” module and may be composed of zero
to many “incremental” modules. The base module must be deployed first,
prior to the incremental modules.

ONAP also supports the concept of an optional, independently deployed
Cinder volume via a separate Heat Orchestration Templates, referred to
as a Cinder Volume Module. This allows the volume to persist after a VM
(i.e., OS::Nova::Server) is deleted, allowing the volume to be reused on
another instance (e.g., during a failover activity).

The scope of a Cinder volume module, when it exists, must be 1:1 with a
Base module or Incremental Module.

A Base Module must have a corresponding environment file.

An Incremental Module must have a corresponding environment file.

A Cinder Volume Module must have a corresponding environment file.

A VNF module (base, incremental, cinder) may support nested templates.

A shared Heat Orchestration Template resource must be defined in the
base module. A shared resource is a resource that that will be
referenced by another resource that is defined in the Base Module and/or
one or more incremental modules.

When the shared resource needs to be referenced by a resource in an
incremental module, the UUID of the shared resource must be exposed by
declaring an ONAP Base Module Output Parameter.

Note that a Cinder volume is *not* a shared resource. A volume template
must correspond 1:1 with a base module or incremental module.

An example of a shared resource is the resource
OS::Neutron::SecurityGroup. Security groups are sets of IP filter rules
that are applied to a VNF’s networking. The resource OS::Neutron::Port
has a property security_groups which provides the security groups
associated with port. The value of parameter(s) associated with this
property must be the UUIDs of the resource(s)
OS::Neutron::SecurityGroup.

*Note:* A Cinder volume is *not* considered a shared resource. A volume
template must correspond 1:1 with a base template or add-on module
template.

Suggested Patterns for Modular VNFs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are numerous variations of VNF modularity. Below are two suggested
usage patterns.

**Option 1: Modules per VNFC type**

a. Base module contains only the shared resources.

b. Group all VMs (e.g., VNFCs) of a given type (i.e. {vm-type}) into its
   own incremental module. That is, the VNF has an incremental module
   for each {vm-type}.

c. For a given {vm-type} incremental module, the VNF may have

   i.  One incremental module used for both initial turn up and re-used
       for scaling. This approach is used when the number of VMs
       instantiated will be the same for initial deployment and scaling.

   ii. Two incremental modules, where one is used for initial turn up
       and one is used for scaling. This approach is used when the
       number of VMs instantiated will be different for initial
       deployment and scaling.

**Option 2: Base VNF with Incremental Growth Modules**

a. Base module contains a complete initial VNF instance

b. Incremental modules for incremental scaling units

   i.  May contain VMs of multiple types in logical scaling combinations

   ii. May be separated by VM type for multi-dimensional scaling

With no growth units, Option 2 is equivalent to the “One Heat Template
per VNF” model.

Note that modularization of VNFs is not required. A single Heat
Orchestration Template (a base module) may still define a complete VNF,
which might be appropriate for smaller VNFs that do not have any scaling
options.

Modularity Rules
^^^^^^^^^^^^^^^^

There are some rules to follow when building modular VNF templates:

1. All VNFs must have one Base VNF Module (template) that must be the
   first one deployed. The base template:

   a. Must include all shared resources (e.g., private networks, server
      groups, security groups)

   b. Must expose all shared resources (by UUID) as “outputs” in its
      associated Heat template (i.e., ONAP Base Module Output
      Parameters)

   c. May include initial set of VMs

   d. May be operational as a stand-alone “minimum” configuration of the
      VNF

2. VNFs may have one or more incremental modules which:

   a. Defines additional resources that can be added to an existing VNF

   b. Must be complete Heat templates

      i. i.e. not snippets to be incorporated into some larger template

   c. Should define logical growth-units or sub-components of an overall
      VNF

   d. On creation, receives appropriate Base Module outputs as
      parameters

      i.  Provides access to all shared resources (by UUID)

      ii. must not be dependent on other Add-On VNF Modules

   e. Multiple instances of an incremental Module may be added to the
      same VNF (e.g., incrementally grow a VNF by a fixed “add-on”
      growth units)

3. Each VNF Module (base or incremental) may have (optional) an
   associated Cinder Volume Module (see Cinder Volume Templates)

   a. Volume modules must correspond 1:1 with a base module or
      incremental module

   b. A Cinder volume may be embedded within the base module or
      incremental module if persistence is not required

4. Shared resource UUIDs are passed between the base module and
   incremental modules via Heat Outputs Parameters (i.e., Base Module
   Output Parameters)

   a. The output parameter name in the base must match the parameter
      name in the add-on module

VNF Modularity Examples
^^^^^^^^^^^^^^^^^^^^^^^

*Example: Base Module creates SecurityGroup*

A VNF has a base module, named base.yaml, that defines a
OS::Neutron::SecurityGroup. The security group will be referenced by an
OS::Neutron::Port resource in an incremental module, named
INCREMENTAL_MODULE.yaml. The base module defines a parameter in the out
section named dns_sec_grp_id. dns_sec_grp_id is defined as a
parameter in the incremental module. ONAP captures the UUID value of
dns_sec_grp_id from the base module output statement and provides the
value to the incremental module.

Note that the example below is not a complete Heat Orchestration
Template. The {network-role} has been defined as oam to represent an oam
network and the {vm-type} has been defined as dns.

base_MODULE.yaml

.. code-block:: yaml

 parameters:
   . . .

 resources:
   DNS_SECURITY_GROUP:
     type: OS::Neutron::SecurityGroup
     properties:
       description: vDNS security group
       name:
         str_replace:
           template: VNF_NAME_sec_grp_DNS
           params:
             VMF_NAME: {get_param: vnf_name}
       rules: [. . . . .

   . . .

 outputs:
   dns_sec_grp_id:
     description: UUID of DNS Resource SecurityGroup
     value: { get_resource: DNS_SECURITY_GROUP }


INCREMENTAL_MODULE.yaml

.. code-block:: yaml

 parameters:
   dns_sec_grp_id:
     type: string
     description: security group UUID
   . . .

 resources:
   dns_oam_0_port:
     type: OS::Neutron::Port
     properties:
       name:
         str_replace:
           template: VNF_NAME_dns_oam_port
           params:
             VNF_NAME: {get_param: vnf_name}
       network: { get_param: oam_net_name }
       fixed_ips: [{ "ip_address": { get_param: dns_oam_ip_0 }}]
       security_groups: [{ get_param: dns_sec_grp_id }]


*Examples: Base Module creates an internal network*

A VNF has a base module, named base_module.yaml, that creates an
internal network. An incremental module, named incremental_module.yaml,
will create a VM that will connect to the internal network. The base
module defines a parameter in the out section named int_oam_net_id.
int_oam_net_id is defined as a parameter in the incremental module.
ONAP captures the UUID value of int_oam_net_id from the base module
output statement and provides the value to the incremental module.

Note that the example below is not a complete Heat Orchestration
Template. The {network-role} has been defined as oam to represent an oam
network and the {vm-type} has been defined as lb for load balancer.

base.yaml

.. code-block:: yaml

 heat_template_version: 2013-05-23

 resources:
    int_oam_network:
       type: OS::Neutron::Network
       properties:
          name: {… }
          . . .
 outputs:
    int_oam_net_id:
       value: {get_resource: int_oam_network }


incremental.yaml

.. code-block:: yaml

 heat_template_version: 2013-05-23

 parameters:
    int_oam_net_id:
       type: string
       description: ID of shared private network from Base template
    lb_name_0:
       type: string
       description: name for the add-on VM instance

 Resources:
    lb_server:
       type: OS::Nova::Server
       properties:
          name: {get_param: lb_name_0}
          networks:
             - port: { get_resource: lb_port }
          . . .

    lb_port:
       type: OS::Neutron::Port
       properties:
          network_id: { get_param: int_oam_net_id }
 ...

e. VNF Devops
-------------

This section includes guidelines for VNF providers to ensure that a Network
Cloud Service Provider’s operations personnel have a common and
consistent way to support VNFs and VNFCs.

NCSPs may elect to support standard images to enable compliance with
security, audit, regulatory and other needs. As part of the overall VNF
software bundle, VNF suppliers using standard images would typically
provide the NCSP with an install package consistent with the default OS
package manager (e.g. aptitude for Ubuntu, yum for Redhat/CentOS).

Section 5.a DevOps in *VNF Guidelines* describes
the DevOps guidelines for VNFs.

DevOps Requirements

* R-46960 The VNF **MUST** utilize only the Guest OS versions that are supported by the NCSP’s Network Cloud. [1]_
* R-23475 The VNF **SHOULD** utilize only NCSP provided Guest OS images. [1]_
* R-NNNNN The VNF **MUST** install the NCSP required software on Guest OS images when not using the NCSP provided Guest OS images. [1]_
* R-09467 The VNF **MUST**  utilize only NCSP standard compute flavors. [1]_
* R-02997 The VNF **MUST** preserve their persistent data. Running VMs will not be backed up in the Network Cloud infrastructure.
* R-29760 The VNFC **MUST** be installed on non-root file systems, unless software is specifically included with the operating system distribution of the guest image.
* R-20860 The VNF **MUST** be agnostic to the underlying infrastructure (such as hardware, host OS, Hypervisor), any requirements should be provided as specification to be fulfilled by any hardware.
* R-89800 The VNF **MUST NOT** require Hypervisor-level customization from the cloud provider.
* R-86758 The VNF **SHOULD** provide an automated test suite to validate every new version of the software on the target environment(s). The tests should be of sufficient granularity to independently test various representative VNF use cases throughout its lifecycle. Operations might choose to invoke these tests either on a scheduled basis or on demand to support various operations functions including test, turn-up and troubleshooting.
* R-39650 The VNF **SHOULD** provide the ability to test incremental growth of the VNF.
* R-14853 The VNF **MUST** respond to a "move traffic" [2]_ command against a specific VNFC, moving all existing session elsewhere with minimal disruption if a VNF provides a load balancing function across multiple instances of its VNFCs. Note: Individual VNF performance aspects (e.g., move duration or disruption scope) may require further constraints.
* R-06327 The VNF **MUST** respond to a "drain VNFC" [2]_ command against a specific VNFC, preventing new session from reaching the targeted VNFC, with no disruption to active sessions on the impacted VNFC, if a VNF provides a load balancing function across multiple instances of its VNFCs. This is used to support scenarios such as proactive maintenance with no user impact.
* R-NNNNN The VNF **SHOULD** support a software promotion methodology from dev/test -> pre-prod -> production in software, development & testing and operations.

f. VNF Develop Steps
--------------------

Aid to help the VNF provider to fasten the integration with the GVNFM, the
ONAP provides the VNF SDK tools, and the documents. In this charter,
the develop steps for VNF providers will be introduced.

First, using the VNF SDK tools to design the VNF with TOSCA model and
output the VNF TOSCA package. The VNF package can be validated, and
tested.

Second, the VNF provider should provide the VNF Rest API to integrate with
the GVNFM if needed. The VNF Rest API is aligned to the ETSI IFA
document.

Third, the TOSCA model supports the EPA feature.

Note:

1. The scripts to extend capacity to satisfy some special requirements.
   In the R2, the scripts is not implemented fully, and will be provided
   in the next release.

2. The monitoring and scale policy also be provide the next release.


.. [1]
   Refer to NCSP’s Network Cloud specification

.. [2]
   Not currently supported in ONAP release 1

**5. VNF Modeling Requirements**
=====================================

a. TOSCA YAML
-------------


Introduction
^^^^^^^^^^^^

This reference document is the VNF TOSCA Template Requirements for
ONAP, which provides recommendations and standards for building VNF
TOSCA templates compatible with ONAP initial implementations of
Network Cloud. It has the following features:

1. VNF TOSCA template designer supports GUI and CLI.

2. VNF TOSCA template is aligned to the newest TOSCA protocol, “Working
   Draft 04-Revision 06”.

3. VNF TOSCA template supports EPA features, such as NUMA, Hyper
   Threading, SRIOV， etc.

Intended Audience
^^^^^^^^^^^^^^^^^^

This document is intended for persons developing VNF TOSCA templates
that will be orchestrated by ONAP.

Scope
^^^^^

ONAP implementations of Network Cloud supports TOSCA Templates, also
referred to as TOSCA in this document.

ONAP requires the TOSCA Templates to follow a specific format. This
document provides the mandatory, recommended, and optional requirements
associated with this format.

Overview
^^^^^^^^

The document includes three charters to help the VNF providers to use the
VNF model design tools and understand the VNF package structure and VNF
TOSCA templates.

In the ONAP, VNF Package and VNFD template can be designed by manually
or via model designer tools. VNF model designer tools can provide the
GUI and CLI tools for the VNF provider to develop the VNF Package and VNFD
template.

The VNF package structure is align to the NFV TOSCA protocol, and
supports CSAR

The VNFD and VNF package are all align to the NFV TOSCA protocol, which
supports multiple TOSCA template yaml files, and also supports
self-defined node or other extensions.

NFV TOSCA Template
^^^^^^^^^^^^^^^^^^

TOSCA templates supported by ONAP must follow the requirements
enumerated in this section.

TOSCA Introduction
^^^^^^^^^^^^^^^^^^

TOSCA defines a Meta model for defining IT services. This Meta model
defines both the structure of a service as well as how to manage it. A
Topology Template (also referred to as the topology model of a service)
defines the structure of a service. Plans define the process models that
are used to create and terminate a service as well as to manage a
service during its whole lifetime.

A Topology Template consists of a set of Node Templates and Relationship
Templates that together define the topology model of a service as a (not
necessarily connected) directed graph. A node in this graph is
represented by a *Node Template*. A Node Template specifies the
occurrence of a Node Type as a component of a service. A *Node Type*
defines the properties of such a component (via *Node Type Properties*)
and the operations (via *Interfaces*) available to manipulate the
component. Node Types are defined separately for reuse purposes and a
Node Template references a Node Type and adds usage constraints, such as
how many times the component can occur.

|image1|

Figure 1: Structural Elements of Service Template and their Relations

TOSCA Modeling Principles & Data Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describing TOSCA modeling principles and data model for
NFV, which shall be based on [TOSCA-1.0] and [TOSCA-Simple-Profile-YAML
V1.0], or new type based on ETSI NFV requirements, etc.

VNF Descriptor Template
^^^^^^^^^^^^^^^^^^^^^^^^

The VNF Descriptor (VNFD) describes the topology of the VNF by means of
ETSI NFV IFA011 [IFA011] terms such as VDUs, Connection Points, Virtual
Links, External Connection Points, Scaling Aspects, Instantiation Levels
and Deployment Flavours.

The VNFD (VNF Descriptor) is read by both the NFVO and the VNFM. It
represents the contract & interface of a VNF and ensures the
interoperability across the NFV functional blocks.

The main parts of the VNFD are the following:

-  VNF topology: it is modeled in a cloud agnostic way using virtualized
   containers and their connectivity. Virtual Deployment Units (VDU)
   describe the capabilities of the virtualized containers, such as
   virtual CPU, RAM, disks; their connectivity is modeled with VDU
   Connection Point Descriptors (VduCpd), Virtual Link Descriptors (Vld)
   and VNF External Connection Point Descriptors (VnfExternalCpd);

-  VNF deployment aspects: they are described in one or more deployment
   flavours, including instantiation levels, supported LCM operations,
   VNF LCM operation configuration parameters, placement constraints
   (affinity / antiaffinity), minimum and maximum VDU instance numbers,
   and scaling aspect for horizontal scaling.

The following table defines the TOSCA Type “derived from” values that
SHALL be used when using the TOSCA Simple Profile for NFV version 1.0
specification [TOSCA-Simple-Profile-NFV-v1.0] for NFV VNFD.

+-----------------------------------------+---------------------------------------+-----------------------+
| **ETSI NFV Element**                    | **TOSCA VNFD**                        | **Derived from**      |
|                                         |                                       |                       |
| **[IFA011]**                            | **[TOSCA-Simple-Profile-NFV-v1.0]**   |                       |
+=========================================+=======================================+=======================+
| VNF                                     | tosca.nodes.nfv.VNF                   | tosca.nodes.Root      |
+-----------------------------------------+---------------------------------------+-----------------------+
| VDU                                     | tosca.nodes.nfv.VDU                   | tosca.nodes.Root      |
+-----------------------------------------+---------------------------------------+-----------------------+
| Cpd (Connection Point)                  | tosca.nodes.nfv.Cpd                   | tosca.nodes.Root      |
+-----------------------------------------+---------------------------------------+-----------------------+
| VduCpd (internal connection point)      | tosca.nodes.nfv.VduCpd                | tosca.nodes.nfv.Cpd   |
+-----------------------------------------+---------------------------------------+-----------------------+
| VnfVirtualLinkDesc (Virtual Link)       | tosca.nodes.nfv.VnfVirtualLinkDesc    | tosca.nodes.Root      |
+-----------------------------------------+---------------------------------------+-----------------------+
| VnfExtCpd (External Connection Point)   | tosca.nodes.nfv.VnfExtCpd             | tosca.nodes.Root      |
+-----------------------------------------+---------------------------------------+-----------------------+
| Virtual Storage                         |                                       |                       |
+-----------------------------------------+---------------------------------------+-----------------------+
| Virtual Compute                         |                                       |                       |
+-----------------------------------------+---------------------------------------+-----------------------+
| Software Image                          |                                       |                       |
+-----------------------------------------+---------------------------------------+-----------------------+
| Deployment Flavour                      |                                       |                       |
+-----------------------------------------+---------------------------------------+-----------------------+
| Scaling Aspect                          |                                       |                       |
+-----------------------------------------+---------------------------------------+-----------------------+
| Element Group                           |                                       |                       |
+-----------------------------------------+---------------------------------------+-----------------------+
| Instantiation Level                     |                                       |                       |
+-----------------------------------------+---------------------------------------+-----------------------+

+--------------------------------------------------------------------+
| +--------------------------------------------------------------+   |
| | tosca_definitions_version: tosca_simple_yaml_1_0       |   |
| |                                                              |   |
| | description: VNFD TOSCA file demo                            |   |
| |                                                              |   |
| | imports:                                                     |   |
| |                                                              |   |
| | - TOSCA_definition_nfv_1_0.yaml                          |   |
| |                                                              |   |
| | - TOSCA_definition_nfv_ext_1_0.yaml                     |   |
| |                                                              |   |
| | | **node_types:                                             |   |
| |   tosca.nodes.nfv.VNF.vOpenNAT:                              |   |
| |   derived_from:** tosca.nodes.nfv.VNF                       |   |
| | | **requirements:                                            |   |
| |   **- **sriov_plane:                                        |   |
| |   capability:** tosca.capabilities.nfv.VirtualLinkable       |   |
| | | **node:** tosca.nodes.nfv.VnfVirtualLinkDesc               |   |
| | | **relationship:** tosca.relationships.nfv.VirtualLinksTo   |   |
| +--------------------------------------------------------------+   |
+====================================================================+
+--------------------------------------------------------------------+

EPA Requirements
^^^^^^^^^^^^^^^^

1. SR-IOV Passthrought

Definitions of SRIOV_Port are necessary if VDU supports SR-IOV. Here is
an example.

+------------------------------------------------+
| node_templates:                               |
|                                                |
| vdu_vNat:                                     |
|                                                |
| SRIOV_Port:                                   |
|                                                |
| attributes:                                    |
|                                                |
| tosca_name: SRIOV_Port                       |
|                                                |
| properties:                                    |
|                                                |
| virtual_network_interface_requirements:     |
|                                                |
| - name: sriov                                  |
|                                                |
| support_mandatory: false                      |
|                                                |
| description: sriov                             |
|                                                |
| requirement:                                   |
|                                                |
| SRIOV: true                                    |
|                                                |
| role: root                                     |
|                                                |
| description: sriov port                        |
|                                                |
| layer_protocol: ipv4                          |
|                                                |
| requirements:                                  |
|                                                |
| - virtual_binding:                            |
|                                                |
| capability: virtual_binding                   |
|                                                |
| node: vdu_vNat                                |
|                                                |
| relationship:                                  |
|                                                |
| type: tosca.relationships.nfv.VirtualBindsTo   |
|                                                |
| - virtual_link:                               |
|                                                |
| node: tosca.nodes.Root                         |
|                                                |
| type: tosca.nodes.nfv.VduCpd                   |
|                                                |
| substitution_mappings:                        |
|                                                |
| requirements:                                  |
|                                                |
| sriov_plane:                                  |
|                                                |
| - SRIOV_Port                                  |
|                                                |
| - virtual_link                                |
|                                                |
| node_type: tosca.nodes.nfv.VNF.vOpenNAT       |
+------------------------------------------------+

2. Hugepages

Definitions of mem_page_size as one property shall be added to
Properties and set the value to large if one VDU node supports
huagepages. Here is an example.

+----------------------------------+
| node_templates:                 |
|                                  |
| vdu_vNat:                       |
|                                  |
| Hugepages:                       |
|                                  |
| attributes:                      |
|                                  |
| tosca_name: Huge_pages_demo   |
|                                  |
| properties:                      |
|                                  |
| mem_page_size:large            |
+==================================+
+----------------------------------+

3. NUMA (CPU/Mem)

Likewise, we shall add definitions of numa to
requested_additional_capabilities if we wand VUD nodes to support
NUMA. Here is an example.

+-------------------------------------------------+
| topology_template:                             |
|                                                 |
| node_templates:                                |
|                                                 |
| vdu_vNat:                                      |
|                                                 |
| capabilities:                                   |
|                                                 |
| virtual_compute:                               |
|                                                 |
| properties:                                     |
|                                                 |
| virtual_memory:                                |
|                                                 |
| numa_enabled: true                             |
|                                                 |
| virtual_mem_size: 2 GB                        |
|                                                 |
| requested_additional_capabilities:            |
|                                                 |
| numa:                                           |
|                                                 |
| support_mandatory: true                        |
|                                                 |
| requested_additional_capability_name: numa   |
|                                                 |
| target_performance_parameters:                |
|                                                 |
| hw:numa_nodes: "2"                             |
|                                                 |
| hw:numa_cpus.0: "0,1"                          |
|                                                 |
| hw:numa_mem.0: "1024"                          |
|                                                 |
| hw:numa_cpus.1: "2,3,4,5"                      |
|                                                 |
| hw:numa_mem.1: "1024"                          |
+-------------------------------------------------+

4. Hyper-Theading

Definitions of Hyper-Theading are necessary as one of
requested_additional_capabilities of one VUD node if that node
supports Hyper-Theading. Here is an example.

+-------------------------------------------------------------+
| topology_template:                                         |
|                                                             |
| node_templates:                                            |
|                                                             |
| vdu_vNat:                                                  |
|                                                             |
| capabilities:                                               |
|                                                             |
| virtual_compute:                                           |
|                                                             |
| properties:                                                 |
|                                                             |
| virtual_memory:                                            |
|                                                             |
| numa_enabled: true                                         |
|                                                             |
| virtual_mem_size: 2 GB                                    |
|                                                             |
| requested_additional_capabilities:                        |
|                                                             |
| hyper_threading:                                           |
|                                                             |
| support_mandatory: true                                    |
|                                                             |
| requested_additional_capability_name: hyper_threading   |
|                                                             |
| target_performance_parameters:                            |
|                                                             |
| hw:cpu_sockets : "2"                                       |
|                                                             |
| hw:cpu_threads : "2"                                       |
|                                                             |
| hw:cpu_cores : "2"                                         |
|                                                             |
| hw:cpu_threads_policy: "isolate"                          |
+-------------------------------------------------------------+

5. OVS+DPDK

Definitions of ovs_dpdk are necessary as one of
requested_additional_capabilities of one VUD node if that node
supports dpdk. Here is an example.

+------------------------------------------------------+
| topology_template:                                  |
|                                                      |
| node_templates:                                     |
|                                                      |
| vdu_vNat:                                           |
|                                                      |
| capabilities:                                        |
|                                                      |
| virtual_compute:                                    |
|                                                      |
| properties:                                          |
|                                                      |
| virtual_memory:                                     |
|                                                      |
| numa_enabled: true                                  |
|                                                      |
| virtual_mem_size: 2 GB                             |
|                                                      |
| requested_additional_capabilities:                 |
|                                                      |
| ovs_dpdk:                                           |
|                                                      |
| support_mandatory: true                             |
|                                                      |
| requested_additional_capability_name: ovs_dpdk   |
|                                                      |
| target_performance_parameters:                     |
|                                                      |
| sw:ovs_dpdk: "true"                                 |
+------------------------------------------------------+

NFV TOSCA Type Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^

tosca.capabilites.nfv.VirtualCompute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------+-----------------------------------------+
| **Shorthand Name**        | VirtualCompute                          |
+===========================+=========================================+
| **Type Qualified Name**   | tosca: VirtualCompute                   |
+---------------------------+-----------------------------------------+
| **Type URI**              | tosca.capabilities.nfv.VirtualCompute   |
+---------------------------+-----------------------------------------+
| **derived from**          | tosca.nodes.Root                        |
+---------------------------+-----------------------------------------+

Properties
^^^^^^^^^^

+-------------------------------------+------------+-----------------------------------------------------+---------------+---------------------------------------------------------+
| Name                                | Required   | Type                                                | Constraints   | Description                                             |
+=====================================+============+=====================================================+===============+=========================================================+
| request_additional_capabilities   | No         | tosca.datatypes.nfv.RequestedAdditionalCapability   |               | Describes additional capability for a particular VDU.   |
+-------------------------------------+------------+-----------------------------------------------------+---------------+---------------------------------------------------------+
| virtual_memory                     | yes        | tosca.datatypes.nfv.VirtualMemory                   |               | Describes virtual memory of the virtualized compute     |
+-------------------------------------+------------+-----------------------------------------------------+---------------+---------------------------------------------------------+
| virtual_cpu                        | yes        | tosca.datatypes.nfv.VirtualCpu                      |               | Describes virtual CPU(s) of the virtualized compute.    |
+-------------------------------------+------------+-----------------------------------------------------+---------------+---------------------------------------------------------+
+-------------------------------------+------------+-----------------------------------------------------+---------------+---------------------------------------------------------+
| name                                | yes        |                                                     |               |                                                         |
+-------------------------------------+------------+-----------------------------------------------------+---------------+---------------------------------------------------------+

Definition
^^^^^^^^^^

+-----------------------------------------------------------+
| tosca.capabilities.nfv.VirtualCompute:                    |
|                                                           |
| derived_from: tosca.capabilities.Root                    |
|                                                           |
| properties:                                               |
|                                                           |
| requested_additional_capabilities:                      |
|                                                           |
| type: map                                                 |
|                                                           |
| entry_schema:                                            |
|                                                           |
| type: tosca.datatypes.nfv.RequestedAdditionalCapability   |
|                                                           |
| required: false                                           |
|                                                           |
| virtual_memory:                                          |
|                                                           |
| type: tosca.datatypes.nfv.VirtualMemory                   |
|                                                           |
| required: true                                            |
|                                                           |
| virtual_cpu:                                             |
|                                                           |
| type: tosca.datatypes.nfv.VirtualCpu                      |
|                                                           |
| required: true                                            |
+-----------------------------------------------------------+

tosca.nodes.nfv.VDU.Compute
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The NFV Virtualization Deployment Unit (VDU) compute node type
represents a VDU entity which it describes the deployment and
operational behavior of a VNF component (VNFC), as defined by **[ETSI
NFV IFA011].**

+-----------------------+-------------------------------+
| Shorthand Name        | VDU.Compute                   |
+=======================+===============================+
| Type Qualified Name   | tosca:VDU.Compute             |
+-----------------------+-------------------------------+
| Type URI              | tosca.nodes.nfv.VDU.Compute   |
+-----------------------+-------------------------------+
| derived_from         | tosca.nodes.Compute           |
+-----------------------+-------------------------------+



Attributes
^^^^^^^^^^

None


Capabilities
^^^^^^^^^^^^

+-------------------------+-------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------+
| Name                    | Type                                            | Constraints   | Description                                                                                         |
+=========================+=================================================+===============+=====================================================================================================+
| virtual_compute        | tosca.capabilities.nfv.VirtualCompute           |               | Describes virtual compute resources capabilities.                                                   |
+-------------------------+-------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------+
| monitoring_parameter   | tosca.capabilities.nfv.Metric                   | None          | Monitoring parameter, which can be tracked for a VNFC based on this VDU                             |
|                         |                                                 |               |                                                                                                     |
|                         |                                                 |               | Examples include: memory-consumption, CPU-utilisation, bandwidth-consumption, VNFC downtime, etc.   |
+-------------------------+-------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------+
| Virtual_binding        | tosca.capabilities.nfv.VirtualBindable          |               | Defines ability of VirtualBindable                                                                  |
|                         |                                                 |               |                                                                                                     |
|                         | editor note: need to create a capability type   |               |                                                                                                     |
+-------------------------+-------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------+

Definition
^^^^^^^^^^

+-----------------------------------------------------------------------------------------------------+
| tosca.nodes.nfv.VDU.Compute:                                                                        |
|                                                                                                     |
| derived_from: tosca.nodes.Compute                                                                  |
|                                                                                                     |
| properties:                                                                                         |
|                                                                                                     |
| name:                                                                                               |
|                                                                                                     |
| type: string                                                                                        |
|                                                                                                     |
| required: true                                                                                      |
|                                                                                                     |
| description:                                                                                        |
|                                                                                                     |
| type: string                                                                                        |
|                                                                                                     |
| required: true                                                                                      |
|                                                                                                     |
| boot_order:                                                                                        |
|                                                                                                     |
| type: list # explicit index (boot index) not necessary, contrary to IFA011                          |
|                                                                                                     |
| entry_schema:                                                                                      |
|                                                                                                     |
| type: string                                                                                        |
|                                                                                                     |
| required: false                                                                                     |
|                                                                                                     |
| nfvi_constraints:                                                                                  |
|                                                                                                     |
| type: list                                                                                          |
|                                                                                                     |
| entry_schema:                                                                                      |
|                                                                                                     |
| type: string                                                                                        |
|                                                                                                     |
| required: false                                                                                     |
|                                                                                                     |
| configurable_properties:                                                                           |
|                                                                                                     |
| type: map                                                                                           |
|                                                                                                     |
| entry_schema:                                                                                      |
|                                                                                                     |
| type: tosca.datatypes.nfv.VnfcConfigurableProperties                                                |
|                                                                                                     |
| required: true                                                                                      |
|                                                                                                     |
| attributes:                                                                                         |
|                                                                                                     |
| private_address:                                                                                   |
|                                                                                                     |
| status: deprecated                                                                                  |
|                                                                                                     |
| public_address:                                                                                    |
|                                                                                                     |
| status: deprecated                                                                                  |
|                                                                                                     |
| networks:                                                                                           |
|                                                                                                     |
| status: deprecated                                                                                  |
|                                                                                                     |
| ports:                                                                                              |
|                                                                                                     |
| status: deprecated                                                                                  |
|                                                                                                     |
| capabilities:                                                                                       |
|                                                                                                     |
| virtual_compute:                                                                                   |
|                                                                                                     |
| type: tosca.capabilities.nfv.VirtualCompute                                                         |
|                                                                                                     |
| virtual_binding:                                                                                   |
|                                                                                                     |
| type: tosca.capabilities.nfv.VirtualBindable                                                        |
|                                                                                                     |
| #monitoring_parameter:                                                                             |
|                                                                                                     |
| # modeled as ad hoc (named) capabilities in VDU node template                                       |
|                                                                                                     |
| # for example:                                                                                      |
|                                                                                                     |
| #capabilities:                                                                                      |
|                                                                                                     |
| # cpu_load: tosca.capabilities.nfv.Metric                                                          |
|                                                                                                     |
| # memory_usage: tosca.capabilities.nfv.Metric                                                      |
|                                                                                                     |
| host: #Editor note: FFS. How this capabilities should be used in NFV Profile                        |
|                                                                                                     |
| type: `*tosca.capabilities.Container* <#DEFN_TYPE_CAPABILITIES_CONTAINER>`__                        |
|                                                                                                     |
| valid_source_types: [`*tosca.nodes.SoftwareComponent* <#DEFN_TYPE_NODES_SOFTWARE_COMPONENT>`__]   |
|                                                                                                     |
| occurrences: [0,UNBOUNDED]                                                                          |
|                                                                                                     |
| endpoint:                                                                                           |
|                                                                                                     |
| occurrences: [0,0]                                                                                  |
|                                                                                                     |
| os:                                                                                                 |
|                                                                                                     |
| occurrences: [0,0]                                                                                  |
|                                                                                                     |
| scalable: #Editor note: FFS. How this capabilities should be used in NFV Profile                    |
|                                                                                                     |
| type: `*tosca.capabilities.Scalable* <#DEFN_TYPE_CAPABILITIES_SCALABLE>`__                          |
|                                                                                                     |
| binding:                                                                                            |
|                                                                                                     |
| occurrences: [0,UNBOUND]                                                                            |
|                                                                                                     |
| requirements:                                                                                       |
|                                                                                                     |
| - virtual_storage:                                                                                 |
|                                                                                                     |
| capability: tosca.capabilities.nfv.VirtualStorage                                                   |
|                                                                                                     |
| relationship: tosca.relationships.nfv.VDU.AttachedTo                                                |
|                                                                                                     |
| node: tosca.nodes.nfv.VDU.VirtualStorage                                                            |
|                                                                                                     |
| occurences: [ 0, UNBOUNDED ]                                                                        |
|                                                                                                     |
| - local_storage: #For NFV Profile, this requirement is deprecated.                                 |
|                                                                                                     |
| occurrences: [0,0]                                                                                  |
|                                                                                                     |
| artifacts:                                                                                          |
|                                                                                                     |
| - sw_image:                                                                                        |
|                                                                                                     |
| file:                                                                                               |
|                                                                                                     |
| type: tosca.artifacts.nfv.SwImage                                                                   |
+-----------------------------------------------------------------------------------------------------+

Artifact
^^^^^^^^
+-----------+------------+-------------------------------+---------------+------------------------------------------------+
| Name      | Required   | Type                          | Constraints   | Description                                    |
+===========+============+===============================+===============+================================================+
| SwImage   | Yes        | tosca.artifacts.nfv.SwImage   |               | Describes the software image which is          |
|           |            |                               |               | directly realizing this virtual storage        |
+-----------+------------+-------------------------------+---------------+------------------------------------------------+


|image2|



tosca.nodes.nfv.Cpd
~~~~~~~~~~~~~~~~~~~

The TOSCA Cpd node represents network connectivity to a compute resource
or a VL as defined by [ETSI GS NFV-IFA 011]. This is an abstract type
used as parent for the various Cpd types.

+-----------------------+-----------------------+
| Shorthand Name        | Cpd                   |
+=======================+=======================+
| Type Qualified Name   | tosca:Cpd             |
+-----------------------+-----------------------+
| Type URI              | tosca.nodes.nfv.Cpd   |
+-----------------------+-----------------------+


Attributes
^^^^^^^^^^

+--------+------------+--------+---------------+---------------+
| Name   | Required   | Type   | Constraints   | Description   |
+========+============+========+===============+===============+
+--------+------------+--------+---------------+---------------+

Requirements
^^^^^^^^^^^^

None

Capabilities
^^^^^^^^^^^^

None

Definition
^^^^^^^^^^

+----------------------------------------------------------------------+
| tosca.nodes.nfv.Cpd:                                                 |
|                                                                      |
| derived_from: tosca.nodes.Root                                      |
|                                                                      |
| properties:                                                          |
|                                                                      |
| layer_protocol:                                                     |
|                                                                      |
| type:string                                                          |
|                                                                      |
| constraints:                                                         |
|                                                                      |
| - valid_values: [ethernet, mpls, odu2, ipv4, ipv6, pseudo_wire ]   |
|                                                                      |
| required:true                                                        |
|                                                                      |
| role: #Name in ETSI NFV IFA011 v0.7.3 cpRole                         |
|                                                                      |
| type:string                                                          |
|                                                                      |
| constraints:                                                         |
|                                                                      |
| - valid_values: [ root, leaf ]                                      |
|                                                                      |
| required:flase                                                       |
|                                                                      |
| description:                                                         |
|                                                                      |
| type: string                                                         |
|                                                                      |
| required: false                                                      |
|                                                                      |
| address_data:                                                       |
|                                                                      |
| type: list                                                           |
|                                                                      |
| entry_schema:                                                       |
|                                                                      |
| type: tosca.datatype.nfv.AddressData                                 |
|                                                                      |
| required:false                                                       |
+----------------------------------------------------------------------+

Additional Requirement
^^^^^^^^^^^^^^^^^^^^^^

None.

tosca.nodes.nfv.VduCpd
~~~~~~~~~~~~~~~~~~~~~~

The TOSCA node VduCpd represents a type of TOSCA Cpd node and describes
network connectivity between a VNFC instance (based on this VDU) and an
internal VL as defined by [ETSI GS NFV-IFA 011].

+-----------------------+--------------------------+
| Shorthand Name        | VduCpd                   |
+=======================+==========================+
| Type Qualified Name   | tosca: VduCpd            |
+-----------------------+--------------------------+
| Type URI              | tosca.nodes.nfv.VduCpd   |
+-----------------------+--------------------------+

Properties
^^^^^^^^^^


+-------------------------------+------------+------------------------------------------+---------------+----------------------------------------------------------+
| Name                          | Required   | Type                                     | Constraints   | Description                                              |
+===============================+============+==========================================+==========================================================================+
| bitrate_requirement           | no         | integer                                  |               | Bitrate requirement on this connection point.            |
+-------------------------------+------------+------------------------------------------+---------------+----------------------------------------------------------+
| virtual_network_interface_\ | no         | VirtualNetworkInterfaceRequirements      |               | Specifies requirements on a virtual network              |
| requirements                  |            |                                          |               | realising the CPs instantiated from this CPD             |
+-------------------------------+------------+------------------------------------------+---------------+----------------------------------------------------------+

Attributes
^^^^^^^^^^

None

Requirements
^^^^^^^^^^^^

+--------------------+------------+------------------------------------------+---------------+----------------------------------------------------------+
| Name               | Required   | Type                                     | Constraints   | Description                                              |
+====================+============+==========================================+===============+==========================================================+
| virtual_binding   | yes        | tosca.capabilities.nfv.VirtualBindable   |               | Describe the requirement for binding with VDU            |
+--------------------+------------+------------------------------------------+---------------+----------------------------------------------------------+
| virtual_link      | no         | tosca.capabilities.nfv.VirtualLinkable   |               | Describes the requirements for linking to virtual link   |
+--------------------+------------+------------------------------------------+---------------+----------------------------------------------------------+

Definition
^^^^^^^^^^

+----------------------------------------------------------------+
| tosca.nodes.nfv.VduCpd:                                        |
|                                                                |
| derived_from: tosca.nodes.nfv.Cpd                             |
|                                                                |
| properties:                                                    |
|                                                                |
| bitrate_requirement:                                          |
|                                                                |
| type: integer                                                  |
|                                                                |
| required:false                                                 |
|                                                                |
| virtual_network_interface_requirements                      |
|                                                                |
| type: list                                                     |
|                                                                |
| entry_schema:                                                 |
|                                                                |
| type: VirtualNetworkInterfaceRequirements                      |
|                                                                |
| required:false                                                 |
|                                                                |
| requirements:                                                  |
|                                                                |
| - virtual_link:                                               |
|                                                                |
| capability: tosca.capabilities.nfv.VirtualLinkable             |
|                                                                |
| relationship: tosca.relationships.nfv.VirtualLinksTo           |
|                                                                |
| node: tosca.nodes.nfv.VnfVirtualLinkDesc - virtual_binding:   |
|                                                                |
| capability: tosca.capabilities.nfv.VirtualBindable             |
|                                                                |
| relationship: tosca.relationships.nfv.VirtualBindsTo           |
|                                                                |
| node: tosca.nodes.nfv.VDU                                      |
+----------------------------------------------------------------+

tosca.nodes.nfv.VDU.VirtualStorage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The NFV VirtualStorage node type represents a virtual storage entity
which it describes the deployment and operational behavior of a virtual
storage resources, as defined by **[ETSI NFV IFA011].**

**[editor note]** open issue: should NFV profile use the current storage
model as described in YAML 1.1. Pending on Shitao proposal (see
NFVIFA(17)000110 discussion paper)

**[editor note]** new relationship type as suggested in Matt
presentation. Slide 8. With specific rules of “valid_target_type”

+---------------------------+--------------------------------------+
| **Shorthand Name**        | VirtualStorage                       |
+===========================+======================================+
| **Type Qualified Name**   | tosca: VirtualStorage                |
+---------------------------+--------------------------------------+
| **Type URI**              | tosca.nodes.nfv.VDU.VirtualStorage   |
+---------------------------+--------------------------------------+
| **derived_from**         | tosca.nodes.Root                     |
+---------------------------+--------------------------------------+

tosca.artifacts.nfv.SwImage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------+------------------------------------+
| **Shorthand Name**        | SwImage                            |
+===========================+====================================+
| **Type Qualified Name**   | tosca:SwImage                      |
+---------------------------+------------------------------------+
| **Type URI**              | tosca.artifacts.nfv.SwImage        |
+---------------------------+------------------------------------+
| **derived_from**         | tosca.artifacts.Deployment.Image   |
+---------------------------+------------------------------------+

Properties
^^^^^^^^^^

+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| Name                                     | Required   | Type               | Constraints   | Description                                                                                        |
+==========================================+============+====================+===============+====================================================================================================+
| name                                     | yes        | string             |               | Name of this software image                                                                        |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| version                                  | yes        | string             |               | Version of this software image                                                                     |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| checksum                                 | yes        | string             |               | Checksum of the software image file                                                                |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| container_format                        | yes        | string             |               | The container format describes the container file format in which software image is provided.      |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| disk_format                             | yes        | string             |               | The disk format of a software image is the format of the underlying disk image                     |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| min_disk                                | yes        | scalar-unit.size   |               | The minimal disk size requirement for this software image.                                         |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| min_ram                                 | no         | scalar-unit.size   |               | The minimal RAM requirement for this software image.                                               |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| Size                                     | yes        | scalar-unit.size   |               | The size of this software image                                                                    |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| sw_image                                | yes        | string             |               | A reference to the actual software image within VNF Package, or url.                               |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| operating_system                        | no         | string             |               | Identifies the operating system used in the software image.                                        |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| supported _virtualization_enviroment   | no         | list               |               | Identifies the virtualization environments (e.g. hypervisor) compatible with this software image   |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+

Definition
^^^^^^^^^^

+-----------------------------------------------------+
| tosca.artifacts.nfv.SwImage:                        |
|                                                     |
|   derived_from: tosca.artifacts.Deployment.Image   |
|                                                     |
|   properties or metadata:                           |
|                                                     |
|     #id:                                            |
|                                                     |
|       # node name                                   |
|                                                     |
|     name:                                           |
|                                                     |
|       type: string                                  |
|                                                     |
| required: true                                      |
|                                                     |
|     version:                                        |
|                                                     |
|       type: string                                  |
|                                                     |
| required: true                                      |
|                                                     |
|     checksum:                                       |
|                                                     |
|       type: string                                  |
|                                                     |
| required: true                                      |
|                                                     |
|     container_format:                              |
|                                                     |
|       type: string                                  |
|                                                     |
| required: true                                      |
|                                                     |
|     disk_format:                                   |
|                                                     |
|       type: string                                  |
|                                                     |
| required: true                                      |
|                                                     |
|     min_disk:                                      |
|                                                     |
|       type: scalar-unit.size # Number               |
|                                                     |
| required: true                                      |
|                                                     |
|     min_ram:                                       |
|                                                     |
|       type: scalar-unit.size # Number               |
|                                                     |
| required: false                                     |
|                                                     |
|     size:                                           |
|                                                     |
|       type: scalar-unit.size # Number               |
|                                                     |
| required: true                                      |
|                                                     |
|     sw_image:                                      |
|                                                     |
|       type: string                                  |
|                                                     |
| required: true                                      |
|                                                     |
|     operating_system:                              |
|                                                     |
|       type: string                                  |
|                                                     |
| required: false                                     |
|                                                     |
|     supported_virtualisation_environments:        |
|                                                     |
|       type: list                                    |
|                                                     |
|       entry_schema:                                |
|                                                     |
|         type: string                                |
|                                                     |
| required: false                                     |
+-----------------------------------------------------+

vNAT Example
^^^^^^^^^^^^

openovnf__vOpenNAT.yaml
~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+
| imports:                                                    |
|                                                             |
| - openonfv__tosca.capabilities.Scalable.yaml              |
|                                                             |
| - openonfv__tosca.capabilities.nfv.Metric.yaml            |
|                                                             |
| - openonfv__tosca.capabilities.network.Bindable.yaml      |
|                                                             |
| - openonfv__tosca.capabilities.Attachment.yaml            |
|                                                             |
| - openonfv__tosca.capabilities.nfv.VirtualBindable.yaml   |
|                                                             |
| - openonfv__tosca.requirements.nfv.VirtualStorage.yaml    |
|                                                             |
| - openonfv__tosca.nodes.nfv.VDU.VirtualStorage.yaml       |
|                                                             |
| - openonfv__tosca.relationships.nfv.VirtualBindsTo.yaml   |
|                                                             |
| - openonfv__tosca.nodes.nfv.VDU.Compute.yaml              |
|                                                             |
| - openonfv__tosca.artifacts.nfv.SwImage.yaml              |
|                                                             |
| - openonfv__tosca.capabilities.nfv.VirtualCompute.yaml    |
|                                                             |
| - openonfv__tosca.capabilities.Container.yaml             |
|                                                             |
| - openonfv__tosca.capabilities.nfv.VirtualStorage.yaml    |
|                                                             |
| - openonfv__tosca.requirements.nfv.VirtualBinding.yaml    |
|                                                             |
| - openovnf__tosca.nodes.nfv.VNF.vOpenNAT.yaml             |
|                                                             |
| - openonfv__tosca.capabilities.Endpoint.Admin.yaml        |
|                                                             |
| - openonfv__tosca.capabilities.OperatingSystem.yaml       |
|                                                             |
| - openonfv__tosca.nodes.nfv.VduCpd.yaml                   |
|                                                             |
| - openonfv__tosca.relationships.nfv.VDU.AttachedTo.yaml   |
|                                                             |
| metadata:                                                   |
|                                                             |
| vnfProductName: openNAT                                     |
|                                                             |
| vnfdVersion: 1.0.0                                          |
|                                                             |
| vnfProvider: intel                                          |
|                                                             |
| vnfmInfo: GVNFM                                             |
|                                                             |
| csarVersion: 1.0.0                                          |
|                                                             |
| vnfdId: openNAT-1.0                                         |
|                                                             |
| csarProvider: intel                                         |
|                                                             |
| vnfProductInfoDescription: openNAT                          |
|                                                             |
| version: 1.0.0                                              |
|                                                             |
| csarType: NFAR                                              |
|                                                             |
| vendor: intel                                               |
|                                                             |
| localizationLanguage: '[english, chinese]'                  |
|                                                             |
| id: openNAT-1.0                                             |
|                                                             |
| defaultLocalizationLanguage: english                        |
|                                                             |
| vnfProductInfoName: openNAT                                 |
|                                                             |
| vnfSoftwareVersion: 1.0.0                                   |
|                                                             |
| topology_template:                                         |
|                                                             |
| node_templates:                                            |
|                                                             |
| vdu_vNat:                                                  |
|                                                             |
| artifacts:                                                  |
|                                                             |
| vNatVNFImage:                                               |
|                                                             |
| file: /swimages/xenial-snat.qcow2                           |
|                                                             |
| type: tosca.artifacts.nfv.SwImage                           |
|                                                             |
| properties:                                                 |
|                                                             |
| name: vNatVNFImage                                          |
|                                                             |
| version: "1.0"                                              |
|                                                             |
| checksum: "5000"                                            |
|                                                             |
| container_format: bare                                     |
|                                                             |
| disk_format: qcow2                                         |
|                                                             |
| min_disk: 10 GB                                            |
|                                                             |
| min_ram: 1 GB                                              |
|                                                             |
| size: 10 GB                                                 |
|                                                             |
| sw_image: /swimages/xenial-snat.qcow2                      |
|                                                             |
| operating_system: unbantu                                  |
|                                                             |
| attributes:                                                 |
|                                                             |
| tosca_name: vdu_vNat                                      |
|                                                             |
| capabilities:                                               |
|                                                             |
| virtual_compute:                                           |
|                                                             |
| properties:                                                 |
|                                                             |
| virtual_memory:                                            |
|                                                             |
| numa_enabled: true                                         |
|                                                             |
| virtual_mem_size: 2 GB                                    |
|                                                             |
| requested_additional_capabilities:                        |
|                                                             |
| numa:                                                       |
|                                                             |
| support_mandatory: true                                    |
|                                                             |
| requested_additional_capability_name: numa               |
|                                                             |
| target_performance_parameters:                            |
|                                                             |
| hw:numa_nodes: "2"                                         |
|                                                             |
| hw:numa_cpus.0: "0,1"                                      |
|                                                             |
| hw:numa_mem.0: "1024"                                      |
|                                                             |
| hw:numa_cpus.1: "2,3,4,5"                                  |
|                                                             |
| hw:numa_mem.1: "1024"                                      |
|                                                             |
| hyper_threading:                                           |
|                                                             |
| support_mandatory: true                                    |
|                                                             |
| requested_additional_capability_name: hyper_threading   |
|                                                             |
| target_performance_parameters:                            |
|                                                             |
| hw:cpu_sockets : "2"                                       |
|                                                             |
| hw:cpu_threads : "2"                                       |
|                                                             |
| hw:cpu_cores : "2"                                         |
|                                                             |
| hw:cpu_threads_policy: "isolate"                          |
|                                                             |
| ovs_dpdk:                                                  |
|                                                             |
| support_mandatory: true                                    |
|                                                             |
| requested_additional_capability_name: ovs_dpdk          |
|                                                             |
| target_performance_parameters:                            |
|                                                             |
| sw:ovs_dpdk: "true"                                        |
|                                                             |
| virtual_cpu:                                               |
|                                                             |
| cpu_architecture: X86                                      |
|                                                             |
| num_virtual_cpu: 2                                        |
|                                                             |
| properties:                                                 |
|                                                             |
| configurable_properties:                                   |
|                                                             |
| test:                                                       |
|                                                             |
| additional_vnfc_configurable_properties:                 |
|                                                             |
| aaa: 1                                                      |
|                                                             |
| name: vNat                                                  |
|                                                             |
| descrption: the virtual machine of vNat                     |
|                                                             |
| boot_order:                                                |
|                                                             |
| - vNAT_Storage                                             |
|                                                             |
| requirements:                                               |
|                                                             |
| - virtual_storage:                                         |
|                                                             |
| capability: virtual_storage                                |
|                                                             |
| node: vNAT_Storage                                         |
|                                                             |
| relationship:                                               |
|                                                             |
| properties:                                                 |
|                                                             |
| location: /mnt/volume_0                                    |
|                                                             |
| type: tosca.relationships.nfv.VDU.AttachedTo                |
|                                                             |
| - local_storage:                                           |
|                                                             |
| node: tosca.nodes.Root                                      |
|                                                             |
| type: tosca.nodes.nfv.VDU.Compute                           |
|                                                             |
| SRIOV_Port:                                                |
|                                                             |
| attributes:                                                 |
|                                                             |
| tosca_name: SRIOV_Port                                    |
|                                                             |
| properties:                                                 |
|                                                             |
| virtual_network_interface_requirements:                  |
|                                                             |
| - name: sriov                                               |
|                                                             |
| support_mandatory: false                                   |
|                                                             |
| description: sriov                                          |
|                                                             |
| requirement:                                                |
|                                                             |
| SRIOV: true                                                 |
|                                                             |
| role: root                                                  |
|                                                             |
| description: sriov port                                     |
|                                                             |
| layer_protocol: ipv4                                       |
|                                                             |
| requirements:                                               |
|                                                             |
| - virtual_binding:                                         |
|                                                             |
| capability: virtual_binding                                |
|                                                             |
| node: vdu_vNat                                             |
|                                                             |
| relationship:                                               |
|                                                             |
| type: tosca.relationships.nfv.VirtualBindsTo                |
|                                                             |
| - virtual_link:                                            |
|                                                             |
| node: tosca.nodes.Root                                      |
|                                                             |
| type: tosca.nodes.nfv.VduCpd                                |
|                                                             |
| vNAT_Storage:                                              |
|                                                             |
| attributes:                                                 |
|                                                             |
| tosca_name: vNAT_Storage                                  |
|                                                             |
| properties:                                                 |
|                                                             |
| id: vNAT_Storage                                           |
|                                                             |
| size_of_storage: 10 GB                                    |
|                                                             |
| rdma_enabled: false                                        |
|                                                             |
| type_of_storage: volume                                   |
|                                                             |
| type: tosca.nodes.nfv.VDU.VirtualStorage                    |
|                                                             |
| substitution_mappings:                                     |
|                                                             |
| requirements:                                               |
|                                                             |
| sriov_plane:                                               |
|                                                             |
| - SRIOV_Port                                               |
|                                                             |
| - virtual_link                                             |
|                                                             |
| node_type: tosca.nodes.nfv.VNF.vOpenNAT                    |
|                                                             |
| tosca_definitions_version: tosca_simple_yaml_1_0      |
+-------------------------------------------------------------+

openonfv__tosca.nodes.nfv.VDU.VirtualStorage.yaml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------+
| imports:                                                   |
|                                                            |
| - openonfv__tosca.capabilities.nfv.VirtualStorage.yaml   |
|                                                            |
| node_types:                                               |
|                                                            |
| tosca.nodes.nfv.VDU.VirtualStorage:                        |
|                                                            |
| capabilities:                                              |
|                                                            |
| virtual_storage:                                          |
|                                                            |
| type: tosca.capabilities.nfv.VirtualStorage                |
|                                                            |
| derived_from: tosca.nodes.Root                            |
|                                                            |
| properties:                                                |
|                                                            |
| id:                                                        |
|                                                            |
| type: string                                               |
|                                                            |
| size_of_storage:                                         |
|                                                            |
| type: string                                               |
|                                                            |
| rdma_enabled:                                             |
|                                                            |
| required: false                                            |
|                                                            |
| type: boolean                                              |
|                                                            |
| type_of_storage:                                         |
|                                                            |
| type: string                                               |
|                                                            |
| tosca_definitions_version: tosca_simple_yaml_1_0     |
+------------------------------------------------------------+

openonfv__tosca.nodes.nfv.VduCpd.yaml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+
| data_types:                                                    |
|                                                                 |
| tosca.datatypes.nfv.L3AddressData:                              |
|                                                                 |
| properties:                                                     |
|                                                                 |
| number_of_ip_address:                                        |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: integer                                                   |
|                                                                 |
| ip_address_assignment:                                        |
|                                                                 |
| type: boolean                                                   |
|                                                                 |
| ip_address_type:                                              |
|                                                                 |
| constraints:                                                    |
|                                                                 |
| - valid_values:                                                |
|                                                                 |
| - ipv4                                                          |
|                                                                 |
| - ipv6                                                          |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: string                                                    |
|                                                                 |
| floating_ip_activated:                                        |
|                                                                 |
| type: string                                                    |
|                                                                 |
| tosca.datatypes.nfv.VirtualNetworkInterfaceRequirements:        |
|                                                                 |
| properties:                                                     |
|                                                                 |
| name:                                                           |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: string                                                    |
|                                                                 |
| support_mandatory:                                             |
|                                                                 |
| type: boolean                                                   |
|                                                                 |
| description:                                                    |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: string                                                    |
|                                                                 |
| requirement:                                                    |
|                                                                 |
| entry_schema:                                                  |
|                                                                 |
| type: string                                                    |
|                                                                 |
| type: map                                                       |
|                                                                 |
| tosca.datatype.nfv.AddressData:                                 |
|                                                                 |
| properties:                                                     |
|                                                                 |
| address_type:                                                  |
|                                                                 |
| constraints:                                                    |
|                                                                 |
| - valid_values:                                                |
|                                                                 |
| - mac_address                                                  |
|                                                                 |
| - ip_address                                                   |
|                                                                 |
| type: string                                                    |
|                                                                 |
| l2_address_data:                                              |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: tosca.datatypes.nfv.L2AddressData                         |
|                                                                 |
| l3_address_data:                                              |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: tosca.datatypes.nfv.L3AddressData                         |
|                                                                 |
| tosca.datatypes.nfv.L2AddressData: {}                           |
|                                                                 |
| imports:                                                        |
|                                                                 |
| - openonfv__tosca.requirements.nfv.VirtualBinding.yaml        |
|                                                                 |
| - openonfv__tosca.requirements.nfv.VirtualBinding.yaml        |
|                                                                 |
| node_types:                                                    |
|                                                                 |
| tosca.nodes.nfv.VduCpd:                                         |
|                                                                 |
| derived_from: tosca.nodes.Root                                 |
|                                                                 |
| properties:                                                     |
|                                                                 |
| virtual_network_interface_requirements:                      |
|                                                                 |
| entry_schema:                                                  |
|                                                                 |
| type: tosca.datatypes.nfv.VirtualNetworkInterfaceRequirements   |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: list                                                      |
|                                                                 |
| role:                                                           |
|                                                                 |
| constraints:                                                    |
|                                                                 |
| - valid_values:                                                |
|                                                                 |
| - root                                                          |
|                                                                 |
| - leaf                                                          |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: string                                                    |
|                                                                 |
| bitrate_requirement:                                           |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: integer                                                   |
|                                                                 |
| description:                                                    |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: string                                                    |
|                                                                 |
| layer_protocol:                                                |
|                                                                 |
| constraints:                                                    |
|                                                                 |
| - valid_values:                                                |
|                                                                 |
| - ethernet                                                      |
|                                                                 |
| - mpls                                                          |
|                                                                 |
| - odu2                                                          |
|                                                                 |
| - ipv4                                                          |
|                                                                 |
| - ipv6                                                          |
|                                                                 |
| - pseudo_wire                                                  |
|                                                                 |
| type: string                                                    |
|                                                                 |
| address_data:                                                  |
|                                                                 |
| entry_schema:                                                  |
|                                                                 |
| type: tosca.datatype.nfv.AddressData                            |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: list                                                      |
|                                                                 |
| requirements:                                                   |
|                                                                 |
| - virtual_binding:                                             |
|                                                                 |
| capability: tosca.capabilities.nfv.VirtualBindable              |
|                                                                 |
| occurrences:                                                    |
|                                                                 |
| - 0                                                             |
|                                                                 |
| - UNBOUNDED                                                     |
|                                                                 |
| - virtual_link:                                                |
|                                                                 |
| capability: tosca.capabilities.nfv.VirtualBindable              |
|                                                                 |
| occurrences:                                                    |
|                                                                 |
| - 0                                                             |
|                                                                 |
| - UNBOUNDED                                                     |
|                                                                 |
| tosca_definitions_version: tosca_simple_yaml_1_0          |
+-----------------------------------------------------------------+

.. |image1| image:: Image1.png
   :width: 5.76806in
   :height: 4.67161in
.. |image2| image:: Image2.png
   :width: 5.40486in
   :height: 2.46042in


b. Heat
-------

General Guidelines
^^^^^^^^^^^^^^^^^^

YAML Format
^^^^^^^^^^^^^

Heat Orchestration Templates must use valid YAML. YAML (YAML Ain't
Markup Language) is a human friendly data serialization standard for all
programming languages. See http://www.yaml.org/.

Heat Orchestration Template Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Heat Orchestration templates must be defined in YAML.

YAML rules include:

-  Tabs are NOT allowed, use spaces ONLY.

-  You MUST indent your properties and lists with 1 or more spaces.

-  All Resource IDs and resource property parameters are case-sensitive.
   (e.g., "ThIs", is not the same as "thiS")

Heat Orchestration Template Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Heat Orchestration template structure follows the following format, as
defined by OpenStack at
https://docs.openstack.org/developer/heat/template_guide/hot_spec.html.

.. code-block:: yaml

 heat_template_version: <date>

 description:
   # a description of the template

 parameter_groups:
   # a declaration of input parameter groups and order

 parameters:
   # declaration of input parameters

 resources:
   # declaration of template resources

 outputs:
   # declaration of output parameters

 conditions:
   # declaration of conditions


Heat Orchestration templates for ONAP must contain the following
sections:

-  heat_template_version:

-  description:

-  parameters:

-  resources:

Heat Orchestration templates for ONAP may contain the following
sections:

-  parameter_groups:

-  outputs:

heat_template_version
^^^^^^^^^^^^^^^^^^^^^^^

This section is ONAP mandatory. The heat_template_version must be set
to a date that is supported by the OpenStack environment.

description
^^^^^^^^^^^

This ONAP mandatory section allows for a description of the template.

parameter_groups
^^^^^^^^^^^^^^^^^

This ONAP optional section allows for specifying how the input
parameters should be grouped and the order to provide the parameters in.

parameters
^^^^^^^^^^

The parameter section is ONAP mandatory. This section allows for
specifying input parameters that have to be provided when instantiating
the template. Each parameter is specified in a separated nested block
with the name of the parameters defined in the first line and additional
attributes (e.g., type, label) defined as nested elements.

The Pre-Amsterdam VNF Validation Program (i.e., ICE Project) process
requires all parameters declared in a template to be used in a resource
with the exception of the parameters for the OS::Nova::Server property
availability_zone. See `Property: availability_zone`_. for more details on
availability_zone.

.. code-block:: yaml

 parameters:
   <param name>:
     type: <string | number | json | comma_delimited_list | boolean>
     label: <human-readable name of the parameter>
     description: <description of the parameter>
     default: <default value for parameter>
     hidden: <true | false>
     constraints:
       <parameter constraints>
     immutable: <true | false>

-  param name:

   -  The name of the parameter.

   -  ONAP requires that the param name must contain only alphanumeric
      characters and “_” underscores. Special characters must not be
      used.

-  type:

   -  The type of the parameter. Supported types are string, number,
      comma_delimited_list, json and boolean.

   -  This attribute must be provided per the OpenStack Heat
      Orchestration Template standard.

-  label:

   -  A human readable name for the parameter.

   -  This attribute is optional.

-  description:

   -  A human readable description for the parameter.

   -  This attribute is ONAP mandatory; it must be provided. (Note that
      this attribute is OpenStack optional.)

-  default:

   -  A default value for the parameter.

   -  ONAP does not support this attribute; it *must not* be provided in
      the Heat Orchestration Template. If a parameter has a default
      value, it must be provided in the environment file. (Note that
      this attribute is OpenStack optional.)

-  hidden:

   -  Defines whether the parameters should be hidden when a user
      requests information about a stack created from the template. This
      attribute can be used to hide passwords specified as parameters.

   -  This attribute is optional and defaults to false.

-  constraints:

   -  A list of constraints to apply. The constraints block of a
      parameter definition defines additional validation constraints
      that apply to the value of the parameter. The parameter values
      provided in the Heat Orchestration Template are validated against
      the constraints at instantiation time. The constraints are defined
      as a list with the following syntax

    constraints:

    - <constraint type>: <constraint definition>

    description: <constraint description>

-  constraint type: Type of constraint to apply.

-  constraint definition: The actual constraint, depending on the
   constraint type.

-  description: A description of the constraint. The text is presented
   to the user when the value the user defines violates the constraint.
   If omitted, a default validation message is presented to the user.
   This attribute is optional.

-  When the parameter type is set to number, the Heat Orchestration
   Template uploaded into ONAP must have constraints for range or
   allowed_values.

   -  range: The range constraint applies to parameters of type number.
      It defines a lower and upper limit for the numeric value of the
      parameter. The syntax of the range constraint is

    range: { min: <lower limit>, max: <upper limit> }

    It is possible to define a range constraint with only a lower limit
    or an upper limit.

-  allowed_values: The allowed_values constraint applies to parameters
   of type string or number. It specifies a set of possible values for a
   parameter. At deployment time, the user-provided value for the
   respective parameter must match one of the elements of the list. The
   syntax of the allowed_values constraint is

    allowed_values: [ <value>, <value>, ... ]

    Alternatively, the following YAML list notation can be used

    allowed_values:

    - <value>

    - <value>

    - ...

-  Other <constraint type> are optional, they may be used (e.g., length,
   modulo, allowed_pattern, custom_constraint, allowed_values (for
   string types))

-  Note that constrains must not be defined for any parameter enumerated
   in a nested heat template.

-  Some ONAP parameters must never have constraints defined. See `ONAP Resource ID and Parameter Naming Convention`_ for the use cases where these exceptions exist.

-  immutable:

   -  Defines whether the parameter is updatable. Stack update fails, if
      this is set to true and the parameter value is changed.

   -  This attribute is optional and defaults to false.

resources
^^^^^^^^^

This section is ONAP mandatory; it must be provided. This section
contains the declaration of the single resources of the template. This
section with at least one resource must be defined in the Heat
Orchestration Template, or the template would not create any resources
when being instantiated.

Each resource is defined as a separate block in the resources section
with the following syntax.

.. code-block:: yaml

 resources:
   <resource ID>:
     type: <resource type>
     properties:
       <property name>: <property value>
     metadata:
       <resource specific metadata>
     depends_on: <resource ID or list of ID>
     update_policy: <update policy>
     deletion_policy: <deletion policy>
     external_id: <external resource ID>
     condition: <condition name or expression or boolean>

-  resource ID

   -  A resource ID that must be unique within the resources section of
      the Heat Orchestration Template.

   -  ONAP requires that the resource ID must be unique across all Heat
      Orchestration Templates that compose the VNF. This requirement
      also applies when a VNF is composed of more than one Heat
      Orchestration Template (see ONAP VNF Modularity Overview).

   -  The naming convention for a resource ID is provided in `Resource IDs`_.

-  type

   -  The resource type, such as OS::Nova::Server or OS::Neutron::Port.
      Note that the type may specify a nested heat file. This attribute
      is required.

-  properties

   -  A list of resource-specific properties. The property value can be
      provided in place, or via a function (e.g., Intrinsic functions). This section is optional.

   -  The naming convention for property parameters is provided in `ONAP Resource ID and Parameter Naming Convention`_.

-  metadata

   -  Resource-specific metadata. This section is optional, except for
      the resource OS::Nova::Server. See `Resource:  OS::Nova::Server - Parameters`_.

-  depends_on

   -  Dependencies of the resource on one or more resources of the
      template. This attribute is optional. See `Resource Data Synchronization`_ for additional details.

-  update_policy

   -  Update policy for the resource, in the form of a nested
      dictionary. Whether update policies are supported and what the
      exact semantics are depends on the type of the current resource.
      This attribute is optional.

-  deletion_policy

   -  Deletion policy for the resource. The allowed deletion policies
      are Delete, Retain, and Snapshot. Beginning with
      heat_template_version 2016-10-14, the lowercase equivalents
      delete, retain, and snapshot are also allowed. This attribute is
      optional; the default policy is to delete the physical resource
      when deleting a resource from the stack.

-  external_id

   -  Allows for specifying the resource_id for an existing external
      (to the stack) resource. External resources cannot depend on other
      resources, but we allow other resources to depend on external
      resource. This attribute is optional. Note: when this is
      specified, properties will not be used for building the resource
      and the resource is not managed by Heat. This is not possible to
      update that attribute. Also, resource won’t be deleted by heat
      when stack is deleted.

-  condition

   -  Condition for the resource. The condition decides whether to
      create the resource or not. This attribute is optional.

outputs
^^^^^^^

This ONAP optional section allows for specifying output parameters
available to users once the template has been instantiated. If the
section is specified, it will need to adhere to specific requirements.
See `ONAP Parameter Classifications Overview`_ and `ONAP Output Parameter Names`_ for additional details.

Environment File Format
^^^^^^^^^^^^^^^^^^^^^^^^

The environment file is a yaml text file.
(https://docs.openstack.org/developer/heat/template_guide/environment.html)

The environment file can contain the following sections:

-  parameters: A list of key/value pairs.

-  resource_registry: Definition of custom resources.

-  parameter_defaults: Default parameters passed to all template
   resources.

-  encrypted_parameters: List of encrypted parameters.

-  event_sinks: List of endpoints that would receive stack events.

-  parameter_merge_strategies: Merge strategies for merging parameters
   and parameter defaults from the environment file.

Environment files for ONAP must contain the following sections:

-  parameters:

Environment files for ONAP may contain the following sections:

-  resource_registry:

-  parameter_defaults:

-  encrypted_parameters:

-  event_sinks:

-  parameter_merge_strategies:

The use of an environment file in OpenStack is optional. In ONAP, it is
mandatory. A Heat Orchestration Template uploaded to ONAP must have a
corresponding environment file, even if no parameters are enumerated in
the mandatory parameter section.

(Note that ONAP, the open source version of ONAP, does not
programmatically enforce the use of an environment file.)

SDC Treatment of Environment Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parameter values enumerated in the environment file are used by SDC as
the default value. However, the SDC user may use the SDC GUI to
overwrite the default values in the environment file.

SDC generates a new environment file for distribution to MSO based on
the uploaded environment file and the user provided GUI updates. The
user uploaded environment file is discarded when the new file is
created.

ONAP has requirements for what parameters must be enumerated in the
environment file and what parameter must not be enumerated in the
environment file. See `ONAP Parameter Classifications Overview`_ and `ONAP Resource ID and Parameter Naming Convention`_ for more details.

Nested Heat Orchestration Templates Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP supports nested Heat Orchestration Templates per OpenStack
specifications.

A Base Module may utilize nested templates.

An Incremental Module may utilize nested templates.

A Cinder Volume Module may utilize nested templates.

A nested template must not define parameter constraints in the parameter
definition section.

Nested templates may be suitable for larger VNFs that contain many
repeated instances of the same VM type(s). A common usage pattern is to
create a nested template for each VM type along with its supporting
resources. The Heat Orchestration Template may then reference these
nested templates either statically (by repeated definition) or
dynamically (via OS::Heat::ResourceGroup).

See `Nested Heat Templates`_ for additional details.

ONAP Heat Orchestration Template Filenames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to enable ONAP to understand the relationship between Heat
files, the following Heat file naming convention must be utilized.

In the examples below, <text> represents any alphanumeric string that
must not contain any special characters and must not contain the word
“base”.

Base Modules
~~~~~~~~~~~~

The file name for the base module must include “base” in the filename
and must match one of the following options:

-  base_<text>.y[a]ml

-  <text>_base.y[a]ml

-  base.y[a]ml

-  <text>_base_<text>.y[a]ml

The base module’s corresponding environment file must be named identical
to the base module with “.y[a]ml” replaced with “.env”.

Incremental Modules
~~~~~~~~~~~~~~~~~~~

There is no explicit naming convention for the incremental modules. As
noted above, <text> represents any alphanumeric string that must not
contain any special characters and must not contain the word “base”.

-  <text>.y[a]ml

The incremental module’s corresponding environment file must be named
identical to the incremental module with “.y[a]ml” replaced with “.env”.

To clearly identify the incremental module, it is recommended to use the
following naming options for modules:

-  module_<text>.y[a]ml

-  <text>_module.y[a]ml

-  module.y[a]ml

Cinder Volume Modules
~~~~~~~~~~~~~~~~~~~~~

The file name for the Cinder volume module must be named the same as the
corresponding module it is supporting (base module or incremental
module) with “_volume” appended

-  <base module name>_volume.y[a]ml

-  <incremental module name>_volume.y[a]ml

The volume module’s corresponding environment file must be named
identical to the volume module with “.y[a]ml” replaced with “.env”.

Nested Heat file
~~~~~~~~~~~~~~~~

There is no explicit naming convention for nested Heat files with the
following exceptions; the name should contain “nest”. As noted above,
<text> represents any alphanumeric string that must not contain any
special characters and must not contain the word “base”.

-  <text>.y[a]m

Nested Heat files do not have corresponding environment files, per
OpenStack specifications. All parameter values associated with the
nested heat file must be passed in as properties in the resource
definition defined in the parent heat template.

ONAP Parameter Classifications Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order for ONAP to support workflow automation, Heat Orchestration
Template resource property parameters must adhere to specific naming
conventions and requirements.

Broadly, ONAP categorizes parameters into four categories:

1. ONAP metadata parameters

2. Instance specific parameters

3. Constant parameters

4. Output parameters.

ONAP Metadata Parameters
~~~~~~~~~~~~~~~~~~~~~~~~

There are both mandatory and optional ONAP metadata parameters
associated with the resource OS::Nova::Server.

-  ONAP metadata parameters must not have parameter constraints defined.

-  Both mandatory and optional (if specified) ONAP metadata parameter
   names must follow the ONAP metadata parameter naming convention.

`Resource:  OS::Nova::Server – Metadata Parameters`_ provides more details on the metadata parameters.

Instance specific parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The instance specific parameters are VNF instance specific. The value of
the parameter will be different for every instance of a VNF (e.g., IP
address). The instance specific parameters are subdivided into two
categories: **ONAP Orchestration Parameters** and **VNF Orchestration
Parameters**

ONAP Orchestration Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP Orchestration Parameters are per instance parameters where the
value is assigned via ONAP automation. (Note that in some cases,
automation is currently not available and the value is loaded into ONAP
prior to instantiation.)

-  ONAP orchestration parameters must not be enumerated in the
   environment file.

-  When the ONAP orchestration parameter type is set to number, the
   parameter must have constraints for range and/or allowed_values.

-  Parameter constraints for ONAP orchestration parameters are optional
   for all parameter types other than number. If constraints are
   specified, they must adhere to the OpenStack specifications.

-  The ONAP orchestration parameter names must follow the ONAP
   orchestration parameter naming convention. `ONAP Resource ID and Parameter Naming Convention`_ provides
   additional details.

VNF Orchestration Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

VNF Orchestration Parameters are per instance parameters where the
values are assigned manually. They are not supported by ONAP automation.
The per instance values are loaded into ONAP prior to VNF instantiation.

-  VNF orchestration parameters must not be enumerated in the
   environment file.

-  When the VNF orchestration parameter type is set to number, the
   parameter must have constraints for range or allowed_values.

-  Parameter constraints for VNF orchestration parameters are optional
   for all parameter types other than number. If constraints are
   specified, they must adhere to the OpenStack specifications.

-  The VNF orchestration parameter names should follow the VNF
   orchestration parameter naming convention. `ONAP Resource ID and Parameter Naming Convention`_ provides
   additional details.

Constant Parameters
~~~~~~~~~~~~~~~~~~~

The constant parameters are parameters that remain constant across many
VNF instances (e.g., image, flavor). The constant parameters are
subdivided into two categories: **ONAP Constant Parameters** and **VNF Constant Parameters.**

ONAP Constant Parameters
^^^^^^^^^^^^^^^^^^^^^^^^

-  ONAP Constant Parameters must be enumerated in the environment file.
   These parameter values are not assigned by ONAP.

-  When the ONAP Constant Parameter type is set to number, the parameter
   must have constraints for range and/or allowed_values.

-  Parameter constraints for ONAP constant parameters are optional for
   all parameter types other than number. If constraints are specified,
   they must adhere to the OpenStack specifications.

-  The ONAP Constant Parameter names must follow the ONAP orchestration
   parameter naming convention. `ONAP Resource ID and Parameter Naming Convention`_ provides additional details.

VNF Constant Parameters
^^^^^^^^^^^^^^^^^^^^^^^

-  VNF Constant Parameters must be enumerated in the environment file.
   These parameter values are not assigned by ONAP.

-  When the VNF Constant Parameters type is set to number, the parameter
   must have constraints for range and/or allowed_values.

-  Parameter constraints for ONAP constant parameters are optional for
   all parameter types other than number. If constraints are specified,
   they must adhere to the OpenStack specifications.

-  The VNF Constant Parameters names should follow the ONAP
   orchestration parameter naming convention. `ONAP Resource ID and Parameter Naming Convention`_ provides
   additional details.

Output Parameters
~~~~~~~~~~~~~~~~~

The output parameters are parameters defined in the output section of a
Heat Orchestration Template. The ONAP output parameters are subdivided
into three categories:

1. ONAP Base Module Output Parameters

2. ONAP Volume Module Output Parameters

3. ONAP Predefined Output Parameters.

ONAP Base Module Output Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP Base Module Output Parameters are declared in the outputs: section
of the base module Heat Orchestration Template. A Base Module Output
Parameter is available as an input parameter (i.e., declared in the
“parameters:” section) to all incremental modules in the VNF.

-  A Base Module Output Parameter may be used as an input parameter in
   an incremental module.

-  The Output parameter name and type must match the input parameter
   name and type unless the Output parameter is of the type
   comma_delimited_list.

   -  If the Output parameter has a comma_delimited_list value (e.g.,
      a collection of UUIDs from a Resource Group), then the
      corresponding input parameter must be declared as type json and
      not a comma_delimited_list, which is actually a string value
      with embedded commas.

-  When a Base Module Output Parameter is declared as an input parameter
   in an incremental module Heat Orchestration Template, parameter
   constraints must not be declared.

Additional details on ONAP Base Module Output Parameters are provided in
`ONAP Output Parameter Names`_ and ONAP VNF Modularity.

ONAP Volume Module Output Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The volume template output parameters are only available for the module
(base or add on) that the volume is associated with.

-  ONAP Volume Module Output Parameters are declared in the “outputs:”
   section of the Cinder volume module Heat Orchestration Template

-  An ONAP Volume Module Output Parameter is available as an input
   parameter (i.e., declared in the parameters: section) only for the
   module (base or incremental) that the Cinder volume module is
   associated with. The Output parameter name and type must match the
   input parameter name and type unless the Output parameter is of the
   type comma_delimited_list.

-  If the Output parameter has a comma_delimited_list value (e.g., a
   collection of UUIDs from a Resource Group), then the corresponding
   input parameter must be declared as type json and not a
   comma_delimited_list, which is actually a string value with
   embedded commas.

-  When an ONAP Volume Module Output Parameter is declared as an input
   parameter in a base module or incremental module, parameter
   constraints must not be declared.

Additional details on ONAP Base Module Output Parameters are provided in
`ONAP Output Parameter Names`_ and `Cinder Volume Templates`_.

ONAP Predefined Output Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP will look for a small set of pre-defined Heat output parameters to
capture resource attributes for inventory in ONAP. These output
parameters are optional and are specified in `OAM Management IP Addresses`_.

Support of heat stack update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

VNF Heat Orchestration Templates must not be designed to utilize the
OpenStack heat stack-update command for scaling (growth/de-growth). ONAP
does not support the use of heat stack-update command for scaling.

It is important to note that ONAP only supports heat stack-update for
image upgrades.

Networking
^^^^^^^^^^

ONAP defines two types of networks: External Networks and Internal
Networks.

ONAP defines an external network in relation to the VNF and not with
regard to the Network Cloud site. External networks may also be referred
to as “inter-VNF” networks. An external network connects VMs in a VNF to

-  VMs in another VNF or

-  an external gateway or router

ONAP defines an internal network in relation to the VNF and not with
regard to the Network Cloud site. Internal networks may also be referred
to as “intra-VNF” networks or “private” networks. An internal network
only connects VMs in a single VNF. It must not connect to other VNFs or
an external gateway or router.

External Networks
^^^^^^^^^^^^^^^^^^

VNF Heat Orchestration Templates must not include any resources for
external networks connected to the VNF. External networks must be
orchestrated separately, as independent, stand-alone VNF Heat
Orchestration Templates, so they can be shared by multiple VNFs and
managed independently.

When the external network is created, it must be assigned a unique
{network-role}. The {network-role} should describe the network (e.g.,
oam). The {network-role} while unique to the LCP, can repeat across
LCPs.

An External Network may be a Neutron Network or a Contrail Network

External networks must be passed into the VNF Heat Orchestration
Templates as parameters.

-  Neutron Network-id (UUID)

-  Neutron Network subnet ID (UUID)

-  Contrail Network Fully Qualified Domain Name (FQDN)

ONAP enforces a naming convention for parameters associated with
external networks. `ONAP Resource ID and Parameter Naming Convention`_ provides additional details.

Parameter values associated with an external network will be generated
and/or assigned by ONAP at orchestration time. Parameter values
associated with an external network must not be enumerated in the
environment file. `ONAP Resource ID and Parameter Naming Convention`_ provides additional details.

VNFs may use **Cloud assigned IP addresses** or **ONAP SDN-C assigned IP addresses**
when attaching VMs to an external network

-  A Cloud assigned IP address is assigned by OpenStack’s DHCP Service.

-  An ONAP SDN-C assigned IP address is assigned by the ONAP SDN-C
   controller

-  Note that Neutron Floating IPs must not be used. ONAP does not
   support Neutron Floating IPs (e.g., OS::Neutron::FloatingIP)

-  ONAP supports the property allowed_address_pairs in the resource
   OS::Neutron:Port and the property
   virtual_machine_interface_allowed_address_pairs in
   OS::ContrailV2::VirtualMachineInterfaces. This allows the assignment
   of a virtual IP (VIP) address to a set of VMs.

VNF Heat Orchestration Templates must pass the appropriate external
network IDs into nested VM templates when nested Heat is used.

Internal Networks
^^^^^^^^^^^^^^^^^^

The VNF Heat Orchestration Templates must include the resource(s) to
create the internal network. The internal network must be either a
Neutron Network or a Contrail Network.

In the modular approach, internal networks must be created in the Base
Module, with their resource IDs exposed as outputs (i.e., ONAP Base
Module Output Parameters) for use by all incremental modules. If the
Network resource ID is required in the base template, then a
get_resource must be used.

When the internal network is created, it should be assigned a unique
{network-role} in the context of the VNF. `ONAP Resource ID and Parameter Naming Convention`_ provides additional
details.

VNFs may use **Cloud assigned IP addresses** or
**predetermined static IPs** when attaching VMs to an internal network.

-  A Cloud assigned IP address is assigned by OpenStack’s DHCP Service.

-  A predetermined static IP address is enumerated in the Heat
   environment file. Since an internal network is local to the VNF, IP
   addresses can be re-used at every VNF instance.

-  Note that Neutron Floating IPs must not be used. ONAP does not
   support Neutron Floating IPs (e.g., OS::Neutron::FloatingIP)

-  ONAP supports the property allowed_address_pairs in the resource
   OS::Neutron:Port and the property
   virtual_machine_interface_allowed_address_pairs in
   OS::ContrailV2::VirtualMachineInterfaces. This allows the assignment
   of a virtual IP (VIP) address to a set of VMs.

ONAP does not programmatically enforce a naming convention for
parameters for internal network. However, a naming convention is
provided that must be followed. `ONAP Resource ID and Parameter Naming Convention`_ provides additional details.

ONAP Resource ID and Parameter Naming Convention
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section provides the ONAP naming requirements for

1. Resource IDs

2. Resource Property Parameters

{vm-type}
^^^^^^^^^^

The Heat Orchestration Templates for a VNF must assign a VNF unique
{vm-type} for each Virtual Machine type (i.e., OS::Nova::Server)
instantiated in the VNF. While the {vm-type} must be unique to the VNF,
it does not have to be globally unique across all VNFs that ONAP
supports.

Any parameter that is associated with a unique Virtual Machine type in
the VNF must include {vm-type} as part of the parameter name.

Any resource ID that is associated with a unique Virtual Machine type in
the VNF must include {vm-type} as part of the resource ID.

Note that {vm-type} must not be a substring of {network-role}. A
substring of a string is another string that occurs "in". For example,
"oam" is a substring of "oam_protected". It will cause the
Pre-Amsterdam VNF Validation Program (i.e., ICE Project) process to
produce erroneous error messages.

The {vm-type} should not contain the string “_int” or “int_” or
“_int_”. It may cause the Pre-Amsterdam VNF Validation Program (i.e.,
ICE Project) process to produce erroneous error messages.

The {vm-type} must be the same case in all parameter names in the VNF.

The {vm-type} must be the same case in all Resource IDs in the VNF.

It is recommended that the {vm-type} case in the parameter names matches
the {vm-type} case in the Resource IDs.

There are two exceptions to the above rules:

1. The six ONAP Metadata parameters must not be prefixed with a common
   {vm-type} identifier. They are *vnf_name*, *vnf_id*,
   *vf_module_id*, *vf_module_name, vm_role*. The ONAP Metadata
   parameters are described in `Resource:  OS::Nova::Server – Metadata Parameters`_.

2. The parameter referring to the OS::Nova::Server property
   availability_zone must not be prefixed with a common {vm-type}
   identifier. availability_zone is described in `Property: availability_zone`_.

{network-role}
^^^^^^^^^^^^^^

The assignment of a {network-role} is discussed in `Networking`_.

Any parameter that is associated with an external network must include
the {network-role} as part of the parameter name.

Any resource ID that is associated with an external network must include
the {network-role} as part of the resource ID.

Any parameter that is associated with an internal network must include
int_{network-role} as part of the parameter name.

Any resource ID that is associated with an internal network must include
int_{network-role} as part of the resource ID.

Note that {network-role} must not be a substring of {vm-type}. A
substring of a string is another string that occurs "in". For example,
"oam" is a substring of "oam_protected". It will cause the
Pre-Amsterdam VNF Validation Program (i.e., ICE Project) process to
produce erroneous error messages.

The {network-role} should not contain the string “_int” or “int_” or
“_int_”. It may cause the Pre-Amsterdam VNF Validation Program (i.e.,
ICE Project) process to produce erroneous error messages.

The {network-role} must be the same case in all parameter names in the
VNF.

The {network-role} must be the same case in all Resource IDs in the VNF.

It is recommended that the {network-role} case in the parameter names
matches the {network-role} case in the Resource IDs.

Resource IDs
^^^^^^^^^^^^

Heat Orchestration Template resources are described in `resources`_

A resource ID that must be unique within the resources section of a Heat
Orchestration Template. This is an OpenStack Requirement.

When a VNF is composed of more than one Heat Orchestration Template
(i.e., modules), ONAP requires that the resource ID must be unique
across all modules that compose the VNF.

When a resource is associated with a single {vm-type}, the resource ID
must contain {vm-type}.

When a resource is associated with a single external network, the
resource ID must contain {network-role}.

When a resource is associated with a single internal network, the
resource ID must contain int_{network-role}.

When a resource is associated with a single {vm-type} and a single
external network, the resource ID must contain both the {vm-type} and
{network-role}.

-  The {vm-type} must appear before the {network-role} and must be
   separated by an underscore (i.e., {vm-type}_{network-role}).

-  Note that an {index} value may separate the {vm-type} and the
   {network-role}. An underscore will separate the three values (i.e.,
   {vm-type}_{index}_{network-role}).

When a resource is associated with a single {vm-type} and a single
internal network, the resource ID must contain both the {vm-type} and
int_{network-role}.

-  The {vm-type} must appear before the int_{network-role} and must be
   separated by an underscore (i.e., {vm-type}_int_{network-role}).

-  Note that an {index} value may separate the {vm-type} and the
   int_{network-role}. An underscore will separate the three values
   (i.e., {vm-type}_{index}_int_{network-role}).

When a resource is associated with more than one {vm-type} and/or more
than one network, the resource ID

-  must not contain the {vm-type} and/or
   {network-role}/int_{network-role}

-  should contain the term “shared” and/or contain text that identifies
   the VNF.

Only alphanumeric characters and “_” underscores must be used in the
resource ID. Special characters must not be used.

All {index} values must be zero based. That is, the {index} must start
at zero and increment by one.

The table below provides example OpenStack Heat resource ID for
resources only associated with one {vm-type} and/or one network.

+--------------------------------+------------------------------------------------------------+
| Resource Type                  | Resource ID Format                                         |
+================================+============================================================+
| OS::Cinder::Volume             | {vm_type}_volume_{index}                                |
+--------------------------------+------------------------------------------------------------+
| OS::Cinder::VolumeAttachment   | {vm_type}_volumeattachment_{index}                      |
+--------------------------------+------------------------------------------------------------+
| OS::Heat::CloudConfig          | {vm_type}_RCC                                            |
+--------------------------------+------------------------------------------------------------+
| OS::Heat::MultipartMime        | {vm_type}_RMM                                            |
+--------------------------------+------------------------------------------------------------+
| OS::Heat::ResourceGroup        | {vm_type}_RRG                                            |
+--------------------------------+------------------------------------------------------------+
| OS::Heat::SoftwareConfig       | {vm_type}_RSC                                            |
+--------------------------------+------------------------------------------------------------+
| OS::Neutron::Port              | {vm_type}_{index}_{network_role}_{index}_port        |
+--------------------------------+------------------------------------------------------------+
|                                | {vm_type}_{index}_int_{network_role}_{index}_port   |
+--------------------------------+------------------------------------------------------------+
| OS::Neutron::SecurityGroup     | {vm_type}_RSG                                            |
+--------------------------------+------------------------------------------------------------+
| OS::Neutron::Subnet            | {network_role}_subnet_{index}                           |
+--------------------------------+------------------------------------------------------------+
| OS::Nova::Server               | {vm_type}_{index}                                        |
+--------------------------------+------------------------------------------------------------+
| OS::Nova::ServerGroup          | {vm_type}_RSG                                            |
+--------------------------------+------------------------------------------------------------+
| OS::Swift::Container           | {vm_type}_RSwiftC                                        |
+--------------------------------+------------------------------------------------------------+

    Table 1: Example OpenStack Heat Resource ID

The table below provides example Contrail Heat resource ID for resources
only associated with one {vm-type} and/or one network.

+-------------------------------------------+---------------------------------------------+
| Resource Type                             | Resource ID Format                          |
+===========================================+=============================================+
| OS::ContrailV2::InstanceIp                | {vm_type}_{index}_{network_role}_RII   |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::InterfaceRouteTable       | {network_role}_RIRT                       |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::NetworkIpam               | {network_role}_RNI                        |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::PortTuple                 | {vm_type}_RPT                             |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::ServiceHealthCheck        | {vm_type}_RSHC_{LEFT\|RIGHT}             |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::ServiceTemplate           | {vm_type}_RST_{index}                    |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::VirtualMachineInterface   | int_{network_role}_RVMI                  |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::VirtualNetwork            | int_{network_role}_RVN                   |
+-------------------------------------------+---------------------------------------------+

    Table 2: Example Contrail Heat resource ID

Resource: OS::Nova::Server - Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The resource OS::Nova::Server manages the running virtual machine (VM)
instance within an OpenStack cloud. (See
https://docs.openstack.org/developer/heat/template_guide/openstack.html#OS::Nova::Server.)

Four properties of this resource must follow the ONAP parameter naming
convention. The four properties are:

1. image

2. flavor

3. name

4. availability_zone

The table below provides a summary. The sections that follow provides
additional details.

Note that the {vm_type} must be identical across all four property
parameter for a given OS::Nova::Server resource.

+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+
| Resource OS::Nova::Server                                                                                                                       |
+=============================+===============================+==================+==============================+=================================+
| Property Name               | ONAP Parameter Name           | Parameter Type   | Parameter Value Generation   | ONAP Parameter Classification   |
+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+
| image                       | {vm-type}_image_name        | string           | Environment File             | ONAP Constant                   |
+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+
| flavor                      | {vm-type}_flavor_name       | string           | Environment File             | ONAP Constant                   |
+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+
| name                        | {vm-type}_name_{index}      | string           | ONAP                         | ONAP Orchestration              |
+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+
|                             | {vm-type}_names              | CDL              | ONAP                         | ONAP Orchestration              |
+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+
| availability_zone          | availability_zone_{index}   | string           | ONAP                         | ONAP Orchestration              |
+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+

Table 3 Resource Property Parameter Names

Property: image
~~~~~~~~~~~~~~~

The parameter associated with the property image is an ONAP Constant
parameter.

The parameters must be named {vm-type}_image_name in the Heat
Orchestration Template.

The parameter must be declared as type: string

The parameter must be enumerated in the Heat Orchestration Template
environment file.

Each VM type (i.e., {vm-type}) must have a separate parameter for image,
even if more than one {vm-type} shares the same image. This provides
maximum clarity and flexibility.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     {vm-type}_image_name:
         type: string
         description: {vm-type} server image

Property: flavor
~~~~~~~~~~~~~~~~

The parameter associated with the property flavor is an ONAP Constant
parameter.

The parameters must be named {vm-type}_flavor_name in the Heat
Orchestration Template.

The parameter must be declared as type: string

The parameter must be enumerated in the Heat Orchestration Template
environment file.

Each VM type (i.e., {vm-type}) must have a separate parameter for
flavors, even if more than one {vm-type} shares the same flavor. This
provides maximum clarity and flexibility.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     {vm-type}_flavor_name:
         type: string
         description: {vm-type} flavor

Property: Name
~~~~~~~~~~~~~~

The parameter associated with the property name is an ONAP Orchestration
parameter.

The parameter value is provided to the Heat template by ONAP. The
parameter must not be enumerated in the environment file.

The parameter must be declared as type: string or type:
comma_delimited_list

If the parameter is declared as type:string, the parameter must be named
{vm-type}_name_{index}, where {index} is a numeric value that starts
at zero and increments by one.

If the parameter is declared as type:comma_delimited_list, the
parameter must be named as {vm-type}_names

Each element in the VM Name list should be assigned to successive
instances of that VM type.

If a VNF contains more than three instances of a given {vm-type}, the
comma_delimited_list form of the parameter name (i.e.,
{vm-type}_names) should be used to minimize the number of unique
parameters defined in the Heat.

*Example: Parameter Definition*

.. code-block:: yaml

 parameters:
     {vm-type}_names:
         type: comma_delimited_list
         description: VM Names for {vm-type} VMs
     {vm-type}_name_{index}:
         type: string
         description: VM Name for {vm-type} VM {index}

*Example: comma_delimited_list*

In this example, the {vm-type} has been defined as “lb” for load
balancer.

.. code-block:: yaml

 parameters:
     lb_names:
         type: comma_delimited_list
         description: VM Names for lb VMs

 resources:
     lb_0:
         type: OS::Nova::Server
         properties:
             name: { get_param: [lb_names, 0] }
             ...

     lb_1:
         type: OS::Nova::Server
         properties:
             name: { get_param: [lb_names, 1] }
             ...

*Example: fixed-index*

In this example, the {vm-type} has been defined as “lb” for load
balancer.

.. code-block:: yaml

 parameters:
     lb_name_0:
         type: string
         description: VM Name for lb VM 0

     lb_name_1:
         type: string
         description: VM Name for lb VM 1

 resources:
     lb_0:
         type: OS::Nova::Server
         properties:
             name: { get_param: lb_name_0 }
             ...

     lb_1:
         type: OS::Nova::Server
         properties:
             name: { get_param: lb_name_1 }
             ...

Contrail Issue with Values for OS::Nova::Server Property Name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Contrail GUI has a limitation displaying special characters. The
issue is documented in
https://bugs.launchpad.net/juniperopenstack/+bug/1590710. It is
recommended that special characters be avoided. However, if special
characters must be used, the only special characters supported are:

- “ ! $ ‘ ( ) = ~ ^ \| @ \` { } [ ] > , . _

Property: availability_zone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The parameter associated with the property availability_zone is an ONAP
Orchestration parameter.

The parameter value is provided to the Heat template by ONAP. The
parameter must not be enumerated in the environment file.

The parameter must be named availability_zone_{index} in the Heat
Orchestration Template. The {index} must start at zero. The {index} must
increment by one. The parameter name must not include the {vm-type}.

The parameter must be declared as type: string

The parameter must not be declared as type: comma_delimited_list

Example
~~~~~~~

The example below depicts part of a Heat Orchestration Template that
uses the four OS::Nova::Server properties discussed in this section.

In the Heat Orchestration Template below, four Virtual Machines
(OS::Nova::Server) are created: two dns servers with {vm-type} set to
“dns” and two oam servers with {vm-type} set to “oam”. Note that the
parameter associated with the property name is a comma_delimited_list
for dns and a string for oam.

.. code-block:: yaml

 parameters:
   dns_image_name:
     type: string
     description: dns server image
   dns_flavor_name:
     type: string
     description: dns server flavor
   dns_names:
     type: comma_delimited_list
     description: dns server names
   oam_image_name:
     type: string
     description: oam server image
   oam_flavor_name:
     type: string
     description: oam server flavor
   oam_name_0:
     type: string
     description: oam server name 0
   oam_name_1:
     type: string
     description: oam server name 1
   availability_zone_0:
     type: string
     description: availability zone ID or Name
   availability_zone_1:
     type: string
     description: availability zone ID or Name

 resources:
   dns_server_0:
     type: OS::Nova::Server
     properties:
       name: { get_param: [ dns_names, 0 ] }
       image: { get_param: dns_image_name }
       flavor: { get_param: dns_flavor_name }
       availability_zone: { get_param: availability_zone_0 }
       . . .

   dns_server_1:
     type: OS::Nova::Server
     properties:
       name: { get_param: [ dns_names, 1 ] }
       image: { get_param: dns_image_name }
       flavor: { get_param: dns_flavor_name }
       availability_zone: { get_param: availability_zone_1 }
       . . .

   oam_server_0:
     type: OS::Nova::Server
     properties:
       name: { get_param: oam_name_0 }
       image: { get_param: oam_image_name }
       flavor: { get_param: oam_flavor_name }
       availability_zone: { get_param: availability_zone_0 }
       . . .

   oam_server_1:
     type: OS::Nova::Server
     properties:
       name: { get_param: oam_name_1 }
       image: { get_param: oam_image_name }
       flavor: { get_param: oam_flavor_name }
       availability_zone: { get_param: availability_zone_1 }
       . . .

Resource: OS::Nova::Server – Metadata Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The resource OS::Nova::Server has an OpenStack optional property
metadata. The metadata property is mandatory for ONAP Heat Orchestration
Templates; it must be included.

ONAP requires the following three mandatory metadata parameters for an
OS::Nova::Server resource:

-  vnf_id

-  vf_module_id

-  vnf_name

ONAP allows the following three optional metadata parameters for an
OS::Nova::Server resource. They may be included

-  vm_role

-  vf_module_name

Note that the metadata parameters do not and must not contain {vm-type}
in their name.

When Metadata parameters are past into a nested heat template, the
parameter names must not change.

The table below provides a summary. The sections that follow provides
additional details.

+---------------------------+------------------+----------------------+------------------------------+
| Metadata Parameter Name   | Parameter Type   | Mandatory/Optional   | Parameter Value Generation   |
+===========================+==================+======================+==============================+
| vnf_id                   | string           | Mandatory            | ONAP                         |
+---------------------------+------------------+----------------------+------------------------------+
| vf_module_id            | string           | Mandatory            | ONAP                         |
+---------------------------+------------------+----------------------+------------------------------+
| vnf_name                 | string           | Mandatory            | ONAP                         |
+---------------------------+------------------+----------------------+------------------------------+
| vf_module_name          | string           | Optional             | ONAP                         |
+---------------------------+------------------+----------------------+------------------------------+
| vm_role                  | string           | Optional             | YAML or Environment File     |
+---------------------------+------------------+----------------------+------------------------------+
+---------------------------+------------------+----------------------+------------------------------+

    Table 4: ONAP Metadata

vnf_id
~~~~~~~

The vnf_id parameter is mandatory; it must be included in the Heat
Orchestration Template.

The vnf_id parameter value will be supplied by ONAP. ONAP generates the
UUID that is the vnf_id and supplies it to the Heat Orchestration
Template at orchestration time.

The parameter must be declared as type: string

Parameter constraints must not be defined.

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     vnf_id:
         type: string
         description: Unique ID for this VNF instance

vf_module_id
~~~~~~~~~~~~~~

The vf_module_id parameter is mandatory; it must be included in the
Heat Orchestration Template.

The vf_module_id parameter value will be supplied by ONAP. ONAP
generates the UUID that is the vf_module_id and supplies it to the
Heat Orchestration Template at orchestration time.

The parameter must be declared as type: string

Parameter constraints must not be defined.

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     vnf_module_id:
         type: string
         description: Unique ID for this VNF module instance

vnf_name
~~~~~~~~~

The vnf_name parameter is mandatory; it must be included in the Heat
Orchestration Template.

The vnf_name parameter value will be generated and/or assigned by ONAP
and supplied to the Heat Orchestration Template by ONAP at orchestration
time.

The parameter must be declared as type: string

Parameter constraints must not be defined.

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     vnf_name:
         type: string
         description: Unique name for this VNF instance

vf_module_name
~~~~~~~~~~~~~~~~

The vf_module_name parameter is optional; it may be included in the
Heat Orchestration Template.

The vf_module_name parameter is the name of the name of the Heat stack
(e.g., <STACK_NAME>) in the command “Heat stack-create” (e.g., Heat
stack-create [-f <FILE>] [-e <FILE>] <STACK_NAME>). The <STACK_NAME>
needs to be specified as part of the orchestration process.

The parameter must be declared as type: string

Parameter constraints must not be defined.

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     vf_module_name:
         type: string
         description: Unique name for this VNF Module instance

vm_role
~~~~~~~~

The vm_role parameter is optional; it may be included in the Heat
Orchestration Template.

Any roles tagged to the VMs via metadata will be stored in ONAP’s A&AI
system and available for use by other ONAP components and/or north bound
systems.

The vm_role values must be either

-  hard-coded into the Heat Orchestration Template or

-  enumerated in the environment file.

Defining the vm_role as the {vm-type} is a recommended convention

The parameter must be declared as type: string

Parameter constraints must not be defined.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     vm_role:
         type: string
         description: Unique role for this VM

*Example Resource Definition: Hard Coded*

In this example, the {vm-role} is hard coded in the Heat Orchestration
Template.

.. code-block:: yaml

 resources:
   dns_servers:
     type: OS::Nova::Server
     properties:
       . . . .
       metadata:
         vm_role: lb

*Example Resource Definition: get_param*

In this example, the {vm-role} is enumerated in the environment file.

.. code-block:: yaml

 resources:
   dns_servers:
     type: OS::Nova::Server
     properties:
       . . . .
       metadata:
         vm_role: { get_param: vm_role }

Example
~~~~~~~

The example below depicts part of a Heat Orchestration Template that
uses the five of the OS::Nova::Server metadata parameter discussed in
this section. The {vm-type} has been defined as lb for load balancer.

.. code-block:: yaml

 parameters:
    lb_name_0
       type: string
       description: VM Name for lb VM 0
    vnf_name:
       type: string
       description: Unique name for this VNF instance
    vnf_id:
       type: string
       description: Unique ID for this VNF instance
    vf_module_name:
       type: string
       description: Unique name for this VNF Module instance
    vf_module_id:
       type: string
       description: Unique ID for this VNF Module instance
    vm_role:
       type: string
       description: Unique role for this VM

 resources:

    lb_vm_0:
       type: OS::Nova::Server
       properties:
       name: { get_param: lb_name_0 }
       ...
       metadata:
          vnf_name: { get_param: vnf_name }
          vnf_id: { get_param: vnf_id }
          vf_module_name: { get_param: vf_module_name }
          vf_module_id: { get_param: vf_module_id }
          vm_role: lb

Resource: OS::Neutron::Port - Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The resource OS::Neutron::Port is for managing Neutron ports (See
https://docs.openstack.org/developer/heat/template_guide/openstack.html#OS::Neutron::Port.)

Introduction
~~~~~~~~~~~~

Four properties of the resource OS::Neutron::Port that must follow the
ONAP parameter naming convention. The four properties are:

1. network

2. fixed_ips, ip_address

3. fixed_ips, subnet_id

4. allowed_address_pairs, ip_address

The parameters associated with these properties may reference an
external network or internal network. External networks and internal
networks are defined in `Networking`_.

External Networks
^^^^^^^^^^^^^^^^^

When the parameter references an external network

-  the parameter name must contain {network-role}

-  the parameter must not be enumerated in the Heat environment file

-  the parameter is classified as an ONAP Orchestration Parameter

+----------------------------------------+-----------------------------------------------+--------------------------+
| Property Name                          | ONAP Parameter Name                           | Parameter Type           |
+========================================+===============================================+==========================+
| network                                | {network-role}_net_id                       | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {network-role}_net_name                     | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
| fixed_ips, ip_address                | {vm-type}_{network-role}_ip_{index}        | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}_{network-role}_ips                | comma_delimited_list   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}_{network-role}_v6_ip_{index}    | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}_{network-role}_v6_ips            | comma_delimited_list   |
+----------------------------------------+-----------------------------------------------+--------------------------+
| fixed_ips, subnet                     | {network-role}_subnet_id                    | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {network-role}_v6_subnet_id                | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
| allowed_address_pairs, ip_address   | {vm-type}_{network-role}_floating_ip       | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}_{network-role}_floating_v6_ip   | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}_{network-role}_ip_{index}        | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}_{network-role}_ips                | comma_delimited_list   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}_{network-role}_v6_ip_{index}    | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}_{network-role}_v6_ips            | comma_delimited_list   |
+----------------------------------------+-----------------------------------------------+--------------------------+

Table 5: OS::Neutron::Port Resource Property Parameters (External
Networks)

Internal Networks
^^^^^^^^^^^^^^^^^

When the parameter references an internal network

-  the parameter name must contain int_{network-role}

-  the parameter may be enumerated in the environment file.

+----------------------------------------+----------------------------------------------------+--------------------------+
| Property                               | Parameter Name for Internal Networks               | Parameter Type           |
+========================================+====================================================+==========================+
| network                                | int_{network-role}_net_id                       | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | int_{network-role}_net_name                     | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
| fixed_ips, ip_address                | {vm-type}_int_{network-role}_ip_{index}        | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}_int_{network-role}_ips                | comma_delimited_list   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}_int_{network-role}_v6_ip_{index}    | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}_int_{network-role}_v6_ips            | comma_delimited_list   |
+----------------------------------------+----------------------------------------------------+--------------------------+
| fixed_ips, subnet                     | int_{network-role}_subnet_id                    | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | int_{network-role}_v6_subnet_id                | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
| allowed_address_pairs, ip_address   | {vm-type}_int_{network-role}_floating_ip       | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}_int_{network-role}_floating_v6_ip   | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}_int_{network-role}_ip_{index}        | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}_int_{network-role}_ips                | comma_delimited_list   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}_int_{network-role}_v6_ip_{index}    | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}_int_{network-role}_v6_ips            | comma_delimited_list   |
+----------------------------------------+----------------------------------------------------+--------------------------+

Table 6: Port Resource Property Parameters (Internal Networks)

Property: network
~~~~~~~~~~~~~~~~~

The property networks in the resource OS::Neutron::Port must be
referenced by Neutron Network ID, a UUID value, or by the network name
defined in OpenStack.

External Networks
^^^^^^^^^^^^^^^^^

When the parameter associated with the property network is referencing
an “external” network, the parameter must adhere to the following naming
convention in the Heat Orchestration Template

-  {network-role}_net_id for the Neutron network ID

-  {network-role}_net_name for the network name in OpenStack

The parameter must be declared as type: string

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     {network-role}_net_id:
         type: string
         description: Neutron UUID for the {network-role} network
     {network-role}_net_name:
         type: string
         description: Neutron name for the {network-role} network

*Example: One Cloud Assigned IP Address (DHCP) assigned to a network
that has only one subnet*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} has been defined as lb for load
balancer. The Cloud Assigned IP Address uses the OpenStack DHCP service
to assign IP addresses.

.. code-block:: yaml

 parameters:
    oam_net_id:
       type: string
       description: Neutron UUID for the oam network

 resources:
    lb_port_1:
       type: OS::Neutron::Port
       network: { get_param: oam_net_id }

Internal Networks
^^^^^^^^^^^^^^^^^

When the parameter associated with the property network is referencing
an “internal” network, the parameter must adhere to the following naming
convention.

-  int_{network-role}_net_id for the Neutron network ID

-  int_{network-role}_net_name for the network name in OpenStack

The parameter must be declared as type: string

The assumption is that internal networks are created in the base module.
The Neutron Network ID will be passed as an output parameter (e.g., ONAP
Base Module Output Parameter) to the incremental modules. In the
incremental modules, it will be defined as input parameter.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     int_{network-role}_net_id:
         type: string
         description: Neutron UUID for the {network-role} network
     int_{network-role}_net_name:
         type: string
         description: Neutron name for the {network-role} network

Property: fixed_ips, Map Property: subnet_id
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The property fixed_ips is used to assign IPs to a port. The Map
Property subnet_id specifies the subnet the IP is assigned from.

The property fixed_ips and Map Property subnet_id must be used if a
Cloud (i.e., DHCP) IP address assignment is being requested and the
Cloud IP address assignment is targeted at a specific subnet when two or
more subnets exist.

The property fixed_ips and Map Property subnet_id should not be used
if all IP assignments are fixed, or if the Cloud IP address assignment
does not target a specific subnet or there is only one subnet.

Note that DHCP assignment of IP addresses is also referred to as cloud
assigned IP addresses.

Subnet of an External Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the parameter is referencing a subnet of an “external” network, the
property fixed_ips and Map Property subnet_id parameter must adhere to
the following naming convention.

-  {network-role}_subnet_id if the subnet is an IPv4 subnet

-  {network-role}_v6_subnet_id if the subnet is an IPv6 subnet

The parameter must be declared as type: string

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     {network-role}_subnet_id:
         type: string
         description: Neutron subnet UUID for the {network-role} network

     {network-role}_v6_subnet_id:
         type: string
         description: Neutron subnet UUID for the {network-role} network

*Example: One Cloud Assigned IPv4 Address (DHCP) assigned to a network
that has two or more subnets subnet:*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} has been defined as lb for load
balancer. The Cloud Assigned IP Address uses the OpenStack DHCP service
to assign IP addresses.

.. code-block:: yaml

 parameters:
    oam_net_id:
       type: string
       description: Neutron UUID for the oam network

    oam_subnet_id:
       type: string
       description: Neutron subnet UUID for the oam network

 resources:
    lb_port_1:
       type: OS::Neutron::Port
       network: { get_param: oam_net_id }
    fixed_ips:
      - subnet_id: { get_param: oam_subnet_id }

*Example: One Cloud Assigned IPv4 address and one Cloud Assigned IPv6
address assigned to a network that has at least one IPv4 subnet and one
IPv6 subnet*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} has been defined as lb for load
balancer.

.. code-block:: yaml

 parameters:
    oam_net_id:
       type: string
       description: Neutron UUID for the oam network

    oam_subnet_id:
       type: string
       description: Neutron subnet UUID for the oam network

    oam_v6_subnet_id:
       type: string
       description: Neutron subnet UUID for the oam network

 resources:
    lb_port_1:
       type: OS::Neutron::Port
       properties:
          network: { get_param: oam_net_id }
          fixed_ips:
           - subnet_id: { get_param: oam_subnet_id }
           - subnet_id: { get_param: oam_v6_subnet_id }

Internal Networks
^^^^^^^^^^^^^^^^^

When the parameter is referencing the subnet of an “internal” network,
the property fixed_ips and Map Property subnet_id parameter must
adhere to the following naming convention.

-  int_{network-role}_subnet_id if the subnet is an IPv4 subnet

-  int_{network-role}_v6_subnet_id if the subnet is an IPv6 subnet

The parameter must be declared as type: string

The assumption is that internal networks are created in the base module.
The Neutron subnet network ID will be passed as an output parameter
(e.g., ONAP Base Module Output Parameter) to the incremental modules. In
the incremental modules, it will be defined as input parameter.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     int_{network-role}_subnet_id:
        type: string
         description: Neutron subnet UUID for the {network-role} network

     int_{network-role}_v6_subnet_id:
         type: string
         description: Neutron subnet UUID for the {network-role} network

Property: fixed_ips, Map Property: ip_address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The property fixed_ips is used to assign IPs to a port. The Map
Property ip_address specifies the IP address to be assigned to the
port.

The property fixed_ips and Map Property ip_address must be used when
statically assigning one or more IP addresses to a port. This is also
referred to as ONAP SDN-C IP address assignment. ONAP’s SDN-C provides
the IP address assignment.

An IP address is assigned to a port on a VM (referenced by {vm-type})
that is connected to an external network (referenced by {network-role})
or internal network (referenced by int_{network-role}).

When a SDN-C IP assignment is made to a port connected to an external
network, the parameter name must contain {vm-type} and {network-role}.

When a SDN-C IP assignment is made to a port connected to an internal
network, the parameter name must contain {vm-type} and
int_{network-role}.

IP Address Assignments on External Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the property fixed_ips and Map Property ip_address is used to
assign IP addresses to an external network, the parameter name is
dependent on the parameter type (comma_delimited_list or string) and
IP address type (IPv4 or IPv6).

When the parameter for property fixed_ips and Map Property ip_address
is declared type: comma_delimited_list, the parameter must adhere to
the following naming convention

-  {vm-type}_{network-role}_ips for IPv4 address

-  {vm-type}_{network-role}_v6_ips for IPv6 address

Each element in the IP list should be assigned to successive instances
of {vm-type} on {network-role}.

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:

    {vm-type}_{network-role}_ips:
       type: comma_delimited_list
       description: Fixed IPv4 assignments for {vm-type} VMs on the {Network-role} network

    {vm-type}_{network-role}_v6_ips:
       type: comma_delimited_list
       description: Fixed IPv6 assignments for {vm-type} VMs on the {network-role} network

*Example: comma_delimited_list parameters for IPv4 and IPv6 Address
Assignments to an external network*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} has been defined as db for database.

.. code-block:: yaml

 parameters:
    oam_net_id:
       type: string
       description: Neutron UUID for a oam network

    db_oam_ips:
       type: comma_delimited_list
       description: Fixed IPv4 assignments for db VMs on the oam network

    db_oam_v6_ips:
       type: comma_delimited_list
       description: Fixed IPv6 assignments for db VMs on the oam network

 resources:
    db_0_port_1:
       type: OS::Neutron::Port
       network: { get_param: oam_net_id }
       fixed_ips: [ { “ip_address”: {get_param: [ db_oam_ips, 0 ]}}, {“ip_address”: {get_param: [ db_oam_v6_ips, 0 ]}}]

    db_1_port_1:
       type: OS::Neutron::Port
       properties:
       network: { get_param: oam_net_id }
       fixed_ips:
          - “ip_address”: {get_param: [ db_oam_ips, 1 ]}
          - “ip_address”: {get_param: [ db_oam_v6_ips, 1 ]}

When the parameter for property fixed_ips and Map Property ip_address
is declared type: string, the parameter must adhere to the following
naming convention.

-  {vm-type}_{network-role}_ip_{index} for an IPv4 address

-  {vm-type}_{network-role}_v6_ip_{index} for an IPv6 address

The value for {index} must start at zero (0) and increment by one.

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
    {vm-type}_{network-role}_ip_{index}:
       type: string
       description: Fixed IPv4 assignment for {vm-type} VM {index} on the{network-role} network

    {vm-type}_{network-role}_v6_ip_{index}:
       type: string
       description: Fixed IPv6 assignment for {vm-type} VM {index} on the{network-role} network

*Example: string parameters for IPv4 and IPv6 Address Assignments to an external network*

In this example, the {network-role} has been defined as “oam” to
represent an oam network and the {vm-type} has been defined as “db” for
database.

.. code-block:: yaml

 parameters:
    oam_net_id:
    type: string
    description: Neutron UUID for an OAM network

 db_oam_ip_0:
    type: string
    description: Fixed IPv4 assignment for db VM 0 on the OAM network

 db_oam_ip_1:
    type: string
    description: Fixed IPv4 assignment for db VM 1 on the OAM network

 db_oam_v6_ip_0:
    type: string
    description: Fixed IPv6 assignment for db VM 0 on the OAM network

 db_oam_v6_ip_1:
    type: string
    description: Fixed IPv6 assignment for db VM 1 on the OAM network

 resources:
    db_0_port_1:
       type: OS::Neutron::Port
       properties:
          network: { get_param: oam_net_id }
          fixed_ips: [ { “ip_address”: {get_param: db_oam_ip_0}}, {“ip_address”: {get_param: db_oam_v6_ip_0 ]}}]

    db_1_port_1:
       type: OS::Neutron::Port
       properties:
          network: { get_param: oam_net_id }
          fixed_ips:
             - “ip_address”: {get_param: db_oam_ip_1}}]
             - “ip_address”: {get_param: db_oam_v6_ip_1}}]

IP Address Assignment on Internal Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the property fixed_ips and Map Property ip_address is used to
assign IP addresses to an internal network, the parameter name is
dependent on the parameter type (comma_delimited_list or string) and
IP address type (IPv4 or IPv6).

When the parameter for property fixed_ips and Map Property ip_address
is declared type: comma_delimited_list, the parameter must adhere to
the following naming convention

-  {vm-type}_int_{network-role}_ips for IPv4 address

-  {vm-type}_int_{network-role}_v6_ips for IPv6 address

Each element in the IP list should be assigned to successive instances
of {vm-type} on {network-role}.

The parameter must be enumerated in the Heat environment file. Since an
internal network is local to the VNF, IP addresses can be re-used at
every VNF instance.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:

    {vm-type}_int_{network-role}_ips:
       type: comma_delimited_list
       description: Fixed IPv4 assignments for {vm-type} VMs on the int_{network-role} network

    {vm-type}_int_{network-role}_v6_ips:
       type: comma_delimited_list
       description: Fixed IPv6 assignments for {vm-type} VMs on the int_{network-role} network

*Example: comma_delimited_list parameters for IPv4 and IPv6 Address
Assignments to an internal network*

In this example, the {network-role} has been defined as oam_int to
represent an oam network internal to the vnf. The role oam_int was
picked to differentiate from an external oam network with a
{network-role} of oam. The {vm-type} has been defined as db for
database.

.. code-block:: yaml

 parameters:
    int_oam_int_net_id:
       type: string
       description: Neutron UUID for the oam internal network

    db_int_oam_int_ips:
       type: comma_delimited_list
       description: Fixed IPv4 assignments for db VMs on the oam internal network

    db_int_oam_int_v6_ips:
       type: comma_delimited_list
       description: Fixed IPv6 assignments for db VMs on the oam internal network

 resources:
    db_0_port_1:
       type: OS::Neutron::Port
       properties:
       network: { get_param: int_oam_int_net_id }
       fixed_ips: [ { “ip_address”: {get_param: [ db_int_oam_int_ips, 0]}}, { “ip_address”: {get_param: [ db_int_oam_int_v6_ips, 0 ]}}]

    db_1_port_1:
       type: OS::Neutron::Port
       properties:
       network: { get_param: int_oam_int_net_id }
       fixed_ips:
          - “ip_address”: {get_param: [ db_int_oam_int_ips, 1 ]}
          - “ip_address”: {get_param: [ db_int_oam_int_v6_ips, 1 ]}

When the parameter for property fixed_ips and Map Property ip_address
is declared type: string, the parameter must adhere to the following
naming convention.

-  {vm-type}_int_{network-role}_ip_{index} for an IPv4 address

-  {vm-type}_int_{network-role}_v6_ip_{index} for an IPv6 address

The value for {index} must start at zero (0) and increment by one.

The parameter must be enumerated in the Heat environment file. Since an
internal network is local to the VNF, IP addresses can be re-used at
every VNF instance.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:

    {vm-type}_int_{network-role}_ip_{index}:
       type: string
       description: Fixed IPv4 assignment for {vm-type} VM {index} on the{network-role} network

    {vm-type}_int_{network-role}_v6_ip_{index}:
       type: string
       description: Fixed IPv6 assignment for {vm-type} VM {index} on the{network-role} network

*Example: string parameters for IPv4 and IPv6 Address Assignments to an internal network*

In this example, the {network-role} has been defined as oam_int to
represent an oam network internal to the vnf. The role oam_int was
picked to differentiate from an external oam network with a
{network-role} of oam. The {vm-type} has been defined as db for
database.

.. code-block:: yaml

 parameters:
    int_oam_int_net_id:
       type: string
       description: Neutron UUID for an OAM internal network

    db_oam_int_ip_0:
       type: string
       description: Fixed IPv4 assignment for db VM on the oam_int network

    db_oam_int_ip_1:
       type: string
       description: Fixed IPv4 assignment for db VM 1 on the oam_int network

    db_oam_int_v6_ip_0:
       type: string
       description: Fixed IPv6 assignment for db VM 0 on the oam_int network

    db_oam_int_v6_ip_1:
       type: string
       description: Fixed IPv6 assignment for db VM 1 on the oam_int network

 resources:
    db_0_port_0:
       type: OS::Neutron::Port
       properties:
          network: { get_param: int_oam_int_net_id }
          fixed_ips: [ { “ip_address”: {get_param: db_oam_int_ip_0}}, {“ip_address”: {get_param: db_oam_int_v6_ip_0 ]}}]

    db_1_port_0:
       type: OS::Neutron::Port
       properties:
          network: { get_param: int_oam_int_net_id }
          fixed_ips:
             - “ip_address”: {get_param: db_oam_int_ip_1}}]
             - “ip_address”: {get_param: db_oam_int_v6_ip_1}}]

Property: allowed_address_pairs, Map Property: ip_address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The property allowed_address_pairs in the resource OS::Neutron::Port
allows the user to specify a mac_address and/or ip_address that will
pass through a port regardless of subnet. This enables the use of
protocols such as VRRP, which floats an IP address between two instances
to enable fast data plane failover. The map property ip_address
specifies the IP address.

The allowed_address_pairs is an optional property. It is not required.

An ONAP Heat Orchestration Template allows the assignment of one IPv4
address allowed_address_pairs and/or one IPv6 address to a {vm-type}
and {network-role}/int_{network-role} combination.

An ONAP Heat Orchestration Template allows the assignment of one IPv6
address allowed_address_pairs and/or one IPv6 address to a {vm-type}
and {network-role}/int_{network-role} combination.

Note that the management of these IP addresses (i.e. transferring
ownership between active and standby VMs) is the responsibility of the
application itself.

Note that these parameters are **not** intended to represent Neutron
“Floating IP” resources, for which OpenStack manages a pool of public IP
addresses that are mapped to specific VM ports. In that case, the
individual VMs are not even aware of the public IPs, and all assignment
of public IPs to VMs is via OpenStack commands. ONAP does not support
Neutron-style Floating IPs.

External Networks
^^^^^^^^^^^^^^^^^

When the parameter is referencing an “external” network, the property
allowed_address_pairs and Map Property ip_address parameter must
adhere to the following naming convention.

-  {vm-type}_{network-role}_floating_ip for an IPv4 address

-  {vm-type}_{network-role}_floating_v6_ip for an IPv6 address

The parameter must be declared as type: string

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:

    {vm-type}_{network-role}_floating_ip:
       type: string
       description: VIP for {vm-type} VMs on the {network-role} network

    {vm-type}_{network-role}_floating_v6_ip:
       type: string
       description: VIP for {vm-type} VMs on the {network-role} network

*Example:*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} has been defined as db for database.

.. code-block:: yaml

 parameters:
    oam_net_id:
       type: string
       description: Neutron UUID for the oam network

    db_oam_ips:
       type: comma_delimited_list
       description: Fixed IPs for db VMs on the oam network

    db_oam_floating_ip:
       type: string
       description: VIP IP for db VMs on the oam network

 resources:
    db_0_port_0:
       type: OS::Neutron::Port
       properties:
          network: { get_param: oam_net_id }
          fixed_ips: [ { “ip_address”: {get_param: [db_oam_ips,0] }}]
          allowed_address_pairs: [ { “ip_address”: {get_param: db_oam_floating_ip}}]

    db_1_port_0:
       type: OS::Neutron::Port
       properties:
          network: { get_param: oam_net_id }
          fixed_ips: [ { “ip_address”: {get_param: [db_oam_ips,1] }}]
          allowed_address_pairs: [ { “ip_address”: {get_param: db_oam_floating_ip}}]

Internal Networks
^^^^^^^^^^^^^^^^^

When the parameter is referencing an “internal” network, the property
allowed_address_pairs and Map Property ip_address parameter must
adhere to the following naming convention.

-  {vm-type}_int_{network-role}_floating_ip for an IPv4 address

-  {vm-type}_int_{network-role}_floating_v6_ip for an IPv6 address

The parameter must be declared as type: string

The parameter must be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:

    {vm-type}_int_{network-role}_floating_ip:
       type: string
       description: VIP for {vm-type} VMs on the int_{network-role} network

    {vm-type}_int_{network-role}_floating_v6_ip:
       type: string
       description: VIP for {vm-type} VMs on the int_{network-role} network

Multiple allowed_address_pairs for a {vm-type} / {network-role} combination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The parameter {vm-type}_{network-role}_floating_ip provides only one
allowed address pair IPv4 address per {vm-type} and {network-role} pair.

The parameter {vm-type}_{network-role}_floating_v6_ip provides only
one allowed address pair IPv6 address per {vm-type} and {network-role}
pair.

If there is a need for multiple allowed address pair IPs for a given
{vm-type} and {network-role} combination within a VNF, then the
parameter names defined for the property fixed_ips and Map Property
ip_address should be used with the allowed_address_pairs property.
The examples below illustrate this.

*Example: A VNF has four load balancers. Each pair has a unique VIP.*

In this example, there are two administrative VM pairs. Each pair has
one VIP. The {network-role} has been defined as oam to represent an oam
network and the {vm-type} has been defined as admin for an
administrative VM.

Pair 1: Resources admin_0_port_0 and admin_1_port_0 share a unique
VIP, [admin_oam_ips,2]

Pair 2: Resources admin_2_port_0 and admin_3_port_0 share a unique
VIP, [admin_oam_ips,5]

.. code-block:: yaml

 parameters:
    oam_net_id:
       type: string
       description: Neutron UUID for the oam network
    admin_oam_ips:
       type: comma_delimited_list
       description: Fixed IP assignments for admin VMs on the oam network

 resources:

    admin_0_port_0:
       type: OS::Neutron::Port
       properties:
          network: { get_param: oam_net_id }
          fixed_ips: [ { “ip_address”: {get_param: [admin_oam_ips,0] }}]
          allowed_address_pairs: [{ “ip_address”: {get_param: [admin_oam_ips,2] }}]

    admin_1_port_0:
       type: OS::Neutron::Port
       properties:
          network: { get_param: oam_net_id }
          fixed_ips: [ { “ip_address”: {get_param: [admin_oam_ips,1] }}]
          allowed_address_pairs: [{ “ip_address”: {get_param:  [admin_oam_ips,2] }}]

    admin_2_port_0:
       type: OS::Neutron::Port
       properties:
          network: { get_param: oam_net_id }
          fixed_ips: [ { “ip_address”: {get_param: [admin_oam_ips,3] }}]
          allowed_address_pairs: [{ “ip_address”: {get_param: [admin_oam_ips,5] }}]

    admin_3_port_0:
       type: OS::Neutron::Port
       properties:
          network: { get_param: oam_net_id }
          fixed_ips: [ { “ip_address”: {get_param: [admin_oam_ips,4] }}]
          allowed_address_pairs: [{ “ip_address”: {get_param:  [admin_oam_ips,5] }}]

*Example: A VNF has two load balancers. The pair of load balancers share
two VIPs.*

In this example, there is one load balancer pairs. The pair has two
VIPs. The {network-role} has been defined as oam to represent an oam
network and the {vm-type} has been defined as lb for a load balancer VM.

.. code-block:: yaml

 resources:
    lb_0_port_0:
       type: OS::Neutron::Port
       properties:
          network: { get_param: oam_net_id }
          fixed_ips: [ { “ip_address”: {get_param: [lb_oam_ips,0] }}]
          allowed_address_pairs: [{ "ip_address": {get_param: [lb_oam_ips,2]}, {get_param: [lb_oam_ips,3] }}]

    lb_1_port_0:
       type: OS::Neutron::Port
       properties:
          network: { get_param: oam_net_id }
          fixed_ips: [ { “ip_address”: {get_param: [lb_oam_ips,1] }}]
          allowed_address_pairs: [{ "ip_address": {get_param: [lb_oam_ips,2]}, {get_param: [lb_oam_ips,3] }}]

As a general rule, provide the fixed IPs for the VMs indexed first in
the CDL and then the VIPs as shown in the examples above.

ONAP SDN-C Assignment of allowed_address_pair IP Addresses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following items must be taken into consideration when designing Heat
Orchestration Templates that expect ONAP’s SDN-C to assign
allowed_address_pair IP addresses via automation.

The VMs must be of the same {vm-type}.

The VMs must be created in the same module (base or incremental).

Resource Property “name”
^^^^^^^^^^^^^^^^^^^^^^^^

The parameter naming convention of the property name for the resource
OS::Nova::Server has been defined in `Resource:  OS::Nova::Server – Metadata Parameters`_.

This section provides the requirements how the property name for non
OS::Nova::Server resources must be defined when the property is used.
Not all resources require the property name (e.g., it is optional) and
some resources do not support the property.

When the property name for a non OS::Nova::Server resources is defined
in a Heat Orchestration Template, the intrinsic function str_replace
must be used in conjunction with the ONAP supplied metadata parameter
vnf_name to generate a unique value. This prevents the enumeration of a
unique value for the property name in a per instance environment file.

Note that

-  In most cases, only the use of the metadata value vnf_name is
   required to create a unique property name

-  the Heat Orchestration Template pseudo parameter 'OS::stack_name’
   may also be used in the str_replace construct to generate a unique
   name when the vnf_name does not provide uniqueness

*Example: Property* name *for resource* OS::Neutron::SecurityGroup

.. code-block:: yaml

 resources:
   DNS_SECURITY_GROUP:
     type: OS::Neutron::SecurityGroup
     properties:
       description: vDNS security group
       name:
         str_replace:
           template: VNF_NAME_sec_grp_DNS
           params:
             VNF_NAME: {get_param: vnf_name}
       rules: [. . . . .
              ]

*Example: Property name for resource* OS::Cinder::Volume

.. code-block:: yaml

 resources:
   DNS_Cinder_Volume:
     type: OS::Cinder::Volume
     properties:
       description: Cinder Volume
       name:
         str_replace:
           template: VNF_NAME_STACK_NAME_dns_volume
           params:
             VNF_NAME: {get_param: vnf_name}
             STACK_NAME: { get_param: 'OS::stack_name' }
       . . . .

Contrail Issue with Values for the Property Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Contrail GUI has a limitation displaying special characters. The
issue is documented in
https://bugs.launchpad.net/juniperopenstack/+bug/1590710. It is
recommended that special characters be avoided. However, if special
characters must be used, note that for the following resources:

-  Virtual Machine

-  Virtual Network

-  Port

-  Security Group

-  Policies

-  IPAM Creation

the only special characters supported are:

- “ ! $ ‘ ( ) = ~ ^ \| @ \` { } [ ] > , . _

ONAP Output Parameter Names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP defines three types of Output Parameters as detailed in `Output Parameters`_.

ONAP Base Module Output Parameters:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP Base Module Output Parameters do not have an explicit naming
convention. The parameter name must contain {vm-type} and {network-role}
when appropriate.

ONAP Volume Template Output Parameters:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP Base Module Output Parameters do not have an explicit naming
convention. The parameter name must contain {vm-type} when appropriate.

Predefined Output Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP currently defines one predefined output parameter the OAM
Management IP Addresses.

OAM Management IP Addresses
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A VNF may have a management interface for application controllers to
interact with and configure the VNF. Typically, this will be via a
specific VM that performs a VNF administration function. The IP address
of this interface must be captured and inventoried by ONAP. The IP
address might be a VIP if the VNF contains an HA pair of management VMs,
or may be a single IP address assigned to one VM.

The Heat template may define either (or both) of the following Output
parameters to identify the management IP address.

-  oam_management_v4_address

-  oam_management_v6_address

*Notes*:

-  The use of this output parameters are optional.

-  The Management IP Address should be defined only once per VNF, so it
   must only appear in one Module template

-  If a fixed IP for the admin VM is passed as an input parameter, it
   may be echoed in the output parameters. In this case, a IPv4 and/or
   IPv6 parameter must be defined in the parameter section of the YAML
   Heat template. The parameter maybe named oam_management_v4_address
   and/or oam_management_v6_address or may be named differently.

-  If the IP for the admin VM is obtained via DHCP, it may be obtained
   from the resource attributes. In this case,
   oam_management_v4_address and/or oam_management_v6_address must
   not be defined in the parameter section of the YAML Heat template.

*Example: SDN-C Assigned IP Address echoed as*
oam_management_v4_address

.. code-block:: yaml

 parameters:
    admin_oam_ip_0:
       type: string
       description: Fixed IPv4 assignment for admin VM 0 on the OAM network
    . . .

 resources:
    admin_oam_net_0_port:
       type: OS::Neutron::Port
       properties:
          name:
             str_replace:
                template: VNF_NAME_admin_oam_net_0_port
                params:
                   VNF_NAME: {get_param: vnf_name}
          network: { get_param: oam_net_id }
          fixed_ips: [{ "ip_address": { get_param: admin_oam_ip_0 }}]
          security_groups: [{ get_param: security_group }]

    admin_server:
       type: OS::Nova::Server
       properties:
          name: { get_param: admin_names }
          image: { get_param: admin_image_name }
          flavor: { get_param: admin_flavor_name }
          availability_zone: { get_param: availability_zone_0 }
          networks:
             - port: { get_resource: admin_oam_net_0_port }
          metadata:
             vnf_id: { get_param: vnf_id }
             vf_module_id: { get_param: vf_module_id }
             vnf_name: {get_param: vnf_name }
    Outputs:
       oam_management_v4_address:
       value: {get_param: admin_oam_ip_0 }

*Example: Cloud Assigned IP Address output as*
oam_management_v4_address

.. code-block:: yaml

 parameters:
    . . .
 resources:
   admin_oam_net_0_port:
     type: OS::Neutron::Port
     properties:
       name:
         str_replace:
           template: VNF_NAME_admin_oam_net_0_port
           params:
             VNF_NAME: {get_param: vnf_name}
       network: { get_param: oam_net_id }
       security_groups: [{ get_param: security_group }]

   admin_server:
     type: OS::Nova::Server
     properties:
       name: { get_param: admin_names }
       image: { get_param: admin_image_name }
       flavor: { get_param: admin_flavor_name }
       availability_zone: { get_param: availability_zone_0 }
       networks:
         - port: { get_resource: admin_oam_net_0_port }
       metadata:
         vnf_id: { get_param: vnf_id }
         vf_module_id: { get_param: vf_module_id }
         vnf_name: {get_param: vnf_name }

 Outputs:
   oam_management_v4_address:
   value: {get_attr: [admin_server, networks, {get_param: oam_net_id}, 0] }

Contrail Resource Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP requires the parameter names of certain Contrail Resources to
follow specific naming conventions. This section provides these
requirements.

Contrail Network Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Contrail based resources may require references to a Contrail network
using the network FQDN.

External Networks
^^^^^^^^^^^^^^^^^

When the parameter associated with the Contrail Network is referencing
an “external” network, the parameter must adhere to the following naming
convention in the Heat Orchestration Template

-  {network-role}_net_fqdn

The parameter must be declared as type: string

The parameter must not be enumerated in the Heat environment file.

*Example: Parameter declaration*

.. code-block:: yaml

 parameters:
    {network-role}_net_fqdn:
       type: string
       description: Contrail FQDN for the {network-role} network

*Example: Contrail Resource OS::ContrailV2::VirtualMachineInterface
Reference to a Network FQDN.*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} has been defined as fw for firewall.
The Contrail resource OS::ContrailV2::VirtualMachineInterface property
virtual_network_refs references a contrail network FQDN.

.. code-block:: yaml

 FW_OAM_VMI:
   type: OS::ContrailV2::VirtualMachineInterface
   properties:
     name:
       str_replace:
         template: VM_NAME_virtual_machine_interface_1
         params:
           VM_NAME: { get_param: fw_name_0 }
     virtual_machine_interface_properties:
       virtual_machine_interface_properties_service_interface_type: { get_param: oam_protected_interface_type }
     virtual_network_refs:
       - get_param: oam_net_fqdn
     security_group_refs:
       - get_param: fw_sec_grp_id

Interface Route Table Prefixes for Contrail InterfaceRoute Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The parameter associated with the resource
OS::ContrailV2::InterfaceRouteTable property
interface_route_table_routes, map property
interface_route_table_routes_route_prefix is an ONAP Orchestration
Parameter.

The parameters must be named {vm-type}_{network-role}_route_prefixes
in the Heat Orchestration Template.

The parameter must be declared as type: json

The parameter supports IP addresses in the format:

1. Host IP Address (e.g., 10.10.10.10)

2. CIDR Notation format (e.g., 10.0.0.0/28)

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
    {vm-type}_{network-role}_route_prefixes:
       type: json
       description: JSON list of Contrail Interface Route Table route prefixes

*Example:*

.. code-block:: yaml

 parameters:
   vnf_name:
     type: string
     description: Unique name for this VF instance
   fw_int_fw_route_prefixes:
     type: json
     description: prefix for the ServiceInstance InterfaceRouteTable
   int_fw_dns_trusted_interface_type:
     type: string
     description: service_interface_type for ServiceInstance

 <resource name>:
   type: OS::ContrailV2::InterfaceRouteTable
   depends_on: [*resource name of* *OS::ContrailV2::ServiceInstance*]
   properties:
     name:
       str_replace:
         template: VNF_NAME_interface_route_table
         params:
           VNF_NAME: { get_param: vnf_name }
     interface_route_table_routes:
       interface_route_table_routes_route: { get_param: fw_int_fw_route_prefixes }
     service_instance_refs:
       - get_resource: < *resource name of* *OS::ContrailV2::ServiceInstance* >
     service_instance_refs_data:
       - service_instance_refs_data_interface_type: { get_param: int_fw_interface_type }

Parameter Names in Contrail Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Contrail Heat resource properties will use, when appropriate, the same
naming convention as OpenStack Heat resources. For example, the resource
OS::ContrailV2::InstanceIp has two properties that the parameter naming
convention is identical to properties in OS::Neutron::Port.

*Example: Contrail Resource OS::ContrailV2::InstanceIp, Property
instance_ip_address*

The property instance_ip_address uses the same parameter naming
convention as the property fixed_ips and Map Property ip_address in
OS::Neutron::Port. The resource is assigning an ONAP SDN-C Assigned IP
Address. The {network-role} has been defined as oam_protected to
represent an oam protected network and the {vm-type} has been defined as
fw for firewall.

.. code-block:: yaml

 CMD_FW_OAM_PROTECTED_RII:
   type: OS::ContrailV2::InstanceIp
   depends_on:
     - FW_OAM_PROTECTED_RVMI
   properties:
     virtual_machine_interface_refs:
       - get_resource: FW_OAM_PROTECTED_RVMI
     virtual_network_refs:
       - get_param: oam_protected_net_fqdn
     instance_ip_address: { get_param: [fw_oam_protected_ips, get_param: index ] }

*Example: Contrail Resource OS::ContrailV2::InstanceIp, Property
subnet_uuid*

The property instance_ip_address uses the same parameter naming
convention as the property fixed_ips and Map Property subnet_id in
OS::Neutron::Port. The resource is assigning a Cloud Assigned IP
Address. The {network-role} has been defined as “oam_protected” to
represent an oam protected network and the {vm-type} has been defined as
“fw” for firewall.

.. code-block:: yaml

 CMD_FW_SGI_PROTECTED_RII:
   type: OS::ContrailV2::InstanceIp
   depends_on:
     - FW_OAM_PROTECTED_RVMI
   properties:
     virtual_machine_interface_refs:
       - get_resource: FW_OAM_PROTECTED_RVMI
     virtual_network_refs:
       - get_param: oam_protected_net_fqdn
     subnet_uuid: { get_param: oam_protected_subnet_id }

Cinder Volume Templates
^^^^^^^^^^^^^^^^^^^^^^^^

ONAP supports the independent deployment of a Cinder volume via separate
Heat Orchestration Templates, the Cinder Volume module. This allows the
volume to persist after VNF deletion so that they can be reused on
another instance (e.g., during a failover activity).

A Base Module or Incremental Module may have a corresponding volume
module. Use of separate volume modules is optional. A Cinder volume may
be embedded within the Base Module or Incremental Module if persistence
is not required.

If a VNF Base Module or Incremental Module has an independent volume
module, the scope of volume templates must be 1:1 with Base module or
Incremental module. A single volume module must create only the volumes
required by a single Incremental module or Base module.

The following rules apply to independent volume Heat templates:

-  Cinder volumes must be created in a separate Heat Orchestration
   Template from the Base Module or Incremental Module.

   -  A single Cinder volume module must include all Cinder volumes
      needed by the Base/Incremental module.

   -  The volume template must define “outputs” for each Cinder volume
      resource universally unique identifier (UUID) (i.e. ONAP Volume
      Template Output Parameters).

-  The VNF Incremental Module or Base Module must define input
   parameters that match each Volume output parameter (i.e., ONAP Volume
   Template Output Parameters).

   -  ONAP will supply the volume template outputs automatically to the
      bases/incremental template input parameters.

-  Volume modules may utilize nested Heat templates.

*Examples: Volume Template*

A VNF has a Cinder volume module, named incremental_volume.yaml, that
creates an independent Cinder volume for a VM in the module
incremental.yaml. The incremental_volume.yaml defines a parameter in
the output section, lb_volume_id_0 which is the UUID of the cinder
volume. lb_volume_id_0 is defined as a parameter in incremental.yaml.
ONAP captures the UUID value of lb_volume_id_0 from the volume module
output statement and provides the value to the incremental module.

Note that the example below is not a complete Heat Orchestration
Template. The {vm-type} has been defined as “lb” for load balancer

incremental_volume.yaml

.. code-block:: yaml

 parameters:
    vnf_name:
       type: string
    lb_volume_size_0:
       type: number
    ...

 resources:
    dns_volume_0:
       type: OS::Cinder::Volume
       properties:
          name:
             str_replace:
                template: VNF_NAME_volume_0
                params:
                   VNF_NAME: { get_param: vnf_name }
          size: {get_param: dns_volume_size_0}
    ...

 outputs:
    lb_volume_id_0:
       value: {get_resource: dns_volume_0}
    ...


incremental.yaml

.. code-block:: yaml

 parameters:
    lb_name_0:
       type: string
    lb_volume_id_0:
       type: string
    ...

 resources:
    lb_0:
       type: OS::Nova::Server
       properties:
          name: {get_param: dns_name_0}
          networks:
          ...

    lb_0_volume_attach:
       type: OS::Cinder::VolumeAttachment
       properties:
          instance_uuid: { get_resource: lb_0 }
          volume_id: { get_param: lb_volume_id_0 }

ONAP Support of Environment Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The use of an environment file in OpenStack is optional. In ONAP, it is
mandatory. A Heat Orchestration Template uploaded to ONAP must have a
corresponding environment file, even if no parameters are required to be
enumerated.

(Note that ONAP, the open source version of ONAP, does not
programmatically enforce the use of an environment file.)

A Base Module Heat Orchestration Template must have a corresponding
environment file.

An Incremental Module Heat Orchestration Template must have a
corresponding environment file.

A Cinder Volume Module Heat Orchestration Template must have a
corresponding environment file.

A nested heat template must not have an environment file; OpenStack does
not support it.

The environment file must contain parameter values for the ONAP
Orchestration Constants and VNF Orchestration Constants. These
parameters are identical across all instances of a VNF type, and
expected to change infrequently. The ONAP Orchestration Constants are
associated with OS::Nova::Server image and flavor properties (See
`Property: image`_ and `Property: flavor`_). Examples of VNF Orchestration Constants are the networking
parameters associated with an internal network (e.g., private IP ranges)
and Cinder volume sizes.

The environment file must not contain parameter values for parameters
that are instance specific (ONAP Orchestration Parameters, VNF
Orchestration Parameters). These parameters are supplied to the Heat by
ONAP at orchestration time.

SDC Treatment of Environment Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameter values enumerated in the environment file are used by SDC as
the default value. However, the SDC user may use the SDC GUI to
overwrite the default values in the environment file.

SDC generates a new environment file for distribution to MSO based on
the uploaded environment file and the user provided GUI updates. The
user uploaded environment file is discarded when the new file is
created. Note that if the user did not change any values via GUI
updates, the SDC generated environment file will contain the same values
as the uploaded file.

Use of Environment Files when using OpenStack “heat stack-create” CLI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When ONAP is instantiating the Heat Orchestration Template, certain
parameter must not be enumerated in the environment file. This document
provides the details of what parameters should not be enumerated.

If the Heat Orchestration Template is to be instantiated from the
OpenStack Command Line Interface (CLI) using the command “heat
stack-create”, all parameters must be enumerated in the environment
file.

Heat Template Constructs
^^^^^^^^^^^^^^^^^^^^^^^^

Nested Heat Templates
^^^^^^^^^^^^^^^^^^^^^^

ONAP supports nested Heat templates per the OpenStack specifications.
Nested templates may be suitable for larger VNFs that contain many
repeated instances of the same VM type(s). A common usage pattern is to
create a nested template for each {vm-type} along with its supporting
resources. The VNF module may then reference these component templates
either statically by repeated definition or dynamically by using the
resource OS::Heat::ResourceGroup.

Nested Heat Template Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP supports nested Heat Orchestration Templates. A Base Module,
Incremental Module, and Cinder Volume Module may use nested heat.

A Heat Orchestration Template may reference the nested heat statically
by repeated definition.

A Heat Orchestration Template may reference the nested heat dynamically
using the resource OS::Heat::ResourceGroup.

A Heat Orchestration template must have no more than three levels of
nesting. ONAP supports a maximum of three levels.

Nested heat templates must be referenced by file name. The use of
resource_registry in the environment file is not supported and must not
be used.

A nested heat yaml file must have a unique file names within the scope
of the VNF

ONAP does not support a directory hierarchy for nested templates. All
templates must be in a single, flat directory (per VNF)

A nested heat template may be used by any module within a given VNF.

Note that:

-  Constrains must not be defined for any parameter enumerated in a
   nested heat template.

-  All parameters defined in nested heat must be passed in as properties
   of the resource calling the nested yaml file.

-  When OS::Nova::Server metadata parameters are past into a nested heat
   template, the parameter names must not change

-  With nested templates, outputs are required to expose any resource
   properties of the child templates to the parent template. Those would
   not explicitly be declared as parameters but simply referenced as
   get_attribute targets against the “parent” resource.

Nested Heat Template Example: Static
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

incremental.yaml

.. code-block:: yaml

 Resources:
   dns_server_0:
     type: nested.yaml
     properties:
       dns_image_name: { get_param: dns_image_name }
       dns_flavor_name: { get_param: dns_flavor_name }
       availability_zone: { get_param: availability_zone_0 }
       security_group: { get_param: DNS_shared_sec_grp_id }
       oam_net_id: { get_param: oam_protected_net_id }
       dns_oam_ip: { get_param: dns_oam_ip_0 }
       dns_name: { get_param: dns_name_0 }
       vnf_name: { get_param: vnf_name }
       vnf_id: { get_param: vnf_id }
       vf_module_id: {get_param: vf_module_id}

 dns_server_1:
   type: nested.yaml
   properties:
     dns_image_name: { get_param: dns_image_name }
     dns_flavor_name: { get_param: dns_flavor_name }
     availability_zone: { get_param: availability_zone_1 }
     security_group: { get_param: DNS_shared_sec_grp_id }
     oam_net_id: { get_param: oam_protected_net_id }
     dns_oam_ip: { get_param: dns_oam_ip_1 }
     dns_name: { get_param: dns_name_1 }
     vnf_name: { get_param: vnf_name }
     vnf_id: { get_param: vnf_id }
     vf_module_id: {get_param: vf_module_id}

nested.yaml

.. code-block:: yaml

 dns_oam_0_port:
   type: OS::Neutron::Port
   properties:
     name:
       str_replace:
         template: VNF_NAME_dns_oam_port
         params:
           VNF_NAME: {get_param: vnf_name}
     network: { get_param: oam_net_id }
     fixed_ips: [{ "ip_address": { get_param: dns_oam_ip }}]
     security_groups: [{ get_param: security_group }]

 dns_servers:
   type: OS::Nova::Server
   properties:
     name: { get_param: dns_names }
     image: { get_param: dns_image_name }
     flavor: { get_param: dns_flavor_name }
     availability_zone: { get_param: availability_zone }
     networks:
       - port: { get_resource: dns_oam_0_port }
     metadata:
       vnf_id: { get_param: vnf_id }
       vf_module_id: { get_param: vf_module_id }
       vnf_name {get_param: vnf_name }

Use of Heat ResourceGroup
~~~~~~~~~~~~~~~~~~~~~~~~~

The OS::Heat::ResourceGroup is a useful Heat element for creating
multiple instances of a given resource or collection of resources.
Typically it is used with a nested Heat template, to create, for
example, a set of identical OS::Nova::Server resources plus their
related OS::Neutron::Port resources via a single resource in a master
template.

ResourceGroup may be used in ONAP to simplify the structure of a Heat
template that creates multiple instances of the same VM type.

However, there are important caveats to be aware of:

ResourceGroup does not deal with structured parameters
(comma-delimited-list and json) as one might typically expect. In
particular, when using a list-based parameter, where each list element
corresponds to one instance of the ResourceGroup, it is not possible to
use the intrinsic “loop variable” %index% in the ResourceGroup
definition.

For instance, the following is **not** valid Heat for ResourceGroup:

.. code-block:: yaml

 type: OS::Heat::ResourceGroup
   resource_def:
     type: my_nested_vm_template.yaml
     properties:
       name: {get_param: [vm_name_list, %index%]}

Although this appears to use the nth entry of the vm_name_list list
for the nth element of the ResourceGroup, it will in fact result in a
Heat exception. When parameters are provided as a list (one for each
element of a ResourceGroup), you must pass the complete parameter to the
nested template along with the current index as separate parameters.

Below is an example of an **acceptable** Heat Syntax for a
ResourceGroup:

.. code-block:: yaml

 type: OS::Heat::ResourceGroup
   resource_def:
     type: my_nested_vm_template.yaml
     properties:
       names: {get_param: vm_name_list}
       index: %index%

You can then reference within the nested template as:

{ get_param: [names, {get_param: index} ] }

ResourceGroup Property count
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP requires that the OS::Heat::ResourceGroup property count be defined
(even if the value is one) and that the value must be enumerated in the
environment file. This is required for ONAP to build the TOSCA model for
the VNF.

.. code-block:: yaml

 type: OS::Heat::ResourceGroup
   properties:
   count: { get_param: count }
   index_var: index
     resource_def:
       type: my_nested_vm_template.yaml
       properties:
         names: {get_param: vm_name_list}
     index: index

Availability Zone and ResourceGroups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The resource OS::Heat::ResourceGroup and the property availability_zone
has been an “issue” with a few VNFs since ONAP only supports
availability_zone as a string parameter and not a
comma_delimited_list. This makes it difficult to use a ResourceGroup
to create Virtual Machines in more than one availability zone.

There are numerous solutions to this issue. Below are two suggested
usage patterns.

**Option 1:** create a CDL in the OS::Heat::ResourceGroup. In the
resource type: OS::Heat::ResourceGroup, create a comma_delimited_list
availability_zones by using the intrinsic function list_join.

.. code-block:: yaml

 <resource name>:
  type: OS::Heat::ResourceGroup
     properties:
       count: { get_param: node_count }
       index_var: index
       resource_def:
         type: nested.yaml
         properties:
           index: index
           avaialability_zones: { list_join: [',', [ { get_param: availability_zone_0 }, { get_param: availability_zone_1 } ] ] }

In the nested heat

.. code-block:: yaml

 parameters:
   avaialability_zones:
     type: comma_delimited_list
     description:

 resources:
   servers:
     type: OS::Nova::Server
     properties:
       name: { get_param: [ dns_names, get_param: index ] }
       image: { get_param: dns_image_name }
       flavor: { get_param: dns_flavor_name }
       availability_zone: { get_param: [ avaialability_zones, get_param: index ] }


**Option 2:** Create a resource group per availability zone. A separate
OS::Heat::ResourceGroup is created for each availability zone.

External References
^^^^^^^^^^^^^^^^^^^^

Heat templates *should not* reference any HTTP-based resource
definitions, any HTTP-based nested configurations, or any HTTP-based
environment files.

-  During orchestration, ONAP *should not* retrieve any such resources
   from external/untrusted/unknown sources.

-  VNF images should not contain such references in user-data or other
   configuration/operational scripts that are specified via Heat or
   encoded into the VNF image itself.

*Note:* HTTP-based references are acceptable if the HTTP-based reference
is accessing information with the VM private/internal network.

Heat Files Support (get_file)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Heat Templates may contain the inclusion of text files into Heat
templates via the Heat get_file directive. This may be used, for
example, to define a common “user-data” script, or to inject files into
a VM on startup via the “personality” property.

Support for Heat Files is subject to the following limitations:

-  The get_files targets must be referenced in Heat templates by file
   name, and the corresponding files should be delivered to ONAP along
   with the Heat templates.

   -  URL-based file retrieval must not be used; it is not supported.

-  The included files must have unique file names within the scope of
   the VNF.

-  ONAP does not support a directory hierarchy for included files.

   -  All files must be in a single, flat directory per VNF.

-  Included files may be used by all Modules within a given VNF.

-  get_file directives may be used in both non-nested and nested
   templates

Key Pairs
^^^^^^^^^^^^

When Nova Servers are created via Heat templates, they may be passed a
“keypair” which provides an ssh key to the ‘root’ login on the newly
created VM. This is often done so that an initial root key/password does
not need to be hard-coded into the image.

Key pairs are unusual in OpenStack, because they are the one resource
that is owned by an OpenStack User as opposed to being owned by an
OpenStack Tenant. As a result, they are usable only by the User that
created the keypair. This causes a problem when a Heat template attempts
to reference a keypair by name, because it assumes that the keypair was
previously created by a specific ONAP user ID.

When a keypair is assigned to a server, the SSH public-key is
provisioned on the VMs at instantiation time. They keypair itself is not
referenced further by the VM (i.e. if the keypair is updated with a new
public key, it would only apply to subsequent VMs created with that
keypair).

Due to this behavior, the recommended usage of keypairs is in a more
generic manner which does not require the pre-requisite creation of a
keypair. The Heat should be structured in such a way as to:

-  Pass a public key as a parameter value instead of a keypair name

-  Create a new keypair within the VNF Heat templates (in the base
   module) for use within that VNF

By following this approach, the end result is the same as pre-creating
the keypair using the public key – i.e., that public key will be
provisioned in the new VM. However, this recommended approach also makes
sure that a known public key is supplied (instead of having OpenStack
generate a public/private pair to be saved and tracked outside of ONAP).
It also removes any access/ownership issues over the created keypair.

The public keys may be enumerated as a VNF Orchestration Constant in the
environment file (since it is public, it is not a secret key), or passed
at run-time as instance-specific parameters. ONAP will never
automatically assign a public/private key pair.

*Example (create keypair with an existing ssh public-key for {vm-type}
of lb (for load balancer)):*

.. code-block:: yaml

 parameters:
    vnf_name:
       type: string
    lb_ssh_public_key:
       type: string

 resources:
    my_keypair:
       type: OS::Nova::Keypair
       properties:
          name:
             str_replace:
                template: VNF_NAME_key_pair
                params:
                VNF_NAME: { get_param: vnf_name }
          public_key: {get_param: lb_ssh_public_key}
          save_private_key: false

Security Groups
^^^^^^^^^^^^^^^^

OpenStack allows a tenant to create Security groups and define rules
within the security groups.

Security groups, with their rules, may either be created in the Heat
Orchestration Template or they can be pre-created in OpenStack and
referenced within the Heat template via parameter(s). There can be a
different approach for security groups assigned to ports on internal
(intra-VNF) networks or external networks (inter-VNF). Furthermore,
there can be a common security group across all VMs for a specific
network or it can vary by VM (i.e., {vm-type}) and network type (i.e.,
{network-role}).

Anti-Affinity and Affinity Rules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Anti-affinity or affinity rules are supported using normal OpenStack
OS::Nova::ServerGroup resources. Separate ServerGroups are typically
created for each VM type to prevent them from residing on the same host,
but they can be applied to multiple VM types to extend the
affinity/anti-affinity across related VM types as well.

*Example:*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} have been defined as lb for load
balancer and db for database.

.. code-block:: yaml

 resources:
 db_server_group:
    type: OS::Nova::ServerGroup
    properties:
       name:
          str_replace:
             params:
                $vnf_name: {get_param: vnf_name}
             template: $vnf_name-server_group1
       policies:
          - anti-affinity

 lb_server_group:
    type: OS::Nova::ServerGroup
    properties:
       name:
          str_replace:
             params:
                $vnf_name: {get_param: vnf_name}
             template: $vnf_name-server_group2
       policies:
          - affinity

 db_0:
    type: OS::Nova::Server
    properties:
    ...
    scheduler_hints:
       group: {get_resource: db_server_group}

 db_1:
    type: OS::Nova::Server
    properties:
    ...
    scheduler_hints:
       group: {get_resource: db_server_group}

 lb_0:
    type: OS::Nova::Server
    properties:
    ...
    scheduler_hints:
       group: {get_resource: lb_server_group} 

Resource Data Synchronization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For cases where synchronization is required in the orchestration of Heat
resources, two approaches are recommended:

-  Standard Heat depends_on property for resources

   -  Assures that one resource completes before the dependent resource
      is orchestrated.

   -  Definition of completeness to OpenStack may not be sufficient
      (e.g., a VM is considered complete by OpenStack when it is ready
      to be booted, not when the application is up and running).

-  Use of Heat Notifications

   -  Create OS::Heat::WaitCondition and OS::Heat::WaitConditionHandle
      resources.

   -  Pre-requisite resources issue *wc_notify* commands in user_data.

   -  Dependent resource define depends_on in the
      OS::Heat::WaitCondition resource.

*Example: “depends_on” case*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} has been defined as oam to represent an
oam server.

.. code-block:: yaml

 resources:
   oam_server_01:
     type: OS::Nova::Server
     properties:
       name: {get_param: [oam_ names, 0]}
       image: {get_param: oam_image_name}
       flavor: {get_param: oam_flavor_name}
       availability_zone: {get_param: availability_zone_0}
       networks:
         - port: {get_resource: oam01_port_0}
         - port: {get_resource: oam01_port_1}
       user_data:
       scheduler_hints: {group: {get_resource: oam_servergroup}}
       user_data_format: RAW

 oam_01_port_0:
   type: OS::Neutron::Port
   properties:
     network: {get_resource: oam_net_name}
     fixed_ips: [{"ip_address": {get_param: [oam_oam_net_ips, 1]}}]
     security_groups: [{get_resource: oam_security_group}]

 oam_01_port_1:
   type: OS::Neutron::Port
   properties:
     network: {get_param: oam_net_name}
     fixed_ips: [{"ip_address": {get_param: [oam_oam_net_ips, 2]}}]
     security_groups: [{get_resource: oam_security_group}]

 oam_01_vol_attachment:
   type: OS::Cinder::VolumeAttachment
   depends_on: oam_server_01
   properties:
     volume_id: {get_param: oam_vol_1}
     mountpoint: /dev/vdb
     instance_uuid: {get_resource: oam_server_01}

High Availability
^^^^^^^^^^^^^^^^^^

VNF/VM parameters may include availability zone IDs for VNFs that
require high availability.

The Heat must comply with the following requirements to specific
availability zone IDs:

-  The Heat template should spread Nova and Cinder resources across the
   availability zones as desired

Post Orchestration & VNF Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Heat templates should contain a minimum amount of post-orchestration
configuration data. For instance, *do not* embed complex user-data
scripts in the template with large numbers of configuration parameters
to the Heat template.

-  VNFs may provide configuration APIs for use after VNF creation. Such
   APIs will be invoked via application and/or SDN controllers.

*Note:* It is important to follow this convention to the extent possible
even in the short-term as of the long-term direction.

c. VNFM Driver Development Steps
--------------------------------

Refer to the ONAP documentation for VNF provider instructions on integrating
special VNFM adaptors with VF-C.  The VNF driver development steps are
highlighted below.

1. Use the VNF SDK tools to design the VNF with TOSCA models to output
the VNF TOSCA package.  Using the VNF SDK tools, the VNF package can be
validated and tested.

2. The VNF provider can provide a special VNFM driver in ONAP, which
is a microservice providing a translation interface from VF-C to
the special VNFM. The interface definitions of special VNFM adaptors are provided by
the VNF providers themselves.

d. Creating Special VNFM Adaptor Microservices
----------------------------------------------

VNFs can be managed by special VNFMs. To add a special VNFM to ONAP, a
special VNFM adaptor is added to ONAP implementing the interface of the special VNFM.

A special VNFM adaptor is a microservice with a unique name and an appointed
port. When started up, the special VNFM adaptor microservice is automatically registered to the
Microservices Bus (MSB). The following RESTful example describes the scenario of
registering a special VNFM adaptor to MSB:

.. code-block:: java

    POST /api/microservices/v1/services
    {
        "serviceName": "catalog",
        "version": "v1",
        "url": "/api/catalog/v1",
        "protocol": "REST",
        "visualRange": "1",
        "nodes": [
        {
            "ip": "10.74.56.36",
            "port": "8988",
            "ttl": 0
        }
        ]
    }


**6. Infrastructure Requirements**
=====================================

This Amsterdam release of the requirements is targeted for those implementations that consist of Network Clouds: Vanilla OpenStack (based on Ocata_) and commercial Clouds for example: OpenStack (including `Titanium - Mitaka from Wind River`_ and `VIO - Ocata from VMware`_). Future versions of ONAP are envisioned to include other targeted cloud infrastructure implementations, for example, on-premise private cloud, public cloud, or hybrid cloud implementations, and related network backends, e.g. `Microsoft Azure`_ et al.

.. _Ocata: https://releases.openstack.org/ocata/
.. _Titanium - Mitaka from Wind River: https://www.windriver.com/products/titanium-cloud/
.. _`VIO - Ocata from VMware`: https://www.vmware.com/products/openstack.html
.. _`Microsoft Azure`: https://azure.microsoft.com

**7. ONAP Management Requirements**
=====================================

a. Service Design
-----------------

This section, Service Design, has been left intentionally blank. It is out-of-scope for the VNF Requirements project for the Amsterdam release and no numbered requirements are expected. Content may be added in future updates of this document.

b. VNF On-boarding and package management
-----------------------------------------

**Design Definition**

The ONAP Design Time Framework provides the ability to design NFV
resources including VNFs, Services, and products. The VNF provider must
provide VNF packages that include a rich set of recipes, management and
functional interfaces, policies, configuration parameters, and
infrastructure requirements that can be utilized by the ONAP Design
module to onboard and catalog these resources. Initially this
information may be provided in documents, but in the near future a
method will be developed to automate as much of the transfer of data as
possible to satisfy its long term requirements.

The current VNF Package Requirement is based on a subset of the
Requirements contained in the ETSI Document: ETSI GS NFV-MAN 001 v1.1.1
and GS NFV IFA011 V0.3.0 (2015-10) - Network Functions Virtualization
(NFV), Management and Orchestration, VNF Packaging Specification.

**Resource Description**

* R-77707 The VNF provider **MUST** include a Manifest File that contains a list of all the components in the VNF package.
* R-66070 The VNF Package **MUST** include VNF Identification Data to uniquely identify the resource for a given VNF provider. The identification data must include: an identifier for the VNF, the name of the VNF as was given by the VNF provider, VNF description, VNF provider, and version.
* R-69565 The VNF Package **MUST** include documentation describing VNF Management APIs. The document must include information and tools for:

 - ONAP to deploy and configure (initially and ongoing) the VNF application(s) (e.g., NETCONF APIs). Includes description of configurable parameters for the VNF and whether the parameters can be configured after VNF instantiation.
 - ONAP to monitor the health of the VNF (conditions that require healing and/or scaling responses). Includes a description of:

  - Parameters that can be monitored for the VNF and event records (status, fault, flow, session, call, control plane, etc.) generated by the VNF after instantiation.
  - Runtime lifecycle events and related actions (e.g., control responses, tests) which can be performed for the VNF.

* R-84366 The VNF Package **MUST** include documentation describing VNF Functional APIs that are utilized to build network and application services. This document describes the externally exposed functional inputs and outputs for the VNF, including interface format and protocols supported.
* R-36280 The VNF provider **MUST** provide documentation describing VNF Functional Capabilities that are utilized to operationalize the VNF and compose complex services.
* R-98617 The VNF provider **MUST** provide information regarding any dependency (e.g., affinity, anti-affinity) with other VNFs and resources.

**Resource Configuration**

* R-89571 The VNF **MUST** support and provide artifacts for configuration management using at least one of the following technologies:

 - Netconf/YANG
 - Chef
 - Ansible

 Note: The requirements for Netconf/YANG, Chef, and Ansible protocols are provided separately and must be supported only if the corresponding protocol option is provided by the VNF providor.

 **Configuration Management via Netconf/YANG**

 * R-30278 The VNF provider **MUST** provide a Resource/Device YANG model as a foundation for creating the YANG model for configuration. This will include VNF attributes/parameters and valid values/attributes configurable by policy.

 **Configuration Management via Chef**

 * R-13390 The VNF provider **MUST** provide cookbooks to be loaded on the appropriate Chef Server.
 * R-18525 The VNF provider **MUST** provide a JSON file for each supported action for the VNF.  The JSON file must contain key value pairs with all relevant values populated with sample data that illustrates its usage. The fields and their description are defined in Appendix A.

 Note: Chef support in ONAP is not currently available and planned for 4Q 2017.

 **Configuration Management via Ansible**

 * R-75608 The VNF provider **MUST** provide playbooks to be loaded on the appropriate Ansible Server.
 * R-16777 The VNF provider **MUST** provide a JSON file for each supported action for the VNF.  The JSON file must contain key value pairs with all relevant values populated with sample data that illustrates its usage. The fields and their description are defined in Appendix B.

* R-46567 The VNF Package **MUST** include configuration scripts for boot sequence and configuration.
* R-16065 The VNF provider **MUST** provide configurable parameters (if unable to conform to YANG model) including VNF attributes/parameters and valid values, dynamic attributes and cross parameter dependencies (e.g., customer provisioning data).

**Resource Control Loop**

* R-22888 The VNF provider **MUST** provide documentation for the VNF Policy Description to manage the VNF runtime lifecycle. The document must include a description of how the policies (conditions and actions) are implemented in the VNF.
* R-01556 The VNF Package **MUST** include documentation describing the fault, performance, capacity events/alarms and other event records that are made available by the VNF. The document must include:

 - A unique identification string for the specific VNF, a description of the problem that caused the error, and steps or procedures to perform Root Cause Analysis and resolve the issue.
 - All events, severity level (e.g., informational, warning, error) and descriptions including causes/fixes if applicable for the event.
 - All events (fault, measurement for VNF Scaling, Syslogs, State Change and Mobile Flow), that need to be collected at each VM, VNFC (defined in *VNF Guidelines for Network Cloud and ONAP*) and for the overall VNF.

* R-27711 The VNF provider **MUST** provide an XML file that contains a list of VNF error codes, descriptions of the error, and possible causes/corrective action.
* R-01478 The VNF Package **MUST** include documentation describing all parameters that are available to monitor the VNF after instantiation (includes all counters, OIDs, PM data, KPIs, etc.) that must be collected for reporting purposes. The documentation must include a list of:

 - Monitoring parameters/counters exposed for virtual resource management and VNF application management.
 - KPIs and metrics that need to be collected at each VM for capacity planning and performance management purposes.
 - The monitoring parameters must include latencies, success rates, retry rates, load and quality (e.g., DPM) for the key transactions/functions supported by the VNF and those that must be exercised by the VNF in order to perform its function.
 - For each KPI, provide lower and upper limits.
 - When relevant, provide a threshold crossing alert point for each KPI and describe the significance of the threshold crossing.
 - For each KPI, identify the suggested actions that need to be performed when a threshold crossing alert event is recorded.
 - Describe any requirements for the monitoring component of tools for Network Cloud automation and management to provide these records to components of the VNF.
 - When applicable, provide calculators needed to convert raw data into appropriate reporting artifacts.

* R-56815 The VNF Package **MUST** include documentation describing supported VNF scaling capabilities and capacity limits (e.g., number of users, bandwidth, throughput, concurrent calls).
* R-48596 The VNF Package **MUST** include documentation describing the characteristics for the VNF reliability and high availability.
* R-74763 The VNF provider **MUST** provide an artifact per VNF that contains all of the VNF Event Records supported. The artifact should include reference to the specific release of the VNF Event Stream Common Event Data Model document it is based on. (e.g., `VES Event Listener <https://github.com/att/evel-test-collector/tree/master/docs/att_interface_definition>`__)

**Compute, Network, and Storage Requirements**

* R-35851 The VNF Package **MUST** include VNF topology that describes basic network and application connectivity internal and external to the VNF including Link type, KPIs, Bandwidth, latency, jitter, QoS (if applicable) for each interface.
* R-97102 The VNF Package **MUST** include VM requirements via a Heat template that provides the necessary data for:

 - VM specifications for all VNF components - for hypervisor, CPU, memory, storage.
 - Network connections, interface connections, internal and external to VNF.
 - High availability redundancy model.
 - Scaling/growth VM specifications.

 Note: Must comply with the *Heat requirements in 5.b*.

* R-26881 The VNF provider **MUST** provide the binaries and images needed to instantiate the VNF (VNF and VNFC images).
* R-96634 The VNF provider **MUST** describe scaling capabilities to manage scaling characteristics of the VNF.


**Testing**

* R-43958 The VNF Package **MUST** include documentation describing the tests that were conducted by the VNF providor and the test results.
* R-04298 The VNF provider **MUST** provide their testing scripts to support testing.
* R-58775 The VNF provider **MUST** provide software components that can be packaged with/near the VNF, if needed, to simulate any functions or systems that connect to the VNF system under test. This component is necessary only if the existing testing environment does not have the necessary simulators.

**Licensing Requirements**

* R-85653 The VNF **MUST** provide metrics (e.g., number of sessions, number of subscribers, number of seats, etc.) to ONAP for tracking every license.
* R-44125 The VNF provider **MUST** agree to the process that can be met by Service Provider reporting infrastructure. The Contract shall define the reporting process and the available reporting tools.
* R-40827 The VNF provider **MUST** enumerate all of the open source licenses their VNF(s) incorporate.
* R-97293 The VNF provider **MUST NOT** require audits of Service Provider’s business.
* R-44569 The VNF provider **MUST NOT** require additional infrastructure such as a VNF provider license server for VNF provider functions and metrics.
* R-13613 The VNF **MUST** provide clear measurements for licensing purposes to allow automated scale up/down by the management system.
* R-27511 The VNF provider **MUST** provide the ability to scale up a VNF provider supplied product during growth and scale down a VNF provider supplied product during decline without “real-time” restrictions based upon VNF provider permissions.
* R-85991 The VNF provider **MUST** provide a universal license key per VNF to be used as needed by services (i.e., not tied to a VM instance) as the recommended solution. The VNF provider may provide pools of Unique VNF License Keys, where there is a unique key for each VNF instance as an alternate solution. Licensing issues should be resolved without interrupting in-service VNFs.
* R-47849 The VNF provider **MUST** support the metadata about licenses (and their applicable entitlements) as defined in this document for VNF software, and any license keys required to authorize use of the VNF software.  This metadata will be used to facilitate onboarding the VNF into the ONAP environment and automating processes for putting the licenses into use and managing the full lifecycle of the licenses. The details of this license model are described in Appendix C. Note: License metadata support in ONAP is not currently available and planned for 1Q 2018.

c. Configuration Management
---------------------------

ONAP interacts directly with VNFs through its Network and Application
Adapters to perform configuration activities within NFV environment.
These activities include service and resource
configuration/reconfiguration, automated scaling of resources, service
and resource removal to support runtime lifecycle management of VNFs and
services. The Adapters employ a model driven approach along with
standardized APIs provided by the VNF developers to configure resources
and manage their runtime lifecycle.

Additional details can be found in the `ONAP Application Controller (APPC) API Guide <http://onap.readthedocs.io/en/latest/submodules/appc.git/docs/APPC%20API%20Guide/APPC%20API%20Guide.html>`_, `ONAP VF-C project <http://onap.readthedocs.io/en/latest/submodules/vfc/nfvo/lcm.git/docs/index.html>`_ and the `ONAP SDNC project <http://onap.readthedocs.io/en/latest/submodules/sdnc/northbound.git/docs/index.html>`_.

NETCONF Standards and Capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP Controllers and their Adapters utilize device YANG model and
NETCONF APIs to make the required changes in the VNF state and
configuration. The VNF providers must provide the Device YANG model and
NETCONF server supporting NETCONF APIs to comply with target ONAP and
industry standards.

**VNF Configuration via NETCONF Requirements**

**Configuration Management**

* R-88026 The VNF **MUST** include a NETCONF server enabling runtime configuration and lifecycle management capabilities.
* R-95950 The VNF **MUST** provide a NETCONF interface fully defined by supplied YANG models for the embedded NETCONF server.

**NETCONF Server Requirements**

* R-73468 The VNF **MUST** allow the NETCONF server connection parameters to be configurable during virtual machine instantiation through Heat templates where SSH keys, usernames, passwords, SSH service and SSH port numbers are Heat template parameters.
* R-90007 The VNF **MUST** implement the protocol operation: **close-session()**- Gracefully close the current session.
* R-70496 The VNF **MUST** implement the protocol operation: **commit(confirmed, confirm-timeout)** - Commit candidate configuration datastore to the running configuration.
* R-18733 The VNF **MUST** implement the protocol operation: **discard-changes()** - Revert the candidate configuration datastore to the running configuration.
* R-44281 The VNF **MUST** implement the protocol operation: **edit-config(target, default-operation, test-option, error-option, config)** - Edit the target configuration datastore by merging, replacing, creating, or deleting new config elements.
* R-60106 The VNF **MUST** implement the protocol operation: **get(filter)** - Retrieve (a filtered subset of) the running configuration and device state information. This should include the list of VNF supported schemas.
* R-29488 The VNF **MUST** implement the protocol operation: **get-config(source, filter)** - Retrieve a (filtered subset of a) configuration from the configuration datastore source.
* R-11235 The VNF **MUST** implement the protocol operation: **kill-session(session)** - Force the termination of **session**.
* R-02597 The VNF **MUST** implement the protocol operation: **lock(target)** - Lock the configuration datastore target.
* R-96554 The VNF **MUST** implement the protocol operation: **unlock(target)** - Unlock the configuration datastore target.
* R-29324 The VNF **SHOULD** implement the protocol operation: **copy-config(target, source) -** Copy the content of the configuration datastore source to the configuration datastore target.
* R-88031 The VNF **SHOULD** implement the protocol operation: **delete-config(target) -** Delete the named configuration datastore target.
* R-97529 The VNF **SHOULD** implement the protocol operation: **get-schema(identifier, version, format) -** Retrieve the YANG schema.
* R-62468 The VNF **MUST** allow all configuration data shall to be edited through a NETCONF <edit-config> operation. Proprietary NETCONF RPCs that make configuration changes are not sufficient.
* R-01382 The VNF **MUST** allow the entire configuration of the VNF to be retrieved via NETCONF's <get-config> and <edit-config>, independently of whether it was configured via NETCONF or other mechanisms.
* R-28756 The VNF **MUST** support **:partial-lock** and **:partial-unlock** capabilities, defined in RFC 5717. This allows multiple independent clients to each write to a different part of the <running> configuration at the same time.
* R-83873 The VNF **MUST** support **:rollback-on-error** value for the <error-option> parameter to the <edit-config> operation. If any error occurs during the requested edit operation, then the target database (usually the running configuration) will be left unaffected. This provides an 'all-or-nothing' edit mode for a single <edit-config> request.
* R-68990 The VNF **MUST** support the **:startup** capability. It will allow the running configuration to be copied to this special database. It can also be locked and unlocked.
* R-68200 The VNF **MUST** support the **:url** value to specify protocol operation source and target parameters. The capability URI for this feature will indicate which schemes (e.g., file, https, sftp) that the server supports within a particular URL value. The 'file' scheme allows for editable local configuration databases. The other schemes allow for remote storage of configuration databases.
* R-20353 The VNF **MUST** implement at least one of the capabilities **:candidate** or **:writable-running**. If both **:candidate** and **:writable-running** are provided then two locks should be supported.
* R-11499 The VNF **MUST** fully support the XPath 1.0 specification for filtered retrieval of configuration and other database contents. The 'type' attribute within the <filter> parameter for <get> and <get-config> operations may be set to 'xpath'. The 'select' attribute (which contains the XPath expression) will also be supported by the server. A server may support partial XPath retrieval filtering, but it cannot advertise the **:xpath** capability unless the entire XPath 1.0 specification is supported.
* R-83790 The VNF **MUST** implement the **:validate** capability
* R-49145 The VNF **MUST** implement **:confirmed-commit** If **:candidate** is supported.
* R-58358 The VNF **MUST** implement the **:with-defaults** capability [RFC6243].
* R-59610 The VNF **MUST** implement the data model discovery and download as defined in [RFC6022].
* R-87662 The VNF **SHOULD** implement the NETCONF Event Notifications [RFC5277].
* R-93443 The VNF **MUST** define all data models in YANG [RFC6020], and the mapping to NETCONF shall follow the rules defined in this RFC.
* R-26115 The VNF **MUST** follow the data model upgrade rules defined in [RFC6020] section 10. All deviations from section 10 rules shall be handled by a built-in automatic upgrade mechanism.
* R-10716 The VNF **MUST** support parallel and simultaneous configuration of separate objects within itself.
* R-29495 The VNF **MUST** support locking if a common object is being manipulated by two simultaneous NETCONF configuration operations on the same VNF within the context of the same writable running data store (e.g., if an interface parameter is being configured then it should be locked out for configuration by a simultaneous configuration operation on that same interface parameter).
* R-53015 The VNF **MUST** apply locking based on the sequence of NETCONF operations, with the first configuration operation locking out all others until completed.
* R-02616 The VNF **MUST** permit locking at the finest granularity if a VNF needs to lock an object for configuration to avoid blocking simultaneous configuration operations on unrelated objects (e.g., BGP configuration should not be locked out if an interface is being configured or entire Interface configuration should not be locked out if a non-overlapping parameter on the interface is being configured).
* R-41829 The VNF **MUST** be able to specify the granularity of the lock via a restricted or full XPath expression.
* R-66793 The VNF **MUST** guarantee the VNF configuration integrity for all simultaneous configuration operations (e.g., if a change is attempted to the BUM filter rate from multiple interfaces on the same EVC, then they need to be sequenced in the VNF without locking either configuration method out).
* R-54190 The VNF **MUST** release locks to prevent permanent lock-outs when/if a session applying the lock is terminated (e.g., SSH session is terminated).
* R-03465 The VNF **MUST** release locks to prevent permanent lock-outs when the corresponding <partial-unlock> operation succeeds.
* R-63935 The VNF **MUST** release locks to prevent permanent lock-outs when a user configured timer has expired forcing the NETCONF SSH Session termination (i.e., product must expose a configuration knob for a user setting of a lock expiration timer)
* R-10173 The VNF **MUST** allow another NETCONF session to be able to initiate the release of the lock by killing the session owning the lock, using the <kill-session> operation to guard against hung NETCONF sessions.
* R-88899 The VNF **MUST** support simultaneous <commit> operations within the context of this locking requirements framework.
* R-07545 The VNF **MUST** support all operations, administration and management (OAM) functions available from the supplier for VNFs using the supplied YANG code and associated NETCONF servers.
* R-60656 The VNF **MUST** support sub tree filtering.
* R-80898 The VNF **MUST** support heartbeat via a <get> with null filter.
* R-06617 The VNF **MUST** support get-schema (ietf-netconf-monitoring) to pull YANG model over session.
* R-25238 The VNF PACKAGE **MUST** validated YANG code using the open source pyang [1]_ program using the following commands:

.. code-block:: python

 $ pyang --verbose --strict <YANG-file-name(s)>
 $ echo $!

* R-63953 The VNF **MUST** have the echo command return a zero value otherwise the validation has failed
* R-26508 The VNF **MUST** support NETCONF server that can be mounted on OpenDaylight (client) and perform the following operations:

- Modify, update, change, rollback configurations using each configuration data element.
- Query each state (non-configuration) data element.
- Execute each YANG RPC.
- Receive data through each notification statement.



The following requirements provides the Yang models that suppliers must
conform, and those where applicable, that suppliers need to use.

* R-28545 The VNF **MUST** conform its YANG model to RFC 6060, “YANG - A Data Modeling Language for the Network Configuration Protocol (NETCONF)”
* R-29967 The VNF **MUST** conform its YANG model to RFC 6022, “YANG module for NETCONF monitoring”.
* R-22700 The VNF **MUST** conform its YANG model to RFC 6470, “NETCONF Base Notifications”.
* R-10353 The VNF **MUST** conform its YANG model to RFC 6244, “An Architecture for Network Management Using NETCONF and YANG”.
* R-53317 The VNF **MUST** conform its YANG model to RFC 6087, “Guidelines for Authors and Reviewers of YANG Data Model Documents”.
* R-33955 The VNF **SHOULD** conform its YANG model to \*\*RFC 6991, “Common YANG Data Types”.
* R-22946 The VNF **SHOULD** conform its YANG model to RFC 6536, “NETCONF Access Control Model”.
* R-10129 The VNF **SHOULD** conform its YANG model to RFC 7223, “A YANG Data Model for Interface Management”.
* R-12271 The VNF **SHOULD** conform its YANG model to RFC 7223, “IANA Interface Type YANG Module”.
* R-49036 The VNF **SHOULD** conform its YANG model to RFC 7277, “A YANG Data Model for IP Management”.
* R-87564 The VNF **SHOULD** conform its YANG model to RFC 7317, “A YANG Data Model for System Management”.
* R-24269 The VNF **SHOULD** conform its YANG model to RFC 7407, “A YANG Data Model for SNMP Configuration”.

The NETCONF server interface shall fully conform to the following
NETCONF RFCs.

* R-33946 The VNF **MUST** conform to the NETCONF RFC 4741, “NETCONF Configuration Protocol”.
* R-04158 The VNF **MUST** conform to the NETCONF RFC 4742, “Using the NETCONF Configuration Protocol over Secure Shell (SSH)”.
* R-13800 The VNF **MUST** conform to the NETCONF RFC 5277, “NETCONF Event Notification”.
* R-01334 The VNF **MUST** conform to the NETCONF RFC 5717, “Partial Lock Remote Procedure Call”.
* R-08134 The VNF **MUST** conform to the NETCONF RFC 6241, “NETCONF Configuration Protocol”.
* R-78282 The VNF **MUST** conform to the NETCONF RFC 6242, “Using the Network Configuration Protocol over Secure Shell”.

VNF REST APIs
^^^^^^^^^^^^^^

Healthcheck is a command for which no NETCONF support exists. Therefore, this must be supported using a RESTful interface (defined in this section) or
with a Chef cookbook/Ansible playbook (defined in sections `Chef Standards and Capabilities`_ and `Ansible Standards and Capabilities`_).

HealthCheck Definition: The VNF level HealthCheck is a check over the entire scope of the VNF.
The VNF must be 100% healthy, ready to take requests and provide services, with all VNF required
capabilities ready to provide services and with all active and standby resources fully ready with
no open MINOR, MAJOR or CRITICAL alarms.  NOTE: A switch may need to be turned on, but the VNF
should be ready to take service requests or be already processing service requests successfully.

The VNF must provide a REST formatted GET RPCs to support Healthcheck queries via the GET method
over HTTP(s).

The port number, url, and other authentication information is provided
by the VNF provider.

**REST APIs**

* R-31809 The VNF **MUST** support the HealthCheck RPC. The HealthCheck RPC executes a VNF Provider-defined VNF Healthcheck over the scope of the entire VNF (e.g., if there are multiple VNFCs, then run a health check, as appropriate, for all VNFCs). It returns a 200 OK if the test completes. A JSON object is returned indicating state (healthy, unhealthy), scope identifier, time-stamp and one or more blocks containing info and fault information. If the VNF is unable to run the HealthCheck, return a standard http error code and message.

Examples:

.. code-block:: java

 200
 {
   "identifier": "scope represented",
   "state": "healthy",
   "time": "01-01-1000:0000"
 }

 200
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

**VNF Configuration via Chef Requirements**

**Chef Client Requirements**

* R-79224 The VNF **MUST** have the chef-client be preloaded with validator keys and configuration to register with the designated Chef Server as part of the installation process.
* R-72184 The VNF **MUST** have routable FQDNs for all the endpoints (VMs) of a VNF that contain chef-clients which are used to register with the Chef Server.  As part of invoking VNF actions, ONAP will trigger push jobs against FQDNs of endpoints for a VNF, if required.
* R-47068 The VNF **MAY** expose a single endpoint that is responsible for all functionality.
* R-67114 The VNF **MUST** be installed with:

 -  Chef-Client >= 12.0
 -  Chef push jobs client >= 2.0

**Chef Roles/Requirements**

* R-27310 The VNF Package **MUST** include all relevant Chef artifacts (roles/cookbooks/recipes) required to execute VNF actions requested by ONAP for loading on appropriate Chef Server.
* R-26567 The VNF Package **MUST** include a run list of roles/cookbooks/recipes, for each supported VNF action, that will perform the desired VNF action in its entirety as specified by ONAP (see Section 8.c, ONAP Controller APIs and Behavior, for list of VNF actions and requirements), when triggered by a chef-client run list in JSON file.
* R-98911 The VNF **MUST NOT** use any instance specific parameters for the VNF in roles/cookbooks/recipes invoked for a VNF action.
* R-37929 The VNF **MUST** accept all necessary instance specific data from the environment or node object attributes for the VNF in roles/cookbooks/recipes invoked for a VNF action.
* R-62170 The VNF **MUST** over-ride any default values for configurable parameters that can be set by ONAP in the roles, cookbooks and recipes.
* R-78116 The VNF **MUST** update status on the Chef Server appropriately (e.g., via a fail or raise an exception) if the chef-client run encounters any critical errors/failures when executing a VNF action.
* R-44013 The VNF **MUST** populate an attribute, defined as node[‘PushJobOutput’] with the desired output on all nodes in the push job that execute chef-client run if the VNF action requires the output of a chef-client run be made available (e.g., get running configuration).
* R-30654 The VNF Package **MUST** have appropriate cookbooks that are designed to automatically ‘rollback’ to the original state in case of any errors for actions that change state of the VNF (e.g., configure).
* R-65755 The VNF **SHOULD** support callback URLs to return information to ONAP upon completion of the chef-client run for any chef-client run associated with a VNF action.

-  As part of the push job, ONAP will provide two parameters in the environment of the push job JSON object:
    -  ‘RequestId’ a unique Id to be used to identify the request,
    -  ‘CallbackUrl’, the URL to post response back.

-  If the CallbackUrl field is empty or missing in the push job, then the chef-client run need not post the results back via callback.

* R-15885 The VNF **MUST** Upon completion of the chef-client run, POST back on the callback URL, a JSON object as described in Table A2 if the chef-client run list includes a cookbook/recipe that is callback capable. Failure to POST on the Callback Url should not be considered a critical error. That is, if the chef-client successfully completes the VNF action, it should reflect this status on the Chef Server regardless of whether the Callback succeeded or not.

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
     "run_timeout": 300,
     "nodes”: [“node1.vnf_a.onap.com”, “node2.vnf_a.onap.com”],
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP will support configuration of VNFs via Ansible subject to the
requirements and guidelines defined in this section.

Ansible allows agentless management of VNFs/VMs/VNFCs via execution of ‘playbooks’
over ssh. The ‘playbooks’ are a structured set of tasks which contain all the necessary
data and execution capabilities to take the necessary action on one or more target VMs
(and/or VNFCs) of the VNF. ONAP will utilize the framework of an Ansible Server that
will host and run playbooks to manage VNFs that support Ansible.

**VNF Configuration via Ansible Requirements**

**Ansible Client Requirements**

* R-32217 The VNF **MUST** have routable FQDNs that are reachable via the Ansible Server for the endpoints (VMs) of a VNF on which playbooks will be executed. ONAP will initiate requests to the Ansible Server for invocation of playbooks against these end points [3]_.
* R-54373 The VNF **MUST** have Python >= 2.7 on the endpoint VM(s) of a VNF on which an Ansible playbook will be executed.
* R-35401 The VNF **MUST** support SSH and allow SSH access to the Ansible server for the endpoint VM(s) and comply with the  Network Cloud Service Provider guidelines for authentication and access.
* R-NNNNN The VNF **SHOULD** load the SSH key onto VNF VM(s) as part of instantiation. This will allow the Ansible Server to authenticate to perform post-instantiation configuration without manual intervention and without requiring specific VNF login IDs and passwords.

 CAUTION: For VNFs configured using Ansible, to eliminate the need for manual steps, post-instantiation and pre-configuration, to upload of SSH keys, SSH keys loaded during (heat) instantiation shall be preserved and not removed by (heat) embedded scripts.

* R-NNNNN The VNF **MUST** include as part of post-instantiation configuration done by Ansible Playbooks the removal/update of SSH keys loaded through instantiation to support Ansible. This may include download and install of new SSH keys.
* R-NNNNN The VNF **MUST** update the Ansible Server and other entities storing and using the SSH key for authentication when the SSH key used by Ansible is regenerated/updated.

**Ansible Playbook Requirements**

An Ansible playbook is a collection of tasks that is executed on the Ansible server (local host) and/or the target VM (s) in order to complete the desired action.

* R-40293 The VNF **MUST** make available playbooks that conform to the ONAP requirement.
* R-49396 The VNF **MUST** support each VNF action be supported by ONAP (APPC) by invocation of **one** playbook [4]_. The playbook will be responsible for executing all necessary tasks (as well as calling other playbooks) to complete the request.
* R-33280 The VNF **MUST NOT** use any instance specific parameters in a playbook.
* R-48698 The VNF **MUST** utilize information from key value pairs that will be provided by the Ansible Server as extra-vars during invocation to execute the desired VNF action. If the playbook requires files, they must also be supplied using the methodology detailed in the Ansible Server API.

The Ansible Server will determine if a playbook invoked to execute a VNF action finished successfully or not using the “PLAY_RECAP” summary in Ansible log.  The playbook will be considered to successfully finish only if the “PLAY RECAP” section at the end of playbook execution output has no unreachable hosts and no failed tasks. Otherwise, the playbook will be considered to have failed.

* R-43253 The VNF **MUST** use playbooks designed to allow Ansible Server to infer failure or success based on the “PLAY_RECAP” capability.
* R-50252 The VNF **MUST** write to a specific set of text files that will be retrieved and made available by the Ansible Server if, as part of a VNF action (e.g., audit), a playbook is required to return any VNF information. The text files must be written in the same directory as the one from which the playbook is being executed. A text file must be created for each host the playbook run targets/affects, with the name ‘<hostname>_results.txt’ into which any desired output from each respective VM/VNF must be written.
* R-51442 The VNF **SHOULD** use playbooks that are designed to automatically ‘rollback’ to the original state in case of any errors for actions that change state of the VNF (e.g., configure).

 NOTE: In case rollback at the playbook level is not supported or possible, the VNF provider shall provide alternative locking mechanism (e.g., for a small VNF the rollback mechanism may rely on workflow to terminate and re-instantiate VNF VMs and then re-run playbook(s)). Backing up updated files also recommended to support rollback when soft rollback is feasible.

* R-NNNNN The VNF **SHOULD NOT** use playbooks that make requests to Cloud resources e.g. Openstack (nova, neutron, glance, heat, etc.); therefore, there is no use for Cloud specific variables like Openstack UUIDs in Ansible Playbooks.

 Rationale: Flows that require interactions with Cloud services e.g. Openstack shall rely on workflows run by an Orchestrator or other capability (such as a control loop or Operations GUI) outside Ansible Server which can be executed by a Controller such as APPC.  There are policies, as part of Control Loop models, that send remediation action requests to APPC; these are triggered as a response to an event or correlated events published to Event Bus.

* R-NNNNN The VNF **SHOULD** use the Ansible backup feature to save a copy of configuration files before implementing changes to support operations such as backing out of software upgrades, configuration changes or other work as this will help backing out of configuration changes when needed.
* R-NNNNN The VNF **MUST** return control from Ansible Playbooks only after tasks are fully complete, signaling that the playbook completed all tasks. When starting services, return control only after all services are up. This is critical for workflows where the next steps are dependent on prior tasks being fully completed.

 Detailed examples:

 StopApplication Playbook – StopApplication Playbook shall return control and a completion status only after VNF application is fully stopped, all processes/services stopped.
 StartApplication Playbook – StartApplication Playbook shall return control and a completion status only after all VNF application services are fully up, all processes/services started and ready to provide services. NOTE: Start Playbook should not be declared complete/done after starting one or several processes that start the other processes.

 HealthCheck Playbook:

 SUCCESS – HealthCheck success shall be returned (return code 0) by a Playbook or Cookbook only when VNF is 100% healthy, ready to take requests and provide services, with all VNF required capabilities ready to provide services and with all active and standby resources fully ready with no open MINOR, MAJOR or CRITICAL alarms.

 NOTE: In some cases, a switch may need to be turned on, but a VNF reported as healthy, should be ready to take service requests or be already processing service requests successfully.

 A successful execution of a health-check playbook shall also create one file per VNF VM, named using IP address or VM name followed by “_results.txt (<hostname>_results.txt) to indicate health-check was executed and completed successfully, example: 1xx.2yy.zzz.105_results.txt, with the following contents:

 "status”:"healthy”

 Example:

 $ cat 1xx.2yy.zzz.105_results.txt

 "status”:"healthy”

 FAILURE – A health check playbook shall return a non-zero return code in case VNF is not 100% healthy because one or more VNF application processes are stopped or not ready to take service requests or because critical or non-critical resources are not ready or because there are open MINOR, MAJOR or CRITICAL traps/alarms or because there are issues with the VNF that need attention even if they do not impact services provided by the VNF.

 A failed health-check playbook shall also create one file per VNF VM, named using Playbook Name plus IP address or VM name, followed by “_results.txt to indicate health-check was executed and found issues in the health of the VNF. This is to differentiate from failure to run health-check playbook or tasks to verify the health of the VNF, example: 1xx.2yy.zzz.105_results.txt, with the following contents:

 "status”:"unhealthy”

 Example:

 $ cat 1xx.2yy.zzz.105_results.txt

 "status”:"unhealthy”

 See `VNF REST APIs`_ for additional details on HealthCheck.

ONAP Controller / Ansible API Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section outlines the workflow that ONAP Controller invokes when it receives an action request against an Ansible managed VNF.

 #. When ONAP Controller receives a request for an action for an AnsibleManaged VNF, it retrieves the corresponding template (based on **action** and **VNF**) from its database and sets necessary values (such as an Id, NodeList, and EnvParameters) from either information in the request or data obtained from other sources.   This is referred to as the payload that is sent as a JSON object to the Ansible server.
 #. The ONAP Controller sends a request to the Ansible server to execute the action.
 #. The ONAP Controller polls the Ansible Server for result (success or failure).  The ONAP Controllers has a timeout value which is contained in the template.   If the result is not available when the timeout is reached, the ONAP Controller stops polling and returns a timeout error to the requester.   The Ansible Server continues to process the request.


ONAP Controller APIs and Behavior
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP Controllers such as APPC expose a northbound API to clients which offer a set of commands. The following commands are expected to be supported
on all VNF’s if applicable, either directly (via the Netconf interface) or indirectly (via a Chef or Ansible server). There are additional commands
offered to northbound clients that are not listed here, as these commands either act internally on the Controller itself or depend upon network cloud
components for implementation (thus, these actions do not put any special requirement on the VNF provider).

The following table summarizes how the VNF must act in response to
commands from ONAP.

Table 8. ONAP Controller APIs and NETCONF Commands

+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Action**          | **Description**                                                                                                                                                                                                                                                                  | **NETCONF Commands**                                                                                                                                                                                                          |
+=====================+==================================================================================================================================================================================================================================================================================+===============================================================================================================================================================================================================================+
| Action              | Queries ONAP Controller for the current state of a previously submitted runtime LCM (Lifecycle Management) action.                                                                                                                                                               | There is currently no way to check the request status in NETCONF so action status is managed internally by the ONAP controller.                                                                                               |
|                     |                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                               |
| Status              |                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                               |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Audit, Sync         | Compare active (uploaded) configuration against the current configuration in the ONAP controller. Audit returns failure if different. Sync considers the active (uploaded) configuration as the current configuration.                                                           | The <get-config> operation is used to retrieve the running configuration from the VNF.                                                                                                                                        |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lock,               | Returns true when the given VNF has been locked.                                                                                                                                                                                                                                 | There is currently no way to query lock state in NETCONF so VNF locking and unlocking is managed internally by the ONAP controller.                                                                                           |
|                     |                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                               |
| Unlock,             |                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                               |
|                     |                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                               |
| CheckLock           |                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                               |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configure,          | Configure applies a post-instantiation configuration the target VNF or VNFC. ConfigModify updates only a subset of the total configuration parameters of a VNF.                                                                                                                  | The <edit-config> operation loads all or part of a specified configuration data set to the specified target database. If there is no <candidate/> database, then the target is the <running/> database. A <commit> follows.   |
|                     |                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                               |
| ConfigModify        |                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                               |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Health              | Executes a VNF health check and returns the result. A health check is VNF-specific.                                                                                                                                                                                              | This command has no existing NETCONF RPC action.  It must be supported either by REST (see `VNF REST APIs`_) or using Ansible or Chef.                                                                                        |
|                     |                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                               |
| Check               |                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                               |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| StartApplication,   | ONAP requests application to be started or stopped on the VNF. These actions do not need to be supported if (1) the application starts automatically after Configure or if the VM’s are started and (2) the application gracefully shuts down if the VM’s are stopped.           | These commands have no specific NETCONF RPC action.                                                                                                                                                                           |
|                     |                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                               |
| StopApplication     |                                                                                                                                                                                                                                                                                  | If applicable, these commands must be supported using Ansible or Chef (see Table 9 below).                                                                                                                                    |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ConfigBackup,       | ONAP requests the VNF configuration parameters to be backed up or restored (replacing existing configuration parameters on the VNF).                                                                                                                                             | These commands have no specific NETCONF RPC action.                                                                                                                                                                           |
|                     |                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                               |
| ConfigRestore       |                                                                                                                                                                                                                                                                                  | They can be supported using Ansible or Chef (see Table 9 below).                                                                                                                                                              |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Table 9 lists the required Chef and Ansible support for commands from
ONAP.

Table 9. ONAP Controller APIs and Chef/Ansible Support

+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Action**          | **Chef**                                                                                                                                                                                                                                                                                         | **Ansible**                                                                                                                                                                                                                                                                                 |
+=====================+==================================================================================================================================================================================================================================================================================================+=============================================================================================================================================================================================================================================================================================+
| Action              | Not needed. ActionStatus is managed internally by the ONAP controller.                                                                                                                                                                                                                           | Not needed. ActionStatus is managed internally by the ONAP controller.                                                                                                                                                                                                                      |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
| Status              |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Audit, Sync         | VNF provider must provide any necessary roles, cookbooks, recipes to retrieve the running configuration from a VNF and place it in the respective Node Objects ‘PushJobOutput’ attribute of all nodes in NodeList when triggered by a chef-client run.                                           | VNF provider must provide an Ansible playbook to retrieve the running configuration from a VNF and place the output on the Ansible server in a manner aligned with playbook requirements listed in this document.                                                                           |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
|                     | The JSON file for this VNF action is required to set “PushJobFlag” to “True” and “GetOutputFlag” to “True”. The “Node” JSON dictionary must have the run list populated with the necessary sequence of roles, cookbooks, recipes.                                                                | The PlaybookName must be provided in the JSON file.                                                                                                                                                                                                                                         |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
|                     | The Environment and Node values should contain all appropriate configuration attributes.                                                                                                                                                                                                         | NodeList must list FQDNs of an example VNF on which to execute playbook.                                                                                                                                                                                                                    |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
|                     | NodeList must list sample FQDNs that are required to conduct a chef-client run for this VNF Action.                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                             |
+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lock,               | Not needed. VNF locking and unlocking is managed internally by the ONAP controller.                                                                                                                                                                                                              | Not needed. VNF locking and unlocking is managed internally by the ONAP controller.                                                                                                                                                                                                         |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
| Unlock,             |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
| CheckLock           |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configure,          | VNF provider must provide any necessary roles, cookbooks, recipes to apply configuration attributes to the VNF when triggered by a chef-client run. All configurable attributes must be obtained from the Environment and Node objects on the Chef Server.                                       | VNF provider must provide an Ansible playbook that can configure the VNF with parameters supplied by the Ansible Server.                                                                                                                                                                    |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
| ConfigModify        | The JSON file for this VNF action should include all configurable attributes in the Environment and/or Node JSON dictionary.                                                                                                                                                                     | The PlaybookName must be provided in the JSON file.                                                                                                                                                                                                                                         |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
|                     | The “PushJobFlag” must be set to “True”.                                                                                                                                                                                                                                                         | The “EnvParameters” and/or “FileParameters” field values should be provided and contain all configurable parameters for the VNF.                                                                                                                                                            |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
|                     | The “Node” JSON dictionary must have the run list populated with necessary sequence of roles, cookbooks, recipes. This action is not expected to return an output.                                                                                                                               | NodeList must list FQDNs of an example VNF on which to execute playbook.                                                                                                                                                                                                                    |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
|                     | “GetOutputFlag” must be set to “False”.                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                             |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
|                     | NodeList must list sample FQDNs that are required to conduct a chef-client run for this VNF Action.                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                             |
+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Health              | The VNF level HealthCheck run a check over the entire scope of the VNF (for more details, see `VNF REST APIs`_).  It can be supported either via a REST interface or with Chef roles, cookbooks, and recipes.                                                                                    | The VNF level HealthCheck run a check over the entire scope of the VNF (for more details, see `VNF REST APIs`_).  It can be supported either via a REST interface or with an Ansible playbook.                                                                                              |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
| Check               |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| StartApplication,   | VNF provider must provide roles, cookbooks, recipes to start an application on the VNF when triggered by a chef-client run. If application does not start, the run must fail or raise an exception. If application is already started, or starts successfully, the run must finish successfully. | VNF provider must provide an Ansible playbook to start the application on the VNF. If application does not start, the playbook must indicate failure. If application is already started, or starts successfully, the playbook must finish successfully.                                     |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
| StopApplication     | For StopApplication, the application must be stopped gracefully (no loss of traffic).                                                                                                                                                                                                            | For StopApplication, the application must be stopped gracefully (no loss of traffic).                                                                                                                                                                                                       |
+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ConfigBackup,       | VNF provider must provide roles, cookbooks, recipes to backup or restore the configuration parameters on the VNF when triggered by an ECOMP request.                                                                                                                                             | VNF provider must provide an Ansible playbook to backup or restore the configuration parameters on the VNF when triggered by an ECOMP request.                                                                                                                                              |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
|                     | When the ConfigBackup command is executed, the current VNF configuration parameters are copied over to the Ansible or Chef server (if there is an existing set of backed up parameters, they are overwritten). When the ConfigRestore command is executed, the VNF configuration parameters      | When the ConfigBackup command is executed, the current VNF configuration parameters are copied over to the Ansible or Chef server (if there is an existing set of backed up parameters, they are overwritten). When the ConfigRestore command is executed, the VNF configuration parameters |
| ConfigRestore       | which are backed up on the Ansible or Chef server are applied to the VNF (replacing existing parameters). It can be assumed that the VNF is not in service when a ConfigRestore command is executed.                                                                                             | which are backed up on the Ansible or Chef server are applied to the VNF (replacing existing parameters). It can be assumed that the VNF is not in service when a ConfigRestore command is executed.                                                                                        |
|                     |                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                             |
|                     | If either command fails, the run must fail or raise an exception.                                                                                                                                                                                                                                | If either command fails, the run must fail or raise an exception.                                                                                                                                                                                                                           |
+---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

For information purposes, the following ONAP controller functions are
planned in the future:

Table 10. Planned ONAP Controller Functions

+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Action           | Description                                                                                                                                                                     |
+==================+=================================================================================================================================================================================+
| UpgradeSoftware  | Upgrades the target VNF to a new software version.                                                                                                                              |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| QuiesceTraffic,  | Quiesces traffic (stops traffic gracefully) and resume traffic on the VNF.   These commands do not stop the application processes (which is done using StopApplication).        |
| ResumeTraffic    |                                                                                                                                                                                 |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


d. Monitoring & Management
--------------------------

This section addresses data collection and event processing functionality that is directly
dependent on the interfaces provided by the VNFs’ APIs. These can be in the form of asynchronous
interfaces for event, fault notifications, and autonomous data streams. They can also be
synchronous interfaces for on-demand requests to retrieve various performance, usage,
and other event information.

The target direction for VNF interfaces is to employ APIs that are implemented
utilizing standardized messaging and modeling protocols over standardized transports.
Migrating to a virtualized environment presents a tremendous opportunity to eliminate
the need for proprietary interfaces for VNF provider equipment while removing the traditional
boundaries between Network Management Systems and Element Management Systems. Additionally,
VNFs provide the ability to instrument the networking applications by creating event
records to test and monitor end-to-end data flow through the network, similar to what
physical or virtual probes provide without the need to insert probes at various points
in the network. The VNF providers must be able to provide the aforementioned set of required
data directly to the ONAP collection layer using standardized interfaces.

Data Model for Event Records
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describes the data model for the collection of telemetry data from VNFs
by Service Providers (SPs) to manage VNF health and runtime lifecycle. This data
model is referred to as the VNF Event Streaming (VES) specifications. While this
document is focused on specifying some of the records from the ONAP perspective,
there may be other external bodies using the same framework to specify additional
records. For example, OPNFV has a VES project  that is looking to specify records
for OpenStack’s internal telemetry to manage Application (VNFs), physical and
virtual infrastructure (compute, storage, network devices), and virtual infrastructure
managers (cloud controllers, SDN controllers). Note that any configurable parameters
for these data records (e.g., frequency, granularity, policy-based configuration)
will be managed using the “Configuration” framework described in the prior sections
of this document.

The Data Model consists of:

-  Common Header Record: This data structure precedes each of the
   Technology Independent and Technology Specific records sections of
   the data model.

-  Technology Independent Records: This version of the document specifies
   the model for Fault, Heartbeat, State Change, Syslog, Threshold Crossing
   Alerts, and VNF Scaling* (short for measurementForVfScalingFields – actual
   name used in JSON specification) records. In the future, these may be
   extended to support other types of technology independent records. Each
   of these records allows additional fields (name/ value pairs) for extensibility.
   The VNF provider can use these VNF Provider-specific additional fields to provide
   additional information that may be relevant to the managing systems.

-  Technology Specific Records: This version of the document specifies the model
   for Mobile Flow records, Signaling and Voice Quality records. In the future,
   these may be extended to support other types of records (e.g. Network Fabric,
   Security records, etc.). Each of these records allows additional fields
   (name/value pairs) for extensibility. The VNF providers can use these VNF-specific
   additional fields to provide additional information that may be relevant to the
   managing systems. A placeholder for additional technology specific areas of
   interest to be defined in the future documents has been depicted.

|image0|

Figure 1. Data Model for Event Records

Event Records - Data Structure Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The data structure for event records consists of:

-  a Common Event Header block;

-  zero or more technology independent domain blocks; and

   -  e.g., Fault domain, State Change domain, Syslog domain, etc.

-  zero or more technology specific domain blocks.

   -  e.g., Mobile Flow domain, Signaling domain, Voice Quality domain,
      etc.

Common Event Header
~~~~~~~~~~~~~~~~~~~~~

The common header that precedes any of the domain-specific records contains
information identifying the type of record to follow, information about
the sender and other identifying characteristics related to timestamp,
sequence number, etc.

Technology Independent Records – Fault Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Fault Record, describing a condition in the Fault domain, contains
information about the fault such as the entity under fault, the
severity, resulting status, etc.

Technology Independent Records – Heartbeat Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Heartbeat Record provides an optional structure for communicating
information about heartbeat or watchdog signaling events.  It can
contain information about service intervals, status information etc.
as required by the heartbeat implementation.

Note: Heartbeat records would only have the Common Event Header block.
An optional heartbeat domain is available if required by the heartbeat
implementation.

Technology Independent Records – State Change Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The State Change Record provides a structure for communicating information
about data flow through the VNF. It can contain information about state
change related to physical device that is reported by VNF. As an example,
when cards or port name of the entity that has changed state.

Technology Independent Records – Syslog Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Syslog Record provides a structure for communicating any type of
information that may be logged by the VNF. It can contain information
about system internal events, status, errors, etc.

Technology Independent Records – Threshold Crossing Alert Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Threshold Crossing Alert (TCA) Record provides a structure for
communicating information about threshold crossing alerts. It can
contain alert definitions and types, actions, events, timestamps
and physical or logical details.

Technology Independent Records - VNF Scaling Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The VNF Scaling\* (short for measurementForVfScalingFields –
actual name used in JSON specification) Record contains information
about VNF and VNF resource structure and its condition to help in
the management of the resources for purposes of elastic scaling.

Technology Independent Records – otherFields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The otherFields Record defines fields for events belonging to the
otherFields domain of the Technology Independent domain enumeration.
This record provides a mechanism to convey a complex set of fields
(possibly nested or opaque) and is purely intended to address
miscellaneous needs such as addressing time-to-market considerations
or other proof-of-concept evaluations. Hence, use of this record
type is discouraged and should be minimized.

Technology Specific Records – Mobile Flow Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Mobile Flow Record provides a structure for communicating
information about data flow through the VNF. It can contain
information about connectivity and data flows between serving
elements for mobile service, such as between LTE reference points, etc.

Technology Specific Records – Signaling Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Signaling Record provides a structure for communicating information
about signaling messages, parameters and signaling state.  It can
contain information about data flows for signaling and controlling
multimedia communication sessions such as voice and video calls.

Technology Specific Records – Voice Quality Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Voice Quality Record provides a structure for communicating information
about voice quality statistics including media connection information,
such as transmitted octet and packet counts, packet loss, packet delay
variation, round-trip delay, QoS parameters and codec selection.

Technology Specific Records – Future Domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The futureDomains Record is a placeholder for additional technology
specific areas of interest that will be defined and described
in the future documents.

Data Structure Specification of the Event Record
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For additional information on the event record formats of the data
structures mentioned above, please refer to `VES Event
Listener <https://github.com/att/evel-test-collector/tree/master/docs/att_interface_definition>`__.

Transports and Protocols Supporting Resource Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delivery of data from VNFs to ONAP must use the common transport mechanisms and protocols
for all VNFs as defined in this document. Transport mechanisms and protocols have been
selected to enable both high volume and moderate volume datasets, as well as asynchronous
and synchronous communications over secure connections. The specified encoding provides
self-documenting content, so data fields can be changed as needs evolve, while minimizing
changes to data delivery.

The term ‘Event Record’ is used throughout this document to represent various forms of
telemetry or instrumentation made available by the VNF including, faults, status events,
various other types of VNF measurements and logs. Headers received by themselves must be
used as heartbeat indicators. Common structures and delivery protocols for other types of
data will be given in future versions of this document as we get more insight into data
volumes and required processing.

In the following sections, we provide options for encoding, serialization and data
delivery. Agreements between Service Providers and VNF providers shall determine which
encoding, serialization and delivery method to use for particular data sets. The selected
methods must be agreed to prior to the on-boarding of the VNF into ONAP design studio.

VNF Telemetry using VES/JSON Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The preferred model for data delivery from a VNF to ONAP DCAE is the JSON driven model as depicted in Figure 2.

|image1|

Figure 2. VES/JSON Driven Model

VNF providers will provide a YAML artifact to the Service Provider that describes:

* standard VES/JSON model information elements (key/values) that the VNF provides
* any additional non-standard (custom) VES/JSON model information elements (key/values) that the VNF provides

Using the semantics and syntax supported by YAML, VNF providers will indicate specific conditions that may
arise, and recommend actions that should be taken at specific thresholds, or if specific conditions
repeat within a specified time interval.

Based on the VNF provider's recommendations, the Service Provider may create additional YAML artifacts
(using ONAP design Studio), which finalizes Service Provider engineering rules for the processing of
the VNF events.  The Service Provider may alter the threshold levels recommended by the VNF providor,
and may modify and more clearly specify actions that should be taken when specified conditions arise.
The Service Provider-created version of the YAML artifact will be distributed to ONAP applications
by the Design framework.

VNF Telemetry using YANG Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the JSON driven model described above, a YANG driven model can also be
supported, as depicted in Figure 3.

|image2|

Figure 3. YANG Driven Model

VNF providers will provide to the Service Provider the following YANG model artifacts:

* common IETF YANG modules that support the VNF
* native (VNF provider-supplied) YANG modules that support the VNF
* open (OpenConfig) YANG modules and the following configuration-related information, including:

  * telemetry configuration and operational state data; such as:

    * sensor paths
    * subscription bindings
    * path destinations
    * delivery frequency
    * transport mechanisms
    * data encodings

* a YAML artifact that provides all necessary mapping relationships between YANG model data types to VES/JSON information elements
* YANG helper or decoder functions that automate the conversion between YANG model data types to VES/JSON information elements
* OPTIONAL: YANG Telemetry modules in JSON format per RFC 7951

Using the semantics and syntax supported by YANG, VNF providers will indicate specific conditions that may
arise, and recommend actions that should be taken at specific thresholds, or if specific conditions
repeat within a specified time interval.

Based on the VNF provider's recommendations, the Service Provider may create additional YAML artifacts
(using ONAP design Studio), which finalizes Service Provider engineering rules for the processing
of the VNF events.  The Service Provider may alter the threshold levels recommended by the
VNF provider, and may modify and more clearly specify actions that should be taken when specified
conditions arise.  The Service Provided-created version of the YAML will be distributed to ONAP
applications by the Design framework.

Note: While supporting the YANG model described above, we are still leveraging the VES JSON
based model in DCAE.  The purpose of the diagram above is to illustrate the concept only and
not to imply a specific implementation.

VNF Telemetry using Google Protocol Buffers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the data delivery models described above, support for delivery of VNF telemetry
using Google Protocol Buffers (GPB) can also be supported, as depicted in Figure 4.

VNF providers will provide to the Service Provider the additional following artifacts to
support the delivery of VNF telemetry to DCAE via the open-source gRPC mechanism using
Google's Protocol Buffers:

* the YANG model artifacts described in support of the "VNF Telemetry using YANG Model"
* valid definition file(s) for all GPB / KV-GPB encoded messages
* valid definition file(s) for all gRPC services
* gRPC method parameters and return types specified as Protocol Buffers messages

|image3|

Figure 4. Protocol Buffers Driven Model

Note: if Google Protocol Buffers are employed for delivery of VNF telemetry, Key-Value
Google Protocol Buffers (KV-GPB) is the preferred serialization method.  Details of
specifications and versioning corresponding to a release can be found
at: `VES Event Listener <https://github.com/att/evel-test-collector/tree/master/docs/att_interface_definition>`__.

Note: While supporting the VNF telemetry delivery approach described above, we are
still leveraging the VES JSON based model in DCAE.  The purpose of the diagram above
is to illustrate the concept only and not to imply a specific implementation.

Monitoring & Management Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**VNF telemetry via standardized interface**

* R-51910 The VNF **MUST** provide all telemetry (e.g., fault event records, syslog records, performance records etc.) to ONAP using the model, format and mechanisms described in this section.

**Encoding and Serialization**

Content delivered from VNFs to ONAP is to be encoded and serialized using JSON:

**JSON**

* R-19624 The VNF **MUST** encode and serialize content delivered to ONAP using JSON (RFC 7159) plain text format. High-volume data
  is to be encoded and serialized using `Avro <http://avro.apache.org/>`_, where the Avro [5]_ data format are described using JSON.

 -  JSON plain text format is preferred for moderate volume data sets (option 1), as JSON has the advantage of having well-understood simple processing and being human-readable without additional decoding. Examples of moderate volume data sets include the fault alarms and performance alerts, heartbeat messages, measurements used for VNF scaling and syslogs.
 -  Binary format using Avro is preferred for high volume data sets (option 2) such as mobility flow measurements and other high-volume streaming events (such as mobility signaling events or SIP signaling) or bulk data, as this will significantly reduce the volume of data to be transmitted. As of the date of this document, all events are reported using plain text JSON and REST.
 -  Avro content is self-documented, using a JSON schema. The JSON schema is delivered along with the data content (http://avro.apache.org/docs/current/ ). This means the presence and position of data fields can be recognized automatically, as well as the data format, definition and other attributes. Avro content can be serialized as JSON tagged text or as binary. In binary format, the JSON schema is included as a separate data block, so the content is not tagged, further compressing the volume. For streaming data, Avro will read the schema when the stream is established and apply the schema to the received content.

In addition to the preferred method (JSON), content can be delivered from VNFs to ONAP can be encoded and serialized using Google Protocol Buffers (GPB).

**KV-GPB/GPB**

Telemetry data delivered using Google Protocol Buffers v3 (proto3) can be serialized in one of the following methods:

* Key-value Google Protocol Buffers (KV-GPB) is also known as self-describing GPB:

  * keys are strings that correspond to the path of the system resources for the VNF being monitored.
  * values correspond to integers or strings that identify the operational state of the VNF resource, such a statistics counters and the state of a VNF resource.

* VNF providers must supply valid KV-GPB definition file(s) to allow for the decoding of all KV-GPB encoded telemetry messages.

* Native Google Protocol Buffers (GPB) is also known as compact GPB:

  * keys are represented as integers pointing to the system resources for the VNF being monitored.
  * values correspond to integers or strings that identify the operational state of the VNF resource, such a statistics counters and the state of a VNF resource.

* Google Protocol Buffers (GPB) requires metadata in the form of .proto files. VNF providers must supply the necessary GPB .proto files such that GPB telemetry messages can be encoded and decoded.

* In the future, we may consider support for other types of encoding & serialization methods based on industry demand


**Reporting Frequency**

* R-98191 The VNF **MUST** vary the frequency that asynchronous data is delivered based on the content and how data may be aggregated or grouped together. For example, alarms and alerts are expected to be delivered as soon as they appear. In contrast, other content, such as performance measurements, KPIs or reported network signaling may have various ways of packaging and delivering content. Some content should be streamed immediately; or content may be monitored over a time interval, then packaged as collection of records and delivered as block; or data may be collected until a package of a certain size has been collected; or content may be summarized statistically over a time interval, or computed as a KPI, with the summary or KPI being delivered.

  -  We expect the reporting frequency to be configurable depending on the virtual network function’s needs for management. For example, Service Provider may choose to vary the frequency of collection between normal and trouble-shooting scenarios.
  -  Decisions about the frequency of data reporting will affect the size of delivered data sets, recommended delivery method, and how the data will be interpreted by ONAP. These considerations should not affect deserialization and decoding of the data, which will be guided by the accompanying JSON schema or GPB definition files.

**Addressing and Delivery Protocol**

ONAP destinations can be addressed by URLs for RESTful data PUT. Future data sets may also be addressed by host name and port number for TCP streaming, or by host name and landing zone directory for SFTP transfer of bulk files.

* R-88482 The VNF **SHOULD** use REST using HTTPS delivery of plain text JSON for moderate sized asynchronous data sets, and for high volume data sets when feasible.
* R-84879 The VNF **MUST** have the capability of maintaining a primary and backup DNS name (URL) for connecting to ONAP collectors, with the ability to switch between addresses based on conditions defined by policy such as time-outs, and buffering to store messages until they can be delivered. At its discretion, the service provider may choose to populate only one collector address for a VNF. In this case, the network will promptly resolve connectivity problems caused by a collector or network failure transparently to the VNF.
* R-81777 The VNF **MUST** be configured with initial address(es) to use at deployment time. Subsequently, address(es) may be changed through ONAP-defined policies delivered from ONAP to the VNF using PUTs to a RESTful API, in the same manner that other controls over data reporting will be controlled by policy.
* R-08312 The VNF **MAY** use other options which are expected to include

 -  REST delivery of binary encoded data sets.
 -  TCP for high volume streaming asynchronous data sets and for other high volume data sets. TCP delivery can be used for either JSON or binary encoded data sets.
 -  SFTP for asynchronous bulk files, such as bulk files that contain large volumes of data collected over a long time interval or data collected across many VNFs. This is not preferred. Preferred is to reorganize the data into more frequent or more focused data sets, and deliver these by REST or TCP as appropriate.
 -  REST for synchronous data, using RESTCONF (e.g., for VNF state polling).

* R-03070 The VNF **MUST**, by ONAP Policy, provide the ONAP addresses as data destinations for each VNF, and may be changed by Policy while the VNF is in operation. We expect the VNF to be capable of redirecting traffic to changed destinations with no loss of data, for example from one REST URL to another, or from one TCP host and port to another.

**Asynchronous and Synchronous Data Delivery**

* R-06924 The VNF **MUST** deliver asynchronous data as data becomes available, or according to the configured frequency.
* R-73285 The VNF **MUST** must encode, address and deliver the data as described in the previous paragraphs.
* R-42140 The VNF **MUST** respond to data requests from ONAP as soon as those requests are received, as a synchronous response.
* R-34660 The VNF **MUST** use the RESTCONF/NETCONF framework used by the ONAP configuration subsystem for synchronous communication.
* R-86585 The VNF **MUST** use the YANG configuration models and RESTCONF  [RFC8040] (https://tools.ietf.org/html/rfc8040).
* R-11240 The VNF **MUST** respond with content encoded in JSON, as described in the RESTCONF specification. This way the encoding of a synchronous communication will be consistent with Avro.
* R-70266 The VNF **MUST** respond to an ONAP request to deliver the current data for any of the record types defined in `Event Records - Data Structure Description`_ by returning the requested record, populated with the current field values. (Currently the defined record types include fault fields, mobile flow fields, measurements for VNF scaling fields, and syslog fields. Other record types will be added in the future as they become standardized and are made available.)
* R-46290 The VNF **MUST** respond to an ONAP request to deliver granular data on device or subsystem status or performance, referencing the YANG configuration model for the VNF by returning the requested data elements.
* R-43327 The VNF **SHOULD** use `Modeling JSON text with YANG <https://tools.ietf.org/html/rfc7951>`_, If YANG models need to be translated to and from JSON{RFC7951]. YANG configuration and content can be represented via JSON, consistent with Avro, as described in “Encoding and Serialization” section.

**Security**

* R-42366 The VNF **MUST** support secure connections and transports such as Transport Layer Security (TLS) protocol [`RFC5246 <https://tools.ietf.org/html/rfc5246>`_] and should adhere to the best current practices outlined in `RFC7525 <https://tools.ietf.org/html/rfc7525>`_.
* R-44290 The VNF **MUST** control access to ONAP and to VNFs, and creation of connections, through secure credentials, log-on and exchange mechanisms.
* R-47597 The VNF **MUST** carry data in motion only over secure connections.
* R-68165 The VNF **MUST** encrypt any content containing Sensitive Personal Information (SPI) or certain proprietary data, in addition to applying the regular procedures for securing access and delivery.


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

.. [5]
   This option is not currently supported in ONAP and it is currently
   under consideration.

.. [6]
   https://wiki.opnfv.org/display/PROJ/VNF+Event+Stream

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

**8. Appendix**
===============

a. – Chef JSON Key Value Description
------------------------------------

The following provides the key value pairs that must be contained in the
JSON file supporting Chef action.

Table A1. Chef JSON File key value description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| **Field Name**    | **Description**                                                                                                                                                                                                                                                                                   | **Type**    | **Comment**                                                                                                                             |
+===================+===================================================================================================================================================================================================================================================================================================+=============+=========================================================================================================================================+
| Environment       | A JSON dictionary representing a Chef Environment object. If the VNF action requires loading or modifying Chef environment attributes associated with the VNF, all the relevant information must be provided in this JSON dictionary in a structure that conforms to a Chef Environment Object.   | Optional    | Depends on VNF action.                                                                                                                  |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Node              | A JSON dictionary representing a Chef Node Object.                                                                                                                                                                                                                                                | Mandatory   |                                                                                                                                         |
|                   |                                                                                                                                                                                                                                                                                                   |             |                                                                                                                                         |
|                   | The Node JSON dictionary must include the run list to be triggered for the desired VNF action by the push job. It should also include any attributes that need to be configured on the Node Object as part of the VNF action.                                                                     |             |                                                                                                                                         |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| NodeList          | Array of FQDNs that correspond to the endpoints (VMs) of a VNF registered with the Chef Server that need to trigger a chef-client run as part of the desired VNF action.                                                                                                                          | Mandatory   |                                                                                                                                         |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| PushJobFlag       | This field indicates whether the VNF action requires a push Job. Push job object will be created by ONAP if required.                                                                                                                                                                             | Mandatory   | If set to “True”, ONAP will request a push job. Ignored otherwise.                                                                      |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| CallbackCapable   | This field indicates if the chef-client run invoked by push job corresponding to the VNF action is capable of posting results on a callback URL.                                                                                                                                                  | Optional    | If Chef cookbook is callback capable, VNF owner is required to set it to “True”. Ignored otherwise.                                     |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| GetOutputFlag     | Flag which indicates whether ONAP should retrieve output generated in a chef-client run from Node object attribute node[‘PushJobOutput’] for this VNF action (e.g., in Audit).                                                                                                                    | Mandatory   | ONAP will retrieve output from NodeObject attributes [‘PushJobOutput’] for all nodes in NodeList if set to “True”. Ignored otherwise.   |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+

Chef Template example:

.. code-block:: chef

 “Environment”:{
      "name": "HAR",
      "description": "VNF Chef environment for HAR",
      "json_class": "Chef::Environment",
      "chef_type": "environment",
      "default_attributes": { },
      "override_attributes": {
            “Retry_Time”:”50”,
            “MemCache”: “1024”,
            “Database_IP”:”10.10.1.5”
      },
 }
 }
 “Node”: {
      “name” : “signal.network.com “
      "chef_type": "node",
      "json_class": "Chef::Node",
      "attributes": {
            “IPAddress1”: “192.168.1.2”,
            “IPAddress2”:”135.16.162.5”,
            “MyRole”:”BE”
      },
      "override": {},
      "default": {},
      “normal”:{},
      “automatic”:{},
      “chef_environment” : “_default”
      "run_list": [ "configure_signal" ]
      },
      “NodeList”:[“node1.vnf_a.onap.com”, “node2.vnf_a.onap.com”],
      “PushJobFlag”: “True”
      “CallbackCapable”:True
      “GetOutputFlag” : “False”
 }

The example JSON file provided by the VNF provider for each VNF action will be
turned into a template by ONAP, that can be updated with instance
specific values at run-time.

Some points worth noting regarding the JSON fields:

a. The JSON file must be created for each action for each VNF.

b. If a VNF action involves multiple endpoints (VMs) of a VNF, ONAP will
   replicate the “Node” JSON dictionary in the template and post it to
   each FQDN (i.e., endpoint) in the NodeList after setting the “name”
   field in the Node object to be the respective FQDN [1]_. Hence, it
   is required that all end points (VMs) of a VNF involved in a VNF
   action support the same set of Node Object attributes.

The following table describes the JSON dictionary to post in Callback.

Table A2. JSON Dictionary to Post in Callback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------------------------------------------------+
| **Key**         | **Description**                                                                                                                                                                                           | **Type**    | **Comment**                                                 |
+=================+===========================================================================================================================================================================================================+=============+=============================================================+
| RequestId       | A unique string associated with the original request by ONAP. This key-value pair will be provided by ONAP in the environment of the push job request and must be returned as part of the POST message.   | Mandatory   |                                                             |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------------------------------------------------+
| StatusCode      | An integer that must be set to                                                                                                                                                                            | Mandatory   |                                                             |
|                 |                                                                                                                                                                                                           |             |                                                             |
|                 | 200 if chef-client run on the node finished successfully                                                                                                                                                  |             |                                                             |
|                 |                                                                                                                                                                                                           |             |                                                             |
|                 | 500 otherwise.                                                                                                                                                                                            |             |                                                             |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------------------------------------------------+
| StatusMessage   | A string which must be set to                                                                                                                                                                             | Mandatory   |                                                             |
|                 |                                                                                                                                                                                                           |             |                                                             |
|                 | ‘SUCCESS’ if StatusCode was 200                                                                                                                                                                           |             |                                                             |
|                 |                                                                                                                                                                                                           |             |                                                             |
|                 | Appropriate error message otherwise.                                                                                                                                                                      |             |                                                             |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------------------------------------------------+
| Name            | A string which corresponds to the name of the node where push job is run. It is required that the value be retrieved from the node object attributes (where it is always defined).                        | Mandatory   |                                                             |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------------------------------------------------+
| PushJobOutput   | Any output from the chef-client run that needs to be returned to ONAP.                                                                                                                                    | Optional    | Depends on VNF action. If empty, it must not be included.   |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------------------------------------------------+


b. – Ansible JSON Key Value Description
----------------------------------------

The following provides the key value pairs that must be contained in the
JSON file supporting Ansible action.

Table B1. Ansible JSON File key value description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+
| **Field Name**   | **Description**                                                                                                                                                                                                                                                                            | **Type**    | **Comment**                                                         |
+==================+============================================================================================================================================================================================================================================================================================+=============+=====================================================================+
| PlaybookName     | VNF providor must list name of the playbook used to execute the VNF action.                                                                                                                                                                                                                | Mandatory   |                                                                     |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+
| Action           | Name of VNF action.                                                                                                                                                                                                                                                                        | Optional    |                                                                     |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+
| EnvParameters    | A JSON dictionary which should list key value pairs to be passed to the Ansible playbook. These values would correspond to instance specific parameters that a playbook may need to execute an action.                                                                                     | Optional    | Depends on the VNF action.                                          |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+
| NodeList         | A JSON array of FQDNs that the playbook must be executed on.                                                                                                                                                                                                                               | Optional    | If not provided, playbook will be executed on the Ansible Server.   |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+
| FileParameters   | A JSON dictionary where keys are filenames and values are contents of files. The Ansible Server will utilize this feature to generate files with keys as filenames and values as content. This attribute can be used to generate files that a playbook may require as part of execution.   | Optional    | Depends on the VNF action and playbook design.                      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+
| Timeout          | Time (in seconds) that a playbook is expected to take to finish execution for the VNF. If playbook execution time exceeds this value, Ansible Server will terminate the playbook process.                                                                                                  | Optional    |                                                                     |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+

Ansible JSON file example:

{

      “Action”:”Configure”,

      "PlaybookName": "Ansible_configure.yml",

      "NodeList": ["test1.vnf_b.onap.com", “test2.vnf_b.onap.com”],

      "Timeout": 60,

      "EnvParameters": {"Retry": 3, "Wait": 5, “ConfigFile”:”config.txt”},

      “FileParameters”:{“config.txt”:”db_ip=10.1.1.1, sip_timer=10000”}

}

In the above example, the Ansible Server will:

a. Process the “FileParameters” dictionary and generate a file named
   ‘config.txt’ with contents set to the value of the ‘config.txt’ key.

b. Execute the playbook named ‘Ansible_configure.yml’ on nodes with
   FQDNs test1.vnf_b.onap.com and test2.vnf_b.onap.com respectively
   while providing the following key value pairs to the playbook:
   Retry=3, Wait=5, ConfigFile=config.txt

c. If execution time of the playbook exceeds 60 secs (across all hosts),
   it will be terminated.

c. – VNF License Information Guidelines
----------------------------------------

This Appendix describes the metadata to be supplied for VNF licenses.

1. General Information

Table C1 defines the required and optional fields for licenses.

Table C1. Required Fields for General Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| **Field Name**                              | **Description**                                                                                                                                                                                                                                                                                           | **Data Type**     | **Type**    |
+=============================================+===========================================================================================================================================================================================================================================================================================================+===================+=============+
| VNF Provider Name                           | The name of the VNF provider.                                                                                                                                                                                                                                                                             | String            | Mandatory   |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| VNF Provider Product                        | The name of the product to which this agreement applies.                                                                                                                                                                                                                                                  | String            | Mandatory   |
|                                             |                                                                                                                                                                                                                                                                                                           |                   |             |
|                                             | Note: a contract/agreement may apply to more than one VNF provider product. In that case, provide the metadata for each product separately.                                                                                                                                                               |                   |             |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| VNF Provider Product Description            | A general description of VNF provider software product.                                                                                                                                                                                                                                                   | String            | Optional    |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| Export Control Classification Number (ECCN) | ECCNs are 5-character alpha-numeric designations used on the Commerce Control List (CCL) to identify dual-use items for export control purposes. An ECCN categorizes items based on the nature of the product, i.e. type of commodity, software, or technology and its respective technical parameters.   | String            | Mandatory   |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| Reporting Requirements                      | A list of any reporting requirements on the usage of the software product.                                                                                                                                                                                                                                | List of strings   | Optional    |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+

1. Entitlements

Entitlements describe software license use rights. The use rights may be
quantified by various metrics: # users, # software instances, # units.
The use rights may be limited by various criteria: location (physical or
logical), type of customer, type of device, time, etc.

One or more entitlements can be defined; each one consists of the
following fields:

Table C2. Required Fields for Entitlements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| **Field Name**                                          | **Description**                                                                                                                                                                       | **Data Type**     | **Type**      |
+=========================================================+=======================================================================================================================================================================================+===================+===============+
| VNF Provider Part Number / Manufacture Reference Number | Identifier for the entitlement as described by the VNF provider in their price list / catalog / contract.                                                                                   | String            | Mandatory     |
+---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| Description                                             | Verbiage that describes the entitlement.                                                                                                                                              | String            | Optional      |
+---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| Entitlement Identifier                                  | Each entitlement defined must be identified by a unique value (e.g., numbered 1, 2, 3….)                                                                                              | String            | Mandatory     |
+---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| Minimum Order Requirement                               | The minimum number of entitlements that need to be purchased. For example, the entitlements must be purchased in a block of 100. If no minimum is required, the value will be zero.   | Number            | Mandatory     |
+---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| Unique Reporting Requirements                           | A list of any reporting requirements on the usage of the software product. (e.g.: quarterly usage reports are required)                                                               | List of Strings   | Optional      |
+---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| License Type                                            | Type of license applicable to the software product. (e.g.: fixed-term, perpetual, trial, subscription.)                                                                               | String            | Mandatory     |
+---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| License Duration                                        | Valid values:                                                                                                                                                                         | String            | Conditional   |
|                                                         |                                                                                                                                                                                       |                   |               |
|                                                         | **year**, **quarter**, **month**, **day**.                                                                                                                                            |                   |               |
|                                                         |                                                                                                                                                                                       |                   |               |
|                                                         | Not applicable when license type is Perpetual.                                                                                                                                        |                   |               |
+---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| License Duration Quantification                         | Number of years, quarters, months, or days for which the license is valid.                                                                                                            | Number            | Conditional   |
|                                                         |                                                                                                                                                                                       |                   |               |
|                                                         | Not applicable when license type is Perpetual.                                                                                                                                        |                   |               |
+---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| Limits                                                  | see section C.4 for possible values                                                                                                                                                   | List              | Optional      |
+---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+

1. License Keys

This section defines information on any License Keys associated with the
Software Product. A license key is a data string (or a file) providing a
means to authorize the use of software. License key does not provide
entitlement information.

License Keys are not required. Optionally, one or more license keys can
be defined; each one consists of the following fields:

Table C3. Required Fields for License Keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------+---------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| **Field Name**           | **Description**                                                                                               | **Data Type**   | **Type**    |
+==========================+===============================================================================================================+=================+=============+
| Description              | Verbiage that describes the license key                                                                       | String          | Mandatory   |
+--------------------------+---------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| License Key Identifier   | Each license key defined must be identified by a unique value (e.g., numbered 1, 2, 3….)                      | String          | Mandatory   |
+--------------------------+---------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Key Function             | Lifecycle stage (e.g., Instantiation or Activation) at which the license key is applied to the software.      | String          | Optional    |
+--------------------------+---------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| License Key Type         | Valid values:                                                                                                 | String          | Mandatory   |
|                          |                                                                                                               |                 |             |
|                          | **Universal, Unique**                                                                                         |                 |             |
|                          |                                                                                                               |                 |             |
|                          | **Universal** - a single license key value that may be used with any number of instances of the software.     |                 |             |
|                          |                                                                                                               |                 |             |
|                          | **Unique**- a unique license key value is required for each instance of the software.                         |                 |             |
+--------------------------+---------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Limits                   | see section C.4 for possible values                                                                           | List            | Optional    |
+--------------------------+---------------------------------------------------------------------------------------------------------------+-----------------+-------------+

1. Entitlement and License Key Limits

Limitations on the use of software entitlements and license keys may be
based on factors such as: features enabled in the product, the allowed
capacity of the product, number of installations, etc... The limits may
generally be categorized as:

-  where (location)

-  when (time)

-  how (usages)

-  who/what (entity)

-  amount (how much)

Multiple limits may be applicable for an entitlement or license key.
Each limit may further be described by limit behavior, duration,
quantification, aggregation, aggregation interval, start date, end date,
and threshold.

When the limit is associated with a quantity, the quantity is relative
to an instance of the entitlement or license key. For example:

-  Each entitlement grants the right to 50 concurrent users. If 10
   entitlements are purchased, the total number of concurrent users
   permitted would be 500. In this example, the limit category is
   **amount**, the limit type is **users**, and the limit
   **quantification** is **50.**

   Each license key may be installed on 3 devices. If 5 license keys are
   acquired, the total number of devices allowed would be 15. In this
   example, the limit category is **usages**, the limit type is
   **device**, and the limit **quantification** is **3.**

1. Location

Locations may be logical or physical location (e.g., site, country). For
example:

-  use is allowed in Canada

Table C4. Required Fields for Location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| **Field Name**         | **Description**                                                                                                     | **Data Type**    | **Type**    |
+========================+=====================================================================================================================+==================+=============+
| Limit Identifier       | Each limit defined for an entitlement or license key must be identified by a unique value (e.g., numbered 1,2,3…)   | String           | Mandatory   |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Description      | Verbiage describing the limit.                                                                                      | String           | Mandatory   |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Behavior         | Description of the actions taken when the limit boundaries are reached.                                             | String           | Mandatory   |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Category         | Valid value: **location**                                                                                           | String           | Mandatory   |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Type             | Valid values: **city, county, state, country, region, MSA, BTA, CLLI**                                              | String           | Mandatory   |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit List             | List of locations where the VNF provider Product can be used or needs to be restricted from use                     | List of String   | Mandatory   |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Set Type         | Indicates if the list is an inclusion or exclusion.                                                                 | String           | Mandatory   |
|                        |                                                                                                                     |                  |             |
|                        | Valid Values:                                                                                                       |                  |             |
|                        |                                                                                                                     |                  |             |
|                        | **Allowed**                                                                                                         |                  |             |
|                        |                                                                                                                     |                  |             |
|                        | **Not allowed**                                                                                                     |                  |             |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Quantification   | The quantity (amount) the limit expresses.                                                                          | Number           | Optional    |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+

1. Time

Limit on the length of time the software may be used. For example:

-  license key valid for 1 year from activation

-  entitlement valid from 15 May 2018 thru 30 June 2020

Table C5. Required Fields for Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| **Field Name**         | **Description**                                                                                                               | **Data Type**    | **Type**      |
+========================+===============================================================================================================================+==================+===============+
| Limit Identifier       | Each limit defined for an entitlement or license key must be identified by a unique value (e.g., numbered)                    | String           | Mandatory     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Limit Description      | Verbiage describing the limit.                                                                                                | String           | Mandatory     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Limit Behavior         | Description of the actions taken when the limit boundaries are reached.                                                       | String           | Mandatory     |
|                        |                                                                                                                               |                  |               |
|                        | The limit behavior may also describe when a time limit takes effect. (e.g., key is valid for 1 year from date of purchase).   |                  |               |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Limit Category         | Valid value: **time**                                                                                                         | String           | Mandatory     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Limit Type             | Valid values: **duration, date**                                                                                              | String           | Mandatory     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Limit List             | List of times for which the VNF Provider Product can be used or needs to be restricted from use                               | List of String   | Mandatory     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Duration Units         | Required when limit type is duration. Valid values: **perpetual, year, quarter, month, day, minute, second, millisecond**     | String           | Conditional   |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Limit Quantification   | The quantity (amount) the limit expresses.                                                                                    | Number           | Optional      |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Start Date             | Required when limit type is date.                                                                                             | Date             | Optional      |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| End Date               | May be used when limit type is date.                                                                                          | Date             | Optional      |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+

1. Usage

Limits based on how the software is used. For example:

-  use is limited to a specific sub-set of the features/capabilities the
   software supports

-  use is limited to a certain environment (e.g., test, development,
   production…)

-  use is limited by processor (vm, cpu, core)

-  use is limited by software release

Table C6. Required Fields for Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| **Field Name**         | **Description**                                                                                              | **Data Type**    | **Type**    |
+========================+==============================================================================================================+==================+=============+
| Limit Identifier       | Each limit defined for an entitlement or license key must be identified by a unique value (e.g., numbered)   | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Description      | Verbiage describing the limit.                                                                               | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Behavior         | Description of the actions taken when the limit boundaries are reached.                                      | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Category         | Valid value: **usages**                                                                                      | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Type             | Valid values: **feature, environment, processor, version**                                                   | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit List             | List of usage limits (e.g., test, development, vm, core, R1.2.1, R1.3.5…)                                    | List of String   | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Set Type         | Indicates if the list is an inclusion or exclusion.                                                          | String           | Mandatory   |
|                        |                                                                                                              |                  |             |
|                        | Valid Values:                                                                                                |                  |             |
|                        |                                                                                                              |                  |             |
|                        | **Allowed**                                                                                                  |                  |             |
|                        |                                                                                                              |                  |             |
|                        | **Not allowed**                                                                                              |                  |             |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Quantification   | The quantity (amount) the limit expresses.                                                                   | Number           | Optional    |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+

1. Entity

Limit on the entity (product line, organization, customer) allowed to
make use of the software. For example:

-  allowed to be used in support of wireless products

-  allowed to be used only for government entities

Table C7. Required Fields for Entity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| **Field Name**         | **Description**                                                                                              | **Data Type**    | **Type**    |
+========================+==============================================================================================================+==================+=============+
| Limit Identifier       | Each limit defined for an entitlement or license key must be identified by a unique value (e.g., numbered)   | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Description      | Verbiage describing the limit.                                                                               | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Behavior         | Description of the actions taken when the limit boundaries are reached.                                      | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Category         | Valid value: **entity**                                                                                      | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Type             | Valid values: **product line, organization, internal customer, external customer**                           | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit List             | List of entities for which the VNF Provider Product can be used or needs to be restricted from use           | List of String   | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Set Type         | Indicates if the list is an inclusion or exclusion.                                                          | String           | Mandatory   |
|                        |                                                                                                              |                  |             |
|                        | Valid Values:                                                                                                |                  |             |
|                        |                                                                                                              |                  |             |
|                        | **Allowed**                                                                                                  |                  |             |
|                        |                                                                                                              |                  |             |
|                        | **Not allowed**                                                                                              |                  |             |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Quantification   | The quantity (amount) the limit expresses.                                                                   | Number           | Optional    |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+

1. Amount

These limits describe terms relative to utilization of the functions of
the software (for example, number of named users permitted, throughput,
or capacity). Limits of this type may also be relative to utilization of
other resources (for example, a limit for firewall software is not based
on use of the firewall software, but on the number of network
subscribers).

The metadata describing this type of limit includes the unit of measure
(e.g., # users, # sessions, # MB, # TB, etc.), the quantity of units,
any aggregation function (e.g., peak or average users), and aggregation
interval (day, month, quarter, year, etc.).

Table C8. Required Fields for Amount
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| **Field Name**         | **Description**                                                                                                                                                                                                                                                | **Data Type**   | **Type**    |
+========================+================================================================================================================================================================================================================================================================+=================+=============+
| Limit Identifier       | Each limit defined for an entitlement or license key must be identified by a unique value (e.g., numbered)                                                                                                                                                     | String          | Mandatory   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Limit Description      | Verbiage describing the limit.                                                                                                                                                                                                                                 | String          | Mandatory   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Limit Behavior         | Description of the actions taken when the limit boundaries are reached.                                                                                                                                                                                        | String          | Mandatory   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Limit Category         | Valid value: **amount**                                                                                                                                                                                                                                        | String          | Mandatory   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Limit Type             | Valid values: **trunk, user, subscriber, session, token, transactions, seats, KB, MB, TB, GB**                                                                                                                                                                 | String          | Mandatory   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Type of Utilization    | Is the limit relative to utilization of the functions of the software or relative to utilization of other resources?                                                                                                                                           | String          | Mandatory   |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | Valid values:                                                                                                                                                                                                                                                  |                 |             |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | -  **software functions**                                                                                                                                                                                                                                      |                 |             |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | -  **other resources**                                                                                                                                                                                                                                         |                 |             |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Limit Quantification   | The quantity (amount) the limit expresses.                                                                                                                                                                                                                     | Number          | Optional    |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Aggregation Function   | Valid values: **peak, average**                                                                                                                                                                                                                                | String          | Optional    |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Aggregation Interval   | Time period over which the aggregation is done (e.g., average sessions per quarter). Required when an Aggregation Function is specified.                                                                                                                       | String          | Optional    |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | Valid values: **day, month, quarter, year, minute, second, millisecond**                                                                                                                                                                                       |                 |             |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Aggregation Scope      | Is the limit quantity applicable to a single entitlement or license key (each separately)? Or may the limit quantity be combined with others of the same type (resulting in limit amount that is the sum of all the purchased entitlements or license keys)?   | String          | Optional    |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | Valid values:                                                                                                                                                                                                                                                  |                 |             |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | -  **single**                                                                                                                                                                                                                                                  |                 |             |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | -  **combined**                                                                                                                                                                                                                                                |                 |             |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Type of User           | Describes the types of users of the functionality offered by the software (e.g., authorized, named). This field is included when Limit Type is user.                                                                                                           | String          | Optional    |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+

d. – Requirement List
----------------------

R-11200: The VNF MUST keep the scope of a Cinder volume module, when it exists, to be 1:1 with the VNF Base Module or Incremental Module.

R-01334: The VNF **MUST** conform to the NETCONF RFC 5717, “Partial Lock Remote Procedure Call”.

R-51910: The VNF **MUST** provide all telemetry (e.g., fault event records, syslog records, performance records etc.) to ONAP using the model, format and mechanisms described in this section.

R-29324: The VNF **SHOULD** implement the protocol operation: **copy-config(target, source) -** Copy the content of the configuration datastore source to the configuration datastore target.

R-72184: The VNF **MUST** have routable FQDNs for all the endpoints (VMs) of a VNF that contain chef-clients which are used to register with the Chef Server.  As part of invoking VNF actions, ONAP will trigger push jobs against FQDNs of endpoints for a VNF, if required.

R-23740: The VNF **MUST** accommodate the security principle of “least privilege” during development, implementation and operation. The importance of “least privilege” cannot be overstated and must be observed in all aspects of VNF development and not limited to security. This is applicable to all sections of this document.

R-12709: The VNFC **SHOULD** be independently deployed, configured, upgraded, scaled, monitored, and administered by ONAP.

R-88031: The VNF **SHOULD** implement the protocol operation: **delete-config(target) -** Delete the named configuration datastore target.

R-42207: The VNF **MUST** design resiliency into a VNF such that the resiliency deployment model (e.g., active-active) can be chosen at run-time.

R-98617: The VNF provider **MUST** provide information regarding any dependency (e.g., affinity, anti-affinity) with other VNFs and resources.

R-62498: The VNF **MUST**, if not using the NCSP’s IDAM API, encrypt OA&M access (e.g., SSH, SFTP).

R-42366: The VNF **MUST** support secure connections and transports.

R-33955: The VNF **SHOULD** conform its YANG model to \*\*RFC 6991, “Common YANG Data Types”.

R-33488: The VNF **MUST** protect against all denial of service attacks, both volumetric and non-volumetric, or integrate with external denial of service protection tools.

R-57617: The VNF **MUST** include the field “success/failure” in the Security alarms (where applicable and technically feasible).

R-57271: The VNF **MUST** provide the capability of generating security audit logs by interacting with the operating system (OS) as appropriate.

R-44569: The VNF provider **MUST NOT** require additional infrastructure such as a VNF provider license server for VNF providor functions and metrics..

R-67918: The VNF **MUST** handle replication race conditions both locally and geo-located in the event of a data base instance failure to maintain service continuity.

R-35532: The VNF **SHOULD** release and clear all shared assets (memory, database operations, connections, locks, etc.) as soon as possible, especially before long running sync and asynchronous operations, so as to not prevent use of these assets by other entities.

R-37692: The VNFC **MUST** provide API versioning to allow for independent upgrades of VNFC.

R-50252: The VNF **MUST** write to a specific set of text files that will be retrieved and made available by the Ansible Server If, as part of a VNF action (e.g., audit), a playbook is required to return any VNF information.

R-58977: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Eavesdropping.

R-59391: The VNF provider **MUST**, where a VNF provider requires the assumption of permissions, such as root or administrator, first log in under their individual user login ID then switch to the other higher level account; or where the individual user login is infeasible, must login with an account with admin privileges in a way that uniquely identifies the individual performing the function.

R-93443: The VNF **MUST** define all data models in YANG [RFC6020], and the mapping to NETCONF shall follow the rules defined in this RFC.

R-72243: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Phishing / SMishing.

R-33280: The VNF **MUST NOT** use any instance specific parameters in a playbook.

R-73468: The VNF **MUST** allow the NETCONF server connection parameters to be configurable during virtual machine instantiation through Heat templates where SSH keys, usernames, passwords, SSH service and SSH port numbers are Heat template parameters.

R-46908: The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "password complexity" policy. When passwords are used, they shall be complex and shall at least meet the following password construction requirements: (1) be a minimum configurable number of characters in length, (2) include 3 of the 4 following types of characters: upper-case alphabetic, lower-case alphabetic, numeric, and special, (3) not be the same as the UserID with which they are associated or other common strings as specified by the environment, (4) not contain repeating or sequential characters or numbers, (5) not to use special characters that may have command functions, and (6) new passwords must not contain sequences of three or more characters from the previous password.

R-86261: The VNF **MUST NOT** allow VNF provider access to VNFs remotely.

R-75343: The VNF **MUST** provide the capability of testing the validity of a digital certificate by recognizing the identity represented by the certificate — the "distinguished name".

R-40813: The VNF **SHOULD** support the use of virtual trusted platform module, hypervisor security testing and standards scanning tools.

R-02454: The VNF **MUST** support the existence of multiple major/minor versions of the VNF software and/or sub-components and interfaces that support both forward and backward compatibility to be transparent to the Service Provider usage.

R-20353: The VNF **MUST** implement at least one of the capabilities **:candidate** or **:writable-running**. If both **:candidate** and **:writable-running** are provided then two locks should be supported.

R-01556: The VNF Package **MUST** include documentation describing the fault, performance, capacity events/alarms and other event records that are made available by the VNF. The document must include:

R-56815: The VNF Package **MUST** include documentation describing supported VNF scaling capabilities and capacity limits (e.g., number of users, bandwidth, throughput, concurrent calls).

R-56793: The VNF **MUST** test for adherence to the defined performance budgets at each layer, during each delivery cycle with delivered results, so that the performance budget is measured and the code is adjusted to meet performance budget.

R-54520: The VNF **MUST** log successful and unsuccessful login attempts.

R-10173: The VNF **MUST** allow another NETCONF session to be able to initiate the release of the lock by killing the session owning the lock, using the <kill-session> operation to guard against hung NETCONF sessions.

R-36280: The VNF provider **MUST** provide documentation describing VNF Functional Capabilities that are utilized to operationalize the VNF and compose complex services.

R-15671: The VNF **MUST NOT** provide public or unrestricted access to any data without the permission of the data owner. All data classification and access controls must be followed.

R-39342: The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "password changes (includes default passwords)" policy. Products will support password aging, syntax and other credential management practices on a configurable basis.

R-21558: The VNF **SHOULD** use intelligent routing by having knowledge of multiple downstream/upstream endpoints that are exposed to it, to ensure there is no dependency on external services (such as load balancers) to switch to alternate endpoints.

R-07545: The VNF **MUST** support all operations, administration and management (OAM) functions available from the supplier for VNFs using the supplied YANG code and associated NETCONF servers.

R-73541: The VNF **MIST** use access controls for VNFs and their supporting computing systems at all times to restrict access to authorized personnel only, e.g., least privilege. These controls could include the use of system configuration or access control software.

R-97102: The VNF Package **MUST** include VM requirements via a Heat template that provides the necessary data for:

R-44013: The VNF **MUST** populate an attribute, defined as node[‘PushJobOutput’] with the desired output on all nodes in the push job that execute chef-client run if the VNF action requires the output of a chef-client run be made available (e.g., get running configuration).

R-40521: The VNF **MUST**, if not using the NCSP’s IDAM API, support use of common third party authentication and authorization tools such as TACACS+, RADIUS.

R-41829: The VNF **MUST** be able to specify the granularity of the lock via a restricted or full XPath expression.

R-19768: The VNF **SHOULD** support L3 VPNs that enable segregation of traffic by application (dropping packets not belonging to the VPN) (i.e., AVPN, IPSec VPN for Internet routes).

R-55478: The VNF **MUST** log logoffs.

R-14853: The VNF **MUST** respond to a "move traffic" [2]_ command against a specific VNFC, moving all existing session elsewhere with minimal disruption if a VNF provides a load balancing function across multiple instances of its VNFCs. Note: Individual VNF performance aspects (e.g., move duration or disruption scope) may require further constraints.

R-68165: The VNF **MUST** encrypt any content containing Sensitive Personal Information (SPI) or certain proprietary data, in addition to applying the regular procedures for securing access and delivery.

R-31614: The VNF **MUST** log the field “event type” in the security audit logs.

R-87662: The VNF **SHOULD** implement the NETCONF Event Notifications [RFC5277].

R-26508: The VNF **MUST** support NETCONF server that can be mounted on OpenDaylight (client) and perform the following operations:

R-26567: The VNF Package **MUST** include a run list of roles/cookbooks/recipes, for each supported VNF action, that will perform the desired VNF action in its entirety as specified by ONAP (see Section 8.c, ONAP Controller APIs and Behavior, for list of VNF actions and requirements), when triggered by a chef-client run list in JSON file.

R-04158: The VNF **MUST** conform to the NETCONF RFC 4742, “Using the NETCONF Configuration Protocol over Secure Shell (SSH)”.

R-49109: The VNF **MUST** encrypt TCP/IP--HTTPS (e.g., TLS v1.2) transmission of data on internal and external networks.

R-15884: The VNF **MUST** include the field “date” in the Security alarms (where applicable and technically feasible).

R-15885: The VNF **MUST** Upon completion of the chef-client run, POST back on the callback URL, a JSON object as described in Table A2 if the chef-client run list includes a cookbook/recipe that is callback capable. Failure to POST on the Callback Url should not be considered a critical error. That is, if the chef-client successfully completes the VNF action, it should reflect this status on the Chef Server regardless of whether the Callback succeeded or not.

R-82223: The VNF **MUST** be decomposed if the functions have significantly different scaling characteristics (e.g., signaling versus media functions, control versus data plane functions).

R-37608: The VNF **MUST** provide a mechanism to restrict access based on the attributes of the VNF and the attributes of the subject.

R-02170: The VNF **MUST** use, whenever possible, standard implementations of security applications, protocols, and format, e.g., S/MIME, TLS, SSH, IPSec, X.509 digital certificates for cryptographic implementations. These implementations must be purchased from reputable vendors and must not be developed in-house.

R-11235: The VNF **MUST** implement the protocol operation: **kill-session(session)** - Force the termination of **session**.

R-87564: The VNF **SHOULD** conform its YANG model to RFC 7317, “A YANG Data Model for System Management”.

R-69649: The VNF **MUST** have all vulnerabilities patched as soon as possible. Patching shall be controlled via change control process with vulnerabilities disclosed along with mitigation recommendations.

R-75041: The VNF **MUST**, if not using the NCSP’s IDAM API, expire passwords at regular configurable intervals.

R-23035: The VNF **MUST** be designed to scale horizontally (more instances of a VNF or VNFC) and not vertically (moving the existing instances to larger VMs or increasing the resources within a VM) to achieve effective utilization of cloud resources.

R-97445: The VNF **MUST** log the field “date/time” in the security audit logs.

R-16777: The VNF provider **MUST** provide a JSON file for each supported action for the VNF.  The JSON file must contain key value pairs with all relevant values populated with sample data that illustrates its usage. The fields and their description are defined in Appendix B.

R-08134: The VNF **MUST** conform to the NETCONF RFC 6241, “NETCONF Configuration Protocol”.

R-01382: The VNF **MUST** allow the entire configuration of the VNF to be retrieved via NETCONF's <get-config> and <edit-config>, independently of whether it was configured via NETCONF or other mechanisms.

R-98929: The VNF **MAY** have a single endpoint.

R-48356: The VNF **MUST** fully exploit exception handling to the extent that resources (e.g., threads and memory) are released when no longer needed regardless of programming language.

R-90007: The VNF **MUST** implement the protocol operation: **close-session()**- Gracefully close the current session.

R-42140: The VNF **MUST** respond to data requests from ONAP as soon as those requests are received, as a synchronous response.

R-27511: The VNF provider **MUST** provide the ability to scale up a VNF provider supplied product during growth and scale down a VNF provider supplied product during decline without “real-time” restrictions based upon VNF provider permissions.

R-05470: The VNF **MUST** host connectors for access to the database layer.

R-85633: The VNF **MUST** implement Data Storage Encryption (database/disk encryption) for Sensitive Personal Information (SPI) and other subscriber identifiable data. Note: subscriber’s SPI/data must be encrypted at rest, and other subscriber identifiable data should be encrypted at rest. Other data protection requirements exist and should be well understood by the developer.

R-36792: The VNF **MUST** automatically retry/resubmit failed requests made by the software to its downstream system to increase the success rate.

R-49036: The VNF **SHOULD** conform its YANG model to RFC 7277, “A YANG Data Model for IP Management”.

R-63217: The VNF **MUST**, if not using the NCSP’s IDAM API, support logging via ONAP for a historical view of “who did what and when”.

R-44125: The VNF provider **MUST** agree to the process that can be met by Service Provider reporting infrastructure. The Contract shall define the reporting process and the available reporting tools.

R-22700: The VNF **MUST** conform its YANG model to RFC 6470, “NETCONF Base Notifications”.

R-74958: The VNF **MUST** activate security alarms automatically when the following event is detected: unsuccessful attempts to gain permissions or assume the identity of another user

R-44281: The VNF **MUST** implement the protocol operation: **edit-config(target, default-operation, test-option, error-option, config)** - Edit the target configuration datastore by merging, replacing, creating, or deleting new config elements.

R-81777: The VNF **MUST** be configured with initial address(es) to use at deployment time. After that the address(es) may be changed through ONAP-defined policies delivered from ONAP to the VNF using PUTs to a RESTful API, in the same way that other controls over data reporting will be controlled by policy.

R-07879: The VNF Package **MUST** include all relevant playbooks to ONAP to be loaded on the Ansible Server.

R-57855: The VNF **MUST** support hitless staggered/rolling deployments between its redundant instances to allow "soak-time/burn in/slow roll" which can enable the support of low traffic loads to validate the deployment prior to supporting full traffic loads.

R-73285: The VNF **MUST** must encode the delivered data using JSON or Avro, addressed and delivered as described in the previous paragraphs.

R-85028: The VNF **MUST** authenticate system to system access and do not conceal a VNF provider user’s individual accountability for transactions.

R-28545: The VNF **MUST** conform its YANG model to RFC 6060, “YANG - A Data Modeling Language for the Network Configuration Protocol (NETCONF)”

R-74712: The VNF **MUST** utilize FQDNs (and not IP address) for both Service Chaining and scaling.

R-29760: The VNFC **MUST** be installed on non-root file systems, unless software is specifically included with the operating system distribution of the guest image.

R-08315: The VNF **SHOULD** use redundant connection pooling to connect to any backend data source that can be switched between pools in an automated/scripted fashion to ensure high availability of the connection to the data source.

R-42874: The VNF **MUST** comply with Least Privilege (no more privilege than required to perform job functions) when persons or non-person entities access VNFs.

R-08312: The VNF **MAY** use other options which are expected to include

R-19082: The VNF **MUST NOT** run security testing tools and programs, e.g., password cracker, port scanners, hacking tools in production, without authorization of the VNF system owner.

R-39650: The VNF **SHOULD** provide the ability to test incremental growth of the VNF.

R-15325: The VNF **MUST** log the field “success/failure” in the security audit logs.

R-07617: The VNF **MUST** log creating, removing, or changing the inherent privilege level of users.

R-53015: The VNF **MUST** apply locking based on the sequence of NETCONF operations, with the first configuration operation locking out all others until completed.

R-83500: The VNF **MUST** provide the capability of allowing certificate renewal and revocation.

R-23772: The VNF **MUST** validate input at all layers implementing VNF APIs.

R-83227: The VNF **MUST** Provide the capability to encrypt data in transit on a physical or virtual network.

R-36843: The VNF **MUST** support the ability of the VNFC to be deployable in multi-zoned cloud sites to allow for site support in the event of cloud zone failure or upgrades.

R-10129: The VNF **SHOULD** conform its YANG model to RFC 7223, “A YANG Data Model for Interface Management”.

R-18733: The VNF **MUST** implement the protocol operation: **discard-changes()** - Revert the candidate configuration datastore to the running configuration.

R-21819: The VNF **MUST** support requests for information from law enforcement and government agencies.

R-92207: The VNF **SHOULD** implement a mechanism for automated and frequent "system configuration (automated provisioning / closed loop)" auditing.

R-63935: The VNF **MUST** release locks to prevent permanent lock-outs when a user configured timer has expired forcing the NETCONF SSH Session termination (i.e., product must expose a configuration knob for a user setting of a lock expiration timer)

R-79224: The VNF **MUST** have the chef-client be preloaded with validator keys and configuration to register with the designated Chef Server as part of the installation process.

R-12467: The VNF **MUST NOT** use the SHA, DSS, MD5, SHA-1 and Skipjack algorithms or other compromised encryption.

R-68589: The VNF **MUST**, if not using the NCSP’s IDAM API, support User-IDs and passwords to uniquely identify the user/application. VNF needs to have appropriate connectors to the Identity, Authentication and Authorization systems that enables access at OS, Database and Application levels as appropriate.

R-26115: The VNF **MUST** follow the data model upgrade rules defined in [RFC6020] section 10. All deviations from section 10 rules shall be handled by a built-in automatic upgrade mechanism.

R-49145: The VNF **MUST** implement **:confirmed-commit** If **:candidate** is supported.

R-04298: The VNF provider **MUST** provide their testing scripts to support testing.

R-92935: The VNF **SHOULD** minimize the propagation of state information across multiple data centers to avoid cross data center traffic.

R-47204: The VNF **MUST** protect the confidentiality and integrity of data at rest and in transit from unauthorized access and modification.

R-32695: The VNF **MUST** provide the ability to modify the number of retries, the time between retries and the behavior/action taken after the retries have been exhausted for exception handling to allow the NCSP to control that behavior.

R-58964: The VNF **MUST** provide the capability to restrict read and write access to data.

R-73364: The VNF **MUST** support at least two major versions of the VNF software and/or sub-components to co-exist within production environments at any time so that upgrades can be applied across multiple systems in a staggered manner.

R-33946: The VNF **MUST** conform to the NETCONF RFC 4741, “NETCONF Configuration Protocol”.

R-24269: The VNF **SHOULD** conform its YANG model to RFC 7407, “A YANG Data Model for SNMP Configuration”.

R-16039: The VNF **SHOULD** test for adherence to the defined resiliency rating recommendation at each layer, during each delivery cycle so that the resiliency rating is measured and feedback is provided where software resiliency requirements are not met.

R-46290: The VNF **MUST** respond to an ONAP request to deliver granular data on device or subsystem status or performance, referencing the YANG configuration model for the VNF by returning the requested data elements.

R-11240: The VNF **MUST** respond with content encoded in JSON, as described in the RESTCONF specification. This way the encoding of a synchronous communication will be consistent with Avro.

R-83790: The VNF **MUST** implement the **:validate** capability

R-83873: The VNF **MUST** support **:rollback-on-error** value for the <error-option> parameter to the <edit-config> operation. If any error occurs during the requested edit operation, then the target database (usually the running configuration) will be left affected. This provides an 'all-or-nothing' edit mode for a single <edit-config> request.

R-25238: The VNF PACKAGE **MUST** validated YANG code using the open source pyang [3]_ program using the following commands:

R-58370: The VNF **MUST** coexist and operate normally with commercial anti-virus software which shall produce alarms every time when there is a security incident.

R-39604: The VNF **MUST** provide the capability of testing the validity of a digital certificate by checking the Certificate Revocation List (CRL) for the certificates of that type to ensure that the certificate has not been revoked.

R-06617: The VNF **MUST** support get-schema (ietf-netconf-monitoring) to pull YANG model over session.

R-13344: The VNF **MUST** log starting and stopping of security logging

R-02360: The VNFC **MUST** be designed as a standalone, executable process.

R-80070: The VNF **MUST** handle errors and exceptions so that they do not interrupt processing of incoming VNF requests to maintain service continuity.

R-02137: The VNF **MUST** implement all monitoring and logging as described in the Security Analytics section.

R-16496: The VNF **MUST** enable instantiating only the functionality that is needed for the decomposed VNF (e.g., if transcoding is not needed it should not be instantiated).

R-32217: The VNF **MUST** have routable FQDNs that are reachable via the Ansible Server for the endpoints (VMs) of a VNF on which playbooks will be executed. ONAP will initiate requests to the Ansible Server for invocation of playbooks against these end points [4]_.

R-47849: The VNF provider **MUST** support the metadata about licenses (and their applicable entitlements) as defined in this document for VNF software, and any license keys required to authorize use of the VNF software.  This metadata will be used to facilitate onboarding the VNF into the ONAP environment and automating processes for putting the licenses into use and managing the full lifecycle of the licenses. The details of this license model are described in Appendix C. Note: License metadata support in ONAP is not currently available and planned for 1Q 2018.

R-85419: The VNF **SHOULD** use REST APIs exposed to Client Applications for the implementation of OAuth 2.0 Authorization Code Grant and Client Credentials Grant, as the standard interface for a VNF.

R-34660: The VNF **MUST** use the RESTCONF/NETCONF framework used by the ONAP configuration subsystem for synchronous communication.

R-88026: The VNF **MUST** include a NETCONF server enabling runtime configuration and lifecycle management capabilities.

R-48080: The VNF **SHOULD** support SCEP (Simple Certificate Enrollment Protocol).

R-43884: The VNF **MUST** integrate with external authentication and authorization services (e.g., IDAM).

R-70933: The VNF **MUST** provide the ability to migrate to newer versions of cryptographic algorithms and protocols with no impact.

R-48917: The VNF **MUST** monitor for and alert on (both sender and receiver) errant, running longer than expected and missing file transfers, so as to minimize the impact due to file transfer errors.

R-79107: The VNF **MUST**, if not using the NCSP’s IDAM API, enforce a configurable maximum number of Login attempts policy for the users. VNF provider must comply with "terminate idle sessions" policy. Interactive sessions must be terminated, or a secure, locking screensaver must be activated requiring authentication, after a configurable period of inactivity. The system-based inactivity timeout for the enterprise identity and access management system must also be configurable.

R-75850: The VNF **SHOULD** decouple persistent data from the VNFC and keep it in its own datastore that can be reached by all instances of the VNFC requiring the data.

R-46960: The VNF **MUST** utilize only the Guest OS versions that are supported by the NCSP’s Network Cloud. [5]_

R-21210: The VNF **MUST** implement the following input validation control: Validate that any input file has a correct and valid Multipurpose Internet Mail Extensions (MIME) type. Input files should be tested for spoofed MIME types.

R-23823: The VNF Package **MUST** include appropriate credentials so that ONAP can interact with the Chef Server.

R-24359: The VNF **MUST** provide the capability of testing the validity of a digital certificate by validating the date the certificate is being used is within the validity period for the certificate.

R-49224: The VNF **MUST** provide unique traceability of a transaction through its life cycle to ensure quick and efficient troubleshooting.

R-04982: The VNF **MUST NOT** include an authentication credential, e.g., password, in the security audit logs, even if encrypted.

R-74481: The VNF **MUST** NOT require the use of a dynamic routing protocol unless necessary to meet functional requirements.

R-98911: The VNF **MUST NOT** use any instance specific parameters for the VNF in roles/cookbooks/recipes invoked for a VNF action.

R-89571: The VNF **MUST** support and provide artifacts for configuration management using at least one of the following technologies:

R-87135: The VNF **MUST** comply with NIST standards and industry best practices for all implementations of cryptography.

R-04492: The VNF **MUST** generate security audit logs that must be sent to Security Analytics Tools for analysis.

R-02597: The VNF **MUST** implement the protocol operation: **lock(target)** - Lock the configuration datastore target.

R-13800: The VNF **MUST** conform to the NETCONF RFC 5277, “NETCONF Event Notification”.

R-64445: The VNF **MUST** support the ability of a requestor of the service to determine the version (and therefore capabilities) of the service so that Network Cloud Service Provider can understand the capabilities of the service.

R-64768: The VNF **MUST** limit the size of application data packets to no larger than 9000 bytes for SDN network-based tunneling when guest data packets are transported between tunnel endpoints that support guest logical networks.

R-75608: The VNF provider **MUST** provide playbooks to be loaded on the appropriate Ansible Server.

R-61354: The VNF **MUST** implement access control list for OA&M services (e.g., restricting access to certain ports or applications).

R-62468: The VNF **MUST** allow all configuration data shall to be edited through a NETCONF <edit-config> operation. Proprietary NETCONF RPCs that make configuration changes are not sufficient.

R-34552: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for OWASP Top 10.

R-29977: The VNF **MUST** provide the capability of testing the validity of a digital certificate by validating the CA signature on the certificate.

R-67709: The VNF **MUST** be designed, built and packaged to enable deployment across multiple fault zones (e.g., VNFCs deployed in different servers, racks, OpenStack regions, geographies) so that in the event of a planned/unplanned downtime of a fault zone, the overall operation/throughput of the VNF is maintained.

R-46567: The VNF Package **MUST** include configuration scripts for boot sequence and configuration.

R-55345: The VNF **SHOULD** use techniques such as “lazy loading” when initialization includes loading catalogues and/or lists which can grow over time, so that the VNF startup time does not grow at a rate proportional to that of the list.

R-88482: The VNF **SHOULD** use REST using HTTPS delivery of plain text JSON for moderate sized asynchronous data sets, and for high volume data sets when feasible.

R-56786: The VNF **MUST** implement “Closed Loop” automatic implementation (without human intervention) for Known Threats with detection rate in low false positives.

R-94525: The VNF **MUST** log connections to a network listener of the resource.

R-85428: The VNF **MUST** meet the same guidelines as Chef Server hosted by ONAP.

R-26371: The VNF **MUST** detect connectivity failure for inter VNFC instance and intra/inter VNF and re-establish connectivity automatically to maintain the VNF without manual intervention to provide service continuity.

R-35851: The VNF Package **MUST** include VNF topology that describes basic network and application connectivity internal and external to the VNF including Link type, KPIs, Bandwidth, latency, jitter, QoS (if applicable) for each interface.

R-29301: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Password Attacks.

R-23957: The VNF **MUST** include the field “time” in the Security alarms (where applicable and technically feasible).

R-32636: The VNF **MUST** support API-based monitoring to take care of the scenarios where the control interfaces are not exposed, or are optimized and proprietary in nature.

R-39562: The VNF **MUST** disable unnecessary or vulnerable cgi-bin programs.

R-77334: The VNF **MUST** allow configurations and configuration parameters to be managed under version control to ensure consistent configuration deployment, traceability and rollback.

R-44723: The VNF **MUST** use symmetric keys of at least 112 bits in length.

R-86585: The VNFC **SHOULD** minimize the use of state within a VNFC to facilitate the movement of traffic from one instance to another.

R-18725: The VNF **MUST** handle the restart of a single VNFC instance without requiring all VNFC instances to be restarted.

R-53317: The VNF **MUST** conform its YANG model to RFC 6087, “Guidelines for Authors and Reviewers of YANG Data Model Documents”.

R-67114: The VNF **MUST** be installed with:

R-28168: The VNF **SHOULD** use an appropriately configured logging level that can be changed dynamically, so as to not cause performance degradation of the VNF due to excessive logging.

R-54930: The VNF **MUST** implement the following input validation control: Do not permit input that contains content or characters inappropriate to the input expected by the design. Inappropriate input, such as SQL insertions, may cause the system to execute undesirable and unauthorized transactions against the database or allow other inappropriate access to the internal network.

R-55830: The VNF **MUST** distribute all production code from NCSP internal sources only. No production code, libraries, OS images, etc. shall be distributed from publically accessible depots.

R-22367: The VNF **MUST** support detection of malformed packets due to software misconfiguration or software vulnerability.

R-93860: The VNF **MUST** provide the capability to integrate with an external encryption service.

R-09467: The VNF **MUST**  utilize only NCSP standard compute flavors. [5]_

R-62170: The VNF **MUST** over-ride any default values for configurable parameters that can be set by ONAP in the roles, cookbooks and recipes.

R-41994: The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "No Self-Signed Certificates" policy. Self-signed certificates must be used for encryption only, using specified and approved encryption protocols such as LS 1.1 or higher or equivalent security protocols such as IPSec, AES.

R-nnnnn: The VNF MUST have a corresponding environment file for a Cinder Volume Module.

R-84160: The VNF **MUST** have security logging for VNFs and their OSs be active from initialization. Audit logging includes automatic routines to maintain activity records and cleanup programs to ensure the integrity of the audit/logging systems.

R-99656: The VNF **MUST** NOT terminate stable sessions if a VNFC instance fails.

R-80898: The VNF **MUST** support heartbeat via a <get> with null filter.

R-20974: The VNF **MUST** deploy the base module first, prior to the incremental modules.

R-69610: The VNF **MUST** provide the capability of using certificates issued from a Certificate Authority not provided by the VNF provider.

R-27310: The VNF Package **MUST** include all relevant Chef artifacts (roles/cookbooks/recipes) required to execute VNF actions requested by ONAP for loading on appropriate Chef Server.

R-98191: The VNF **MUST** vary the frequency that asynchronous data is delivered based on the content and how data may be aggregated or grouped together. For example, alarms and alerts are expected to be delivered as soon as they appear. In contrast, other content, such as performance measurements, KPIs or reported network signaling may have various ways of packaging and delivering content. Some content should be streamed immediately; or content may be monitored over a time interval, then packaged as collection of records and delivered as block; or data may be collected until a package of a certain size has been collected; or content may be summarized statistically over a time interval, or computed as a KPI, with the summary or KPI being delivered.

R-31412: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for XSS / CSRF.

R-58775: The VNF provider **MUST** provide software components that can be packaged with/near the VNF, if needed, to simulate any functions or systems that connect to the VNF system under test. This component is necessary only if the existing testing environment does not have the necessary simulators.

R-45496: The VNF **MUST** host connectors for access to the OS (Operating System) layer.

R-13151: The VNF **SHOULD** disable the paging of the data requiring encryption, if possible, where the encryption of non-transient data is required on a device for which the operating system performs paging to virtual memory. If not possible to disable the paging of the data requiring encryption, the virtual memory should be encrypted.

R-49308: The VNF **SHOULD** test for adherence to the defined resiliency rating recommendation at each layer, during each delivery cycle with delivered results, so that the resiliency rating is measured and the code is adjusted to meet software resiliency requirements.

R-74763: The VNF provider **MUST** provide an artifact per VNF that contains all of the VNF Event Records supported. The artifact should include reference to the specific release of the VNF Event Stream Common Event Data Model document it is based on. (e.g., `VES Event Listener <https://github.com/att/evel-test-collector/tree/master/docs/att_interface_definition>`__)

R-77786: The VNF Package **MUST** include all relevant cookbooks to be loaded on the ONAP Chef Server.

R-54373: The VNF **MUST** have Python >= 2.7 on the endpoint VM(s) of a VNF on which an Ansible playbook will be executed.

R-60106: The VNF **MUST** implement the protocol operation: **get(filter)** - Retrieve (a filtered subset of) the running configuration and device state information. This should include the list of VNF supported schemas.

R-35305: The VNF **MUST** meet the same guidelines as the Ansible Server hosted by ONAP.

R-95864: The VNF **MUST** use commercial tools that comply with X.509 standards and produce x.509 compliant keys for public/private key generation.

R-23475: The VNF **SHOULD** utilize only NCSP provided Guest OS images. [5]_

R-64503: The VNF **MUST** provide minimum privileges for initial and default settings for new user accounts.

R-42681: The VNF **MUST** use the NCSP’s IDAM API or comply with the requirements if not using the NCSP’s IDAM API, for identification, authentication and access control of OA&M and other system level functions.

R-19219: The VNF **MUST** provide audit logs that include user ID, dates, times for log-on and log-off, and terminal location at minimum.

R-73067: The VNF **MUST** use industry standard cryptographic algorithms and standard modes of operations when implementing cryptography.

R-25878: The VNF **MUST** use certificates issued from publicly recognized Certificate Authorities (CA) for the authentication process where PKI-based authentication is used.

R-70266: The VNF **MUST** respond to an ONAP request to deliver the current data for any of the record types defined in Section 8.d “Data Model for Event Records” by returning the requested record, populated with the current field values. (Currently the defined record types include the common header record, technology independent records such as Fault, Heartbeat, State Change, Syslog, and technology specific records such as Mobile Flow, Signaling and Voice Quality records.  Additional record types will be added in the future as they are standardized and become available.)

R-70496: The VNF **MUST** implement the protocol operation: **commit(confirmed, confirm-timeout)** - Commit candidate configuration datastore to the running configuration.

R-19624: The VNF **MUST** encode and serialize content delivered to ONAP using JSON (option 1). High-volume data is to be encoded and serialized using Avro, where Avro data format are described using JSON (option 2) [6]_.

R-25094: The VNF **MUST** perform data capture for security functions.

R-44032: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Man in the Middle (MITM).

R-47068: The VNF **MAY** expose a single endpoint that is responsible for all functionality.

R-49396: The VNF **MUST** support each VNF action by invocation of **one** playbook [7]_. The playbook will be responsible for executing all necessary tasks (as well as calling other playbooks) to complete the request.

R-63953: The VNF **MUST** have the echo command return a zero value otherwise the validation has failed

R-56904: The VNF **MUST** interoperate with the ONAP (SDN) Controller so that it can dynamically modify the firewall rules, ACL rules, QoS rules, virtual routing and forwarding rules.

R-37929: The VNF **MUST** accept all necessary instance specific data from the environment or node object attributes for the VNF in roles/cookbooks/recipes invoked for a VNF action.

R-84366: The VNF Package **MUST** include documentation describing VNF Functional APIs that are utilized to build network and application services. This document describes the externally exposed functional inputs and outputs for the VNF, including interface format and protocols supported.

R-58421: The VNF **SHOULD** be decomposed into granular re-usable VNFCs.

R-27711: The VNF provider **MUST** provide an XML file that contains a list of VNF error codes, descriptions of the error, and possible causes/corrective action.

R-78282: The VNF **MUST** conform to the NETCONF RFC 6242, “Using the Network Configuration Protocol over Secure Shell”.

R-99766: The VNF **MUST** allow configurations and configuration parameters to be managed under version control to ensure the ability to rollback to a known valid configuration.

R-89010: The VNF **MUST** survive any single points of software failure internal to the VNF (e.g., in memory structures, JMS message queues).

R-77667: The VNF **MUST** test for adherence to the defined performance budget at each layer, during each delivery cycle so that the performance budget is measured and feedback is provided where the performance budget is not met.

R-21652: The VNF **MUST** implement the following input validation control: Check the size (length) of all input. Do not permit an amount of input so great that it would cause the VNF to fail. Where the input may be a file, the VNF API must enforce a size limit.

R-54190: The VNF **MUST** release locks to prevent permanent lock-outs when/if a session applying the lock is terminated (e.g., SSH session is terminated).

R-12271: The VNF **SHOULD** conform its YANG model to RFC 7223, “IANA Interface Type YANG Module”.

R-25547: The VNF **MUST** log the field “protocol” in the security audit logs.

R-22286: The VNF **MUST** support Integration functionality via API/Syslog/SNMP to other functional modules in the network (e.g., PCRF, PCEF) that enable dynamic security control by blocking the malicious traffic or malicious end users

R-16560: The VNF **MUST** conduct a resiliency impact assessment for all inter/intra-connectivity points in the VNF to provide an overall resiliency rating for the VNF to be incorporated into the software design and development of the VNF.

R-99112: The VNF **MUST** provide the capability to restrict access to data to specific users.

R-02997: The VNF **MUST** preserve their persistent data. Running VMs will not be backed up in the Network Cloud infrastructure.

R-19367: The VNF **MUST** monitor API invocation patterns to detect anomalous access patterns that may represent fraudulent access or other types of attacks, or integrate with tools that implement anomaly and abuse detection.

R-33981: The VNF **SHOULD** interoperate with various access control mechanisms for the Network Cloud execution environment (e.g., Hypervisors, containers).

R-26881: The VNF provider **MUST** provide the binaries and images needed to instantiate the VNF (VNF and VNFC images).

R-69565: The VNF Package **MUST** include documentation describing VNF Management APIs. The document must include information and tools for:

R-92571: The VNF **MUST** provide operational instrumentation such as logging, so as to facilitate quick resolution of issues with the VNF to provide service continuity.

R-77737: The VNF **MUST**

R-29488: The VNF **MUST** implement the protocol operation: **get-config(source, filter)** - Retrieve a (filtered subset of a) configuration from the configuration datastore source.

R-03070: The VNF **MUST**, by ONAP Policy, provide the ONAP addresses as data destinations for each VNF, and may be changed by Policy while the VNF is in operation. We expect the VNF to be capable of redirecting traffic to changed destinations with no loss of data, for example from one REST URL to another, or from one TCP host and port to another.

R-89800: The VNF **MUST NOT** require Hypervisor-level customization from the cloud provider.

R-12110: The VNF **MUST NOT** use keys generated or derived from predictable functions or values, e.g., values considered predictable include user identity information, time of day, stored/transmitted data.

R-03954: The VNF **MUST** survive any single points of failure within the Network Cloud (e.g., virtual NIC, VM, disk failure).

R-98391: The VNF **MUST**, if not using the NCSP’s IDAM API, support Role-Based Access Control to permit/limit the user/application to performing specific activities.

R-29967: The VNF **MUST** conform its YANG model to RFC 6022, “YANG module for NETCONF monitoring”.

R-80335: The VNF **MUST** make visible a Warning Notices: A formal statement of resource intent, i.e., a warning notice, upon initial access to a VNF provider user who accesses private internal networks or Company computer resources, e.g., upon initial logon to an internal web site, system or application which requires authentication.

R-48596: The VNF Package **MUST** include documentation describing the characteristics for the VNF reliability and high availability.

R-49956: The VNF **MUST** pass all access to applications (Bearer, signaling and OA&M) through various security tools and platforms from ACLs, stateful firewalls and application layer gateways depending on manner of deployment. The application is expected to function (and in some cases, interwork) with these security tools.

R-02616: The VNF **MUST** permit locking at the finest granularity if a VNF needs to lock an object for configuration to avoid blocking simultaneous configuration operations on unrelated objects (e.g., BGP configuration should not be locked out if an interface is being configured or entire Interface configuration should not be locked out if a non-overlapping parameter on the interface is being configured).

R-15659: The VNF **MUST** restrict changing the criticality level of a system security alarm to administrator(s).

R-96634: The VNF provider **MUST** describe scaling capabilities to manage scaling characteristics of the VNF.

R-32641: The VNF **MUST** provide the capability to encrypt data on non-volatile memory.

R-48470: The VNF **MUST** support Real-time detection and notification of security events.

R-91681: The VNF **MUST** meet the ONAP Ansible Server API Interface requirements.

R-41825: The VNF **MUST** activate security alarms automatically when the following event is detected: configurable number of consecutive unsuccessful login attempts

R-52870: The VNF **MUST** provide a method of metrics gathering and analysis to evaluate the resiliency of the software from both a granular as well as a holistic standpoint. This includes, but is not limited to thread utilization, errors, timeouts, and retries.

R-89474: The VNF **MUST** log the field “Login ID” in the security audit logs.

R-13390: The VNF provider **MUST** provide cookbooks to be loaded on the appropriate Chef Server.

R-24825: The VNF **MUST** provide Context awareness data (device, location, time, etc.) and be able to integrate with threat detection system.

R-23882: The VNF **SHOULD** be scanned using both network scanning and application scanning security tools on all code, including underlying OS and related configuration. Scan reports shall be provided. Remediation roadmaps shall be made available for any findings.

R-22946: The VNF **SHOULD** conform its YANG model to RFC 6536, “NETCONF Access Control Model”.

R-89753: The VNF **MUST NOT** install or use systems, tools or utilities capable of capturing or logging data that was not created by them or sent specifically to them in production, without authorization of the VNF system owner.

R-88899: The VNF **MUST** support simultaneous <commit> operations within the context of this locking requirements framework.

R-96554: The VNF **MUST** implement the protocol operation: **unlock(target)** - Unlock the configuration datastore target.

R-27995: The VNF **SHOULD** include control loop mechanisms to notify the consumer of the VNF of their exceeding SLA thresholds so the consumer is able to control its load against the VNF.

R-31809: The VNF **MUST** support the HealthCheck RPC. The HealthCheck RPC, executes a VNF providor-defined VNF Healthcheck over the scope of the entire VNF (e.g., if there are multiple VNFCs, then run a health check, as appropriate, for all VNFCs). It returns a 200 OK if the test completes. A JSON object is returned indicating state (healthy, unhealthy), scope identifier, time-stamp and one or more blocks containing info and fault information. If the VNF is unable to run the HealthCheck, return a standard http error code and message.

R-25401: The VNF **MUST** use asymmetric keys of at least 2048 bits in length.

R-31961: The VNF **MUST** support integrated DPI/monitoring functionality as part of VNFs (e.g., PGW, MME).

R-47597: The VNF **MUST** carry data in motion only over secure connections.

R-43253: The VNF **MUST** use playbooks designed to allow Ansible Server to infer failure or success based on the “PLAY_RECAP” capability.

R-23135: The VNF **MUST**, if not using the NCSP’s IDAM API, authenticate system to system communications were one system accesses the resources of another system, and must never conceal individual accountability.

R-99730: The VNF **MUST** include the field “Login ID” in the Security alarms (where applicable and technically feasible).

R-88199: The VNF **MUST** utilize virtualized, scalable open source database software that can meet the performance/latency requirements of the service for all datastores.

R-08598: The VNF **MUST** log successful and unsuccessful changes to a privilege level.

R-87352: The VNF **SHOULD** utilize Cloud health checks, when available from the Network Cloud, from inside the application through APIs to check the network connectivity, dropped packets rate, injection, and auto failover to alternate sites if needed.

R-56920: The VNF **MUST** protect all security audit logs (including API, OS and application-generated logs), security audit software, data, and associated documentation from modification, or unauthorized viewing, by standard OS access control mechanisms, by sending to a remote system, or by encryption.

R-35291: The VNF **MUST** support the ability to failover a VNFC automatically to other geographically redundant sites if not deployed active-active to increase the overall resiliency of the VNF.

R-43332: The VNF **MUST** activate security alarms automatically when the following event is detected: successful modification of critical system or application files

R-81147: The VNF **MUST** have greater restrictions for access and execution, such as up to 3 factors of authentication and restricted authorization, for commands affecting network services, such as commands relating to VNFs, must.

R-60656: The VNF **MUST** support sub tree filtering.

R-51883: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Replay.

R-66070: The VNF Package **MUST** include VNF Identification Data to uniquely identify the resource for a given VNF provider. The identification data must include: an identifier for the VNF, the name of the VNF as was given by the VNF provider, VNF description, VNF provider, and version.

R-19804: The VNF **MUST** validate the CA signature on the certificate, ensure that the date is within the validity period of the certificate, check the Certificate Revocation List (CRL), and recognize the identity represented by the certificate where PKI-based authentication is used.

R-06327: The VNF **MUST** respond to a "drain VNFC" [2]_ command against a specific VNFC, preventing new session from reaching the targeted VNFC, with no disruption to active sessions on the impacted VNFC, if a VNF provides a load balancing function across multiple instances of its VNFCs. This is used to support scenarios such as proactive maintenance with no user impact,

R-85653: The VNF **MUST** provide metrics (e.g., number of sessions, number of subscribers, number of seats, etc.) to ONAP for tracking every license.

R-63330: The VNF **MUST** detect when the security audit log storage medium is approaching capacity (configurable) and issue an alarm via SMS or equivalent as to allow time for proper actions to be taken to pre-empt loss of audit data.

R-22645: The VNF **SHOULD** use commercial algorithms only when there are no applicable governmental standards for specific cryptographic functions, e.g., public key cryptography, message digests.

R-22888: The VNF provider **MUST** provide documentation for the VNF Policy Description to manage the VNF runtime lifecycle. The document must include a description of how the policies (conditions and actions) are implemented in the VNF.

R-78066: The VNF **MUST** support requests for information from law enforcement and government agencies.

R-35144: The VNF **MUST**, if not using the NCSP’s IDAM API, comply with the NCSP’s credential management policy.

R-85959: The VNF **SHOULD** automatically enable/disable added/removed sub-components or component so there is no manual intervention required.

R-28756: The VNF **MUST** support **:partial-lock** and **:partial-unlock** capabilities, defined in RFC 5717. This allows multiple independent clients to each write to a different part of the <running> configuration at the same time.

R-41252: The VNF **MUST** support the capability of online storage of security audit logs.

R-77707: The VNF provider **MUST** include a Manifest File that contains a list of all the components in the VNF package.

R-20860: The VNF **MUST** be agnostic to the underlying infrastructure (such as hardware, host OS, Hypervisor), any requirements should be provided as specification to be fulfilled by any hardware.

R-01478: The VNF Package **MUST** include documentation describing all parameters that are available to monitor the VNF after instantiation (includes all counters, OIDs, PM data, KPIs, etc.) that must be collected for reporting purposes. The documentation must include a list of:

R-22059: The VNF **MUST NOT** execute long running tasks (e.g., IO, database, network operations, service calls) in a critical section of code, so as to minimize blocking of other operations and increase concurrent throughput.

R-30650: The VNF **MUST** utilize cloud provided infrastructure and VNFs (e.g., virtualized Local Load Balancer) as part of the VNF so that the cloud can manage and provide a consistent service resiliency and methods across all VNF's.

R-30654: The VNF Package **MUST** have appropriate cookbooks that are designed to automatically ‘rollback’ to the original state in case of any errors for actions that change state of the VNF (e.g., configure).

R-29705: The VNF **MUST** restrict changing the criticality level of a system security alarm to administrator(s).

R-71787: The VNF **MUST** comply with Segregation of Duties (access to a single layer and no developer may access production without special oversight) when persons or non-person entities access VNFs.

R-86758: The VNF **SHOULD** provide an automated test suite to validate every new version of the software on the target environment(s). The tests should be of sufficient granularity to independently test various representative VNF use cases throughout its lifecycle. Operations might choose to invoke these tests either on a scheduled basis or on demand to support various operations functions including test, turn-up and troubleshooting.

R-06885: The VNF **SHOULD** support the ability to scale down a VNFC pool without jeopardizing active sessions. Ideally, an active session should not be tied to any particular VNFC instance.

R-06924: The VNF **MUST** deliver asynchronous data as data becomes available, or according to the configured frequency.

R-65134: The VNF **SHOULD** maintain state in a geographically redundant datastore that may, in fact, be its own VNFC.

R-13627: The VNF **MUST** monitor API invocation patterns to detect anomalous access patterns that may represent fraudulent access or other types of attacks, or integrate with tools that implement anomaly and abuse detection.

R-86455: The VNF **SHOULD** support hosting connectors for OS Level and Application Access.

R-68990: The VNF **MUST** support the **:startup** capability. It will allow the running configuration to be copied to this special database. It can also be locked and unlocked.

R-78010: The VNF **MUST** use the NCSP’s IDAM API for Identification, authentication and access control of customer or VNF application users.

R-46986: The VNF **SHOULD** have source code scanned using scanning tools (e.g., Fortify) and provide reports.

R-97293: The VNF provider **MUST NOT** require audits of Service Provider’s business.

R-16065: The VNF provider **MUST** provide configurable parameters (if unable to conform to YANG model) including VNF attributes/parameters and valid values, dynamic attributes and cross parameter dependencies (e.g., customer provisioning data).

R-34484: The VNF **SHOULD** create a single component VNF for VNFCs that can be used by other VNFs.

R-30278: The VNF provider **MUST** provide a Resource/Device YANG model as a foundation for creating the YANG model for configuration. This will include VNF attributes/parameters and valid values/attributes configurable by policy.

R-35401: The VNF **MUST** must support SSH and allow SSH access to the Ansible server for the endpoint VM(s) and comply with the  Network Cloud Service Provider guidelines for authentication and access.

R-68200: The VNF **MUST** support the **:url** value to specify protocol operation source and target parameters. The capability URI for this feature will indicate which schemes (e.g., file, https, sftp) that the server supports within a particular URL value. The 'file' scheme allows for editable local configuration databases. The other schemes allow for remote storage of configuration databases.

R-41159: The VNF **MUST** deliver any and all functionality from any VNFC in the pool. The VNFC pool member should be transparent to the client. Upstream and downstream clients should only recognize the function being performed, not the member performing it.

R-18864: The VNF **MUST** NOT use technologies that bypass virtualization layers (such as SR-IOV) unless approved by the NCSP (e.g., if necessary to meet functional or performance requirements).

R-37028: The VNF **MUST** be composed of one “base” module.

R-40827: The VNF provider **MUST** enumerate all of the open source licenses their VNF(s) incorporate.

R-95950: The VNF **MUST** provide a NETCONF interface fully defined by supplied YANG models for the embedded NETCONF server.

R-10716: The VNF **MUST** support parallel and simultaneous configuration of separate objects within itself.

R-71842: The VNF **MUST** include the field “service or program used for access” in the Security alarms (where applicable and technically feasible).

R-54430: The VNF **MUST** use the NCSP’s supported library and compute flavor that supports DPDK to optimize network efficiency if using DPDK. [5]_

R-03465: The VNF **MUST** release locks to prevent permanent lock-outs when the corresponding <partial-unlock> operation succeeds.

R-65755: The VNF **SHOULD** support callback URLs to return information to ONAP upon completion of the chef-client run for any chef-client run associated with a VNF action.

R-11499: The VNF **MUST** fully support the XPath 1.0 specification for filtered retrieval of configuration and other database contents. The 'type' attribute within the <filter> parameter for <get> and <get-config> operations may be set to 'xpath'. The 'select' attribute (which contains the XPath expression) will also be supported by the server. A server may support partial XPath retrieval filtering, but it cannot advertise the **:xpath** capability unless the entire XPath 1.0 specification is supported.

R-95105: The VNF **MUST** host connectors for access to the application layer.

R-77157: The VNF **MUST** conform to approved request, workflow authorization, and authorization provisioning requirements when creating privileged users.

R-63473: The VNF **MUST** automatically advertise newly scaled components so there is no manual intervention required.

R-13613: The VNF **MUST** provide clear measurements for licensing purposes to allow automated scale up/down by the management system.

R-66793: The VNF **MUST** guarantee the VNF configuration integrity for all simultaneous configuration operations (e.g., if a change is attempted to the BUM filter rate from multiple interfaces on the same EVC, then they need to be sequenced in the VNF without locking either configuration method out).

R-19790: The VNF **MUST NOT** include authentication credentials in security audit logs, even if encrypted.

R-97529: The VNF **SHOULD** implement the protocol operation: **get-schema(identifier, version, format) -** Retrieve the YANG schema.

R-84473: The VNF **MUST** enable DPDK in the guest OS for VNF’s requiring high packets/sec performance.  High packet throughput is defined as greater than 500K packets/sec.

R-54816: The VNF **MUST** support the storage of security audit logs for agreed period of time for forensic analysis.

R-34957: The VNF **MUST** provide a method of metrics gathering for each layer's performance to identify/document variances in the allocations so they can be addressed.

R-43958: The VNF Package **MUST** include documentation describing the tests that were conducted by the VNF provider and the test results.

R-61648: The VNF **MUST** support event logging, formats, and delivery tools to provide the required degree of event data to ONAP

R-18525: The VNF provider **MUST** provide a JSON file for each supported action for the VNF.  The JSON file must contain key value pairs with all relevant values populated with sample data that illustrates its usage. The fields and their description are defined in Appendix A.

R-99174: The VNF **MUST** comply with Individual Accountability (each person must be assigned a unique ID) when persons or non-person entities access VNFs.

R-99771: The VNF **MUST** provide all code/configuration files in a “Locked down” or hardened state or with documented recommendations for such hardening. All unnecessary services will be disabled. VNF provider default credentials, community strings and other such artifacts will be removed or disclosed so that they can be modified or removed during provisioning.

R-58358: The VNF **MUST** implement the **:with-defaults** capability [RFC6243].

R-78116: The VNF **MUST** update status on the Chef Server appropriately (e.g., via a fail or raise an exception) if the chef-client run encounters any critical errors/failures when executing a VNF action.

R-84879: The VNF **MUST** have the capability of maintaining a primary and backup DNS name (URL) for connecting to ONAP collectors, with the ability to switch between addresses based on conditions defined by policy such as time-outs, and buffering to store messages until they can be delivered. At its discretion, the service provider may choose to populate only one collector address for a VNF. In this case, the network will promptly resolve connectivity problems caused by a collector or network failure transparently to the VNF.

R-06413: The VNF **MUST** log the field “service or program used for access” in the security audit logs.

R-51442: The VNF **SHOULD** use playbooks that are designed to automatically ‘rollback’ to the original state in case of any errors for actions that change state of the VNF (e.g., configure).

R-98989: The VNF **SHOULD** utilize resource pooling (threads, connections, etc.) within the VNF application so that resources are not being created and destroyed resulting in resource management overhead.

R-58998: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Malware (Key Logger).

R-52499: The VNF **MUST** meet their own resiliency goals and not rely on the Network Cloud.

R-43327: The VNF **SHOULD** use “Modeling JSON text with YANG”, https://trac.tools.ietf.org/id/draft-lhotka-netmod-yang-json-00.html, If YANG models need to be translated to and from JSON. YANG configuration and content can be represented via JSON, consistent with Avro, as described in “Encoding and Serialization” section.

R-52060: The VNF **MUST** provide the capability to configure encryption algorithms or devices so that they comply with the laws of the jurisdiction in which there are plans to use data encryption.

R-10353: The VNF **MUST** conform its YANG model to RFC 6244, “An Architecture for Network Management Using NETCONF and YANG”.

R-26586: The VNF **SHOULD** support the ability to work with aliases (e.g., gateways, proxies) to protect and encapsulate resources.

R-14025: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Session Hijacking.

R-86835: The VNF **MUST** set the default settings for user access to sensitive commands and data to deny authorization.

R-73583: The VNF **MUST** allow changes of configuration parameters to be consumed by the VNF without requiring the VNF or its sub-components to be bounced so that the VNF availability is not effected.

R-73223: The VNF **MUST** support proactive monitoring to detect and report the attacks on resources so that the VNFs and associated VMs can be isolated, such as detection techniques for resource exhaustion, namely OS resource attacks, CPU attacks, consumption of kernel memory, local storage attacks.

R-06668: The VNF **MUST** handle the start or restart of VNFC instances in any order with each VNFC instance establishing or re-establishing required connections or relationships with other VNFC instances and/or VNFs required to perform the VNF function/role without requiring VNFC instance(s) to be started/restarted in a particular order.

R-41215: The VNF **MAY** have zero to many “incremental” modules.

R-85991: The VNF provider **MUST** provide a universal license key per VNF to be used as needed by services (i.e., not tied to a VM instance) as the recommended solution. The VNF provider may provide pools of Unique VNF License Keys, where there is a unique key for each VNF instance as an alternate solution. Licensing issues should be resolved without interrupting in-service VNFs.

R-52085: The VNF **MUST**, if not using the NCSP’s IDAM API, provide the ability to support Multi-Factor Authentication (e.g., 1st factor = Software token on device (RSA SecureID); 2nd factor = User Name+Password, etc.) for the users.

R-29495: The VNF **MUST** support locking if a common object is being manipulated by two simultaneous NETCONF configuration operations on the same VNF within the context of the same writable running data store (e.g., if an interface parameter is being configured then it should be locked out for configuration by a simultaneous configuration operation on that same interface parameter).

R-31751: The VNF **MUST** subject VNF provider VNF access to privilege reconciliation tools to prevent access creep and ensure correct enforcement of access policies.

R-48698: The VNF **MUST** utilize   information from key value pairs that will be provided by the Ansible Server as extra-vars during invocation to execute the desired VNF action. If the playbook requires files, they must also be supplied using the methodology detailed in the Ansible Server API.

R-44290: The VNF **MUST** control access to ONAP and to VNFs, and creation of connections, through secure credentials, log-on and exchange mechanisms.

R-40293: The VNF **MUST** make available (or load on VNF Ansible Server) playbooks that conform to the ONAP requirement.

R-30932: The VNF **MUST** provide security audit logs including records of successful and rejected system access data and other resource access attempts.

R-12538: The VNF **SHOULD** support load balancing and discovery mechanisms in resource pools containing VNFC instances.

R-59610: The VNF **MUST** implement the data model discovery and download as defined in [RFC6022].

R-49945: The VNF **MUST** authorize VNF provider access through a client application API by the client application owner and the resource owner of the VNF before provisioning authorization through Role Based Access Control (RBAC), Attribute Based Access Control (ABAC), or other policy based mechanism.

R-20912: The VNF **MUST** support alternative monitoring capabilities when VNFs do not expose data or control traffic or use proprietary and optimized protocols for inter VNF communication.


e. - Ansible Playbook Examples
------------------------------

The following sections contain examples of Ansible playbook contents
which follow the guidelines.

Guidelines for Playbooks to properly integrate with APPC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NOTE: To support concurrent requests to multiple VNF instances of same
or different type, VNF hosts and other files with VNF specific default
values are kept or created in separate directories.

Example of an Ansible command (after pwd) to run playbook again
vfdb9904v VNF instance:

.. code-block:: none

 $ pwd
 /storage/vfdb/V16.1/ansible/configure
 $ ansible-playbook -i ../inventory/vfdb9904v/hosts site.yml --extra-vars "vnf_instance=vfdb9904v"

Example of corresponding APPC API Call from ONAP – Ansible Server
Specifications:

An example POST for requesting execution of configure Playbook:

.. code-block:: none

 {"Id": "10", "PlaybookName":
 "/storage/vfdb/latest/ansible/configure/site.yml", "NodeList":
 ["vfdb9904v"], "Timeout": 60, "EnvParameters": {"Retry": 3, "Wait": 5},
 "LocalParameters": {"vfdb9904v": {"T_true": 10, "T_false": 5,
 "T_nfo": 5}}}

Comments:

-  An ID number is assigned to each request. This ID number is used to
   track request down to completion and provide status to APPC when
   requested.

-  Playbook Name provided in the request (full path in this case)

-  Playbook path (in this example provided as part of playbook name as
   full path) or, later in a separate variable, playbook root directory
   needs to be part of APPC template.

Ansible Playbooks will use the VNF instance name (passed using
--extra-vars "vnf_instance=vfdb9904v") to identify other default values
to run the playbook(s) against the target VNF instance. Same example as
above:

.. code-block:: none

 $ ansible-playbook -i ../inventory/vfdb9904v/hosts site.yml --extra-vars "vnf_instance=vfdb9904v"

SSH key info (name/path), used to authenticate with the VNF VMs, is one
of the attributes stored in the Ansible Server inventory hosts file for
the VNF instance and later will be passed down by APPC, in the inventory
hosts file, to the Ansible Server as part of the request. Here hosts
file to run ansible-playbook listed in this example above (IP addresses
were scrubbed):

.. code-block:: none

 $ more ../inventory/vfdb9904v/hosts
 [host]
 localhost ansible_connection=local

 [oam]
 1xx.2yy.zzz.109 ansible_ssh_private_key_file=/storage/.ssh/Kilo-SSH-Key.pem
 1xx.2yy.zzz.110 ansible_ssh_private_key_file=/storage/.ssh/Kilo-SSH-Key.pem

 [rdb]
 1xx.2yy.zzz.105 ansible_ssh_private_key_file=/storage/.ssh/Kilo-SSH-Key.pem
 1xx.2yy.zzz.106 ansible_ssh_private_key_file=/storage/.ssh/Kilo-SSH-Key.pem

NOTE: APPC requests to run Playbooks/Cookbooks are specific to a VNF,
but could be more limited to one VM or one type of VM by the request
parameters. Actions that may impact a site (LCP), a service, or an
entire platform must be orchestrated by MSO in order to execute requests
via APPC which then invoke VNF level playbooks. Playbooks that impact
more than a single VNF are not the current focus of these guidelines.

And here the scrubbed default arguments for this VNF instance:

.. code-block:: none

 vnf_instance=vfdb9904v

 $ more ../vars/vfdb9904v/default_args.yml
 vnf_provider_network_network: d69fea03-xxx-yyy-zzz-nnnnnnnnnnnn
 vnf_provider_network_subnet: a07f6a3d-xxxx-yyy-zzz-ssssssssssss
 vm_config_oam_vnfc_name: vfdb9904vm001oam001
 vm_config_oam_hostname: vfdb9904vm001
 vm_config_oam_provider_ip_address: 1xx.2yy.zzz.109
 …

IMPORTANT: The APPC and default file attribute name for
vm_config_oam_vnfc_name, as an example, is derived from vm_config
array structure (list) in the CSAR package ENV file, with dots replaced
by underscore:

.. code-block:: none

 vm_config:

 oam: {vnfc_name: {{ vm_config_oam_vnfc_name }}, hostname: {{
 vm_config_oam_hostname }}, provider_ip_address: {{
 vm_config_oam_provider_ip_address }

 },

 …

Parameters like VNF names, VNFC names, OA&M IP addresses, after
February, 2018 ONAP release, will be extracted from A&AI by APPC and
then passed down to Ansible Server, as part of APPC request through REST
API. In the meantime, these VNF instance specific required values, will
be stored on VNF instance directory, default arguments file and will be
used as defaults. For parameterized playbooks attribute-value pairs
passed down by APPC to Ansible Server always take precedence over
template or VNF instance specific defaults stored in defaults file(s).

.. code-block:: none

 $ pwd
 /storage/vfdb/latest/ansible

 $ more vars/vfdb9904v/default_args.yml

 vm_config_oam1_vnfc_name: vfdb9904vm001oam001
 vm_config_oam1_hostname: vfdb9904vm001
 vm_config_oam1_provider_ip_address: 1xx.2yy.zzz.109

 vm_config_oam2_vnfc_name: vfdb9904vm002oam001
 vm_config_oam2_hostname: vfdb9904vm002
 vm_config_oam2_provider_ip_address: 1xx.2yy.zzz.110

 vm_config_rdb1_vnfc_name: vfdb9904vm003rdb001
 vm_config_rdb1_hostname: vfdb9904vm003
 vm_config_rdb1_provider_ip_address: 1xx.2yy.zzz.105

 vm_config_rdb2_vnfc_name: vfdb9904vm004rdb001
 vm_config_rdb2_hostname: vfdb9904vm004
 vm_config_rdb2_provider_ip_address: 1xx.2yy.zzz.106

 vm_config_rdb3_vnfc_name: vfdb9904vm005rdb001
 vm_config_rdb3_hostname: vfdb9904vm005
 vm_config_rdb3_provider_ip_address: 1xx.2yy.zzz.xxx

 vm_config_rdb4_vnfc_name: vfdb9904vm006rdb001
 vm_config_rdb4_hostname: vfdb9904vm006
 vm_config_rdb4_provider_ip_address: 1xx.2yy.zzz.yyy

One of the first tasks on the Ansible Playbooks is to combine the VNF
type generic template, derived from ENV files in CSAR or other files,
with these default values stored on the Ansible Server, together with
the overriding parameters passed down from APPC, to create the VNF
instance specific set of attribute-value pairs to be used for the run in
YAML format. Here is an excerpt from such a file that should look
somewhat similar to ENV files:

.. code-block:: none

 $ more tmp/vfdb9904v/all.yml

 deployment_prefix: vfdb9904v
 vm_config:
 oam1: { vnfc_name: vfdb9904vm001oam001, hostname: vfdb9904vm001, provider_ip_address: 1xx.2yy.zzz.109, private_ip_address: 192.168.10.107 }
 oam2: { vnfc_name: vfdb9904vm002oam001, hostname: vfdb9904vm002, provider_ip_address: 1xx.2yy.zzz.110, private_ip_address: 192.168.10.108 }
 rdb1: { vnfc_name: vfdb9904vm003rdb001, hostname: vfdb9904vm003, provider_ip_address: 1xx.2yy.zzz.105, private_ip_address: 192.168.10.109 }
 rdb2: { vnfc_name: vfdb9904vm004rdb001, hostname: vfdb9904vm004, provider_ip_address: 1xx.2yy.zzz.106, private_ip_address: 192.168.10.110 }
 rdb3: { vnfc_name: vfdb9904vm005rdb001, hostname: vfdb9904vm005, provider_ip_address: 1xx.2yy.zzz.xxx, private_ip_address: 192.168.10.111 }
 rdb4: { vnfc_name: vfdb9904vm006rdb001, hostname: vfdb9904vm006, provider_ip_address: 1xx.2yy.zzz.yyy, private_ip_address: 192.168.10.112 }
 …
 timezone: Etc/UTC
 …
 template_version: '2014-10-16'
 stack_name: vfdb9904v
 key_name: ONAPkilo-keypair
 c3dbtype: OAM
 stackName: vfdb9904v
 juno_base: true
 …

# logins list contain 'login name', 'login group', 'login password'

.. code-block:: none

 logins:
 - { name: 'm99999', group: 'm99999', password: 'abcdefgha' }
 - { name: 'gsuser', group: 'gsuser', password: ' abcdefgha' }
 - { name: 'peruser', group: 'peruser', password: ' abcdefgha' }
 - { name: 'dbuser', group: 'dbuser', password: ' abcdefgha' }

NOTE: Arguments passed by APPC to Ansible Server to run a playbook take
precedence over any defaults stored in Ansible Server.

Ansible Playbooks – Notes On Artifacts Required to Run Playbooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inventory hosts file: should be VNF instance specific.

Default variables: should be VNF instance specific/

NOTE: Some playbooks may rely on inventory directory contents to target
the collection of VNFs in the Services Platform supported through
Ansible.

Playbooks and paths to referenced files: Playbooks shall not use
absolute paths for file include entries (variables or playbooks) or
other types of references.

For this to work properly when running playbooks, the directory where
the playbook resides shall be the current directory.

Playbook includes use paths relative to the main playbook directory when
necessary.

Root directory named ansible - Any files provided with playbooks,
included or referenced by playbooks, shall reside under the ansible
playbooks (root) directory, containing all playbook subdirectories, or
below that ansible root directory, in other subdirectories to support
on-boarding and portability of VNF collection of playbooks and related
artifacts.

Designing for a shared environment, concurrently running playbooks,
targeting multiple VNF instances – inventory hosts file:

To avoid inventory hosts file overwrites or collisions between multiple
concurrently running VNF instance requests, chosen approach is for each
VNF instance hosts file, to be stored under the Ansible Server Playbooks
root directory, under the inventory subdirectory, and under a directory
for each VNF instance, named after the VNF instance, as follows:

ansible/inventory/<VNF_instance_name>/hosts

Example of inventory hosts file path, relative to ansible playbooks root
directory (playbooks_dir): ansible/inventory/vnfx0001v/hosts

Designing for a shared environment, concurrently running playbooks,
targeting multiple VNF instances – default argument variables for
specific VNF instances:

Files containing attribute name value pairs (variable name and default
values), referenced/included by playbooks – Files containing VNF
instance specific default values – in a later APPC release, some or all
the default attribute value pairs contained in the defaults file, may be
passed down by APPC, to the Ansible Server, overriding these defaults:

Following the same approach for inventory hosts files, files
referenced/included by playbooks containing default values,
default_args.yml, shall be stored under a directory with VNF instance
name on the path.

Example:

ansible/vars/<VNF_instance_name>/default_args.yml

Files containing attribute name value pairs (variable name and default
values), referenced/included by playbooks – created dynamically by
playbooks:

Following the same approach for inventory hosts files, to avoid
overwrites or collisions of multiple concurrently running VNF instance
requests, files created dynamically by playbooks, based on VNF generic
templates, combined with default values and arguments passed down by
APPC (as part of the request), shall be stored under a directory with
VNF instance name on the path.

Example:

tmp/<VNF_instance_name>/all.yml

Files containing site specific (Openstack location non-instance
specific) attribute name value pairs, like NTP server and DNS server’s
IP addresses and other parameters, referenced/included by playbooks, not
VNF specific – Could/should be stored under vars directory, in a
subdirectory named after the string used to identify the site (nyc1,
lax2,…).

Examples:

ansible/vars/<Site>/default_args.yml

ansible/vars/nyc1/default_args.yml

ansible/vars/lax2/default_args.yml

\ **Ansible Server Design - Directory Structure**

To help understanding the contents of this section, here are few basic
definitions:

**VNF type a.k.a VNF Function Code** - Based on current Services
Platform naming convention, each Virtual Network Function is assigned a
4 character string (example vfdb), they are the first 4 characters on
the VNF instance name, which is 9 characters long. VNF instance name in
some cases corresponds to the stack name for the VNF when VNF instance
is built based on a single module, single stack. Example of VNF instance
name: vfdb9904v. All VNF performing this function, running the same
software, coming from the same VNF provider will start with the same 4
characters, in this example, vfdb.

VNF type, determined through these 4 characters, is also known as VNF
Function Code and is assigned by inventory team. All Services Platform
VNF Function Codes can be found in inventory database and/or A&AI as
well as Services Platform Network Design Documents.

NOTE: Current Services Platform naming convention is undergoing changes
to include geographical location to the VNF names.

Version – As in VNF software version is the release of the software
running on the VNF for which the playbooks were developed. VNF
configuration steps may change from release to release and this
<Version> in the path will allow the Ansible Server to host playbooks
associated with each software release. And run the playbooks that match
the software release running on each VNF instance. APPC initially will
not support playbook versioning only latest playbook is supported.

Playbook Function - Is a name associated with a life cycle management
task(s) performed by the playbook(s) stored in this directory. It should
clearly identify the type of action(s) performed by the main playbook
and possibly other playbooks stored in this same directory. Ideally,
playbook function would match APPC corresponding function that executes
the main playbook in this directory. Following Ansible Naming standards
main playbook is usually named site.yml. There can be other playbooks on
the same directory that use a subset of the roles used by the main
playbook site.yml. Examples of Playbook Function directory names:

-  configure – Contains post-instantiation (bulk) configuration
   playbooks, roles,…

-  healthcheck – Contains VNF health check playbook(s), roles,…

-  stop – Contains VNF application stop playbook(s), roles,…

-  start – Contains VNF application start playbook(s), roles,…

Directory structure to allow hosting multiple version sets of playbooks,
for the same VNF type, to be hosted in the runtime environment on the
Ansible Servers. Generic directory structure:

Ansible Playbooks – Function directory and main playbook:

.. code-block:: none

 /storage/<VNF type>/<Version>/ansible/<Playbook Function>/site.yml

Example – Post-instantiation (bulk) configuration –APPC Function -
Configure:

.. code-block:: none

 /storage/<VNF type>/<Version>/ansible/configure/site.yml

Example – Health-check –APPC Function - HealthCheck:

.. code-block:: none

 /storage/<VNF type>/<Version>/ansible/healthcheck/site.yml

OR (Function directory name does not need to match APPC function name)

.. code-block:: none

 /storage/<VNF type>/<Version>/ansible/check/site.yml

Ansible Directories for other artifacts – VNF inventory hosts file -
Required:

.. code-block:: none

 /storage/<VNF type>/<Version>/ansible/inventory/<VNF instance name>/hosts

Ansible Directories for other artifacts – VNF inventory hosts file –
Required:

.. code-block:: none

 /storage/<VNF type>/<Version>/ansible/vars/<VNF instance name>/default_args.yml

NOTE: This requirement is expected to be deprecated in part in the
future, for automated actions, once APPC can pass down all VNF specific
arguments for each action. Requirement remains while manual actions are
to be supported. Other automated inventory management mechanisms may be
considered in the future, Ansible supports many automated inventory
management mechanisms/tools/solutions.

Ansible Directories for other artifacts – VNF (special) groups –
Optional:

.. code-block:: none

 /storage/<VNF type>/<Version>/ansible/groups/<VNF instance name>/common_groups.yml

NOTE: Default groups will be created based on VNFC type, 3 characters,
on VNFC name. Example: “oam”, “rdb”, “dbs”, “man”, “iox”, “app”,…

Ansible Directories for other artifacts – VNF (special) other files –
Optional – Example – License file:

.. code-block:: none

 /storage/<VNF type>/<Version>/ansible/<Other directory(s)>

CAUTION: On referenced files used/required by playbooks.

-  To avoid missing files, during on-boarding or uploading of Ansible
   Playbooks and related artifacts, all permanent files (not generated
   by playbooks as part of execution), required to run any playbook,
   shall reside under the ansible root directory or below on other
   subdirectories.

-  Any references to files, on includes or other playbook entries, shall
   use relative paths.

-  This is the ansible (root directory) directory referenced on this
   note:

.. code-block:: none

     /storage/<VNF type>/<Version>/ansible/

There will be a soft link to the latest set of Ansible Playbooks for
each VNF type and this is the default set of playbooks that are executed
unless a different release is specified in APPC request.

VNF type directories use A&AI inventory VNF function code. Ansible
Playbooks will be stored on a Cinder Volume mounted on the Ansible
Servers as /storage. Example:

/storage/vfdb/latest/ansible – This soft link point to the latest set of
playbooks (or the only set)

/storage/vfdb/V16.1/ansible – Root directory for database VNF Ansible
Playbooks for release 16.1

CAUTION: To support this directory structure as the repository to store
Ansible Playbooks run by APPC, APPC API in the Ansible Server side needs
to be configured to run playbooks from directory, not MySQL database.

Ansible Server HTTP will be configured to support APPC REST API requests
to run playbooks as needed, against specific VNF instances, or specific
VM(s) as specified in the request.

ONAP APPC REST API to Ansible Server is documented separately and can be
found under ONAP (onap.org).

\ **Ansible Server – On-boarding Ansible Playbooks **

Once playbooks are developed following the guidelines listed in prior
section(s), playbooks need to be on-boarded onto Ansible Server(s). In
the future, they’ll be on-boarded and distributed through ONAP, at least
that is the proposed plan, but for now they need to be uploaded
manually.

These are the basic steps to on-board playbooks manually onto the
Ansible Server.

1. Upload CSAR, zip, or tar file containing VNF playbooks and related
   artifacts.

2. Create full directory (using –p option below) to store Ansible
   Playbooks and other artifacts under /storage file system.

   a. Includes VNF type using VNF function code 4 characters under
      /storage.

   b. Includes VNF “Version” directory as part of the path to store
      playbooks for this VNF version.

   c. Include generic ansible root directory. Creating full directory
      path as an example:

.. code-block:: none

     $ mkdir –p /storage/vfdb/V16.1/ansible**/**

3. Make this directory (VNF ansible root directory) current directory
   for next few steps:

.. code-block:: none

     cd /storage/vfdb/V16.1/ansible/

4. Extract Ansible Playbooks and other Ansible artifacts associated with
   the playbooks onto the ansible directory. Command depends on the type
   of file uploaded, examples would be:

.. code-block:: none

     tar xvf ..
     unzip …
     bunzip ..

5. Create directory for VNF (VMs) inventory hosts file with all VMs and
   OA&M IP addresses for all VNF instances with known OA&M IP addresses
   for respective VMs, example:

.. code-block:: none

    $ mkdir –p inventory/vfdb9904v

    $ touch inventory/vfdb9904v/hosts

    $ cat inventory/vfdb9904v/hosts

    [host]
    localhost ansible_connection=local

    [oam]
    1xx.2yy.zzz.109 ansible_ssh_private_key_file=/storage/.ssh/Kilo-SSH-Key.pem
    1xx.2yy.zzz.110 ansible_ssh_private_key_file=/storage/.ssh/Kilo-SSH-Key.pem

    [rdb]
    1xx.2yy.zzz.105 ansible_ssh_private_key_file=/storage/.ssh/Kilo-SSH-Key.pem
    1xx.2yy.zzz.106 ansible_ssh_private_key_file=/storage/.ssh/Kilo-SSH-Key.pem

6. Create directory to hold default arguments for each VNF instance,
   example:

.. code-block:: none

   $ mkdir –p vars/vfdb9904v
   $ touch vars/vfdb9904v/default_args.yml
   $ cat vars/vfdb9904v/default_args.yml
   vm_config_oam1_vnfc_name: vfdb9904vm001oam001
   vm_config_oam1_hostname: vfdb9904vm001
   vm_config_oam1_provider_ip_address: 1xx.2yy.zzz.109

   vm_config_oam2_vnfc_name: vfdb9904vm002oam001
   vm_config_oam2_hostname: vfdb9904vm002
   vm_config_oam2_provider_ip_address: 1xx.2yy.zzz.110

   vm_config_rdb1_vnfc_name: vfdb9904vm003rdb001
   vm_config_rdb1_hostname: vfdb9904vm003
   vm_config_rdb1_provider_ip_address: 1xx.2yy.zzz.105

   vm_config_rdb2_vnfc_name: vfdb9904vm004rdb001
   vm_config_rdb2_hostname: vfdb9904vm004
   vm_config_rdb2_provider_ip_address: 1xx.2yy.zzz.106

   vm_config_rdb3_vnfc_name: vfdb9904vm005rdb001
   vm_config_rdb3_hostname: vfdb9904vm005
   vm_config_rdb3_provider_ip_address: 1xx.2yy.zzz.xxx

   vm_config_rdb4_vnfc_name: vfdb9904vm006rdb001
   vm_config_rdb4_hostname: vfdb9904vm006
   vm_config_rdb4_provider_ip_address: 1xx.2yy.zzz.yyy

NOTE: Please note names in this file shall use underscore “_” not dots
“.” or dashes “-“.

7. Perform some basic playbook validation running with “--check” option,
   running dummy playbooks or other.

8. Upload any SSH keys referenced on hosts file to appropriate
   directory.

NOTE: HOT templates used by Heat to instantiate VNF configured by these
playbooks shall include the same SSH key to be installed as part of
instantiation.

Other non-VNF provider specific playbook tasks need to be incorporated on
overall post-instantiation configuration playbooks or company Playbooks
need to be uploaded and executed after VNF provided or internally
developed playbooks for the VNF.


.. [1]
   The “name” field is a mandatory field in a valid Chef Node Object
   JSON dictionary.

.. [2]
   Not currently supported in ONAP release 1

.. [3]
   https://github.com/mbj4668/pyang

.. [4]
   Upstream elements must provide the appropriate FQDN in the request to
   ONAP for the desired action.

.. [5]
   Refer to NCSP’s Network Cloud specification

.. [6]
   This option is not currently supported in ONAP and it is currently
   under consideration.

.. [7]
   Multiple ONAP actions may map to one playbook.
