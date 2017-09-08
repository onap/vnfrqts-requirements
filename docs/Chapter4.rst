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
being modular and reusable to enable using best-in-breed vendors

Section 5.a VNF Design in *VNF Guidelines* describes
the overall guidelines for designing VNFs from VNF Components (VNFCs).
Below are more detailed requirements for composing VNFs.

VNF Design Requirements

* R-xxxxx The VNF **SHOULD** be decomposed into granular re-usable VNFCs.
* R-xxxxx The VNF **MUST** be decomposed if the functions have significantly different scaling characteristics (e.g., signaling versus media functions, control versus data plane functions).
* R-xxxxx The VNF **MUST** enable instantiating only the functionality that is needed for the decomposed VNF (e.g., if transcoding is not needed it should not be instantiated).
* R-xxxxx The VNFC **MUST** be designed as a standalone, executable process.
* R-xxxxx The VNF **SHOULD** create a single component VNF for VNFCs that can be used by other VNFs.
* R-xxxxx The VNF **MUST** be designed to scale horizontally (more instances of a VNF or VNFC) and not vertically (moving the existing instances to larger VMs or increasing the resources within a VM) to achieve effective utilization of cloud resources.
* R-xxxxx The VNF **MUST** utilize cloud provided infrastructure and VNFs (e.g., virtualized Local Load Balancer) as part of the VNF so that the cloud can manage and provide a consistent service resiliency and methods across all VNF's.
* R-xxxxx The VNFC **SHOULD** be independently deployed, configured, upgraded, scaled, monitored, and administered by ONAP.
* R-xxxxx The VNFC **MUST** provide API versioning to allow for independent upgrades of VNFC.
* R-xxxxx The VNFC **SHOULD** minimize the use of state within a VNFC to facilitate the movement of traffic from one instance to another.
* R-xxxxx The VNF **SHOULD** maintain state in a geographically redundant datastore that may, in fact, be its own VNFC.
* R-xxxxx The VNF **SHOULD** decouple persistent data from the VNFC and keep it in its own datastore that can be reached by all instances of the VNFC requiring the data.
* R-xxxxx The VNF **MUST** utilize virtualized, scalable open source database software that can meet the performance/latency requirements of the service for all datastores.
* R-xxxxx The VNF **MUST** NOT terminate stable sessions if a VNFC instance fails.
* R-xxxxx The VNF **MUST** enable DPDK in the guest OS for VNF’s requiring high packets/sec performance.  High packet throughput is defined as greater than 500K packets/sec.
* R-xxxxx The VNF **MUST** use the NCSP’s supported library and compute flavor that supports DPDK to optimize network efficiency if using DPDK. [1]_
* R-xxxxx The VNF **MUST** NOT use technologies that bypass virtualization layers (such as SR-IOV) unless approved by the NCSP (e.g., if necessary to meet functional or performance requirements).
* R-xxxxx The VNF **MUST** limit the size of application data packets to no larger than 9000 bytes for SDN network-based tunneling when guest data packets are transported between tunnel endpoints that support guest logical networks.
* R-xxxxx The VNF **MUST** NOT require the use of a dynamic routing protocol unless necessary to meet functional requirements.

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

* R-xxxxx The VNF **MUST** meet their own resiliency goals and not rely on the Network Cloud.
* R-xxxxx The VNF **MUST** design resiliency into a VNF such that the resiliency deployment model (e.g., active-active) can be chosen at run-time.
* R-xxxxx The VNF **MUST** survive any single points of failure within the Network Cloud (e.g., virtual NIC, VM, disk failure).
* R-xxxxx The VNF **MUST** survive any single points of software failure internal to the VNF (e.g., in memory structures, JMS message queues).
* R-xxxxx The VNF **MUST** be designed, built and packaged to enable deployment across multiple fault zones (e.g., VNFCs deployed in different servers, racks, OpenStack regions, geographies) so that in the event of a planned/unplanned downtime of a fault zone, the overall operation/throughput of the VNF is maintained.
* R-xxxxx The VNF **MUST** support the ability to failover a VNFC automatically to other geographically redundant sites if not deployed active-active to increase the overall resiliency of the VNF.
* R-xxxxx The VNF **MUST** support the ability of the VNFC to be deployable in multi-zoned cloud sites to allow for site support in the event of cloud zone failure or upgrades.

Minimize Cross Data-Center Traffic
----------------------------------

Avoid performance-sapping data center-to-data center replication delay
by applying techniques such as caching and persistent transaction paths
- Eliminate replication delay impact between data centers by using a
concept of stickiness (i.e., once a client is routed to data center "A",
the client will stay with Data center “A” until the entire session is
completed).

Minimize Cross Data-Center Traffic Requirements

* R-xxxxx The VNF **SHOULD** minimize the propagation of state information across multiple data centers to avoid cross data center traffic.

Application Resilient Error Handling
------------------------------------

Ensure an application communicating with a downstream peer is equipped
to intelligently handle all error conditions. Make sure code can handle
exceptions seamlessly - implement smart retry logic and implement
multi-point entry (multiple data centers) for back-end system
applications.

Application Resilient Error Handling Requirements

* R-xxxxx The VNF **MUST** detect connectivity failure for inter VNFC instance and intra/inter VNF and re-establish connectivity automatically to maintain the VNF without manual intervention to provide service continuity.
* R-xxxxx The VNF **MUST** handle the restart of a single VNFC instance without requiring all VNFC instances to be restarted.
* R-xxxxx The VNF **MUST** handle the start or restart of VNFC instances in any order with each VNFC instance establishing or re-establishing required connections or relationships with other VNFC instances and/or VNFs required to perform the VNF function/role without requiring VNFC instance(s) to be started/restarted in a particular order.
* R-xxxxx The VNF **MUST** handle errors and exceptions so that they do not interrupt processing of incoming VNF requests to maintain service continuity.
* R-xxxxx The VNF **MUST** provide the ability to modify the number of retries, the time between retries and the behavior/action taken after the retries have been exhausted for exception handling to allow the NCSP to control that behavior.
* R-xxxxx The VNF **MUST** fully exploit exception handling to the extent that resources (e.g., threads and memory) are released when no longer needed regardless of programming language.
* R-xxxxx The VNF **MUST** handle replication race conditions both locally and geo-located in the event of a data base instance failure to maintain service continuity.
* R-xxxxx The VNF **MUST** automatically retry/resubmit failed requests made by the software to its downstream system to increase the success rate.


