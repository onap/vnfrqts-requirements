**5. VNF Modeling Requirements**
=====================================

a. TOSCA YAML
=============


Introduction
-------------

This reference document is the VNF TOSCA Template Requirements for
OpenO, which provides recommendations and standards for building VNF
TOSCA templates compatible with OpenO– initial implementations of
Network Cloud. It has the following features:

1. VNF TOSCA template designer supports GUI and CLI.

2. VNF TOSCA template is aligned to the newest TOSCA protocol, “Working
   Draft 04-Revision 06”.

3. VNF TOSCA template supports EPA features, such as NUMA, Hyper
   Threading, SRIOV， etc.

Intended Audience
-----------------

This document is intended for persons developing VNF TOSCA templates
that will be orchestrated by OpenO.

Scope 
------

OpenO implementations of Network Cloud supports TOSCA Templates, also
referred to as TOSCA in this document.

OpenO requires the TOSCA Templates to follow a specific format. This
document provides the mandatory, recommended, and optional requirements
associated with this format.

Overview 
---------

The document includes three charters to help the VNF vendors to use the
VNF model design tools and understand the VNF package structure and VNF
TOSCA templates.

In the OPENO, VNF Package and VNFD template can be designed by manually
or via model designer tools. VNF model designer tools can provide the
GUI and CLI tools for the VNF vendor to develop the VNF Package and VNFD
template.

The VNF package structure is align to the NFV TOSCA protocol, and
supports CSAR

The VNFD and VNF package are all align to the NFV TOSCA protocol, which
supports multiple TOSCA template yaml files, and also supports
self-defined node or other extensions.

NFV TOSCA Template
------------------

TOSCA templates supported by OPENO must follow the requirements
enumerated in this section.

TOSCA Introduction
------------------

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
--------------------------------------

This section describing TOSCA modeling principles and data model for
NFV, which shall be based on [TOSCA-1.0] and [TOSCA-Simple-Profile-YAML
V1.0], or new type based on ETSI NFV requirements, etc.

VNF Descriptor Template
-----------------------

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
| | tosca\_definitions\_version: tosca\_simple\_yaml\_1\_0       |   |
| |                                                              |   |
| | description: VNFD TOSCA file demo                            |   |
| |                                                              |   |
| | imports:                                                     |   |
| |                                                              |   |
| | - TOSCA\_definition\_nfv\_1\_0.yaml                          |   |
| |                                                              |   |
| | - TOSCA\_definition\_nfv\_ext\_1\_0.yaml                     |   |
| |                                                              |   |
| | | **node\_types:                                             |   |
| |   tosca.nodes.nfv.VNF.vOpenNAT:                              |   |
| |   derived\_from:** tosca.nodes.nfv.VNF                       |   |
| | | **requirements:                                            |   |
| |   **- **sriov\_plane:                                        |   |
| |   capability:** tosca.capabilities.nfv.VirtualLinkable       |   |
| | | **node:** tosca.nodes.nfv.VnfVirtualLinkDesc               |   |
| | | **relationship:** tosca.relationships.nfv.VirtualLinksTo   |   |
| +--------------------------------------------------------------+   |
+====================================================================+
+--------------------------------------------------------------------+

EPA Requirements
----------------

1. SR-IOV Passthrought

Definitions of SRIOV\_Port are necessary if VDU supports SR-IOV. Here is
an example.

+------------------------------------------------+
| node\_templates:                               |
|                                                |
| vdu\_vNat:                                     |
|                                                |
| SRIOV\_Port:                                   |
|                                                |
| attributes:                                    |
|                                                |
| tosca\_name: SRIOV\_Port                       |
|                                                |
| properties:                                    |
|                                                |
| virtual\_network\_interface\_requirements:     |
|                                                |
| - name: sriov                                  |
|                                                |
| support\_mandatory: false                      |
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
| layer\_protocol: ipv4                          |
|                                                |
| requirements:                                  |
|                                                |
| - virtual\_binding:                            |
|                                                |
| capability: virtual\_binding                   |
|                                                |
| node: vdu\_vNat                                |
|                                                |
| relationship:                                  |
|                                                |
| type: tosca.relationships.nfv.VirtualBindsTo   |
|                                                |
| - virtual\_link:                               |
|                                                |
| node: tosca.nodes.Root                         |
|                                                |
| type: tosca.nodes.nfv.VduCpd                   |
|                                                |
| substitution\_mappings:                        |
|                                                |
| requirements:                                  |
|                                                |
| sriov\_plane:                                  |
|                                                |
| - SRIOV\_Port                                  |
|                                                |
| - virtual\_link                                |
|                                                |
| node\_type: tosca.nodes.nfv.VNF.vOpenNAT       |
+------------------------------------------------+

2. Hugepages

Definitions of mem\_page\_size as one property shall be added to
Properties and set the value to large if one VDU node supports
huagepages. Here is an example.

+----------------------------------+
| node\_templates:                 |
|                                  |
| vdu\_vNat:                       |
|                                  |
| Hugepages:                       |
|                                  |
| attributes:                      |
|                                  |
| tosca\_name: Huge\_pages\_demo   |
|                                  |
| properties:                      |
|                                  |
| mem\_page\_size:large            |
+==================================+
+----------------------------------+

3. NUMA (CPU/Mem)

Likewise, we shall add definitions of numa to
requested\_additional\_capabilities if we wand VUD nodes to support
NUMA. Here is an example.

+-------------------------------------------------+
| topology\_template:                             |
|                                                 |
| node\_templates:                                |
|                                                 |
| vdu\_vNat:                                      |
|                                                 |
| capabilities:                                   |
|                                                 |
| virtual\_compute:                               |
|                                                 |
| properties:                                     |
|                                                 |
| virtual\_memory:                                |
|                                                 |
| numa\_enabled: true                             |
|                                                 |
| virtual\_mem\_size: 2 GB                        |
|                                                 |
| requested\_additional\_capabilities:            |
|                                                 |
| numa:                                           |
|                                                 |
| support\_mandatory: true                        |
|                                                 |
| requested\_additional\_capability\_name: numa   |
|                                                 |
| target\_performance\_parameters:                |
|                                                 |
| hw:numa\_nodes: "2"                             |
|                                                 |
| hw:numa\_cpus.0: "0,1"                          |
|                                                 |
| hw:numa\_mem.0: "1024"                          |
|                                                 |
| hw:numa\_cpus.1: "2,3,4,5"                      |
|                                                 |
| hw:numa\_mem.1: "1024"                          |
+-------------------------------------------------+

4. Hyper-Theading

Definitions of Hyper-Theading are necessary as one of
requested\_additional\_capabilities of one VUD node if that node
supports Hyper-Theading. Here is an example.

+-------------------------------------------------------------+
| topology\_template:                                         |
|                                                             |
| node\_templates:                                            |
|                                                             |
| vdu\_vNat:                                                  |
|                                                             |
| capabilities:                                               |
|                                                             |
| virtual\_compute:                                           |
|                                                             |
| properties:                                                 |
|                                                             |
| virtual\_memory:                                            |
|                                                             |
| numa\_enabled: true                                         |
|                                                             |
| virtual\_mem\_size: 2 GB                                    |
|                                                             |
| requested\_additional\_capabilities:                        |
|                                                             |
| hyper\_threading:                                           |
|                                                             |
| support\_mandatory: true                                    |
|                                                             |
| requested\_additional\_capability\_name: hyper\_threading   |
|                                                             |
| target\_performance\_parameters:                            |
|                                                             |
| hw:cpu\_sockets : "2"                                       |
|                                                             |
| hw:cpu\_threads : "2"                                       |
|                                                             |
| hw:cpu\_cores : "2"                                         |
|                                                             |
| hw:cpu\_threads\_policy: "isolate"                          |
+-------------------------------------------------------------+

5. OVS+DPDK

Definitions of ovs\_dpdk are necessary as one of
requested\_additional\_capabilities of one VUD node if that node
supports dpdk. Here is an example.

+------------------------------------------------------+
| topology\_template:                                  |
|                                                      |
| node\_templates:                                     |
|                                                      |
| vdu\_vNat:                                           |
|                                                      |
| capabilities:                                        |
|                                                      |
| virtual\_compute:                                    |
|                                                      |
| properties:                                          |
|                                                      |
| virtual\_memory:                                     |
|                                                      |
| numa\_enabled: true                                  |
|                                                      |
| virtual\_mem\_size: 2 GB                             |
|                                                      |
| requested\_additional\_capabilities:                 |
|                                                      |
| ovs\_dpdk:                                           |
|                                                      |
| support\_mandatory: true                             |
|                                                      |
| requested\_additional\_capability\_name: ovs\_dpdk   |
|                                                      |
| target\_performance\_parameters:                     |
|                                                      |
| sw:ovs\_dpdk: "true"                                 |
+------------------------------------------------------+

NFV TOSCA Type Definition
-------------------------

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
| request\_additional\_capabilities   | No         | tosca.datatypes.nfv.RequestedAdditionalCapability   |               | Describes additional capability for a particular VDU.   |
+-------------------------------------+------------+-----------------------------------------------------+---------------+---------------------------------------------------------+
| virtual\_memory                     | yes        | tosca.datatypes.nfv.VirtualMemory                   |               | Describes virtual memory of the virtualized compute     |
+-------------------------------------+------------+-----------------------------------------------------+---------------+---------------------------------------------------------+
| virtual\_cpu                        | yes        | tosca.datatypes.nfv.VirtualCpu                      |               | Describes virtual CPU(s) of the virtualized compute.    |
+-------------------------------------+------------+-----------------------------------------------------+---------------+---------------------------------------------------------+
+-------------------------------------+------------+-----------------------------------------------------+---------------+---------------------------------------------------------+
| name                                | yes        |                                                     |               |                                                         |
+-------------------------------------+------------+-----------------------------------------------------+---------------+---------------------------------------------------------+

Definition
^^^^^^^^^^

+-----------------------------------------------------------+
| tosca.capabilities.nfv.VirtualCompute:                    |
|                                                           |
| derived\_from: tosca.capabilities.Root                    |
|                                                           |
| properties:                                               |
|                                                           |
| requested\_additional\_capabilities:                      |
|                                                           |
| type: map                                                 |
|                                                           |
| entry\_schema:                                            |
|                                                           |
| type: tosca.datatypes.nfv.RequestedAdditionalCapability   |
|                                                           |
| required: false                                           |
|                                                           |
| virtual\_memory:                                          |
|                                                           |
| type: tosca.datatypes.nfv.VirtualMemory                   |
|                                                           |
| required: true                                            |
|                                                           |
| virtual\_cpu:                                             |
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
| derived\_from         | tosca.nodes.Compute           |
+-----------------------+-------------------------------+



