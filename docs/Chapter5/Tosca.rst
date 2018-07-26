.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

TOSCA YAML
----------


Introduction
^^^^^^^^^^^^

This reference document is the VNF TOSCA Template Requirements for
ONAP, which provides recommendations and standards for building VNF
TOSCA templates compatible with ONAP initial implementations of
Network Cloud. It has the following features:

1. VNF TOSCA template designer supports GUI and CLI.

2. VNF TOSCA template is aligned to the newest TOSCA protocol, “Working
   Draft 04-Revision 06”.

3. VNF TOSCA template supports HPA features, such as NUMA, Hyper
   Threading, SRIOV， etc.

Intended Audience
^^^^^^^^^^^^^^^^^^

This document is intended for persons developing VNF TOSCA templates
that will be orchestrated by ONAP.

Scope
^^^^^^^^^^^^^^^^

ONAP implementations of Network Cloud supports TOSCA Templates, also
referred to as TOSCA in this document.

ONAP requires the TOSCA Templates to follow a specific format. This
document provides the mandatory, recommended, and optional requirements
associated with this format.

Overview
^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^

TOSCA templates supported by ONAP must follow the requirements
enumerated in this section.

TOSCA Introduction
^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describing TOSCA modeling principles and data model for
NFV, which shall be based on [TOSCA-1.0] and [TOSCA-Simple-Profile-YAML
V1.0], or new type based on ETSI NFV requirements, etc.

VNF Descriptor Template
^^^^^^^^^^^^^^^^^^^^^^^^^

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
specification [TOSCA-Simple-Profile-NFV-v1.0] for NFV VNFD with aggreed
changes from ETSI SOL001 draft.

+---------------------+------------------------------------+-----------------+
| **ETSI NFV Element**| **TOSCA VNFD**                     | **Derived from**|
|                     |                                    |                 |
| **[IFA011]**        | **[TOSCA-Simple-Profile-NFV-v1.0]**|                 |
+=====================+====================================+=================+
| VNF                 | tosca.nodes.nfv.VNF                | tosca.nodes.Root|
+---------------------+------------------------------------+-----------------+
| Cpd (Connection     | tosca.nodes.nfv.Cp                 | tosca.nodes.Root|
| Point)              | tosca.nodes.nfv.Cp                 | tosca.nodes.Root|
+---------------------+------------------------------------+-----------------+
| VduCpd (internal    | tosca.nodes.nfv.VduCp              | tosca.nodes.\   |
| connection point)   |                                    | nfv.Cp          |
+---------------------+------------------------------------+-----------------+
| VnfVirtualLinkDesc  | tosca.nodes.nfv.VnfVirtualLink     | tosca.nodes.Root|
| (Virtual Link)      |                                    |                 |
+---------------------+------------------------------------+-----------------+
| VDU Virtual Storage | tosca.nodes.nfv.VDU.VirtualStorage | tosca.nodes.Root|
+---------------------+------------------------------------+-----------------+
| VDU Virtual Compute | tosca.nodes.nfv.VDU.Compute        | tosca.nodes.Root|
+---------------------+------------------------------------+-----------------+
| Software Image      |                                    |                 |
+---------------------+------------------------------------+-----------------+
| Deployment Flavour  |                                    |                 |
+---------------------+------------------------------------+-----------------+
| Scaling Aspect      |                                    |                 |
+---------------------+------------------------------------+-----------------+
| Element Group       |                                    |                 |
+---------------------+------------------------------------+-----------------+
| Instantiation       |                                    |                 |
| Level               |                                    |                 |
+---------------------+------------------------------------+-----------------+


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


HPA Requirements
^^^^^^^^^^^^^^^^^^

1. SR-IOV Passthrought

Definitions of SRIOV\_Port are necessary if VDU supports SR-IOV. Here is
an example.

.. code-block:: yaml

  node\_templates:

  vdu\_vNat:

  SRIOV\_Port:

  attributes:

  tosca\_name: SRIOV\_Port

  properties:

  virtual\_network\_interface\_requirements:

  - name: sriov

  support\_mandatory: false

  description: sriov

  requirement:

  SRIOV: true

  role: root

  description: sriov port

  layer\_protocol: ipv4

  requirements:

  - virtual\_binding:

  capability: virtual\_binding

  node: vdu\_vNat

  relationship:

  type: tosca.relationships.nfv.VirtualBindsTo

  - virtual\_link:

  node: tosca.nodes.Root

  type: tosca.nodes.nfv.VduCpd

  substitution\_mappings:

  requirements:

  sriov\_plane:

  - SRIOV\_Port

  - virtual\_link

  node\_type: tosca.nodes.nfv.VNF.vOpenNAT


2. Hugepages

Definitions of mem\_page\_size as one property shall be added to
Properties and set the value to large if one VDU node supports
huagepages. Here is an example.

.. code-block:: yaml

  node\_templates:

  vdu\_vNat:

  Hugepages:

  attributes:

  tosca\_name: Huge\_pages\_demo

  properties:

  mem\_page\_size:large