System Resource Optimization
----------------------------

Ensure an application is using appropriate system resources for the task
at hand; for example, do not use network or IO operations inside
critical sections, which could end up blocking other threads or
processes or eating memory if they are unable to complete. Critical
sections should only contain memory operation, and should not contain
any network or IO operation.


System Resource Optimization Requirements

* R-xxxxx The VNF **MUST NOT** execute long running tasks (e.g., IO, database, network operations, service calls) in a critical section of code, so as to minimize blocking of other operations and increase concurrent throughput.
* R-xxxxx The VNF **MUST** automatically advertise newly scaled components so there is no manual intervention required.
* R-xxxxx The VNF **MUST** utilize FQDNs (and not IP address) for both Service Chaining and scaling.
* R-xxxxx The VNF **MUST** deliver any and all functionality from any VNFC in the pool. The VNFC pool member should be transparent to the client. Upstream and downstream clients should only recognize the function being performed, not the member performing it.
* R-xxxxx The VNF **SHOULD** automatically enable/disable added/removed sub-components or component so there is no manual intervention required.
* R-xxxxx The VNF **SHOULD** support the ability to scale down a VNFC pool without jeopardizing active sessions. Ideally, an active session should not be tied to any particular VNFC instance.
* R-xxxxx The VNF **SHOULD** support load balancing and discovery mechanisms in resource pools containing VNFC instances.
* R-xxxxx The VNF **SHOULD** utilize resource pooling (threads, connections, etc.) within the VNF application so that resources are not being created and destroyed resulting in resource management overhead.
* R-xxxxx The VNF **SHOULD** use techniques such as “lazy loading” when initialization includes loading catalogues and/or lists which can grow over time, so that the VNF startup time does not grow at a rate proportional to that of the list.
* R-xxxxx The VNF **SHOULD** release and clear all shared assets (memory, database operations, connections, locks, etc.) as soon as possible, especially before long running sync and asynchronous operations, so as to not prevent use of these assets by other entities.


Application Configuration Management
------------------------------------

Leverage configuration management audit capability to drive conformity
to develop gold configurations for technologies like Java, Python, etc.

Application Configuration Management Requirements

* R-xxxxx The VNF **MUST** allow configurations and configuration parameters to be managed under version control to ensure consistent configuration deployment, traceability and rollback.
* R-xxxxx The VNF **MUST** allow configurations and configuration parameters to be managed under version control to ensure the ability to rollback to a known valid configuration.
* R-xxxxx The VNF **MUST** allow changes of configuration parameters to be consumed by the VNF without requiring the VNF or its sub-components to be bounced so that the VNF availability is not effected.


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

* R-xxxxx The VNF **SHOULD** use intelligent routing by having knowledge of multiple downstream/upstream endpoints that are exposed to it, to ensure there is no dependency on external services (such as load balancers) to switch to alternate endpoints.
* R-xxxxx The VNF **SHOULD** use redundant connection pooling to connect to any backend data source that can be switched between pools in an automated/scripted fashion to ensure high availability of the connection to the data source.
* R-xxxxx The VNF **SHOULD** include control loop mechanisms to notify the consumer of the VNF of their exceeding SLA thresholds so the consumer is able to control its load against the VNF.

Deployment Optimization
-----------------------

Reduce opportunity for failure, by human or by machine, through smarter
deployment practices and automation. This can include rolling code
deployments, additional testing strategies, and smarter deployment
automation (remove the human from the mix).

Deployment Optimization Requirements

* R-xxxxx The VNF **MUST** support at least two major versions of the VNF software and/or sub-components to co-exist within production environments at any time so that upgrades can be applied across multiple systems in a staggered manner.
* R-xxxxx The VNF **MUST** support the existence of multiple major/minor versions of the VNF software and/or sub-components and interfaces that support both forward and backward compatibility to be transparent to the Service Provider usage.
* R-xxxxx The VNF **MUST** support hitless staggered/rolling deployments between its redundant instances to allow "soak-time/burn in/slow roll" which can enable the support of low traffic loads to validate the deployment prior to supporting full traffic loads.
* R-xxxxx The VNF **MUST** support the ability of a requestor of the service to determine the version (and therefore capabilities) of the service so that Network Cloud Service Provider can understand the capabilities of the service.
* R-xxxxx The VNF **MUST** test for adherence to the defined performance budgets at each layer, during each delivery cycle with delivered results, so that the performance budget is measured and the code is adjusted to meet performance budget.
* R-xxxxx The VNF **MUST** test for adherence to the defined performance budget at each layer, during each delivery cycle so that the performance budget is measured and feedback is provided where the performance budget is not met.
* R-xxxxx The VNF **SHOULD** test for adherence to the defined resiliency rating recommendation at each layer, during each delivery cycle with delivered results, so that the resiliency rating is measured and the code is adjusted to meet software resiliency requirements.
* R-xxxxx The VNF **SHOULD** test for adherence to the defined resiliency rating recommendation at each layer, during each delivery cycle so that the resiliency rating is measured and feedback is provided where software resiliency requirements are not met.

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

