.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

.. _ONAP Heat VNF Modularity:

ONAP Heat VNF Modularity
---------------------------

ONAP supports a modular Heat Orchestration Template design pattern,
referred to as *VNF Modularity.* With this approach, a single VNF **MAY** be
composed from one or more Heat Orchestration Templates, each of which
represents a subset of the overall VNF. These component parts are
referred to as *VNF Modules*. During orchestration, these modules
are deployed incrementally to create the complete VNF.

As stated in :need:`R-33132`, a VNF's Heat Orchestration Template **MAY** be
     1. Base Module Heat Orchestration Template (also referred to as a
        Base Module),
     2. Incremental Module Heat Orchestration Template (referred to as
        an Incremental Module), or
     3. a Cinder Volume Module Heat Orchestration Template (referred to as
        Cinder Volume  Module).

At orchestration time, the VNF's Base
Module **MUST** be deployed first, prior to any incremental modules.

As stated in :need:`R-28980`, :need:`R-86926`, and :need:`R-91497`, a
VNF's incremental module **MAY** be used for

  * initial VNF deployment only
  * scale out only
  * both deployment and scale out

As stated in :need:`R-68122`, a VNF's incremental module **MAY** be deployed
more than once, either during initial VNF deployment and/or scale out

As stated in :need:`R-37028` and :need:`R-13196`, a VNF **MUST** be composed
of one Base Module and **MAY** be composed of zero to many Incremental
Modules.

ONAP also supports the concept of an optional, independently deployed
Cinder volume via a separate Heat Orchestration Templates, referred to
as a Cinder Volume Module. This allows the volume to persist after a VM
(i.e., OS::Nova::Server) is deleted, allowing the volume to be reused on
another instance (e.g., during a fail over activity).

The scope of a Cinder volume module, when it exists, must be 1:1 with a
Base module or Incremental Module.

A VNF module (base, incremental, cinder) **MAY** support nested templates.

.. req::
    :id: R-610010
    :target: VNF
    :keyword: MAY
    :validation_mode: none
    :introduced: el alto

    A VNF's Heat Orchestration Template's Base Module **MAY** declare zero, one,
    or more than one ``OS::Nova::Server`` resource.  A ``OS::Nova::Server``
    **MAY** be created in the base module or a nested yaml file invoked by the
    base module.

.. req::
    :id: R-610015
    :target: VNF
    :keyword: MAY
    :validation_mode: none
    :introduced: guilin

    When a VNF's Heat Orchestration Template is composed of a Base Module and
    one or more Incremental Modules, the Base Module **SHOULD NOT** declare an
    ``OS::Nova::Server`` resource.
    When a VNF is composed of a Base Module and one or more Incremental
    Modules, the ONAP *VF Module Replacement Feature* does not support
    the replacement (updating) of the Base Module.
    An ``OS::Nova::Server`` resource declared in the Base Module can not be
    updated.



.. req::
    :id: R-610020
    :target: VNF
    :keyword: MAY
    :validation_mode: none
    :introduced: el alto

    If a VNF's Heat Orchestration Template's Base Module contains two or more
    ``OS::Nova::Server`` resources (created in the base module itself and/or
    in a nested yaml file invoked by the base module), the ``OS::Nova::Server``
    resources **MAY**
    define the same ``{vm-type}`` (as defined in R-01455) or **MAY**
    define different ``{vm-type}``.

    Note that

    - there is no constraint on the number of unique ``{vm-type}`` defined in
      the base module.
    - there is no constraint on the number of ``OS::Nova::Server`` resources
      that define the same ``{vm-type}`` in the base module.
    - if an ``OS::Nova::Server`` is created in a nested yaml file invoked by
      the base module, the nested yaml file **MUST NOT** contain more than one
      ``OS::Nova::Server`` resource (as defined in R-17528).

.. req::
    :id: R-610030
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :introduced: el alto

    A VNF's Heat Orchestration Template's Incremental Module **MUST**
    declare one or more ``OS::Nova::Server`` resources.  A ``OS::Nova::Server``
    **MAY** be created in the incremental module or a nested yaml file invoked
    by the incremental module.

.. req::
    :id: R-610040
    :target: VNF
    :keyword: MAY
    :validation_mode: none
    :introduced: el alto

    If a VNF's Heat Orchestration Template's Incremental Module contains two or
    more ``OS::Nova::Server`` resources, the ``OS::Nova::Server`` resources
    **MAY** define the same ``{vm-type}`` (as defined in R-01455) or **MAY**
    define different ``{vm-type}``.

    Note that

    - there is no constraint on the number of unique ``{vm-type}`` defined in
      the incremental module.
    - there is no constraint on the number of ``OS::Nova::Server`` resources
      that define the same ``{vm-type}`` in the incremental module.
    - if an ``OS::Nova::Server`` is created in a nested yaml file invoked by
      the incremental module, the nested yaml file **MUST NOT** contain more
      than one ``OS::Nova::Server`` resource (as defined in R-17528).


