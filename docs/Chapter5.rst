**5. VNF Modeling Requirements**
=====================================

a. TOSCA YAML
=============

b. Heat
=======

General Guidelines
------------------

The Heat templates supported by OpenECOMP must follow the requirements
enumerated in this section.

Filenames
---------

In order to enable OpenECOMP to understand the relationship between Heat
files, the following Heat file naming convention must be followed.

-  The file name for the base module Heat template must include “base”
   in the filename.

   -  Examples: *base\_xyz.yml* or *base\_xyz.yaml*; *xyz\_base.yml* or
      *xyz\_base.yaml*

-  There is no explicit naming convention for the add-on modules.

   -  Examples: *module1.yml* or *module1.yaml*

-  All Cinder volume templates must be named the same as the
   corresponding Heat template with “\_volume” appended to the file
   name.

   -  Examples: *base\_xyz\_volume.yml* or *base\_xyz\_volume.yaml*;
      *xyz\_base\_volume.yml* or *xyz\_base\_volume.yaml*;
      *module1\_volume.yml* or *module1\_volume.yaml* (referencing the
      above base module Heat template name)

-  The file name of the environment files must fully match the
   corresponding Heat template filename and have *.env* or *.ENV*
   extension.

   -  Examples: *base\_xyz.env* or *base\_xyz.ENV*; *xyz\_base.env* or
      *xyz\_base.ENV*; *base\_xyz\_volume.env* or
      *base\_xyz\_volume.ENV*; *module1.env* or *module1.ENV;
      module1\_volume.env* or *module1\_volume.ENV* (referencing the
      above base module Heat template name)

-  A YAML file must have a corresponding ENV file, even if the ENV file
   enumerates no parameters. It is an OpenECOMP requirement.

Valid YAML Format
------------------

A Heat template (a YAML file and its corresponding environment file) 
must be formatted in valid YAML. For a description of YAML, refer to the
following OpenStack wiki.

https://wiki.openstack.org/wiki/Heat/YAMLTemplates

A Heat template must follow a specific format. The OpenStack Heat
Orchestration Template (HOT) specification explains in detail all
elements of the HOT template format.

http://docs.openstack.org/developer/heat/template_guide/hot_spec.html

Parameter Categories & Specification
------------------------------------

Parameter Categories
~~~~~~~~~~~~~~~~~~~~

OpenECOMP requires the Heat template parameters to follow certain
requirements in order for it to be orchestrated or deployed. OpenECOMP
classifies parameters into eight broad categories.

-  **OpenECOMP Metadata**: OpenECOMP mandatory and optional metadata
   parameters in the resource *OS::Nova::Server*.

   -  OpenECOMP dictates the naming convention of these Metadata
      parameters and must be adhered to (See Section 4.4).

   -  Metadata parameters must not be enumerated in the environment
      file.

   -  The OpenECOMP Metadata are generated and/or assigned by OpenECOMP
      and supplied to the Heat by OpenECOMP at orchestration time.

-  **OpenECOMP Orchestration Parameters**: The data associated with
   these parameters are VNF instance specific.

   -  OpenECOMP enforces the naming convention of these parameters and
      must be adhered to (See Section 4).

   -  These parameters must not be enumerated in the environment file.

   -  The OpenECOMP Orchestration Parameters are generated and/or
      assigned by OpenECOMP and supplied to the Heat by OpenECOMP at
      orchestration time.

-  **VNF Orchestration Parameters**: The data associated with these
   parameters are VNF instance specific.

   -  While OpenECOMP does not enforce a naming convention, the
      parameter names should include {vm-type} and {network-role} when
      appropriate. (See Section 4)

   -  These parameters must not be enumerated in the environment file.

   -  The VNF Orchestration Parameters Heat are generated and/or
      assigned by OpenECOMP and supplied to the Heat by OpenECOMP at
      orchestration time.

-  **OpenECOMP Orchestration Constants**: The data associated with these
   parameters must be constant across all VNF instances.

   -  OpenECOMP enforces the naming convention of these parameters and
      must be adhered to (See Section 4).

   -  These parameters must be enumerated in the environment file.

-  **VNF Orchestration Constants**: The data associated with these
   parameters must be constant across all VNF instances.

   -  While OpenECOMP does not enforce a naming convention, the
      parameter names should include {vm-type} and {network-role} when
      appropriate. (See Section 4)

   -  These parameters must be enumerated in the environment file.

-  **OpenECOMP Base Template Output Parameters** (also referred to as
   Base Template Output Parameters): The output section of the base
   template allows for specifying output parameters available to add-on
   modules once the base template has been instantiated. The parameter
   defined in the output section of the base must be identical to the
   parameter defined in the add-on module(s) where the parameter is
   used.

-  **OpenECOMP Volume Template Output Parameters** (also referred to as
   Volume Template Output Parameters): The output section of the volume
   template allows for specifying output parameters available to the
   corresponding Heat template (base or add-on) once the volume template
   has been instantiated. The parameter defined in the output section of
   the volume must be identical to the parameter defined in the base or
   add-on module.

-  **OpenECOMP Predefined Output Parameters** (also referred to as
   Predefined Output Parameters): OpenECOMP will look for a small set of
   pre-defined Heat output parameters to capture resource attributes for
   inventory in OpenECOMP. These parameters are specified in Section
   4.6.

The table below summarizes the Parameter Types. If the user is
orchestrating a manual spin up of Heat (e.g. OpenStack command line),
the parameter values that OpenECOMP supplies must be enumerated in the
environment file. However, when the Heat is to be loaded into OpenECOMP
for orchestration, the parameters that OpenECOMP supplies must be
deleted or marked with a comment (i.e., a “#” placed at the beginning of
a line).

+-----------------------------------------------+---------------------+---------------------------------------------------------------------------------+
| Parameter Type                                | Naming Convention   | Parameter Value Source                                                          |
+===============================================+=====================+=================================================================================+
| OpenECOMP Metadata                            | Explicit            | OpenECOMP                                                                       |
+-----------------------------------------------+---------------------+---------------------------------------------------------------------------------+
| OpenECOMP Orchestration Parameters            | Explicit            | OpenECOMP                                                                       |
+-----------------------------------------------+---------------------+---------------------------------------------------------------------------------+
| VNF Orchestration Parameters                  | Recommended         | OpenECOMP                                                                       |
+-----------------------------------------------+---------------------+---------------------------------------------------------------------------------+
| OpenECOMP Orchestration Constants             | Explicit            | Environment File                                                                |
+-----------------------------------------------+---------------------+---------------------------------------------------------------------------------+
| VNF Orchestration Constants                   | Recommended         | Environment File                                                                |
+-----------------------------------------------+---------------------+---------------------------------------------------------------------------------+
| OpenECOMP Base Template Output Parameters     | Recommended         | Heat Output Statement for base, OpenECOMP supplied to add-on modules            |
+-----------------------------------------------+---------------------+---------------------------------------------------------------------------------+
| OpenECOMP Volume Template Output Parameters   | Recommended         | Heat Output Statement for volume, OpeneECOMP supplies to corresponding module   |
+-----------------------------------------------+---------------------+---------------------------------------------------------------------------------+
| OpenECOMP Predefined Output Parameters        | Explicit            | Heat Output Statement                                                           |
+-----------------------------------------------+---------------------+---------------------------------------------------------------------------------+

