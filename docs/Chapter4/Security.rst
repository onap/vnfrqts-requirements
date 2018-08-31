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


VNF Security
----------------------

The objective of this section is to provide the key security
requirements that need to be met by VNFs. The security requirements are
grouped into five areas as listed below. Other security areas will be
addressed in future updates. These security requirements are applicable
to all VNFs. Additional security requirements for specific types of VNFs
will be applicable and are outside the scope of these general
requirements.

Section 4.3 Security in *VNF Guidelines* outlines
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section provides details on the VNF general security requirements
on various security areas such as user access control, network security,
ACLs, infrastructure security, and vulnerability management. These
requirements cover topics associated with compliance, security patching,
logging/accounting, authentication, encryption, role-based access
control, least privilege access/authorization. The following security
requirements need to be met by the solution in a virtual environment:

General Security Requirements

Integration and operation within a robust security environment is necessary
and expected. The security architecture will include one or more of the
following: IDAM (Identity and Access Management) for all system and
applications access, Code scanning, network vulnerability scans, OS,
Database and application patching, malware detection and cleaning,
DDOS prevention, network security gateways (internal and external)
operating at various layers, host and application based tools for
security compliance validation, aggressive security patch application,
tightly controlled software distribution and change control processes
and other state of the art security solutions. The VNF is expected to
function reliably within such an environment and the developer is
expected to understand and accommodate such controls and can expected
to supply responsive interoperability support and testing throughout
the product’s lifecycle.


.. req::
    :id: R-23740
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** implement and enforce the principle of least privilege
    on all protected interfaces.

.. req::
    :id: R-61354
    :target: VNF
    :keyword: MUST

    The VNF **MUST** implement access control list for OA&M
    services (e.g., restricting access to certain ports or applications).

.. req::
    :id: R-92207
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** implement a mechanism for automated and
    frequent "system configuration (automated provisioning / closed loop)"
    auditing.

.. req::
    :id: R-23882
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** be scanned using both network scanning
    and application scanning security tools on all code, including underlying
    OS and related configuration. Scan reports shall be provided. Remediation
    roadmaps shall be made available for any findings.

.. req::
    :id: R-46986
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** have source code scanned using scanning
    tools (e.g., Fortify) and provide reports.

.. req::
    :id: R-99771
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide all code/configuration files in a
    "Locked down" or hardened state or with documented recommendations for
    such hardening. All unnecessary services will be disabled. VNF provider
    default credentials, community strings and other such artifacts will be
    removed or disclosed so that they can be modified or removed during
    provisioning.

.. req::
    :id: R-19768
    :target: VNF
    :keyword: SHOULD
    :updated: casablanca

    The VNF **SHOULD** support Layer 3 VPNs that enable segregation of
    traffic by application (i.e., AVPN, IPSec VPN for Internet routes).

.. req::
    :id: R-33981
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** interoperate with various access control
    mechanisms for the Network Cloud execution environment (e.g.,
    Hypervisors, containers).

.. req::
    :id: R-40813
    :target: VNF
    :keyword: SHOULD
    :updated: casablanca

    The VNF **SHOULD** support the use of virtual trusted platform
    module.

.. req::
    :id: R-56904
    :target: VNF
    :keyword: MUST

    The VNF **MUST** interoperate with the ONAP (SDN) Controller so that
    it can dynamically modify the firewall rules, ACL rules, QoS rules, virtual
    routing and forwarding rules.

.. req::
    :id: R-26586
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** support the ability to work with aliases
    (e.g., gateways, proxies) to protect and encapsulate resources.

.. req::
    :id: R-49956
    :target: VNF
    :keyword: MUST

    The VNF **MUST** pass all access to applications (Bearer,
    signaling and OA&M) through various security tools and platforms from
    ACLs, stateful firewalls and application layer gateways depending on
    manner of deployment. The application is expected to function (and in
    some cases, interwork) with these security tools.

