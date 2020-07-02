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


TOSCA model
-----------

Table D1. ONAP Resource DM TOSCA/YAML constructs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Standard TOSCA/YAML definitions agreed by VNF SDK Modeling team to be used by
VNF vendors to create a standard VNF descriptor.

All definitions are summarized in the table below based on the agreed ONAP
Resource DM TOSCA/YAML constructs for Beijing. Their syntax is specified in
ETSI GS NFV-SOL001 stable draft for VNF-D.

+------------+------------------------------+---------------------------------+
| Requirement| Resource IM Info Elements    | TOSCA Constructs as per SOL001  |
| Number     |                              |                                 |
+============+==============================+=================================+
| R-02454    | VNFD.vnfSoftwareVersion      | For VDU.Compute -               |
|            |                              | tosca.artifacts.nfv.SwImage     |
|            |                              |                                 |
|            | SwImageDesc.Version          | For Virtual Storage -           |
|            |                              | tosca.artifacts.Deployment.Image|
+------------+------------------------------+---------------------------------+
| R-03070    | vnfExtCpd's with virtual     | tosca.nodes.nfv.VnfExtCp with a |
|            | NetworkInterfaceRequirements | property tosca.datatypes.nfv.\  |
|            | (vNIC)                       | VirtualNetworkInterface\        |
|            |                              | Requirements                    |
+------------+------------------------------+---------------------------------+
| R-09467    | VDU.Compute descriptor       | tosca.nodes.nfv.Vdu.Compute     |
+------------+------------------------------+---------------------------------+
| R-16065    | VDU.Compute. Configurable    | tosca.datatypes.nfv.Vnfc        |
|            | Properties                   | ConfigurableProperties          |
+------------+------------------------------+---------------------------------+
| R-30654    | VNFD.lifeCycleManagement     | Interface construct tosca.\     |
|            | Script - IFA011 LifeCycle\   | interfaces.nfv.vnf.lifecycle.Nfv|
|            | ManagementScript             | with a list of standard LCM     |
|            |                              | operations                      |
+------------+------------------------------+---------------------------------+
| R-35851    | CPD: VduCp, VnfExtCp,        | tosca.nodes.nfv.VduCp, tosca.\  |
|            | VnfVirtualLinkDesc, QoS      | nodes.nfv.VnfVirtualLink,       |
|            | Monitoring info element  -   | tosca.nodes.nfv.VnfExtCp        |
|            | TBD                          |                                 |
+------------+------------------------------+---------------------------------+
| R-41215    | VNFD/VDU Profile and scaling | tosca.datatypes.nfv.VduProfile  |
|            | aspect                       | and tosca.datatypes.nfv.\       |
|            |                              | ScalingAspect                   |
+------------+------------------------------+---------------------------------+
| R-66070    |  VNFD meta data              | tosca.datatypes.nfv.            |
|            |                              | VnfInfoModifiableAttributes -   |
|            |                              | metadata?                       |
+------------+------------------------------+---------------------------------+
| R-96634    | VNFD.configurableProperties  | tosca.datatypes.nfv.Vnf\        |
|            | describing scaling           | ConfigurableProperties,         |
|            | characteristics.  VNFD.\     | tosca.datatypes.nfv.ScaleInfo   |
|            | autoscale defines the rules  |                                 |
|            | for scaling based on specific|                                 |
|            | VNF  indications             |                                 |
+------------+------------------------------+---------------------------------+
| ?          |  VDU Virtual Storage         | tosca.nodes.nfv.Vdu.\           |
|            |                              | VirtualStorage                  |
+------------+------------------------------+---------------------------------+
| R-01478    | Monitoring Info Element (TBD)| tosca.capabilities.nfv.Metric - |
|            | - SOL001 per VNF/VDU/VLink   | type for monitoring             |
| R-01556    | memory-consumption,          |                                 |
|            | CPU-utilization,             | monitoring_parameter  of above  |
|            | bandwidth-consumption, VNFC  | type per VNF/VDU/VLink          |
|            | downtime, etc.               |                                 |
+------------+------------------------------+---------------------------------+


Table D2. TOSCA CSAR structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section defines the requirements around the CSAR structure.

The table below describes the numbered requirements for CSAR structure as
agreed with SDC. The format of the CSAR is specified in SOL004.

+------------+-------------------------------------+--------------------------+
| Requirement| Description                         | CSAR artifact directory  |
| Number     |                                     |                          |
+============+=====================================+==========================+
| R-26881    | The VNF provider MUST provide the   | ROOT\\Artifacts\         |
|            | binaries and images needed to       | \\VNF_Image.bin          |
|            | instantiate the VNF (VNF and VNFC   |                          |
|            | images).                            |                          |
+------------+-------------------------------------+--------------------------+
| R-30654    | VNFD.lifeCycleManagementScript that | ROOT\\Artifacts\         |
|            | includes a list of events and       | \\Informational\         |
|            | corresponding management scripts    | \\Install.csh            |
|            | performed for the VNF - SOL001      |                          |
+------------+-------------------------------------+--------------------------+
| R-35851    | All VNF topology related definitions| ROOT\\Definitions\       |
|            | in yaml files VNFD/Main Service     | \\VNFC.yaml              |
|            | template at the ROOT                |                          |
|            |                                     | ROOT\                    |
|            |                                     | \\MainService\           |
|            |                                     | \\Template.yaml          |
+------------+-------------------------------------+--------------------------+
| R-40827    | CSAR License directory - SOL004     | ROOT\\Licenses\          |
|            |                                     | \\License_term.txt       |
+------------+-------------------------------------+--------------------------+
| R-77707    | CSAR Manifest file - SOL004         | ROOT\                    |
|            |                                     | \\MainServiceTemplate.mf |
+------------+-------------------------------------+--------------------------+