Table 1 Parameter Types

Parameter Specifications
~~~~~~~~~~~~~~~~~~~~~~~~

OpenECOMP METADATA Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenECOMP defines four “metadata” parameters: vnf\_id, vf\_module\_id,
vnf\_name, vf\_module\_name. These parameters must not define any
constraints in the Heat template, including length restrictions, ranges,
default value and/or allowed patterns.

OpenECOMP Base Template & Volume Template Output Parameters 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The base template and volume template output parameters are defined as
input parameters in subsequent modules. When defined as input
parameters, these parameters must not define any constraints in the Heat
template, including length restrictions, ranges, default value and/or
allowed patterns. The parameter name defined in the output statement of
the Heat must be identical to the parameter name defined in the Heat
that is to receive the value.

OpenECOMP Predefined Output Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These parameters must not define any constraints in the Heat template,
including length restrictions, ranges, default value and/or allowed
patterns.

OpenECOMP Orchestration Parameters, VNF Orchestration Parameters, OpenECOMP Orchestration Constants, VNF Orchestration Constants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenECOMP Orchestration Parameters, VNF Orchestration Parameters,
OpenECOMP Orchestration Constants, VNF Orchestration Constants must
adhere to the following:

-  All parameters should be clearly documented in the template,
   including expected values.

-  All parameters should be clearly specified, including constraints and
   description.

-  Numeric parameter constraints should include range and/or allowed
   values.

-  When the parameter type is a string and the parameter name contains
   an index, the index must be zero based. That is, the index starts at
   zero.

-  When the parameter type is a Comma Delimited List (CDL), the
   reference index must start at zero.

-  Default values must only be supplied in a Heat environment file to
   keep the template itself as clean as possible.

-  Special characters must not be used in parameter names, as currently
   only alphanumeric characters and “\_” underscores are allowed.

Use of Heat Environments
------------------------

A YAML file must have a corresponding environment file (also referred to
as ENV file), even if the environment file defines no parameters. It is
an OpenECOMP requirement.

The environment file must contain parameter values for the OpenECOMP
Orchestration Constants and VNF Orchestration Constants. These
parameters are identical across all instances of a VNF type, and
expected to change infrequently. The OpenECOMP Orchestration Constants
are associated with OS::Nova::Server image and flavor properties (See
Section 4.3). Examples of VNF Orchestration Constants are the networking
parameters associated with an internal network (e.g. private IP ranges)
and Cinder volume sizes.

The environment file must not contain parameter values for parameters
that are instance specific (OpenECOMP Orchestration Parameters, VNF
Orchestration Parameters). These parameters are supplied to the Heat by
OpenECOMP at orchestration time. The parameters are generated and/or
assigned by OpenECOMP at orchestration time

Independent Volume Templates
----------------------------

OpenECOMP supports independent deployment of a Cinder volume via
separate Heat templates. This allows the volume to persist after VNF
deletion so that they can be reused on another instance (e.g. during a
failover activity).

A VNF Incremental Module or Base Module may have an independent volume
module. Use of separate volume modules is optional. A Cinder volume may
be embedded within the Incremental or Base Module if persistence is not
required.

If a VNF Incremental Module or Base Module has an independent volume
module, the scope of volume templates must be 1:1 with Incremental
module or Base module. A single volume module must create only the
volumes required by a single Incremental module or Base module.

The following rules apply to independent volume Heat templates:

-  Cinder volumes must be created in a separate Heat template from the
   Incremental and Base Modules.

   -  A single volume module must include all Cinder volumes needed by
      the Incremental/Base module.

   -  The volume template must define “outputs” for each Cinder volume
      resource universally unique identifier (UUID) (i.e. OpenECOMP
      Volume Template Output Parameters).

-  The VNF Incremental Module or Base Module must define input
   parameters that match each Volume output parameter (i.e., OpenECOMP
   Volume Template Output Parameters).

   -  OpenECOMP will supply the volume template outputs automatically to
      the bases/incremental template input parameters.

-  Volume modules may utilize nested Heat templates.

**Example (volume template):**

    In this example, the {vm-type} has been left as a variable.
    {vm-type} is described in section 4.1. If the VM was a load
    balancer, the {vm-type} could be defined as “lb”

.. code-block:: python

    parameters:
        vm-typevnf\_name:
            type: string
        {vm-type}\_volume\_size\_0:
            type: number
        ...

    resources:
        {vm-type}\_volume\_0:
            type: OS::Cinder::Volume
            properties:
                name:
                    str\_replace:
                        template: VNF\_NAME\_volume\_0
                        params:
                            VNF\_NAME: { get\_param: vnf\_name }
                size: {get\_param: {vm-type}\_volume\_size\_0}
        ...

*(+ additional volume definitions)*

.. code-block:: python

    outputs:
        {vm-type}\_volume\_id\_0:
            value: {get\_resource: {vm-type}\_volume\_0}
        ...

*(+ additional volume outputs)*

*Example (VNF module template):*

.. code-block:: python

    parameters:
        {vm-type}\_name\_0:
            type: string
        {vm-type}\_volume\_id\_0:
            type: string
        ...

    resources:
        {vm-type}\_0:
            type: OS::Nova::Server
            properties:
                name: {get\_param: {vm-type}\_name\_0}
                networks:
                ...

    {vm-type}\_0\_volume\_attach:
        type: OS::Cinder::VolumeAttachment
        properties:
            instance\_uuid: { get\_resource: {vm-type}\_0 }
            volume\_id: { get\_param: {vm-type}\_volume\_id\_0 }

Nested Heat Templates
---------------------

OpenECOMP supports nested Heat templates per the OpenStack
specifications. Nested templates may be suitable for larger VNFs that
contain many repeated instances of the same VM type(s). A common usage
pattern is to create a nested template for each VM type along with its
supporting resources. The master VNF template (or VNF Module template)
may then reference these component templates either statically (by
repeated definition) or dynamically (via *OS::Heat::ResourceGroup*).

Nested template support in OpenECOMP is subject to the following
limitations:

-  Heat templates for OpenECOMP must only have one level of nesting.
   OpenECOMP only supports one level of nesting.

-  Nested templates must be referenced by file name in the master
   template

   -  i.e. use of *resource\_registry* in the .env file is *not*
      currently supported

-  Nested templates must have unique file names within the scope of the
   VNF

-  OpenECOMP does not support a directory hierarchy for nested
   templates. All templates must be in a single, flat directory (per
   VNF)