* R-xxxxx The VNF **MUST** provide a method of metrics gathering for each layer's performance to identify/document variances in the allocations so they can be addressed.
* R-xxxxx The VNF **MUST** provide unique traceability of a transaction through its life cycle to ensure quick and efficient troubleshooting.
* R-xxxxx The VNF **MUST** provide a method of metrics gathering and analysis to evaluate the resiliency of the software from both a granular as well as a holistic standpoint. This includes, but is not limited to thread utilization, errors, timeouts, and retries.
* R-xxxxx The VNF **MUST** provide operational instrumentation such as logging, so as to facilitate quick resolution of issues with the VNF to provide service continuity.
* R-xxxxx The VNF **MUST** monitor for and alert on (both sender and receiver) errant, running longer than expected and missing file transfers, so as to minimize the impact due to file transfer errors.
* R-xxxxx The VNF **SHOULD** use an appropriately configured logging level that can be changed dynamically, so as to not cause performance degradation of the VNF due to excessive logging.
* R-xxxxx The VNF **SHOULD** utilize Cloud health checks, when available from the Network Cloud, from inside the application through APIs to check the network connectivity, dropped packets rate, injection, and auto failover to alternate sites if needed.
* R-xxxxx The VNF **MUST** conduct a resiliency impact assessment for all inter/intra-connectivity points in the VNF to provide an overall resiliency rating for the VNF to be incorporated into the software design and development of the VNF.

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
   requirements for the VNFs that the vendors will need to address.

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

* R-xxxxx The VNF **MUST** accommodate the security principle of “least privilege” during development, implementation and operation. The importance of “least privilege” cannot be overstated and must be observed in all aspects of VNF development and not limited to security. This is applicable to all sections of this document.
* R-xxxxx The VNF **MUST** implement access control list for OA&M services (e.g., restricting access to certain ports or applications).
* R-xxxxx The VNF **MUST** implement Data Storage Encryption (database/disk encryption) for Sensitive Personal Information (SPI) and other subscriber identifiable data. Note: subscriber’s SPI/data must be encrypted at rest, and other subscriber identifiable data should be encrypted at rest. Other data protection requirements exist and should be well understood by the developer.
* R-xxxxx The VNF **SHOULD** implement a mechanism for automated and frequent "system configuration (automated provisioning / closed loop)" auditing.
* R-xxxxx The VNF **SHOULD** be scanned using both network scanning and application scanning security tools on all code, including underlying OS and related configuration. Scan reports shall be provided. Remediation roadmaps shall be made available for any findings.
* R-xxxxx The VNF **SHOULD** have source code scanned using scanning tools (e.g., Fortify) and provide reports. 
* R-xxxxx The VNF **MUST** distribute all production code from NCSP internal sources only. No production code, libraries, OS images, etc. shall be distributed from publically accessible depots.
* R-xxxxx The VNF **MUST** provide all code/configuration files in a “Locked down” or hardened state or with documented recommendations for such hardening. All unnecessary services will be disabled. Vendor default credentials, community strings and other such artifacts will be removed or disclosed so that they can be modified or removed during provisioning.
* R-xxxxx The VNF **SHOULD** support L3 VPNs that enable segregation of traffic by application (dropping packets not belonging to the VPN) (i.e., AVPN, IPSec VPN for Internet routes).
* R-xxxxx The VNF **SHOULD** interoperate with various access control mechanisms for the Network Cloud execution environment (e.g., Hypervisors, containers).
* R-xxxxx The VNF **SHOULD** support the use of virtual trusted platform module, hypervisor security testing and standards scanning tools.
* R-xxxxx The VNF **MUST** interoperate with the ONAP (SDN) Controller so that it can dynamically modify the firewall rules, ACL rules, QoS rules, virtual routing and forwarding rules.
* R-xxxxx The VNF **SHOULD** support the ability to work with aliases (e.g., gateways, proxies) to protect and encapsulate resources.
* R-xxxxx The VNF **MUST** pass all access to applications (Bearer, signaling and OA&M) through various security tools and platforms from ACLs, stateful firewalls and application layer gateways depending on manner of deployment. The application is expected to function (and in some cases, interwork) with these security tools.
* R-xxxxx The VNF **MUST** have all vulnerabilities patched as soon as possible. Patching shall be controlled via change control process with vulnerabilities disclosed along with mitigation recommendations.
* R-xxxxx The VNF **MUST** use the NCSP’s IDAM API for Identification, authentication and access control of customer or VNF application users.
* R-xxxxx The VNF **MUST** use the NCSP’s IDAM API or comply with the requirements if not using the NCSP’s IDAM API, for identification, authentication and access control of OA&M and other system level functions.
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, support User-IDs and passwords to uniquely identify the user/application. VNF needs to have appropriate connectors to the Identity, Authentication and Authorization systems that enables access at OS, Database and Application levels as appropriate.
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, provide the ability to support Multi-Factor Authentication (e.g., 1st factor = Software token on device (RSA SecureID); 2nd factor = User Name+Password, etc.) for the users.
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, support Role-Based Access Control to permit/limit the user/application to performing specific activities.
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, support logging via ONAP for a historical view of “who did what and when”.
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, encrypt OA&M access (e.g., SSH, SFTP).
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, enforce a configurable maximum number of Login attempts policy for the users. VNF vendor must comply with "terminate idle sessions" policy. Interactive sessions must be terminated, or a secure, locking screensaver must be activated requiring authentication, after a configurable period of inactivity. The system-based inactivity timeout for the enterprise identity and access management system must also be configurable.
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, comply with the NCSP’s credential management policy.
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, expire passwords at regular configurable intervals.
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "password complexity" policy. When passwords are used, they shall be complex and shall at least meet the following password construction requirements: (1) be a minimum configurable number of characters in length, (2) include 3 of the 4 following types of characters: upper-case alphabetic, lower-case alphabetic, numeric, and special, (3) not be the same as the UserID with which they are associated or other common strings as specified by the environment, (4) not contain repeating or sequential characters or numbers, (5) not to use special characters that may have command functions, and (6) new passwords must not contain sequences of three or more characters from the previous password.
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "password changes (includes default passwords)" policy. Products will support password aging, syntax and other credential management practices on a configurable basis.
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, support use of common third party authentication and authorization tools such as TACACS+, RADIUS.
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "No Self-Signed Certificates" policy. Self-signed certificates must be used for encryption only, using specified and approved encryption protocols such as LS 1.1 or higher or equivalent security protocols such as IPSec, AES.
* R-xxxxx The VNF **MUST**, if not using the NCSP’s IDAM API, authenticate system to system communications were one system accesses the resources of another system, and must never conceal individual accountability.

