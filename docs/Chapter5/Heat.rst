.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

Heat
----

General Guidelines
^^^^^^^^^^^^^^^^^^
This section contains general Heat Orchestration Template guidelines.

YAML Format
~~~~~~~~~~~

R-95303 A VNF's Heat Orchestration Template **MUST** be defined
using valid YAML.

YAML (YAML Ain't
Markup Language) is a human friendly data serialization standard for all
programming languages. See http://www.yaml.org/.

Heat Orchestration Template Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As stated above, Heat Orchestration templates must be defined in YAML.

YAML rules include:

 - Tabs are not allowed, use spaces ONLY

 - You must indent your properties and lists with 1 or more spaces

 - All Resource IDs and resource property parameters are
   case-sensitive. (e.g., "ThIs", is not the same as "thiS")

Heat Orchestration Template Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Heat Orchestration template structure follows the following format,
as defined by OpenStack at
https://docs.openstack.org/developer/heat/template_guide/hot_spec.html

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

heat_template_version
+++++++++++++++++++++

R-27078 A VNF's Heat Orchestration template **MUST** contain
the section "heat_template_version:".

The section "heat_template_version:" must be set to a date
that is supported by the OpenStack environment.

description
+++++++++++

R-39402 A VNF's Heat Orchestration Template **MUST**
contain the section "description:".

parameter_groups
++++++++++++++++

A VNF Heat Orchestration template may
contain the section "parameter_groups:".

parameters
++++++++++

R-35414 A VNF Heat Orchestration's template **MUST**
contain the section "parameters:".


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

This section allows for
specifying input parameters that have to be provided when instantiating
the template. Each parameter is specified in a separate nested block
with the name of the parameters defined in the first line and additional
attributes (e.g., type, label) defined as nested elements.

R-90279 A VNF Heat Orchestration's template's parameter **MUST**
be used in a resource with the exception of the parameters
for the OS::Nova::Server resource property availability_zone.

R-91273 A VNF Heat Orchestration’s template’s parameter for
the OS::Nova::Server resource property availability_zone
**MAY NOT** be used in any OS::Nova::Resource.

<param name>
____________

The name of the parameter.

R-25877 A VNF's Heat Orchestration Template's parameter
name (i.e., <param name>) **MUST** contain only
alphanumeric characters and underscores ('_').

type
____

R-36772 A VNF’s Heat Orchestration Template’s parameter
**MUST** include the attribute “type:”.

R-11441 A VNF’s Heat Orchestration Template’s parameter
type **MUST** be one of the following values: "string",
"number", "json", "comma_delimited_list" or "boolean".

label
_____

R-32094 A VNF's Heat Orchestration Template parameter
declaration **MAY** contain the attribute "label:"

description
___________

R-44001 A VNF's Heat Orchestration Template parameter
declaration **MUST** contain the attribute "description".

Note that the parameter attribute “description:” is an
OpenStack optional attribute that provides a description
of the parameter. ONAP implementation requires this attribute.

default
_______

R-90526 A VNF Heat Orchestration Template parameter
declaration **MUST** not contain the default attribute.

R-26124 If a VNF Heat Orchestration Template parameter
requires a default value, it **MUST** be enumerated in the environment file.

Note that the parameter attribute “default:” is an OpenStack
optional attribute that declares the default value of the
parameter. ONAP implementation prohibits the use of this attribute.

hidden
______

R-32557 A VNF's Heat Orchestration Template parameter
declaration MAY contain the attribute "hidden:".

The parameter attribute "hidden:" is an OpenStack optional
attribute that defines whether the parameters should be
hidden when a user requests information about a stack
created from the template. This attribute can be used
to hide passwords specified as parameters.

constraints
___________

The parameter attribute "constraints:" is an OpenStack optional
attribute that defines a list of constraints to apply to the parameter.

R-88863 A VNF's Heat Orchestration Template's parameter defined as
type "number" **MUST** have a parameter constraint of "range" or
"allowed_values" defined.

R-40518 A VNF's Heat Orchestration Template’s parameter defined as
type "string" **MAY** have a parameter constraint defined.

R-96227 A VNF's Heat Orchestration Template’s parameter defined as
type "json" **MAY** have a parameter constraint defined.

R-79817 A VNF's Heat Orchestration Template’s parameter defined as
type "comma_delimited_list" **MAY** have a parameter constraint defined.

R-06613 A VNF's Heat Orchestration Template’s parameter defined as
type "boolean" **MAY** have a parameter constraint defined.

R-00011 A VNF's Heat Orchestration Template's Nested YAML files
parameter's **MUST NOT** have a parameter constraint defined.

The constraints block of a parameter definition defines additional
validation constraints that apply to the value of the parameter.
The parameter values provided in the VNF Heat Orchestration Template
are validated against the constraints at instantiation time.
The stack creation fails if the parameter value doesn’t comply to
the constraints.

The constraints are defined as a list with the following syntax

.. code-block:: python

  constraints:

    <constraint type>: <constraint definition>

    description: <constraint description>

..

**<constraint type>** Provides the type of constraint to apply.
The list of OpenStack supported constraints can be found at
https://docs.openstack.org/heat/latest/template_guide/hot_spec.html .

**<constraint definition>** provides the actual constraint.
The syntax and constraint is dependent of the <constraint type> used.

**description** is an optional attribute that provides a description of the
constraint. The text is presented to the user when the value the user
defines violates the constraint. If omitted, a default validation
message is presented to the user.

Below is a brief overview of the "range" and "allowed values" constraints.
For complete details on constraints, see
https://docs.openstack.org/heat/latest/template_guide/hot_spec.html#parameter-constraints

**range**

range: The range constraint applies to parameters of type: number.
It defines a lower and upper limit for the numeric value of the
parameter. The syntax of the range constraint is

.. code-block:: python

    range: { min: <lower limit>, max: <upper limit> }

..

It is possible to define a range constraint with only a lower
limit or an upper limit.

**allowed_values**

allowed_values: The allowed_values constraint applies to parameters of
type \"string\" or type \"number\". It specifies a set of possible
values for a parameter. At deployment time, the user-provided value
for the respective parameter must match one of the elements of the
list. The syntax of the allowed_values constraint is

.. code-block:: python

    allowed_values: [ <value>, <value>, ... ]

    Alternatively, the following YAML list notation can be used

    allowed_values:

    - <value>

    - <value>

    - ...

. .

immutable
_________

R-22589 A VNF’s Heat Orchestration Template parameter declaration
**MAY** contain the attribute "immutable:".

The parameter attribute \"immutable:\" is an OpenStack optional
attribute that defines whether the parameter is updatable. A Heat
Orchestration Template stack update fails if immutable is set to
true and the parameter value is changed.  This attribute
\"immutable:\" defaults to false.

resources
+++++++++

R-23664 A VNF's Heat Orchestration template **MUST** contain
the section "resources:".

R-90152 A VNF's Heat Orchestration Template's "resources:"
section **MUST** contain the declaration of at least one resource.

R-40551 A VNF's Heat Orchestration Template's Nested YAML files
**MAY** contain the section "resources:".

Each resource is defined as a
separate block in the resources section with the following syntax.

.. code-block:: python

  resources:

    <resource ID>:

      type: <resource type>

      properties:

        <property name>: <property value>

      metadata:

        <resource specific metadata>

      depends_on: <resource ID or list of ID>

      update_policy: <update policy>

      deletion_policy: <deletion policy>

      external_id: <external resource ID>

      condition: <condition name or expression or boolean>



resource ID
___________

R-75141 A VNF's Heat Orchestration Template's resource name
(i.e., <resource ID>) **MUST** only contain alphanumeric
characters and underscores ('_').

R-16447 A VNF's <resource ID> **MUST** be unique across all
Heat Orchestration Templates and all HEAT Orchestration Template
Nested YAML files that are used to create the VNF.

Note that a VNF can be composed of one or more Heat Orchestration Templates.

Note that OpenStack requires the <resource ID> to be unique to the
Heat Orchestration Template and not unique across all Heat
Orchestration Templates the compose the VNF.

type
____

The resource attribute \"type:\" is an OpenStack required
attribute that defines the resource type, such as
OS::Nova::Server or OS::Neutron::Port.

The resource attribute \"type:\" may specify a VNF HEAT
Orchestration Template Nested YAML file.

R-53952 A VNF’s Heat Orchestration Template’s Resource
**MUST NOT** reference a HTTP-based resource definitions.

R-71699 A VNF’s Heat Orchestration Template’s Resource
**MUST NOT** reference a HTTP-based Nested YAML file.

properties
__________

The resource attribute \"properties:\" is an OpenStack optional
attribute that provides a list of resource-specific properties.
The property value can be provided in place, or via a function
(e.g., `Intrinsic functions <https://docs.openstack.org/developer/heat/template_guide/hot_spec.html#hot-spec-intrinsic-functions>`__).

R-10834 If a VNF Heat Orchestration Template resource attribute
"property:" uses a nested "get_param", one level of nesting is
supported and the nested "get_param" **MUST** reference an index

metadata
________

The resource attribute \"metadata:\" is an OpenStack optional attribute.

R-97199 A VNF's Heat Orchestration Template's OS::Nova::Server
resource **MUST** contain the attribute "metadata".

Section 5.4 contains the OS::Nova::Server mandatory and optional metadata.


depends_on
__________

The resource attribute \"depends_on:\" is an OpenStack optional
attribute.
See `OpenStack documentation <https://docs.openstack.org/developer/heat/template_guide/hot_spec.html#hot-spec-resources-dependencies>`__
for additional details.

R-46968 VNF’s Heat Orchestration Template’s Resource **MAY**
declare the attribute “depends_on:”.

update_policy
_____________

R-63137 VNF’s Heat Orchestration Template’s Resource **MAY**
declare the attribute “update_policy:”.

deletion_policy
_______________

R-43740 A VNF’s Heat Orchestration Template’s Resource
**MAY** declare the attribute “deletion_policy:”.

If specified, the \"deletion_policy:\" attribute for resources
allows values 'Delete', 'Retain', and 'Snapshot'.
Starting with heat_template_version 2016-10-14, lowercase
equivalents are also allowed.

The default policy is to delete the physical resource when
deleting a resource from the stack.

external_id
___________

R-78569 A VNF’s Heat Orchestration Template’s Resouce **MAY**
declare the attribute “external_id:”.

This attribute allows for specifying the resource_id for an
existing external (to the stack) resource. External resources
cannot depend on other resources, but we allow other resources to
depend on external resource. This attribute is optional.
Note: when this is specified, properties will not be used for
building the resource and the resource is not managed by Heat.
This is not possible to update that attribute. Also,
resource won’t be deleted by heat when stack is deleted.


condition
_________

The resource attribute \"condition:\" is an OpenStack optional attribute.

Support for the resource condition attribute was added
in the Newton release of OpenStack.

outputs
+++++++

R-36982 A VNF’s Heat Orchestration template **MAY**
contain the “outputs:” section.

This section allows for specifying output parameters
available to users once the template has been instantiated. If the
section is specified, it will need to adhere to specific requirements.
See `ONAP Parameter Classifications Overview`_ and
`ONAP Output Parameter Names`_ for additional details.

Environment File Format
~~~~~~~~~~~~~~~~~~~~~~~

The environment file is a yaml text file.
(https://docs.openstack.org/developer/heat/template_guide/environment.html)

R-86285 The VNF Heat Orchestration Template **MUST** have a corresponding
environment file, even if no parameters are required to be enumerated.

The use of an environment file in OpenStack is optional.
In ONAP, it is mandatory.

R-03324 The VNF Heat Orchestration Template **MUST** contain the
"parameters" section in the
environment file

R-68198 A VNF’s Heat Orchestration template’s Environment File’s
“parameters:” section **MAY** enumerate parameters.

ONAP implementation requires the parameters section in the
environmental file to be declared. The parameters section
contains a list of key/value pairs.

R-59930 A VNF’s Heat Orchestration template’s Environment
File’s **MAY** contain the “parameter_defaults:” section.

The “parameter_defaults:” section contains default parameters
that are passed to all template resources.

R-46096 A VNF’s Heat Orchestration template’s Environment File’s
**MAY** contain the “encrypted_parameters:” section.

The “encrypted_parameters:” section contains a list of encrypted parameters.

R-24893 A VNF’s Heat Orchestration template’s Environment File’s
**MAY** contain the “event_sinks:” section.

The “event_sinks:” section contains the list of endpoints that would
receive stack events.

R-42685 A VNF’s Heat Orchestration template’s Environment File’s
**MAY** contain the “parameter_merge_strategies:” section.

The “parameter_merge_strategies:” section provides the merge strategies
for merging parameters and parameter defaults from the environment file.

R-67231 A VNF’s Heat Orchestration template’s Environment File’s **MUST NOT**
contain the “resource_registry:” section.

ONAP implementation does not support the Environment File
resource_registry section. The resource_registry section
allows for the definition of custom resources.


SDC Treatment of Environment Files
++++++++++++++++++++++++++++++++++

Parameter values enumerated in the environment file are used by SDC as
the default value. However, the SDC user may use the SDC GUI to
overwrite the default values in the environment file.

SDC generates a new environment file for distribution to MSO based on
the uploaded environment file and the user provided GUI updates. The
user uploaded environment file is discarded when the new file is
created.

ONAP has requirements for what parameters must be enumerated in the
environment file and what parameter must not be enumerated in the
environment file. See `ONAP Parameter Classifications Overview`_ and
`ONAP Resource ID and Parameter Naming Convention`_ for more details.

ONAP Heat Orchestration Templates: Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP supports a modular Heat Orchestration Template design pattern,
referred to as *VNF Modularity.*

ONAP VNF Modularity Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

R-69663 A VNF **MAY** be composed from one or more Heat Orchestration
Templates, each of which represents a subset of the overall VNF.

The Heat Orchestration Templates can be thought of a components or
modules of the VNF and are referred to as “\ *VNF Modules*\ ”.
During orchestration, these modules are
deployed incrementally to create the complete VNF.

R-33132 A VNF’s Heat Orchestration Template **MAY** be 1.) Base Module
Heat Orchestration Template (also referred to as a Base Module), 2.)
Incremental Module Heat Orchestration Template (referred to as an Incremental
Module), or 3.) a Cinder Volume Module Heat Orchestration Template
(referred to as Cinder Volume Module).