.. req::
    :id: R-610050
    :target: VNF
    :keyword: MAY
    :validation_mode: none
    :introduced: el alto

    The same ``{vm-type}`` for a VNF's Heat Orchestration Template's
    ``OS::Nova::Server`` resource (as defined in R-01455) **MAY** exist in
    the VNF's Heat Orchestration Template's Base Module (or invoked nested yaml
    file) and/or one or more of the VNF's Heat Orchestration Template's
    Incremental Modules (or invoked nested yaml file).


A shared Heat Resource is a resource that **MAY** be used by
other Heat Resources either in the Base Module or an
Incremental Module.

.. req::
    :id: R-61001
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: dublin

    A shared Heat Orchestration Template resource is a resource that **MUST**
    be defined in the base module and will be referenced by one or
    more resources in one or more incremental modules.

    The UUID of the shared resource (created in the base module) **MUST** be
    exposed by declaring a parameter in the
    ``outputs`` section of the base module.

    For ONAP to provided the UUID value of the shared resource to the
    incremental module, the parameter name defined in the ``outputs``
    section of the base module **MUST** be defined as a parameter
    in the ``parameters`` section of the incremental module.

    ONAP will capture the output parameter name and value in the base module
    and provide the value to the corresponding parameter(s) in the
    incremental module(s).

When the shared resource needs to be referenced by a resource in an
incremental module, the UUID of the shared resource must be exposed by
declaring an ONAP Base Module Output Parameter.

Note that a Cinder volume is not a shared resource. A volume template
must correspond 1:1 with a base module or incremental module.

An example of a shared resource is the resource
OS::Neutron::SecurityGroup. Security groups are sets of IP filter rules
that are applied to a VNF’s networking. The resource OS::Neutron::Port
has a property security_groups which provides the security groups
associated with port. The value of parameter(s) associated with this
property must be the UUIDs of the resource(s)
OS::Neutron::SecurityGroup.

*Note:* A Cinder volume is not considered a shared resource. A volume
template must correspond 1:1 with a base template or add-on module
template.

Suggested Patterns for Modular VNFs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are numerous variations of VNF modularity. Below are two suggested
usage patterns.

**Option 1: Incremental Modules per VNFC type**

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
^^^^^^^^^^^^^^^^^^^

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

      ii. *VNFs may have one or more incremental modules which must not be
          dependent on other Add-On VNF Modules*

   e. Multiple instances of an incremental Module may be added to the
      same VNF (e.g., incrementally grow a VNF by a fixed "add-on"
      growth units)

3. Each VNF Module (base or incremental) may have (optional) an
   associated Cinder Volume Module (see Cinder Volumes)

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
^^^^^^^^^^^^^^^^^^^^^^^^^

*Example: Base Module creates SecurityGroup*

A VNF has a base module, named base.yaml, that defines a
OS::Neutron::SecurityGroup. The security group will be referenced by an
OS::Neutron::Port resource in an incremental module, named
INCREMENTAL_MODULE.yaml. The base module defines a parameter in the
outputs:section named dns_sec_grp_id. dns_sec_grp_id is defined as a
parameter in the incremental module. ONAP captures the UUID value of
dns_sec_grp_id from the base module output statement and provides the
value to the incremental module.

Note that the example below is not a complete Heat Orchestration
Template. The {network-role} has been defined as oam to represent an oam
network and the {vm-type} has been defined as dns.

base_MODULE.yaml

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
        ]
  . . .
  outputs:
    dns_sec_grp_id:
      description: UUID of DNS Resource SecurityGroup
      value: { get_resource: DNS_SECURITY_GROUP }

INCREMENTAL_MODULE.yaml

.. code-block:: yaml

  parameters:
    dns_sec_grp_id:
      type: string
      description: security group UUID
  . . .

  resources:
    dns_0_oam_0_port:
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

A VNF has a base module, named base_module.yaml, that creates an
internal network. An incremental module, named incremental_module.yaml,
will create a VM that will connect to the internal network. The base
module defines a parameter in the out section named int_oam_net_id.
int_oam_net_id is defined as a parameter in the incremental module.
ONAP captures the UUID value of int_oam_net_id from the base module
output statement and provides the value to the incremental module.

Note that the example below is not a complete Heat Orchestration
Template. The {network-role} has been defined as oam to represent an oam
network and the {vm-type} has been defined as lb for load balancer.

base.yaml

.. code-block:: yaml

  heat_template_version: 2013-05-23

  resources:
    int_oam_network:
      type: OS::Neutron::Net
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

  resources:
    lb_server_0:
      type: OS::Nova::Server
      properties:
        name: {get_param: lb_name_0}
        networks:
          - port: { get_resource: get_resource: lb_0_int_oam_port_0  }
  . . .
    lb_0_int_oam_port_0:
      type: OS::Neutron::Port
        properties:
        network: { get_param: int_oam_net_id }
  ...