-  A nested template may be shared by all Modules (i.e., Heat templates)
   within a given VNF

Networking 
----------

External Networks
-----------------

VNF templates must not include any resources for external networks
connected to the VNF. In this context, “external” is in relation to the
VNF itself (not with regard to the Network Cloud site). External
networks may also be referred to as “inter-VNF” networks.

-  External networks must be orchestrated separately, so they can be
   shared by multiple VNFs and managed independently. When the external
   network is created, it must be assigned a unique {network-role} (See
   section 4.2).

-  External networks must be passed into the VNF template as parameters,
   including the network-id (i.e. the neutron network UUID) and optional
   subnet ID.

-  VNF templates must pass the appropriate external network IDs into
   nested VM templates when nested Heat is used.

-  VNFs may use DHCP assigned IP addresses or assign fixed IPs when
   attaching VMs to an external network.

-  OpenECOMP enforces a naming convention for parameters associated with
   external networks.

-  Parameter values associated with an external network will be
   generated and/or assigned by OpenECOMP at orchestration time.

-  Parameter values associated with an external network must not be
   enumerated in the environment file.

Internal Networks
-----------------

Orchestration activities related to internal networks must be included
in VNF templates. In this context, “internal” is in relation to the VNF
itself (not in relation to the Network Cloud site). Internal networks
may also be referred to as “intra-VNF” networks or “private” networks.

-  Internal networks must not attach to any external gateways and/or
   routers. Internal networks are for intra-VM communication only.

-  In the modular approach, internal networks must be created in the
   Base Module template, with their resource IDs exposed as outputs
   (i.e., OpenECOMP Base Template Output Parameters) for use by all
   add-on module templates. When the external network is created, it
   must be assigned a unique {network-role} (See section 4.2).

-  VNFs may use DHCP assigned IP addresses or assign fixed IPs when
   attaching VMs to an internal network.

-  OpenECOMP does not enforce a naming convention for parameters for
   internal network, however, a naming convention is provided that
   should be followed.

-  Parameter values associated with an internal network must either be
   passed as output parameter from the base template (i.e., OpenECOMP
   Base Template Output Parameters) into the add-on modules or be
   enumerated in the environment file.

IP Address Assignment
---------------------

-  VMs connect to external networks using either fixed (e.g. statically
   assigned) IP addresses or DHCP assigned IP addresses.

-  VMs connect to internal networks using either fixed (e.g. statically
   assigned) IP addresses or DHCP assigned IP addresses.

-  Neutron Floating IPs must not be used. OpenECOMP does not support
   Neutron Floating IPs.

-  OpenECOMP supports the OS::Neutron::Port property
   “allowed\_address\_pairs.” See Section 4.4.3.

Parameter Naming Convention
---------------------------

{vm-type}
---------

A common *{vm-type}* identifier must be used throughout the Heat
template in naming parameters, for each VM type in the VNF with the
following exceptions:

-  The four OpenECOMP Metadata parameters must not be prefixed with a
   common {vm-type} identifier. They are *vnf\_name*, *vnf\_id*,
   *vf\_module\_id*, *vf\_module\_name*.

-  Parameters only referring to a network or subnetwork must not be
   prefixed with a common {vm-type} identifier.

-  The parameter referring to the OS::Nova::Server property
   availability\_zone must not be prefixed with a common {vm-type}
   identifier.

-  {vm-type} must be unique to the VNF. It does not have to be globally
   unique across all VNFs that OpenECOMP supports.

{network-role}
--------------

VNF templates must not include any resources for external networks
connected to the VNF. In this context, “external” is in relation to the
VNF itself (not with regard to the Network Cloud site). External
networks may also be referred to as “inter-VNF” networks.

External networks must be orchestrated separately, so they can be shared
by multiple VNFs and managed independently. When the external network is
created, it must be assigned a unique {network-role}.

“External” networks must be passed into the VNF template as parameters.
Examples include the network-id (i.e. the neutron network UUID) and
optional subnet ID. See section 4.4.3.

Any parameter that is associated with an external network must include
the {network-role} as part of the parameter name.

Internal network parameters must also define a {network-role}. Any
parameter that is associated with an internal network must include
int\_{network-role} as part of the parameter name.

Resource: OS::Nova::Server - Parameters
---------------------------------------

The following OS::Nova::Server Resource Property Parameter Names must
follow the OpenECOMP parameter Naming Convention. All the parameters
associated with OS::Nova::Server are classified as OpenECOMP
Orchestration Parameters.

+----------------------+-----------------------------------------+------------------+
| OS::Nova::Server                                                                  |
+======================+=========================================+==================+
| Property             | OpenECOMP Parameter Naming Convention   | Parameter Type   |
+----------------------+-----------------------------------------+------------------+
| image                | {*vm-type*}\_image\_name                | string           |
+----------------------+-----------------------------------------+------------------+
| flavor               | {*vm-type*}\_flavor\_name               | string           |
+----------------------+-----------------------------------------+------------------+
| name                 | {*vm-type*}\_name\_{*index*}            | string           |
+----------------------+-----------------------------------------+------------------+
|                      | {vm-type}\_names                        | CDL              |
+----------------------+-----------------------------------------+------------------+
| availability\_zone   | availability\_zone\_{index}             | string           |
+----------------------+-----------------------------------------+------------------+

Table 2 Resource Property Parameter Names

Property: image
~~~~~~~~~~~~~~~

Image is an OpenECOMP Orchestration Constant parameter. The image must
be referenced by the Network Cloud Service Provider (NCSP) image name,
with the parameter enumerated in the Heat environment file.

The parameters must be named *“{vm-type}\_image\_name”* in the VNF.

Each VM type (e.g., {vm-type}) should have a separate parameter for
images, even if several share the same image. This provides maximum
clarity and flexibility.

Property: flavor
~~~~~~~~~~~~~~~~

Flavor is an OpenECOMP Orchestration Constant parameter. The flavors
must be referenced by the Network Cloud Service Provider (NCSP) flavor
name, with the parameter enumerated in the Heat environment file.

The parameters must be named *“{vm-type}\_flavor\_name”* for each
*{vm-type}* in the VNF.

Each VM type should have separate parameters for flavors, even if more
than one VM shares the same flavor. This provides maximum clarity and
flexibility.

Property: Name
~~~~~~~~~~~~~~

Name is an OpenEOMP Orchestration parameter; the value is provided to
the Heat template by OpenECOMP.

VM names (hostnames) for assignment to VM instances must be passed to
Heat templates either as

-  an array (comma delimited list) for each VM type

-  a set of fixed-index parameters for each VM type instance.

Each element in the VM Name list should be assigned to successive
instances of that VM type.

The parameter names must reflect the VM Type (i.e., include the
{vm-type} in the parameter name.) The parameter name format must be one
of the following:

-  If the parameter type is a comma delimited list: {**vm-type**}\_names