VNF Identity and Access Management Requirements
-----------------------------------------------

The following security requirements for logging, identity, and access
management need to be met by the solution in a virtual environment:


Identity and Access Management Requirements

* R-xxxxx The VNF **MUST** host connectors for access to the application layer.
* R-xxxxx The VNF **MUST** host connectors for access to the OS (Operating System) layer.
* R-xxxxx The VNF **MUST** host connectors for access to the database layer.
* R-xxxxx The VNF **MUST** 
* R-xxxxx The VNF **MUST** comply with Individual Accountability (each person must be assigned a unique ID) when persons or non-person entities access VNFs.
* R-xxxxx The VNF **MUST** comply with Least Privilege (no more privilege than required to perform job functions) when persons or non-person entities access VNFs.
* R-xxxxx The VNF **MUST** comply with Segregation of Duties (access to a single layer and no developer may access production without special oversight) when persons or non-person entities access VNFs.
* R-xxxxx The VNF **MUST NOT** allow vendor access to VNFs remotely.
* R-xxxxx The VNF **MUST** authorize vendor access through a client application API by the client application owner and the resource owner of the VNF before provisioning authorization through Role Based Access Control (RBAC), Attribute Based Access Control (ABAC), or other policy based mechanism.
* R-xxxxx The VNF **MUST** subject vendor VNF access to privilege reconciliation tools to prevent access creep and ensure correct enforcement of access policies.
* R-xxxxx The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for OWASP Top 10.
* R-xxxxx The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Password Attacks.
* R-xxxxx The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Phishing / SMishing.
* R-xxxxx The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Malware (Key Logger).
* R-xxxxx The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Session Hijacking.
* R-xxxxx The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for XSS / CSRF.
* R-xxxxx The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Replay.
* R-xxxxx The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Man in the Middle (MITM).
* R-xxxxx The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Eavesdropping.
* R-xxxxx The VNF **MUST** provide Context awareness data (device, location, time, etc.) and be able to integrate with threat detection system.
* R-xxxxx The VNF vendor **MUST**, where a VNF vendor requires the assumption of permissions, such as root or administrator, first log in under their individual user login ID then switch to the other higher level account; or where the individual user login is infeasible, must login with an account with admin privileges in a way that uniquely identifies the individual performing the function.
* R-xxxxx The VNF **MUST** authenticate system to system access and do not conceal a VNF vendor user’s individual accountability for transactions.
* R-xxxxx The VNF **MUST** make visible a Warning Notices: A formal statement of resource intent, i.e., a warning notice, upon initial access to a VNF vendor user who accesses private internal networks or Company computer resources, e.g., upon initial logon to an internal web site, system or application which requires authentication.
* R-xxxxx The VNF **MIST** use access controls for VNFs and their supporting computing systems at all times to restrict access to authorized personnel only, e.g., least privilege. These controls could include the use of system configuration or access control software.
* R-xxxxx The VNF **MUST** provide minimum privileges for initial and default settings for new user accounts.
* R-xxxxx The VNF **MUST** set the default settings for user access to sensitive commands and data to deny authorization.
* R-xxxxx The VNF **MUST** conform to approved request, workflow authorization, and authorization provisioning requirements when creating privileged users.
* R-xxxxx The VNF **MUST** have greater restrictions for access and execution, such as up to 3 factors of authentication and restricted authorization, for commands affecting network services, such as commands relating to VNFs, must.
* R-xxxxx The VNF **MUST** encrypt TCP/IP--HTTPS (e.g., TLS v1.2) transmission of data on internal and external networks.
* R-xxxxx The VNF **MUST** disable unnecessary or vulnerable cgi-bin programs.
* R-xxxxx The VNF **MUST NOT** provide public or unrestricted access to any data without the permission of the data owner. All data classification and access controls must be followed.
* R-xxxxx The VNF **MUST NOT** install or use systems, tools or utilities capable of capturing or logging data that was not created by them or sent specifically to them in production, without authorization of the VNF system owner.
* R-xxxxx The VNF **MUST NOT** run security testing tools and programs, e.g., password cracker, port scanners, hacking tools in production, without authorization of the VNF system owner.
* R-xxxxx The VNF **MUST NOT** include authentication credentials in security audit logs, even if encrypted.
* R-xxxxx The VNF **SHOULD** use REST APIs exposed to Client Applications for the implementation of OAuth 2.0 Authorization Code Grant and Client Credentials Grant, as the standard interface for a VNF.
* R-xxxxx The VNF **SHOULD** support hosting connectors for OS Level and Application Access.
* R-xxxxx The VNF **SHOULD** support SCEP (Simple Certificate Enrollment Protocol).


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

