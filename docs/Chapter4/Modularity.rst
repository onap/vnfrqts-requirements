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


VNF Modularity
--------------

ONAP Heat Orchestration Templates: Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP supports a modular Heat Orchestration Template design pattern,
referred to as *VNF Modularity.*

ONAP VNF Modularity Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With VNF Modularity, a single VNF may be composed from one or more Heat
Orchestration Templates, each of which represents a subset of the
overall VNF. These component parts are referred to as "\ *VNF
Modules*\ ". During orchestration, these modules are deployed
incrementally to create the complete VNF.

A modular Heat Orchestration Template can be either one of the following
types:

1. Base Module

2. Incremental Module

3. Cinder Volume Module

:need:`R-37028` - The VNF **MUST** be composed of one "base" module.

.. req::
    :id: R-41215
    :target: VNF
    :keyword: MAY

    The VNF **MAY** have zero to many "incremental" modules.

ONAP also supports the concept of an optional, independently deployed
Cinder volume via a separate Heat Orchestration Templates, referred to
as a Cinder Volume Module. This allows the volume to persist after a
Virtual Machine (VM) (i.e., OS::Nova::Server) is deleted, allowing the
volume to be reused on another instance (e.g., during a failover
activity).

:need:`R-11200` - The VNF **MUST** keep the scope of a Cinder volume module,
when it exists, to be 1:1 with the VNF Base Module or Incremental Module.

:need:`R-38474` - The VNF **MUST** have a corresponding environment file for a
Base Module.

:need:`R-81725` - The VNF **MUST** have a corresponding environment file for an
Incremental Module.

:need:`R-53433` - The VNF **MUST** have a corresponding environment file for a
Cinder Volume Module.

These concepts will be described in more detail throughout the document.
This overview is provided to set the stage and help clarify the concepts
that will be introduced.

ONAP VNF Modularity
^^^^^^^^^^^^^^^^^^^

ONAP supports a modular Heat Orchestration Template design pattern,
referred to as *VNF Modularity.* With this approach, a single VNF may be
composed from one or more Heat Orchestration Templates, each of which
represents a subset of the overall VNF. These component parts are
referred to as "\ *VNF Modules*\ ". During orchestration, these modules
are deployed incrementally to create the complete VNF.

A modular Heat Orchestration Template can be either one of the following
types:

1. Base Module

2. Incremental Module

3. Cinder Volume Module

A VNF must be composed of one "base" module and may be composed of zero
to many "incremental" modules. The base module must be deployed first,
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

With no growth units, Option 2 is equivalent to the "One Heat Template
per VNF" model.

Note that modularization of VNFs is not required. A single Heat
Orchestration Template (a base module) may still define a complete VNF,
which might be appropriate for smaller VNFs that do not have any scaling
options.

Modularity Rules
^^^^^^^^^^^^^^^^

There are some rules to follow when building modular VNF templates:

1. All VNFs must have one Base VNF Module (template) that must be the
   first one deployed. The base template:

   a. Must include all shared resources (e.g., private networks, server
      groups, security groups)

   b. Must expose all shared resources (by UUID) as "outputs" in its
      associated Heat template (i.e., ONAP Base Module Output
      Parameters)

   c. May include initial set of VMs

   d. May be operational as a stand-alone "minimum" configuration of the
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
      same VNF (e.g., incrementally grow a VNF by a fixed "add-on"
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
^^^^^^^^^^^^^^^^^^^^^^^

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