-  If the parameter type is a string with a fixed index:
   {**vm-type**}\_name\_{**index**}

If a VNF contains more than three instances of a given {vm-type}, the
CDL form of the parameter name (i.e., *{vm-type}*\ \_names} should be
used to minimize the number of unique parameters defined in the Heat.

*Examples:*

.. code-block:: python

    parameters:
        {vm-type}\_names:
            type: comma\_delimited\_list
            description: VM Names for {vm-type} VMs
        {vm-type}\_name\_{index}:
            type: string
            description: VM Name for {vm-type} VM {index}

*Example (CDL):*

In this example, the {vm-type} has been defined as “lb” for load
balancer.

.. code-block:: python

    parameters:
        lb\_names:
            type: comma\_delimited\_list
            description: VM Names for lb VMs
    resources:
        lb\_0:
            type: OS::Nova::Server
            properties:
                name: { get\_param: [lb\_names, 0] }
                ...

        lb\_1:
            type: OS::Nova::Server
            properties:
                name: { get\_param: [lb\_names, 1] }
                ...

**Example (fixed-index):**

In this example, the {vm-type} has been defined as “lb” for load
balancer.

.. code-block:: python

    parameters:
        lb\_name\_0:
            type: string
            description: VM Name for lb VM 0
        lb\_name\_1:
            type: string
            description: VM Name for lb VM 1

    resources:
        lb\_0:
            type: OS::Nova::Server
            properties:
                name: { get\_param: lb\_name\_0 }
                ...

    lb\_1:
        type: OS::Nova::Server
        properties:
            name: { get\_param: lb\_name\_1 }
            ...

Property: availability\_zone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Availability\_zone is an OpenECOMP Orchestration parameter; the value is
provided to the Heat template by OpenECOMP.

Availability zones must be passed as individual numbered parameters (not
as arrays) so that VNFs with multi-availability zone requirements can
clearly specify that in its parameter definitions.

The availability zone parameter must be defined as
“availability\_zone\_{index}”, with the {index} starting at zero.

*Example:*

In this example, the {vm-type} has been defined as “lb” for load
balancer.

.. code-block:: python

    parameters:
        lb\_names:
            type: comma\_delimited\_list
            description: VM Names for lb VMs
        availability\_zone\_0:
            type: string
            description: First availability zone ID or Name

    resources:
        lb\_0:
            type: OS::Nova::Server
            properties:
                name: { get\_param: [lb\_names, 0] }
                availability\_zone: { get\_param: availability\_zone\_0 }
                ...

Resource: OS::Nova::Server - Metadata
-------------------------------------

This section describes the OpenECOMP Metadata parameters.

OpenECOMP Heat templates must include the following three parameters
that are used as metadata under the resource OS::Nova:Server: vnf\_id,
vf\_module\_id, vnf\_name

OpenECOMP Heat templates may include the following parameter that is
used as metadata under the resource OS::Nova:Server: vf\_module\_name.

These parameters are all classified as OpenECOMP Metadata.

+---------------------------+------------------+----------------------+
| Metadata Parameter Name   | Parameter Type   | Mandatory/Optional   |
+===========================+==================+======================+
| vnf\_id                   | string           | mandatory            |
+---------------------------+------------------+----------------------+
| vf\_module\_id            | string           | mandatory            |
+---------------------------+------------------+----------------------+
| vnf\_name                 | string           | mandatory            |
+---------------------------+------------------+----------------------+
| vf\_module\_name          | string           | optional             |
+---------------------------+------------------+----------------------+

    Table 3 OpenECOMP Metadata

Required Metadata Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~

The vnf\_id, vf\_module\_id, and vnf\_name metadata elements are
required (must) for *OS::Nova::Server* resources. The metadata
parameters will be used by OpenECOMP to associate the servers with the
VNF instance.

-  vnf\_id

   -  *“vnf\_id”* parameter value will be supplied by OpenECOMP.
      OpenECOMP generates the UUID that is the vnf\_id and supplies it
      to the Heat at orchestration time.

-  vf\_module\_id

   -  “\ *vf\_module\_id”* parameter value will be supplied by
      OpenECOMP. OpenECOMP generates the UUID that is the vf\_module\_id
      and supplies it to the Heat at orchestration time.

-  vnf\_name

   -  “\ *vnf\_name”* parameter value will be generated and/or assigned
      by OpenECOMP and supplied to the Heat by OpenECOMP at
      orchestration time.

Optional Metadata Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following metadata element is optional for *OS::Nova::Server*
resources:

-  *vf\_module\_name*

   -  The vf\_module\_name is the name of the name of the Heat stack
      (e.g., <STACK\_NAME>) in the command “Heat stack-create” (e.g.
      Heat stack-create [-f <FILE>] [-e <FILE>] <STACK\_NAME>). The
      <STACK\_NAME> needs to be specified as part of the orchestration
      process.

   -  *“vf\_module\_name”* parameter value, when used, will be supplied
      by OpenECOMP to the Heat at orchestration time. The parameter will
      be generated and/or assigned by OpenECOMP and supplied to the Heat
      by OpenECOMP at orchestration time.

*Example*

In this example, the {vm-type} has been defined as “lb” for load
balancer.

.. code-block:: python

    parameters:
        vnf\_name:
            type: string
            description: Unique name for this VNF instance
        vnf\_id:
            type: string
            description: Unique ID for this VNF instance
        vf\_module\_name:
            type: string
            description: Unique name for this VNF Module instance
        vf\_module\_id:
            type: string
            description: Unique ID for this VNF Module instance

    resources:
        lb\_server\_group:
            type: OS::Nova::ServerGroup
                properties:
                    name:
                        str\_replace:
                            template: VNF\_NAME\_lb\_ServerGroup
                            params:
                                VNF\_NAME: { get\_param: VNF\_name }
                    policies: [ ‘anti-affinity’ ]
        
        lb\_vm\_0:
            type: OS::Nova::Server
            properties:
                name: { get\_param: lb\_name\_0 }
                scheduler\_hints:
                group: { get\_resource: lb\_server\_group }
                metadata:   
                    vnf\_name: { get\_param: vnf\_name }
                    vnf\_id: { get\_param: vnf\_id }
                    vf\_module\_name: { get\_param: vf\_module\_name }
                    vf\_module\_id: { get\_param: vf\_module\_id }
                ...

Resource: OS::Neutron::Port - Parameters
----------------------------------------

The following four OS::Neutron::Port Resource Property Parameters must
adhere to the OpenECOMP parameter naming convention.

-  network

-  subnet

-  fixed\_ips

-  allowed\_address\_pairs

These four parameters reference a network, which maybe an external
network or an internal network. Thus the parameter will include
{network-role} in its name.

When the parameter references an external network, the parameter is an
OpenECOMP Orchestration Parameter. The parameter value must be supplied
by OpenECOMP. The parameters must adhere to the OpenECOMP parameter
naming convention.

