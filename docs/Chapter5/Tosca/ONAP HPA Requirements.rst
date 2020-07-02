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


HPA Requirements
----------------

1. SR-IOV Passthrought

Definitions of SRIOV_Port are necessary if VDU supports SR-IOV. Here is
an example.

.. code-block:: yaml

  node_templates:

  vdu_vNat:

  SRIOV_Port:

  attributes:

  tosca_name: SRIOV_Port

  properties:

  virtual_network_interface_requirements:

  - name: sriov

  support_mandatory: false

  description: sriov

  requirement:

  SRIOV: true

  role: root

  description: sriov port

  layer_protocol: ipv4

  requirements:

  - virtual_binding:

  capability: virtual_binding

  node: vdu_vNat

  relationship:

  type: tosca.relationships.nfv.VirtualBindsTo

  - virtual_link:

  node: tosca.nodes.Root

  type: tosca.nodes.nfv.VduCpd

  substitution_mappings:

  requirements:

  sriov_plane:

  - SRIOV_Port

  - virtual_link

  node_type: tosca.nodes.nfv.VNF.vOpenNAT


2. Hugepages

Definitions of mem_page_size as one property shall be added to
Properties and set the value to large if one VDU node supports
huagepages. Here is an example.

.. code-block:: yaml

  node_templates:

  vdu_vNat:

  Hugepages:

  attributes:

  tosca_name: Huge_pages_demo

  properties:

  mem_page_size:large


3. NUMA (CPU/Mem)

Likewise, we shall add definitions of numa to
requested_additional_capabilities if we wand VUD nodes to support
NUMA. Here is an example.

.. code-block:: yaml

  topology_template:

  node_templates:

  vdu_vNat:

  capabilities:

  virtual_compute:

  properties:

  virtual_memory:

  numa_enabled: true

  virtual_mem_size: 2 GB

  requested_additional_capabilities:

  numa:

  support_mandatory: true

  requested_additional_capability_name: numa

  target_performance_parameters:

  hw:numa_nodes: "2"

  hw:numa_cpus.0: "0,1"

  hw:numa_mem.0: "1024"

  hw:numa_cpus.1: "2,3,4,5"

  hw:numa_mem.1: "1024"


4. Hyper-Theading

Definitions of Hyper-Theading are necessary as one of
requested_additional_capabilities of one VUD node if that node
supports Hyper-Theading. Here is an example.

.. code-block:: yaml

  topology_template:

  node_templates:

  vdu_vNat:

  capabilities:

  virtual_compute:

  properties:

  virtual_memory:

  numa_enabled: true

  virtual_mem_size: 2 GB

  requested_additional_capabilities:

  hyper_threading:

  support_mandatory: true

  requested_additional_capability_name: hyper_threading

  target_performance_parameters:

  hw:cpu_sockets : "2"

  hw:cpu_threads : "2"

  hw:cpu_cores : "2"

  hw:cpu_threads_policy: "isolate"


5. OVS+DPDK

Definitions of ovs_dpdk are necessary as one of
requested_additional_capabilities of one VUD node if that node
supports dpdk. Here is an example.

.. code-block:: yaml

  topology_template:

  node_templates:

  vdu_vNat:

  capabilities:

  virtual_compute:

  properties:

  virtual_memory:

  numa_enabled: true

  virtual_mem_size: 2 GB

  requested_additional_capabilities:

  ovs_dpdk:

  support_mandatory: true

  requested_additional_capability_name: ovs_dpdk

  target_performance_parameters:

  sw:ovs_dpdk: "true"