.. req::
    :id: R-69649
    :target: VNF
    :keyword: MUST

    The VNF **MUST** have all vulnerabilities patched as soon
    as possible. Patching shall be controlled via change control process
    with vulnerabilities disclosed along with mitigation recommendations.

.. req::
    :id: R-78010
    :target: VNF
    :keyword: MUST

    The VNF **MUST** use the NCSP's IDAM API for Identification,
    authentication and access control of customer or VNF application users.

.. req::
    :id: R-42681
    :target: VNF
    :keyword: MUST

    The VNF **MUST** use the NCSP's IDAM API or comply with
    the requirements if not using the NCSP's IDAM API, for identification,
    authentication and access control of OA&M and other system level
    functions.

.. req::
    :id: R-68589
    :target: VNF
    :keyword: MUST

    The VNF **MUST**, if not using the NCSP's IDAM API, support
    User-IDs and passwords to uniquely identify the user/application. VNF
    needs to have appropriate connectors to the Identity, Authentication
    and Authorization systems that enables access at OS, Database and
    Application levels as appropriate.

.. req::
    :id: R-98391
    :target: VNF
    :keyword: MUST

    The VNF **MUST**, if not using the NCSP's IDAM API, support
    Role-Based Access Control to permit/limit the user/application to
    performing specific activities.

.. req::
    :id: R-62498
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** support encrypted access protocols, e.g., TLS,
    SSH, SFTP.

.. req::
    :id: R-79107
    :target: VNF
    :keyword: MUST

    The VNF **MUST**, if not using the NCSP's IDAM API, enforce
    a configurable maximum number of Login attempts policy for the users.
    VNF provider must comply with "terminate idle sessions" policy.
    Interactive sessions must be terminated, or a secure, locking screensaver
    must be activated requiring authentication, after a configurable period
    of inactivity. The system-based inactivity timeout for the enterprise
    identity and access management system must also be configurable.

.. req::
    :id: R-35144
    :target: VNF
    :keyword: MUST

    The VNF **MUST**, if not using the NCSP's IDAM API, comply
    with the NCSP's credential management policy.

.. req::
    :id: R-75041
    :target: VNF
    :keyword: MUST

    The VNF **MUST**, if not using the NCSP's IDAM API, expire
    passwords at regular configurable intervals.

.. req::
    :id: R-46908
    :target: VNF
    :keyword: MUST

    The VNF **MUST**, if not using the NCSP's IDAM API, comply
    with "password complexity" policy. When passwords are used, they shall
    be complex and shall at least meet the following password construction
    requirements: (1) be a minimum configurable number of characters in
    length, (2) include 3 of the 4 following types of characters:
    upper-case alphabetic, lower-case alphabetic, numeric, and special,
    (3) not be the same as the UserID with which they are associated or
    other common strings as specified by the environment, (4) not contain
    repeating or sequential characters or numbers, (5) not to use special
    characters that may have command functions, and (6) new passwords must
    not contain sequences of three or more characters from the previous
    password.

.. req::
    :id: R-39342
    :target: VNF
    :keyword: MUST

    The VNF **MUST**, if not using the NCSP's IDAM API, comply
    with "password changes (includes default passwords)" policy. Products
    will support password aging, syntax and other credential management
    practices on a configurable basis.

.. req::
    :id: R-40521
    :target: VNF
    :keyword: MUST

    The VNF **MUST**, if not using the NCSP's IDAM API, support
    use of common third party authentication and authorization tools such
    as TACACS+, RADIUS.

.. req::
    :id: R-41994
    :target: VNF
    :keyword: MUST

    The VNF **MUST**, if not using the NCSP's IDAM API, comply
    with "No Self-Signed Certificates" policy. Self-signed certificates
    must be used for encryption only, using specified and approved
    encryption protocols such as TLS 1.2 or higher or equivalent security
    protocols such as IPSec, AES.

.. req::
    :id: R-23135
    :target: VNF
    :keyword: MUST

    The VNF **MUST**, if not using the NCSP's IDAM API,
    authenticate system to system communications where one system
    accesses the resources of another system, and must never conceal
    individual accountability.