Attributes
^^^^^^^^^^

None


Capabilities
^^^^^^^^^^^^

+-------------------------+-------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------+
| Name                    | Type                                            | Constraints   | Description                                                                                         |
+=========================+=================================================+===============+=====================================================================================================+
| virtual\_compute        | tosca.capabilities.nfv.VirtualCompute           |               | Describes virtual compute resources capabilities.                                                   |
+-------------------------+-------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------+
| monitoring\_parameter   | tosca.capabilities.nfv.Metric                   | None          | Monitoring parameter, which can be tracked for a VNFC based on this VDU                             |
|                         |                                                 |               |                                                                                                     |
|                         |                                                 |               | Examples include: memory-consumption, CPU-utilisation, bandwidth-consumption, VNFC downtime, etc.   |
+-------------------------+-------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------+
| Virtual\_binding        | tosca.capabilities.nfv.VirtualBindable          |               | Defines ability of VirtualBindable                                                                  |
|                         |                                                 |               |                                                                                                     |
|                         | editor note: need to create a capability type   |               |                                                                                                     |
+-------------------------+-------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------+

Definition
^^^^^^^^^^

+-----------------------------------------------------------------------------------------------------+
| tosca.nodes.nfv.VDU.Compute:                                                                        |
|                                                                                                     |
| derived\_from: tosca.nodes.Compute                                                                  |
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
| boot\_order:                                                                                        |
|                                                                                                     |
| type: list # explicit index (boot index) not necessary, contrary to IFA011                          |
|                                                                                                     |
| entry\_schema:                                                                                      |
|                                                                                                     |
| type: string                                                                                        |
|                                                                                                     |
| required: false                                                                                     |
|                                                                                                     |
| nfvi\_constraints:                                                                                  |
|                                                                                                     |
| type: list                                                                                          |
|                                                                                                     |
| entry\_schema:                                                                                      |
|                                                                                                     |
| type: string                                                                                        |
|                                                                                                     |
| required: false                                                                                     |
|                                                                                                     |
| configurable\_properties:                                                                           |
|                                                                                                     |
| type: map                                                                                           |
|                                                                                                     |
| entry\_schema:                                                                                      |
|                                                                                                     |
| type: tosca.datatypes.nfv.VnfcConfigurableProperties                                                |
|                                                                                                     |
| required: true                                                                                      |
|                                                                                                     |
| attributes:                                                                                         |
|                                                                                                     |
| private\_address:                                                                                   |
|                                                                                                     |
| status: deprecated                                                                                  |
|                                                                                                     |
| public\_address:                                                                                    |
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
| virtual\_compute:                                                                                   |
|                                                                                                     |
| type: tosca.capabilities.nfv.VirtualCompute                                                         |
|                                                                                                     |
| virtual\_binding:                                                                                   |
|                                                                                                     |
| type: tosca.capabilities.nfv.VirtualBindable                                                        |
|                                                                                                     |
| #monitoring\_parameter:                                                                             |
|                                                                                                     |
| # modeled as ad hoc (named) capabilities in VDU node template                                       |
|                                                                                                     |
| # for example:                                                                                      |
|                                                                                                     |
| #capabilities:                                                                                      |
|                                                                                                     |
| # cpu\_load: tosca.capabilities.nfv.Metric                                                          |
|                                                                                                     |
| # memory\_usage: tosca.capabilities.nfv.Metric                                                      |
|                                                                                                     |
| host: #Editor note: FFS. How this capabilities should be used in NFV Profile                        |
|                                                                                                     |
| type: `*tosca.capabilities.Container* <#DEFN_TYPE_CAPABILITIES_CONTAINER>`__                        |
|                                                                                                     |
| valid\_source\_types: [`*tosca.nodes.SoftwareComponent* <#DEFN_TYPE_NODES_SOFTWARE_COMPONENT>`__]   |
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
| - virtual\_storage:                                                                                 |
|                                                                                                     |
| capability: tosca.capabilities.nfv.VirtualStorage                                                   |
|                                                                                                     |
| relationship: tosca.relationships.nfv.VDU.AttachedTo                                                |
|                                                                                                     |
| node: tosca.nodes.nfv.VDU.VirtualStorage                                                            |
|                                                                                                     |
| occurences: [ 0, UNBOUNDED ]                                                                        |
|                                                                                                     |
| - local\_storage: #For NFV Profile, this requirement is deprecated.                                 |
|                                                                                                     |
| occurrences: [0,0]                                                                                  |
|                                                                                                     |
| artifacts:                                                                                          |
|                                                                                                     |
| - sw\_image:                                                                                        |
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
| derived\_from: tosca.nodes.Root                                      |
|                                                                      |
| properties:                                                          |
|                                                                      |
| layer\_protocol:                                                     |
|                                                                      |
| type:string                                                          |
|                                                                      |
| constraints:                                                         |
|                                                                      |
| - valid\_values: [ethernet, mpls, odu2, ipv4, ipv6, pseudo\_wire ]   |
|                                                                      |
| required:true                                                        |
|                                                                      |
| role: #Name in ETSI NFV IFA011 v0.7.3 cpRole                         |
|                                                                      |
| type:string                                                          |
|                                                                      |
| constraints:                                                         |
|                                                                      |
| - valid\_values: [ root, leaf ]                                      |
|                                                                      |
| required:flase                                                       |
|                                                                      |
| description:                                                         |
|                                                                      |
| type: string                                                         |
|                                                                      |
| required: false                                                      |
|                                                                      |
| address\_data:                                                       |
|                                                                      |
| type: list                                                           |
|                                                                      |
| entry\_schema:                                                       |
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
| virtual\_network\_interface_\ | no         | VirtualNetworkInterfaceRequirements      |               | Specifies requirements on a virtual network              |
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
| virtual\_binding   | yes        | tosca.capabilities.nfv.VirtualBindable   |               | Describe the requirement for binding with VDU            |
+--------------------+------------+------------------------------------------+---------------+----------------------------------------------------------+
| virtual\_link      | no         | tosca.capabilities.nfv.VirtualLinkable   |               | Describes the requirements for linking to virtual link   |
+--------------------+------------+------------------------------------------+---------------+----------------------------------------------------------+

Definition
^^^^^^^^^^

+----------------------------------------------------------------+
| tosca.nodes.nfv.VduCpd:                                        |
|                                                                |
| derived\_from: tosca.nodes.nfv.Cpd                             |
|                                                                |
| properties:                                                    |
|                                                                |
| bitrate\_requirement:                                          |
|                                                                |
| type: integer                                                  |
|                                                                |
| required:false                                                 |
|                                                                |
| virtual\_network\_interface\_requirements                      |
|                                                                |
| type: list                                                     |
|                                                                |
| entry\_schema:                                                 |
|                                                                |
| type: VirtualNetworkInterfaceRequirements                      |
|                                                                |
| required:false                                                 |
|                                                                |
| requirements:                                                  |
|                                                                |
| - virtual\_link:                                               |
|                                                                |
| capability: tosca.capabilities.nfv.VirtualLinkable             |
|                                                                |
| relationship: tosca.relationships.nfv.VirtualLinksTo           |
|                                                                |
| node: tosca.nodes.nfv.VnfVirtualLinkDesc - virtual\_binding:   |
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
presentation. Slide 8. With specific rules of “valid\_target\_type”

+---------------------------+--------------------------------------+
| **Shorthand Name**        | VirtualStorage                       |
+===========================+======================================+
| **Type Qualified Name**   | tosca: VirtualStorage                |
+---------------------------+--------------------------------------+
| **Type URI**              | tosca.nodes.nfv.VDU.VirtualStorage   |
+---------------------------+--------------------------------------+
| **derived\_from**         | tosca.nodes.Root                     |
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
| **derived\_from**         | tosca.artifacts.Deployment.Image   |
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
| container\_format                        | yes        | string             |               | The container format describes the container file format in which software image is provided.      |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| disk\_format                             | yes        | string             |               | The disk format of a software image is the format of the underlying disk image                     |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| min\_disk                                | yes        | scalar-unit.size   |               | The minimal disk size requirement for this software image.                                         |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| min\_ram                                 | no         | scalar-unit.size   |               | The minimal RAM requirement for this software image.                                               |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| Size                                     | yes        | scalar-unit.size   |               | The size of this software image                                                                    |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| sw\_image                                | yes        | string             |               | A reference to the actual software image within VNF Package, or url.                               |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| operating\_system                        | no         | string             |               | Identifies the operating system used in the software image.                                        |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+
| supported \_virtualization\_enviroment   | no         | list               |               | Identifies the virtualization environments (e.g. hypervisor) compatible with this software image   |
+------------------------------------------+------------+--------------------+---------------+----------------------------------------------------------------------------------------------------+

Definition
^^^^^^^^^^

+-----------------------------------------------------+
| tosca.artifacts.nfv.SwImage:                        |
|                                                     |
|   derived\_from: tosca.artifacts.Deployment.Image   |
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
|     container\_format:                              |
|                                                     |
|       type: string                                  |
|                                                     |
| required: true                                      |
|                                                     |
|     disk\_format:                                   |
|                                                     |
|       type: string                                  |
|                                                     |
| required: true                                      |
|                                                     |
|     min\_disk:                                      |
|                                                     |
|       type: scalar-unit.size # Number               |
|                                                     |
| required: true                                      |
|                                                     |
|     min\_ram:                                       |
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
|     sw\_image:                                      |
|                                                     |
|       type: string                                  |
|                                                     |
| required: true                                      |
|                                                     |
|     operating\_system:                              |
|                                                     |
|       type: string                                  |
|                                                     |
| required: false                                     |
|                                                     |
|     supported\_virtualisation\_environments:        |
|                                                     |
|       type: list                                    |
|                                                     |
|       entry\_schema:                                |
|                                                     |
|         type: string                                |
|                                                     |
| required: false                                     |
+-----------------------------------------------------+

vNAT Example
------------

