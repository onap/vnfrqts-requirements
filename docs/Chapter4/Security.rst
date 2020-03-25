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
the product's lifecycle.


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
    :updated: casablanca

    The VNF **MUST** provide a mechanism (e.g., access control list) to
    permit and/or restrict access to services on the VNF by source,
    destination, protocol, and/or port.

.. req::
    :id: R-92207
    :target: VNF
    :keyword: SHOULD
    :updated: casablanca

    The VNF **SHOULD** provide a mechanism that enables the operators to
    perform automated system configuration auditing at configurable time
    intervals.

.. req::
    :id: R-46986
    :target: VNF
    :keyword: MUST
    :updated: frankfurt

    The VNF provider **MUST** follow GSMA vendor practices and SEI CERT Coding
    Standards when developing the VNF in order to minimize the risk of
    vulnerabilities. See GSMA NESAS Network Equipment Security Assurance Scheme –
    Development and Lifecycle Security Requirements Version 1.0 (https://www.gsma.com/
    security/wp-content/uploads/2019/11/FS.16-NESAS-Development-and-Lifecycle-Security-
    Requirements-v1.0.pdf) and SEI CERT Coding Standards (https://wiki.sei.cmu.edu/
    confluence/display/seccode/SEI+CERT+Coding+Standards).

.. req::
    :id: R-99771
    :target: VNF
    :keyword: MUST
    :updated: dublin

    The VNF **MUST** have all code (e.g., QCOW2) and configuration files
    (e.g., HEAT template, Ansible playbook, script) hardened, or with
    documented recommended configurations for hardening and interfaces that
    allow the Operator to harden the VNF. Actions taken to harden a system
    include disabling all unnecessary services, and changing default values
    such as default credentials and community strings.

.. req::
    :id: R-19768
    :target: VNF
    :keyword: SHOULD
    :updated: frankfurt

    The VNF **SHOULD** support the separation of (1) signaling and payload traffic
    (i.e., customer facing traffic), (2) operations, administration and management
    traffic, and (3) internal VNF traffic (i.e., east-west traffic such as storage
    access) using technologies such as VPN and VLAN.

.. req::
    :id: R-56904
    :target: VNF
    :keyword: MUST
    :updated: frankfurt

    The VNF **MUST** interoperate with the ONAP (SDN) Controller so that
    it can dynamically modify the firewall rules, ACL rules, QoS rules, virtual
    routing and forwarding rules. This does not preclude the VNF providing other
    interfaces for modifying rules.

.. req::
    :id: R-69649
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF Provider **MUST** have patches available for vulnerabilities
    in the VNF as soon as possible. Patching shall be controlled via change
    control process with vulnerabilities disclosed along with
    mitigation recommendations.

.. req::
    :id: R-62498
    :target: VNF
    :keyword: MUST
    :updated: frankfurt

    The VNF **MUST** support only encrypted access protocols, e.g., TLS,
    SSH, SFTP.

.. req::
   :id: R-872986
   :target: VNF
   :keyword: MUST
   :introduced: casablanca

   The VNF **MUST** store Authentication Credentials used to authenticate to
   other systems encrypted except where there is a technical need to store
   the password unencrypted in which case it must be protected using other
   security techniques that include the use of file and directory permissions.
   Ideally, credentials SHOULD rely on a HW Root of Trust, such as a
   TPM or HSM.

.. req::
    :id: R-80335
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    For all GUI and command-line interfaces, the VNF **MUST** provide the
    ability to present a warning notice that is set by the Operator. A warning
    notice is a formal statement of resource intent presented to everyone
    who accesses the system.

.. req::
    :id: R-19082
    :target: VNF
    :keyword: MUST
    :updated: frankfurt

    The VNF **MUST** not contain undocumented functionality.

.. req::
    :id: R-21819
    :target: VNF
    :keyword: MUST
    :updated: el alto

    VNFs that are subject to regulatory requirements **MUST** provide
    functionality that enables the Operator to comply with ETSI TC LI
    requirements, and, optionally, other relevant national equivalents.