VNF Identity and Access Management Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following security requirements for logging, identity, and access
management need to be met by the solution in a virtual environment:


Identity and Access Management Requirements


.. req::
    :id: R-95105
    :target: VNF
    :keyword: MUST

    The VNF **MUST** host connectors for access to the application layer.

.. req::
    :id: R-45496
    :target: VNF
    :keyword: MUST

    The VNF **MUST** host connectors for access to the OS (Operating System) layer.

.. req::
    :id: R-05470
    :target: VNF
    :keyword: MUST

    The VNF **MUST** host connectors for access to the database layer.

.. req::
    :id: R-99174
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** allow the creation of multiple IDs so that
    individual accountability can be supported.

.. req::
    :id: R-42874
    :target: VNF
    :keyword: MUST

    The VNF **MUST** comply with Least Privilege (no more
    privilege than required to perform job functions) when persons
    or non-person entities access VNFs.

.. req::
    :id: R-71787
    :target: VNF
    :keyword: MUST

    The VNF **MUST** comply with Segregation of Duties (access to a
    single layer and no developer may access production without special
    oversight) when persons or non-person entities access VNFs.

.. req::
    :id: R-86261
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** allow vendor access to VNFs remotely.

.. req::
    :id: R-49945
    :target: VNF
    :keyword: MUST

    The VNF **MUST** authorize VNF provider access through a
    client application API by the client application owner and the resource
    owner of the VNF before provisioning authorization through Role Based
    Access Control (RBAC), Attribute Based Access Control (ABAC), or other
    policy based mechanism.

.. req::
    :id: R-31751
    :target: VNF
    :keyword: MUST

    The VNF **MUST** subject VNF provider access to privilege
    reconciliation tools to prevent access creep and ensure correct
    enforcement of access policies.

.. req::
    :id: R-34552
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for OWASP Top 10.

.. req::
    :id: R-29301
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Password Attacks.

.. req::
    :id: R-72243
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Phishing / SMishing.

.. req::
    :id: R-58998
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Malware (Key Logger).

.. req::
    :id: R-14025
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Session Hijacking.

.. req::
    :id: R-31412
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for XSS / CSRF.

.. req::
    :id: R-51883
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Replay.

.. req::
    :id: R-44032
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Man in the Middle (MITM).

.. req::
    :id: R-58977
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide or support the Identity and Access
    Management (IDAM) based threat detection data for Eavesdropping.

.. req::
    :id: R-24825
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide Context awareness data (device,
    location, time, etc.) and be able to integrate with threat detection system.

.. req::
    :id: R-59391
    :target: VNF
    :keyword: MUST

    The VNF provider **MUST**, where a VNF provider requires
    the assumption of permissions, such as root or administrator, first
    log in under their individual user login ID then switch to the other
    higher level account; or where the individual user login is infeasible,
    must login with an account with admin privileges in a way that
    uniquely identifies the individual performing the function.

.. req::
    :id: R-85028
    :target: VNF
    :keyword: MUST

    The VNF **MUST** authenticate system to system access and
    do not conceal a VNF provider user's individual accountability for
    transactions.

.. req::
    :id: R-80335
    :target: VNF
    :keyword: MUST

    The VNF **MUST** make visible a Warning Notice: A formal
    statement of resource intent, i.e., a warning notice, upon initial
    access to a VNF provider user who accesses private internal networks
    or Company computer resources, e.g., upon initial logon to an internal
    web site, system or application which requires authentication.

.. req::
    :id: R-73541
    :target: VNF
    :keyword: MUST

    The VNF **MUST** use access controls for VNFs and their
    supporting computing systems at all times to restrict access to
    authorized personnel only, e.g., least privilege. These controls
    could include the use of system configuration or access control
    software.

.. req::
    :id: R-64503
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide minimum privileges for initial
    and default settings for new user accounts.