R-37028 The VNF **MUST** be composed of one “base” module.

R-13196 A VNF **MAY** be composed of zero to many Incremental Modules

R-20974 The VNF **MUST** deploy the base module first, prior to
the incremental modules.

R-28980 A VNF’s incremental module **MAY** be used for initial VNF
deployment only.

R-86926 A VNF’s incremental module **MAY** be used for scale out only.

A VNF’s Incremental Module that is used for scale out is deployed
sometime after initial VNF deployment to add capacity.

R-91497 A VNF’s incremental module **MAY** be used for both deployment
and scale out.

R-68122 A VNF’s incremental module **MAY** be deployed more than once,
either during initial VNF deployment and/or scale out.

R-46119 A VNF’s Heat Orchestration Template’s Resource OS::Heat::CinderVolume
**MAY** be defined in a Base Module.

R-90748 A VNF’s Heat Orchestration Template’s Resource OS::Cinder::Volume
**MAY** be defined in an Incremental Module.

R-03251 A VNF’s Heat Orchestration Template’s Resource OS::Cinder::Volume
**MAY** be defined in a Cinder Volume Module.

ONAP also supports the concept of an optional, independently deployed Cinder
volume via a separate Heat Orchestration Templates, referred to as a Cinder
Volume Module. This allows the volume to persist after a Virtual Machine
(VM) (i.e., OS::Nova::Server) is deleted, allowing the volume to be reused
on another instance (e.g., during a failover activity).

R-11200 The VNF **MUST** keep the scope of a Cinder volume module, when it
exists, to be 1:1 with the VNF Base Module or Incremental Module

It is strongly recommended that Cinder Volumes be created in a Cinder Volume
Module.

R-38474 The VNF **MUST** have a corresponding environment file for a
Base Module.

R-81725 The VNF **MUST** have a corresponding environment file for an
Incremental Module.

R-53433 The VNF **MUST** have a corresponding environment file for a
Cinder Volume Module.

These concepts will be described in more detail throughout the document.
This overview is provided to set the stage and help clarify the concepts
that will be introduced.

Nested Heat Orchestration Templates Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP supports nested Heat Orchestration Templates per OpenStack
specifications.

R-36582 A VNF’s Base Module **MAY** utilize nested heat.

R-56721 A VNF’s Incremental Module **MAY** utilize nested heat.

R-30395 A VNF’s Cinder Volume Module **MAY** utilize nested heat.

Nested templates may be suitable for larger VNFs that contain many
repeated instances of the same VM type(s). A common usage pattern is to
create a nested template for each VM type along with its supporting
resources. The Heat Orchestration Template may then reference these
nested templates either statically (by repeated definition) or
dynamically (via OS::Heat::ResourceGroup).

See `Nested Heat Templates`_ for additional details.

ONAP Heat Orchestration Template Filenames
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to enable ONAP to understand the relationship between Heat
files, the following Heat file naming convention must be utilized.

In the examples below, <text> represents any alphanumeric string that
must not contain any special characters and must not contain the word
“base”.

R-87485 A VNF’s Heat Orchestration Template’s file extension **MUST**
be in the lower case format ‘.yaml’ or ‘.yml’.

R-56438 A VNF’s Heat Orchestration Template’s Nested YAML file extension
**MUST** be in the lower case format ‘.yaml’ or ‘.yml’.

R-74304 A VNF’s Heat Orchestration Template’s Environment file extension
**MUST** be in the lower case format ‘.env’.

Base Modules
++++++++++++

R-81339 A VNF Heat Orchestration Template’s Base Module file name **MUST**
include ‘base’ in the filename and **MUST** match one of the following four
formats: 1.) ‘base_<text>.y[a]ml’, 2.) ‘<text>_base.y[a]ml’, 3.)
‘base.y[a]ml’, or 4.) ‘<text>_base_<text>’.y[a]ml; where ‘base’ is case
insensitive and where ‘<text>’ **MUST** contain only alphanumeric characters
and underscores ‘_’ and **MUST NOT** contain the case insensitive word ‘base’.

R-91342  A VNF Heat Orchestration Template’s Base Module’s Environment File
**MUST** be named identical to the VNF Heat Orchestration Template’s Base
Module with ‘.y[a]ml’ replaced with ‘.env’.

Incremental Modules
+++++++++++++++++++

R-87247 A VNF Heat Orchestration Template’s Incremental Module file name
**MUST** contain only alphanumeric characters and underscores ‘_’ and
**MUST NOT** contain the case insensitive word ‘base’.

R-94509 A VNF Heat Orchestration Template’s Incremental Module’s Environment
File **MUST** be named identical to the VNF Heat Orchestration Template’s
Incremental Module with ‘.y[a]ml’ replaced with ‘.env’.

To clearly identify the incremental module, it is recommended to use the
following naming options for modules:

 -  module_<text>.y[a]ml

 -  <text>_module.y[a]ml

 -  module.y[a]ml

 -  <text>_module_<text>.y[a]ml

Cinder Volume Modules
+++++++++++++++++++++

R-82732 A VNF Heat Orchestration Template’s Cinder Volume Module **MUST** be
named identical to the base or incremental module it is supporting with
‘_volume appended’

R-31141 A VNF Heat Orchestration Template’s Cinder Volume Module’s Environment
File **MUST** be named identical to the VNF Heat Orchestration Template’s
Cinder Volume Module with .y[a]ml replaced with ‘.env’.

Nested Heat file
++++++++++++++++

R-76057 A VNF Heat Orchestration Template’s Nested YAML file name **MUST**
contain only alphanumeric characters and underscores ‘_’ and **MUST NOT**
contain the case insensitive word ‘base’.

Examples include

 -  <text>.y[a]ml

 -  nest_<text>.y[a]ml

 -  <text>_nest.y[a]ml

 -  nest.y[a]ml

 -  <text>_nest_<text>.y[a]ml

VNF Heat Orchestration Template's Nested YAML file does not have a
corresponding environment files, per OpenStack specifications.

R-18224 The VNF Heat Orchestration Template **MUST** pass in as properties
all parameter values
associated with the nested heat file in the resource definition defined
in the parent heat template.

Output Parameters
~~~~~~~~~~~~~~~~~

The output parameters are parameters defined in the output section of a
Heat Orchestration Template. The ONAP output parameters are subdivided
into three categories:

1. ONAP Base Module Output Parameters

2. ONAP Volume Module Output Parameters

3. ONAP Predefined Output Parameters.

ONAP Base Module Output Parameters
++++++++++++++++++++++++++++++++++++

ONAP Base Module Output Parameters are declared in the 'outputs:'' section of
the VNF's Heat Orchestration Template's Base Module. A Base Module Output
Parameter is available as an input parameter (i.e., declared in the
'parameters:'' section) to all Incremental Modules in the VNF.

A Base Module Output Parameter may be used as an input parameter in any
incremental module in the VNF.  Note that the parameter is not
available to other VNFs.

R-52753 VNF’s Heat Orchestration Template’s Base Module’s output parameter’s
name and type **MUST** match the VNF’s Heat Orchestration Template’s
incremental Module’s name and type unless the output parameter is of type
‘comma_delimited_list’, then the corresponding input parameter **MUST**
be declared as type ‘json’.

If the Output parameter has a comma_delimited_list value (e.g., a collection
of UUIDs from a Resource Group), then the corresponding input parameter
must be declared as type json and not a comma_delimited_list, which is
actually a string value with embedded commas.

R-22608 When a VNF’s Heat Orchestration Template’s Base Module’s output
parameter is declared as an input parameter in an Incremental Module,
the parameter attribute ‘constraints:’ **MUST NOT** be declared.

Additional details on ONAP Base Module Output Parameters are provided in
`ONAP Output Parameter Names`_ and ONAP VNF Modularity.

ONAP Volume Module Output Parameters
++++++++++++++++++++++++++++++++++++

R-89913 A VNF’s Heat Orchestration Template’s Cinder Volume Module Output
Parameter(s) **MUST** include the UUID(s) of the Cinder Volumes created in
template, while other Output Parameters **MAY** be included.

A VNF’s Heat Orchestration Template’s Cinder Volume Module Output Parameter(s)
are only available for the module (base or incremental) that the volume
template is associated with.

R-07443 A VNF’s Heat Orchestration Templates’ Cinder Volume Module Output
Parameter’s name and type **MUST** match the input parameter name and type
in the corresponding Base Module or Incremental Module unless the Output
Parameter is of the type ‘comma_delimited_list’, then the corresponding input
parameter **MUST** be declared as type ‘json’.

If the Output parameter has a comma_delimited_list value (e.g., a collection
of UUIDs from a Resource Group), then the corresponding input parameter must
be declared as type json and not a comma_delimited_list, which is actually a
string value with embedded commas.

R-20547 When an ONAP Volume Module Output Parameter is declared as an input
parameter in a base or an incremental module Heat Orchestration Template,
parameter constraints **MUST NOT** be declared.

Additional details on ONAP Base Module Output Parameters are provided in
`ONAP Output Parameter Names`_ and `Cinder Volume Templates`_.

ONAP Predefined Output Parameters
+++++++++++++++++++++++++++++++++++

ONAP will look for a small set of pre-defined Heat output parameters to
capture resource attributes for inventory in ONAP. These output parameters
are optional and currently only two parameters are supported. These output
parameters are optional and are specified in `OAM Management IP Addresses`_.

Support of heat stack update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP does not support the use of heat stack-update command for scaling
(growth/de-growth).

R-39349 A VNF Heat Orchestration Template **MUST NOT** be designed to
utilize the OpenStack ‘heat stack-update’ command for scaling
(growth/de-growth).

R-43413 A VNF **MUST** utilize a modular Heat Orchestration Template
design to support scaling (growth/de-growth).

Scope of a Heat Orchestration Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

R-59482 A VNF’s Heat Orchestration Template **MUST NOT** be VNF instance
specific or Cloud site specific

R-56750 A VNF’s Heat Orchestration Template’s parameter values that are
constant across all deployments **MUST** be declared in a Heat Orchestration
Template Environment File.

ONAP provides the instance specific parameter values to the Heat
Orchestration Template at orchestration time.

R-01896 A VNF’s Heat Orchestration Template’s parameter values that are
constant across all deployments **MUST** be declared in a Heat Orchestration
Template Environment File.

Networking
^^^^^^^^^^

ONAP defines two types of networks: External Networks and Internal Networks.

External Networks
~~~~~~~~~~~~~~~~~

ONAP defines an external network in relation to the VNF and not with regard
to the Network Cloud site. External networks may also be referred to as
“inter-VNF” networks.  An external network must connect VMs in a VNF to
VMs in another VNF or an external gateway or external router.

An External Network may be a Neutron Network or a Contrail Network.

R-16968 A VNF’s Heat Orchestration Templates **MUST NOT** include heat
resources to create external networks.

External networks must be orchestrated separately, independent of the VNF.
This allows the network to be shared by multiple VNFs and managed
independently of VNFs.

R-00606 A VNF **MAY** be connected to zero, one or more than one external
networks.

R-57424 A VNF’s port connected to an external network **MUST** connect the
port to VMs in another VNF and/or an external gateway and/or external router.

R-29865 A VNF’s port connected to an external network **MUST NOT** connect
the port to VMs in the same VNF.

R-69014 When a VNF connects to an external network, a network role, referred
to as the ‘{network-role}’ **MUST** be assigned to the external network
for use in the VNF’s Heat Orchestration Template.

R-05201 When a VNF connects to two or more external networks, each external
network **MUST** be assigned a unique ‘{network-role}’ in the context of
the VNF for use in the VNF’s Heat Orchestration Template.

R-83015 A VNF’s ‘{network-role}’ assigned to an external network **MUST**
be different than the ‘{network-role}’ assigned to the VNF’s internal
networks, if internal networks exist.

ONAP enforces a naming convention for parameters associated with
external networks. `ONAP Resource ID and Parameter Naming Convention`_
provides additional details.

Internal Networks
~~~~~~~~~~~~~~~~~

ONAP defines an internal network in relation to the VNF and not with
regard to the Network Cloud site. Internal networks may also be referred
to as “intra-VNF” networks or “private” networks. An internal network
only connects VMs in a single VNF; it must not connect to other VNFs
or an external gateway or router

R-87096 A VNF **MAY** contain zero, one or more than one internal networks.

R-35666 If a VNF has an internal network, the VNF Heat Orchestration
Template **MUST** include the heat resources to create the internal network.

R-86972 A VNF **SHOULD** create the internal network in the VNF’s Heat
Orchestration Template Base Module.

An Internal Network may be created using Neutron Heat Resources and/or
Contrail Heat Resources.

R-52425 A VNF’s port connected to an internal network **MUST** connect
the port to VMs in the same VNF.

R-46461 A VNF’s port connected to an internal network **MUST NOT** connect
the port to VMs in another VNF and/or an external gateway and/or
external router.

R-68936 When a VNF creates an internal network, a network role, referred to
as the ‘{network-role}’ **MUST** be assigned to the internal network for
use in the VNF’s Heat Orchestration Template.

R-32025 When a VNF creates two or more internal networks, each internal
network **MUST** be assigned a unique ‘{network-role}’ in the context of
the VNF for use in the VNF’s Heat Orchestration Template.

R-69874 A VNF’s ‘{network-role}’ assigned to an internal network **MUST**
be different than the ‘{network-role}’ assigned to the VNF’s external
networks.

R-34726 If a VNF’s port is connected to an internal network and the port
is created in the same Heat Orchestration Template as the internal network,
then the port resource **MUST** use a ‘get_resource’ to obtain
the network UUID.

R-22688  If a VNF’s port is connected to an internal network and the
port is created in an Incremental Module and the internal network is created
in the Base Module then the UUID of the internal network **MUST** be exposed
as a parameter in the ‘outputs:’ section of the Base Module and the port
resource **MUST** use a ‘get_param’ to obtain the network UUID.

ONAP does not programmatically enforce a naming convention for
parameters for internal network. However, a naming convention is
provided that must be followed.
`ONAP Resource ID and Parameter Naming Convention`_
provides additional details.

ONAP Resource ID and Parameter Naming Convention
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section provides the ONAP naming requirements for

1. Resource IDs

2. Resource Property Parameters

{vm-type}
~~~~~~~~~

R-01455 When a VNF's Heat Orchestration Template creates a
Virtual Machine  (i.e., 'OS::Nova::Server'), each 'class' of VMs
**MUST** be assigned a VNF unique '{vm-type}'; where 'class'
defines VMs that **MUST** have the following identical characteristics:

      1.) OS::Nova::Server property flavor value

      2.) OS::Nova::Server property image value

      3.) Cinder Volume attachments
        - Each VM in the 'class' **MUST** have the identical Cinder Volume
          configuration

      4.) Network attachments and IP address requirements
        - Each VM in the 'class' **MUST** have the the identical number
          of ports connecting to the identical networks and requiring the
          identical IP address configuration.