.. req::
    :id: R-86261
    :target: VNF
    :keyword: MUST
    :updated: frankfurt

    The VNF **MUST** be able to authenticate and authorize all remote access.

.. req::
   :id: R-638682
   :target: VNF
   :keyword: MUST
   :introduced: casablanca
   :validation_mode: in_service

   The VNF **MUST** log any security event required by the VNF Requirements to
   Syslog using LOG_AUTHPRIV for any event that would contain sensitive
   information and LOG_AUTH for all other relevant events.

.. req::
   :id: R-756950
   :target: VNF
   :keyword: MUST
   :introduced: casablanca

   The VNF **MUST** be operable without the use of Network File System (NFS).

.. req::
   :id: R-240760
   :target: VNF
   :keyword: MUST NOT
   :introduced: casablanca

   The VNF **MUST NOT** contain any backdoors.

.. req::
   :id: R-256267
   :target: VNF
   :keyword: MUST
   :introduced: casablanca

   If SNMP is utilized, the VNF **MUST** support at least SNMPv3 with
   message authentication.

.. req::
   :id: R-258686
   :target: VNF
   :keyword: SHOULD NOT
   :introduced: casablanca
   :updated: el alto

   The VNF application processes **SHOULD NOT** run as root. If a VNF
   application process must run as root, the technical reason must
   be documented.

.. req::
   :id: R-118669
   :target: VNF
   :keyword: MUST
   :introduced: casablanca

   Login access (e.g., shell access) to the operating system layer, whether
   interactive or as part of an automated process, **MUST** be through an
   encrypted protocol such as SSH or TLS.

.. req::
   :id: R-842258
   :target: VNF
   :keyword: MUST
   :introduced: casablanca
   :updated: frankfurt

   The VNF **MUST** include a configuration (e.g. a heat template or CSAR package)
   that specifies the targeted parameters (e.g. a limited set of ports)
   over which the VNF will communicate; including internal, external and
   management communication.

.. req::
   :id: R-353637
   :target: VNF
   :keyword: SHOULD
   :introduced: frankfurt

   Containerized components of VNFs **SHOULD** follow the recommendations for
   Container Base Images and Build File Configuration in the latest available version
   of the CIS Docker Community Edition Benchmarks to ensure that containerized VNFs
   are secure. All non-compliances with the benchmarks MUST be documented.

.. req::
   :id: R-381623
   :target: VNF
   :keyword: SHOULD
   :introduced: frankfurt

   Containerized components of VNFs **SHOULD** execute in a Docker run-time environment
   that follows the Container Runtime Configuration in the latest available version
   of the CIS Docker Community Edition Benchmarks to ensure that containerized VNFs
   are secure. All non-compliances with the benchmarks MUST be documented.

VNF Identity and Access Management Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following security requirements for logging, identity, and access
management need to be met by the solution in a virtual environment:


Identity and Access Management Requirements

.. req::
    :id: R-99174
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST**, if not integrated with the Operator's Identity and
    Access Management system, support the creation of multiple IDs so that
    individual accountability can be supported.

.. req::
    :id: R-42874
    :target: VNF
    :keyword: MUST
    :updated: frankfurt

    The VNF **MUST** allow the Operator to restrict access to protected
    resources based on the assigned permissions associated with an ID in
    order to support Least Privilege (no more privilege than required to
    perform job functions).

.. req::
    :id: R-358699
    :target: VNF
    :keyword: MUST
    :introduced: frankfurt

    The VNF **MUST** support at least the following roles: system administrator,
    application administrator, network function O&M.

.. req::
    :id: R-373737
    :target: VNF
    :keyword: MUST
    :introduced: frankfurt

    The VNF **MUST**, if not integrated with the operator's IAM system, provide
    a mechanism for assigning roles and/or permissions to an identity.

.. req::
    :id: R-59391
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca

    The VNF **MUST NOT** allow the assumption of the permissions of another
    account to mask individual accountability. For example, use SUDO when a
    user requires elevated permissions such as root or admin.

.. req::
    :id: R-86835
    :target: VNF
    :keyword: MUST
    :updated: frankfurt

    The VNF **MUST** set the default settings for user access
    to deny authorization, except for a super user type of account.