.. req::
    :id: R-86835
    :target: VNF
    :keyword: MUST

    The VNF **MUST** set the default settings for user access
    to sensitive commands and data to deny authorization.

.. req::
    :id: R-77157
    :target: VNF
    :keyword: MUST

    The VNF **MUST** conform to approved request, workflow
    authorization, and authorization provisioning requirements when
    creating privileged users.

.. req::
    :id: R-81147
    :target: VNF
    :keyword: MUST

    The VNF **MUST** have greater restrictions for access and
    execution, such as up to 3 factors of authentication and restricted
    authorization, for commands affecting network services, such as
    commands relating to VNFs.

.. req::
    :id: R-49109
    :target: VNF
    :keyword: MUST

    The VNF **MUST** encrypt TCP/IP--HTTPS (e.g., TLS v1.2)
    transmission of data on internal and external networks.

.. req::
    :id: R-39562
    :target: VNF
    :keyword: MUST

    The VNF **MUST** disable unnecessary or vulnerable cgi-bin programs.

.. req::
    :id: R-15671
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** provide public or unrestricted access
    to any data without the permission of the data owner. All data
    classification and access controls must be followed.

.. req::
    :id: R-89753
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** install or use systems, tools or
    utilities capable of capturing or logging data that was not created
    by them or sent specifically to them in production, without
    authorization of the VNF system owner.

.. req::
    :id: R-19082
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** run security testing tools and
    programs, e.g., password cracker, port scanners, hacking tools
    in production, without authorization of the VNF system owner.

.. req::
    :id: R-19790
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** include authentication credentials
    in security audit logs, even if encrypted.

.. req::
    :id: R-85419
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** use REST APIs exposed to Client
    Applications for the implementation of OAuth 2.0 Authorization
    Code Grant and Client Credentials Grant, as the standard interface
    for a VNF.

.. req::
    :id: R-48080
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** support SCEP (Simple Certificate Enrollment Protocol).

VNF API Security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section covers API security requirements when these are used by the
VNFs. Key security areas covered in API security are Access Control,
Authentication, Passwords, PKI Authentication Alarming, Anomaly
Detection, Lawful Intercept, Monitoring and Logging, Input Validation,
Cryptography, Business continuity, Biometric Authentication,
Identification, Confidentiality and Integrity, and Denial of Service.

The solution in a virtual environment needs to meet the following API
security requirements:


API Requirements


.. req::
    :id: R-37608
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide a mechanism to restrict access based
    on the attributes of the VNF and the attributes of the subject.

.. req::
    :id: R-43884
    :target: VNF
    :keyword: MUST

    The VNF **MUST** integrate with external authentication
    and authorization services (e.g., IDAM).

.. req::
    :id: R-25878
    :target: VNF
    :keyword: MUST

    The VNF **MUST** use certificates issued from publicly
    recognized Certificate Authorities (CA) for the authentication process
    where PKI-based authentication is used.

.. req::
    :id: R-19804
    :target: VNF
    :keyword: MUST

    The VNF **MUST** validate the CA signature on the certificate,
    ensure that the date is within the validity period of the certificate,
    check the Certificate Revocation List (CRL), and recognize the identity
    represented by the certificate where PKI-based authentication is used.

.. req::
    :id: R-47204
    :target: VNF
    :keyword: MUST

    The VNF **MUST** protect the confidentiality and integrity of
    data at rest and in transit from unauthorized access and modification.

.. req::
    :id: R-33488
    :target: VNF
    :keyword: MUST

    The VNF **MUST** protect against all denial of service
    attacks, both volumetric and non-volumetric, or integrate with external
    denial of service protection tools.

.. req::
    :id: R-21652
    :target: VNF
    :keyword: MUST

    The VNF **MUST** implement the following input validation
    control: Check the size (length) of all input. Do not permit an amount
    of input so great that it would cause the VNF to fail. Where the input
    may be a file, the VNF API must enforce a size limit.