* R-xxxxx The VNF **MUST** provide a mechanism to restrict access based on the attributes of the VNF and the attributes of the subject.
* R-xxxxx The VNF **MUST** integrate with external authentication and authorization services (e.g., IDAM).
* R-xxxxx The VNF **MUST** use certificates issued from publicly recognized Certificate Authorities (CA) for the authentication process where PKI-based authentication is used.
* R-xxxxx The VNF **MUST** validate the CA signature on the certificate, ensure that the date is within the validity period of the certificate, check the Certificate Revocation List (CRL), and recognize the identity represented by the certificate where PKI-based authentication is used.
* R-xxxxx The VNF **MUST** protect the confidentiality and integrity of data at rest and in transit from unauthorized access and modification.
* R-xxxxx The VNF **MUST** protect against all denial of service attacks, both volumetric and non-volumetric, or integrate with external denial of service protection tools.
* R-xxxxx The VNF **MUST** implement the following input validation control: Check the size (length) of all input. Do not permit an amount of input so great that it would cause the VNF to fail. Where the input may be a file, the VNF API must enforce a size limit.
* R-xxxxx The VNF **MUST** implement the following input validation control: Do not permit input that contains content or characters inappropriate to the input expected by the design. Inappropriate input, such as SQL insertions, may cause the system to execute undesirable and unauthorized transactions against the database or allow other inappropriate access to the internal network.
* R-xxxxx The VNF **MUST** implement the following input validation control: Validate that any input file has a correct and valid Multipurpose Internet Mail Extensions (MIME) type. Input files should be tested for spoofed MIME types.
* R-xxxxx The VNF **MUST** validate input at all layers implementing VNF APIs.
* R-xxxxx The VNF **MUST** comply with NIST standards and industry best practices for all implementations of cryptography.
* R-xxxxx The VNF **MUST** implement all monitoring and logging as described in the Security Analytics section.
* R-xxxxx The VNF **MUST** restrict changing the criticality level of a system security alarm to administrator(s).
* R-xxxxx The VNF **MUST** monitor API invocation patterns to detect anomalous access patterns that may represent fraudulent access or other types of attacks, or integrate with tools that implement anomaly and abuse detection.
* R-xxxxx The VNF **MUST** support requests for information from law enforcement and government agencies.


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

* R-xxxxx The VNF **MUST** support Real-time detection and notification of security events.
* R-xxxxx The VNF **MUST** support Integration functionality via API/Syslog/SNMP to other functional modules in the network (e.g., PCRF, PCEF) that enable dynamic security control by blocking the malicious traffic or malicious end users
* R-xxxxx The VNF **MUST** support API-based monitoring to take care of the scenarios where the control interfaces are not exposed, or are optimized and proprietary in nature.
* R-xxxxx The VNF **MUST** support event logging, formats, and delivery tools to provide the required degree of event data to ONAP
* R-xxxxx The VNF **MUST** support detection of malformed packets due to software misconfiguration or software vulnerability.
* R-xxxxx The VNF **MUST** support integrated DPI/monitoring functionality as part of VNFs (e.g., PGW, MME).
* R-xxxxx The VNF **MUST** support alternative monitoring capabilities when VNFs do not expose data or control traffic or use proprietary and optimized protocols for inter VNF communication.
* R-xxxxx The VNF **MUST** support proactive monitoring to detect and report the attacks on resources so that the VNFs and associated VMs can be isolated, such as detection techniques for resource exhaustion, namely OS resource attacks, CPU attacks, consumption of kernel memory, local storage attacks.
* R-xxxxx The VNF **MUST** coexist and operate normally with commercial anti-virus software which shall produce alarms every time when there is a security incident.
* R-xxxxx The VNF **MUST** protect all security audit logs (including API, OS and application-generated logs), security audit software, data, and associated documentation from modification, or unauthorized viewing, by standard OS access control mechanisms, by sending to a remote system, or by encryption.
* R-xxxxx The VNF **MUST** log successful and unsuccessful login attempts.
* R-xxxxx The VNF **MUST** log logoffs.
* R-xxxxx The VNF **MUST** log successful and unsuccessful changes to a privilege level.
* R-xxxxx The VNF **MUST** log starting and stopping of security logging
* R-xxxxx The VNF **MUST** log creating, removing, or changing the inherent privilege level of users.
* R-xxxxx The VNF **MUST** log connections to a network listener of the resource.
* R-xxxxx The VNF **MUST** log the field “event type” in the security audit logs.
* R-xxxxx The VNF **MUST** log the field “date/time” in the security audit logs.
* R-xxxxx The VNF **MUST** log the field “protocol” in the security audit logs.
* R-xxxxx The VNF **MUST** log the field “service or program used for access” in the security audit logs.
* R-xxxxx The VNF **MUST** log the field “success/failure” in the security audit logs.
* R-xxxxx The VNF **MUST** log the field “Login ID” in the security audit logs.
* R-xxxxx The VNF **MUST NOT** include an authentication credential, e.g., password, in the security audit logs, even if encrypted.
* R-xxxxx The VNF **MUST** detect when the security audit log storage medium is approaching capacity (configurable) and issue an alarm via SMS or equivalent as to allow time for proper actions to be taken to pre-empt loss of audit data.
* R-xxxxx The VNF **MUST** support the capability of online storage of security audit logs.
* R-xxxxx The VNF **MUST** activate security alarms automatically when the following event is detected: configurable number of consecutive unsuccessful login attempts
* R-xxxxx The VNF **MUST** activate security alarms automatically when the following event is detected: successful modification of critical system or application files
* R-xxxxx The VNF **MUST** activate security alarms automatically when the following event is detected: unsuccessful attempts to gain permissions or assume the identity of another user
* R-xxxxx The VNF **MUST** include the field “date” in the Security alarms (where applicable and technically feasible).
* R-xxxxx The VNF **MUST** include the field “time” in the Security alarms (where applicable and technically feasible).
* R-xxxxx The VNF **MUST** include the field “service or program used for access” in the Security alarms (where applicable and technically feasible).
* R-xxxxx The VNF **MUST** include the field “success/failure” in the Security alarms (where applicable and technically feasible).
* R-xxxxx The VNF **MUST** include the field “Login ID” in the Security alarms (where applicable and technically feasible).
* R-xxxxx The VNF **MUST** restrict changing the criticality level of a system security alarm to administrator(s).
* R-xxxxx The VNF **MUST** monitor API invocation patterns to detect anomalous access patterns that may represent fraudulent access or other types of attacks, or integrate with tools that implement anomaly and abuse detection.
* R-xxxxx The VNF **MUST** support requests for information from law enforcement and government agencies.
* R-xxxxx The VNF **MUST** implement “Closed Loop” automatic implementation (without human intervention) for Known Threats with detection rate in low false positives.
* R-xxxxx The VNF **MUST** perform data capture for security functions.
* R-xxxxx The VNF **MUST** generate security audit logs that must be sent to Security Analytics Tools for analysis.
* R-xxxxx The VNF **MUST** provide audit logs that include user ID, dates, times for log-on and log-off, and terminal location at minimum.
* R-xxxxx The VNF **MUST** provide security audit logs including records of successful and rejected system access data and other resource access attempts.
* R-xxxxx The VNF **MUST** support the storage of security audit logs for agreed period of time for forensic analysis.
* R-xxxxx The VNF **MUST** provide the capability of generating security audit logs by interacting with the operating system (OS) as appropriate.
* R-xxxxx The VNF **MUST** have security logging for VNFs and their OSs be active from initialization. Audit logging includes automatic routines to maintain activity records and cleanup programs to ensure the integrity of the audit/logging systems.