+---------------------------+-----------------------------------------------+------------------+
| OS::Neutron::Port                                                                            |
+===========================+===============================================+==================+
| Property                  | Parameter Name for External Networks          | Parameter Type   |
+---------------------------+-----------------------------------------------+------------------+
| Network                   | {network-role}\_net\_id                       | string           |
+---------------------------+-----------------------------------------------+------------------+
|                           | {network-role}\_net\_name                     | string           |
+---------------------------+-----------------------------------------------+------------------+
| Subnet                    | {network-role}\_subnet\_id                    | string           |
+---------------------------+-----------------------------------------------+------------------+
|                           | {network-role}\_v6\_subnet\_id                | string           |
+---------------------------+-----------------------------------------------+------------------+
| fixed\_ips                | {vm-type}\_{network-role}\_ip\_{index}        | string           |
+---------------------------+-----------------------------------------------+------------------+
|                           | {vm-type}\_{network-role}\_ips                | CDL              |
+---------------------------+-----------------------------------------------+------------------+
|                           | {vm-type}\_{network-role}\_v6\_ip\_{index}    | string           |
+---------------------------+-----------------------------------------------+------------------+
|                           | {vm-type}\_{network-role}\_v6\_ips            | CDL              |
+---------------------------+-----------------------------------------------+------------------+
| allowed\_address\_pairs   | {vm-type}\_{network-role}\_floating\_ip       | string           |
+---------------------------+-----------------------------------------------+------------------+
|                           | {vm-type}\_{network-role}\_floating\_v6\_ip   | string           |
+---------------------------+-----------------------------------------------+------------------+
|                           | {vm-type}\_{network-role}\_ip\_{index}        | string           |
+---------------------------+-----------------------------------------------+------------------+
|                           | {vm-type}\_{network-role}\_ips                | CDL              |
+---------------------------+-----------------------------------------------+------------------+
|                           | {vm-type}\_{network-role}\_v6\_ip\_{index}    | string           |
+---------------------------+-----------------------------------------------+------------------+
|                           | {vm-type}\_{network-role}\_v6\_ips            | CDL              |
+---------------------------+-----------------------------------------------+------------------+

Table 4 Port Resource Property Parameters (External Networks)

When the parameter references an internal network, the parameter is a
VNF Orchestration Parameters. The parameter value(s) must be supplied
either via an output statement(s) in the base module (i.e., OpenECOMP
Base Template Output Parameters) or be enumerated in the environment
file. The parameters must adhere to the following parameter naming
convention.

+---------------------------+----------------------------------------------------+------------------+
| OS::Neutron::Port                                                                                 |
+===========================+====================================================+==================+
| Property                  | Parameter Name for Internal Networks               | Parameter Type   |
+---------------------------+----------------------------------------------------+------------------+
| Network                   | int\_{network-role}\_net\_id                       | string           |
+---------------------------+----------------------------------------------------+------------------+
|                           | int\_{network-role}\_net\_name                     | string           |
+---------------------------+----------------------------------------------------+------------------+
| Subnet                    | int\_{network-role}\_subnet\_id                    | string           |
+---------------------------+----------------------------------------------------+------------------+
|                           | Int\_{network-role}\_v6\_subnet\_id                | string           |
+---------------------------+----------------------------------------------------+------------------+
| fixed\_ips                | {vm-type}\_int\_{network-role}\_ip\_{index}        | string           |
+---------------------------+----------------------------------------------------+------------------+
|                           | {vm-type}\_int\_{network-role}\_ips                | CDL              |
+---------------------------+----------------------------------------------------+------------------+
|                           | {vm-type}\_int\_{network-role}\_v6\_ip\_{index}    | string           |
+---------------------------+----------------------------------------------------+------------------+
|                           | {vm-type}\_int\_{network-role}\_v6\_ips            | CDL              |
+---------------------------+----------------------------------------------------+------------------+
| allowed\_address\_pairs   | {vm-type}\_int\_{network-role}\_floating\_ip       | string           |
+---------------------------+----------------------------------------------------+------------------+
|                           | {vm-type}\_int\_{network-role}\_floating\_v6\_ip   | string           |
+---------------------------+----------------------------------------------------+------------------+
|                           | {vm-type}\_int\_{network-role}\_ip\_{index}        | string           |
+---------------------------+----------------------------------------------------+------------------+
|                           | {vm-type}\_int\_{network-role}\_ips                | CDL              |
+---------------------------+----------------------------------------------------+------------------+
|                           | {vm-type}\_int\_{network-role}\_v6\_ip\_{index}    | string           |
+---------------------------+----------------------------------------------------+------------------+
|                           | {vm-type}\_int\_{network-role}\_v6\_ips            | CDL              |
+---------------------------+----------------------------------------------------+------------------+

Table 5 Port Resource Property Parameters (Internal Networks)

Property: network & subnet
~~~~~~~~~~~~~~~~~~~~~~~~~~

The property “networks” in the resource OS::Neutron::Port must be
referenced by Neutron Network ID, a UUID value, or by the network name
defined in OpenStack.

When the parameter is referencing an “external” network, the parameter
must adhere to the following naming convention

-  *“{*\ network-role}\_net\_id”, for the Neutron network ID

-  “{network-role}\_net\_name”, for the network name in OpenStack

When the parameter is referencing an “internal” network, the parameter
must adhere to the following naming convention.

-  “\ *int\_{network-role}\_net\_id*\ ”, for the Neutron network ID

-  “\ *int\_{network-role}\_net\_name*\ ”, for the network name in
   OpenStack

The property “subnet\_id” must be used if a DHCP IP address assignment
is being requested and the DHCP IP address assignment is targeted at a
specific subnet.

The property “subnet\_id” should not be used if all IP assignments are
fixed, or if the DHCP assignment does not target a specific subnet

When the parameter is referencing an “external” network subnet, the
“subnet\_id” parameter must adhere to the following naming convention.

-  “\ *{network-role}\_subnet\_id*\ ” if the subnet is an IPv4 subnet

-  “\ *{network-role}\_v6\_subnet\_id”* if the subnet is an IPv6 subnet

When the parameter is referencing an “internal” network subnet, the
“subnet\_id” parameter must adhere to the following naming convention.

-  “\ *int\_{network-role}\_subnet\_id*\ ” if the subnet is an IPv4
   subnet

-  “\ *int\_{network-role}\_v6\_subnet\_id*\ ” if the subnet is an IPv6
   subnet

*Example:*

.. code-block:: python

    parameters:
        {network-role}\_net\_id:
            type: string
            description: Neutron UUID for the {network-role} network
        {network-role}\_net\_name:
            type: string
            description: Neutron name for the {network-role} network
        {network-role}\_subnet\_id:
            type: string
            description: Neutron subnet UUID for the {network-role} network
        {network-role}\_v6\_subnet\_id:
            type: string
            description: Neutron subnet UUID for the {network-role} network