.. req::
    :id: R-54930
    :target: VNF
    :keyword: MUST

    The VNF **MUST** implement the following input validation
    control: Do not permit input that contains content or characters
    inappropriate to the input expected by the design. Inappropriate input,
    such as SQL insertions, may cause the system to execute undesirable
    and unauthorized transactions against the database or allow other
    inappropriate access to the internal network.

.. req::
    :id: R-21210
    :target: VNF
    :keyword: MUST

    The VNF **MUST** implement the following input validation
    control: Validate that any input file has a correct and valid
    Multipurpose Internet Mail Extensions (MIME) type. Input files
    should be tested for spoofed MIME types.

.. req::
    :id: R-23772
    :target: VNF
    :keyword: MUST

    The VNF **MUST** validate input at all layers implementing VNF APIs.

.. req::
    :id: R-87135
    :target: VNF
    :keyword: MUST

    The VNF **MUST** comply with NIST standards and industry
    best practices for all implementations of cryptography.

.. req::
    :id: R-02137
    :target: VNF
    :keyword: MUST

    The VNF **MUST** implement all monitoring and logging as
    described in the Security Analytics section.

.. req::
    :id: R-15659
    :target: VNF
    :keyword: MUST

    The VNF **MUST** restrict changing the criticality level of
    a system security alarm to administrator(s).

.. req::
    :id: R-19367
    :target: VNF
    :keyword: MUST

    The VNF **MUST** monitor API invocation patterns to detect
    anomalous access patterns that may represent fraudulent access or
    other types of attacks, or integrate with tools that implement anomaly
    and abuse detection.

.. req::
    :id: R-78066
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support requests for information from law
    enforcement and government agencies.


VNF Security Analytics Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


.. req::
    :id: R-48470
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support Real-time detection and
    notification of security events.

.. req::
    :id: R-22286
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support Integration functionality via
    API/Syslog/SNMP to other functional modules in the network (e.g.,
    PCRF, PCEF) that enable dynamic security control by blocking the
    malicious traffic or malicious end users.

.. req::
    :id: R-32636
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support API-based monitoring to take care of
    the scenarios where the control interfaces are not exposed, or are
    optimized and proprietary in nature.

.. req::
    :id: R-61648
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support event logging, formats, and delivery
    tools to provide the required degree of event data to ONAP.

.. req::
    :id: R-22367
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support detection of malformed packets due to
    software misconfiguration or software vulnerability.

.. req::
    :id: R-31961
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support integrated DPI/monitoring functionality
    as part of VNFs (e.g., PGW, MME).

.. req::
    :id: R-20912
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support alternative monitoring capabilities
    when VNFs do not expose data or control traffic or use proprietary and
    optimized protocols for inter VNF communication.

.. req::
    :id: R-73223
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support proactive monitoring to detect and
    report the attacks on resources so that the VNFs and associated VMs can
    be isolated, such as detection techniques for resource exhaustion, namely
    OS resource attacks, CPU attacks, consumption of kernel memory, local
    storage attacks.

.. req::
    :id: R-58370
    :target: VNF
    :keyword: MUST

    The VNF **MUST** coexist and operate normally with commercial
    anti-virus software which shall produce alarms every time when there is a
    security incident.

.. req::
    :id: R-56920
    :target: VNF
    :keyword: MUST

    The VNF **MUST** protect all security audit logs (including
    API, OS and application-generated logs), security audit software, data,
    and associated documentation from modification, or unauthorized viewing,
    by standard OS access control mechanisms, by sending to a remote system,
    or by encryption.

.. req::
    :id: R-54520
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log successful and unsuccessful login attempts.

.. req::
    :id: R-55478
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log logoffs.

.. req::
    :id: R-08598
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log successful and unsuccessful changes to a privilege level.

.. req::
    :id: R-13344
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log starting and stopping of security
    logging.

.. req::
    :id: R-07617
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log creating, removing, or changing the
    inherent privilege level of users.

.. req::
    :id: R-94525
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log connections to a network listener of the
    resource.