openovnf\_\_vOpenNAT.yaml
~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+
| imports:                                                    |
|                                                             |
| - openonfv\_\_tosca.capabilities.Scalable.yaml              |
|                                                             |
| - openonfv\_\_tosca.capabilities.nfv.Metric.yaml            |
|                                                             |
| - openonfv\_\_tosca.capabilities.network.Bindable.yaml      |
|                                                             |
| - openonfv\_\_tosca.capabilities.Attachment.yaml            |
|                                                             |
| - openonfv\_\_tosca.capabilities.nfv.VirtualBindable.yaml   |
|                                                             |
| - openonfv\_\_tosca.requirements.nfv.VirtualStorage.yaml    |
|                                                             |
| - openonfv\_\_tosca.nodes.nfv.VDU.VirtualStorage.yaml       |
|                                                             |
| - openonfv\_\_tosca.relationships.nfv.VirtualBindsTo.yaml   |
|                                                             |
| - openonfv\_\_tosca.nodes.nfv.VDU.Compute.yaml              |
|                                                             |
| - openonfv\_\_tosca.artifacts.nfv.SwImage.yaml              |
|                                                             |
| - openonfv\_\_tosca.capabilities.nfv.VirtualCompute.yaml    |
|                                                             |
| - openonfv\_\_tosca.capabilities.Container.yaml             |
|                                                             |
| - openonfv\_\_tosca.capabilities.nfv.VirtualStorage.yaml    |
|                                                             |
| - openonfv\_\_tosca.requirements.nfv.VirtualBinding.yaml    |
|                                                             |
| - openovnf\_\_tosca.nodes.nfv.VNF.vOpenNAT.yaml             |
|                                                             |
| - openonfv\_\_tosca.capabilities.Endpoint.Admin.yaml        |
|                                                             |
| - openonfv\_\_tosca.capabilities.OperatingSystem.yaml       |
|                                                             |
| - openonfv\_\_tosca.nodes.nfv.VduCpd.yaml                   |
|                                                             |
| - openonfv\_\_tosca.relationships.nfv.VDU.AttachedTo.yaml   |
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
| topology\_template:                                         |
|                                                             |
| node\_templates:                                            |
|                                                             |
| vdu\_vNat:                                                  |
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
| container\_format: bare                                     |
|                                                             |
| disk\_format: qcow2                                         |
|                                                             |
| min\_disk: 10 GB                                            |
|                                                             |
| min\_ram: 1 GB                                              |
|                                                             |
| size: 10 GB                                                 |
|                                                             |
| sw\_image: /swimages/xenial-snat.qcow2                      |
|                                                             |
| operating\_system: unbantu                                  |
|                                                             |
| attributes:                                                 |
|                                                             |
| tosca\_name: vdu\_vNat                                      |
|                                                             |
| capabilities:                                               |
|                                                             |
| virtual\_compute:                                           |
|                                                             |
| properties:                                                 |
|                                                             |
| virtual\_memory:                                            |
|                                                             |
| numa\_enabled: true                                         |
|                                                             |
| virtual\_mem\_size: 2 GB                                    |
|                                                             |
| requested\_additional\_capabilities:                        |
|                                                             |
| numa:                                                       |
|                                                             |
| support\_mandatory: true                                    |
|                                                             |
| requested\_additional\_capability\_name: numa               |
|                                                             |
| target\_performance\_parameters:                            |
|                                                             |
| hw:numa\_nodes: "2"                                         |
|                                                             |
| hw:numa\_cpus.0: "0,1"                                      |
|                                                             |
| hw:numa\_mem.0: "1024"                                      |
|                                                             |
| hw:numa\_cpus.1: "2,3,4,5"                                  |
|                                                             |
| hw:numa\_mem.1: "1024"                                      |
|                                                             |
| hyper\_threading:                                           |
|                                                             |
| support\_mandatory: true                                    |
|                                                             |
| requested\_additional\_capability\_name: hyper\_threading   |
|                                                             |
| target\_performance\_parameters:                            |
|                                                             |
| hw:cpu\_sockets : "2"                                       |
|                                                             |
| hw:cpu\_threads : "2"                                       |
|                                                             |
| hw:cpu\_cores : "2"                                         |
|                                                             |
| hw:cpu\_threads\_policy: "isolate"                          |
|                                                             |
| ovs\_dpdk:                                                  |
|                                                             |
| support\_mandatory: true                                    |
|                                                             |
| requested\_additional\_capability\_name: ovs\_dpdk          |
|                                                             |
| target\_performance\_parameters:                            |
|                                                             |
| sw:ovs\_dpdk: "true"                                        |
|                                                             |
| virtual\_cpu:                                               |
|                                                             |
| cpu\_architecture: X86                                      |
|                                                             |
| num\_virtual\_cpu: 2                                        |
|                                                             |
| properties:                                                 |
|                                                             |
| configurable\_properties:                                   |
|                                                             |
| test:                                                       |
|                                                             |
| additional\_vnfc\_configurable\_properties:                 |
|                                                             |
| aaa: 1                                                      |
|                                                             |
| name: vNat                                                  |
|                                                             |
| descrption: the virtual machine of vNat                     |
|                                                             |
| boot\_order:                                                |
|                                                             |
| - vNAT\_Storage                                             |
|                                                             |
| requirements:                                               |
|                                                             |
| - virtual\_storage:                                         |
|                                                             |
| capability: virtual\_storage                                |
|                                                             |
| node: vNAT\_Storage                                         |
|                                                             |
| relationship:                                               |
|                                                             |
| properties:                                                 |
|                                                             |
| location: /mnt/volume\_0                                    |
|                                                             |
| type: tosca.relationships.nfv.VDU.AttachedTo                |
|                                                             |
| - local\_storage:                                           |
|                                                             |
| node: tosca.nodes.Root                                      |
|                                                             |
| type: tosca.nodes.nfv.VDU.Compute                           |
|                                                             |
| SRIOV\_Port:                                                |
|                                                             |
| attributes:                                                 |
|                                                             |
| tosca\_name: SRIOV\_Port                                    |
|                                                             |
| properties:                                                 |
|                                                             |
| virtual\_network\_interface\_requirements:                  |
|                                                             |
| - name: sriov                                               |
|                                                             |
| support\_mandatory: false                                   |
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
| layer\_protocol: ipv4                                       |
|                                                             |
| requirements:                                               |
|                                                             |
| - virtual\_binding:                                         |
|                                                             |
| capability: virtual\_binding                                |
|                                                             |
| node: vdu\_vNat                                             |
|                                                             |
| relationship:                                               |
|                                                             |
| type: tosca.relationships.nfv.VirtualBindsTo                |
|                                                             |
| - virtual\_link:                                            |
|                                                             |
| node: tosca.nodes.Root                                      |
|                                                             |
| type: tosca.nodes.nfv.VduCpd                                |
|                                                             |
| vNAT\_Storage:                                              |
|                                                             |
| attributes:                                                 |
|                                                             |
| tosca\_name: vNAT\_Storage                                  |
|                                                             |
| properties:                                                 |
|                                                             |
| id: vNAT\_Storage                                           |
|                                                             |
| size\_of\_storage: 10 GB                                    |
|                                                             |
| rdma\_enabled: false                                        |
|                                                             |
| type\_of\_storage: volume                                   |
|                                                             |
| type: tosca.nodes.nfv.VDU.VirtualStorage                    |
|                                                             |
| substitution\_mappings:                                     |
|                                                             |
| requirements:                                               |
|                                                             |
| sriov\_plane:                                               |
|                                                             |
| - SRIOV\_Port                                               |
|                                                             |
| - virtual\_link                                             |
|                                                             |
| node\_type: tosca.nodes.nfv.VNF.vOpenNAT                    |
|                                                             |
| tosca\_definitions\_version: tosca\_simple\_yaml\_1\_0      |
+-------------------------------------------------------------+

openonfv\_\_tosca.nodes.nfv.VDU.VirtualStorage.yaml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------+
| imports:                                                   |
|                                                            |
| - openonfv\_\_tosca.capabilities.nfv.VirtualStorage.yaml   |
|                                                            |
| node\_types:                                               |
|                                                            |
| tosca.nodes.nfv.VDU.VirtualStorage:                        |
|                                                            |
| capabilities:                                              |
|                                                            |
| virtual\_storage:                                          |
|                                                            |
| type: tosca.capabilities.nfv.VirtualStorage                |
|                                                            |
| derived\_from: tosca.nodes.Root                            |
|                                                            |
| properties:                                                |
|                                                            |
| id:                                                        |
|                                                            |
| type: string                                               |
|                                                            |
| size\_of\_storage:                                         |
|                                                            |
| type: string                                               |
|                                                            |
| rdma\_enabled:                                             |
|                                                            |
| required: false                                            |
|                                                            |
| type: boolean                                              |
|                                                            |
| type\_of\_storage:                                         |
|                                                            |
| type: string                                               |
|                                                            |
| tosca\_definitions\_version: tosca\_simple\_yaml\_1\_0     |
+------------------------------------------------------------+