R-82481 A VNF's Heat Orchestration Template's Resource property
parameter that is
associated with a unique Virtual Machine type **MUST**
include '{vm-type}'  as part of the parameter name with two
exceptions:

     1.) The Resource OS::Nova::Server property availability_zone parameter
     **MUST NOT** be prefixed with a common '{vm-type} identifier,

     2.) The Resource OS::Nova::Server eight mandatory and optional metadata
     parameters (vnf_name, vnf_id, vf_module_id, vf_module_name, vm_role,
     vf_module_index, environment_context, workload_context) **MUST NOT**
     be prefixed with a common '{vm-type}' identifier.


R-66729 A VNF’s Heat Orchestration Template’s Resource that is
associated with a unique Virtual Machine type **MUST** include
‘{vm-type}’ as part of the resource ID.

R-98407 A VNF's Heat Orchestration Template's '{vm-type}' **MUST** contain
only alphanumeric characters and/or underscores '_' and
**MUST NOT** contain any of the following strings: '_int' or 'int\_'
or '\_int\_'.

R-48067 A VNF's Heat Orchestration Template's {vm-type} **MUST NOT** be a
substring of {network-role}.

It may cause the Pre-Amsterdam VNF Validation Program (i.e.,
ICE Project) process to produce erroneous error messages.

R-32394 A VNF’s Heat Orchestration Template’s use of ‘{vm-type}’
in all Resource property parameter names **MUST** be the same case.

R-46839 A VNF’s Heat Orchestration Template’s use of
‘{vm-type}’ in all Resource IDs **MUST** be the same case.

R-36687 A VNF’s Heat Orchestration Template’s ‘{vm-type}’ case in
Resource property parameter names **SHOULD** match the case of
‘{vm-type}’ in Resource IDs and vice versa.

{network-role}
~~~~~~~~~~~~~~

The assignment of a {network-role} is discussed in `Networking`_.

R-21330 A VNF’s Heat Orchestration Template’s Resource property
parameter that is associated with external network **MUST**
include the ‘{network-role}’’ as part of the parameter name

R-11168 A VNF's Heat Orchestration Template's Resource ID that is
associated with an external network **MUST** include the
'{network-role}' as part of the resource ID.

R-84322 A VNF's Heat Orchestration Template's Resource property
parameter that is associated with an internal network
**MUST** include 'int\_{network-role}' as part of the parameter
name, where 'int\_' is a hard coded string.

R-96983 A VNF's Heat Orchestration Template's Resource ID that is
associated with an internal network **MUST** include
'int\_{network-role}' as part of the Resource ID, where
'int\_' is a hard coded string.

R-26506 A VNF's Heat Orchestration Template's '{network-role}'
**MUST** contain only alphanumeric characters and/or
underscores '_' and **MUST NOT** contain any of the following
strings: '_int' or 'int\_' or '\_int\_'.

R-00977 A VNF’s Heat Orchestration Template’s ‘{network-role}’
**MUST NOT** be a substring of ‘{vm-type}’.

For example, if a VNF has a ‘{vm-type}’ of ‘oam’ and a
‘{network-role}’ of ‘oam_protected’ would be a violation of the requirement.

R-58424 A VNF’s Heat Orchestration Template’s use of ‘{network-role}’
in all Resource property parameter names **MUST** be the same case

R-21511 A VNF’s Heat Orchestration Template’s use of ‘{network-role}’
in all Resource IDs **MUST** be the same case.

R-86588 A VNF’s Heat Orchestration Template’s ‘{network-role}’ case
in Resource property parameter names **SHOULD** match the case
of ‘{network-role}’ in Resource IDs and vice versa.

Resource IDs
~~~~~~~~~~~~

Requirement R-75141 states a VNF’s Heat Orchestration Template’s
resource name (i.e., <resource ID>) MUST only contain alphanumeric
characters and underscores (‘_’).*

Requirement R-16447 states a VNF’s <resource ID> MUST be unique
across all Heat Orchestration Templates and all HEAT Orchestration
Template Nested YAML files that are used to create the VNF.

As stated previously, OpenStack requires the <resource ID> to be unique
to the Heat Orchestration Template and not unique across all Heat
Orchestration Templates the compose the VNF.

Heat Orchestration Template resources are described in `resources`_

R-54517 When a VNF’s Heat Orchestration Template’s resource is associated
with a single ‘{vm-type}’, the Resource ID **MUST** contain the ‘{vm-type}’.

R-96482 When a VNF’s Heat Orchestration Template’s resource is associated
with a single external network, the Resource ID MUST contain the text
‘{network-role}’.

R-98138 When a VNF’s Heat Orchestration Template’s resource is associated
with a single internal network, the Resource ID MUST contain the text
‘int\_{network-role}’.

R-82115 When a VNF's Heat Orchestration Template's resource is associated
with a single '{vm-type}' and a single external network, the Resource
ID text **MUST** contain both the '{vm-type}' and the '{network-role}'

- the '{vm-type}' **MUST** appear before the '{network-role}' and **MUST**
  be separated by an underscore '_'

   - e.g., '{vm-type}_{network-role}', '{vm-type}_{index}_{network-role}'

- note that an '{index}' value **MAY** separate the '{vm-type}' and the
  '{network-role}' and when this occurs underscores **MUST** separate the
  three values.

R-82551 When a VNF's Heat Orchestration Template's resource is associated
with a single '{vm-type}' and a single internal network, the Resource ID
**MUST** contain both the '{vm-type}' and the 'int\_{network-role}' and

- the '{vm-type}' **MUST** appear before the 'int\_{network-role}' and
  **MUST** be separated by an underscore '_'

   - (e.g., '{vm-type}\_int\_{network-role}',
     '{vm-type}_{index}\_int\_{network-role}')

- note that an '{index}' value **MAY** separate the '{vm-type}' and the
  'int\_{network-role}' and when this occurs underscores **MUST** separate
  the three values.

R-67793 When a VNF’s Heat Orchestration Template’s resource is associated
with more than one ‘{vm-type}’ and/or more than one internal and/or
external network, the Resource ID **MUST NOT** contain the ‘{vm-type}’
and/or ‘{network-role}’/’int\_{network-role}’. It also should contain the
term ‘shared’ and/or contain text that identifies the VNF

R-27970 When a VNF’s Heat Orchestration Template’s resource is associated
with more than one ‘{vm-type}’ and/or more than one internal and/or
external network, the Resource ID **MAY** contain the term ‘shared’
and/or **MAY** contain text that identifies the VNF.

R-11690 When a VNF’s Heat Orchestration Template’s Resource ID contains
an {index} value (e.g. multiple VMs of same {vm-type}), the ‘{index}’
**MUST** start at zero and increment by one.

The table below provides example OpenStack Heat resource ID for
resources only associated with one {vm-type} and/or one network.

The Requirements column states if the Resource ID Format MUST be followed
or SHOULD be followed. Resource ID formats that are marked MUST must be
followed, no deviations are permitted. Resource ID formats that are marked
SHOULD should be followed. However, deviations are permissible to meet
the needs of the VNF’s Heat Orchestration Template.

+-----------------+-------------------------+-------------+------------------+
|Resource Type    |Resource ID Format       | Requirements| Notes            |
|                 |                         |             |                  |
+=================+=========================+=============+==================+
| OS::Cinder::    | {vm-type}\_volume\      | **SHOULD**  |                  |
| Volume          | _{index}                |             |                  |
+-----------------+-------------------------+-------------+------------------+
| OS::Cinder::    | {vm-type}\              | **SHOULD**  |                  |
| VolumeAttachment| _volumeattachment\      |             |                  |
|                 | _{index}                |             |                  |
+-----------------+-------------------------+-------------+------------------+
| OS::Heat::      | {vm-type}_RCC           | **SHOULD**  |                  |
| CloudConfig     |                         |             |                  |
+-----------------+-------------------------+-------------+------------------+
| OS::Heat::      | {vm-type}_RMM           | **SHOULD**  |                  |
| MultipartMime   |                         |             |                  |
+-----------------+-------------------------+-------------+------------------+
| OS::Heat::      | {vm-type}_RRG           | **SHOULD**  |                  |
| ResourceGroup   |                         |             |                  |
+-----------------+-------------------------+-------------+------------------+
|                 | {vm-type}\_{index}\     | **MUST** for| Resource ID for  |
|                 | _subint\_{network-role}\| subinterface| the OS::Heat::   |
|                 | _port\_{index}\         | creation    | ResourceGroup    |
|                 | _subinterfaces          |             | that creates     |
|                 |                         |             | subinterfaces    |
+-----------------+-------------------------+-------------+------------------+
| OS::Heat::      | {vm-type}_RSC           | **SHOULD**  |                  |
| SoftwareConfig  |                         |             |                  |
+-----------------+-------------------------+-------------+------------------+
| OS::Neutron::   | {vm-type}\              | **MUST**    | Resource ID for  |
| Port            | _{vm-type-index}\       |             | port connecting  |
|                 | _{network-role}\_port\  |             | to an external   |
|                 | _{port-index}           |             | network. The     |
|                 |                         |             | {vm-type-index}  |
|                 |                         |             | is the instance  |
|                 |                         |             | of the {vm_type}.|
|                 |                         |             | The {port-index} |
|                 |                         |             | is the instance  |
|                 |                         |             | of the “port” on |
|                 |                         |             | the {vm-type}.   |
|                 |                         |             | There is no index|
|                 |                         |             | after            |
|                 |                         |             | {network_role}   |
|                 |                         |             | since            |
|                 |                         |             | {network-role} is|
|                 |                         |             | unique to the    |
|                 |                         |             | VNF, there should|
|                 |                         |             | only be one      |
|                 |                         |             | instance.        |
+-----------------+-------------------------+-------------+------------------+
|                 | {vm-type}\_{index}\_int\| **MUST**    | Resource ID for  |
|                 | _{network-role}\_port\  |             | port connecting  |
|                 | _{index}                |             | to an internal   |
|                 |                         |             | network. The     |
|                 |                         |             | {index} that     |
|                 |                         |             | follows {vm-type}|
|                 |                         |             | is the instance  |
|                 |                         |             | of the {vm_type}.|
|                 |                         |             | The {index} that |
|                 |                         |             | follows “port” is|
|                 |                         |             | the instance of  |
|                 |                         |             | the “port” on the|
|                 |                         |             | {vm-type}. There |
|                 |                         |             | is no index after|
|                 |                         |             | {network_role}   |
|                 |                         |             | since            |
|                 |                         |             | {network-role} is|
|                 |                         |             | unque to the AIC |
|                 |                         |             | LCP; there should|
|                 |                         |             | only be one      |
|                 |                         |             | instance.        |
+-----------------+-------------------------+-------------+------------------+
|                 | Reserve_Port\_{vm-type}\|             | Resource ID for a|
|                 | _{network-role}\        | **MUST**    | reserve port that|
|                 | _floating_ip\_{index}   |             | is used for an   |
|                 |                         |             | allowed_address  |
|                 | Reserve_Port\_{vm-type}\|             | \_pair. See      |
|                 | _{network-role}\        |             | Section 5.6.5.5  |
|                 | _floating_v6_ip\        |             | for additional   |
|                 | _{index}                |             | details.         |
|                 |                         |             |                  |
|                 |                         |             | There is no      |
|                 |                         |             | {index} that     |
|                 |                         |             | follows {vm-type}|
+-----------------+-------------------------+-------------+------------------+
| OS::Neutron::   | {vm-type}\_Sec\_Grp     | **SHOULD**  | Security Group   |
| SecurityGroup   |                         |             | applicable to one|
|                 |                         |             | {vm-type} and    |
|                 |                         |             | more than one    |
|                 |                         |             | network (internal|
|                 |                         |             | and/or external) |
+-----------------+-------------------------+-------------+------------------+
|                 | {network-role}\_Sec\_Grp| **SHOULD**  | Security Group   |
|                 |                         |             | applicable to    |
|                 |                         |             | more than one    |
|                 |                         |             | {vm-type} and one|
|                 |                         |             | external network |
+-----------------+-------------------------+-------------+------------------+
|                 | int\_{network-role}\    | **SHOULD**  | Security Group   |
|                 | _Sec\_Grp               |             | applicable to    |
|                 |                         |             | more than one    |
|                 |                         |             | {vm-type} and one|
|                 |                         |             | internal network |
+-----------------+-------------------------+-------------+------------------+
|                 | {vm-type}\              | **SHOULD**  | Security Group   |
|                 | _{network-role}\_Sec\   |             | applicable to one|
|                 | _Grp                    |             | {vm-type} and one|
|                 |                         |             | external network |
+-----------------+-------------------------+-------------+------------------+
|                 | {vm-type}\_int\         | **SHOULD**  | Security Group   |
|                 | _{network-role}\_Sec\   |             | applicable to one|
|                 | _Grp                    |             | {vm-type} and one|
|                 |                         |             | internal network |
+-----------------+-------------------------+-------------+------------------+
|                 | Shared\_Sec\_Grp        | **SHOULD**  | Security Group   |
|                 |                         |             | applicable to    |
|                 |                         |             | more than one    |
|                 |                         |             | {vm-type} and    |
|                 |                         |             | more than one    |
|                 |                         |             | network (internal|
|                 |                         |             | and/or external) |
+-----------------+-------------------------+-------------+------------------+
| OS::Neutron::   | int\_{network-role}\    | **MUST**    | VNF Heat         |
| Subnet          | _subnet\_{index}        |             | Orchestration    |
|                 |                         |             | Templates can    |
|                 |                         |             | only create      |
|                 |                         |             | internal         |
|                 |                         |             | networks.        |
+-----------------+-------------------------+-------------+------------------+
| OS::Neutron::Net| int\_{network-role}\    | **MUST**    | VNF Heat         |
|                 | _network                |             | Orchestration    |
|                 |                         |             | Templates can    |
|                 |                         |             | only create      |
|                 |                         |             | internal         |
|                 |                         |             | networks. There  |
|                 |                         |             | is no {index}    |
|                 |                         |             | because          |
|                 |                         |             | {nework-role}    |
|                 |                         |             |should be unique. |
+-----------------+-------------------------+-------------+------------------+
| OS::Nova::      | {vm-type}\_keypair\     | **SHOULD**  | Key Pair         |
| Keypair         | _{index}                |             | applicable to one|
|                 |                         |             | a{vm-type}       |
+-----------------+-------------------------+-------------+------------------+
|                 | {vnf-type}_keypair      | **SHOULD**  | Key Pair         |
|                 |                         |             | applicable to all|
|                 |                         |             | {vm-type} in the |
|                 |                         |             | VNF              |
+-----------------+-------------------------+-------------+------------------+
| OS::Nova::Server| {vm-type}\_server\      | Mandatory   |                  |
|                 | _{index}                |             |                  |
+-----------------+-------------------------+-------------+------------------+
| OS::Nova::      | {vm-type}_RSG           | **SHOULD**  | Both formats are |
| ServerGroup     |                         |             | valid.           |
+-----------------+-------------------------+-------------+------------------+
|                 | {vm-type}_Server_Grp    | **SHOULD**  |                  |
+-----------------+-------------------------+-------------+------------------+
|                 | {vm-type}_ServerGroup   | **SHOULD**  |                  |
+-----------------+-------------------------+-------------+------------------+
| OS::Swift::     | {vm-type}\_RSwiftC      | **SHOULD**  |                  |
| Container       |                         |             |                  |
+-----------------+-------------------------+-------------+------------------+


    Table 2: Example OpenStack Heat Resource ID