.. req::
    :id: R-31614
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log the field "event type" in the security audit
    logs.

.. req::
    :id: R-97445
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log the field "date/time" in the security audit
    logs.

.. req::
    :id: R-25547
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log the field "protocol" in the security audit logs.

.. req::
    :id: R-06413
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log the field "service or program used for access"
    in the security audit logs.

.. req::
    :id: R-15325
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log the field "success/failure" in the
    security audit logs.

.. req::
    :id: R-89474
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log the field "Login ID" in the security audit logs.

.. req::
    :id: R-04982
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** include an authentication credential,
    e.g., password, in the security audit logs, even if encrypted.

.. req::
    :id: R-63330
    :target: VNF
    :keyword: MUST

    The VNF **MUST** detect when the security audit log storage
    medium is approaching capacity (configurable) and issue an alarm via
    SMS or equivalent as to allow time for proper actions to be taken to
    pre-empt loss of audit data.

.. req::
    :id: R-41252
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support the capability of online storage of
    security audit logs.

.. req::
    :id: R-41825
    :target: VNF
    :keyword: MUST

    The VNF **MUST** activate security alarms automatically when
    the following event is detected: configurable number of consecutive
    unsuccessful login attempts.

.. req::
    :id: R-43332
    :target: VNF
    :keyword: MUST

    The VNF **MUST** activate security alarms automatically when
    the following event is detected: successful modification of critical
    system or application files.

.. req::
    :id: R-74958
    :target: VNF
    :keyword: MUST

    The VNF **MUST** activate security alarms automatically when
    the following event is detected: unsuccessful attempts to gain permissions
    or assume the identity of another user.

.. req::
    :id: R-15884
    :target: VNF
    :keyword: MUST

    The VNF **MUST** include the field "date" in the Security alarms
    (where applicable and technically feasible).

.. req::
    :id: R-23957
    :target: VNF
    :keyword: MUST

    The VNF **MUST** include the field "time" in the Security alarms
    (where applicable and technically feasible).

.. req::
    :id: R-71842
    :target: VNF
    :keyword: MUST

    The VNF **MUST** include the field "service or program used for
    access" in the Security alarms (where applicable and technically feasible).

.. req::
    :id: R-57617
    :target: VNF
    :keyword: MUST

    The VNF **MUST** include the field "success/failure" in the
    Security alarms (where applicable and technically feasible).

.. req::
    :id: R-99730
    :target: VNF
    :keyword: MUST

    The VNF **MUST** include the field "Login ID" in the Security
    alarms (where applicable and technically feasible).

.. req::
    :id: R-29705
    :target: VNF
    :keyword: MUST

    The VNF **MUST** restrict changing the criticality level of a
    system security alarm to administrator(s).

.. req::
    :id: R-13627
    :target: VNF
    :keyword: MUST

    The VNF **MUST** monitor API invocation patterns to detect
    anomalous access patterns that may represent fraudulent access or other
    types of attacks, or integrate with tools that implement anomaly and
    abuse detection.

.. req::
    :id: R-21819
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support requests for information from law
    enforcement and government agencies.

.. req::
    :id: R-56786
    :target: VNF
    :keyword: MUST

    The VNF **MUST** implement "Closed Loop" automatic implementation
    (without human intervention) for Known Threats with detection rate in low
    false positives.

.. req::
    :id: R-25094
    :target: VNF
    :keyword: MUST

    The VNF **MUST** perform data capture for security functions.

.. req::
    :id: R-04492
    :target: VNF
    :keyword: MUST

    The VNF **MUST** generate security audit logs that must be sent
    to Security Analytics Tools for analysis.

.. req::
    :id: R-19219
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide audit logs that include user ID, dates,
    times for log-on and log-off, and terminal location at minimum.

.. req::
    :id: R-30932
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide security audit logs including records
    of successful and rejected system access data and other resource access
    attempts.

.. req::
    :id: R-54816
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support the storage of security audit logs
    for agreed period of time for forensic analysis.