openonfv\_\_tosca.nodes.nfv.VduCpd.yaml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+
| data\_types:                                                    |
|                                                                 |
| tosca.datatypes.nfv.L3AddressData:                              |
|                                                                 |
| properties:                                                     |
|                                                                 |
| number\_of\_ip\_address:                                        |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: integer                                                   |
|                                                                 |
| ip\_address\_assignment:                                        |
|                                                                 |
| type: boolean                                                   |
|                                                                 |
| ip\_address\_type:                                              |
|                                                                 |
| constraints:                                                    |
|                                                                 |
| - valid\_values:                                                |
|                                                                 |
| - ipv4                                                          |
|                                                                 |
| - ipv6                                                          |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: string                                                    |
|                                                                 |
| floating\_ip\_activated:                                        |
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
| support\_mandatory:                                             |
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
| entry\_schema:                                                  |
|                                                                 |
| type: string                                                    |
|                                                                 |
| type: map                                                       |
|                                                                 |
| tosca.datatype.nfv.AddressData:                                 |
|                                                                 |
| properties:                                                     |
|                                                                 |
| address\_type:                                                  |
|                                                                 |
| constraints:                                                    |
|                                                                 |
| - valid\_values:                                                |
|                                                                 |
| - mac\_address                                                  |
|                                                                 |
| - ip\_address                                                   |
|                                                                 |
| type: string                                                    |
|                                                                 |
| l2\_address\_data:                                              |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: tosca.datatypes.nfv.L2AddressData                         |
|                                                                 |
| l3\_address\_data:                                              |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: tosca.datatypes.nfv.L3AddressData                         |
|                                                                 |
| tosca.datatypes.nfv.L2AddressData: {}                           |
|                                                                 |
| imports:                                                        |
|                                                                 |
| - openonfv\_\_tosca.requirements.nfv.VirtualBinding.yaml        |
|                                                                 |
| - openonfv\_\_tosca.requirements.nfv.VirtualBinding.yaml        |
|                                                                 |
| node\_types:                                                    |
|                                                                 |
| tosca.nodes.nfv.VduCpd:                                         |
|                                                                 |
| derived\_from: tosca.nodes.Root                                 |
|                                                                 |
| properties:                                                     |
|                                                                 |
| virtual\_network\_interface\_requirements:                      |
|                                                                 |
| entry\_schema:                                                  |
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
| - valid\_values:                                                |
|                                                                 |
| - root                                                          |
|                                                                 |
| - leaf                                                          |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: string                                                    |
|                                                                 |
| bitrate\_requirement:                                           |
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
| layer\_protocol:                                                |
|                                                                 |
| constraints:                                                    |
|                                                                 |
| - valid\_values:                                                |
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
| - pseudo\_wire                                                  |
|                                                                 |
| type: string                                                    |
|                                                                 |
| address\_data:                                                  |
|                                                                 |
| entry\_schema:                                                  |
|                                                                 |
| type: tosca.datatype.nfv.AddressData                            |
|                                                                 |
| required: false                                                 |
|                                                                 |
| type: list                                                      |
|                                                                 |
| requirements:                                                   |
|                                                                 |
| - virtual\_binding:                                             |
|                                                                 |
| capability: tosca.capabilities.nfv.VirtualBindable              |
|                                                                 |
| occurrences:                                                    |
|                                                                 |
| - 0                                                             |
|                                                                 |
| - UNBOUNDED                                                     |
|                                                                 |
| - virtual\_link:                                                |
|                                                                 |
| capability: tosca.capabilities.nfv.VirtualBindable              |
|                                                                 |
| occurrences:                                                    |
|                                                                 |
| - 0                                                             |
|                                                                 |
| - UNBOUNDED                                                     |
|                                                                 |
| tosca\_definitions\_version: tosca\_simple\_yaml\_1\_0          |
+-----------------------------------------------------------------+

.. |image1| image:: Image1.png
   :width: 5.76806in
   :height: 4.67161in
.. |image2| image:: Image2.png
   :width: 5.40486in
   :height: 2.46042in


b. Heat
=======

General Guidelines
------------------

YAML Format
-----------

Heat Orchestration Templates must use valid YAML. YAML (YAML Ain't
Markup Language) is a human friendly data serialization standard for all
programming languages. See http://www.yaml.org/.

Heat Orchestration Template Format
----------------------------------

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

.. code-block:: python

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

-  heat\_template\_version:

-  description:

-  parameters:

-  resources:

Heat Orchestration templates for ONAP may contain the following
sections:

-  parameter\_groups:

-  outputs:

heat\_template\_version
^^^^^^^^^^^^^^^^^^^^^^^

This section is ONAP mandatory. The heat\_template\_version must be set
to a date that is supported by the OpenStack environment.

description
^^^^^^^^^^^

This ONAP mandatory section allows for a description of the template.

parameter\_groups
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
availability\_zone. See `Property: availability\_zone`_. for more details on
availability\_zone.

.. code-block:: python

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
      characters and “\_” underscores. Special characters must not be
      used.

-  type:

   -  The type of the parameter. Supported types are string, number,
      comma\_delimited\_list, json and boolean.

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
   allowed\_values.

   -  range: The range constraint applies to parameters of type number.
      It defines a lower and upper limit for the numeric value of the
      parameter. The syntax of the range constraint is

    range: { min: <lower limit>, max: <upper limit> }

    It is possible to define a range constraint with only a lower limit
    or an upper limit.

-  allowed\_values: The allowed\_values constraint applies to parameters
   of type string or number. It specifies a set of possible values for a
   parameter. At deployment time, the user-provided value for the
   respective parameter must match one of the elements of the list. The
   syntax of the allowed\_values constraint is

    allowed\_values: [ <value>, <value>, ... ]

    Alternatively, the following YAML list notation can be used

    allowed\_values:

    - <value>

    - <value>

    - ...