The table below provides Resource ID Formats for Contrail heat resources.
 - The Resource ID formats that are marked mandatory must be followed.
   No deviations are permitted.
 - The Resource ID formats that are marked optional should be followed.
   However, deviations in the Resource ID format that is shown is
   permitted.

+-----------------+---------------------+-----------------+-----------------+
|     Resource    | Resource ID         |   Mandatory /   |      Notes      |
|       Type      | Format              |     Optional    |                 |
+=================+=====================+=================+=================+
| OS::ContrailV2: | {vm-type}\_{index}\ | **MUST** –      | The {index}     |
| :InstanceIp     | _{network-role}\    | IPv4 address on | that follows    |
|                 | _vmi\_{index}\      | vmi external    | {vm-type} is    |
|                 | _IP\_{index}        | network         | the instance of |
|                 |                     |                 | the {vm_type}.  |
|                 |                     |                 | The {index}     |
|                 |                     |                 | that follows    |
|                 |                     |                 | “vmi” is the    |
|                 |                     |                 | instance of the |
|                 |                     |                 | “vmi” on the    |
|                 |                     |                 | {vm-type}.      |
|                 |                     |                 | There is no     |
|                 |                     |                 | index after     |
|                 |                     |                 | {network_role}  |
|                 |                     |                 | since since     |
|                 |                     |                 | {network-role}  |
|                 |                     |                 | is unque. The   |
|                 |                     |                 | {index} that    |
|                 |                     |                 | follows the     |
|                 |                     |                 | “IP” is the     |
|                 |                     |                 | instance of the |
|                 |                     |                 | “IP” on the     |
|                 |                     |                 | “vmi”           |
+-----------------+---------------------+-----------------+-----------------+
|                 | {vm-type}\_{index}\ | **MUST** –      |                 |
|                 | _{network-role}\    | IPv6 address on |                 |
|                 | _vmi\_{index}\_v6\  | vmi external    |                 |
|                 | _IP\_{index}        | network         |                 |
+-----------------+---------------------+-----------------+-----------------+
|                 | {vm-type}\_{index}\ | **MUST** –      |                 |
|                 | _int\               | IPv4 address on |                 |
|                 | _{network-role}\    | vmi internal    |                 |
|                 | _vmi\_{index}\_IP\  | network         |                 |
|                 | _{index}            |                 |                 |
+-----------------+---------------------+-----------------+-----------------+
|                 | {vm-type}\_{index}\ | **MUST** –      |                 |
|                 | _int\               | IPv6 address on |                 |
|                 | _{network-role}\    | vmi internal    |                 |
|                 | _vmi\_{index}\_v6\  | network         |                 |
|                 | _IP\_{index}        |                 |                 |
+-----------------+---------------------+-----------------+-----------------+
|                 | {vm-type}\_{index}\ | **MUST** –      |                 |
|                 | _subint\            | IPv4 address on |                 |
|                 | _{network-role}\    | sub-interface   |                 |
|                 | _vmi\_{index}\_IP\  | vmi external    |                 |
|                 | _{index}            | network         |                 |
+-----------------+---------------------+-----------------+-----------------+
|                 | {vm-type}\_{index}\ | **MUST** –      |                 |
|                 | _subint\            | IPv6 address on |                 |
|                 | _{network-role}\    | sub-interface   |                 |
|                 | _vmi\_{index}\_v6\  | vmi external    |                 |
|                 | _IP\_{index}        | network         |                 |
+-----------------+---------------------+-----------------+-----------------+
| OS::ContrailV2: | {network-role}\_RIRT| **MAY**         |                 |
| :InterfaceRoute |                     |                 |                 |
| Table           |                     |                 |                 |
+-----------------+---------------------+-----------------+-----------------+
| OS::ContrailV2: | {network-role}\_RNI | **MAY**         |                 |
| :NetworkIpam    |                     |                 |                 |
+-----------------+---------------------+-----------------+-----------------+
| OS::ContrailV2: | {vm-type}\_RPT      | **MAY**         |                 |
| :PortTuple      |                     |                 |                 |
+-----------------+---------------------+-----------------+-----------------+
| OS::ContrailV2: | {vm-type}\_RSHC\    | **MAY**         |                 |
| :ServiceHealthC | _{LEFT/RIGHT}       |                 |                 |
| heck            |                     |                 |                 |
+-----------------+---------------------+-----------------+-----------------+
| OS::ContrailV2: | {vm-type}\_RST\     | **MAY**         |                 |
| :ServiceTemplat | _{index}            |                 |                 |
| e               |                     |                 |                 |
+-----------------+---------------------+-----------------+-----------------+
| OS::ContrailV2: | {vm-type}\_{index}\ | **MUST** - vmi  | Resource ID for |
| :VirtualMachine | _{network-role}\    | attached to an  | virtual machine |
| Interface       | _vmi\_{index}       | external        | interface (vmi) |
|                 |                     | network         | connecting to   |
|                 |                     |                 | an external     |
|                 |                     |                 | network. The    |
|                 |                     |                 | {index} that    |
|                 |                     |                 | follows         |
|                 |                     |                 | {vm-type} is    |
|                 |                     |                 | the instance of |
|                 |                     |                 | the {vm_type}.  |
|                 |                     |                 | The {index}     |
|                 |                     |                 | that follows    |
|                 |                     |                 | “vmi” is the    |
|                 |                     |                 | instance of the |
|                 |                     |                 | “vmi” on the    |
|                 |                     |                 | {vm-type}.      |
|                 |                     |                 | There is no     |
|                 |                     |                 | index after     |
|                 |                     |                 | {network_role}  |
|                 |                     |                 | since since     |
|                 |                     |                 | {network-role}  |
|                 |                     |                 | is unque to the |
|                 |                     |                 | AIC LCP; there  |
|                 |                     |                 | should only be  |
|                 |                     |                 | one instance.   |
+-----------------+---------------------+-----------------+-----------------+
|                 | {vm-type}\_{index}\ | **MUST** - vmi  |                 |
|                 | _int\               | attached to an  |                 |
|                 | _{network-role}\    | internal        |                 |
|                 | _vmi\_{index}       | network         |                 |
+-----------------+---------------------+-----------------+-----------------+
|                 | {vm-type}\_{index}\ | **MUST** - vmi  |                 |
|                 | _subint\            | attached to a   |                 |
|                 | _{network-role}\    | sub-interface   |                 |
|                 | _vmi\_{index}       | network         |                 |
+-----------------+---------------------+-----------------+-----------------+
| OS::ContrailV2: | int\_{network-role}\| **MAY**         | VNF Heat        |
| :VirtualNetwork | _RVN                |                 | Orchestration   |
|                 |                     |                 | Templates can   |
|                 |                     |                 | only create     |
|                 |                     |                 | internal        |
|                 |                     |                 | networks. There |
|                 |                     |                 | is no {index}   |
|                 |                     |                 | because         |
|                 |                     |                 | {nework-role}   |
|                 |                     |                 | should be       |
|                 |                     |                 | unique. Both    |
|                 |                     |                 | formats are     |
|                 |                     |                 | valid.          |
+-----------------+---------------------+-----------------+-----------------+
|                 | int\_{network-role}\| **MAY**         |                 |
|                 | _network            |                 |                 |
+-----------------+---------------------+-----------------+-----------------+

    Table 3: Example Contrail Heat resource ID

There is a use case where the template filename is used as the type: as
shown in the example below.  There is no suggested Resource ID naming
convention for this use case.

Example:  Template Filename used as the type:

.. code-block:: python

  heat_template_version: 2015-04-30

  resources:
    <Resource ID>:
      type: file.yaml
      properties:
        ...