VNF Data Protection Requirements
--------------------------------

This section covers VNF data protection requirements that are mostly
applicable to security monitoring.


Data Protection Requirements

* R-xxxxx The VNF **MUST** provide the capability to restrict read and write access to data.
* R-xxxxx The VNF **MUST** provide the capability to restrict access to data to specific users.
* R-xxxxx The VNF **MUST** Provide the capability to encrypt data in transit on a physical or virtual network.
* R-xxxxx The VNF **MUST** provide the capability to encrypt data on non-volatile memory.
* R-xxxxx The VNF **SHOULD** disable the paging of the data requiring encryption, if possible, where the encryption of non-transient data is required on a device for which the operating system performs paging to virtual memory. If not possible to disable the paging of the data requiring encryption, the virtual memory should be encrypted.
* R-xxxxx The VNF **MUST** provide the capability to integrate with an external encryption service.
* R-xxxxx The VNF **MUST** use industry standard cryptographic algorithms and standard modes of operations when implementing cryptography.
* R-xxxxx The VNF **SHOULD** use commercial algorithms only when there are no applicable governmental standards for specific cryptographic functions, e.g., public key cryptography, message digests.
* R-xxxxx The VNF **MUST NOT** use the SHA, DSS, MD5, SHA-1 and Skipjack algorithms or other compromised encryption.
* R-xxxxx The VNF **MUST** use, whenever possible, standard implementations of security applications, protocols, and format, e.g., S/MIME, TLS, SSH, IPSec, X.509 digital certificates for cryptographic implementations. These implementations must be purchased from reputable vendors and must not be developed in-house.
* R-xxxxx The VNF **MUST** provide the ability to migrate to newer versions of cryptographic algorithms and protocols with no impact.
* R-xxxxx The VNF **MUST** use symmetric keys of at least 112 bits in length.
* R-xxxxx The VNF **MUST** use asymmetric keys of at least 2048 bits in length.
* R-xxxxx The VNF **MUST** use commercial tools that comply with X.509 standards and produce x.509 compliant keys for public/private key generation.
* R-xxxxx The VNF **MUST NOT** use keys generated or derived from predictable functions or values, e.g., values considered predictable include user identity information, time of day, stored/transmitted data.
* R-xxxxx The VNF **MUST** provide the capability to configure encryption algorithms or devices so that they comply with the laws of the jurisdiction in which there are plans to use data encryption.
* R-xxxxx The VNF **MUST** provide the capability of using certificates issued from a Certificate Authority not provided by the VNF vendor.
* R-xxxxx The VNF **MUST** provide the capability of allowing certificate renewal and revocation.
* R-xxxxx The VNF **MUST** provide the capability of testing the validity of a digital certificate by validating the CA signature on the certificate.
* R-xxxxx The VNF **MUST** provide the capability of testing the validity of a digital certificate by validating the date the certificate is being used is within the validity period for the certificate.
* R-xxxxx The VNF **MUST** provide the capability of testing the validity of a digital certificate by checking the Certificate Revocation List (CRL) for the certificates of that type to ensure that the certificate has not been revoked.
* R-xxxxx The VNF **MUST** provide the capability of testing the validity of a digital certificate by recognizing the identity represented by the certificate — the "distinguished name".

d. VNF Modularity
=================

VNF Modularity Overview
-----------------------

ONAP supports a modular Heat design pattern, referred to as *VNF
Modularity.* With this approach, a single VNF may be composed from one
or more Heat templates, each of which represents some subset of the
overall VNF. These component parts are referred to as “\ *VNF
Modules*\ ”. During orchestration, these modules may be deployed
incrementally to build up the complete VNF.

A Heat template can be either one of the following types of modules:

1. Base Module

2. Incremental Modules

3. Independent Cinder Volume Modules

* R-xxxxx The VNF **MUST** follow the naming convention (Section 5.b Filenames) for the ONAP Heat template. The naming convention identifies the module type.

* R-xxxxx The VNF **MUST** be composed of one “base” VNF module (also called a base module).
* R-xxxxx The VNF **MAY** have zero to many “incremental” or “add on” VNF modules.
* R-xxxxx The VNF **MUST** deploy the base module first, prior to the add-on modules.