*Example:*

In this example, the {network-role} has been defined as “oam” to
represent an oam network and the {vm-type} has been defined as “lb” for
load balancer.

.. code-block:: python

    parameters:
        oam\_net\_id:
            type: string
            description: Neutron UUID for the oam network

    resources:
        lb\_port\_1:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }

Property: fixed\_ips
~~~~~~~~~~~~~~~~~~~~

The property “fixed\_ips” in the resource OS::Neutron::Port must be used
when statically assigning IP addresses.

An IP address is assigned to a port on a type of VM (i.e., {vm-type})
that is connected to a type of network (i.e., {network-role}). These two
tags are components of the parameter name.

When the “fixed\_ips” parameter is referencing an “external” network,
the parameter must adhere to the naming convention below. The parameter
may be a comma delimited list or a string.

There must be a different parameter name for IPv4 IP addresses and IPv6
addresses

-  **Comma-delimited list:** Each element in the IP list should be
   assigned to successive instances of that VM type on that network.

   -  *Format for IPv4 addresses:* {vm-type}\_{network-role}\_ips

   -  *Format for IPv6 addresses:* {vm-type}\_{network-role}\_v6\_ips

-  **A set of fixed-index parameters:** In this case, the parameter
   should have “\ *type: string*\ ” and must be repeated for every IP
   expected for each {vm-type} + {network-role} pair.

   -  *Format for IPv4 addresses:*
      {vm-type}\_{network-role}\_ip\_{index}

   -  *Format for IPv6 addresses:*
      {vm-type}\_{network-role}\_v6\_ip\_{index}

When the “fixed\_ips” parameter is referencing an “internal” network,
the parameter must adhere to the naming convention below. The parameter
may be a comma delimited list or a string.

There must be a different parameter name for IPv4 IP addresses and IPv6
addresses

-  **Comma-delimited list:** Each element in the IP list should be
   assigned to successive instances of that VM type on that network.

   -  *Format for IPv4 addresses:* {vm-type}\_int\_{network-role}\_ips

   -  *Format for IPv6 addresses:*
      {vm-type}\_int\_{network-role}\_v6\_ips

-  **A set of fixed-index parameters:** In this case, the parameter
   should have “\ *type: string*\ ” and must be repeated for every IP
   expected for each {vm-type} and {network-role}pair.

   -  *Format for IPv4 addresses:*
      {vm-type}\_int\_{network-role}\_ip\_{index}

   -  *Format for IPv6 addresses:*
      {vm-type}\_int\_{network-role}\_v6\_ip\_{index}

If a VNF contains more than three IP addresses for a given {vm-type} and
{network-role} combination, the CDL form of the parameter name should be
used to minimize the number of unique parameters defined in the Heat.

*Example (external network)*

.. code-block:: python

    parameters:
        {vm-type}\_{network-role}\_ips:
            type: comma\_delimited\_list
            description: Fixed IPv4 assignments for {vm-type} VMs on the
    {network-role} network
        {vm-type}\_{network-role}\_v6\_ips:
            type: comma\_delimited\_list
            description: Fixed IPv6 assignments for {vm-type} VMs on the
    {network-role} network
        {vm-type}\_{network-role}\_ip\_{index}:
            type: string
            description: Fixed IPv4 assignment for {vm-type} VM {index} on the
            {network-role} network
        {vm-type}\_{network-role}\_v6\_ip\_{index}:
            type: string
            description: Fixed IPv6 assignment for {vm-type} VM {index} on the
            {network-role} network

*Example (CDL parameter for IPv4 Address Assignments to an external
network):*

In this example, the {network-role} has been defined as “oam” to
represent an oam network and the {vm-type} has been defined as “db” for
database.

.. code-block:: python

    parameters:
        oam\_net\_id:
            type: string
            description: Neutron UUID for a oam network
        db\_oam\_ips:
            type: comma\_delimited\_list
            description: Fixed IP assignments for db VMs on the oam network

    resources:
        db\_0\_port\_1:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }
            fixed\_ips: [ { “ip\_address”: {get\_param: [ db\_oam\_ips, 0]
            }}]
        db\_1\_port\_1:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }
            fixed\_ips: [ { “ip\_address”: {get\_param: [ db\_oam\_ips, 1]
            }}]

*Example (string parameters for IPv4 Address Assignments to an external
network):*

In this example, the {network-role} has been defined as “oam” to
represent an oam network and the {vm-type} has been defined as “db” for
database.

.. code-block:: python

    parameters:
        oam\_net\_id:
            type: string
            description: Neutron UUID for an OAM network
        db\_oam\_ip\_0:
            type: string
            description: First fixed IP assignment for db VMs on the OAM network
        db\_oam\_ip\_1:
            type: string
            description: Second fixed IP assignment for db VMs on the OAM network

    resources:
        db\_0\_port\_1:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }
            fixed\_ips: [ { “ip\_address”: {get\_param: db\_oam\_ip\_0}}]
        db\_1\_port\_1:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }
            fixed\_ips: [ { “ip\_address”: {get\_param: db\_oam\_ip\_1}}]

Property: allowed\_address\_pairs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The property “allowed\_address\_pairs” in the resource OS::Neutron::Port
allows the user to specify mac\_address/ip\_address (CIDR) pairs that
pass through a port regardless of subnet. This enables the use of
protocols such as VRRP, which floats an IP address between two instances
to enable fast data plane failover. An “allowed\_address\_pairs” is
unique to a {vm-type} and {network-role} combination. The management of
these IP addresses (i.e. transferring ownership between active and
standby VMs) is the responsibility of the application itself.

Note that these parameters are *not* intended to represent Neutron
“Floating IP” resources, for which OpenStack manages a pool of public IP
addresses that are mapped to specific VM ports. In that case, the
individual VMs are not even aware of the public IPs, and all assignment
of public IPs to VMs is via OpenStack commands. OpenECOMP does not
support Neutron-style Floating IPs.

Both IPv4 and IPv6 “allowed\_address\_pairs” addresses are supported.

If property “allowed\_address\_pairs” is used with an external network,
the parameter name must adhere to the following convention:

-  *Format for IPv4 addresses: {vm-type}\_{network-role}\_floating\_ip*

-  *Format for IPv6 addresses:
   {vm-type}\_{network-role}\_floating\_v6\_ip*

*Example:*

.. code-block:: python

    parameters:
        {vm-type}\_{network-role}\_floating\_ip:
            type: string
            description: VIP for {vm-type} VMs on the {network-role} network
        {vm-type}\_{network-role}\_floating\_v6\_ip:
            type: string
            description: VIP for {vm-type} VMs on the {network-role} network

*Example:*

In this example, the {network-role} has been defined as “oam” to
represent an oam network and the {vm-type} has been defined as “db” for
database.