Resource: OS::Nova::Server - Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The resource OS::Nova::Server manages the running virtual machine (VM)
instance within an OpenStack cloud. (See
https://docs.openstack.org/developer/heat/template_guide/openstack.html#OS::Nova::Server.)

Four properties of this resource must follow the ONAP parameter naming
convention. The four properties are:

1. image

2. flavor

3. name

4. availability\_zone

Requirement R-01455 defines how the ‘{vm-type]’ is defined.

Requirement R-82481 defines how the ‘{vm-type} is used.’

The table below provides a summary. The sections that follow provides
the detailed requirements.

.. csv-table:: **Table 4 OS::Nova::Server Resource Property Parameter Naming Convention**
   :header: Property Name,Parameter Type,Parameter Name,Parameter Value Provided to Heat
   :align: center
   :widths: auto

   image, string, {vm-type}\_image\_name, Environment File
   flavor, string, {vm-type}\_flavor\_name, Environment File
   name, string, {vm-type}\_name\_{index}, ONAP
   name, CDL, {vm-type}_names, ONAP
   availability_zone, string, availability\_zone\_{index}, ONAP

Property: image
+++++++++++++++

R-71152 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘image’ parameter **MUST** be declared as
type: ‘string’.

R-58670 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘image’ parameter name **MUST** follow the
naming convention ‘{vm-type}_image_name’.

R-91125 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘image’ parameter **MUST** be enumerated in
the Heat Orchestration Template’s Environment File and a value **MUST** be
assigned.

R-57282 Each VNF’s Heat Orchestration Template’s ‘{vm-type}’
**MUST** have a unique parameter name for the ‘OS::Nova::Server’
property ‘image’ even if more than one {vm-type} shares the same image.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     {vm-type}_image_name:
         type: string
         description: {vm-type} server image

Property: flavor
++++++++++++++++

R-50436 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘flavor’ parameter **MUST** be declared as
type: ‘string’.

R-45188 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘flavor’ parameter name **MUST** follow the
naming convention ‘{vm-type}_flavor_name’.

R-69431 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘flavor’ parameter **MUST** be enumerated in the
Heat Orchestration Template’s Environment File and a value **MUST** be
assigned.

R-40499 Each VNF’s Heat Orchestration Template’s ‘{vm-type}’ **MUST**
have a unique parameter name for the ‘OS::Nova::Server’ property
‘flavor’ even if more than one {vm-type} shares the same flavor.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     {vm-type}_flavor_name:
         type: string
         description: {vm-type} flavor

Property: Name
++++++++++++++

R-51430 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘name’ parameter **MUST** be declared as
either type ‘string’ or type ‘comma_delimited_list”.

R-54171 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘name’ parameter is defined as a ‘string’,
the parameter name **MUST** follow the naming convention
‘{vm-type}\_name\_{index}’, where {index} is a numeric value that starts
at zero and increments by one.

R-40899 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘name’ parameter is defined as a ‘string’,
a parameter **MUST** be declared for each ‘OS::Nova::Server’ resource
associated with the ‘{vm-type}’.

R-87817 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘name’ parameter is defined as a
‘comma_delimited_list’, the parameter name **MUST** follow the naming
convention ‘{vm-type}_names’.

R-85800 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘name’ parameter is defined as a
‘comma_delimited_list’, a parameter **MUST** be delcared once for all
‘OS::Nova::Server’ resources associated with the ‘{vm-type}’.

R-22838 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘name’ parameter **MUST NOT** be enumerated
in the Heat Orchestration Template’s Environment File.

If a VNF’s Heat Orchestration Template’s contains more than three
OS::Nova::Server resources of a given {vm-type}, the comma_delimited_list
form of the parameter name (i.e., ‘{vm-type}_names’) should be used to
minimize the number of unique parameters defined in the template.


*Example: Parameter Definition*

.. code-block:: python

  parameters:

  {vm-type}_names:
    type: comma_delimited_list
    description: VM Names for {vm-type} VMs

  {vm-type}_name_{index}:
    type: string
    description: VM Name for {vm-type} VM {index}

*Example: comma_delimited_list*

In this example, the {vm-type} has been defined as “lb” for load balancer.

.. code-block:: python

  parameters:

    lb_names:
      type: comma_delimited_list
      description: VM Names for lb VMs

  resources:
    lb_server_0:
      type: OS::Nova::Server
      properties:
        name: { get_param: [lb_names, 0] }
        ...

    lb_server_1:
      type: OS::Nova::Server
      properties:
        name: { get_param: [lb_names, 1] }
        ...

*Example: fixed-index*

In this example, the {vm-type} has been defined as “lb” for load balancer.

.. code-block:: python

  parameters:

    lb_name_0:
      type: string
      description: VM Name for lb VM 0

    lb_name_1:
      type: string
      description: VM Name for lb VM 1

  resources:

    lb_server_0:
      type: OS::Nova::Server
      properties:
        name: { get_param: lb_name_0 }
        ...

    lb_server_1:
      type: OS::Nova::Server
      properties:
        name: { get_param: lb_name_1 }
        ...

Contrail Issue with Values for OS::Nova::Server Property Name
_____________________________________________________________

R-44271 The VNF's Heat Orchestration Template's Resource
'OS::Nova::Server' property 'name' parameter value **SHOULD NOT**
contain special characters since the Contrail GUI has a limitation
displaying special characters.

However, if special characters must be used, the only special characters
supported are:

--- \" ! $ ' (\ \ ) = ~ ^ | @ ` { } [ ] > , . _


Property: availability\_zone
++++++++++++++++++++++++++++

R-98450 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘availability_zone’ parameter name
**MUST** follow the naming convention ‘availability\_zone\_{index}’
where the ‘{index}’ **MUST** start at zero and increment by one.

R-23311 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘availability_zone’ parameter **MUST**
be declared as type: ‘string’.

The parameter must not be declared as type ‘comma_delimited_list’,
ONAP does not support it.

R-59568  The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘availability_zone’ parameter **MUST NOT**
be enumerated in the Heat Orchestration Template’s Environment File.

Example Parameter Definition

.. code-block:: python

  parameters:
    availability_zone_{index}:
      type: string
      description: availability zone {index} name

Requirement R-90279 states that a VNF Heat Orchestration’s template’s
parameter MUST be used in a resource with the exception of the parameters
for the OS::Nova::Server resource property availability_zone.

R-01359 A VNF’s Heat Orchstration Template that contains an
‘OS::Nova:Server’ Resource **MAY** define a parameter for the property
‘availability_zone’ that is not utilized in any ‘OS::Nova::Server’
resources in the Heat Orchestration Template.

Example
+++++++

The example below depicts part of a Heat Orchestration Template that
uses the four OS::Nova::Server properties discussed in this section.

In the Heat Orchestration Template below, four Virtual
Machines (OS::Nova::Server) are created: two dns servers with
{vm-type} set to “dns” and two oam servers with {vm-type} set to “oam”.
Note that the parameter associated with the property name is a
comma_delimited_list for dns and a string for oam.

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

Boot Options
++++++++++++

R-99798 A VNF’s Heat Orchestration Template’s Virtual Machine
(i.e., OS::Nova::Server Resource) **MAY** boot from an image or **MAY**
boot from a Cinder Volume.

R-83706 When a VNF’s Heat Orchestration Template’s Virtual Machine
(i.e., ‘OS::Nova::Server’ Resource) boots from an image, the
‘OS::Nova::Server’ resource property ‘image’ **MUST** be used.

The requirements associated with
the 'image' property are detailed in `Property: image`_

R-69588 When a VNF’s Heat Orchestration Template’s Virtual Machine
(i.e., ‘OS::Nova::Server’ Resource) boots from Cinder Volume, the
‘OS::Nova::Server’ resource property ‘block_device_mapping’ or
‘block_device_mapping_v2’ **MUST** be used.

There are currently no heat guidelines
associated with these two properties:
'block_device_mapping' and 'block_device_mapping_v2'.

Resource: OS::Nova::Server – Metadata Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The OS::Nova::Server Resource property metadata is an optional
OpenStack property.
The table below summarizes the mandatory and optional metadata
supported by ONAP.

The sections that follow provides the requirements associated with each
metadata parameter.

.. csv-table:: **Table 5 OS::Nova::Server Mandatory and Optional Metadata**
   :header: Metadata Parameter Name, Parameter Type, Required, Parameter Value Provided to Heat
   :align: center
   :widths: auto

   vnf_id, string, **MUST**, ONAP
   vf_module_id, string, **MUST**, ONAP
   vnf_name, string, **MUST**, ONAP
   vf_module_name, string, **SHOULD**, ONAP
   vm_role, string, **MAY**, YAML or Environment File
   vf_module_index, string, **MAY**, ONAP
   workload_context, string, **SHOULD**, ONAP
   environment_context, string, **SHOULD**, ONAP

vnf\_id
+++++++

The OS::Nova::Server Resource metadata map value parameter 'vnf_id'
is an ONAP generated UUID that identifies the VNF.  The value
is provided by ONAP to the VNF's Heat Orchestration
Template at orchestration time.

R-37437 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **MUST** contain the metadata map value parameter ‘vnf_id’.

R-07507 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_id’ **MUST** be declared
as type: ‘string’.

R-55218 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_id’ **MUST NOT** have
parameter contraints defined.

R-20856 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_id’ **MUST NOT** be
enumerated in the Heat Orchestration Template’s environment file.

R-44491 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_id’ is passed into a
Nested YAML file, the parameter name ‘vnf_id’ **MUST NOT** change.


*Example 'vnf_id' Parameter Definition*

.. code-block:: python

  parameters:

    vnf_id:
      type: string
      description: Unique ID for this VNF instance

vf\_module\_id
++++++++++++++

The OS::Nova::Server Resource metadata map value parameter 'vf\_module\_id'
is an ONAP generated UUID that identifies the VF Module (e.g., Heat
Orchestration Template).  The value
is provided by ONAP to the VNF's Heat Orchestration
Template at orchestration time.

R-71493 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **MUST** contain the metadata map value parameter
‘vf\_module\_id’.

R-82134 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_id’ **MUST**
be declared as type: ‘string’.

R-98374 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_id’ **MUST NOT**
have parameter contraints defined.

R-72871 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_id’ **MUST NOT**
be enumerated in the Heat Orchestration Template’s environment file.

R-86237 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf_module_id’ is passed
into a Nested YAML file, the parameter name ‘vf\_module\_id’
**MUST NOT** change.

*Example 'vf\_module\_id' Parameter Definition*

.. code-block:: python

  parameters:

    vnf_module_id:
      type: string
      description: Unique ID for this VNF module instance


vnf\_name
+++++++++

The OS::Nova::Server Resource metadata map value parameter 'vnf_name'
is the ONAP generated alphanumeric name of the deployed VNF instance.
The value
is provided by ONAP to the VNF's Heat Orchestration
Template at orchestration time.
The parameter must be declared as type: string

R-72483 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **MUST** contain the metadata map value parameter
‘vnf_name’.

R-62428 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_name’ **MUST** be
declared as type: ‘string’.

R-44318 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_name’ **MUST NOT** have
parameter contraints defined.

R-36542 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_name’ **MUST NOT** be
enumerated in the Heat Orchestration Template’s environment file.

R-16576 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_name’ is passed into a
Nested YAML file, the parameter name ‘vnf_name’ **MUST NOT** change.

*Example 'vnf_name' Parameter Definition*

.. code-block:: python

  parameters:

    vnf_name:
      type: string
      description: Unique name for this VNF instance

vf\_module\_name
++++++++++++++++

The OS::Nova::Server Resource metadata map value parameter 'vf_module_name'
is the deployment name of the heat stack created (e.g., <STACK_NAME>) from the
VNF's Heat Orchestration template
in the command 'Heat stack-create'
(e.g., 'Heat stack-create [-f <FILE>] [-e <FILE>] <STACK_NAME>').
The 'vf_module_name' (e.g., <STACK_NAME> is specified as
part of the orchestration process.

R-68023 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **SHOULD** contain the metadata map value parameter
‘vf\_module\_name’.

R-39067 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_name’ **MUST**
be declared as type: ‘string’.

R-15480 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_name’
**MUST NOT** have parameter contraints defined.

R-80374 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_name’
**MUST NOT** be enumerated in the Heat Orchestration Template’s
environment file.

R-49177 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_name’ is passed
into a Nested YAML file, the parameter name ‘vf\_module\_name’
**MUST NOT** change.

*Example 'vf_module_name' Parameter Definition*

.. code-block:: python

  parameters:

    vf_module_name:
      type: string
      description: Unique name for this VNF Module instance

vm\_role
++++++++

The OS::Nova::Server Resource metadata map value parameter 'vm-role'
is a metadata tag that describes the role of the Virtual Machine.
The 'vm_role' is stored in ONAP's A&AI module and is
available for use by other ONAP components and/or north bound systems.

R-85328 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **MAY** contain the metadata map value parameter ‘vm_role’.

R-95430 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vm_role’ **MUST** be
declared as type: ‘string’.

R-67597 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vm_role’ **MUST NOT** have
parameter contraints defined.

R-46823 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_name’ **MUST** be
either

 - enumerated in the VNF’s Heat Orchestration
   Template’s environment file.

 - hard coded in the VNF’s Heat Orchestration
   Template’s OS::Nova::Resource metadata property.

Defining the 'vm_role' as the '{vm-type}' is a recommended convention

R-86476 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vm_role’ value **MUST only**
contain alphanumeric characters and underscores ‘_’.

R-70757 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vm_role’ is passed into a
Nested YAML file, the parameter name ‘vm_role’ **MUST NOT** change.


*Example 'vm_role' Parameter Definition*

.. code-block:: python

  parameters:

    vm_role:
      type: string
      description: Unique role for this VM

*Example: 'vm-role' Definition: Hard Coded in
OS::Nova::Resource metadata property*

.. code-block:: python

  resources:

    dns_server_0
      type: OS::Nova::Server
      properties:
        . . . .
        metadata:
          vm_role: dns

*Example 'vm-role' Definition: Defined in Environment file
and retrieved via 'get_param'*

.. code-block:: python

  resources:

    dns_server_0:
      type: OS::Nova::Server
      properties:
        . . . .
        metadata:
          vm_role: { get_param: vm_role }

Example vnf_id, vf_module_id, vnf_name, vf_module_name, vm_role
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The example below depicts part of a Heat Orchestration Template
that uses the five of the OS::Nova::Server metadata parameter
discussed in this section. The {vm-type} has been defined as lb
for load balancer.

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
    lb_server_0:
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

vf\_module\_index
+++++++++++++++++

R-50816 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **MAY** contain the metadata map value parameter
‘vf\_module\_index’.

R-54340 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_index’ **MUST** be
declared as type: ‘number’.

R-09811 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_index’ **MUST NOT**
have parameter contraints defined.

R-37039 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_index’ **MUST NOT**
be enumerated in the Heat Orchestration Template’s environment file.

R-22441 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_index’ is passed
into a Nested YAML file, the parameter name ‘vf\_module\_index’
**MUST NOT** change.

R-55306 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_index’ **MUST NOT** be
used in a VNF’s Volume Template; it is not supported.

The vf_module_index parameter indicates which instance of the module is being
deployed into the VNF.
This parameter may be used in cases where multiple instances of the same
incremental module may be instantiated for scaling purposes. The index
can be used in the Heat Orchestration Template for indexing into a
pseudo-constant array parameter when unique values are required for each
module instance, e.g., for fixed private IP addresses on VM types.

The vf_module_index will start at 0 for the first instance of a module
type. Subsequent instances of the same module type will receive the
lowest unused index. This means that indexes will be reused if a module
is deleted and re-added. As an example, if three copies of a module are
deployed with vf_module_index values of 0, 1, and 2 then subsequently
the second one is deleted (index 1), and then re-added, index 1 will be
reused.

*Example*

In this example, the {vm-type} has been defined as oam_vm to represent
an OAM VM. An incremental heat module is used to deploy the OAM VM. The
OAM VM attaches to an internal control network which has a
{network-role} of ctrl. A maximum of four OAM VMs can be deployed. The
environment file contains the four IP addresses that each successive OAM
VM will be assigned. The vf_module_index is used as the index to
determine the IP assignment.

Environment File

.. code-block:: python

  parameters:
    oam_vm_int_ctrl_ips: 10.10.10.1,10.10.10.2,10.10.10.3,10.10.10.4

YAML File

.. code-block:: python

  parameters:
    vf_module_index:
      type: number
      description: Unique index for this VNF Module instance
    oam_vm_name_0:
      type: string
      description: VM Name for lb VM 0
    int_ctrl_net_id:
      type: string
      description: Neutron UUID for the internal control network
    oam_vm_int_ctrl_ips:
      type: comma_delimited_list
      description: Fixed IP assignments for oam VMs on the internal control
      network
  resources:
    oam_vm_server_0:
      type: OS::Nova::Server
      properties:
        name: { get_param: oam_vm_name_0 }
        networks:
          - port: { get_resource: oam_vm_0_int_ctrl_port_0 }
        . . .
        metadata:
          vf_module_index: { get_param: vf_module_index }
    oam_vm_0_int_ctrl_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: int_ctrl_net_id }
        fixed_ips: [ { “ip_address”: {get_param: [ oam_vm_int_ctrl_ips, { get_param, vf_module_index]}}}]

workload_context
++++++++++++++++

R-47061 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **SHOULD** contain the metadata map value parameter
‘workload_context’.

R-74978 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘workload_context’ **MUST** be
declared as type: ‘string’.

R-34055 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘workload_context’ **MUST NOT**
have parameter contraints defined.

R-02691 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘workload_context’ **MUST NOT**
be enumerated in the Heat Orchestration Template’s environment file.

R-75202 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘workload_context’ is passed
into a Nested YAML file, the parameter name ‘workload_context’
**MUST NOT** change.

The 'workload_context' parameter value will be chosen by the Service Model
Distribution context client in VID and will be supplied to the
Heat Orchestration Template by ONAP at orchestration time.

*Example Parameter Definition*

.. code-block:: python

  parameters:
    workload_context:
      type: string
      description: Workload Context for this VNF instance


*Example OS::Nova::Server with metadata*

.. code-block:: python

  resources:
    . . .

    {vm-type}_server_{index}:
       type: OS::Nova::Server
       properties:
         name:
         flavor:
         image:
        ...
       metadata:
          vnf_name: { get_param: vnf_name }
          vnf_id: { get_param: vnf_id }
          vf_module_name: { get_param: vf_module_name }
          vf_module_id: { get_param: vf_module_id }
          workload_context: {get_param: workload_context}

environment_context
+++++++++++++++++++

R-88536 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **SHOULD** contain the metadata map value parameter
‘environment_context’.

R-20308 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘environment_context’ **MUST**
be declared as type: ‘string’.

R-56183 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘environment_context’ **MUST NOT**
have parameter contraints defined.

R-13194 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘environment_context’ **MUST NOT**
be enumerated in the Heat Orchestration Template’s environment file.

R-62954 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘environment_context’ is
passed into a Nested YAML file, the parameter name
‘environment_context’ **MUST NOT** change.

The 'environment_context' parameter value will be defined by the
service designer as part of the service model during the SDC
on-boarding process and will be supplied to the Heat Orchestration
Template by ONAP at orchestration time.


*Example Parameter Definition*

.. code-block:: python

  parameters:
    environment_context:
      type: string
      description: Environment Context for this VNF instance


*Example OS::Nova::Server with metadata*

.. code-block:: python

  resources:
    . . .

    {vm-type}_server_{index}:
       type: OS::Nova::Server
       properties:
         name:
         flavor:
         image:
        ...
       metadata:
          vnf_name: { get_param: vnf_name }
          vnf_id: { get_param: vnf_id }
          vf_module_name: { get_param: vf_module_name }
          vf_module_id: { get_param: vf_module_id }
          workload_context: {get_param: workload_context}
          environment_context: {get_param: environment_context }


Resource: OS::Neutron::Port - Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The resource OS::Neutron::Port is for managing Neutron ports (See
https://docs.openstack.org/developer/heat/template_guide/openstack.html#OS::Neutron::Port.)

Introduction
++++++++++++

Four properties of the resource OS::Neutron::Port that must follow the
ONAP parameter naming convention. The four properties are:

1. network
2. fixed_ips, ip_address
3. fixed_ips, subnet_id or fixed_ips, subnet

 * Note that in many examples in this document fixed_ips, subnet_id is used.

4. allowed_address_pairs, ip_address

Below is a generic example. Note that for some parameters
comma_delimited_list are supported in addition to String.

.. code-block:: python

  resources:

  ...

  <resource ID>:
    type: OS::Neutron::Port
    properties:
      allowed_address_pairs: [{"ip_address": String, "mac_address": String},
      {"ip_address": String, "mac_address": String}, ...]
      fixed_ips: [{"ip_address": String, "subnet_id": String, "subnet":
      String}, {"ip_address": String, "subnet_id": String, "subnet": String},
      ...]
      network: String

The parameters associated with these properties may reference an
external network or internal network. External networks and internal
networks are defined in `Networking`_.

When the OS::Neutron::Port is attaching to an external network, all
property values are parameters that are retrieved via the intrinsic
function 'get_param'.

When the OS::Neutron::Port is attaching to an internal network, a
property value maybe retrieved via the intrinsic
function 'get_param', 'get_resource', or 'get_attr'.

This will be described in the forth coming sections.

Items to Note
_____________

A network (internal or external) may contain one or or more subnets.

A VNF can have one or more ports connected to the same network.

A port can have one or more IP addresses assigned.

The IP address assignments can be IPv4 addresses and/or IPv6 addresses.

The IP addresses assignments for a unique external network **MUST**
be all Cloud Assigned addresses OR **MUST** be all ONAP
SDN-C assigned IP addresses.

If the IP addresses are Cloud Assigned, all the IPv4 Addresses **MUST**
be from
the same subnet and all the IPv6 Addresses **MUST** be from the
same subnet.

If the IP addresses are ONAP SDN-C assigned,
the IPv4 Addresses **MAY**
be from
different subnets and the IPv6 Addresses **MAY** be from different
subnets.

If a VNF's Port is attached to an external network the IP addresses **MAY**
either be assigned by

 1. ONAP's SDN-Controller (SDN-C)
 2. Cloud Assigned by OpenStack’s DHCP Service

If a VNF's Port is attached to an external network and the port's IP addresses
are assigned by ONAP's SDN-Controller, the 'OS::Neutron::Port' Resource's

 * property 'fixed_ips' map property 'ip_address' **MUST** be used
 * property 'fixed_ips' map property 'subnet'/'subnet_id' **MUST NOT** be used

If a VNF's Port is attached to an external network and the port's IP addresses
are Cloud Assigned by OpenStack’s DHCP Service,
the 'OS::Neutron::Port' Resource's

 * property 'fixed_ips' map property 'ip_address' **MUST NOT** be used
 * property fixed_ips' map property 'subnet'/'subnet_id' **MAY** be used

If a VNF's Port is attached to an internal network and the port's IP addresses
are assigned by the VNF's Heat Orchestration Template
(i.e., enumerated in the Heat Orchestration Template's environment file),
the 'OS::Neutron::Port' Resource's

 * property 'fixed_ips' map property 'ip_address' **MUST** be used
 * property 'fixed_ips' map property 'subnet'/'subnet_id'
   **MUST NOT** be used

If a VNF's Port is attached to an internal network and the port's IP addresses
are Cloud Assigned by OpenStack’s DHCP Service,
the 'OS::Neutron::Port' Resource's

 * property 'fixed_ips' map property 'ip_address' **MUST NOT** be used
 * property 'fixed_ips' map property 'subnet'/'subnet_id' **MAY** be used

If a VNF's Heat Orchestration Template 'OS::Neutron::Port' Resource property
'fixed_ips' map property 'ip_address' is specified, then the
'fixed_ips' map property 'subnet'/'subnet_id' **MUST NOT**
be specified.

If a VNF's Heat Orchestration Template 'OS::Neutron::Port' Resource property
'fixed_ips' map property 'subnet'/'subnet_id' is specified, then the
'fixed_ips' map property 'ip_address' **MUST NOT**
be specified.

.. csv-table:: **Table 4 OS::Nova::Server Resource Property Parameter Naming Convention**
   :header: Resource,Property,Parameter Type,Parameter Name,Parameter Value Provided to Heat
   :align: center
   :widths: auto

   OS::Nova::Server, image, string, {vm-type}_image_name, Environment File

Property: network
+++++++++++++++++

The Resource 'OS::Neutron::Port' property 'network' determines what network
the port is attached to.


R-18008 The VNF’s Heat Orchestration Template’s Resource ‘OS::Neutron::Port’
property ‘network’ parameter **MUST** be declared as type: ‘string’.

R-62983 When the VNF’s Heat Orchestration Template’s
Resource ‘OS::Neutron::Port’ is attaching to an external network,
the ‘network’ parameter name **MUST**

- follow the naming convention ‘{network-role}_net_id’ if the Neutron
  network UUID value is used to reference the network
- follow the naming convention ‘{network-role}_net_name’ if the OpenStack
  network name is used to reference the network.

where ‘{network-role}’ is the network-role of the external network and
a ‘get_param’ **MUST** be used as the intrinsic function.

R-86182 When the VNF’s Heat Orchestration Template’s
Resource ‘OS::Neutron::Port’ is attaching to an internal network,
and the internal network is created in a different
Heat Orchestration Template than the ‘OS::Neutron::Port’, the ‘network’
parameter name **MUST**

- follow the naming convention ‘int\_{network-role}_net_id’ if the Neutron
  network UUID value is used to reference the network
- follow the naming convention ‘int\_{network-role}_net_name’ if the
  OpenStack network name in is used to reference the network.

where ‘{network-role}’ is the network-role of the internal network
and a ‘get_param’ **MUST** be used as the intrinsic function.

In Requirement R-86182, the internal network is created in the VNF's
Base Module (Heat Orchestration Template) and the parameter name is
declared in the Base Module's outputs' section.
The output parameter name will be declared as a parameter in the
'parameters' section of the incremental module.

R-93177 When the VNF’s Heat Orchestration Template’s
Resource ‘OS::Neutron::Port’ is attaching to an internal
network, and the internal network is created in the same Heat
Orchestration Template than the ‘OS::Neutron::Port’, the ‘network’
parameter name **MUST** obtain the UUID of the internal network
by using the intrinsic function ‘get_resource’ or ‘get_attr’
and referencing the Resource ID of the internal network.

R-29872 The VNF’s Heat Orchestration Template’s Resource ‘OS::Nova::Server’
property ‘network’ parameter **MUST NOT** be enumerated in the Heat
Orchestration Template’s Environment File.

The parameter values for external networks are provided by ONAP
to the VNF's Heat Orchestration Template at orchestration time.

The parameter values for internal networks created in the VNF's Base Module
Heat Orchestration Template
are provided to the VNF's Incremental Module Heat Orchestration Template
at orchestration time.

*Example Parameter Definition of External Networks*

.. code-block:: python

  parameters:

    {network-role}_net_id:
      type: string
      description: Neutron UUID for the external {network-role} network

    {network-role}_net_name:
      type: string
      description: Neutron name for the external {network-role} network


*Example Parameter Definition of Internal Networks in an Incremental Module*

.. code-block:: python

  parameters:

    int_{network-role}_net_id:
      type: string
      description: Neutron UUID for the internal int_{network-role} network

    int_{network-role}_net_name:
      type: string
      description: Neutron name for the internal int_{network-role} network

Property: fixed_ips, Map Property: ip_address
+++++++++++++++++++++++++++++++++++++++++++++

The resource 'OS::Neutron::Port' property 'fixed_ips'
map property 'ip_address'
is used to assign one IPv4 or IPv6
addresses to port.

One 'OS::Neutron::Port' resource may assign one or more
IPv4 and/or IPv6 addresses.

R-34037 The VNF’s Heat Orchestration Template’s resource ‘OS::Neutron::Port’
property ‘fixed_ips’ map property ‘ip_address’ parameter **MUST**
be declared as either type ‘string’ or type ‘comma_delimited_list’.

R-40971 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an external network, and an IPv4 address is
assigned using the property
‘fixed_ips’ map property ‘ip_address’ and the parameter type is defined
as a string, the parameter name **MUST** follow the naming
convention ‘{vm-type}_{network-role}\_ip\_{index}’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the external network
- the value for {index} must start at zero (0) and increment by one

R-39841 The VNF’s Heat Orchestration Template’s Resource ‘OS::Neutron::Port’
property ‘fixed_ips’ map property ‘ip_address’ parameter
‘{vm-type}_{network-role}\_ip\_{index}’ **MUST NOT** be enumerated in the
VNF’s Heat Orchestration Template’s Environment File.

ONAP's SDN-Controller assigns the IP Address and ONAP provides
the value at orchestration to the Heat Orchestration Template.

*Example External Network IPv4 Address string Parameter Definition*

.. code-block:: python

  parameters:

    {vm-type}_{network-role}_ip_{index}:
      type: string
      description: Fixed IPv4 assignment for {vm-type} VM {index} on the{network-role} network

R-04697 When the VNF’s Heat Orchestration Template’s
Resource ‘OS::Neutron::Port’ is attaching to an external
network, and an IPv4 address is assigned using the property
‘fixed_ips’ map property ‘ip_address’ and the parameter type
is defined as a comma_delimited_list, the parameter name **MUST**
follow the naming convention ‘{vm-type}_{network-role}_ips’,
where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the external network

R-98905 The VNF’s Heat Orchestration Template’s Resource ‘OS::Neutron::Port’
property ‘fixed_ips’ map property ‘ip_address’ parameter
‘{vm-type}_{network-role}_ips’ **MUST NOT** be enumerated in the VNF’s
Heat Orchestration Template’s Environment File.

ONAP's SDN-Controller assigns the IP Address and ONAP provides
the value at orchestration to the Heat Orchestration Template.

*Example External Network IPv4 Address comma_delimited_list
Parameter Definition*

.. code-block:: python

  parameters:

    {vm-type}_{network-role}_ips:
      type: comma_delimited_list
      description: Fixed IPv4 assignments for {vm-type} VMs on the {network-role} network

R-71577 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an external network, and an IPv6 address
is assigned using the property ‘fixed_ips’ map property ‘ip_address’ and
the parameter type is defined as a string, the parameter name **MUST** follow
the naming convention ‘{vm-type}_{network-role}\_v6\_ip\_{index}’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the external network
- the value for {index} must start at zero (0) and increment by one


R-87123 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter ‘{vm-type}_{network-role}\_v6\_ip\_{index}’
**MUST NOT** be enumerated in the VNF’s Heat Orchestration
Template’s Environment File.

ONAP's SDN-Controller assigns the IP Address and ONAP provides
the value at orchestration to the Heat Orchestration Template.

*Example External Network IPv6 Address string Parameter Definition*

.. code-block:: python

  parameters:

    {vm-type}_{network-role}_v6_ip_{index}:
      type: string
      description: Fixed IPv6 assignment for {vm-type} VM {index} on the {network-role} network

R-23503 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an external network, and an IPv6
address is assigned using the property ‘fixed_ips’ map property ‘ip_address’
and the parameter type is defined as a comma_delimited_list, the parameter
name **MUST** follow the naming convention
‘{vm-type}_{network-role}_v6_ips’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the external network

R-93030 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter ‘{vm-type}_{network-role}_v6_ips’ **MUST NOT** be enumerated in the
VNF’s Heat Orchestration Template’s Environment File.

ONAP's SDN-Controller assigns the IP Address and ECOMP provides
the value at orchestration to the Heat Orchestration Template.

*Example External Network IPv6 Address comma_delimited_list Parameter
Definition*

.. code-block:: python

  parameters:

    {vm-type}_{network-role}_v6_ips:
      type: comma_delimited_list
      description: Fixed IPv6 assignments for {vm-type} VMs on the {network-role} network

R-78380 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an internal network, and an IPv4 address
is assigned using the property ‘fixed_ips’ map property ‘ip_address’ and
the parameter type is defined as a string, the parameter name **MUST** follow
the naming convention ‘{vm-type}\_int\_{network-role}\_ip\_{index}’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the internal network
- the value for {index} must start at zero (0) and increment by one

R-28795 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter ‘{vm-type}\_int\_{network-role}\_ip\_{index}’ **MUST** be enumerated
in the VNF’s Heat Orchestration Template’s Environment File.

The IP address is local to the VNF's internal network and is (re)used
in every VNF spin up, thus the constant value is declared in the VNF's
Heat Orchestration Template's Environment File.

*Example Internal Network IPv4 Address string Parameter Definition*

.. code-block:: python

  parameters:

    {vm-type}_int_{network-role}_ip_{index}:
      type: string
      description: Fixed IPv4 assignment for {vm-type} VM {index} on the int_{network-role} network

R-85235 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an internal network, and an IPv4
address is assigned using the property ‘fixed_ips’ map property ‘ip_address’
and the parameter type is defined as a comma_delimited_list, the parameter
name **MUST** follow the naming convention
‘{vm-type}\_int\_{network-role}_ips’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the internal network

R-90206 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter ‘{vm-type}\_int\_{network-role}_int_ips’ **MUST** be enumerated in
the VNF’s Heat Orchestration Template’s Environment File.

The IP address is local to the VNF's internal network and is (re)used
in every VNF spin up, thus the constant value is declared in the VNF's
Heat Orchestration Template's Environment File.

.. code-block:: python

  parameters:

    {vm-type}_int_{network-role}_ips:
      type: comma_delimited_list
      description: Fixed IPv4 assignments for {vm-type} VMs on the int_{network-role} network

R-27818 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an internal network, and an IPv6 address
is assigned using the property ‘fixed_ips’ map property ‘ip_address’ and
the parameter type is defined as a string, the parameter name **MUST** follow
the naming convention ‘{vm-type}\_int\_{network-role}\_v6\_ip\_{index}’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the internal network
- the value for {index} must start at zero (0) and increment by one

R-97201 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter ‘{vm-type}\_int\_{network-role}\_v6\_ip\_{index}’
**MUST** be enumerated in the VNF’s Heat Orchestration
Template’s Environment File.

The IP address is local to the VNF's internal network and is (re)used
in every VNF spin up, thus the constant value is declared in the VNF's
Heat Orchestration Template's Environment File.

*Example Internal Network IPv6 Address string Parameter Definition*

.. code-block:: python

  parameters:

    {vm-type}_int_{network-role}_v6_ip_{index}:
      type: string
      description: Fixed IPv6 assignment for {vm-type} VM {index} on the int_{network-role} network

R-29765 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an internal network, and an IPv6
address is assigned using the property ‘fixed_ips’ map property ‘ip_address’
and the parameter type is defined as a comma_delimited_list, the parameter
name **MUST** follow the naming convention
‘{vm-type}\_int\_{network-role}_v6_ips’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the internal network

*Example Internal Network IPv6 Address comma_delimited_list Parameter
Definition*

.. code-block:: python

  parameters:

    {vm-type}_int_{network-role}_v6_ips:
      type: comma_delimited_list
      description: Fixed IPv6 assignments for {vm-type} VMs on the int_{network-role} network

R-98569 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter ‘{vm-type}\_int\_{network-role}_v6_ips’ **MUST** be enumerated in
the VNF’s Heat Orchestration Template’s Environment File.

The IP address is local to the VNF's internal network and is (re)used
in every VNF spin up, thus the constant value is declared in the VNF's
Heat Orchestration Template's Environment File.

R-62590 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter associated with an external network, i.e.,

- {vm-type}_{network-role}\_ip\_{index}
- {vm-type}_{network-role}\_ip\_v6\_{index}
- {vm-type}_{network-role}_ips
- {vm-type}_{network-role}_v6_ips

**MUST NOT** be enumerated in the Heat Orchestration Template’s
Environment File. ONAP provides the IP address assignments at
orchestration time.

R-93496 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter associated with an internal network, i.e.,

- {vm-type}\_int\_{network-role}\_ip\_{index}
- {vm-type}\_int\_{network-role}\_ip\_v6\_{index}
- {vm-type}\_int\_{network-role}_ips
- {vm-type}\_int\_{network-role}_v6_ips

**MUST** be enumerated in the Heat Orchestration Template’s Environment
File and IP addresses **MUST** be assigned.

Summary Table
_____________

.. csv-table:: **Table # OS::Neutron::Port Property fixed_ips map property ip_address Parameter Naming Convention**
   :header: Resource,Property,Map Property,Network Type,IP Address,Parameter Type,Parameter Name, Environment File
   :align: center
   :widths: auto

   OS::Neutron::Port, fixed_ips, ip_address, external, IPv4, string, {vm-type}\_{network-role}\_ip\_{index}, NO
   OS::Neutron::Port, fixed_ips, ip_address, external, IPv4, comma\_delimited\_list, {vm-type}\_{network-role}\_ips, NO
   OS::Neutron::Port, fixed_ips, ip_address, external, IPv6, string, {vm-type}\_{network-role}\_v6\_ip\_{index}, NO
   OS::Neutron::Port, fixed_ips, ip_address, external, IPv6, comma\_delimited\_list, {vm-type}\_{network-role}\_v6\_ips, NO
   OS::Neutron::Port, fixed_ips, ip_address, internal, IPv4, string, {vm-type}\_int\_{network-role}\_ip\_{index}, YES
   OS::Neutron::Port, fixed_ips, ip_address, internal, IPv4, comma\_delimited\_list, {vm-type}\_int\_{network-role}\_ips, YES
   OS::Neutron::Port, fixed_ips, ip_address, internal, IPv6, string, {vm-type}\_int\_{network-role}\_v6\_ip\_{index}, YES
   OS::Neutron::Port, fixed_ips, ip_address, internal, IPv6, comma\_delimited\_list, {vm-type}\_int\_{network-role}\_v6\_ips, YES


Examples
________

*Example: comma_delimited_list parameters for IPv4 and IPv6 Address
Assignments to an external network*

In this example, the '{network-role}' has been defined as 'oam' to represent
an oam network and the '{vm-type}' has been defined as 'db' for database.

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
    db_0_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips: [ { “ip_address”: {get_param: [ db_oam_ips, 0 ]}}, {
        “ip_address”: {get_param: [ db_oam_v6_ips, 0 ]}}]
    db_1_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips:
          - “ip_address”: {get_param: [ db_oam_ips, 1 ]}
          - “ip_address”: {get_param: [ db_oam_v6_ips, 1 ]}

*Example: string parameters for IPv4 and IPv6 Address Assignments to an
external network*

In this example, the '{network-role}' has been defined as 'oam' to
represent an oam network and the '{vm-type}' has been defined as 'db' for
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
    db_0_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips: [ { “ip_address”: {get_param: db_oam_ip_0}}, { “ip_address”: {get_param: db_oam_v6_ip_0 ]}}]
    db_1_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips:
          - “ip_address”: {get_param: db_oam_ip_1}}]
          - “ip_address”: {get_param: db_oam_v6_ip_1}}]