A module can be thought of as equivalent to a Heat template, where a
Heat template is composed of a YAML file and an environment file (also
referred to as an ENV file). A given YAML file must have a corresponding
environment file; ONAP requires it.

A Heat template is used to create or deploy a Heat stack. Therefore, a
module is also equivalent to a Heat Stack.

ONAP supports the concept of an optional, independent deployment of
a Cinder volume via separate Heat templates. This allows the volume to
persist after VNF deletion so that the volume can be reused on another
instance (e.g. during a failover activity).

* R-xxxxx The VNF **MUST** keep the scope of a volume module, when it exists, to be 1:1 with the VNF Module (base or add-on).
* R-xxxxx The VNF **MUST** create only the volumes needed by a single VNF module (base or add-on) in a single volume module.

These concepts will be described in more detail throughout the document.
This overview is provided to set the stage and help clarify the concepts
that will be introduced.

Design Pattern: VNF Modularity
------------------------------

ONAP supports the concept of *VNF Modularity*. With this approach,
a single VNF may be composed from one or more Heat templates, each of
which represents some subset of the overall VNF. These component parts
are referred to as “\ *VNF Modules*\ ”. During orchestration, these
modules may be deployed incrementally to build up the complete VNF.

A Heat template can be either one for the following types of modules

1. Base Module

2. Incremental Modules

3. Independent Cinder Volume Modules

The ONAP Heat template naming convention must be followed (Section
5.b Filenames). The naming convention identifies the module type.

A VNF must be composed of one “base” VNF module (also called a base
module) and zero to many “incremental” or “add on” VNF modules. The base
module must be deployed first prior to the add-on modules.

A module can be thought of as equivalent to a Heat template, where a
Heat template is composed of a YAML file and an environment file. A
given YAML file must have a corresponding environment file; ONAP
requires it. A Heat template is used to create or deploy a Heat stack.
Therefore, a module is also equivalent to a Heat Stack.

* R-xxxxx The VNF **MUST** have a corresponding environment file for given YAML file.

However, there are cases where a module maybe composed of more than one
Heat stack and/or more than one YAML file.

As discussed in Section 5.b, Independent Volume Templates, each VNF
Module may have an associated Volume template.

-  When a volume template is utilized, it must correspond 1:1 with
   add-on module template or base template it is associated with

-  A Cinder volume may be embedded within the add-on module template
   and/or base template if persistence is not required, thus not
   requiring the optional Volume template.

* R-xxxxx The VNF **MAY** have a VNF module that supports nested templates. In this case, there will be
one or more additional YAML files.

* R-xxxxx The VNF **MUST** expose any shared resource defined in the base module template and used across the entire VNF (e.g., private networks, server groups) to the incremental or add-on modules by declaring their resource UUIDs as Heat outputs (i.e., ONAP Base Template Output Parameter in the output section of the Heat template).Those outputs will be provided by ONAP as input parameter values to all add-on module Heat templates in the VNF that have declared the parameter in the template.

*Note:* A Cinder volume is *not* considered a shared resource. A volume
template must correspond 1:1 with a base template or add-on module
template.

There are two suggested usage patterns for modular VNFs, though any
variation is supported.

A. **Modules per VNFC type**

   a. Group all VMs (VNFCs) of a given type into its own module

   b. Build up the VNF one VNFC type at a time

   c. Base module contains only the shared resources (and possibly
      initial Admin VMs)

   d. Suggest one or two modules per VNFC type

      i.  one for initial count

      ii. one for scaling increment (if different from initial count)

B. **Base VNF + Growth Units**

   a. Base module (template) contains a complete initial VNF instance

   b. Growth modules for incremental scaling units

      i.  May contain VMs of multiple types in logical scaling
          combinations

      ii. May be separated by VM type for multi-dimensional scaling

   c. With no growth units, this is equivalent to the “\ *One Heat
      Template per VNF*\ ” model

Note that modularization of VNFs is not required. A single Heat template
(a base template) may still define a complete VNF, which might be
appropriate for smaller VNFs without a lot of scaling options.

There are some rules to follow when building modular VNF templates:

1. All VNFs must have one Base VNF Module (template) that must be the
   first one deployed. The base template:

   a. Must include all shared resources (e.g., private networks, server
      groups, security groups)

   b. Must expose all shared resources (by UUID) as “outputs” in its
      associated Heat template (i.e., ONAP Base Template Output
      Parameters)

   c. May include initial set of VMs

   d. May be operational as a stand-alone “minimum” configuration of the
      VNF

2. VNFs may have one or more Add-On VNF Modules (templates) which:

   a. Defines additional resources that can be added to an existing VNF

   b. Must be complete Heat templates

      i. i.e. not snippets to be incorporated into some larger template

   c. Should define logical growth-units or sub-components of an overall
      VNF

   d. On creation, receives all Base VNF Module outputs as parameters

      i.  Provides access to all shared resources (by UUID)

      ii. must not be dependent on other Add-On VNF Modules

   e. Multiple instances of an Add-On VNF Module type may be added to
      the same VNF (e.g. incrementally grow a VNF by a fixed “add-on”
      growth units)

3. Each VNF Module (base or add-on) may have (optional) an associated
   Volume template (*see Section 5.b, Independent Volume Templates*)

   a. Volume templates should correspond 1:1 with Module (base or
      add-on) templates

   b. A Cinder volume may be embedded within the Module template (base
      or add-on) if persistence is not required

4. Shared resource UUIDs are passed between the base template and add-on
   template via Heat Outputs Parameters (i.e., Base Template Output
   Parameters)

   a. The output parameter name in the base must match the parameter
      name in the add-on module

*Examples:*

In this example, the {vm-type} have been defined as “lb” for load
balancer and “admin” for admin server.

1. **Base VNF Module Heat Template (partial)**

Heat\_template\_version: 2013-05-23