.. code-block:: python

    parameters:
        db\_oam\_ips:
            type: comma\_delimited\_list
            description: Fixed IPs for db VMs on the oam network
        db\_oam\_floating\_ip:
            type: string
            description: Floating IP for db VMs on the oam network
    resources:
        db\_0\_port\_0:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }
            fixed\_ips: [ { “ip\_address”: {get\_param: [db\_oam\_ips,0] }}]
            allowed\_address\_pairs: [
                { “ip\_address”: {get\_param: db\_oam\_floating\_ip}}]
        db\_1\_port\_0:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }
            fixed\_ips: [ { “ip\_address”: {get\_param: [db\_oam\_ips,1] }}]
            allowed\_address\_pairs: [
                { “ip\_address”: {get\_param: db\_oam\_floating\_ip}}]

If property “allowed\_address\_pairs” is used with an internal network,
the parameter name should adhere to the following convention:

-  *Format for IPv4 addresses:
   {vm-type}\_int\_{network-role}\_floating\_ip*

-  *Format for IPv6 addresses:
   {vm-type}\_int\_{network-role}\_floating\_v6\_ip*

Using the parameter *{vm-type}\_{network-role}\_floating\_ip* or
*{vm-type}\_{network-role}\_floating\_v6\_ip* provides only one floating
IP per Vm-type{vm-type} and {network-role} pair. If there is a need for
multiple floating IPs (e.g., Virtual IPs (VIPs)) for a given {vm-type}
and {network-role} combination within a VNF, then the parameter names
defined for the “fixed\_ips” should be used with the
“allowed\_address\_pairs” property. The examples below illustrate this.

Below example reflects two load balancer pairs in a single VNF. Each
pair has one VIP.

*Example: A VNF has four load balancers. Each pair has a unique VIP.*

*Pair 1:* lb\_0 and lb\_1 share a unique VIP

*Pair 2:* lb\_2 and lb\_3 share a unique VIP

In this example, the {network-role} has been defined as “oam” to
represent an oam network and the {vm-type} has been defined as “lb” for
load balancer.

.. code-block:: python

    resources:
        lb\_0\_port\_0:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }
            fixed\_ips: [ { “ip\_address”: {get\_param: [lb\_oam\_ips,0] }}]
            allowed\_address\_pairs: [{ “ip\_address”: {get\_param: [lb\_oam\_ips,2] }}]
        
        lb\_1\_port\_0:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }
            fixed\_ips: [ { “ip\_address”: {get\_param: [lb\_oam\_ips,1] }}]
            allowed\_address\_pairs: [{ “ip\_address”: {get\_param: [lb\_oam\_ips,2] }}]

          lb\_2\_port\_0:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }
            fixed\_ips: [ { “ip\_address”: {get\_param: [lb\_oam\_ips,3] }}]
            allowed\_address\_pairs: [{ “ip\_address”: {get\_param: [lb\_oam\_ips,5] }}]

        lb\_3\_port\_0:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }
            fixed\_ips: [ { “ip\_address”: {get\_param: [lb\_oam\_ips,4] }}]
            allowed\_address\_pairs: [{ “ip\_address”: {get\_param: [lb\_oam\_ips,5] }}]

Below example reflects a single app VM pair within a VNF with two VIPs: 

*Example: A VNF has two load balancers. The pair of load balancers share
two VIPs.*

In this example, the {network-role} has been defined as “oam” to
represent an oam network and the {vm-type} has been defined as “lb” for
load balancer.

.. code-block:: python

    resources:
        lb\_0\_port\_0:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }
            fixed\_ips: [ { “ip\_address”: {get\_param: [lb\_oam\_ips,0] }}]
            allowed\_address\_pairs: [{ "ip\_address": {get\_param: [lb\_oam\_ips,2] }, {get\_param: [lb\_oam\_ips,3] }}]

        lb\_1\_port\_0:
            type: OS::Neutron::Port
            network: { get\_param: oam\_net\_id }
            fixed\_ips: [ { “ip\_address”: {get\_param: [lb\_oam\_ips,1] }}]
           allowed\_address\_pairs: [{ "ip\_address": {get\_param: [lb\_oam\_ips,2] }, {get\_param: [lb\_oam\_ips,3] }}]

As a general rule, provide the fixed IPs for the VMs indexed first in
the CDL and then the VIPs as shown in the examples above.

Resource Property: name
-----------------------

The parameter naming standard for the resource OS::Nova::Server has been
defined in Section 4.3.3. This section describes how the name property
of all other resources must be defined.

Heat templates must use the Heat “str\_replace” function in conjunction
with the OpenECOMP supplied metadata parameter *vnf\_name* or
*vnf\_module\_id* to generate a unique name for each VNF instance. This
prevents the use of unique parameters values for resource “name”
properties to be enumerated in a per instance environment file.

Note that

-  In most cases, only the use of the vnf\_name is necessary to create a
   unique name

-  the Heat pseudo parameter 'OS::stack\_name’ can also be used in the
   ‘str\_replace’ construct to generate a unique name when the vnf\_name
   does not provide uniqueness

.. code-block:: python

    type: OS::Cinder::Volume
        properities:
            name:
                str\_replace:
                    template: VF\_NAME\_STACK\_NAME\_oam\_volume
                    params:
                        VF\_NAME: { get\_param: vnf\_name }
                        STACK\_NAME: { get\_param: 'OS::stack\_name'  }

        type: OS::Neutron::SecurityGroup
        properties:
            description: Security Group of Firewall
            name:
                str\_replace:
                    template: VNF\_NAME\_Firewall\_SecurityGroup
                    params:
                        VNF\_NAME: { get\_param: vnf\_name }

Output Parameters
-----------------

OpenECOMP defines three type of Output Parameters.

Base Template Output Parameters: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The base template output parameters are available for use as input
parameters in all add-on modules. The add-on modules may (or may not)
use these parameters.

Volume Template Output Parameters: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The volume template output parameters are only available only for the
module (base or add on) that the volume is associated with.

Predefined Output Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenECOMP currently defines one predefined output parameter.

OAM Management IP Addresses
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Many VNFs will have a management interface for application controllers
to interact with and configure the VNF. Typically, this will be via a
specific VM that performs a VNF administration function. The IP address
of this interface must be captured and inventoried by OpenECOMP. This
might be a VIP if the VNF contains an HA pair of management VMs, or may
be a single IP address assigned to one VM.

The Heat template may define either (or both) of the following Output
parameters to identify the management IP address.

-  *oam\_management\_v4\_address*

-  *oam\_management\_v6\_address*

*Notes*:

-  The Management IP Address should be defined only once per VNF, so it
   would only appear in one Module template

-  If a fixed IP for the admin VM is passed as an input parameter, it
   may be echoed in the output parameters

-  If the IP for the admin VM is obtained via DHCP, it may be obtained
   from the resource attributes

*Example:*

