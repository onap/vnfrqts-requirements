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


TOSCA VNF Descriptor
--------------------

General
^^^^^^^

.. req::
    :id: R-35854
    :target: VNF
    :keyword: MUST
    :introduced: casablanca

    The VNF Descriptor (VNFD) provided by VNF vendor **MUST** comply with
    TOSCA/YAML based Service template for VNF descriptor specified in
    ETSI NFV-SOL001.

    **Note**: As the ETSI NFV-SOL001 is work in progress the below tables
    summarizes the TOSCA definitions agreed to be part of current version
    of NFV profile and that VNFD MUST comply with in ONAP Release 2+
    Requirements.


.. req::
    :id: R-65486
    :target: VNF
    :keyword: MUST
    :introduced: casablanca
    :updated: dublin

    The VNFD **MUST** comply with ETSI GS NFV-SOL001 specification endorsing
    the above mentioned NFV Profile and maintaining the gaps with the
    requirements specified in ETSI GS NFV-IFA011 standard.


.. req::
    :id: R-17852
    :target: VNF
    :keyword: MAY
    :introduced: casablanca

    The VNFD **MAY** include TOSCA/YAML definitions that are not part of
    NFV Profile. If provided, these definitions MUST comply with TOSCA
    Simple Profile in YAML v.1.2.

.. req::
    :id: R-46527
    :target: VNF
    :keyword: MUST
    :introduced: casablanca

    A VNFD is a deployment template which describes a VNF in terms of
    deployment and operational behavior requirements. It contains
    virtualized resources (nodes) requirements as well as connectivity
    and interfaces requirements and **MUST** comply with info elements
    specified in ETSI GS NFV-IFA 011. The main parts of the VNFD are
    the following:

      - VNF topology: it is modeled in a cloud agnostic way using virtualized
        containers and their connectivity. Virtual Deployment Units (VDU)
        describe the capabilities of the virtualized containers, such as
        virtual CPU, RAM, disks; their connectivity is modeled with VDU
        Connection Point Descriptors (VduCpd), Virtual Link Descriptors
        (VnfVld) and VNF External Connection Point Descriptors
        (VnfExternalCpd);

      - VNF deployment aspects: they are described in one or more
        deployment flavours, including configurable parameters, instantiation
        levels, placement constraints (affinity / antiaffinity), minimum and
        maximum VDU instance numbers. Horizontal scaling is modeled with
        scaling aspects and the respective scaling levels in the deployment
        flavours;

    **Note**: The deployment aspects (deployment flavour etc.) are postponed
    for future ONAP releases.

      - VNF lifecycle management (LCM) operations: describes the LCM operations
        supported per deployment flavour, and their input parameters;
        Note, thatthe actual LCM implementation resides in a different layer,
        namely referring to additional template artifacts.

.. req::
    :id: R-15837
    :target: VNF
    :keyword: MUST
    :introduced: casablanca

    The following table defines the major TOSCA  Types specified in
    ETSI NFV-SOL001 standard draft. The VNFD provided by a VNF vendor
    **MUST** comply with the below definitions:


.. csv-table:: **TOSCA Definition**
   :file: TOSCA_descriptor.csv
   :header-rows: 1
   :align: center
   :widths: auto

Data Types
^^^^^^^^^^

.. req::
    :id: R-54356
    :target: VNF
    :keyword: MUST
    :introduced: casablanca

    The below table includes the data types used by NFV node and is based
    on TOSCA/YAML constructs specified in draft GS NFV-SOL 001. The node
    data definitions/attributes used in VNFD **MUST** comply with the below
    table.

.. csv-table:: **NFV Data Types**
   :file: NFV_data_type.csv
   :header-rows: 1
   :align: center
   :widths: auto

.. req::
    :id: R-54876
    :target: VNF
    :keyword: MUST
    :introduced: casablanca

    The below table describes the data types used for LCM configuration
    and is based on TOSCA constructs specified in draft GS NFV-SOL 001.
    The LCM configuration data elements used in VNFD **MUST** comply
    with the below table.

.. csv-table:: **LCM Configuration**
   :file: LCM_config.csv
   :header-rows: 1
   :align: center
   :widths: auto

Artifact Types
^^^^^^^^^^^^^^

No artifact type is currently supported in ONAP.

Capability Types
^^^^^^^^^^^^^^^^

.. req::
    :id: R-67895
    :target: VNF
    :keyword: MUST
    :introduced: casablanca

    The VNFD provided by VNF vendor may use the below described TOSCA
    capabilities. An on-boarding entity (ONAP SDC) **MUST** support them.

      **tosca.capabilities.nfv.VirtualBindable**

        A node type that includes the VirtualBindable capability indicates
        that it can be pointed by **tosca.relationships.nfv.VirtualBindsTo**
        relationship type.

      **tosca.capabilities.nfv.VirtualLinkable**

        A node type that includes the VirtualLinkable capability indicates
        that it can be pointed by **tosca.relationships.nfv.VirtualLinksTo**
        relationship.

      **tosca.capabilities.nfv.ExtVirtualLinkable**

        A node type that includes the ExtVirtualLinkable capability
        indicates that it can be pointed by
        **tosca.relationships.nfv.VirtualLinksTo** relationship.

      **Note**: This capability type is used in Casablanca how it does
      not exist in the last SOL001 draft

      **tosca.capabilities.nfv.VirtualCompute** and
      **tosca.capabilities.nfv.VirtualStorage** includes flavours of VDU


Relationship Types
^^^^^^^^^^^^^^^^^^

.. req::
    :id: R-95321
    :target: VNF
    :keyword: MUST
    :introduced: casablanca

    The VNFD provided by VNF vendor may use the below described TOSCA
    relationships. An on-boarding entity (ONAP SDC) **MUST** support them.

      **tosca.relationships.nfv.VirtualBindsTo**

        This relationship type represents an association relationship between
        VDU and CP node types.

      **tosca.relationships.nfv.VirtualLinksTo**

        This relationship type represents an association relationship between
        the VduCpd's and VirtualLinkDesc node types.


Interface Types
^^^^^^^^^^^^^^^

.. req::
    :id: R-32155
    :target: VNF
    :keyword: MUST
    :introduced: casablanca

    The VNFD provided by VNF vendor may use the below described TOSCA
    interface types. An on-boarding entity (ONAP SDC) **MUST** support them.

      **tosca.interfaces.nfv.vnf.lifecycle.Nfv** supports LCM operations

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