3. NUMA (CPU/Mem)

Likewise, we shall add definitions of numa to
requested\_additional\_capabilities if we wand VUD nodes to support
NUMA. Here is an example.

.. code-block:: yaml

  topology\_template:

  node\_templates:

  vdu\_vNat:

  capabilities:

  virtual\_compute:

  properties:

  virtual\_memory:

  numa\_enabled: true

  virtual\_mem\_size: 2 GB

  requested\_additional\_capabilities:

  numa:

  support\_mandatory: true

  requested\_additional\_capability\_name: numa

  target\_performance\_parameters:

  hw:numa\_nodes: "2"

  hw:numa\_cpus.0: "0,1"

  hw:numa\_mem.0: "1024"

  hw:numa\_cpus.1: "2,3,4,5"

  hw:numa\_mem.1: "1024"


4. Hyper-Theading

Definitions of Hyper-Theading are necessary as one of
requested\_additional\_capabilities of one VUD node if that node
supports Hyper-Theading. Here is an example.

.. code-block:: yaml

  topology\_template:

  node\_templates:

  vdu\_vNat:

  capabilities:

  virtual\_compute:

  properties:

  virtual\_memory:

  numa\_enabled: true

  virtual\_mem\_size: 2 GB

  requested\_additional\_capabilities:

  hyper\_threading:

  support\_mandatory: true

  requested\_additional\_capability\_name: hyper\_threading

  target\_performance\_parameters:

  hw:cpu\_sockets : "2"

  hw:cpu\_threads : "2"

  hw:cpu\_cores : "2"

  hw:cpu\_threads\_policy: "isolate"


5. OVS+DPDK

Definitions of ovs\_dpdk are necessary as one of
requested\_additional\_capabilities of one VUD node if that node
supports dpdk. Here is an example.

.. code-block:: yaml

  topology\_template:

  node\_templates:

  vdu\_vNat:

  capabilities:

  virtual\_compute:

  properties:

  virtual\_memory:

  numa\_enabled: true

  virtual\_mem\_size: 2 GB

  requested\_additional\_capabilities:

  ovs\_dpdk:

  support\_mandatory: true

  requested\_additional\_capability\_name: ovs\_dpdk

  target\_performance\_parameters:

  sw:ovs\_dpdk: "true"


NFV TOSCA Type Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tosca.capabilites.nfv.VirtualCompute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This capability is used with the properties specified in ETSI SOL001 draft.

tosca.nodes.nfv.VDU.Compute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
++++++++++++

None


Capabilities
++++++++++++++

+------------+--------------------+------------+------------------------------+
| Name       | Type               | Constraints| Description                  |
+============+====================+============+==============================+
| virtual\   | tosca.\            |            | Describes virtual compute    |
| _compute   | capabilities.nfv.\ |            | resources capabilities.      |
|            | VirtualCompute     |            |                              |
+------------+--------------------+------------+------------------------------+
| monitoring\| tosca.\            | None       | Monitoring parameter, which  |
| _parameter | capabilities.nfv.\ |            | can be tracked for a VNFC    |
|            | Metric             |            | based on this VDU            |
|            |                    |            |                              |
|            |                    |            | Examples include:            |
|            |                    |            | memory-consumption,          |
|            |                    |            | CPU-utilisation,             |
|            |                    |            | bandwidth-consumption, VNFC  |
|            |                    |            | downtime, etc.               |
+------------+--------------------+------------+------------------------------+
| Virtual\   | tosca.\            |            | Defines ability of           |
| _binding   | capabilities.nfv.\ |            | VirtualBindable              |
|            | VirtualBindable    |            |                              |
|            |                    |            |                              |
|            | editor note: need  |            |                              |
|            | to create a        |            |                              |
|            | capability type    |            |                              |
+------------+--------------------+------------+------------------------------+



Definition
++++++++++++

.. code-block:: yaml

  tosca.nodes.nfv.VDU.Compute:

  derived\_from: tosca.nodes.Compute

  properties:

  name:

  type: string

  required: true

  description:

  type: string

  required: true

  boot\_order:

  type: list # explicit index (boot index) not necessary, contrary to IFA011

  entry\_schema:

  type: string

  required: false

  nfvi\_constraints:

  type: list

  entry\_schema:

  type: string

  required: false

  configurable\_properties:

  type: map

  entry\_schema:

  type: tosca.datatypes.nfv.VnfcConfigurableProperties

  required: true

  attributes:

  private\_address:

  status: deprecated

  public\_address:

  status: deprecated

  networks:

  status: deprecated

  ports:

  status: deprecated

  capabilities:

  virtual\_compute:

  type: tosca.capabilities.nfv.VirtualCompute

  virtual\_binding:

  type: tosca.capabilities.nfv.VirtualBindable

  #monitoring\_parameter:

  # modeled as ad hoc (named) capabilities in VDU node template

  # for example:

  #capabilities:

  # cpu\_load: tosca.capabilities.nfv.Metric

  # memory\_usage: tosca.capabilities.nfv.Metric

  host: #Editor note: FFS. How this capabilities should be used in NFV Profile|

  type: *tosca.capabilities.Container*

  valid\_source\_types:
  [*tosca.nodes.SoftwareComponent*]

  occurrences: [0,UNBOUNDED]

  endpoint:

  occurrences: [0,0]

  os:

  occurrences: [0,0]

  scalable:
  #Editor note: FFS. How this capabilities should be used in NFV Profile

  type: *tosca.capabilities.Scalable*

  binding:

  occurrences: [0,UNBOUND]

  requirements:

  - virtual\_storage:

  capability: tosca.capabilities.nfv.VirtualStorage

  relationship: tosca.relationships.nfv.VDU.AttachedTo

  node: tosca.nodes.nfv.VDU.VirtualStorage

  occurences: [ 0, UNBOUNDED ]

  - local\_storage: #For NFV Profile, this requirement is deprecated.

  occurrences: [0,0]

  artifacts:

  - sw\_image:

  file:

  type: tosca.artifacts.nfv.SwImage