.. code-block:: python

    parameters:
        admin\_name\_0:
            type: string

    resources:
        int\_oam\_network:
            type: OS::Neutron::Network
            properties:
                name: {… }

        admin\_server:
            type: OS::Nova::Server
            properties:
            name: {get\_param: admin\_name\_0}
            image: ...

    outputs:
        int\_oam\_net\_id:
            value: {get\_resource: int\_oam\_network }


2. **Add-on VNF Module Heat Template (partial)**

Heat\_template\_version: 2013-05-23

.. code-block:: python

    Parameters:
        int\_oam\_net\_id:
            type: string
            description: ID of shared private network from Base template
        lb\_name\_0:
            type: string
            description: name for the add-on VM instance

    Resources:
        lb\_server:
            type: OS::Nova::Server
            properties:
                name: {get\_param: lb\_name\_0}
                networks:
                    - port: { get\_resource: lb\_port }
                    ...

        lb\_port:
            type: OS::Neutron::Port
            properties:
                network\_id: { get\_param: int\_oam\_net\_id }
    ...

Scaling Considerations
----------------------

* R-xxxxx The VNF **MAY** be scaled by (**static scaling**) manually driven to add new capacity or **(dynamic scaling)** driven in near real-time by the ONAP controllers based on a real-time need.

With VNF Modularity, the recommended approach for scaling is to provide
additional “growth unit” templates that can be used to create additional
resources in logical scaling increments. This approach is very
straightforward, and has minimal impact on the currently running VNFCs
and must comply with the following:

-  Combine resources into reasonable-sized scaling increments; do not
   just scale by one VM at a time in potentially large VNFs.

-  Combine related resources into the same growth template where
   appropriate, e.g. if VMs of different types are always deployed in
   pairs, include them in a single growth template.

-  Growth templates can use the private networks and other shared
   resources exposed by the Base Module template.

* R-xxxxx The VNF **SHOULD** be scaled by providing additional "growth unit" templates that can be used to create additional resources in logical scaling increments.

VNF Modules may also be updated “in-place” using the OpenStack Heat
Update capability, by deploying an updated Heat template with different
VM counts to an existing stack. This method requires another VNF module
template that includes the new resources *in addition to all resources
contained in the original module template*. Note that this also requires
re-specification of all existing parameters as well as new ones.

* R-xxxxx The VNF **MAY** be scaled "in-place" using the OpenStack Heat update capability.

*For this approach:*

-  Use a fixed number of pre-defined VNF module configurations

-  Successively larger templates must be identical to the next smaller
   one, plus add the additional VMs of the scalable type(s)

-  VNF is scalable by sending a stack-update with a different template

*Please do note that:*

-  If properties do not change for existing VMs, those VMs should remain
   unchanged

-  If the update is performed with a smaller template, the Heat engine
   recognizes and deletes no-longer-needed VMs (and associated
   resources)

-  Nested templates for the various server types will simplify reuse
   across multiple configurations

-  Per the section on Use of Heat ResourceGroup, if *ResourceGroup* is
   ever used for scaling (e.g. increment the count and include an
   additional element to each list parameter), Heat will often rebuild
   every existing element in addition to adding the “deltas”.  For this
   reason, use of *ResourceGroup* for scaling in this manner is not
   supported.

e. VNF Devops
=============

This section includes guidelines for vendors to ensure that a Network
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

* R-xxxxx The VNF **MUST** utilize only the Guest OS versions that are supported by the NCSP’s Network Cloud. [1]_
* R-xxxxx The VNF **SHOULD** utilize only NCSP provided Guest OS images. [2]_
* R-xxxxx The VNF **MUST**  utilize only NCSP standard compute flavors. [2]_
* R-xxxxx The VNF **MUST** preserve their persistent data. Running VMs will not be backed up in the Network Cloud infrastructure.
* R-xxxxx The VNFC **MUST** be installed on non-root file systems, unless software is specifically included with the operating system distribution of the guest image.
* R-xxxxx The VNF **MUST** be agnostic to the underlying infrastructure (such as hardware, host OS, Hypervisor), any requirements should be provided as specification to be fulfilled by any hardware.
* R-xxxxx The VNF **MUST NOT** require Hypervisor-level customization from the cloud provider.
* R-xxxxx The VNF **SHOULD** provide an automated test suite to validate every new version of the software on the target environment(s). The tests should be of sufficient granularity to independently test various representative VNF use cases throughout its lifecycle. Operations might choose to invoke these tests either on a scheduled basis or on demand to support various operations functions including test, turn-up and troubleshooting.
* R-xxxxx The VNF **SHOULD** provide the ability to test incremental growth of the VNF.
* R-xxxxx The VNF **MUST** respond to a "move traffic" [3]_ command against a specific VNFC, moving all existing session elsewhere with minimal disruption if a VNF provides a load balancing function across multiple instances of its VNFCs. Note: Individual VNF performance aspects (e.g., move duration or disruption scope) may require further constraints.
* R-xxxxx  The VNF **MUST** respond to a "drain VNFC" [2]_ command against a specific VNFC, preventing new session from reaching the targeted VNFC, with no disruption to active sessions on the impacted VNFC, if a VNF provides a load balancing function across multiple instances of its VNFCs. This is used to support scenarios such as proactive maintenance with no user impact,

f. VNF Develop Steps
=======================

Aid to help the VNF vendor to fasten the integration with the GVNFM, the
OpenO provides the VNF SDK tools, and the documents. In this charter,
the develop steps for VNF vendors will be introduced.

First, using the VNF SDK tools to design the VNF with TOSCA model and
output the VNF TOSCA package. The VNF package can be validated, and
tested.

Second, the VNF vendor should provide the VNF Rest API to integrate with
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
   Refer to NCSP’s Network Cloud specification

.. [3]
   Not currently supported in ONAP release 1