.. code-block:: python

    resources:
        admin\_server:
            type: OS::Nova::Server
            properties:
                networks:
                    - network: {get\_param: oam\_net\_id }
                ...

    Outputs:
    oam\_management\_v4\_address:
        value: {get\_attr: [admin\_server, networks, {get\_param: oam\_net\_id}, 0] }

Heat Template Constructs
------------------------

External References
-------------------

Heat templates *should not* reference any HTTP-based resource
definitions, any HTTP-based nested configurations, or any HTTP-based
environment files.

-  During orchestration, OpenECOMP *should not* retrieve any such
   resources from external/untrusted/unknown sources.

-  VNF images should not contain such references in user-data or other
   configuration/operational scripts that are specified via Heat or
   encoded into the VNF image itself.

*Note:* HTTP-based references are acceptable if the HTTP-based reference
is accessing information with the VM private/internal network.

Heat Files Support (get\_file)
------------------------------

Heat Templates may contain the inclusion of text files into Heat
templates via the Heat “get\_file” directive. This may be used, for
example, to define a common “user-data” script, or to inject files into
a VM on startup via the “personality” property.

Support for Heat Files is subject to the following limitations:

-  The ‘get\_files’ targets must be referenced in Heat templates by file
   name, and the corresponding files should be delivered to OpenECOMP
   along with the Heat templates.

   -  URL-based file retrieval must not be used; it is not supported.

-  The included files must have unique file names within the scope of
   the VNF.

-  OpenECOMP does not support a directory hierarchy for included files.

   -  All files must be in a single, flat directory per VNF.

-  Included files may be used by all Modules within a given VNF.

-  get\_file directives may be used in both non-nested and nested
   templates

Use of Heat ResourceGroup
-------------------------

The *OS::Heat::ResourceGroup* is a useful Heat element for creating
multiple instances of a given resource or collection of resources.
Typically it is used with a nested Heat template, to create, for
example, a set of identical *OS::Nova::Server* resources plus their
related *OS::Neutron::Port* resources via a single resource in a master
template.

*ResourceGroup* may be used in OpenECOMP to simplify the structure of a
Heat template that creates multiple instances of the same VM type.
However, there are important caveats to be aware of.

*ResourceGroup* does not deal with structured parameters
(comma-delimited-list and json) as one might typically expect. In
particular, when using a list-based parameter, where each list element
corresponds to one instance of the *ResourceGroup*, it is not possible
to use the intrinsic “loop variable” %index% in the *ResourceGroup*
definition.

For instance, the following is **not** valid Heat for a *ResourceGroup*:

.. code-block:: python

    type: OS::Heat::ResourceGroup
        resource:
            type: my\_nested\_vm\_template.yaml
             properties:
                name: {get\_param: [vm\_name\_list, %index%]}

Although this appears to use the nth entry of the *vm\_name\_list* list
for the nth element of the *ResourceGroup*, it will in fact result in a
Heat exception. When parameters are provided as a list (one for each
element of a *ResourceGroup*), you must pass the complete parameter to
the nested template along with the current index as separate parameters.

Below is an example of an **acceptable** Heat Syntax for a
*ResourceGroup*:

.. code-block:: python

    type: OS::Heat::ResourceGroup
    resource:
        type: my\_nested\_vm\_template.yaml
        properties:
            names: {get\_param: vm\_name\_list}
            index: %index%

You can then reference within the nested template as:

{ get\_param: [names, {get\_param: index} ] }

Note that this is workaround has very important limitations. Since the
entire list parameter is passed to the nested template, any change to
that list (e.g., adding an additional element) will cause Heat to treat
the entire parameter as updated within the context of the nested
template (i.e., for each *ResourceGroup* element).  As a result, if
*ResourceGroup* is ever used for scaling (e.g., increment the count and
include an additional element to each list parameter), Heat will often
rebuild every existing element in addition to adding the “deltas”. For
this reason, use of *ResourceGroup* for scaling in this manner is not
supported.

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
previously created by a specific OpenECOMP user ID.

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
generate a public/private pair to be saved and tracked outside of
OpenECOMP). It also removes any access/ownership issues over the created
keypair.

The public keys may be enumerated as a VNF Orchestration Constant in the
environment file (since it is public, it is not a secret key), or passed
at run-time as an instance-specific parameters. OpenECOMP will never
automatically assign a public/private key pair.

*Example (create keypair with an existing ssh public-key for {vm-type}
of lb (for load balancer)):*

.. code-block:: python

    parameters:
        vnf\_name:
            type: string
        ssh\_public\_key:
            type: string
        resources:
        my\_keypair:
            type: OS::Nova::Keypair
            properties:
                name:
                    str\_replace:
                    template: VNF\_NAME\_key\_pair
                    params:
                    VNF\_NAME: { get\_param: vnf\_name }
                public\_key: {get\_param: lb\_ssh\_public\_key}
                save\_private\_key: false

Security Groups
---------------

OpenStack allows a tenant to create Security groups and define rules
within the security groups.

Security groups, with their rules, may either be created in the Heat
template or they can be pre-created in OpenStack and referenced within
the Heat template via parameter(s). There can be a different approach
for security groups assigned to ports on internal (intra-VNF) networks
or external networks (inter-VNF). Furthermore, there can be a common
security group across all VMs for a specific network or it can vary by
VM (i.e., {vm-type}) and network type (i.e., {network-role}).

Anti-Affinity and Affinity Rules
--------------------------------

Anti-affinity or affinity rules are supported using normal OpenStack
*“OS::Nova::ServerGroup”* resources. Separate ServerGroups are typically
created for each VM type to prevent them from residing on the same host,
but they can be applied to multiple VM types to extend the
affinity/anti-affinity across related VM types as well.

*Example:*

In this example, the {network-role} has been defined as “oam” to
represent an oam network and the {vm-type} have been defined as “lb” for
load balancer and “db” for database.

.. code-block:: python

    resources:
        db\_server\_group:
            type: OS::Nova::ServerGroup
            properties:
                name:
                str\_replace:
                    params:
                        $vnf\_name: {get\_param: vnf\_name}
                    template: $vnf\_name-server\_group1
                policies:
                    - *anti-affinity*
            
        lb\_server\_group:
            type: OS::Nova::ServerGroup
            properties:
                name:
                    str\_replace:
                    params:
                        $vnf\_name: {get\_param: vnf\_name}
                    template: $vnf\_name-server\_group2
                policies:
                    - *affinity*

        *db\_0:*
            *type: OS::Nova::Server*
            *properties:*
            *...*
            scheduler\_hints:
                group: {get\_param: db\_server\_group}

        db\_1:
            type: OS::Nova::Server
            properties:
            ...
            scheduler\_hints:
                group: {get\_param: db\_server\_group}

        lb\_0:
            type: OS::Nova::Server
            properties:
            ...
            scheduler\_hints:
                group: {get\_param: lb\_server\_group} 