*Example: comma_delimited_list parameters for IPv4 and IPv6 Address
Assignments to an internal network*

In this example, the '{network-role}' has been defined as 'ctrl' to
represent an ctrl network internal to the vnf.
The '{vm-type}' has been defined as 'db' for
database.

.. code-block:: python

  parameters:
    int_ctrl_net_id:
      type: string
      description: Neutron UUID for the ctrl internal network
    db_int_ctrl_ips:
      type: comma_delimited_list
      description: Fixed IPv4 assignments for db VMs on the ctrl internal
      network
    db_int_ctrl_v6_ips:
      type: comma_delimited_list
      description: Fixed IPv6 assignments for db VMs on the ctrl internal
      network
  resources:
    db_0_int_ctrl_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: int_ctrl_net_id }
        fixed_ips: [ { “ip_address”: {get_param: [ db_int_ctrl_ips, 0 ]}}, {
        “ip_address”: {get_param: [ db_int_ctrl_v6_ips, 0 ]}}]
    db_1_int_ctrl_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: int_ctrl_net_id }
        fixed_ips:
        - “ip_address”: {get_param: [ db_int_ctrl_ips, 1 ]}
        - “ip_address”: {get_param: [ db_int_ctrl_v6_ips, 1 ]}


*Example: string parameters for IPv4 and IPv6 Address Assignments to an
internal network*