.. req::
    :id: R-81147
    :target: VNF
    :keyword: MUST
    :updated: frankfurt

    The VNF **MUST**, if not integrated with the Operator’s Identity and
    Access Management system, support multifactor authentication on all
    protected interfaces exposed by the VNF for use by human users.

.. req::
    :id: R-39562
    :target: VNF
    :keyword: MUST

    The VNF **MUST** disable unnecessary or vulnerable cgi-bin programs.

.. req::
    :id: R-75041
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST**, if not integrated with the Operator's Identity and
    Access Management system, support configurable password expiration.

.. req::
    :id: R-46908
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST**, if not integrated with the Operator's Identity and
    Access Management system, comply with "password complexity" policy. When
    passwords are used, they shall be complex and shall at least meet the
    following password construction requirements: (1) be a minimum configurable
    number of characters in length, (2) include 3 of the 4 following types of
    characters: upper-case alphabetic, lower-case alphabetic, numeric, and
    special, (3) not be the same as the UserID with which they are associated
    or other common strings as specified by the environment, (4) not contain
    repeating or sequential characters or numbers, (5) not to use special
    characters that may have command functions, and (6) new passwords must
    not contain sequences of three or more characters from the previous
    password.

.. req::
   :id: R-844011
   :target: VNF
   :keyword: MUST
   :introduced: casablanca
   :updated: frankfurt

   The VNF **MUST** not store authentication credentials to itself in clear
   text or any reversible form and must use salting.

.. req::
    :id: R-79107
    :target: VNF
    :keyword: MUST
    :updated: frankfurt

    The VNF **MUST**, if not integrated with the Operator’s Identity
    and Access Management system, support the ability to lock out the
    userID after a configurable number of consecutive unsuccessful
    authentication attempts using the same userID. The locking mechanism
    must be reversible by an administrator and should be reversible after
    a configurable time period.

.. req::
    :id: R-23135
    :target: VNF
    :keyword: MUST
    :updated: frankfurt

    The VNF **MUST**, if not integrated with the Operator's identity and
    access management system, authenticate all access to protected resources.

.. req::
    :id: R-78010
    :target: VNF
    :keyword: MUST
    :updated: frankfurt

    The VNF **MUST** support LDAP in order to integrate with an external identity
    and access manage system. It MAY support other identity and access management
    protocols.

.. req::
   :id: R-814377
   :target: VNF
   :keyword: MUST
   :introduced: casablanca
   :updated: frankfurt

   The VNF **MUST** have the capability of allowing the Operator to create,
   manage, and automatically provision user accounts using one of the protocols
   specified in Chapter 7.

.. req::
   :id: R-931076
   :target: VNF
   :keyword: MUST
   :introduced: casablanca
   :updated: frankfurt

   The VNF **MUST** support account names that contain at least A-Z, a-z,
   and 0-9 character sets and be at least 6 characters in length.

.. req::
   :id: R-581188
   :target: VNF
   :keyword: MUST NOT
   :introduced: casablanca
   :updated: frankfurt

   The VNF **MUST NOT** identify the reason for a failed authentication,
   only that the authentication failed.

.. req::
   :id: R-479386
   :target: VNF
   :keyword: MUST
   :introduced: casablanca
   :updated: frankfurt

   The VNF **MUST** provide the capability of setting a configurable message
   to be displayed after successful login. It MAY provide a list of supported
   character sets.

.. req::
   :id: R-231402
   :target: VNF
   :keyword: MUST
   :introduced: casablanca
   :updated: frankfurt

   The VNF **MUST** provide a means to explicitly logout, thus ending that session.

.. req::
   :id: R-251639
   :target: VNF
   :keyword: MUST
   :introduced: frankfurt

   The VNF **MUST** provide explicit confirmation of a session termination
   such as a message, new page, or rerouting to a login page.