Artifact
++++++++++

Note: currently not supported.

+--------+---------+----------------+------------+------------------------+
| Name   | Required| Type           | Constraints| Description            |
+========+=========+================+============+========================+
| SwImage| Yes     | tosca.\        |            | Describes the software |
|        |         | artifacts.nfv.\|            | image which is directly|
|        |         | SwImage        |            | realizing this virtual |
|        |         |                |            | storage                |
+--------+---------+----------------+------------+------------------------+


|image2|



tosca.nodes.nfv.VDU.VirtualStorage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
++++++++++++

+-----------------+---------+----------+------------+-------------------------+
| Name            | Required| Type     | Constraints| Description             |
+=================+=========+==========+============+=========================+
| name            | yes     | string   |            | Name of this software   |
|                 |         |          |            | image                   |
+-----------------+---------+----------+------------+-------------------------+
| version         | yes     | string   |            | Version of this software|
|                 |         |          |            | image                   |
+-----------------+---------+----------+------------+-------------------------+
| checksum        | yes     | string   |            | Checksum of the software|
|                 |         |          |            | image file              |
+-----------------+---------+----------+------------+-------------------------+
| container\      | yes     | string   |            | The container format    |
| _format         |         |          |            | describes the container |
|                 |         |          |            | file format in which    |
|                 |         |          |            | software image is       |
|                 |         |          |            | provided.               |
+-----------------+---------+----------+------------+-------------------------+
| disk\_format    | yes     | string   |            | The disk format of a    |
|                 |         |          |            | software image is the   |
|                 |         |          |            | format of the underlying|
|                 |         |          |            | disk image              |
+-----------------+---------+----------+------------+-------------------------+
| min\_disk       | yes     | scalar-\ |            | The minimal disk size   |
|                 |         | unit.size|            | requirement for this    |
|                 |         |          |            | software image.         |
+-----------------+---------+----------+------------+-------------------------+
| min\_ram        | no      | scalar-\ |            | The minimal RAM         |
|                 |         | unit.size|            | requirement for this    |
|                 |         |          |            | software image.         |
+-----------------+---------+----------+------------+-------------------------+
| Size            | yes     | scalar-\ |            | The size of this        |
|                 |         | unit.size|            | software image          |
+-----------------+---------+----------+------------+-------------------------+
| sw\_image       | yes     | string   |            | A reference to the      |
|                 |         |          |            | actual software image   |
|                 |         |          |            | within VNF Package, or  |
|                 |         |          |            | url.                    |
+-----------------+---------+----------+------------+-------------------------+
| operating\      | no      | string   |            | Identifies the operating|
| _system         |         |          |            | system used in the      |
|                 |         |          |            | software image.         |
+-----------------+---------+----------+------------+-------------------------+
| supported\      | no      | list     |            | Identifies the          |
| _virtualization\|         |          |            | virtualization          |
| _enviroment     |         |          |            | environments (e.g.      |
|                 |         |          |            | hypervisor) compatible  |
|                 |         |          |            | with this software image|
+-----------------+---------+----------+------------+-------------------------+


Definition
+++++++++++

.. code-block:: yaml

  tosca.artifacts.nfv.SwImage:

    derived\_from: tosca.artifacts.Deployment.Image

    properties or metadata:

      #id:

        # node name

      name:

        type: string

  required: true

      version:

        type: string

  required: true

      checksum:

        type: string

  required: true

      container\_format:

        type: string

  required: true

      disk\_format:

        type: string

  required: true

      min\_disk:

        type: scalar-unit.size # Number

  required: true

      min\_ram:

        type: scalar-unit.size # Number

  required: false

      size:

        type: scalar-unit.size # Number

  required: true

      sw\_image:

        type: string

  required: true

      operating\_system:

        type: string

  required: false

      supported\_virtualisation\_environments:

        type: list

        entry\_schema:

          type: string

  required: false


.. |image1| image:: ../Image1.png
   :width: 5.76806in
   :height: 4.67161in

.. |image2| image:: ../Image2.png
   :width: 5.40486in
   :height: 2.46042in