In this example, the int\_{network-role} has been defined as
int_ctrl to represent a control network internal to the vnf.
The {vm-type} has been defined as db for database.

.. code-block:: python

  parameters:
    int_ctrl_net_id:
      type: string
      description: Neutron UUID for an OAM internal network
    db_int_ctrl_ip_0:
      type: string
      description: Fixed IPv4 assignment for db VM on the oam_int network
    db_int_ctrl_ip_1:
      type: string
      description: Fixed IPv4 assignment for db VM 1 on the oam_int network
    db_int_ctrl_v6_ip_0:
      type: string
      description: Fixed IPv6 assignment for db VM 0 on the oam_int network
    db_int_ctrl_v6_ip_1:
      type: string
      description: Fixed IPv6 assignment for db VM 1 on the oam_int network
  resources:
    db_0_int_ctrl_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: int_oam_int_net_id }
        fixed_ips: [ { “ip_address”: {get_param: db_oam_int_ip_0}}, {
        “ip_address”: {get_param: db_oam_int_v6_ip_0 ]}}]
    db_1_int_ctrl_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: int_oam_int_net_id }
        fixed_ips:
          - “ip_address”: {get_param: db_oam_int_ip_1}}]
          - “ip_address”: {get_param: db_oam_int_v6_ip_1}}]


Property: fixed\_ips, Map Property: subnet\_id
++++++++++++++++++++++++++++++++++++++++++++++

The resource 'OS::Neutron::Port' property 'fixed_ips' map
property 'subnet'/'subnet_id' is used when a
port is requesting an IP assignment via
OpenStack’s DHCP Service (i.e., Cloud Assigned).

The IP address assignment will be made from the specified subnet.

Specifying the subnet is not required; it is optional.

If the network (external or internal) that the port is attaching
to only contains one subnet, specifying the subnet is
superfluous.  The IP address will be assigned from the one existing
subnet.

If the network (external or internal) that the port is attaching
to contains two or more subnets, specifying the subnet in the
'fixed_ips' map property 'subnet'/'subnet_id' determines which
subnet the IP address will be assigned from.

If the network (external or internal) that the port is attaching
to contains two or more subnets, and the subnet is not is not
specified, OpenStack will randomly(?) determine which subnet
the IP address will be assigned from.

The property fixed_ips is used to assign IPs to a port. The Map Property
subnet_id specifies the subnet the IP is assigned from.

R-38236 The VNF’s Heat Orchestration Template’s resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property
‘subnet’/’subnet_id’ parameter **MUST** be declared type ‘string’.

R-62802 When the VNF’s Heat Orchestration Template’s resource
‘OS::Neutron::Port’ is attaching to an external network, and an IPv4
address is being Cloud Assigned by OpenStack’s DHCP Service and the
external network IPv4 subnet is to be specified using the property
‘fixed_ips’ map property ‘subnet’/’subnet_id’, the parameter **MUST**
follow the naming convention ‘{network-role}_subnet_id’, where
‘{network-role}’ is the network role of the network.

R-83677 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property
subnet’/’subnet_id’ parameter ‘{network-role}_subnet_id’
**MUST NOT** be enumerated in the VNF’s Heat Orchestration Template’s
Environment File.

ONAP's SDN-Controller provides the network's subnet's UUID
value at orchestration to the Heat Orchestration Template.

*Example Parameter Definition*

.. code-block:: python

  parameters:

    {network-role}_subnet_id:
      type: string
      description: Neutron IPv4 subnet UUID for the {network-role} network

R-15287 When the VNF’s Heat Orchestration Template’s resource
‘OS::Neutron::Port’ is attaching to an external network, and an IPv6
address is being Cloud Assigned by OpenStack’s DHCP Service and the
external network IPv6 subnet is to be specified using the property
‘fixed_ips’ map property ‘subnet’/’subnet_id’, the parameter **MUST**
follow the naming convention ‘{network-role}_subnet_v6_id’, where
‘{network-role}’ is the network role of the network.

R-80829 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property
subnet’/’subnet_id’ parameter ‘{network-role}_subnet_v6_id’
**MUST NOT** be enumerated in the VNF’s Heat Orchestration Template’s
Environment File.

ONAP's SDN-Controller provides the network's subnet's UUID
value at orchestration to the Heat Orchestration Template.

*Example Parameter Definition*

.. code-block:: python

  parameters:

    {network-role}_v6_subnet_id:
      type: string
      description: Neutron IPv6 subnet UUID for the {network-role} network


*Example: One Cloud Assigned IPv4 Address (DHCP) assigned to a network
that has two or more IPv4 subnets*

In this example, the '{network-role}' has been defined as 'oam' to represent
an oam network and the '{vm-type}' has been defined as 'lb' for load
balancer. The Cloud Assigned IP Address uses the OpenStack DHCP service
to assign IP addresses.

.. code-block:: python

  parameters:
    oam_net_id:
      type: string
      description: Neutron UUID for the oam network
    oam_subnet_id:
      type: string
      description: Neutron IPv4 subnet UUID for the oam network
  resources:
    lb_0_oam_port_0:
      type: OS::Neutron::Port
        parameters:
          network: { get_param: oam_net_id }
          fixed_ips:
            - subnet_id: { get_param: oam_subnet_id }

*Example: One Cloud Assigned IPv4 address and one Cloud Assigned IPv6
address assigned to a network that has at least one IPv4 subnet and one
IPv6 subnet*

In this example, the '{network-role}' has been defined as 'oam' to represent
an oam network and the '{vm-type}' has been defined as 'lb' for load
balancer.

.. code-block:: python

  parameters:
    oam_net_id:
      type: string
      description: Neutron UUID for the oam network
    oam_subnet_id:
      type: string
      description: Neutron IPv4 subnet UUID for the oam network
    oam_v6_subnet_id:
      type: string
      description: Neutron IPv6 subnet UUID for the oam network
  resources:
    lb_0_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips:
          - subnet_id: { get_param: oam_subnet_id }
          - subnet_id: { get_param: oam_v6_subnet_id }