-  Other <constraint type> are optional, they may be used (e.g., length,
   modulo, allowed\_pattern, custom\_constraint, allowed\_values (for
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

.. code-block:: python

 resources:
   <resource ID>:
     type: <resource type>
     properties:
       <property name>: <property value>
     metadata:
       <resource specific metadata>
     depends\_on: <resource ID or list of ID>
     update\_policy: <update policy>
     deletion\_policy: <deletion policy>
     external\_id: <external resource ID>
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

-  depends\_on

   -  Dependencies of the resource on one or more resources of the
      template. This attribute is optional. See `Resource Data Synchronization`_ for additional details.

-  update\_policy

   -  Update policy for the resource, in the form of a nested
      dictionary. Whether update policies are supported and what the
      exact semantics are depends on the type of the current resource.
      This attribute is optional.

-  deletion\_policy

   -  Deletion policy for the resource. The allowed deletion policies
      are Delete, Retain, and Snapshot. Beginning with
      heat\_template\_version 2016-10-14, the lowercase equivalents
      delete, retain, and snapshot are also allowed. This attribute is
      optional; the default policy is to delete the physical resource
      when deleting a resource from the stack.

-  external\_id

   -  Allows for specifying the resource\_id for an existing external
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
-----------------------

The environment file is a yaml text file.
(https://docs.openstack.org/developer/heat/template_guide/environment.html)

The environment file can contain the following sections:

-  parameters: A list of key/value pairs.

-  resource\_registry: Definition of custom resources.

-  parameter\_defaults: Default parameters passed to all template
   resources.

-  encrypted\_parameters: List of encrypted parameters.

-  event\_sinks: List of endpoints that would receive stack events.

-  parameter\_merge\_strategies: Merge strategies for merging parameters
   and parameter defaults from the environment file.

Environment files for ONAP must contain the following sections:

-  parameters:

Environment files for ONAP may contain the following sections:

-  resource\_registry:

-  parameter\_defaults:

-  encrypted\_parameters:

-  event\_sinks:

-  parameter\_merge\_strategies:

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
--------------------------------------------

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
------------------------------------------

In order to enable ONAP to understand the relationship between Heat
files, the following Heat file naming convention must be utilized.

In the examples below, <text> represents any alphanumeric string that
must not contain any special characters and must not contain the word
“base”.

Base Modules
~~~~~~~~~~~~

The file name for the base module must include “base” in the filename
and must match one of the following options:

-  base\_<text>.y[a]ml

-  <text>\_base.y[a]ml

-  base.y[a]ml

-  <text>\_base\_<text>.y[a]ml

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

-  module\_<text>.y[a]ml

-  <text>\_module.y[a]ml

-  module.y[a]ml

Cinder Volume Modules
~~~~~~~~~~~~~~~~~~~~~

The file name for the Cinder volume module must be named the same as the
corresponding module it is supporting (base module or incremental
module) with “\_volume” appended

-  <base module name>\_volume.y[a]ml

-  <incremental module name>\_volume.y[a]ml

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
---------------------------------------

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
   parameter must have constraints for range and/or allowed\_values.

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
   parameter must have constraints for range or allowed\_values.

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
   must have constraints for range and/or allowed\_values.

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
   must have constraints for range and/or allowed\_values.

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
   comma\_delimited\_list.

   -  If the Output parameter has a comma\_delimited\_list value (e.g.,
      a collection of UUIDs from a Resource Group), then the
      corresponding input parameter must be declared as type json and
      not a comma\_delimited\_list, which is actually a string value
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
   type comma\_delimited\_list.

-  If the Output parameter has a comma\_delimited\_list value (e.g., a
   collection of UUIDs from a Resource Group), then the corresponding
   input parameter must be declared as type json and not a
   comma\_delimited\_list, which is actually a string value with
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
----------------------------

VNF Heat Orchestration Templates must not be designed to utilize the
OpenStack heat stack-update command for scaling (growth/de-growth). ONAP
does not support the use of heat stack-update command for scaling.

It is important to note that ONAP only supports heat stack-update for
image upgrades.

Networking
----------

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
-----------------

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

-  ONAP supports the property allowed\_address\_pairs in the resource
   OS::Neutron:Port and the property
   virtual\_machine\_interface\_allowed\_address\_pairs in
   OS::ContrailV2::VirtualMachineInterfaces. This allows the assignment
   of a virtual IP (VIP) address to a set of VMs.

VNF Heat Orchestration Templates must pass the appropriate external
network IDs into nested VM templates when nested Heat is used.

Internal Networks
-----------------

The VNF Heat Orchestration Templates must include the resource(s) to
create the internal network. The internal network must be either a
Neutron Network or a Contrail Network.

In the modular approach, internal networks must be created in the Base
Module, with their resource IDs exposed as outputs (i.e., ONAP Base
Module Output Parameters) for use by all incremental modules. If the
Network resource ID is required in the base template, then a
get\_resource must be used.

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

-  ONAP supports the property allowed\_address\_pairs in the resource
   OS::Neutron:Port and the property
   virtual\_machine\_interface\_allowed\_address\_pairs in
   OS::ContrailV2::VirtualMachineInterfaces. This allows the assignment
   of a virtual IP (VIP) address to a set of VMs.

ONAP does not programmatically enforce a naming convention for
parameters for internal network. However, a naming convention is
provided that must be followed. `ONAP Resource ID and Parameter Naming Convention`_ provides additional details.

ONAP Resource ID and Parameter Naming Convention
------------------------------------------------

This section provides the ONAP naming requirements for

1. Resource IDs

2. Resource Property Parameters

{vm-type}
---------

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
"oam" is a substring of "oam\_protected". It will cause the
Pre-Amsterdam VNF Validation Program (i.e., ICE Project) process to
produce erroneous error messages.

The {vm-type} should not contain the string “\_int” or “int\_” or
“\_int\_”. It may cause the Pre-Amsterdam VNF Validation Program (i.e.,
ICE Project) process to produce erroneous error messages.

The {vm-type} must be the same case in all parameter names in the VNF.

The {vm-type} must be the same case in all Resource IDs in the VNF.

It is recommended that the {vm-type} case in the parameter names matches
the {vm-type} case in the Resource IDs.

There are two exceptions to the above rules:

1. The six ONAP Metadata parameters must not be prefixed with a common
   {vm-type} identifier. They are *vnf\_name*, *vnf\_id*,
   *vf\_module\_id*, *vf\_module\_name, vm\_role*. The ONAP Metadata
   parameters are described in `Resource:  OS::Nova::Server – Metadata Parameters`_.

2. The parameter referring to the OS::Nova::Server property
   availability\_zone must not be prefixed with a common {vm-type}
   identifier. availability\_zone is described in `Property: availability_zone`_.

{network-role}
--------------

The assignment of a {network-role} is discussed in `Networking`_.

Any parameter that is associated with an external network must include
the {network-role} as part of the parameter name.

Any resource ID that is associated with an external network must include
the {network-role} as part of the resource ID.

Any parameter that is associated with an internal network must include
int\_{network-role} as part of the parameter name.

Any resource ID that is associated with an internal network must include
int\_{network-role} as part of the resource ID.

Note that {network-role} must not be a substring of {vm-type}. A
substring of a string is another string that occurs "in". For example,
"oam" is a substring of "oam\_protected". It will cause the
Pre-Amsterdam VNF Validation Program (i.e., ICE Project) process to
produce erroneous error messages.

The {network-role} should not contain the string “\_int” or “int\_” or
“\_int\_”. It may cause the Pre-Amsterdam VNF Validation Program (i.e.,
ICE Project) process to produce erroneous error messages.

The {network-role} must be the same case in all parameter names in the
VNF.

The {network-role} must be the same case in all Resource IDs in the VNF.

It is recommended that the {network-role} case in the parameter names
matches the {network-role} case in the Resource IDs.

Resource IDs
------------

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
resource ID must contain int\_{network-role}.

When a resource is associated with a single {vm-type} and a single
external network, the resource ID must contain both the {vm-type} and
{network-role}.

-  The {vm-type} must appear before the {network-role} and must be
   separated by an underscore (i.e., {vm-type}\_{network-role}).

-  Note that an {index} value may separate the {vm-type} and the
   {network-role}. An underscore will separate the three values (i.e.,
   {vm-type}\_{index}\_{network-role}).

When a resource is associated with a single {vm-type} and a single
internal network, the resource ID must contain both the {vm-type} and
int\_{network-role}.

-  The {vm-type} must appear before the int\_{network-role} and must be
   separated by an underscore (i.e., {vm-type}\_int\_{network-role}).

-  Note that an {index} value may separate the {vm-type} and the
   int\_{network-role}. An underscore will separate the three values
   (i.e., {vm-type}\_{index}\_int\_{network-role}).

When a resource is associated with more than one {vm-type} and/or more
than one network, the resource ID

-  must not contain the {vm-type} and/or
   {network-role}/int\_{network-role}

-  should contain the term “shared” and/or contain text that identifies
   the VNF.

Only alphanumeric characters and “\_” underscores must be used in the
resource ID. Special characters must not be used.

All {index} values must be zero based. That is, the {index} must start
at zero and increment by one.

The table below provides example OpenStack Heat resource ID for
resources only associated with one {vm-type} and/or one network.

+--------------------------------+------------------------------------------------------------+
| Resource Type                  | Resource ID Format                                         |
+================================+============================================================+
| OS::Cinder::Volume             | {vm\_type}\_volume\_{index}                                |
+--------------------------------+------------------------------------------------------------+
| OS::Cinder::VolumeAttachment   | {vm\_type}\_volumeattachment\_{index}                      |
+--------------------------------+------------------------------------------------------------+
| OS::Heat::CloudConfig          | {vm\_type}\_RCC                                            |
+--------------------------------+------------------------------------------------------------+
| OS::Heat::MultipartMime        | {vm\_type}\_RMM                                            |
+--------------------------------+------------------------------------------------------------+
| OS::Heat::ResourceGroup        | {vm\_type}\_RRG                                            |
+--------------------------------+------------------------------------------------------------+
| OS::Heat::SoftwareConfig       | {vm\_type}\_RSC                                            |
+--------------------------------+------------------------------------------------------------+
| OS::Neutron::Port              | {vm\_type}\_{index}\_{network\_role}\_{index}\_port        |
+--------------------------------+------------------------------------------------------------+
|                                | {vm\_type}\_{index}\_int\_{network\_role}\_{index}\_port   |
+--------------------------------+------------------------------------------------------------+
| OS::Neutron::SecurityGroup     | {vm\_type}\_RSG                                            |
+--------------------------------+------------------------------------------------------------+
| OS::Neutron::Subnet            | {network\_role}\_subnet\_{index}                           |
+--------------------------------+------------------------------------------------------------+
| OS::Nova::Server               | {vm\_type}\_{index}                                        |
+--------------------------------+------------------------------------------------------------+
| OS::Nova::ServerGroup          | {vm\_type}\_RSG                                            |
+--------------------------------+------------------------------------------------------------+
| OS::Swift::Container           | {vm\_type}\_RSwiftC                                        |
+--------------------------------+------------------------------------------------------------+

    Table 1: Example OpenStack Heat Resource ID

The table below provides example Contrail Heat resource ID for resources
only associated with one {vm-type} and/or one network.

+-------------------------------------------+---------------------------------------------+
| Resource Type                             | Resource ID Format                          |
+===========================================+=============================================+
| OS::ContrailV2::InstanceIp                | {vm\_type}\_{index}\_{network\_role}\_RII   |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::InterfaceRouteTable       | {network\_role}\_RIRT                       |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::NetworkIpam               | {network\_role}\_RNI                        |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::PortTuple                 | {vm\_type}\_RPT                             |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::ServiceHealthCheck        | {vm\_type}\_RSHC\_{LEFT\|RIGHT}             |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::ServiceTemplate           | {vm\_type}\_RST\_{index}                    |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::VirtualMachineInterface   | int\_{network\_role}\_RVMI                  |
+-------------------------------------------+---------------------------------------------+
| OS::ContrailV2::VirtualNetwork            | int\_{network\_role}\_RVN                   |
+-------------------------------------------+---------------------------------------------+

    Table 2: Example Contrail Heat resource ID

Resource: OS::Nova::Server - Parameters
---------------------------------------

The resource OS::Nova::Server manages the running virtual machine (VM)
instance within an OpenStack cloud. (See
https://docs.openstack.org/developer/heat/template_guide/openstack.html#OS::Nova::Server.)

Four properties of this resource must follow the ONAP parameter naming
convention. The four properties are:

1. image

2. flavor

3. name

4. availability\_zone

The table below provides a summary. The sections that follow provides
additional details.

Note that the {vm\_type} must be identical across all four property
parameter for a given OS::Nova::Server resource.

+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+
| Resource OS::Nova::Server                                                                                                                       |
+=============================+===============================+==================+==============================+=================================+
| Property Name               | ONAP Parameter Name           | Parameter Type   | Parameter Value Generation   | ONAP Parameter Classification   |
+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+
| image                       | {vm-type}\_image\_name        | string           | Environment File             | ONAP Constant                   |
+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+
| flavor                      | {vm-type}\_flavor\_name       | string           | Environment File             | ONAP Constant                   |
+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+
| name                        | {vm-type}\_name\_{index}      | string           | ONAP                         | ONAP Orchestration              |
+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+
|                             | {vm-type}\_names              | CDL              | ONAP                         | ONAP Orchestration              |
+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+
| availability\_zone          | availability\_zone\_{index}   | string           | ONAP                         | ONAP Orchestration              |
+-----------------------------+-------------------------------+------------------+------------------------------+---------------------------------+

Table 3 Resource Property Parameter Names

Property: image
~~~~~~~~~~~~~~~

The parameter associated with the property image is an ONAP Constant
parameter.

The parameters must be named {vm-type}\_image\_name in the Heat
Orchestration Template.

The parameter must be declared as type: string

The parameter must be enumerated in the Heat Orchestration Template
environment file.

Each VM type (i.e., {vm-type}) must have a separate parameter for image,
even if more than one {vm-type} shares the same image. This provides
maximum clarity and flexibility.

*Example Parameter Definition*

.. code-block:: python

 parameters:
     {vm-type}_image_name:
         type: string
         description: {vm-type} server image

Property: flavor
~~~~~~~~~~~~~~~~

The parameter associated with the property flavor is an ONAP Constant
parameter.

The parameters must be named {vm-type}\_flavor\_name in the Heat
Orchestration Template.

The parameter must be declared as type: string

The parameter must be enumerated in the Heat Orchestration Template
environment file.

Each VM type (i.e., {vm-type}) must have a separate parameter for
flavors, even if more than one {vm-type} shares the same flavor. This
provides maximum clarity and flexibility.

*Example Parameter Definition*

.. code-block:: python

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
comma\_delimited\_list

If the parameter is declared as type:string, the parameter must be named
{vm-type}\_name\_{index}, where {index} is a numeric value that starts
at zero and increments by one.

If the parameter is declared as type:comma\_delimited\_list, the
parameter must be named as {vm-type}\_names

Each element in the VM Name list should be assigned to successive
instances of that VM type.

If a VNF contains more than three instances of a given {vm-type}, the
comma\_delimited\_list form of the parameter name (i.e.,
{vm-type}\_names) should be used to minimize the number of unique
parameters defined in the Heat.

*Example: Parameter Definition*

.. code-block:: python

 parameters:
     {vm-type}_names:
         type: comma_delimited_list
         description: VM Names for {vm-type} VMs
     {vm-type}_name_{index}:
         type: string
         description: VM Name for {vm-type} VM {index}

*Example: comma\_delimited\_list*

In this example, the {vm-type} has been defined as “lb” for load
balancer.

.. code-block:: python

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

.. code-block:: python

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

- “ ! $ ‘ ( ) = ~ ^ \| @ \` { } [ ] > , . \_

Property: availability\_zone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The parameter associated with the property availability\_zone is an ONAP
Orchestration parameter.

The parameter value is provided to the Heat template by ONAP. The
parameter must not be enumerated in the environment file.

The parameter must be named availability\_zone\_{index} in the Heat
Orchestration Template. The {index} must start at zero. The {index} must
increment by one. The parameter name must not include the {vm-type}.

The parameter must be declared as type: string

The parameter must not be declared as type: comma\_delimited\_list

Example
~~~~~~~

The example below depicts part of a Heat Orchestration Template that
uses the four OS::Nova::Server properties discussed in this section.

In the Heat Orchestration Template below, four Virtual Machines
(OS::Nova::Server) are created: two dns servers with {vm-type} set to
“dns” and two oam servers with {vm-type} set to “oam”. Note that the
parameter associated with the property name is a comma\_delimited\_list
for dns and a string for oam.

.. code-block:: python

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
------------------------------------------------

The resource OS::Nova::Server has an OpenStack optional property
metadata. The metadata property is mandatory for ONAP Heat Orchestration
Templates; it must be included.

ONAP requires the following three mandatory metadata parameters for an
OS::Nova::Server resource:

-  vnf\_id

-  vf\_module\_id

-  vnf\_name

ONAP allows the following three optional metadata parameters for an
OS::Nova::Server resource. They may be included

-  vm\_role

-  vf\_module\_name

Note that the metadata parameters do not and must not contain {vm-type}
in their name.

When Metadata parameters are past into a nested heat template, the
parameter names must not change.

The table below provides a summary. The sections that follow provides
additional details.

+---------------------------+------------------+----------------------+------------------------------+
| Metadata Parameter Name   | Parameter Type   | Mandatory/Optional   | Parameter Value Generation   |
+===========================+==================+======================+==============================+
| vnf\_id                   | string           | Mandatory            | ONAP                         |
+---------------------------+------------------+----------------------+------------------------------+
| vf\_module\_id            | string           | Mandatory            | ONAP                         |
+---------------------------+------------------+----------------------+------------------------------+
| vnf\_name                 | string           | Mandatory            | ONAP                         |
+---------------------------+------------------+----------------------+------------------------------+
| vf\_module\_name          | string           | Optional             | ONAP                         |
+---------------------------+------------------+----------------------+------------------------------+
| vm\_role                  | string           | Optional             | YAML or Environment File     |
+---------------------------+------------------+----------------------+------------------------------+
+---------------------------+------------------+----------------------+------------------------------+

    Table 4: ONAP Metadata

vnf\_id
~~~~~~~

The vnf\_id parameter is mandatory; it must be included in the Heat
Orchestration Template.

The vnf\_id parameter value will be supplied by ONAP. ONAP generates the
UUID that is the vnf\_id and supplies it to the Heat Orchestration
Template at orchestration time.

The parameter must be declared as type: string

Parameter constraints must not be defined.

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: python

 parameters:
     vnf_id:
         type: string
         description: Unique ID for this VNF instance

vf\_module\_id
~~~~~~~~~~~~~~

The vf\_module\_id parameter is mandatory; it must be included in the
Heat Orchestration Template.

The vf\_module\_id parameter value will be supplied by ONAP. ONAP
generates the UUID that is the vf\_module\_id and supplies it to the
Heat Orchestration Template at orchestration time.

The parameter must be declared as type: string

Parameter constraints must not be defined.

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: python

 parameters:
     vnf_module_id:
         type: string
         description: Unique ID for this VNF module instance

vnf\_name
~~~~~~~~~

The vnf\_name parameter is mandatory; it must be included in the Heat
Orchestration Template.

The vnf\_name parameter value will be generated and/or assigned by ONAP
and supplied to the Heat Orchestration Template by ONAP at orchestration
time.

The parameter must be declared as type: string

Parameter constraints must not be defined.

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: python

 parameters:
     vnf_name:
         type: string
         description: Unique name for this VNF instance

vf\_module\_name
~~~~~~~~~~~~~~~~

The vf\_module\_name parameter is optional; it may be included in the
Heat Orchestration Template.

The vf\_module\_name parameter is the name of the name of the Heat stack
(e.g., <STACK\_NAME>) in the command “Heat stack-create” (e.g., Heat
stack-create [-f <FILE>] [-e <FILE>] <STACK\_NAME>). The <STACK\_NAME>
needs to be specified as part of the orchestration process.

The parameter must be declared as type: string

Parameter constraints must not be defined.

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: python

 parameters:
     vf_module_name:
         type: string
         description: Unique name for this VNF Module instance

vm\_role
~~~~~~~~

The vm\_role parameter is optional; it may be included in the Heat
Orchestration Template.

Any roles tagged to the VMs via metadata will be stored in ONAP’s A&AI
system and available for use by other ONAP components and/or north bound
systems.

The vm\_role values must be either

-  hard-coded into the Heat Orchestration Template or

-  enumerated in the environment file.

Defining the vm\_role as the {vm-type} is a recommended convention

The parameter must be declared as type: string

Parameter constraints must not be defined.

*Example Parameter Definition*

.. code-block:: python

 parameters:
     vm_role:
         type: string
         description: Unique role for this VM

*Example Resource Definition: Hard Coded*

In this example, the {vm-role} is hard coded in the Heat Orchestration
Template.

.. code-block:: python

 resources:
   dns_servers:
     type: OS::Nova::Server
     properties:
       . . . .
       metadata:
         vm_role: lb

*Example Resource Definition: get\_param*

In this example, the {vm-role} is enumerated in the environment file.

.. code-block:: python

 resources:
   dns_servers:
     type: OS::Nova::Server
     properties:
       . . . .
       metadata:
         vm_role: { get_param: vm_role }

Example 
~~~~~~~~

The example below depicts part of a Heat Orchestration Template that
uses the five of the OS::Nova::Server metadata parameter discussed in
this section. The {vm-type} has been defined as lb for load balancer.

.. code-block:: python

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
----------------------------------------

The resource OS::Neutron::Port is for managing Neutron ports (See
https://docs.openstack.org/developer/heat/template_guide/openstack.html#OS::Neutron::Port.)

Introduction
~~~~~~~~~~~~

Four properties of the resource OS::Neutron::Port that must follow the
ONAP parameter naming convention. The four properties are:

1. network

2. fixed\_ips, ip\_address

3. fixed\_ips, subnet\_id

4. allowed\_address\_pairs, ip\_address

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
| network                                | {network-role}\_net\_id                       | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {network-role}\_net\_name                     | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
| fixed\_ips, ip\_address                | {vm-type}\_{network-role}\_ip\_{index}        | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}\_{network-role}\_ips                | comma\_delimited\_list   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}\_{network-role}\_v6\_ip\_{index}    | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}\_{network-role}\_v6\_ips            | comma\_delimited\_list   |
+----------------------------------------+-----------------------------------------------+--------------------------+
| fixed\_ips, subnet                     | {network-role}\_subnet\_id                    | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {network-role}\_v6\_subnet\_id                | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
| allowed\_address\_pairs, ip\_address   | {vm-type}\_{network-role}\_floating\_ip       | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}\_{network-role}\_floating\_v6\_ip   | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}\_{network-role}\_ip\_{index}        | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}\_{network-role}\_ips                | comma\_delimited\_list   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}\_{network-role}\_v6\_ip\_{index}    | string                   |
+----------------------------------------+-----------------------------------------------+--------------------------+
|                                        | {vm-type}\_{network-role}\_v6\_ips            | comma\_delimited\_list   |
+----------------------------------------+-----------------------------------------------+--------------------------+

Table 5: OS::Neutron::Port Resource Property Parameters (External
Networks)

Internal Networks
^^^^^^^^^^^^^^^^^

When the parameter references an internal network

-  the parameter name must contain int\_{network-role}

-  the parameter may be enumerated in the environment file.

+----------------------------------------+----------------------------------------------------+--------------------------+
| Property                               | Parameter Name for Internal Networks               | Parameter Type           |
+========================================+====================================================+==========================+
| network                                | int\_{network-role}\_net\_id                       | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | int\_{network-role}\_net\_name                     | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
| fixed\_ips, ip\_address                | {vm-type}\_int\_{network-role}\_ip\_{index}        | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}\_int\_{network-role}\_ips                | comma\_delimited\_list   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}\_int\_{network-role}\_v6\_ip\_{index}    | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}\_int\_{network-role}\_v6\_ips            | comma\_delimited\_list   |
+----------------------------------------+----------------------------------------------------+--------------------------+
| fixed\_ips, subnet                     | int\_{network-role}\_subnet\_id                    | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | int\_{network-role}\_v6\_subnet\_id                | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
| allowed\_address\_pairs, ip\_address   | {vm-type}\_int\_{network-role}\_floating\_ip       | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}\_int\_{network-role}\_floating\_v6\_ip   | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}\_int\_{network-role}\_ip\_{index}        | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}\_int\_{network-role}\_ips                | comma\_delimited\_list   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}\_int\_{network-role}\_v6\_ip\_{index}    | string                   |
+----------------------------------------+----------------------------------------------------+--------------------------+
|                                        | {vm-type}\_int\_{network-role}\_v6\_ips            | comma\_delimited\_list   |
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

-  {network-role}\_net\_id for the Neutron network ID

-  {network-role}\_net\_name for the network name in OpenStack

The parameter must be declared as type: string

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: python

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

.. code-block:: python

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

-  int\_{network-role}\_net\_id for the Neutron network ID

-  int\_{network-role}\_net\_name for the network name in OpenStack

The parameter must be declared as type: string

The assumption is that internal networks are created in the base module.
The Neutron Network ID will be passed as an output parameter (e.g., ONAP
Base Module Output Parameter) to the incremental modules. In the
incremental modules, it will be defined as input parameter.

*Example Parameter Definition*

.. code-block:: python

 parameters:
     int_{network-role}_net_id:
         type: string
         description: Neutron UUID for the {network-role} network
     int_{network-role}_net_name:
         type: string
         description: Neutron name for the {network-role} network

Property: fixed\_ips, Map Property: subnet\_id
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The property fixed\_ips is used to assign IPs to a port. The Map
Property subnet\_id specifies the subnet the IP is assigned from.

The property fixed\_ips and Map Property subnet\_id must be used if a
Cloud (i.e., DHCP) IP address assignment is being requested and the
Cloud IP address assignment is targeted at a specific subnet when two or
more subnets exist.

The property fixed\_ips and Map Property subnet\_id should not be used
if all IP assignments are fixed, or if the Cloud IP address assignment
does not target a specific subnet or there is only one subnet.

Note that DHCP assignment of IP addresses is also referred to as cloud
assigned IP addresses.

Subnet of an External Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the parameter is referencing a subnet of an “external” network, the
property fixed\_ips and Map Property subnet\_id parameter must adhere to
the following naming convention.

-  {network-role}\_subnet\_id if the subnet is an IPv4 subnet

-  {network-role}\_v6\_subnet\_id if the subnet is an IPv6 subnet

The parameter must be declared as type: string

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: python

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

.. code-block:: python

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

.. code-block:: python

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
the property fixed\_ips and Map Property subnet\_id parameter must
adhere to the following naming convention.

-  int\_{network-role}\_subnet\_id if the subnet is an IPv4 subnet

-  int\_{network-role}\_v6\_subnet\_id if the subnet is an IPv6 subnet

The parameter must be declared as type: string

The assumption is that internal networks are created in the base module.
The Neutron subnet network ID will be passed as an output parameter
(e.g., ONAP Base Module Output Parameter) to the incremental modules. In
the incremental modules, it will be defined as input parameter.

*Example Parameter Definition*

.. code-block:: python

 parameters:
     int_{network-role}_subnet_id:
        type: string
         description: Neutron subnet UUID for the {network-role} network

     int_{network-role}_v6_subnet_id:
         type: string
         description: Neutron subnet UUID for the {network-role} network

Property: fixed\_ips, Map Property: ip\_address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The property fixed\_ips is used to assign IPs to a port. The Map
Property ip\_address specifies the IP address to be assigned to the
port.

The property fixed\_ips and Map Property ip\_address must be used when
statically assigning one or more IP addresses to a port. This is also
referred to as ONAP SDN-C IP address assignment. ONAP’s SDN-C provides
the IP address assignment.

An IP address is assigned to a port on a VM (referenced by {vm-type})
that is connected to an external network (referenced by {network-role})
or internal network (referenced by int\_{network-role}).

When a SDN-C IP assignment is made to a port connected to an external
network, the parameter name must contain {vm-type} and {network-role}.

When a SDN-C IP assignment is made to a port connected to an internal
network, the parameter name must contain {vm-type} and
int\_{network-role}.

IP Address Assignments on External Networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the property fixed\_ips and Map Property ip\_address is used to
assign IP addresses to an external network, the parameter name is
dependent on the parameter type (comma\_delimited\_list or string) and
IP address type (IPv4 or IPv6).

When the parameter for property fixed\_ips and Map Property ip\_address
is declared type: comma\_delimited\_list, the parameter must adhere to
the following naming convention

-  {vm-type}\_{network-role}\_ips for IPv4 address

-  {vm-type}\_{network-role}\_v6\_ips for IPv6 address

Each element in the IP list should be assigned to successive instances
of {vm-type} on {network-role}.

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: python

 parameters:
 
    {vm-type}_{network-role}_ips:
       type: comma_delimited_list
       description: Fixed IPv4 assignments for {vm-type} VMs on the {Network-role} network

    {vm-type}_{network-role}_v6_ips:
       type: comma_delimited_list
       description: Fixed IPv6 assignments for {vm-type} VMs on the {network-role} network

*Example: comma\_delimited\_list parameters for IPv4 and IPv6 Address
Assignments to an external network*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} has been defined as db for database.

.. code-block:: python

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

When the parameter for property fixed\_ips and Map Property ip\_address
is declared type: string, the parameter must adhere to the following
naming convention.

-  {vm-type}\_{network-role}\_ip\_{index} for an IPv4 address

-  {vm-type}\_{network-role}\_v6\_ip\_{index} for an IPv6 address

The value for {index} must start at zero (0) and increment by one.

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: python

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

.. code-block:: python

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

When the property fixed\_ips and Map Property ip\_address is used to
assign IP addresses to an internal network, the parameter name is
dependent on the parameter type (comma\_delimited\_list or string) and
IP address type (IPv4 or IPv6).

When the parameter for property fixed\_ips and Map Property ip\_address
is declared type: comma\_delimited\_list, the parameter must adhere to
the following naming convention

-  {vm-type}\_int\_{network-role}\_ips for IPv4 address

-  {vm-type}\_int\_{network-role}\_v6\_ips for IPv6 address

Each element in the IP list should be assigned to successive instances
of {vm-type} on {network-role}.

The parameter must be enumerated in the Heat environment file. Since an
internal network is local to the VNF, IP addresses can be re-used at
every VNF instance.

*Example Parameter Definition*

.. code-block:: python

 parameters:

    {vm-type}_int_{network-role}_ips:
       type: comma_delimited_list
       description: Fixed IPv4 assignments for {vm-type} VMs on the int_{network-role} network

    {vm-type}_int_{network-role}_v6_ips:
       type: comma_delimited_list
       description: Fixed IPv6 assignments for {vm-type} VMs on the int_{network-role} network

*Example: comma\_delimited\_list parameters for IPv4 and IPv6 Address
Assignments to an internal network*

In this example, the {network-role} has been defined as oam\_int to
represent an oam network internal to the vnf. The role oam\_int was
picked to differentiate from an external oam network with a
{network-role} of oam. The {vm-type} has been defined as db for
database.

.. code-block:: python

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

When the parameter for property fixed\_ips and Map Property ip\_address
is declared type: string, the parameter must adhere to the following
naming convention.

-  {vm-type}\_int\_{network-role}\_ip\_{index} for an IPv4 address

-  {vm-type}\_int\_{network-role}\_v6\_ip\_{index} for an IPv6 address

The value for {index} must start at zero (0) and increment by one.

The parameter must be enumerated in the Heat environment file. Since an
internal network is local to the VNF, IP addresses can be re-used at
every VNF instance.

*Example Parameter Definition*

.. code-block:: python

 parameters:

    {vm-type}_int_{network-role}_ip_{index}:
       type: string
       description: Fixed IPv4 assignment for {vm-type} VM {index} on the{network-role} network

    {vm-type}_int_{network-role}_v6_ip_{index}:
       type: string
       description: Fixed IPv6 assignment for {vm-type} VM {index} on the{network-role} network

*Example: string parameters for IPv4 and IPv6 Address Assignments to an internal network*

In this example, the {network-role} has been defined as oam\_int to
represent an oam network internal to the vnf. The role oam\_int was
picked to differentiate from an external oam network with a
{network-role} of oam. The {vm-type} has been defined as db for
database.

.. code-block:: python

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

Property: allowed\_address\_pairs, Map Property: ip\_address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The property allowed\_address\_pairs in the resource OS::Neutron::Port
allows the user to specify a mac\_address and/or ip\_address that will
pass through a port regardless of subnet. This enables the use of
protocols such as VRRP, which floats an IP address between two instances
to enable fast data plane failover. The map property ip\_address
specifies the IP address.

The allowed\_address\_pairs is an optional property. It is not required.

An ONAP Heat Orchestration Template allows the assignment of one IPv4
address allowed\_address\_pairs and/or one IPv6 address to a {vm-type}
and {network-role}/int\_{network-role} combination.

An ONAP Heat Orchestration Template allows the assignment of one IPv6
address allowed\_address\_pairs and/or one IPv6 address to a {vm-type}
and {network-role}/int\_{network-role} combination.

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
allowed\_address\_pairs and Map Property ip\_address parameter must
adhere to the following naming convention.

-  {vm-type}\_{network-role}\_floating\_ip for an IPv4 address

-  {vm-type}\_{network-role}\_floating\_v6\_ip for an IPv6 address

The parameter must be declared as type: string

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: python

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

.. code-block:: python

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
allowed\_address\_pairs and Map Property ip\_address parameter must
adhere to the following naming convention.

-  {vm-type}\_int\_{network-role}\_floating\_ip for an IPv4 address

-  {vm-type}\_int\_{network-role}\_floating\_v6\_ip for an IPv6 address

The parameter must be declared as type: string

The parameter must be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: python

 parameters:

    {vm-type}_int_{network-role}_floating_ip:
       type: string
       description: VIP for {vm-type} VMs on the int_{network-role} network

    {vm-type}_int_{network-role}_floating_v6_ip:
       type: string
       description: VIP for {vm-type} VMs on the int_{network-role} network

Multiple allowed\_address\_pairs for a {vm-type} / {network-role} combination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The parameter {vm-type}\_{network-role}\_floating\_ip provides only one
allowed address pair IPv4 address per {vm-type} and {network-role} pair.

The parameter {vm-type}\_{network-role}\_floating\_v6\_ip provides only
one allowed address pair IPv6 address per {vm-type} and {network-role}
pair.

If there is a need for multiple allowed address pair IPs for a given
{vm-type} and {network-role} combination within a VNF, then the
parameter names defined for the property fixed\_ips and Map Property
ip\_address should be used with the allowed\_address\_pairs property.
The examples below illustrate this.

*Example: A VNF has four load balancers. Each pair has a unique VIP.*

In this example, there are two administrative VM pairs. Each pair has
one VIP. The {network-role} has been defined as oam to represent an oam
network and the {vm-type} has been defined as admin for an
administrative VM.

Pair 1: Resources admin\_0\_port\_0 and admin\_1\_port\_0 share a unique
VIP, [admin\_oam\_ips,2]

Pair 2: Resources admin\_2\_port\_0 and admin\_3\_port\_0 share a unique
VIP, [admin\_oam\_ips,5]

.. code-block:: python

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

.. code-block:: python

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

ONAP SDN-C Assignment of allowed\_address\_pair IP Addresses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following items must be taken into consideration when designing Heat
Orchestration Templates that expect ONAP’s SDN-C to assign
allowed\_address\_pair IP addresses via automation.

The VMs must be of the same {vm-type}.

The VMs must be created in the same module (base or incremental).

Resource Property “name”
------------------------

The parameter naming convention of the property name for the resource
OS::Nova::Server has been defined in `Resource:  OS::Nova::Server – Metadata Parameters`_.

This section provides the requirements how the property name for non
OS::Nova::Server resources must be defined when the property is used.
Not all resources require the property name (e.g., it is optional) and
some resources do not support the property.

When the property name for a non OS::Nova::Server resources is defined
in a Heat Orchestration Template, the intrinsic function str\_replace
must be used in conjunction with the ONAP supplied metadata parameter
vnf\_name to generate a unique value. This prevents the enumeration of a
unique value for the property name in a per instance environment file.

Note that

-  In most cases, only the use of the metadata value vnf\_name is
   required to create a unique property name

-  the Heat Orchestration Template pseudo parameter 'OS::stack\_name’
   may also be used in the str\_replace construct to generate a unique
   name when the vnf\_name does not provide uniqueness

*Example: Property* name *for resource* OS::Neutron::SecurityGroup

.. code-block:: python

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

.. code-block:: python

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

- “ ! $ ‘ ( ) = ~ ^ \| @ \` { } [ ] > , . \_

ONAP Output Parameter Names
---------------------------

ONAP defines three types of Output Parameters as detailed in `Output Parameters`_.

ONAP Base Module Output Parameters: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP Base Module Output Parameters do not have an explicit naming
convention. The parameter name must contain {vm-type} and {network-role}
when appropriate.

ONAP Volume Template Output Parameters: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

-  oam\_management\_v4\_address

-  oam\_management\_v6\_address

*Notes*:

-  The use of this output parameters are optional.

-  The Management IP Address should be defined only once per VNF, so it
   must only appear in one Module template

-  If a fixed IP for the admin VM is passed as an input parameter, it
   may be echoed in the output parameters. In this case, a IPv4 and/or
   IPv6 parameter must be defined in the parameter section of the YAML
   Heat template. The parameter maybe named oam\_management\_v4\_address
   and/or oam\_management\_v6\_address or may be named differently.

-  If the IP for the admin VM is obtained via DHCP, it may be obtained
   from the resource attributes. In this case,
   oam\_management\_v4\_address and/or oam\_management\_v6\_address must
   not be defined in the parameter section of the YAML Heat template.

*Example: SDN-C Assigned IP Address echoed as*
oam\_management\_v4\_address

.. code-block:: python

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
oam\_management\_v4\_address

.. code-block:: python

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
----------------------------

ONAP requires the parameter names of certain Contrail Resources to
follow specific naming conventions. This section provides these
requirements.

Contrail Network Parameters 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Contrail based resources may require references to a Contrail network
using the network FQDN.

External Networks
^^^^^^^^^^^^^^^^^

When the parameter associated with the Contrail Network is referencing
an “external” network, the parameter must adhere to the following naming
convention in the Heat Orchestration Template

-  {network-role}\_net\_fqdn

The parameter must be declared as type: string

The parameter must not be enumerated in the Heat environment file.

*Example: Parameter declaration*

.. code-block:: python

 parameters:
    {network-role}_net_fqdn:
       type: string
       description: Contrail FQDN for the {network-role} network

*Example: Contrail Resource OS::ContrailV2::VirtualMachineInterface
Reference to a Network FQDN.*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} has been defined as fw for firewall.
The Contrail resource OS::ContrailV2::VirtualMachineInterface property
virtual\_network\_refs references a contrail network FQDN.

.. code-block:: python

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
interface\_route\_table\_routes, map property
interface\_route\_table\_routes\_route\_prefix is an ONAP Orchestration
Parameter.

The parameters must be named {vm-type}\_{network-role}\_route\_prefixes
in the Heat Orchestration Template.

The parameter must be declared as type: json

The parameter supports IP addresses in the format:

1. Host IP Address (e.g., 10.10.10.10)

2. CIDR Notation format (e.g., 10.0.0.0/28)

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: python

 parameters:
    {vm-type}_{network-role}_route_prefixes:
       type: json
       description: JSON list of Contrail Interface Route Table route prefixes

*Example:*

.. code-block:: python

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
-------------------------------------

Contrail Heat resource properties will use, when appropriate, the same
naming convention as OpenStack Heat resources. For example, the resource
OS::ContrailV2::InstanceIp has two properties that the parameter naming
convention is identical to properties in OS::Neutron::Port.

*Example: Contrail Resource OS::ContrailV2::InstanceIp, Property
instance\_ip\_address*

The property instance\_ip\_address uses the same parameter naming
convention as the property fixed\_ips and Map Property ip\_address in
OS::Neutron::Port. The resource is assigning an ONAP SDN-C Assigned IP
Address. The {network-role} has been defined as oam\_protected to
represent an oam protected network and the {vm-type} has been defined as
fw for firewall.

.. code-block:: python

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
subnet\_uuid*

The property instance\_ip\_address uses the same parameter naming
convention as the property fixed\_ips and Map Property subnet\_id in
OS::Neutron::Port. The resource is assigning a Cloud Assigned IP
Address. The {network-role} has been defined as “oam\_protected” to
represent an oam protected network and the {vm-type} has been defined as
“fw” for firewall.

.. code-block:: python

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
-----------------------

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

A VNF has a Cinder volume module, named incremental\_volume.yaml, that
creates an independent Cinder volume for a VM in the module
incremental.yaml. The incremental\_volume.yaml defines a parameter in
the output section, lb\_volume\_id\_0 which is the UUID of the cinder
volume. lb\_volume\_id\_0 is defined as a parameter in incremental.yaml.
ONAP captures the UUID value of lb\_volume\_id\_0 from the volume module
output statement and provides the value to the incremental module.

Note that the example below is not a complete Heat Orchestration
Template. The {vm-type} has been defined as “lb” for load balancer

incremental\_volume.yaml

.. code-block:: python

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

.. code-block:: python

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
---------------------------------

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
----------------------------------

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
---------------------------------------------------------------------

When ONAP is instantiating the Heat Orchestration Template, certain
parameter must not be enumerated in the environment file. This document
provides the details of what parameters should not be enumerated.

If the Heat Orchestration Template is to be instantiated from the
OpenStack Command Line Interface (CLI) using the command “heat
stack-create”, all parameters must be enumerated in the environment
file.

Heat Template Constructs
------------------------

Nested Heat Templates
---------------------

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
resource\_registry in the environment file is not supported and must not
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
   get\_attribute targets against the “parent” resource.

Nested Heat Template Example: Static
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

incremental.yaml

.. code-block:: python

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

.. code-block:: python

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

.. code-block:: python

 type: OS::Heat::ResourceGroup
   resource_def:
     type: my_nested_vm_template.yaml
     properties:
       name: {get_param: [vm_name_list, %index%]}

Although this appears to use the nth entry of the vm\_name\_list list
for the nth element of the ResourceGroup, it will in fact result in a
Heat exception. When parameters are provided as a list (one for each
element of a ResourceGroup), you must pass the complete parameter to the
nested template along with the current index as separate parameters.

Below is an example of an **acceptable** Heat Syntax for a
ResourceGroup:

.. code-block:: python

 type: OS::Heat::ResourceGroup
   resource_def:
     type: my_nested_vm_template.yaml
     properties:
       names: {get_param: vm_name_list}
       index: %index%

You can then reference within the nested template as:

{ get\_param: [names, {get\_param: index} ] }

ResourceGroup Property count
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP requires that the OS::Heat::ResourceGroup property count be defined
(even if the value is one) and that the value must be enumerated in the
environment file. This is required for ONAP to build the TOSCA model for
the VNF.

.. code-block:: python

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

The resource OS::Heat::ResourceGroup and the property availability\_zone
has been an “issue” with a few VNFs since ONAP only supports
availability\_zone as a string parameter and not a
comma\_delimited\_list. This makes it difficult to use a ResourceGroup
to create Virtual Machines in more than one availability zone.

There are numerous solutions to this issue. Below are two suggested
usage patterns.

**Option 1:** create a CDL in the OS::Heat::ResourceGroup. In the
resource type: OS::Heat::ResourceGroup, create a comma\_delimited\_list
availability\_zones by using the intrinsic function list\_join.

.. code-block:: python

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

.. code-block:: python

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
-------------------

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

Heat Files Support (get\_file)
------------------------------

Heat Templates may contain the inclusion of text files into Heat
templates via the Heat get\_file directive. This may be used, for
example, to define a common “user-data” script, or to inject files into
a VM on startup via the “personality” property.

Support for Heat Files is subject to the following limitations:

-  The get\_files targets must be referenced in Heat templates by file
   name, and the corresponding files should be delivered to ONAP along
   with the Heat templates.

   -  URL-based file retrieval must not be used; it is not supported.

-  The included files must have unique file names within the scope of
   the VNF.

-  ONAP does not support a directory hierarchy for included files.

   -  All files must be in a single, flat directory per VNF.

-  Included files may be used by all Modules within a given VNF.

-  get\_file directives may be used in both non-nested and nested
   templates

Key Pairs
---------

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

.. code-block:: python

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
---------------

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
--------------------------------

Anti-affinity or affinity rules are supported using normal OpenStack
OS::Nova::ServerGroup resources. Separate ServerGroups are typically
created for each VM type to prevent them from residing on the same host,
but they can be applied to multiple VM types to extend the
affinity/anti-affinity across related VM types as well.

*Example:*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} have been defined as lb for load
balancer and db for database.

.. code-block:: python

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
------------------------------

For cases where synchronization is required in the orchestration of Heat
resources, two approaches are recommended:

-  Standard Heat depends\_on property for resources

   -  Assures that one resource completes before the dependent resource
      is orchestrated.

   -  Definition of completeness to OpenStack may not be sufficient
      (e.g., a VM is considered complete by OpenStack when it is ready
      to be booted, not when the application is up and running).

-  Use of Heat Notifications

   -  Create OS::Heat::WaitCondition and OS::Heat::WaitConditionHandle
      resources.

   -  Pre-requisite resources issue *wc\_notify* commands in user\_data.

   -  Dependent resource define depends\_on in the
      OS::Heat::WaitCondition resource.

*Example: “depends\_on” case*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} has been defined as oam to represent an
oam server.

.. code-block:: python

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
-----------------

VNF/VM parameters may include availability zone IDs for VNFs that
require high availability.

The Heat must comply with the following requirements to specific
availability zone IDs:

-  The Heat template should spread Nova and Cinder resources across the
   availability zones as desired

Post Orchestration & VNF Configuration
--------------------------------------

Heat templates should contain a minimum amount of post-orchestration
configuration data. For instance, *do not* embed complex user-data
scripts in the template with large numbers of configuration parameters
to the Heat template.

-  VNFs may provide configuration APIs for use after VNF creation. Such
   APIs will be invoked via application and/or SDN controllers.

*Note:* It is important to follow this convention to the extent possible
even in the short-term as of the long-term direction.

d. VNFM Driver Develop Steps
==============================

Aid to help the VNF vendor to fasten the integration with the NFVO via
Special VNFM, the OpenO provides the documents. In this charter, the
develop steps for VNF vendors will be introduced.

First, using the VNF SDK tools to design the VNF with TOSCA model and
output the VNF TOSCA package. The VNF package can be validated, and
tested.

Second, the VNF vendor should provide SVNFM Driver in the OpenO, which
is a micro service and in duty of translation interface from NFVO to
SVNFM. The interface of NFVO is aligned to the ETSI IFA interfaces and
can be gotten in the charter 5.5. The interface of SVNFM is provided by
the VNF vendor self.

e. Create SVNFM Adaptor Mircoservice
=======================================

Some vnfs are managed by special vnfm, before add svnfm to openo, a
svnfm adaptor must be added to openo to adapter the interface of nfvo
and svnfm.

A svnfm adaptor is a micro service with unique name and an appointed
port, when started up, it must be auto registered to MSB(Micro server
bus),following describes an example rest of register to MSB:

POST /openoapi/microservices/v1/services

    {

    "serviceName": "catalog",

    "version": "v1",

    "url": "/openoapi/catalog/v1",

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