.. req::
   :id: R-45719
   :target: VNF
   :keyword: MUST
   :introduced: casablanca
   :updated: frankfurt

   The VNF **MUST**, if not integrated with the Operator's Identity and Access
   Management system, enforce a configurable "terminate idle sessions"
   policy by terminating the session after a configurable period of inactivity.


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
    :id: R-43884
    :target: VNF
    :keyword: SHOULD
    :updated: casablanca

    The VNF **SHOULD** integrate with the Operator's authentication and
    authorization services (e.g., IDAM).

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
    :updated: casablanca

    The VNF **MUST** implement the following input validation controls:
    Do not permit input that contains content or characters inappropriate
    to the input expected by the design. Inappropriate input, such as
    SQL expressions, may cause the system to execute undesirable and
    unauthorized transactions against the database or allow other
    inappropriate access to the internal network (injection attacks).

.. req::
    :id: R-21210
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** implement the following input validation control
    on APIs: Validate that any input file has a correct and valid
    Multipurpose Internet Mail Extensions (MIME) type. Input files
    should be tested for spoofed MIME types.

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
    :id: R-32636
    :target: VNF
    :keyword: MUST

    The VNF **MUST** support API-based monitoring to take care of
    the scenarios where the control interfaces are not exposed, or are
    optimized and proprietary in nature.

.. req::
    :id: R-22367
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** support detection of malformed packets due to software
    misconfiguration or software vulnerability, and generate an error to the
    syslog console facility.

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
    :keyword: SHOULD
    :updated: casablanca

    The VNF **SHOULD** operate with anti-virus software which produces alarms
    every time a virus is detected.

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
    :updated: casablanca

    The VNF **MUST** log successful and unsuccessful authentication
    attempts, e.g., authentication associated with a transaction,
    authentication to create a session, authentication to assume elevated
    privilege.

.. req::
    :id: R-55478
    :target: VNF
    :keyword: MUST

    The VNF **MUST** log logoffs.

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
    :updated: casablanca

    The VNF **MUST** log success and unsuccessful creation, removal, or
    change to the inherent privilege level of users.

.. req::
    :id: R-94525
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** log connections to the network listeners of the
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
    :updated: casablanca

    The VNF **MUST** detect when its security audit log storage
    medium is approaching capacity (configurable) and issue an alarm.

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
    :updated: casablanca

    The VNF **MUST** activate security alarms automatically when
    a configurable number of consecutive unsuccessful login attempts
    is reached.

.. req::
    :id: R-43332
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** activate security alarms automatically when
    it detects the successful modification of a critical system or
    application file.

.. req::
    :id: R-74958
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** activate security alarms automatically when
    it detects an unsuccessful attempt to gain permissions
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
    :updated: casablanca

    The VNF **MUST** restrict changing the criticality level of a
    system security alarm to users with administrative privileges.

.. req::
    :id: R-13627
    :target: VNF
    :keyword: MUST

    The VNF **MUST** monitor API invocation patterns to detect
    anomalous access patterns that may represent fraudulent access or other
    types of attacks, or integrate with tools that implement anomaly and
    abuse detection.

.. req::
    :id: R-04492
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** generate security audit logs that can be sent
    to Security Analytics Tools for analysis.

.. req::
    :id: R-30932
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** log successful and unsuccessful access to VNF
    resources, including data.

.. req::
    :id: R-54816
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** support the storage of security audit logs for a
    configurable period of time.

.. req::
    :id: R-84160
    :target: VNF
    :keyword: MUST

    The VNF **MUST** have security logging for VNFs and their
    OSs be active from initialization. Audit logging includes automatic
    routines to maintain activity records and cleanup programs to ensure
    the integrity of the audit/logging systems.

.. req::
    :id: R-34552
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** be implemented so that it is not vulnerable to OWASP
    Top 10 web application security risks.

.. req::
    :id: R-33488
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** protect against all denial of service
    attacks, both volumetric and non-volumetric, or integrate with external
    denial of service protection tools.

.. req::
   :id: R-629534
   :target: VNF
   :keyword: MUST
   :introduced: casablanca

   The VNF **MUST** be capable of automatically synchronizing the system clock
   daily with the Operator's trusted time source, to assure accurate time
   reporting in log files. It is recommended that Coordinated Universal Time
   (UTC) be used where possible, so as to eliminate ambiguity owing to daylight
   savings time.

