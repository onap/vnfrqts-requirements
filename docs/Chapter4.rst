**4. VNF Development Requirements**
====================================

a. VNF Design
==============

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
=================

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
--------------------

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
----------------------------------

Avoid performance-sapping data center-to-data center replication delay
by applying techniques such as caching and persistent transaction paths
- Eliminate replication delay impact between data centers by using a
concept of stickiness (i.e., once a client is routed to data center "A",
the client will stay with Data center “A” until the entire session is
completed).

Minimize Cross Data-Center Traffic Requirements

* R-92935 The VNF **SHOULD** minimize the propagation of state information across multiple data centers to avoid cross data center traffic.

Application Resilient Error Handling
------------------------------------

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
----------------------------

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
------------------------------------

Leverage configuration management audit capability to drive conformity
to develop gold configurations for technologies like Java, Python, etc.

Application Configuration Management Requirements

* R-77334 The VNF **MUST** allow configurations and configuration parameters to be managed under version control to ensure consistent configuration deployment, traceability and rollback.
* R-99766 The VNF **MUST** allow configurations and configuration parameters to be managed under version control to ensure the ability to rollback to a known valid configuration.
* R-73583 The VNF **MUST** allow changes of configuration parameters to be consumed by the VNF without requiring the VNF or its sub-components to be bounced so that the VNF availability is not effected.


Intelligent Transaction Distribution & Management
-------------------------------------------------

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
-----------------------

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
----------------------

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
===============

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
---------------------------------

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
* R-41994 The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "No Self-Signed Certificates" policy. Self-signed certificates must be used for encryption only, using specified and approved encryption protocols such as TLS 1.2 or higher or equivalent security protocols such as IPSec, AES.
* R-23135 The VNF **MUST**, if not using the NCSP’s IDAM API, authenticate system to system communications were one system accesses the resources of another system, and must never conceal individual accountability.

VNF Identity and Access Management Requirements
-----------------------------------------------

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
* R-73541 The VNF **MUST** use access controls for VNFs and their supporting computing systems at all times to restrict access to authorized personnel only, e.g., least privilege. These controls could include the use of system configuration or access control software.
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
-----------------------------

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
-----------------------------------

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
--------------------------------

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
=================

ONAP Heat Orchestration Templates: Overview
-------------------------------------------

ONAP supports a modular Heat Orchestration Template design pattern,
referred to as *VNF Modularity.*

ONAP VNF Modularity Overview
----------------------------

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

* R-38474 The VNF MUST have a corresponding environment file for a Base Module.
* R-81725 The VNF MUST have a corresponding environment file for an Incremental Module.
* R-53433 The VNF MUST have a corresponding environment file for a Cinder Volume Module.

These concepts will be described in more detail throughout the document.
This overview is provided to set the stage and help clarify the concepts
that will be introduced.


ONAP VNF Modularity
-------------------

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
has a property security\_groups which provides the security groups
associated with port. The value of parameter(s) associated with this
property must be the UUIDs of the resource(s)
OS::Neutron::SecurityGroup.

*Note:* A Cinder volume is *not* considered a shared resource. A volume
template must correspond 1:1 with a base template or add-on module
template.

Suggested Patterns for Modular VNFs
-----------------------------------

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
----------------

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
-----------------------

*Example: Base Module creates SecurityGroup*

A VNF has a base module, named base.yaml, that defines a
OS::Neutron::SecurityGroup. The security group will be referenced by an
OS::Neutron::Port resource in an incremental module, named
INCREMENTAL\_MODULE.yaml. The base module defines a parameter in the out
section named dns\_sec\_grp\_id. dns\_sec\_grp\_id is defined as a
parameter in the incremental module. ONAP captures the UUID value of
dns\_sec\_grp\_id from the base module output statement and provides the
value to the incremental module.

Note that the example below is not a complete Heat Orchestration
Template. The {network-role} has been defined as oam to represent an oam
network and the {vm-type} has been defined as dns.

base\_MODULE.yaml

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


INCREMENTAL\_MODULE.yaml

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

A VNF has a base module, named base\_module.yaml, that creates an
internal network. An incremental module, named incremental\_module.yaml,
will create a VM that will connect to the internal network. The base
module defines a parameter in the out section named int\_oam\_net\_id.
int\_oam\_net\_id is defined as a parameter in the incremental module.
ONAP captures the UUID value of int\_oam\_net\_id from the base module
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
=============

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

* R-46960 NCSPs **MAY** operate a limited set of Guest OS and CPU architectures and families, virtual machines, etc.
* R-23475 VNFCs **SHOULD** be agnostic to the details of the Network Cloud (such as hardware, host OS, Hypervisor or container technology) and must run on the Network Cloud with acknowledgement to the paradigm that the Network Cloud will continue to rapidly evolve and the underlying components of the platform will change regularly.
* R-33846 The VNF **MUST** install the NCSP required software on Guest OS images when not using the NCSP provided Guest OS images. [1]_
* R-09467 The VNF **MUST**  utilize only NCSP standard compute flavors. [1]_
* R-02997 The VNF **MUST** preserve their persistent data. Running VMs will not be backed up in the Network Cloud infrastructure.
* R-29760 The VNFC **MUST** be installed on non-root file systems, unless software is specifically included with the operating system distribution of the guest image.
* R-20860 The VNF **MUST** be agnostic to the underlying infrastructure (such as hardware, host OS, Hypervisor), any requirements should be provided as specification to be fulfilled by any hardware.
* R-89800 The VNF **MUST NOT** require Hypervisor-level customization from the cloud provider.
* R-86758 The VNF **SHOULD** provide an automated test suite to validate every new version of the software on the target environment(s). The tests should be of sufficient granularity to independently test various representative VNF use cases throughout its lifecycle. Operations might choose to invoke these tests either on a scheduled basis or on demand to support various operations functions including test, turn-up and troubleshooting.
* R-39650 The VNF **SHOULD** provide the ability to test incremental growth of the VNF.
* R-14853 The VNF **MUST** respond to a "move traffic" [2]_ command against a specific VNFC, moving all existing session elsewhere with minimal disruption if a VNF provides a load balancing function across multiple instances of its VNFCs. Note: Individual VNF performance aspects (e.g., move duration or disruption scope) may require further constraints.
* R-06327 The VNF **MUST** respond to a "drain VNFC" [2]_ command against a specific VNFC, preventing new session from reaching the targeted VNFC, with no disruption to active sessions on the impacted VNFC, if a VNF provides a load balancing function across multiple instances of its VNFCs. This is used to support scenarios such as proactive maintenance with no user impact.
* R-64713 The VNF **SHOULD** support a software promotion methodology from dev/test -> pre-prod -> production in software, development & testing and operations. 

f. VNF Develop Steps
=======================

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