R-84123 When

- the VNF’s Heat Orchestration Template’s resource ‘OS::Neutron::Port’
  in an Incremental Module is attaching to an internal network
  that is created in the Base Module, AND
- an IPv4 address is being Cloud Assigned by OpenStack’s DHCP Service AND
- the internal network IPv4 subnet is to be specified using the
  property ‘fixed_ips’ map property ‘subnet’/’subnet_id’,

the parameter **MUST** follow the naming convention
‘int\_{network-role}_subnet_id’, where ‘{network-role}’ is the
network role of the internal network

- Note that the parameter **MUST** be defined as an ‘output’ parameter in
  the base module.

R-69634 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property
subnet’/’subnet_id’ parameter ‘int\_{network-role}_subnet_id’
**MUST NOT** be enumerated in the VNF’s Heat Orchestration Template’s
Environment File.

The assumption is that internal networks are created in the base module.
The Neutron subnet network ID will be passed as an output parameter
(e.g., ECOMP Base Module Output Parameter) to the incremental modules.
In the incremental modules, the output parameter name will be defined as
input parameter.

*Example Parameter Definition*

.. code-block:: python

  parameters:

    int_{network-role}_subnet_id:
      type: string
      description: Neutron IPv4 subnet UUID for the int_{network-role} network

R-76160 When

- the VNF’s Heat Orchestration Template’s resource
  ‘OS::Neutron::Port’ in an Incremental Module is attaching to an
  internal network that is created in the Base Module, AND
- an IPv6 address is being Cloud Assigned by OpenStack’s DHCP Service AND
- the internal network IPv6 subnet is to be specified using the property
  ‘fixed_ips’ map property ‘subnet’/’subnet_id’,

the parameter **MUST** follow the naming convention
‘int\_{network-role}_v6_subnet_id’, where ‘{network-role}’
is the network role of the internal network

- Note that the parameter **MUST** be defined as an ‘output’ parameter in
  the base module.

R-22288 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property
‘subnet’/’subnet_id’ parameter ‘int\_{network-role}_v6_subnet_id’
**MUST NOT** be enumerated in the VNF’s Heat Orchestration Template’s
Environment File.

*Example Parameter Definition*

.. code-block:: python

  parameters:

    int_{network-role}_v6_subnet_id:
      type: string
      description: Neutron subnet UUID for the int_{network-role} network


Property: allowed\_address\_pairs, Map Property: ip\_address
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
_________________

R-61282 The VNF Heat Orchestration Template **MUST**
adhere to the following naming convention for the property
allowed\_address\_pairs and Map Property ip\_address parameter,
when the parameter is referencing an “external” network:

-  {vm-type}\_{network-role}\_floating\_ip for an IPv4 address

-  {vm-type}\_{network-role}\_floating\_v6\_ip for an IPv6 address

The parameter must be declared as type: string

The parameter must not be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

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

.. code-block:: yaml

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
_________________

R-16805 The VNF Heat Orchestration Template **MUST** adhere to the
following naming convention for the property allowed\_address\_pairs
and Map Property ip\_address parameter when the parameter is
referencing an “internal” network.

-  {vm-type}\_int\_{network-role}\_floating\_ip for an IPv4 address

-  {vm-type}\_int\_{network-role}\_floating\_v6\_ip for an IPv6 address

The parameter must be declared as type: string

The parameter must be enumerated in the Heat environment file.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:

    {vm-type}_int_{network-role}_floating_ip:
       type: string
       description: VIP for {vm-type} VMs on the int_{network-role} network

    {vm-type}_int_{network-role}_floating_v6_ip:
       type: string
       description: VIP for {vm-type} VMs on the int_{network-role} network

Multiple allowed\_address\_pairs for a {vm-type} / {network-role} combination
______________________________________________________________________________

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

.. code-block:: yaml

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

.. code-block:: yaml

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
__________________________________________________________________

The following items must be taken into consideration when designing Heat
Orchestration Templates that expect ONAP’s SDN-C to assign
allowed\_address\_pair IP addresses via automation.

The VMs must be of the same {vm-type}.

The VMs must be created in the same module (base or incremental).

Resource Property “name”
~~~~~~~~~~~~~~~~~~~~~~~~

The parameter naming convention of the property name for the resource
OS::Nova::Server has been defined in
`Resource:  OS::Nova::Server – Metadata Parameters`_.

This section provides the requirements how the property name for non
OS::Nova::Server resources must be defined when the property is used.
Not all resources require the property name (e.g., it is optional) and
some resources do not support the property.

R-85734 The VNF Heat Orchestration Template **MUST** use the
intrinsic function str\_replace in conjunction with the ONAP
supplied metadata parameter vnf\_name to generate a unique
value, when the property name for a non OS::Nova::Server
resources is defined in a Heat Orchestration Template.

This prevents the enumeration of a
unique value for the property name in a per instance environment file.

Note that

-  In most cases, only the use of the metadata value vnf\_name is
   required to create a unique property name

-  the Heat Orchestration Template pseudo parameter 'OS::stack\_name’
   may also be used in the str\_replace construct to generate a unique
   name when the vnf\_name does not provide uniqueness

*Example: Property* name *for resource* OS::Neutron::SecurityGroup

.. code-block:: yaml

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

.. code-block:: yaml

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
++++++++++++++++++++++++++++++++++++++++++++++++

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP defines three types of Output Parameters as detailed in
`Output Parameters`_.

ONAP Base Module Output Parameters:
+++++++++++++++++++++++++++++++++++

ONAP Base Module Output Parameters do not have an explicit naming
convention. The parameter name must contain {vm-type} and {network-role}
when appropriate.

ONAP Volume Template Output Parameters:
+++++++++++++++++++++++++++++++++++++++

ONAP Base Module Output Parameters do not have an explicit naming
convention. The parameter name must contain {vm-type} when appropriate.

Predefined Output Parameters
++++++++++++++++++++++++++++

ONAP currently defines one predefined output parameter the OAM
Management IP Addresses.

OAM Management IP Addresses
___________________________

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

.. code-block:: yaml

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

.. code-block:: yaml

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP requires the parameter names of certain Contrail Resources to
follow specific naming conventions. This section provides these
requirements.

Contrail Network Parameters
+++++++++++++++++++++++++++

Contrail based resources may require references to a Contrail network
using the network FQDN.

External Networks
_________________

When the parameter associated with the Contrail Network is referencing
an “external” network, the parameter must adhere to the following naming
convention in the Heat Orchestration Template

-  {network-role}\_net\_fqdn

The parameter must be declared as type: string

The parameter must not be enumerated in the Heat environment file.

*Example: Parameter declaration*

.. code-block:: yaml

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

.. code-block:: yaml

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
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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

.. code-block:: yaml

 parameters:
    {vm-type}_{network-role}_route_prefixes:
       type: json
       description: JSON list of Contrail Interface Route Table route prefixes

*Example:*

.. code-block:: yaml

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

.. code-block:: yaml

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

.. code-block:: yaml

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
^^^^^^^^^^^^^^^^^^^^^^^^

ONAP supports the independent deployment of a Cinder volume via separate
Heat Orchestration Templates, the Cinder Volume module. This allows the
volume to persist after VNF deletion so that they can be reused on
another instance (e.g., during a failover activity).

A Base Module or Incremental Module may have a corresponding volume
module. Use of separate volume modules is optional. A Cinder volume may
be embedded within the Base Module or Incremental Module if persistence
is not required.

R-47788 The VNF Heat Orchestration Template **MUST** have a 1:1
scope of a cinder volume module, when it exists, with the
Base Module or Incremental Module

A single volume module must create only the volumes
required by a single Incremental module or Base module.

The following rules apply to independent volume Heat templates:

-  Cinder volumes must be created in a separate Heat Orchestration
   Template from the Base Module or Incremental Module.

-  A single Cinder volume module must include all Cinder volumes
   needed by the Base/Incremental module.

-  R-79531 The VNF Heat Orchestration Template **MUST** define
   “outputs” in the volume template for each Cinder volume
   resource universally unique identifier (UUID) (i.e. ONAP
   Volume Template Output Parameters).

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

.. code-block:: yaml

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

.. code-block:: yaml

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The use of an environment file in OpenStack is optional. In ONAP, it is
mandatory.

R-86285 The VNF Heat Orchestration Template **MUST** have a
corresponding environment file, even if no parameters are required to be
enumerated.

(Note that ONAP, the open source version of ONAP, does not
programmatically enforce the use of an environment file.)

R-67205 The VNF Heat Orchestration Template **MUST** have a corresponding
environment file for a Base Module.

R-35727 The VNF Heat Orchestration Template **MUST** have a
corresponding environment file for an Incremental module.

R-22656 The VNF Heat Orchestration Template **MUST** have a
corresponding environment file for a Cinder Volume Module.

A nested heat template must not have an environment file; OpenStack does
not support it.

The environment file must contain parameter values for the ONAP
Orchestration Constants and VNF Orchestration Constants. These
parameters are identical across all instances of a VNF type, and
expected to change infrequently. The ONAP Orchestration Constants are
associated with OS::Nova::Server image and flavor properties (See
`Property: image`_ and `Property: flavor`_). Examples of VNF
Orchestration Constants are the networking parameters associated
with an internal network (e.g., private IP ranges) and Cinder
volume sizes.

The environment file must not contain parameter values for parameters
that are instance specific (ONAP Orchestration Parameters, VNF
Orchestration Parameters). These parameters are supplied to the Heat by
ONAP at orchestration time.

SDC Treatment of Environment Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When ONAP is instantiating the Heat Orchestration Template, certain
parameter must not be enumerated in the environment file. This document
provides the details of what parameters should not be enumerated.

If the Heat Orchestration Template is to be instantiated from the
OpenStack Command Line Interface (CLI) using the command “heat
stack-create”, all parameters must be enumerated in the environment
file.

Heat Template Constructs
^^^^^^^^^^^^^^^^^^^^^^^^^

Nested Heat Templates
~~~~~~~~~~~~~~~~~~~~~

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

R-89868 The VNF Heat Orchestration Template **MUST** have unique
file names within the scope of the VNF for a nested heat yaml file.

R-52530 The VNF Heat Orchestration Template **MUST NOT** use a
directory hierarchy for nested templates. All templates must
be in a single, flat directory (per VNF).

A nested heat template may be used by any module within a given VNF.

Note that:

-  Constrains must not be defined for any parameter enumerated in a
   nested heat template.

-  R-11041 The VNF Heat Orchestration Template **MUST** have the
   resource calling the nested yaml file pass in as properties
   all parameters defined in nested yaml file.

-  R-61183 The VNF Heat Orchestration Template **MUST NOT**
   change the parameter names, when OS::Nova::Server metadata
   parameters are past into a nested heat template.

-  With nested templates, outputs are required to expose any resource
   properties of the child templates to the parent template. Those would
   not explicitly be declared as parameters but simply referenced as
   get\_attribute targets against the “parent” resource.

Nested Heat Template Example: Static
++++++++++++++++++++++++++++++++++++++

incremental.yaml

.. code-block:: yaml

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

.. code-block:: yaml

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
+++++++++++++++++++++++++

The OS::Heat::ResourceGroup is a useful Heat element for creating
multiple instances of a given resource or collection of resources.
Typically, it is used with a nested Heat template, to create, for
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

.. code-block:: yaml

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

.. code-block:: yaml

 type: OS::Heat::ResourceGroup
   resource_def:
     type: my_nested_vm_template.yaml
     properties:
       names: {get_param: vm_name_list}
       index: %index%

You can then reference within the nested template as:

{ get\_param: [names, {get\_param: index} ] }

ResourceGroup Property count
____________________________

ONAP requires that the OS::Heat::ResourceGroup property count be defined
(even if the value is one) and that the value must be enumerated in the
environment file. This is required for ONAP to build the TOSCA model for
the VNF.

.. code-block:: yaml

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
____________________________________

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

.. code-block:: yaml

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

.. code-block:: yaml

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
~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Heat Templates may contain the inclusion of text files into Heat
templates via the Heat get\_file directive. This may be used, for
example, to define a common “user-data” script, or to inject files into
a VM on startup via the “personality” property.

Support for Heat Files is subject to the following limitations:

R-76718 The VNF Heat Orchestration Template **MUST** reference
the get\_files targets in Heat templates by file name, and the
corresponding files should be delivered to ONAP along with the
Heat templates.

R-41888 The VNE Heat **MUST NOT** use URL-based file retrieval.

R-62177 The VNF Heat Orchestration Template **MUST** have unique
file names for the included files within the scope of the VNF.

R-87848 The VNF Heat Orchestration Template **MUST** have all
included files in a single, flat directory per VNF. ONAP does
not support a directory hierarchy.

-  Included files may be used by all Modules within a given VNF.

-  get\_file directives may be used in both non-nested and nested
   templates

Key Pairs
~~~~~~~~~

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

-  Create a new keypair within The VNF Heat Orchestration Template (in the base
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

.. code-block:: yaml

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
~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Anti-affinity or affinity rules are supported using normal OpenStack
OS::Nova::ServerGroup resources. Separate ServerGroups are typically
created for each VM type to prevent them from residing on the same host,
but they can be applied to multiple VM types to extend the
affinity/anti-affinity across related VM types as well.

*Example:*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} have been defined as lb for load
balancer and db for database.

.. code-block:: yaml

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

.. code-block:: yaml

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
^^^^^^^^^^^^^^^^^

VNF/VM parameters may include availability zone IDs for VNFs that
require high availability.

The Heat must comply with the following requirements to specific
availability zone IDs:

-  The Heat template should spread Nova and Cinder resources across the
   availability zones as desired

Post Orchestration & VNF Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Heat templates should contain a minimum amount of post-orchestration
configuration data. For instance, *do not* embed complex user-data
scripts in the template with large numbers of configuration parameters
to the Heat template.

-  VNFs may provide configuration APIs for use after VNF creation. Such
   APIs will be invoked via application and/or SDN controllers.

*Note:* It is important to follow this convention to the extent possible
even in the short-term as of the long-term direction.