.. req::
   :id: R-303569
   :target: VNF
   :keyword: MUST
   :introduced: casablanca

   The VNF **MUST** log the Source IP address in the security audit logs.

.. req::
   :id: R-703767
   :target: VNF
   :keyword: MUST
   :introduced: casablanca

   The VNF **MUST** have the capability to securely transmit the security logs
   and security events to a remote system before they are purged from the
   system.

.. req::
   :id: R-465236
   :target: VNF
   :keyword: SHOULD
   :introduced: casablanca

   The VNF **SHOULD** provide the capability of maintaining the integrity of
   its static files using a cryptographic method.

.. req::
   :id: R-859208
   :target: VNF
   :keyword: MUST
   :introduced: casablanca

   The VNF **MUST** log automated remote activities performed with
   elevated privileges.

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
    Complementary metal-oxide-semiconductor (CMOS) or hard drives.

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
    :updated: casablanca

    The VNF **MUST NOT** use compromised encryption algorithms.
    For example, SHA, DSS, MD5, SHA-1 and Skipjack algorithms.
    Acceptable algorithms can be found in the NIST FIPS publications
    (https://csrc.nist.gov/publications/fips) and in the
    NIST Special Publications (https://csrc.nist.gov/publications/sp).

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
    :id: R-95864
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** support digital certificates that comply with X.509
    standards.

.. req::
    :id: R-12110
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** use keys generated or derived from
    predictable functions or values, e.g., values considered predictable
    include user identity information, time of day, stored/transmitted data.

.. req::
    :id: R-69610
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** provide the capability of using X.509 certificates
    issued by an external Certificate Authority.

.. req::
    :id: R-47204
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** be capable of protecting the confidentiality and integrity
    of data at rest and in transit from unauthorized access and modification.


VNF Cryptography Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section covers VNF cryptography requirements that are mostly
applicable to encryption or protocol meethods.

.. req::
    :id: R-48080
    :target: VNF
    :keyword: SHOULD
    :updated: casablanca

    The VNF **SHOULD** support an automated certificate management protocol
    such as CMPv2, Simple Certificate Enrollment Protocol (SCEP) or
    Automated Certificate Management Environment (ACME).

.. req::
    :id: R-93860
    :target: VNF
    :keyword: SHOULD
    :updated: casablanca

    The VNF **SHOULD** provide the capability to integrate with an
    external encryption service.

.. req::
    :id: R-44723
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** use symmetric keys of at least 112 bits in length.

.. req::
    :id: R-25401
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** use asymmetric keys of at least 2048 bits in length.

.. req::
    :id: R-52060
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** provide the capability to configure encryption
    algorithms or devices so that they comply with the laws of the jurisdiction
    in which there are plans to use data encryption.

.. req::
    :id: R-83500
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** provide the capability of allowing certificate
    renewal and revocation.

.. req::
    :id: R-29977
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** provide the capability of testing the validity
    of a digital certificate by validating the CA signature on the certificate.

.. req::
    :id: R-24359
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** provide the capability of testing the validity
    of a digital certificate by validating the date the certificate is being
    used is within the validity period for the certificate.

.. req::
    :id: R-39604
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** provide the capability of testing the
    validity of a digital certificate by checking the Certificate Revocation
    List (CRL) for the certificates of that type to ensure that the
    certificate has not been revoked.

.. req::
    :id: R-75343
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** provide the capability of testing the
    validity of a digital certificate by recognizing the identity represented
    by the certificate - the "distinguished name".

.. req::
    :id: R-49109
    :target: VNF or PNF
    :keyword: MUST
    :updated: el alto

    The VNF or PNF **MUST** support HTTPS using TLS v1.2 or higher
    with strong cryptographic ciphers.

.. req::
    :id: R-41994
    :target: VNF
    :keyword: MUST
    :updated: casablanca

    The VNF **MUST** support the use of X.509 certificates issued from any
    Certificate Authority (CA) that is compliant with RFC5280, e.g., a public
    CA such as DigiCert or Let's Encrypt, or an RFC5280  compliant Operator
    CA.

    Note: The VNF provider cannot require the use of self-signed certificates
    in an Operator's run time environment.