.. req::
    :id: R-57271
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide the capability of generating security
    audit logs by interacting with the operating system (OS) as appropriate.

.. req::
    :id: R-84160
    :target: VNF
    :keyword: MUST

    The VNF **MUST** have security logging for VNFs and their
    OSs be active from initialization. Audit logging includes automatic
    routines to maintain activity records and cleanup programs to ensure
    the integrity of the audit/logging systems.

VNF Data Protection Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section covers VNF data protection requirements that are mostly
applicable to security monitoring.


Data Protection Requirements

.. req::
    :id: R-58964
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** provide the capability to restrict read
    and write access to data handled by the VNF.

.. req::
    :id: R-83227
    :target: VNF
    :keyword: MUST

    The VNF **MUST** Provide the capability to encrypt data in
    transit on a physical or virtual network.

.. req::
    :id: R-32641
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** provide the capability to encrypt data on
    non-volatile memory.Non-volative memory is storage that is
    capable of retaining data without electrical power, e.g.
    Complementary metal–oxide–semiconductor (CMOS) or hard drives.

.. req::
    :id: R-13151
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** disable the paging of the data requiring
    encryption, if possible, where the encryption of non-transient data is
    required on a device for which the operating system performs paging to
    virtual memory. If not possible to disable the paging of the data
    requiring encryption, the virtual memory should be encrypted.

.. req::
    :id: R-93860
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide the capability to integrate with an
    external encryption service.

.. req::
    :id: R-73067
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** use NIST and industry standard cryptographic
    algorithms and standard modes of operations when implementing
    cryptography.

.. req::
    :id: R-12467
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** use the SHA, DSS, MD5, SHA-1 and
    Skipjack algorithms or other compromised encryption.

.. req::
    :id: R-02170
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** use, whenever possible, standard implementations
    of security applications, protocols, and formats, e.g., S/MIME, TLS, SSH,
    IPSec, X.509 digital certificates for cryptographic implementations.
    These implementations must be purchased from reputable vendors or obtained
    from reputable open source communities and must not be developed in-house.

.. req::
    :id: R-70933
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** provide the ability to migrate to newer
    versions of cryptographic algorithms and protocols with minimal impact.

.. req::
    :id: R-44723
    :target: VNF
    :keyword: MUST

    The VNF **MUST** use symmetric keys of at least 112 bits in length.

.. req::
    :id: R-25401
    :target: VNF
    :keyword: MUST

    The VNF **MUST** use asymmetric keys of at least 2048 bits in length.

.. req::
    :id: R-95864
    :target: VNF
    :keyword: MUST

    The VNF **MUST** use commercial tools that comply with X.509
    standards and produce x.509 compliant keys for public/private key generation.

.. req::
    :id: R-12110
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** use keys generated or derived from
    predictable functions or values, e.g., values considered predictable
    include user identity information, time of day, stored/transmitted data.

.. req::
    :id: R-52060
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide the capability to configure encryption
    algorithms or devices so that they comply with the laws of the jurisdiction
    in which there are plans to use data encryption.

.. req::
    :id: R-69610
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** provide the capability of using X.509 certificates
    issued by an external Certificate Authority.

.. req::
    :id: R-83500
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide the capability of allowing certificate
    renewal and revocation.

.. req::
    :id: R-29977
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide the capability of testing the validity
    of a digital certificate by validating the CA signature on the certificate.

.. req::
    :id: R-24359
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide the capability of testing the validity
    of a digital certificate by validating the date the certificate is being
    used is within the validity period for the certificate.

.. req::
    :id: R-39604
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide the capability of testing the
    validity of a digital certificate by checking the Certificate Revocation
    List (CRL) for the certificates of that type to ensure that the
    certificate has not been revoked.

.. req::
    :id: R-75343
    :target: VNF
    :keyword: MUST

    The VNF **MUST** provide the capability of testing the
    validity of a digital certificate by recognizing the identity represented
    by the certificate - the "distinguished name".

