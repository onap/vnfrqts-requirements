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


Scope
=====

- The audience for this document are VNF or PNF providers, NCSPs and other
  interested 3rd parties who need to know the design, build and lifecycle
  management requirements for VNFs or PNFs to be compliant with ONAP.
- These requirements are strictly from a standpoint of what the VNF or PNF
  developer needs to know to operate and be compliant with ONAP.
- Requirements that are not applicable to VNF or PNF providers such as those
  that applicable to service providers are not included in this document.
- These requirements are applicable to the current release of ONAP.
- Scope of the ONAP versions/release and future functionality
- The VNF Requirements should include support for the functionality of the
  ONAP E-E use cases.
- These requirements apply to VNFs or PNFs at both ONAP Design-Time and ONAP
  Run-Time.
- Network Service Descriptions are beyond the scope of these requirements.

References
-----------------------

This section contains a list of normative and informative references along
with information on acquiring the identified references.  Normative references
are required to be implemented by this document. Informative references are
for informational purposes only.

Glossary
-----------------------

.. glossary::

    ACL
        Access Control List

    ACME
        Automated Certificate Management

    API
        Application Programming Interface

    BGP
        Border Gateway Protocol

    CA
        Certificate Authority

    CCL
        Commerce Control List

    CLLI
        Common Language Location Identification

    CMOS
        Complementary metal-oxide-semiconductor

    CMP
        Certificate Management Protocol

    CRL
        Certificate Revocation List

    CSAR
        Cloud Service Archive

    DBaaS
        Database as a Service

    DDOS
        Distributer Denial-of-Service

    DNS
        Domain Name System

    DPDK
        Data Plane Development Kit

    DPI
        Deep Packet Inspection

    DPM
        Data Position Measurement

    DSS
        Digital Signature Services

    ECCN
        Export Control Classification Number

    EMS
        Element Management Systems

    EVC
        Ethernet Virtual Connection

    FIPS
        Federal Information Processing Standards

    FQDN
        Fully Qualified Domain Name

    FTPES
        File Transfer Protocol Secure

    GPB
        Google Protocol Buffers

    GUI
        Graphical User Interface

    GVNFM
        Generic Virtualized Network Function Manager

    HSM
        Hardware Security Module

    IDAM
        Identity and Access Management

    IPSec
        IP Security 

    JMS
        Java Message Service

    JSON
        JavaScript Object Notation

    KPI
        Key Performance Indicator

    LCM
        Life Cycle Management

    LCP
        Link Control Protocol

    LDAP
        Lightweight Directory Access Protocol

    LTE
        Long-Term Evolution 

    MD5
        Message-Digest Algorithm

    MIME
        Multipurpose Internet Mail Extensions

    MTTI
        Mean Time to Identify

    MTTR
        Mean Time to Repair

    NCSP
        Network Cloud Service Providers

    NFS
        Network File System

    NFV
        Network Functions Virtualization

    NIC
        Network Interface Controller

    NIST
        National Institute of Standards and Technology

    NTP
        Network Time Protocol

    OA&M
        Operations, administration and management

    OAuth
        Open Authorization

    OID
        Object Identifier

    OPNFV
        Open Platform for Network Functions Virtualization

    OWASP
        Open Web Application Security Project 

    PCEF
        Policy and Charging Enforcement Function

    PCRF
        Policy and Charging Rules Function

    PKI
        Public Key Infrastructure

    PM
        Performance Monitoring

    PNF
        Physical Network Function

    PnP
        Plug and Play

    QoS
        Quality of Service

    RAN
        Radio Access Network

    RBAC
        Role-Based Access Control

    RTPM
        Real Time Performance Monitoring

    RFC
        Remote Function Call

    RFP
        Request For Proposal

    RPC
        Remote Procedure Call

    SAML
        Security Assertion Markup Language

    SCEP
        Simple Certificate Enrollment Protocol 

    SDN
        Software-Defined Networking

    SFTP
        SSH File Transfer Protocol

    SHA
        Secure Hash Algorithm

    SLA
        Service Level Agreement 

    SNMP
        Simple Network Management Protocol

    SP
        Service Provider

    SPI
        Sensitive Personal Information

    SR-IOV
        Single-Root Input/Output Virtualization

    SSL
        Secure Sockets Layer

    SSH
        Secure Shell

    TACACS
        Terminal Access Controller Access Control System

    TCA
        Threshold Crossing Alert

    TLS
        Transport Layer Security 

    TOSCA
        Topology and Orchestration Specification for Cloud Applications

    TPM
        Trusted Platform Module

    UUID
        Universally Unique Identifier

    VDU
        Virtualization Deployment Unit

    VES
        VNF Event Streaming

    VLAN
        Virtual LAN

    VM
        Virtual Machine

    VNF
        Virtual Network Function

    VNFC
        Virtual Network Function Component

    VNF-D
        Virtual Network Function Descriptor

    VPN
        Virtual Private Network

    XML
        eXtensible Markup Language

    YAML
        YAML Ain't Markup Languag

    YANG
        Yet Another Next Generation

    NFVI
        Network Function Virtualization Infrastructure

    VNFC
        Virtualized Network Function Components

    MANO
        Management And Network Orchestration

    VNFM
        Virtualized Network Function Manager

    BUM
        Broadcast, Unknown-Unicast and Multicast traffic



Normative References
^^^^^^^^^^^^^^^^^^^^^^^
+---------------+-----------------------------------------------------+
| Reference     | Description                                         |
+===============+=====================================================+
| [RFC 2119]    | IETF RFC2119, Key words for use in RFCs to Indicate |
|               | Requirement Levels, S. Bradner, March 1997.         |
+---------------+-----------------------------------------------------+

Informative References
^^^^^^^^^^^^^^^^^^^^^^^^
+---------------+-----------------------------------------------------+
| Reference     | Description                                         |
+===============+=====================================================+
|               |                                                     |
+---------------+-----------------------------------------------------+

Reference Acquisition
^^^^^^^^^^^^^^^^^^^^^^^
IETF Specifications:

- Internet Engineering Task Force (IETF) Secretariat, 48377 Fremont Blvd.,
  Suite 117, Fremont, California 94538, USA; Phone: +1-510-492-4080,
  Fax: +1-510-492-4001.

Submitting Feedback
------------------------------------
Please refer to the `VNF Requirements - How to Contribute <https://wiki.onap.org/display/DW/VNFRQTS+How+to+Contribute>`__
guide for instructions on how to create issues or contribute changes to the
VNF Requirements project.