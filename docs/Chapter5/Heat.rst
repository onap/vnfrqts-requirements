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


.. req::
    :id: R-95303
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template **MUST** be defined using valid YAML.

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

.. code-block:: yaml

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


.. req::
    :id: R-27078
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration template **MUST** contain
    the section "heat_template_version:".

The section "heat_template_version:" must be set to a date
that is supported by the OpenStack environment.

description
+++++++++++


.. req::
    :id: R-39402
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template **MUST**
    contain the section "description:".

parameter_groups
++++++++++++++++

A VNF Heat Orchestration template may
contain the section "parameter_groups:".

parameters
++++++++++


.. req::
    :id: R-35414
    :target: VNF
    :keyword: MUST

    A VNF Heat Orchestration's template **MUST**
    contain the section "parameters:".


.. code-block:: yaml

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


.. req::
    :id: R-90279
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration template's parameter **MUST**
    be used in a resource with the exception of the parameters
    for the OS::Nova::Server resource property availability_zone.

.. req::
    :id: R-91273
    :target: VNF
    :keyword: MAY NOT

    A VNF Heat Orchestration's template's parameter for
    the OS::Nova::Server resource property availability_zone
    **MAY NOT** be used in any OS::Nova::Resource.

That is, the parameter associated with the property 'availability_zone'
maybe declared but not used in a resource.

<param name>
____________

The name of the parameter.


.. req::
    :id: R-25877
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's parameter
    name (i.e., <param name>) **MUST** contain only
    alphanumeric characters and underscores ('_').

type
____


.. req::
    :id: R-36772
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's parameter
    **MUST** include the attribute "type:".

.. req::
    :id: R-11441
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's parameter
    type **MUST** be one of the following values: "string",
    "number", "json", "comma_delimited_list" or "boolean".

label
_____


.. req::
    :id: R-32094
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template parameter
    declaration **MAY** contain the attribute "label:".

description
___________


.. req::
    :id: R-44001
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template parameter
    declaration **MUST** contain the attribute "description".

Note that the parameter attribute "description:" is an OpenStack
optional attribute that provides a description of the parameter.
ONAP implementation requires this attribute.

default
_______


.. req::
    :id: R-90526
    :target: VNF
    :keyword: MUST

    A VNF Heat Orchestration Template parameter
    declaration **MUST** not contain the default attribute.

.. req::
    :id: R-26124
    :target: VNF
    :keyword: MUST

    If a VNF Heat Orchestration Template parameter
    requires a default value, it **MUST** be enumerated in the environment file.

Note that the parameter attribute "default:" is an OpenStack
optional attribute that declares the default value of the
parameter. ONAP implementation prohibits the use of this attribute.

hidden
______


.. req::
    :id: R-32557
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template parameter
    declaration **MAY** contain the attribute "hidden:".

The parameter attribute "hidden:" is an OpenStack optional
attribute that defines whether the parameters should be
hidden when a user requests information about a stack
created from the template. This attribute can be used
to hide passwords specified as parameters.

constraints
___________

The parameter attribute "constraints:" is an OpenStack optional
attribute that defines a list of constraints to apply to the parameter.


.. req::
    :id: R-88863
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's parameter defined as
    type "number" **MUST** have a parameter constraint of "range" or
    "allowed_values" defined.

.. req::
    :id: R-40518
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's parameter defined as
    type "string" **MAY** have a parameter constraint defined.

.. req::
    :id: R-96227
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's parameter defined as
    type "json" **MAY** have a parameter constraint defined.

.. req::
    :id: R-79817
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's parameter defined as
    type "comma_delimited_list" **MAY** have a parameter constraint defined.

.. req::
    :id: R-06613
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's parameter defined as
    type "boolean" **MAY** have a parameter constraint defined.

.. req::
    :id: R-00011
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's Nested YAML files
    parameter's **MUST NOT** have a parameter constraint defined.

The constraints block of a parameter definition defines additional
validation constraints that apply to the value of the parameter.
The parameter values provided in the VNF Heat Orchestration Template
are validated against the constraints at instantiation time.
The stack creation fails if the parameter value doesn't comply to
the constraints.

The constraints are defined as a list with the following syntax

.. code-block:: yaml

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

.. code-block:: yaml

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

.. code-block:: yaml

    allowed_values: [ <value>, <value>, ... ]

    Alternatively, the following YAML list notation can be used

    allowed_values:

    - <value>

    - <value>

    - ...

. .

immutable
_________


.. req::
    :id: R-22589
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template parameter declaration
    **MAY** contain the attribute "immutable:".

The parameter attribute \"immutable:\" is an OpenStack optional
attribute that defines whether the parameter is updatable. A Heat
Orchestration Template stack update fails if immutable is set to
true and the parameter value is changed.  This attribute
\"immutable:\" defaults to false.

resources
+++++++++


.. req::
    :id: R-23664
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration template **MUST** contain
    the section "resources:".

.. req::
    :id: R-90152
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's "resources:"
    section **MUST** contain the declaration of at least one resource.

.. req::
    :id: R-40551
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's Nested YAML files
    **MAY** contain the section "resources:".

Each resource is defined as a
separate block in the resources section with the following syntax.

.. code-block:: yaml

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


.. req::
    :id: R-75141
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's resource name
    (i.e., <resource ID>) **MUST** only contain alphanumeric
    characters and underscores ('_').

.. req::
    :id: R-16447
    :target: VNF
    :keyword: MUST

    A VNF's <resource ID> **MUST** be unique across all
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


.. req::
    :id: R-53952
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's Resource
    **MUST NOT** reference a HTTP-based resource definitions.

.. req::
    :id: R-71699
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's Resource
    **MUST NOT** reference a HTTP-based Nested YAML file.

properties
__________

The resource attribute \"properties:\" is an OpenStack optional
attribute that provides a list of resource-specific properties.
The property value can be provided in place, or via a function
(e.g., `Intrinsic functions <https://docs.openstack.org/developer/heat/template_guide/hot_spec.html#hot-spec-intrinsic-functions>`__).


.. req::
    :id: R-10834
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF Heat Orchestration Template resource attribute
    "property:" uses a nested "get_param", one level of nesting is
    supported and the nested "get_param" **MUST** reference an index.

metadata
________

The resource attribute \"metadata:\" is an OpenStack optional attribute.


.. req::
    :id: R-97199
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    resource **MUST** contain the attribute "metadata".

Section 5.4 contains the OS::Nova::Server mandatory and optional metadata.

depends_on
__________

The resource attribute \"depends_on:\" is an OpenStack optional
attribute.
See `OpenStack documentation <https://docs.openstack.org/developer/heat/template_guide/hot_spec.html#hot-spec-resources-dependencies>`__
for additional details.


.. req::
    :id: R-46968
    :target: VNF
    :keyword: MAY

    VNF's Heat Orchestration Template's Resource **MAY**
    declare the attribute "depends_on:".

update_policy
_____________


.. req::
    :id: R-63137
    :target: VNF
    :keyword: MAY

    VNF's Heat Orchestration Template's Resource **MAY**
    declare the attribute "update_policy:".

deletion_policy
_______________


.. req::
    :id: R-43740
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's Resource
    **MAY** declare the attribute "deletion_policy:".

If specified, the \"deletion_policy:\" attribute for resources
allows values 'Delete', 'Retain', and 'Snapshot'.
Starting with heat_template_version 2016-10-14, lowercase
equivalents are also allowed.

The default policy is to delete the physical resource when
deleting a resource from the stack.

external_id
___________


.. req::
    :id: R-78569
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's Resouce **MAY**
    declare the attribute "external_id:".

This attribute allows for specifying the resource_id for an
existing external (to the stack) resource. External resources
cannot depend on other resources, but we allow other resources to
depend on external resource. This attribute is optional.
Note: when this is specified, properties will not be used for
building the resource and the resource is not managed by Heat.
This is not possible to update that attribute. Also,
resource won't be deleted by heat when stack is deleted.


condition
_________

The resource attribute \"condition:\" is an OpenStack optional attribute.

Support for the resource condition attribute was added
in the Newton release of OpenStack.

outputs
+++++++


.. req::
    :id: R-36982
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration template **MAY**
    contain the "outputs:" section.

This section allows for specifying output parameters
available to users once the template has been instantiated. If the
section is specified, it will need to adhere to specific requirements.
See `Output Parameters`_ and
`ONAP Output Parameter Names`_ for additional details.

Environment File Format
~~~~~~~~~~~~~~~~~~~~~~~

The environment file is a yaml text file.
(https://docs.openstack.org/developer/heat/template_guide/environment.html)


.. req::
    :id: R-86285
    :target: VNF
    :keyword: MUST

    The VNF Heat Orchestration Template **MUST** have a corresponding
    environment file, even if no parameters are required to be enumerated.

The use of an environment file in OpenStack is optional.
In ONAP, it is mandatory.


.. req::
    :id: R-03324
    :target: VNF
    :keyword: MUST

    The VNF Heat Orchestration Template **MUST** contain the
    "parameters" section in the environment file.

.. req::
    :id: R-68198
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration template's Environment File's
    "parameters:" section **MAY** enumerate parameters.

ONAP implementation requires the parameters section in the
environmental file to be declared. The parameters section
contains a list of key/value pairs.


.. req::
    :id: R-59930
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration template's Environment
    File's **MAY** contain the "parameter_defaults:" section.

The "parameter_defaults:" section contains default parameters
that are passed to all template resources.


.. req::
    :id: R-46096
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration template's Environment File's
    **MAY** contain the "encrypted_parameters:" section.

The "encrypted_parameters:" section contains a list of encrypted parameters.


.. req::
    :id: R-24893
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration template's Environment File's
    **MAY** contain the "event_sinks:" section.

The "event_sinks:" section contains the list of endpoints that would
receive stack events.


.. req::
    :id: R-42685
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration template's Environment File's
    **MAY** contain the "parameter_merge_strategies:" section.

The "parameter_merge_strategies:" section provides the merge strategies
for merging parameters and parameter defaults from the environment file.


.. req::
    :id: R-67231
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration template's Environment File's **MUST NOT**
    contain the "resource_registry:" section.

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
environment file. See `Output Parameters`_ and
`ONAP Resource ID and Parameter Naming Convention`_ for more details.

ONAP Heat Orchestration Templates: Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP supports a modular Heat Orchestration Template design pattern,
referred to as *VNF Modularity.*

ONAP VNF Modularity Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. req::
    :id: R-69663
    :target: VNF
    :keyword: MAY

    A VNF **MAY** be composed from one or more Heat Orchestration
    Templates, each of which represents a subset of the overall VNF.

The Heat Orchestration Templates can be thought of a components or
modules of the VNF and are referred to as "\ *VNF Modules*\ ".
During orchestration, these modules are
deployed incrementally to create the complete VNF.


.. req::
    :id: R-33132
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template **MAY** be

       * a Base Module Heat Orchestration Template
         (also referred to as a Base Module)

       * an Incremental Module Heat Orchestration Template
         (referred to as an Incremental Module)

       * a Cinder Volume Module Heat Orchestration Template
         (referred to as Cinder Volume Module).

.. req::
    :id: R-37028
    :target: VNF
    :keyword: MUST

    The VNF **MUST** be composed of one "base" module.

.. req::
    :id: R-13196
    :target: VNF
    :keyword: MAY

    A VNF **MAY** be composed of zero to many Incremental Modules.

.. req::
    :id: R-20974
    :target: VNF
    :keyword: MUST

    The VNF **MUST** deploy the base module first, prior to
    the incremental modules.

.. req::
    :id: R-28980
    :target: VNF
    :keyword: MAY

    A VNF's incremental module **MAY** be used for initial VNF
    deployment only.

.. req::
    :id: R-86926
    :target: VNF
    :keyword: MAY

    A VNF's incremental module **MAY** be used for scale out only.

A VNF's Incremental Module that is used for scale out is deployed
sometime after initial VNF deployment to add capacity.


.. req::
    :id: R-91497
    :target: VNF
    :keyword: MAY

    A VNF's incremental module **MAY** be used for both deployment
    and scale out.

.. req::
    :id: R-68122
    :target: VNF
    :keyword: MAY

    A VNF's incremental module **MAY** be deployed more than once,
    either during initial VNF deployment and/or scale out.

.. req::
    :id: R-46119
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's Resource OS::Heat::CinderVolume
    **MAY** be defined in a Base Module.

.. req::
    :id: R-90748
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's Resource OS::Heat::CinderVolume
    **MAY** be defined in an Incremental Module.

.. req::
    :id: R-03251
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's Resource OS::Heat::CinderVolume
    **MAY** be defined in a Cinder Volume Module.

ONAP also supports the concept of an optional, independently deployed Cinder
volume via a separate Heat Orchestration Templates, referred to as a Cinder
Volume Module. This allows the volume to persist after a Virtual Machine
(VM) (i.e., OS::Nova::Server) is deleted, allowing the volume to be reused
on another instance (e.g., during a failover activity).

.. req::
    :id: R-11200
    :target: VNF
    :keyword: MUST

    The VNF **MUST** keep the scope of a Cinder volume module,
    when it exists, to be 1:1 with the VNF Base Module or Incremental Module.

It is strongly recommended that Cinder Volumes be created in a Cinder Volume
Module.

.. req::
    :id: R-38474
    :target: VNF
    :keyword: MUST

    The VNF **MUST** have a corresponding environment file for a Base Module.

.. req::
    :id: R-81725
    :target: VNF
    :keyword: MUST

    The VNF **MUST** have a corresponding environment file for an Incremental Module.

.. req::
    :id: R-53433
    :target: VNF
    :keyword: MUST

    The VNF **MUST** have a corresponding environment file for a Cinder Volume Module.

These concepts will be described in more detail throughout the document.
This overview is provided to set the stage and help clarify the concepts
that will be introduced.

Nested Heat Orchestration Templates Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP supports nested Heat Orchestration Templates per OpenStack
specifications.


.. req::
    :id: R-36582
    :target: VNF
    :keyword: MAY

    A VNF's Base Module **MAY** utilize nested heat.

.. req::
    :id: R-56721
    :target: VNF
    :keyword: MAY

    A VNF's Incremental Module **MAY** utilize nested heat.

.. req::
    :id: R-30395
    :target: VNF
    :keyword: MAY

    A VNF's Cinder Volume Module **MAY** utilize nested heat.

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
"base".


.. req::
    :id: R-87485
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's file extension **MUST**
    be in the lower case format '.yaml' or '.yml'.

.. req::
    :id: R-56438
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's Nested YAML file extension
    **MUST** be in the lower case format '.yaml' or '.yml'.

.. req::
    :id: R-74304
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's Environment file extension
    **MUST** be in the lower case format '.env'.

.. req::
    :id: R-99646
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's YAML files (i.e, Heat Orchestration Template files and
    Nested files) **MUST** have a unique name in the scope of the VNF.

Base Modules
++++++++++++


.. req::
    :id: R-81339
    :target: VNF
    :keyword: MUST

    A VNF Heat Orchestration Template's Base Module file name **MUST**
    include 'base' in the filename and **MUST** match one of the following four
    formats:

       * 'base_<text>.y[a]ml'
       * '<text>_base.y[a]ml'
       * 'base.y[a]ml'
       * '<text>_base_<text>'.y[a]ml

    where 'base' is case insensitive and where '<text>'
    **MUST** contain only alphanumeric characters
    and underscores '_' and **MUST NOT** contain the case
    insensitive word 'base'.

.. req::
    :id: R-91342
    :target: VNF
    :keyword: MUST

    A VNF Heat Orchestration Template's Base Module's Environment File
    **MUST** be named identical to the VNF Heat Orchestration Template's Base
    Module with '.y[a]ml' replaced with '.env'.

Incremental Modules
+++++++++++++++++++


.. req::
    :id: R-87247
    :target: VNF
    :keyword: MUST

    A VNF Heat Orchestration Template's Incremental Module file name
    **MUST** contain only alphanumeric characters and underscores '_' and
    **MUST NOT** contain the case insensitive word 'base'.

.. req::
    :id: R-94509
    :target: VNF
    :keyword: MUST

    A VNF Heat Orchestration Template's Incremental Module's Environment
    File **MUST** be named identical to the VNF Heat Orchestration Template's
    Incremental Module with '.y[a]ml' replaced with '.env'.

To clearly identify the incremental module, it is recommended to use the
following naming options for modules:

 -  module_<text>.y[a]ml

 -  <text>_module.y[a]ml

 -  module.y[a]ml

 -  <text>_module_<text>.y[a]ml

Cinder Volume Modules
+++++++++++++++++++++


.. req::
    :id: R-82732
    :target: VNF
    :keyword: MUST

    A VNF Heat Orchestration Template's Cinder Volume Module **MUST** be
    named identical to the base or incremental module it is supporting with
    '_volume appended'

.. req::
    :id: R-31141
    :target: VNF
    :keyword: MUST

    A VNF Heat Orchestration Template's Cinder Volume Module's Environment
    File **MUST** be named identical to the VNF Heat Orchestration Template's
    Cinder Volume Module with .y[a]ml replaced with '.env'.

Nested Heat file
++++++++++++++++


.. req::
    :id: R-76057
    :target: VNF
    :keyword: MUST

    A VNF Heat Orchestration Template's Nested YAML file name **MUST**
    contain only alphanumeric characters and underscores '_' and **MUST NOT**
    contain the case insensitive word 'base'.

.. req::
    :id: R-70276
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF HEAT's Orchestration Nested Template's YAML file
    name **MUST NOT** be in the format '{vm-type}.y[a]ml' where
    '{vm-type}' is defined in the Heat Orchestration Template.

Examples include

 -  <text>.y[a]ml

 -  nest_<text>.y[a]ml

 -  <text>_nest.y[a]ml

 -  nest.y[a]ml

 -  <text>_nest_<text>.y[a]ml

VNF Heat Orchestration Template's Nested YAML file does not have a
corresponding environment files, per OpenStack specifications.

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


.. req::
    :id: R-52753
    :target: VNF
    :keyword: MUST

    VNF's Heat Orchestration Template's Base Module's output parameter's
    name and type **MUST** match the VNF's Heat Orchestration Template's
    incremental Module's name and type unless the output parameter is of type
    'comma_delimited_list', then the corresponding input parameter **MUST**
    be declared as type 'json'.

If the Output parameter has a comma_delimited_list value (e.g., a collection
of UUIDs from a Resource Group), then the corresponding input parameter
must be declared as type json and not a comma_delimited_list, which is
actually a string value with embedded commas.


.. req::
    :id: R-22608
    :target: VNF
    :keyword: MUST NOT

    When a VNF's Heat Orchestration Template's Base Module's output
    parameter is declared as an input parameter in an Incremental Module,
    the parameter attribute 'constraints:' **MUST NOT** be declared.

Additional details on ONAP Base Module Output Parameters are provided in
`ONAP Output Parameter Names`_ and ONAP VNF Modularity.

ONAP Volume Module Output Parameters
++++++++++++++++++++++++++++++++++++


.. req::
    :id: R-89913
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's Cinder Volume Module Output
    Parameter(s) **MUST** include the UUID(s) of the Cinder Volumes created in
    template, while other Output Parameters **MAY** be included.

A VNF's Heat Orchestration Template's Cinder Volume Module Output Parameter(s)
are only available for the module (base or incremental) that the volume
template is associated with.


.. req::
    :id: R-07443
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Templates' Cinder Volume Module Output
    Parameter's name and type **MUST** match the input parameter name and type
    in the corresponding Base Module or Incremental Module unless the Output
    Parameter is of the type 'comma\_delimited\_list', then the corresponding input
    parameter **MUST** be declared as type 'json'.

If the Output parameter has a comma_delimited_list value (e.g., a collection
of UUIDs from a Resource Group), then the corresponding input parameter must
be declared as type json and not a comma\_delimited\_list, which is actually a
string value with embedded commas.


.. req::
    :id: R-20547
    :target: VNF
    :keyword: MUST NOT

    When an ONAP Volume Module Output Parameter is declared as an input
    parameter in a base or an incremental module Heat Orchestration Template,
    parameter constraints **MUST NOT** be declared.

Additional details on ONAP Base Module Output Parameters are provided in
`ONAP Output Parameter Names`_ and `Cinder Volumes`_.

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


.. req::
    :id: R-39349
    :target: VNF
    :keyword: MUST NOT

    A VNF Heat Orchestration Template **MUST NOT** be designed to
    utilize the OpenStack 'heat stack-update' command for scaling
    (growth/de-growth).

.. req::
    :id: R-43413
    :target: VNF
    :keyword: MUST

    A VNF **MUST** utilize a modular Heat Orchestration Template
    design to support scaling (growth/de-growth).

Scope of a Heat Orchestration Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. req::
    :id: R-59482
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template **MUST NOT** be VNF instance
    specific or Cloud site specific.

ONAP provides the instance specific parameter values to the Heat
Orchestration Template at orchestration time.


.. req::
    :id: R-01896
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's parameter values that are
    constant across all deployments **MUST** be declared in a Heat Orchestration
    Template Environment File.

Networking
^^^^^^^^^^

ONAP defines two types of networks: External Networks and Internal Networks.

External Networks
~~~~~~~~~~~~~~~~~

ONAP defines an external network in relation to the VNF and not with regard
to the Network Cloud site. External networks may also be referred to as
"inter-VNF" networks.  An external network must connect VMs in a VNF to
VMs in another VNF or an external gateway or external router.

An External Network may be a Neutron Network or a Contrail Network.


.. req::
    :id: R-16968
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Templates **MUST NOT** include heat
    resources to create external networks.

External networks must be orchestrated separately, independent of the VNF.
This allows the network to be shared by multiple VNFs and managed
independently of VNFs.


.. req::
    :id: R-00606
    :target: VNF
    :keyword: MAY

    A VNF **MAY** be connected to zero, one or more than one external
    networks.

.. req::
    :id: R-57424
    :target: VNF
    :keyword: MUST

    A VNF's port connected to an external network **MUST**
    use the port for the purpose of reaching VMs in another VNF
    and/or an external gateway and/or external router. A VNF's port
    connected to an external network **MAY** use the port for
    the purpose of reaching VMs in the same VNF.

.. req::
    :id: R-29865
    :target: VNF
    :keyword: MUST

    When a VNF connects to an external network, a network role,
    referred to as the '{network-role}' **MUST** be assigned to the
    external network for use in the VNF's Heat Orchestration Template.

.. req::
    :id: R-69014
    :target: VNF
    :keyword: MUST

    When a VNF connects to an external network, a network role, referred
    to as the '{network-role}' **MUST** be assigned to the external network
    for use in the VNF's Heat Orchestration Template.

.. req::
    :id: R-05201
    :target: VNF
    :keyword: MUST

    When a VNF connects to two or more external networks, each external
    network **MUST** be assigned a unique '{network-role}' in the context of
    the VNF for use in the VNF's Heat Orchestration Template.

.. req::
    :id: R-83015
    :target: VNF
    :keyword: MUST

    A VNF's '{network-role}' assigned to an external network **MUST**
    be different than the '{network-role}' assigned to the VNF's internal
    networks, if internal networks exist.

.. req::
    :id: R-99794
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    An external network **MUST** have one subnet. An external network
    **MAY** have more than one subnet.

Note that this document refers to **'{network-role}'** which in reality
is the **'{network-role-tag}'**.  The value of the
'{network-role}' / '{network-role-tag}'
is determined by the designer of the VNF's Heat Orchestration Template and
there is no requirement for '{network-role}' / '{network-role-tag}'
uniqueness across Heat Orchestration Templates for
different VNFs.

When an external network is created by ONAP, the network is assigned a
'{network-role}'.  The '{network-role}' of the network is not required to
match the '{network-role}' of the VNF Heat Orchestration Template.

For example, the VNF Heat Orchestration Template can assign a '{network-role}'
of 'oam' to a network which attaches to an external network with a
'{network-role}' of 'oam_protected_1' .

When the Heat Orchestration Template is on-boarded into ONAP
  * each '{network-role}' value in the Heat Orchestration Template
    is mapped to the '{network-role-tag}' in the ONAP
    data structure.
  * each OS::Neutron::Port is associated with the external network it is
    connecting to, thus creating the VNF Heat Orchestration Template
    '{network-role}' / '{network-role-tag}' to external network '{network-role}'
    mapping.

ONAP enforces a naming convention for parameters associated with
external networks. `ONAP Resource ID and Parameter Naming Convention`_
provides additional details.

Internal Networks
~~~~~~~~~~~~~~~~~

ONAP defines an internal network in relation to the VNF and not with
regard to the Network Cloud site. Internal networks may also be referred
to as "intra-VNF" networks or "private" networks. An internal network
only connects VMs in a single VNF; it must not connect to other VNFs
or an external gateway or router


.. req::
    :id: R-87096
    :target: VNF
    :keyword: MAY

    A VNF **MAY** contain zero, one or more than one internal networks.

.. req::
    :id: R-35666
    :target: VNF
    :keyword: MUST

    If a VNF has an internal network, the VNF Heat Orchestration
    Template **MUST** include the heat resources to create the internal network.

.. req::
    :id: R-86972
    :target: VNF
    :keyword: SHOULD

    A VNF **SHOULD** create the internal network in the VNF's Heat
    Orchestration Template Base Module.

An Internal Network may be created using Neutron Heat Resources and/or
Contrail Heat Resources.


.. req::
    :id: R-52425
    :target: VNF
    :keyword: MUST

    A VNF's port connected to an internal network **MUST** connect
    the port to VMs in the same VNF.

.. req::
    :id: R-46461
    :target: VNF
    :keyword: MUST NOT

    A VNF's port connected to an internal network **MUST NOT** connect
    the port to VMs in another VNF and/or an external gateway and/or
    external router.

.. req::
    :id: R-68936
    :target: VNF
    :keyword: MUST

    When a VNF creates an internal network, a network role, referred to
    as the '{network-role}' **MUST** be assigned to the internal network for
    use in the VNF's Heat Orchestration Template.

.. req::
    :id: R-32025
    :target: VNF
    :keyword: MUST

    When a VNF creates two or more internal networks, each internal
    network **MUST** be assigned a unique '{network-role}' in the context of
    the VNF for use in the VNF's Heat Orchestration Template.

.. req::
    :id: R-69874
    :target: VNF
    :keyword: MUST

    A VNF's '{network-role}' assigned to an internal network **MUST**
    be different than the '{network-role}' assigned to the VNF's external
    networks.

.. req::
    :id: R-16241
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's internal network **MUST** have one subnet.
    A VNF's internal network **MAY** have more than one subnet.

.. req::
    :id: R-34726
    :target: VNF
    :keyword: MUST

    If a VNF's port is connected to an internal network and the port
    is created in the same Heat Orchestration Template as the internal network,
    then the port resource **MUST** use a 'get_resource' to obtain
    the network UUID.

.. req::
    :id: R-22688
    :target: VNF
    :keyword: MUST

    If a VNF's port is connected to an internal network and the
    port is created in an Incremental Module and the internal network is created
    in the Base Module then the UUID of the internal network **MUST** be exposed
    as a parameter in the 'outputs:' section of the Base Module and the port
    resource **MUST** use a 'get_param' to obtain the network UUID.
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


.. req::
    :id: R-01455
    :target: VNF
    :keyword: MUST

    When a VNF's Heat Orchestration Template creates a
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

.. req::
    :id: R-82481
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's Resource property
    parameter that is associated with a unique Virtual Machine
    type **MUST** include '{vm-type}'  as part of the parameter
    name with two exceptions:

      1.) The Resource OS::Nova::Server property availability_zone parameter
      **MUST NOT** be prefixed with a common '{vm-type} identifier,

      2.) The Resource OS::Nova::Server eight mandatory and optional metadata
      parameters (vnf_name, vnf_id, vf_module_id, vf_module_name, vm_role,
      vf_module_index, environment_context, workload_context) **MUST NOT**
      be prefixed with a common '{vm-type}' identifier.

.. req::
    :id: R-66729
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's Resource that is
    associated with a unique Virtual Machine type **MUST** include
    '{vm-type}' as part of the resource ID.

.. req::
    :id: R-98407
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's '{vm-type}' **MUST** contain
    only alphanumeric characters and/or underscores '_' and
    **MUST NOT** contain any of the following strings: '_int' or 'int\_'
    or '\_int\_'.

.. req::
    :id: R-48067
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's {vm-type} **MUST NOT** be a
    substring of {network-role}.

It may cause the VNF Validation Program validation-scripts project
to produce erroneous error messages.


.. req::
    :id: R-32394
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's use of '{vm-type}'
    in all Resource property parameter names **MUST** be the same case.

.. req::
    :id: R-46839
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's use of
    '{vm-type}' in all Resource IDs **MUST** be the same case.

.. req::
    :id: R-36687
    :target: VNF
    :keyword: SHOULD

    A VNF's Heat Orchestration Template's '{vm-type}' case in
    Resource property parameter names **SHOULD** match the case of
    '{vm-type}' in Resource IDs and vice versa.

{network-role}
~~~~~~~~~~~~~~

The assignment of a {network-role} is discussed in `Networking`_.


.. req::
    :id: R-21330
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's Resource property
    parameter that is associated with external network **MUST**
    include the '{network-role}' as part of the parameter name.

.. req::
    :id: R-11168
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's Resource ID that is
    associated with an external network **MUST** include the
    '{network-role}' as part of the resource ID.

.. req::
    :id: R-84322
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's Resource property
    parameter that is associated with an internal network
    **MUST** include 'int\_{network-role}' as part of the parameter
    name, where 'int\_' is a hard coded string.

.. req::
    :id: R-96983
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's Resource ID that is
    associated with an internal network **MUST** include
    'int\_{network-role}' as part of the Resource ID, where
    'int\_' is a hard coded string.

.. req::
    :id: R-26506
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's '{network-role}'
    **MUST** contain only alphanumeric characters and/or
    underscores '_' and **MUST NOT** contain any of the following
    strings: '_int' or 'int\_' or '\_int\_'.

.. req::
    :id: R-00977
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's '{network-role}'
    **MUST NOT** be a substring of '{vm-type}'.

For example, if a VNF has a '{vm-type}' of 'oam' and a
'{network-role}' of 'oam\_protected' would be a violation of the requirement.


.. req::
    :id: R-58424
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's use of '{network-role}'
    in all Resource property parameter names **MUST** be the same case.

.. req::
    :id: R-21511
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's use of '{network-role}'
    in all Resource IDs **MUST** be the same case.

.. req::
    :id: R-86588
    :target: VNF
    :keyword: SHOULD

    A VNF's Heat Orchestration Template's '{network-role}' case
    in Resource property parameter names **SHOULD** match the case
    of '{network-role}' in Resource IDs and vice versa.

Resource IDs
~~~~~~~~~~~~

Requirement R-75141 states a VNF's Heat Orchestration Template's
resource name (i.e., <resource ID>) MUST only contain alphanumeric
characters and underscores ('_').*

Requirement R-16447 states a VNF's <resource ID> MUST be unique
across all Heat Orchestration Templates and all HEAT Orchestration
Template Nested YAML files that are used to create the VNF.

As stated previously, OpenStack requires the <resource ID> to be unique
to the Heat Orchestration Template and not unique across all Heat
Orchestration Templates the compose the VNF.

Heat Orchestration Template resources are described in `resources`_


.. req::
    :id: R-54517
    :target: VNF
    :keyword: MUST

    When a VNF's Heat Orchestration Template's resource is associated
    with a single '{vm-type}', the Resource ID **MUST** contain the '{vm-type}'.

.. req::
    :id: R-96482
    :target: VNF
    :keyword: MUST

    When a VNF's Heat Orchestration Template's resource is associated
    with a single external network, the Resource ID **MUST** contain the text
    '{network-role}'.

.. req::
    :id: R-98138
    :target: VNF
    :keyword: MUST

    When a VNF's Heat Orchestration Template's resource is associated
    with a single internal network, the Resource ID **MUST** contain the text
    'int\_{network-role}'.

.. req::
    :id: R-82115
    :target: VNF
    :keyword: MUST

    When a VNF's Heat Orchestration Template's resource is associated
    with a single '{vm-type}' and a single external network, the Resource
    ID text **MUST** contain both the '{vm-type}' and the '{network-role}'

      - the '{vm-type}' **MUST** appear before the '{network-role}' and **MUST**
        be separated by an underscore '_'

          - e.g.,'{vm-type}\_{network-role}', '{vm-type}\_{index}\_{network-role}'

      - note that an '{index}' value **MAY** separate the '{vm-type}' and the
        '{network-role}' and when this occurs underscores **MUST** separate the
        three values.

.. req::
    :id: R-82551
    :target: VNF
    :keyword: MUST

    When a VNF's Heat Orchestration Template's resource is associated
    with a single '{vm-type}' and a single internal network, the Resource ID
    **MUST** contain both the '{vm-type}' and the 'int\_{network-role}' and

      - the '{vm-type}' **MUST** appear before the 'int\_{network-role}' and
      **MUST** be separated by an underscore '_'

        - e.g.,'{vm-type}\_int\_{network-role}', '{vm-type}_{index}\_int\_{network-role}'

      - note that an '{index}' value **MAY** separate the '{vm-type}' and the
        'int\_{network-role}' and when this occurs underscores **MUST** separate
        the three values.

.. req::
    :id: R-67793
    :target: VNF
    :keyword: MUST NOT

    When a VNF's Heat Orchestration Template's resource is associated
    with more than one '{vm-type}' and/or more than one internal and/or
    external network, the Resource ID **MUST NOT** contain the '{vm-type}'
    and/or '{network-role}'/'int\_{network-role}'. It also should contain the
    term 'shared' and/or contain text that identifies the VNF

.. req::
    :id: R-27970
    :target: VNF
    :keyword: MAY

    When a VNF's Heat Orchestration Template's resource is associated
    with more than one '{vm-type}' and/or more than one internal and/or
    external network, the Resource ID **MAY** contain the term 'shared'
    and/or **MAY** contain text that identifies the VNF.

.. req::
    :id: R-11690
    :target: VNF
    :keyword: MUST

    When a VNF's Heat Orchestration Template's Resource ID contains
    an {index} value (e.g. multiple VMs of same {vm-type}), the '{index}'
    **MUST** start at zero and increment by one.

OpenStack Heat Resources Resource ID Naming Convention
++++++++++++++++++++++++++++++++++++++++++++++++++++++

Some OpenStack Heat Resources Resource IDs
have mandatory or suggested naming conventions.  They are provided
in the following sections.

OS::Cinder::Volume
__________________


.. req::
    :id: R-87004
    :target: VNF
    :keyword: SHOULD
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Cinder::Volume Resource ID **SHOULD** use the naming convention

       * {vm-type}_volume_{index}

    where

       * {vm-type} is the vm-type
       * {index} starts at zero and increments by one

OS::Cinder::VolumeAttachment
____________________________


.. req::
    :id: R-86497
    :target: VNF
    :keyword: SHOULD
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Cinder::VolumeAttachment Resource ID **SHOULD** use the naming convention

       * {vm-type}_volume_attachment_{index}

    where

       * {vm-type} is the vm-type
       * {index} starts at zero and increments by one

OS::Heat::CloudConfig
_____________________


.. req::
    :id: R-04747
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::Heat::CloudConfig' Resource ID **MUST** contain the '{vm-type}'.

.. req::
    :id: R-20319
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource 'OS::Heat::CloudConfig'
    Resource ID **MAY** use the naming convention

       * {vm-type}_RCC

    where

       * {vm-type} is the vm-type
       * 'RCC' signifies that it is the Resource Cloud Config

OS::Heat::MultipartMime
_______________________


.. req::
    :id: R-30804
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::Heat::MultipartMime' Resource ID **MUST** contain the '{vm-type}'.

.. req::
    :id: R-18202
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::Heat::MultipartMime' Resource ID **MAY** use the naming convention

       * {vm-type}_RMM

    where

       * {vm-type} is the vm-type
       * 'RMM' signifies that it is the Resource Multipart Mime

OS::Heat::ResourceGroup
_______________________

There is only a mandatory naming convention for a 'OS::Heat::ResourceGroup'
that is is creating sub-interfaces.


.. req::
    :id: R-64197
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Heat::ResourceGroup Resource ID that creates sub-interfaces **MUST**
    use the naming convention

       * {vm-type}_{vm-type_index}_subint_{network-role}_port_{port-index}_subinterfaces

    where

       * {vm-type} is the vm-type
       * {vm-type_index} is the instance of the {vm-type}
       * {network-role} is the network-role of the networks
         that the sub-interfaces attach to
       * {port-index} is the instance of the the port on the vm-type
         attached to the network of {network-role}

OS::Heat::SoftwareConfig
________________________


.. req::
    :id: R-08975
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::Heat::SoftwareConfig' Resource ID **MUST** contain the '{vm-type}'.

.. req::
    :id: R-03656
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::Heat::SoftwareConfig' Resource ID **MAY** use the naming convention

       * {vm-type}_RSC

    where

       * {vm-type} is the vm-type
       * 'RSC' signifies that it is the Resource Software Config

OS::Neutron::Net
________________


.. req::
    :id: R-25720
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Neutron::Net Resource ID **MUST** use the naming convention

       * int_{network-role}_network

VNF Heat Orchestration Templates can only create internal networks.
There is no {index} after {network-role} because {network-role}
**MUST** be unique in the scope of the VNF's
Heat Orchestration Template.

OS::Neutron::Port
_________________


.. req::
    :id: R-20453
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Neutron::Port that is attaching to an external network Resource ID
    **MUST** use the naming convention

       * {vm-type}_{vm-type_index}_{network-role}_port_{port-index}

    where

       * {vm-type} is the vm-type
       * {vm-type_index} is the instance of the {vm-type}
       * {network-role} is the network-role of the network
         that the port is attached to
       * {port-index} is the instance of the the port on the vm-type
         attached to the network of {network-role}

.. req::
    :id: R-26351
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Neutron::Port that is attaching to an internal network Resource ID
    **MUST** use the naming convention

       * {vm-type}_{vm-type_index}_int_{network-role}_port_{port-index}

    where

       * {vm-type} is the vm-type
       * {vm-type_index} is the instance of the {vm-type}
       * {network-role} is the network-role of the network
         that the port is attached to
       * {port-index} is the instance of the the port on the vm-type
         attached to the network of {network-role}

.. req::
    :id: R-27469
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Neutron::Port that is creating a *Reserve Port* with an IPv4 address
    Resource ID **MUST** use the naming convention

       * reserve_port_{vm-type}_{network-role}_floating_ip_{index}

    where

       * {vm-type} is the vm-type
       * {network-role} is the network-role of the network
         that the port is attached to
       * {index} is the instance of the IPv4 *Reserve Port*
         for the vm-type attached to the network of {network-role}

.. req::
    :id: R-68520
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource OS::Neutron::Port
    that is creating a *Reserve Port* with an IPv6 address Resource ID
    **MUST** use the naming convention

       * reserve_port_{vm-type}_{network-role}_floating_v6_ip_{index}

    where

       * {vm-type} is the vm-type
       * {network-role} is the network-role of the network
         that the port is attached to
       * {index} is the instance of the IPv6 *Reserve Port*
         for the vm-type attached to the network of {network-role}

OS::Neutron::SecurityGroup
__________________________


.. req::
    :id: R-08775
    :target: VNF
    :keyword: SHOULD
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Neutron::SecurityGroup that is applicable to one {vm-type} and
    more than one network (internal and/or external) Resource ID
    **SHOULD** use the naming convention

       * {vm-type}_security_group

    where

       * {vm-type} is the vm-type

.. req::
    :id: R-03595
    :target: VNF
    :keyword: SHOULD
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Neutron::SecurityGroup that is applicable to more than
    one {vm-type} and one external network Resource ID **SHOULD**
    use the naming convention

       * {network-role}_security_group

    where

       * {network-role} is the network-role

.. req::
    :id: R-73213
    :target: VNF
    :keyword: SHOULD
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Neutron::SecurityGroup that is applicable to more than
    one {vm-type} and one internal network Resource ID **SHOULD**
    use the naming convention

       * int_{network-role}_security_group

    where

       * {network-role} is the network-role

.. req::
    :id: R-17334
    :target: VNF
    :keyword: SHOULD
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Neutron::SecurityGroup that is applicable to one {vm-type}
    and one external network Resource ID **SHOULD** use the naming convention

       * {vm-type}_{network-role}_security_group

    where

       * {vm-type} is the vm-type
       * {network-role} is the network-role

.. req::
    :id: R-14198
    :target: VNF
    :keyword: SHOULD
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Neutron::SecurityGroup that is applicable to one {vm-type}
    and one internal network Resource ID **SHOULD** use the naming convention

       * {vm-type}_int_{network-role}_security_group

    where

       * {vm-type} is the vm-type
       * {network-role} is the network-role

.. req::
    :id: R-30005
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Neutron::SecurityGroup that is applicable to more than one
    {vm-type} and more than one network (internal and/or external)
    Resource ID **MAY** use the naming convention

       * shared_security_group

    or

       * {vnf-type}_security_group

    where

       * {vnf-type} describes the VNF

OS::Neutron::Subnet
___________________


.. req::
    :id: R-59434
    :target: VNF
    :keyword: SHOULD
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Neutron::Subnet Resource ID **SHOULD** use the naming convention

       * int_{network-role}_subnet_{index}

    where

       * {network-role} is the network-role
       * {index} is the {index} of the subnet of the network

OS::Nova::Keypair
_________________


.. req::
    :id: R-24997
    :target: VNF
    :keyword: SHOULD
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::Nova::Keypair applies to one {vm-type} Resource ID **SHOULD**
    use the naming convention

       * {vm-type}_keypair_{index}

    where

       * {network-role} is the network-role
       * {index} is the {index} of the keypair

.. req::
    :id: R-65516
    :target: VNF
    :keyword: SHOULD
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource OS::Nova::Keypair
    applies to all Virtual Machines in the the VNF, the Resource ID **SHOULD**
    use the naming convention

       * {vnf-type}_keypair

    where

       * {vnf-type} describes the VNF

OS::Nova::Server
________________


.. req::
    :id: R-29751
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource OS::Nova::Server
    Resource ID **MUST** use the naming convention

       * {vm-type}_server_{index}

    where

       * {vm-type} is the vm-type
       * {index} is the index

OS::Nova::ServerGroup
_____________________


.. req::
    :id: R-15189
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource OS::Nova::ServerGroup
    Resource ID **MAY** use the naming convention

       * {vm-type}_RSG

    or

       * {vm-type}_Server_Grp

    or

       * {vm-type}_ServerGroup

    or

       * {vm-type}_servergroup

Contrail Heat Resources Resource ID Naming Convention
+++++++++++++++++++++++++++++++++++++++++++++++++++++

Some Contrail Heat Resources Resource IDs
have mandatory or suggested naming conventions. They are provided
in the following sections.


OS::ContrailV2::InstanceIp
__________________________


.. req::
    :id: R-53310
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::InstanceIp' that is configuring an IPv4 Address
    on a port attached to an external network Resource ID **MUST**
    use the naming convention

       *  {vm-type}_{vm-type_index}_{network-role}_vmi_{vmi_index}_IP_{index}

    where

       * {vm-type} is the vm-type
       * {vm-type_index} is the instance of the {vm-type}
       * {network-role} is the network-role of the network
         that the port is attached to
       * {vmi_index} is the instance of the the virtual machine interface
         (e.g., port)  on the vm-type
         attached to the network of {network-role}
       * 'IP' signifies that an IPv4 address is being configured
       * {index} is the index of the IPv4 address

.. req::
    :id: R-46128
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::InstanceIp' that is configuring an
    IPv6 Address on a port attached to an external network
    Resource ID **MUST** use the naming convention

       *  {vm-type}_{vm-type_index}_{network-role}_vmi_{vmi_index}_v6_IP_{index}

    where

       * {vm-type} is the vm-type
       * {vm-type_index} is the instance of the {vm-type}
       * {network-role} is the network-role of the network
         that the port is attached to
       * {vmi_index} is the instance of the the virtual machine interface
         (e.g., port)  on the vm-type
         attached to the network of {network-role}
       * 'v6_IP' signifies that an IPv6 address is being configured
       * {index} is the index of the IPv6 address

.. req::
    :id: R-62187
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::InstanceIp' that is configuring an
    IPv4 Address on a port attached to an internal network
    Resource ID **MUST** use the naming convention

       *  {vm-type}_{vm-type_index}_int_{network-role}_vmi_{vmi_index}_IP_{index}

    where

       * {vm-type} is the vm-type
       * {vm-type_index} is the instance of the {vm-type}
       * {network-role} is the network-role of the network
         that the port is attached to
       * {vmi_index} is the instance of the the virtual machine interface
         (e.g., port)  on the vm-type
         attached to the network of {network-role}
       * 'IP' signifies that an IPv4 address is being configured
       * {index} is the index of the IPv4 address

.. req::
    :id: R-87563
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::InstanceIp' that is configuring an
    IPv6 Address on a port attached to an internal network
    Resource ID **MUST** use the naming convention

       *  {vm-type}_{vm-type_index}_int_{network-role}_vmi_{vmi_index}_v6_IP_{index}

    where

       * {vm-type} is the vm-type
       * {vm-type_index} is the instance of the {vm-type}
       * {network-role} is the network-role of the network
         that the port is attached to
       * {vmi_index} is the instance of the the virtual machine interface
         (e.g., port)  on the vm-type
         attached to the network of {network-role}
       * 'v6_IP' signifies that an IPv6 address is being configured
       * {index} is the index of the IPv6 address

.. req::
    :id: R-20947
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::InstanceIp' that is configuring an IPv4 Address
    on a sub-interface port attached to a sub-interface network
    Resource ID **MUST** use the naming convention

       *  {vm-type}_{vm-type_index}_subint_{network-role}_vmi_{vmi_index}_IP_{index}

    where

       * {vm-type} is the vm-type
       * {vm-type_index} is the instance of the {vm-type}
       * {network-role} is the network-role of the network
         that the port is attached to
       * {vmi_index} is the instance of the the virtual machine interface
         (e.g., port)  on the vm-type
         attached to the network of {network-role}
       * 'IP' signifies that an IPv4 address is being configured
       * {index} is the index of the IPv4 address

.. req::
    :id: R-88540
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::InstanceIp' that is configuring an IPv6 Address
    on a sub-interface port attached to a sub-interface network
    Resource ID **MUST** use the naming convention

       *  {vm-type}_{vm-type_index}_subint_{network-role}_vmi_{vmi_index}_v6_IP_{index}

    where

       * {vm-type} is the vm-type
       * {vm-type_index} is the instance of the {vm-type}
       * {network-role} is the network-role of the network
         that the port is attached to
       * {vmi_index} is the instance of the the virtual machine interface
         (e.g., port)  on the vm-type
         attached to the network of {network-role}
       * 'v6_IP' signifies that an IPv6 address is being configured
       * {index} is the index of the IPv6 address

OS::ContrailV2::InterfaceRouteTable
___________________________________


.. req::
    :id: R-81214
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::InterfaceRouteTable' Resource ID **MUST**
    contain the '{network-role}'.

.. req::
    :id: R-28189
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::InterfaceRouteTable' Resource ID **MAY**
    use the naming convention

       * {network-role}_RIRT

    where

       * {network-role} is the network-role
       * 'RIRT' signifies that it is the Resource Interface Route Table

OS::ContrailV2::NetworkIpam
___________________________


.. req::
    :id: R-30753
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::NetworkIpam' Resource ID **MUST**
    contain the '{network-role}'.

.. req::
    :id: R-81979
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::NetworkIpam' Resource ID **MAY**
    use the naming convention

       * {network-role}_RNI

    where

       * {network-role} is the network-role
       * 'RNI' signifies that it is the Resource Network IPAM

OS::ContrailV2::PortTuple
_________________________


.. req::
    :id: R-20065
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::PortTuple' Resource ID **MUST**
    contain the '{vm-type}'.

.. req::
    :id: R-84457
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::PortTuple' Resource ID **MAY**
    use the naming convention

       * {vm-type}_RPT

    where

       * {vm-type} is the vm-type
       * 'RPT' signifies that it is the Resource Port Tuple

OS::ContrailV2::ServiceHealthCheck
__________________________________


.. req::
    :id: R-76014
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::ServiceHealthCheck' Resource ID **MUST**
    contain the '{vm-type}'.

.. req::
    :id: R-65618
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::ServiceHealthCheck' Resource ID
    **MAY** use the naming convention

       * {vm-type}_RSHC_{LEFT|RIGHT}

    where

       * {vm-type} is the vm-type
       * 'RSHC' signifies that it is the Resource Service Health Check
       * 'LEFT' is used if the Service Health Check is on the left interface
       * 'RIGHT' is used if the Service Health Check is on the right interface

OS::ContrailV2::ServiceTemplate
_______________________________


.. req::
    :id: R-16437
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::ServiceTemplate' Resource ID **MUST**
    contain the '{vm-type}'.

.. req::
    :id: R-14447
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    'OS::ContrailV2::ServiceTemplate' Resource ID **MAY**
    use the naming convention

       * {vm-type}_RST_{index}

    where

       * {vm-type} is the vm-type
       * 'RST' signifies that it is the Resource Service Template
       * '{index}' is is the index

OS::ContrailV2::VirtualMachineInterface
_______________________________________


.. req::
    :id: R-96253
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::ContrailV2::VirtualMachineInterface that is attaching
    to an external network Resource ID **MUST**
    use the naming convention

       * {vm-type}_{vm-type_index}_{network-role}_vmi_{vmi_index}

    where

       * {vm-type} is the vm-type
       * {vm-type_index} is the instance of the {vm-type}
       * {network-role} is the network-role of the network
         that the port (i.e. virtual machine interface) is attached to
       * {vmi_index} is the instance of the the vmi on the vm-type
         attached to the network of {network-role}

.. req::
    :id: R-50468
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::ContrailV2::VirtualMachineInterface that is attaching
    to an internal network Resource ID **MUST** use the naming convention

       * {vm-type}_{vm-type_index}_int_{network-role}_vmi_{vmi_index}

    where

       * {vm-type} is the vm-type
       * {vm-type_index} is the instance of the {vm-type}
       * {network-role} is the network-role of the network
         that the port (i.e. virtual machine interface) is attached to
       * {vmi_index} is the instance of the the vmi on the vm-type
         attached to the network of {network-role}

.. req::
    :id: R-54458
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::ContrailV2::VirtualMachineInterface that is attaching to
    a sub-interface network Resource ID **MUST** use the naming convention

       * {vm-type}_{vm-type_index}_subint_{network-role}_vmi_{vmi_index}

    where

       * {vm-type} is the vm-type
       * {vm-type_index} is the instance of the {vm-type}
       * {network-role} is the network-role of the network
         that the port (i.e. virtual machine interface) is attached to
       * {vmi_index} is the instance of the the vmi on the vm-type
         attached to the network of {network-role}

OS::ContrailV2::VirtualNetwork
______________________________


.. req::
    :id: R-99110
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Resource
    OS::ContrailV2::VirtualNetwork Resource ID **MUST**
    use the naming convention

       * 'int_{network-role}_network'

    or

       * 'int_{network-role}_RVN' where RVN represents Resource Virtual Network

VNF Heat Orchestration Templates can only create internal networks.
There is no {index} after {network-role} because {network-role}
**MUST** be unique in the scope of the VNF's
Heat Orchestration Template.

Note that the first option is preferred.

Resource: OS::Nova::Server - Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The resource OS::Nova::Server manages the running virtual machine (VM)
instance within an OpenStack cloud. (See
https://docs.openstack.org/developer/heat/template_guide/openstack.html#OS::Nova::Server.)

The following four properties of the OS::Nova::Server must follow
the ONAP parameter naming convention. The four properties are:

1. image

2. flavor

3. name

4. availability\_zone

Requirement R-01455 defines how the '{vm-type}' is defined.

Requirement R-82481 defines how the '{vm-type}' is used.

The table below provides a summary. The sections that follow provides
the detailed requirements.

.. csv-table:: **Table 4 OS::Nova::Server Resource Property Parameter Naming Convention**
   :header: Property Name,Parameter Type,Parameter Name,Parameter Value Provided to Heat
   :align: center
   :widths: auto

   OS::Nova::Server, image, string, {vm-type}\_image\_name, Environment File
   OS::Nova::Server, flavor, string, {vm-type}\_flavor\_name, Environment File
   OS::Nova::Server, name, string, {vm-type}\_name\_{index}, ONAP
   OS::Nova::Server, name, CDL, {vm-type}\_names, ONAP
   OS::Nova::Server, availability\_zone, string, availability\_zone\_{index}, ONAP

Property: image
+++++++++++++++


.. req::
    :id: R-71152
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'image' parameter **MUST** be declared as
    type: 'string'.

.. req::
    :id: R-58670
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'image' parameter name **MUST** follow the
    naming convention '{vm-type}_image_name'.

.. req::
    :id: R-91125
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'image' parameter **MUST** be enumerated in
    the Heat Orchestration Template's Environment File and a value **MUST** be
    assigned.

.. req::
    :id: R-57282
    :target: VNF
    :keyword: MUST

    Each VNF's Heat Orchestration Template's '{vm-type}'
    **MUST** have a unique parameter name for the 'OS::Nova::Server'
    property 'image' even if more than one {vm-type} shares the same image.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     {vm-type}_image_name:
         type: string
         description: {vm-type} server image

Property: flavor
++++++++++++++++


.. req::
    :id: R-50436
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'flavor' parameter **MUST** be declared as
    type: 'string'.

.. req::
    :id: R-45188
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'flavor' parameter name **MUST** follow the
    naming convention '{vm-type}_flavor_name'.

.. req::
    :id: R-69431
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'flavor' parameter **MUST** be enumerated in the
    Heat Orchestration Template's Environment File and a value **MUST** be
    assigned.

.. req::
    :id: R-40499
    :target: VNF
    :keyword: MUST

    Each VNF's Heat Orchestration Template's '{vm-type}' **MUST**
    have a unique parameter name for the 'OS::Nova::Server' property
    'flavor' even if more than one {vm-type} shares the same flavor.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     {vm-type}_flavor_name:
         type: string
         description: {vm-type} flavor

Property: Name
++++++++++++++


.. req::
    :id: R-51430
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'name' parameter **MUST** be declared as
    either type 'string' or type 'comma\_delimited\_list".

.. req::
    :id: R-54171
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'name' parameter is defined as a 'string',
    the parameter name **MUST** follow the naming convention
    '{vm-type}\_name\_{index}', where {index} is a numeric value that starts
    at zero and increments by one.

.. req::
    :id: R-40899
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'name' parameter is defined as a 'string',
    a parameter **MUST** be declared for each 'OS::Nova::Server' resource
    associated with the '{vm-type}'.

.. req::
    :id: R-87817
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'name' parameter is defined as a
    'comma_delimited_list', the parameter name **MUST** follow the naming
    convention '{vm-type}_names'.

.. req::
    :id: R-85800
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'name' parameter is defined as a
    'comma_delimited_list', a parameter **MUST** be delcared once for all
    'OS::Nova::Server' resources associated with the '{vm-type}'.

.. req::
    :id: R-22838
    :target: VNF
    :keyword: MUST NOT

    The VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'name' parameter **MUST NOT** be enumerated
    in the Heat Orchestration Template's Environment File.

If a VNF's Heat Orchestration Template's contains more than three
OS::Nova::Server resources of a given {vm-type}, the comma\_delimited\_list
form of the parameter name (i.e., '{vm-type}\_names') should be used to
minimize the number of unique parameters defined in the template.


*Example: Parameter Definition*

.. code-block:: yaml

  parameters:

  {vm-type}_names:
    type: comma_delimited_list
    description: VM Names for {vm-type} VMs

  {vm-type}_name_{index}:
    type: string
    description: VM Name for {vm-type} VM {index}

*Example: comma\_delimited\_list*

In this example, the {vm-type} has been defined as "lb" for load balancer.

.. code-block:: yaml

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

In this example, the {vm-type} has been defined as "lb" for load balancer.

.. code-block:: yaml

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


.. req::
    :id: R-44271
    :target: VNF
    :keyword: SHOULD NOT

    The VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'name' parameter value **SHOULD NOT**
    contain special characters since the Contrail GUI has a limitation
    displaying special characters.

However, if special characters must be used, the only special characters
supported are:

--- \" ! $ ' (\ \ ) = ~ ^ | @ ` { } [ ] > , . _


Property: availability\_zone
++++++++++++++++++++++++++++


.. req::
    :id: R-98450
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'availability\_zone' parameter name
    **MUST** follow the naming convention 'availability\_zone\_{index}'
    where the '{index}' **MUST** start at zero and increment by one.

.. req::
    :id: R-23311
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'availability_zone' parameter **MUST**
    be declared as type: 'string'.

The parameter must not be declared as type 'comma\_delimited\_list',
ONAP does not support it.


.. req::
    :id: R-59568
    :target: VNF
    :keyword: MUST NOT

    The VNF's Heat Orchestration Template's Resource
    'OS::Nova::Server' property 'availability_zone' parameter **MUST NOT**
    be enumerated in the Heat Orchestration Template's Environment File.

Example Parameter Definition

.. code-block:: yaml

  parameters:
    availability_zone_{index}:
      type: string
      description: availability zone {index} name

Requirement R-90279 states that a VNF Heat Orchestration's template's
parameter MUST be used in a resource with the exception of the parameters
for the OS::Nova::Server resource property availability_zone.


.. req::
    :id: R-01359
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchstration Template that contains an
    'OS::Nova:Server' Resource **MAY** define a parameter for the property
    'availability_zone' that is not utilized in any 'OS::Nova::Server'
    resources in the Heat Orchestration Template.

Example
+++++++

The example below depicts part of a Heat Orchestration Template that
uses the four OS::Nova::Server properties discussed in this section.

In the Heat Orchestration Template below, four Virtual
Machines (OS::Nova::Server) are created: two dns servers with
{vm-type} set to "dns" and two oam servers with {vm-type} set to "oam".
Note that the parameter associated with the property name is a
comma_delimited_list for dns and a string for oam.

.. code-block:: yaml

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


.. req::
    :id: R-99798
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's Virtual Machine
    (i.e., OS::Nova::Server Resource) **MAY** boot from an image or **MAY**
    boot from a Cinder Volume.

.. req::
    :id: R-83706
    :target: VNF
    :keyword: MUST

    When a VNF's Heat Orchestration Template's Virtual Machine
    (i.e., 'OS::Nova::Server' Resource) boots from an image, the
    'OS::Nova::Server' resource property 'image' **MUST** be used.

The requirements associated with
the 'image' property are detailed in `Property: image`_


.. req::
    :id: R-69588
    :target: VNF
    :keyword: MUST

    When a VNF's Heat Orchestration Template's Virtual Machine
    (i.e., 'OS::Nova::Server' Resource) boots from Cinder Volume, the
    'OS::Nova::Server' resource property 'block_device_mapping' or
    'block_device_mapping_v2' **MUST** be used.

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


.. req::
    :id: R-37437
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource **MUST** contain the metadata map value parameter 'vnf_id'.

.. req::
    :id: R-07507
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vnf_id' **MUST** be declared
    as type: 'string'.

.. req::
    :id: R-55218
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vnf_id' **MUST NOT** have
    parameter contraints defined.

.. req::
    :id: R-20856
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vnf_id' **MUST NOT** be
    enumerated in the Heat Orchestration Template's environment file.

.. req::
    :id: R-44491
    :target: VNF
    :keyword: MUST NOT

    If a VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vnf_id' is passed into a
    Nested YAML file, the parameter name 'vnf_id' **MUST NOT** change.

*Example 'vnf_id' Parameter Definition*

.. code-block:: yaml

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


.. req::
    :id: R-71493
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource **MUST** contain the metadata map value parameter
    'vf\_module\_id'.

.. req::
    :id: R-82134
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf\_module\_id' **MUST**
    be declared as type: 'string'.

.. req::
    :id: R-98374
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf\_module\_id' **MUST NOT**
    have parameter contraints defined.

.. req::
    :id: R-72871
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf\_module\_id' **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.

.. req::
    :id: R-86237
    :target: VNF
    :keyword: MUST NOT

    If a VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf_module_id' is passed
    into a Nested YAML file, the parameter name 'vf\_module\_id'
    **MUST NOT** change.

*Example 'vf\_module\_id' Parameter Definition*

.. code-block:: yaml

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


.. req::
    :id: R-72483
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource **MUST** contain the metadata map value parameter
    'vnf_name'.

.. req::
    :id: R-62428
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vnf_name' **MUST** be
    declared as type: 'string'.

.. req::
    :id: R-44318
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vnf\_name' **MUST NOT** have
    parameter contraints defined.

.. req::
    :id: R-36542
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vnf\_name' **MUST NOT** be
    enumerated in the Heat Orchestration Template's environment file.

.. req::
    :id: R-16576
    :target: VNF
    :keyword: MUST NOT

    If a VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vnf_name' is passed into a
    Nested YAML file, the parameter name 'vnf_name' **MUST NOT** change.

*Example 'vnf\_name' Parameter Definition*

.. code-block:: yaml

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


.. req::
    :id: R-68023
    :target: VNF
    :keyword: SHOULD

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource **SHOULD** contain the metadata map value parameter
    'vf\_module\_name'.

.. req::
    :id: R-39067
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf\_module\_name' **MUST**
    be declared as type: 'string'.

.. req::
    :id: R-15480
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf\_module\_name'
    **MUST NOT** have parameter contraints defined.

.. req::
    :id: R-80374
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf\_module\_name'
    **MUST NOT** be enumerated in the Heat Orchestration Template's
    environment file.

.. req::
    :id: R-49177
    :target: VNF
    :keyword: MUST

    If a VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf\_module\_name' is passed
    into a Nested YAML file, the parameter name 'vf\_module\_name'
    **MUST NOT** change.

*Example 'vf_module_name' Parameter Definition*

.. code-block:: yaml

  parameters:

    vf_module_name:
      type: string
      description: Unique name for this VNF Module instance

vm\_role
++++++++

The OS::Nova::Server Resource metadata map value parameter 'vm-role'
is a metadata tag that describes the role of the Virtual Machine.
The 'vm\_role' is stored in ONAP's A&AI module and is
available for use by other ONAP components and/or north bound systems.


.. req::
    :id: R-85328
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource **MAY** contain the metadata map value parameter 'vm_role'.

.. req::
    :id: R-95430
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vm_role' **MUST** be
    declared as type: 'string'.

.. req::
    :id: R-67597
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vm_role' **MUST NOT** have
    parameter contraints defined.


.. req::
    :id: R-46823
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vnf_name' **MUST** be
    either

     - enumerated in the VNF's Heat Orchestration
       Template's environment file.

     - hard coded in the VNF's Heat Orchestration
       Template's OS::Nova::Resource metadata property.

Defining the 'vm_role' as the '{vm-type}' is a recommended convention


.. req::
    :id: R-86476
    :target: VNF
    :keyword: MUST

    If a VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vm_role' value **MUST** only
    contain alphanumeric characters and underscores '_'.

.. req::
    :id: R-70757
    :target: VNF
    :keyword: MUST NOT

    If a VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vm_role' is passed into a
    Nested YAML file, the parameter name 'vm_role' **MUST NOT** change.

*Example 'vm\_role' Parameter Definition*

.. code-block:: yaml

  parameters:

    vm_role:
      type: string
      description: Unique role for this VM

*Example: 'vm-role' Definition: Hard Coded in
OS::Nova::Resource metadata property*

.. code-block:: yaml

  resources:

    dns_server_0
      type: OS::Nova::Server
      properties:
        . . . .
        metadata:
          vm_role: dns

*Example 'vm-role' Definition: Defined in Environment file
and retrieved via 'get_param'*

.. code-block:: yaml

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

.. code-block:: yaml

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


.. req::
    :id: R-50816
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource **MAY** contain the metadata map value parameter
    'vf\_module\_index'.

.. req::
    :id: R-54340
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf\_module\_index' **MUST** be
    declared as type: 'number'.

.. req::
    :id: R-09811
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf\_module\_index' **MUST NOT**
    have parameter contraints defined.

.. req::
    :id: R-37039
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf\_module\_index' **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.

.. req::
    :id: R-22441
    :target: VNF
    :keyword: MUST NOT

    If a VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf\_module\_index' is passed
    into a Nested YAML file, the parameter name 'vf\_module\_index'
    **MUST NOT** change.

.. req::
    :id: R-55306
    :target: VNF
    :keyword: MUST NOT

    If a VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'vf\_module\_index' **MUST NOT** be
    used in a VNF's Volume Template; it is not supported.

The vf\_module_index parameter indicates which instance of the module is being
deployed into the VNF.
This parameter may be used in cases where multiple instances of the same
incremental module may be instantiated for scaling purposes. The index
can be used in the Heat Orchestration Template for indexing into a
pseudo-constant array parameter when unique values are required for each
module instance, e.g., for fixed private IP addresses on VM types.

The vf\_module\_index will start at 0 for the first instance of a module
type. Subsequent instances of the same module type will receive the
lowest unused index. This means that indexes will be reused if a module
is deleted and re-added. As an example, if three copies of a module are
deployed with vf\_module\_index values of 0, 1, and 2 then subsequently
the second one is deleted (index 1), and then re-added, index 1 will be
reused.

*Example*

In this example, the {vm-type} has been defined as oam\_vm to represent
an OAM VM. An incremental heat module is used to deploy the OAM VM. The
OAM VM attaches to an internal control network which has a
{network-role} of ctrl. A maximum of four OAM VMs can be deployed. The
environment file contains the four IP addresses that each successive OAM
VM will be assigned. The vf\_module\_index is used as the index to
determine the IP assignment.

Environment File

.. code-block:: yaml

  parameters:
    oam_vm_int_ctrl_ips: 10.10.10.1,10.10.10.2,10.10.10.3,10.10.10.4

YAML File

.. code-block:: yaml

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
        fixed_ips: [ { "ip_address": {get_param: [ oam_vm_int_ctrl_ips, { get_param, vf_module_index]}}}]

workload\_context
++++++++++++++++++


.. req::
    :id: R-47061
    :target: VNF
    :keyword: SHOULD

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource **SHOULD** contain the metadata map value parameter
    'workload_context'.

.. req::
    :id: R-74978
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'workload_context' **MUST** be
    declared as type: 'string'.

.. req::
    :id: R-34055
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'workload_context' **MUST NOT**
    have parameter contraints defined.

.. req::
    :id: R-02691
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'workload_context' **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.

.. req::
    :id: R-75202
    :target: VNF
    :keyword: MUST NOT

    If a VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'workload_context' is passed
    into a Nested YAML file, the parameter name 'workload_context'
    **MUST NOT** change.

The 'workload\_context' parameter value will be chosen by the Service Model
Distribution context client in VID and will be supplied to the
Heat Orchestration Template by ONAP at orchestration time.

*Example Parameter Definition*

.. code-block:: yaml

  parameters:
    workload_context:
      type: string
      description: Workload Context for this VNF instance


*Example OS::Nova::Server with metadata*

.. code-block:: yaml

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

environment\_context
++++++++++++++++++++++


.. req::
    :id: R-88536
    :target: VNF
    :keyword: SHOULD

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource **SHOULD** contain the metadata map value parameter
    'environment_context'.

.. req::
    :id: R-20308
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'environment_context' **MUST**
    be declared as type: 'string'.

.. req::
    :id: R-56183
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'environment_context' **MUST NOT**
    have parameter contraints defined.

.. req::
    :id: R-13194
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'environment_context' **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.

.. req::
    :id: R-62954
    :target: VNF
    :keyword: MUST NOT

    If a VNF's Heat Orchestration Template's OS::Nova::Server
    Resource metadata map value parameter 'environment_context' is
    passed into a Nested YAML file, the parameter name
    'environment_context' **MUST NOT** change.

The 'environment\_context' parameter value will be defined by the
service designer as part of the service model during the SDC
on-boarding process and will be supplied to the Heat Orchestration
Template by ONAP at orchestration time.


*Example Parameter Definition*

.. code-block:: yaml

  parameters:
    environment_context:
      type: string
      description: Environment Context for this VNF instance


*Example OS::Nova::Server with metadata*

.. code-block:: yaml

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

.. code-block:: yaml

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

The values associated with these properties may reference an external
network or internal network. External networks and internal
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


.. req::
    :id: R-93272
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF **MAY** have one or more ports connected to a unique
    external network. All VNF ports connected to the unique external
    network **MUST** have Cloud Assigned IP Addresses
    or **MUST** have ONAP SDN-C assigned IP addresses.

.. req::
    :id: R-13841
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF **MAY** have one or more ports connected to a unique
    internal network. All VNF ports connected to the unique internal
    network **MUST** have Cloud Assigned IP Addresses
    or **MUST** have statically assigned IP addresses.

.. req::
    :id: R-07577
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If the VNF's ports connected to a unique network (internal or external)
    and the port's IP addresses are Cloud Assigned IP Addresses,
    all the IPv4 Addresses **MUST** be from
    the same subnet and all the IPv6 Addresses **MUST** be from the
    same subnet.

.. req::
    :id: R-45602
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF's Port is attached to a network (internal or external)
    and the port's IP addresses are Cloud Assigned by OpenStack's DHCP
    Service, the 'OS::Neutron::Port' Resource's

       * property 'fixed_ips' map property 'ip_address' **MUST NOT** be used
       * property 'fixed_ips' map property 'subnet'/'subnet_id' **MAY** be used

.. req::
    :id: R-63956
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If the VNF's ports connected to a unique external network
    and the port's IP addresses are ONAP SDN-C assigned IP Addresses,
    the IPv4 Addresses **MAY** be from different subnets and the IPv6
    Addresses **MAY** be from different subnets.

.. req::
    :id: R-48880
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF's Port is attached to an external network and the port's
    IP addresses are assigned by ONAP's SDN-Controller,
    the 'OS::Neutron::Port' Resource's

       * property 'fixed_ips' map property 'ip_address' **MUST** be used
       * property 'fixed_ips' map property 'subnet'/'subnet_id' **MUST NOT** be used

.. req::
    :id: R-18001
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If the VNF's ports connected to a unique internal network
    and the port's IP addresses are statically assigned IP Addresses,
    the IPv4 Addresses **MAY** be from different subnets and the
    IPv6 Addresses **MAY** be from different subnets.

.. req::
    :id: R-70964
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF's Port is attached to an internal network and the port's
    IP addresses are statically assigned by the VNF's Heat Orchestration\
    Template (i.e., enumerated in the Heat Orchestration Template's
    environment file), the 'OS::Neutron::Port' Resource's

       * property 'fixed_ips' map property 'ip_address' **MUST** be used
       * property 'fixed_ips' map property 'subnet'/'subnet_id'
         **MUST NOT** be used

Property: network
+++++++++++++++++

The Resource 'OS::Neutron::Port' property 'network' determines what network
the port is attached to.


.. req::
    :id: R-18008
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource 'OS::Neutron::Port'
    property 'network' parameter **MUST** be declared as type: 'string'.

.. req::
    :id: R-62983
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource 'OS::Neutron::Port'
    is attaching to an external network, the 'network' parameter name **MUST**

    - follow the naming convention '{network-role}_net_id' if the Neutron
      network UUID value is used to reference the network
    - follow the naming convention '{network-role}_net_name' if the OpenStack
      network name is used to reference the network.

    where '{network-role}' is the network-role of the external network and
    a 'get_param' **MUST** be used as the intrinsic function.

.. req::
    :id: R-86182
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource 'OS::Neutron::Port'
    is attaching to an internal network, and the internal network is created in a different
    Heat Orchestration Template than the 'OS::Neutron::Port', the 'network'
    parameter name **MUST**

    - follow the naming convention 'int\_{network-role}_net_id' if the Neutron
      network UUID value is used to reference the network
    - follow the naming convention 'int\_{network-role}_net_name' if the
      OpenStack network name in is used to reference the network.

    where '{network-role}' is the network-role of the internal network and a 'get_param' **MUST** be used as the intrinsic function.

In Requirement R-86182, the internal network is created in the VNF's
Base Module (Heat Orchestration Template) and the parameter name is
declared in the Base Module's outputs' section.
The output parameter name will be declared as a parameter in the
'parameters' section of the incremental module.


.. req::
    :id: R-93177
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's
    Resource 'OS::Neutron::Port' is attaching to an internal
    network, and the internal network is created in the same Heat
    Orchestration Template than the 'OS::Neutron::Port', the 'network'
    parameter name **MUST** obtain the UUID of the internal network
    by using the intrinsic function 'get_resource' or 'get_attr'
    and referencing the Resource ID of the internal network.

.. req::
    :id: R-29872
    :target: VNF
    :keyword: MUST NOT

    The VNF's Heat Orchestration Template's Resource 'OS::Nova::Server'
    property 'network' parameter **MUST NOT** be enumerated in the Heat
    Orchestration Template's Environment File.

The parameter values for external networks are provided by ONAP
to the VNF's Heat Orchestration Template at orchestration time.

The parameter values for internal networks created in the VNF's Base Module
Heat Orchestration Template
are provided to the VNF's Incremental Module Heat Orchestration Template
at orchestration time.

*Example Parameter Definition of External Networks*

.. code-block:: yaml

  parameters:

    {network-role}_net_id:
      type: string
      description: Neutron UUID for the external {network-role} network

    {network-role}_net_name:
      type: string
      description: Neutron name for the external {network-role} network


*Example Parameter Definition of Internal Networks in an Incremental Module*

.. code-block:: yaml

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


.. req::
    :id: R-34037
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's resource 'OS::Neutron::Port'
    property 'fixed_ips' map property 'ip_address' parameter **MUST**
    be declared as either type 'string' or type 'comma_delimited_list'.

.. req::
    :id: R-40971
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' is attaching to an external network, and an IPv4 address is
    assigned using the property
    'fixed_ips' map property 'ip_address' and the parameter type is defined
    as a string, the parameter name **MUST** follow the naming
    convention
    - '{vm-type}_{network-role}\_ip\_{index}'

where

    - '{vm-type}' is the {vm-type} associated with the OS::Nova::Server
    - '{network-role}' is the {network-role} of the external network
    - the value for {index} must start at zero (0) and increment by one

.. req::
    :id: R-39841
    :target: VNF
    :keyword: MUST NOT

    The VNF's Heat Orchestration Template's Resource 'OS::Neutron::Port'
    property 'fixed_ips' map property 'ip_address' parameter
    '{vm-type}_{network-role}\_ip\_{index}' **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

ONAP's SDN-Controller assigns the IP Address and ONAP provides
the value at orchestration to the Heat Orchestration Template.

*Example External Network IPv4 Address string Parameter Definition*

.. code-block:: yaml

  parameters:

    {vm-type}_{network-role}_ip_{index}:
      type: string
      description: Fixed IPv4 assignment for {vm-type} VM {index} on the{network-role} network


.. req::
    :id: R-04697
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource 'OS::Neutron::Port'
    is attaching to an external network, and an IPv4 address is assigned using
    the property 'fixed_ips' map property 'ip_address' and the parameter type
    is defined as a comma_delimited_list, the parameter name **MUST** follow the
    naming convention

      * '{vm-type}_{network-role}_ips',

    where

      * '{vm-type}' is the {vm-type} associated with the OS::Nova::Server
      * '{network-role}' is the {network-role} of the external network

.. req::
    :id: R-98905
    :target: VNF
    :keyword: MUST NOT

    The VNF's Heat Orchestration Template's Resource 'OS::Neutron::Port'
    property 'fixed_ips' map property 'ip_address' parameter
    '{vm-type}_{network-role}_ips' **MUST NOT** be enumerated in the VNF's
    Heat Orchestration Template's Environment File.

ONAP's SDN-Controller assigns the IP Address and ONAP provides
the value at orchestration to the Heat Orchestration Template.

*Example External Network IPv4 Address comma_delimited_list
Parameter Definition*

.. code-block:: yaml

  parameters:

    {vm-type}_{network-role}_ips:
      type: comma_delimited_list
      description: Fixed IPv4 assignments for {vm-type} VMs on the {network-role} network


.. req::
    :id: R-71577
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' is attaching to an external network, and an IPv6 address
    is assigned using the property 'fixed_ips' map property 'ip_address' and
    the parameter type is defined as a string, the parameter name **MUST** follow
    the naming convention

      * '{vm-type}_{network-role}\_v6\_ip\_{index}'

    where

      * '{vm-type}' is the {vm-type} associated with the OS::Nova::Server
      * '{network-role}' is the {network-role} of the external network
      * the value for {index} must start at zero (0) and increment by one

.. req::
    :id: R-87123
    :target: VNF
    :keyword: MUST NOT

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'fixed_ips' map property 'ip_address'
    parameter '{vm-type}_{network-role}\_v6\_ip\_{index}'
    **MUST NOT** be enumerated in the VNF's Heat Orchestration
    Template's Environment File.

ONAP's SDN-Controller assigns the IP Address and ONAP provides
the value at orchestration to the Heat Orchestration Template.

*Example External Network IPv6 Address string Parameter Definition*

.. code-block:: yaml

  parameters:

    {vm-type}_{network-role}_v6_ip_{index}:
      type: string
      description: Fixed IPv6 assignment for {vm-type} VM {index} on the {network-role} network


.. req::
    :id: R-23503
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' is attaching to an external network, and an IPv6
    address is assigned using the property 'fixed_ips' map property 'ip_address'
    and the parameter type is defined as a comma_delimited_list, the parameter
    name **MUST** follow the naming convention

      * '{vm-type}_{network-role}_v6_ips'

    where

      * '{vm-type}' is the {vm-type} associated with the OS::Nova::Server
      * '{network-role}' is the {network-role} of the external network

.. req::
    :id: R-93030
    :target: VNF
    :keyword: MUST NOT

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'fixed_ips' map property 'ip_address'
    parameter '{vm-type}_{network-role}_v6_ips' **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

ONAP's SDN-Controller assigns the IP Address and ONAP provides
the value at orchestration to the Heat Orchestration Template.

*Example External Network IPv6 Address comma_delimited_list Parameter
Definition*

.. code-block:: yaml

  parameters:

    {vm-type}_{network-role}_v6_ips:
      type: comma_delimited_list
      description: Fixed IPv6 assignments for {vm-type} VMs on the {network-role} network


.. req::
    :id: R-78380
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' is attaching to an internal network, and an IPv4 address
    is assigned using the property 'fixed_ips' map property 'ip_address' and
    the parameter type is defined as a string, the parameter name **MUST** follow
    the naming convention

       * '{vm-type}\_int\_{network-role}\_ip\_{index}'

    where

       * '{vm-type}' is the {vm-type} associated with the OS::Nova::Server
       * '{network-role}' is the {network-role} of the internal network
       * the value for {index} must start at zero (0) and increment by one

.. req::
    :id: R-28795
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'fixed_ips' map property 'ip_address'
    parameter '{vm-type}\_int\_{network-role}\_ip\_{index}' **MUST** be enumerated
    in the VNF's Heat Orchestration Template's Environment File.

The IP address is local to the VNF's internal network and is (re)used
in every VNF spin up, thus the constant value is declared in the VNF's
Heat Orchestration Template's Environment File.

*Example Internal Network IPv4 Address string Parameter Definition*

.. code-block:: yaml

  parameters:

    {vm-type}_int_{network-role}_ip_{index}:
      type: string
      description: Fixed IPv4 assignment for {vm-type} VM {index} on the int_{network-role} network


.. req::
    :id: R-85235
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' is attaching to an internal network, and an IPv4
    address is assigned using the property 'fixed_ips' map property 'ip_address'
    and the parameter type is defined as a comma_delimited_list, the parameter
    name **MUST** follow the naming convention

       * '{vm-type}\_int\_{network-role}_ips'

    where

       * '{vm-type}' is the {vm-type} associated with the OS::Nova::Server
       * '{network-role}' is the {network-role} of the internal network

.. req::
    :id: R-90206
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'fixed_ips' map property 'ip_address'
    parameter '{vm-type}\_int\_{network-role}_int_ips' **MUST** be enumerated in
    the VNF's Heat Orchestration Template's Environment File.

The IP address is local to the VNF's internal network and is (re)used
in every VNF spin up, thus the constant value is declared in the VNF's
Heat Orchestration Template's Environment File.

.. code-block:: yaml

  parameters:

    {vm-type}_int_{network-role}_ips:
      type: comma_delimited_list
      description: Fixed IPv4 assignments for {vm-type} VMs on the int_{network-role} network


.. req::
    :id: R-27818
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' is attaching to an internal network, and an IPv6 address
    is assigned using the property 'fixed_ips' map property 'ip_address' and
    the parameter type is defined as a string, the parameter name **MUST** follow
    the naming convention

       * '{vm-type}\_int\_{network-role}\_v6\_ip\_{index}'

    where

       * '{vm-type}' is the {vm-type} associated with the OS::Nova::Server
       * '{network-role}' is the {network-role} of the internal network
       * the value for {index} must start at zero (0) and increment by one

.. req::
    :id: R-97201
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'fixed_ips' map property 'ip_address'
    parameter '{vm-type}\_int\_{network-role}\_v6\_ip\_{index}'
    **MUST** be enumerated in the VNF's Heat Orchestration
    Template's Environment File.

The IP address is local to the VNF's internal network and is (re)used
in every VNF spin up, thus the constant value is declared in the VNF's
Heat Orchestration Template's Environment File.

*Example Internal Network IPv6 Address string Parameter Definition*

.. code-block:: yaml

  parameters:

    {vm-type}_int_{network-role}_v6_ip_{index}:
      type: string
      description: Fixed IPv6 assignment for {vm-type} VM {index} on the int_{network-role} network


.. req::
    :id: R-29765
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' is attaching to an internal network, and an IPv6
    address is assigned using the property 'fixed_ips' map property 'ip_address'
    and the parameter type is defined as a comma_delimited_list, the parameter
    name **MUST** follow the naming convention

       * '{vm-type}\_int\_{network-role}_v6_ips'

    where

       * '{vm-type}' is the {vm-type} associated with the OS::Nova::Server
       * '{network-role}' is the {network-role} of the internal network

*Example Internal Network IPv6 Address comma_delimited_list Parameter
Definition*

.. code-block:: yaml

  parameters:

    {vm-type}_int_{network-role}_v6_ips:
      type: comma_delimited_list
      description: Fixed IPv6 assignments for {vm-type} VMs on the int_{network-role} network


.. req::
    :id: R-98569
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'fixed_ips' map property 'ip_address'
    parameter '{vm-type}\_int\_{network-role}_v6_ips' **MUST** be enumerated in
    the VNF's Heat Orchestration Template's Environment File.

The IP address is local to the VNF's internal network and is (re)used
in every VNF spin up, thus the constant value is declared in the VNF's
Heat Orchestration Template's Environment File.


.. req::
    :id: R-62590
    :target: VNF
    :keyword: MUST NOT

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'fixed_ips' map property 'ip_address'
    parameter associated with an external network, i.e.,

    - {vm-type}_{network-role}\_ip\_{index}
    - {vm-type}_{network-role}\_ip\_v6\_{index}
    - {vm-type}_{network-role}_ips
    - {vm-type}_{network-role}_v6_ips

    **MUST NOT** be enumerated in the Heat Orchestration Template's Environment File.
    ONAP provides the IP address assignments at orchestration time.

.. req::
    :id: R-93496
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'fixed_ips' map property 'ip_address'
    parameter associated with an internal network, i.e.,

    - {vm-type}\_int\_{network-role}\_ip\_{index}
    - {vm-type}\_int\_{network-role}\_ip\_v6\_{index}
    - {vm-type}\_int\_{network-role}_ips
    - {vm-type}\_int\_{network-role}_v6_ips

    **MUST** be enumerated in the Heat Orchestration Template's Environment
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

.. code-block:: yaml

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
        fixed_ips: [ { "ip_address": {get_param: [ db_oam_ips, 0 ]}}, {
        "ip_address": {get_param: [ db_oam_v6_ips, 0 ]}}]
    db_1_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips:
          - "ip_address": {get_param: [ db_oam_ips, 1 ]}
          - "ip_address": {get_param: [ db_oam_v6_ips, 1 ]}

*Example: string parameters for IPv4 and IPv6 Address Assignments to an
external network*

In this example, the '{network-role}' has been defined as 'oam' to
represent an oam network and the '{vm-type}' has been defined as 'db' for
database.

.. code-block:: yaml

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
        fixed_ips: [ { "ip_address": {get_param: db_oam_ip_0}}, { "ip_address": {get_param: db_oam_v6_ip_0 ]}}]
    db_1_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips:
          - "ip_address": {get_param: db_oam_ip_1}}]
          - "ip_address": {get_param: db_oam_v6_ip_1}}]


*Example: comma_delimited_list parameters for IPv4 and IPv6 Address
Assignments to an internal network*

In this example, the '{network-role}' has been defined as 'ctrl' to
represent an ctrl network internal to the vnf.
The '{vm-type}' has been defined as 'db' for
database.

.. code-block:: yaml

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
        fixed_ips: [ { "ip_address": {get_param: [ db_int_ctrl_ips, 0 ]}}, {
        "ip_address": {get_param: [ db_int_ctrl_v6_ips, 0 ]}}]
    db_1_int_ctrl_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: int_ctrl_net_id }
        fixed_ips:
        - "ip_address": {get_param: [ db_int_ctrl_ips, 1 ]}
        - "ip_address": {get_param: [ db_int_ctrl_v6_ips, 1 ]}


*Example: string parameters for IPv4 and IPv6 Address Assignments to an
internal network*

In this example, the int\_{network-role} has been defined as
int_ctrl to represent a control network internal to the vnf.
The {vm-type} has been defined as db for database.

.. code-block:: yaml

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
        fixed_ips: [ { "ip_address": {get_param: db_oam_int_ip_0}}, {
        "ip_address": {get_param: db_oam_int_v6_ip_0 ]}}]
    db_1_int_ctrl_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: int_oam_int_net_id }
        fixed_ips:
          - "ip_address": {get_param: db_oam_int_ip_1}}]
          - "ip_address": {get_param: db_oam_int_v6_ip_1}}]


Property: fixed\_ips, Map Property: subnet\_id
++++++++++++++++++++++++++++++++++++++++++++++

The resource 'OS::Neutron::Port' property 'fixed_ips' map
property 'subnet'/'subnet_id' is used when a
port is requesting an IP assignment via
OpenStack's DHCP Service (i.e., Cloud Assigned).

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


.. req::
    :id: R-38236
    :target: VNF
    :keyword: MUST

    The VNF's Heat Orchestration Template's resource
    'OS::Neutron::Port' property 'fixed_ips' map property
    'subnet'/'subnet_id' parameter **MUST** be declared type 'string'.

.. req::
    :id: R-62802
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's resource
    'OS::Neutron::Port' is attaching to an external network, and an IPv4
    address is being Cloud Assigned by OpenStack's DHCP Service and the
    external network IPv4 subnet is to be specified using the property
    'fixed_ips' map property 'subnet'/'subnet_id', the parameter **MUST**
    follow the naming convention

       * '{network-role}_subnet_id'

    where

       * '{network-role}' is the network role of the network.

.. req::
    :id: R-83677
    :target: VNF
    :keyword: MUST NOT

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'fixed_ips' map property
    subnet'/'subnet_id' parameter '{network-role}_subnet_id'
    **MUST NOT** be enumerated in the VNF's Heat Orchestration Template's
    Environment File.

ONAP's SDN-Controller provides the network's subnet's UUID
value at orchestration to the Heat Orchestration Template.

*Example Parameter Definition*

.. code-block:: yaml

  parameters:

    {network-role}_subnet_id:
      type: string
      description: Neutron IPv4 subnet UUID for the {network-role} network


.. req::
    :id: R-15287
    :target: VNF
    :keyword: MUST

    When the VNF's Heat Orchestration Template's resource
    'OS::Neutron::Port' is attaching to an external network, and an IPv6
    address is being Cloud Assigned by OpenStack's DHCP Service and the
    external network IPv6 subnet is to be specified using the property
    'fixed_ips' map property 'subnet'/'subnet_id', the parameter **MUST**
    follow the naming convention

       * '{network-role}_subnet_v6_id'

    where

       * '{network-role}' is the network role of the network.

.. req::
    :id: R-80829
    :target: VNF
    :keyword: MUST NOT

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'fixed_ips' map property
    subnet'/'subnet_id' parameter '{network-role}_subnet_v6_id'
    **MUST NOT** be enumerated in the VNF's Heat Orchestration Template's
    Environment File.

ONAP's SDN-Controller provides the network's subnet's UUID
value at orchestration to the Heat Orchestration Template.

*Example Parameter Definition*

.. code-block:: yaml

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

.. code-block:: yaml

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

.. code-block:: yaml

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


.. req::
    :id: R-84123
    :target: VNF
    :keyword: MUST

    When

    - the VNF's Heat Orchestration Template's resource 'OS::Neutron::Port'
      in an Incremental Module is attaching to an internal network
      that is created in the Base Module, AND
    - an IPv4 address is being Cloud Assigned by OpenStack's DHCP Service AND
    - the internal network IPv4 subnet is to be specified using the
      property 'fixed_ips' map property 'subnet'/'subnet_id',

    the parameter **MUST** follow the naming convention
       * 'int\_{network-role}_subnet_id'
    where
       * '{network-role}' is the network role of the internal network

    - Note that the parameter **MUST** be defined as an 'output' parameter in
      the base module.

.. req::
    :id: R-69634
    :target: VNF
    :keyword: MUST NOT

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'fixed_ips' map property
    subnet'/'subnet_id' parameter 'int\_{network-role}_subnet_id'
    **MUST NOT** be enumerated in the VNF's Heat Orchestration Template's
    Environment File.

The assumption is that internal networks are created in the base module.
The Neutron subnet network ID will be passed as an output parameter
(e.g., ONAP Base Module Output Parameter) to the incremental modules.
In the incremental modules, the output parameter name will be defined as
input parameter.

*Example Parameter Definition*

.. code-block:: yaml

  parameters:

    int_{network-role}_subnet_id:
      type: string
      description: Neutron IPv4 subnet UUID for the int_{network-role} network


.. req::
    :id: R-76160
    :target: VNF
    :keyword: MUST

    When

    - the VNF's Heat Orchestration Template's resource
      'OS::Neutron::Port' in an Incremental Module is attaching to an
      internal network that is created in the Base Module, AND
    - an IPv6 address is being Cloud Assigned by OpenStack's DHCP Service AND
    - the internal network IPv6 subnet is to be specified using the property
      'fixed_ips' map property 'subnet'/'subnet_id',

    the parameter **MUST** follow the naming convention
       * 'int\_{network-role}_v6_subnet_id'
    where
       * '{network-role}' is the network role of the internal network

    - Note that the parameter **MUST** be defined as an 'output' parameter in
      the base module.

.. req::
    :id: R-22288
    :target: VNF
    :keyword: MUST NOT

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'fixed_ips' map property
    'subnet'/'subnet_id' parameter 'int\_{network-role}_v6_subnet_id'
    **MUST NOT** be enumerated in the VNF's Heat Orchestration Template's
    Environment File.

*Example Parameter Definition*

.. code-block:: yaml

  parameters:

    int_{network-role}_v6_subnet_id:
      type: string
      description: Neutron subnet UUID for the int_{network-role} network


Property: allowed\_address\_pairs, Map Property: ip\_address
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The property 'allowed_address_pairs' in the resource 'OS::Neutron::Port'
allows the user to specify a mac_address and/or ip_address that will
pass through a port regardless of subnet. This enables the use of
protocols, such as VRRP, which allow for a Virtual IP (VIP) address
to be shared among two or more ports, with one designated as the master
and the others as backups. In case the master fails,
the Virtual IP address is mapped to a backup's IP address and
the backup becomes the master.

Note that the management of the VIP IP addresses (i.e. transferring
ownership between active and standby VMs) is the responsibility of
the VNF application.


.. req::
    :id: R-62300
    :target: VNF
    :keyword: MUST

    If a VNF has two or more ports that require a Virtual IP Address (VIP),
    a VNF's Heat Orchestration Template's Resource 'OS::Neutron::Port' property
    'allowed_address_pairs' map property 'ip_address' parameter **MUST** be used.

The 'allowed_address_pairs' is an optional property. It is not required.

ONAP automation supports the assignment of VIP addresses
for external networks. ONAP support the assignment of one IPv4 VIP address
and/or one IPv6 VIP address to a set of ports associated with a
'{vm-type}' and '{network-role}'.

If a VNF requires more than one IPv4 VIP address
and/or more than one IPv6 VIP address to a set of ports associated with a
'{vm-type}' and '{network-role}', there are "manual" work-around
procedures that can be utilized.

VIP Assignment, External Networks, Supported by Automation
__________________________________________________________



.. req::
    :id: R-91810
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF requires ONAP to assign a Virtual IP (VIP) Address to
    ports connected an external network, the port
    **MUST NOT** have more than one IPv4 VIP address.

.. req::
    :id: R-41956
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF requires ONAP to assign a Virtual IP (VIP) Address to
    ports connected an external network, the port
    **MUST NOT** have more than one IPv6 VIP address.

.. req::
    :id: R-10754
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF has two or more ports that
    attach to an external network that require a Virtual IP Address (VIP),
    and the VNF requires ONAP automation to assign the IP address,
    all the Virtual Machines using the VIP address **MUST**
    be instantiated in the same Base Module Heat Orchestration Template
    or in the same Incremental Module Heat Orchestration Template.

.. req::
    :id: R-98748
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'allowed_address_pairs'
    map property 'ip_address' parameter
    **MUST** be declared as type 'string'.

.. req::
    :id: R-41492
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    When the VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' is attaching to an external network,
    and an IPv4 Virtual IP (VIP) address is assigned via ONAP automation
    using the property 'allowed_address_pairs' map property 'ip_address' and
    the parameter name **MUST** follow the naming convention

       * '{vm-type}_{network-role}_floating_ip'

    where

       * '{vm-type}' is the {vm-type} associated with the OS::Nova::Server
       * '{network-role}' is the {network-role} of the external network

    And the parameter **MUST** be declared as type 'string'.

.. req::
    :id: R-83412
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'allowed_address_pairs'
    map property 'ip_address' parameter
    '{vm-type}_{network-role}_floating_ip'
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

*Example Parameter Definition*

.. code-block:: yaml

  parameters:

    {vm-type}_{network-role}_floating_ip:
      type: string
      description: IPv4 VIP for {vm-type} VMs on the {network-role} network




.. req::
    :id: R-35735
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    When the VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' is attaching to an external network,
    and an IPv6 Virtual IP (VIP) address is assigned via ONAP automation
    using the property 'allowed_address_pairs' map property 'ip_address',
    the parameter name **MUST** follow the naming convention

       * '{vm-type}_{network-role}_v6_floating_ip'

    where

       * '{vm-type}' is the {vm-type} associated with the OS::Nova::Server
       * '{network-role}' is the {network-role} of the external network

    And the parameter **MUST** be declared as type 'string'.

.. req::
    :id: R-83418
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    The VNF's Heat Orchestration Template's Resource
    'OS::Neutron::Port' property 'allowed_address_pairs'
    map property 'ip_address' parameter
    '{vm-type}_{network-role}_floating_v6_ip'
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

*Example Parameter Definition*

.. code-block:: yaml

  parameters:

    {vm-type}_{network-role}_floating_v6_ip:
      type: string
      description: VIP for {vm-type} VMs on the {network-role} network

Note that these parameters are **not** intended to represent an OpenStack
"Floating IP", for which OpenStack manages a pool of public IP
addresses that are mapped to specific VM ports. In that case, the
individual VMs are not even aware of the public IPs, and all assignment
of public IPs to VMs is via OpenStack commands. ONAP does not support
Neutron-style Floating IPs.  That is, ONAP does not support the
resources 'OS::Neutron::FloatingIP'
and 'OS::Neutron::FloatingIPAssociation'.


.. req::
    :id: R-05257
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's **MUST NOT**
    contain the Resource 'OS::Neutron::FloatingIP'.

.. req::
    :id: R-76449
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's **MUST NOT**
    contain the Resource 'OS::Neutron::FloatingIPAssociation'.

The Floating IP functions as a NAT.  They are allocated within
Openstack, and always "terminate" within the Openstack infrastructure.
When Openstack receives packets on a Floating IP, the packets will
be forwarded to the
Port that has been mapped to the Floating IP, using the private address of the
port.  The VM never sees or knows about the Openstack Floating IP.
The process to use is:

  - User allocates a floating IP from the Openstack pool.
  - User 'attaches' that floating IP to one of the VM ports.

If there is a high-availability VNF that wants to "float" the IP to a
different VM, it requires a Neutron command to request Openstack to 'attach'
the floating IP to a different VM port.
The pool of such addresses is managed by Openstack infrastructure.
Users cannot create new ones, they can only choose from those in the pool.
The pool is typically global (i.e. any user/tenant can grab them).

Allowed address pairs are for more typical Linux-level "virtual IPs".
They are additional IP addresses that are advertised by some port on the VM,
in addition to the primary private IP address.  Typically in a
high-availability VNF, an additional IP is assigned and will float between
VMs (e.g., via some health-check app that will plumb the IP on one or other
VM).  In order for this to work, the actual packets must be addressed to that
IP address (and the allowed_ip_address list will let it pass through
to the VM).  This generally requires provider network access
(i.e. direct access to a data center network for the VMs), such that these
IPs can pass through all of the virtual routers.
Contrail also provides the enhanced networking that allows routing of such
additional IPs.

Floating IPs are not used in ONAP due to the NAT-ting nature of the IPs,
the inability to reserve such IPs for specific use, the need to manage them
via Openstack commands (i.e. a HA VNF would require direct access to
Openstack to 'float' such an IP from one VM to another).

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
    db_0_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips: [ { "ip_address": {get_param: [db_oam_ips,0] }}]
        allowed_address_pairs: [ { "ip_address": {get_param:
        db_oam_floating_ip}}]
    db_1_oam_port_0:
      type: OS::Neutron::Port
        properties:
          network: { get_param: oam_net_id }
          fixed_ips: [ { "ip_address": {get_param: [db_oam_ips,1] }}]
          allowed_address_pairs: [ { "ip_address": {get_param:
          db_oam_floating_ip}}]


VIP Assignment, External Networks, Additional Options
_____________________________________________________

The parameter {'vm-type}_{network-role}_floating_ip' allows for only one
allowed address pair IPv4 address per '{vm-type}' and '{network-role}'
combination.

The parameter '{vm-type}_{network-role}_floating_v6_ip' allows for only one
allowed address pair IPv6 address per '{vm-type}' and '{network-role}'
combination.

If there is a need for multiple allowed address pair IPs for a given
{vm-type} and {network-role} combination within a VNF, there are two
options.

**Option One**

If there is a need for multiple allowed address pair IPs for a given
'{vm-type}' and '{network-role}' combination within a VNF, then the
parameter names defined for the Property 'fixed_ips' Map Property
'ip_address' should be used or the Property 'allowed_address_pairs'
Map Property 'ip_address'. The
parameter names are provided in the table below.

.. csv-table:: **Table 5 OS::Neutron::Port Property allowed_address_pairs map property ip_address Parameter Naming Convention**
   :header: IP Address,Parameter Type,Parameter Name
   :align: center
   :widths: auto

   IPv4, string, {vm-type}_{network-role}_ip_{index}
   IPv4, comma_delimited_list, {vm-type}_{network-role}_ips
   IPv6, string, {vm-type}_{network-role}_v6_ip_{index}
   IPv6, comma_delimited_list, {vm-type}_{network-role}_v6_ips

The examples below illustrate this concept.

*Example: A VNF has four load balancers. Each pair has a unique VIP.*

In this example, there are two administrative VM pairs. Each pair has
one VIP. The {network-role} has been defined as oam to represent an oam
network and the {vm-type} has been defined as admin for an
administrative VM.

Pair 1: Resources admin_0_port_0 and admin_1_port_0 share a unique VIP,
[admin_oam_ips,2]

Pair 2: Resources admin_2_port_0 and admin_3_port_0 share a unique VIP,
[admin_oam_ips,5]

.. code-block:: yaml

  parameters:
    oam_net_id:
      type: string
      description: Neutron UUID for the oam network
    admin_oam_ips:
      type: comma_delimited_list
      description: Fixed IP assignments for admin VMs on the oam network

  resources:
    admin_0_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips: [ { "ip_address": {get_param: [admin_oam_ips,0] }}]
        allowed_address_pairs: [{ "ip_address": {get_param: [admin_oam_ips,2]
        }}]
    admin_1_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips: [ { "ip_address": {get_param: [admin_oam_ips,1] }}]
        allowed_address_pairs: [{ "ip_address": {get_param: [admin_oam_ips,2]
      }}]
    admin_2_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips: [ { "ip_address": {get_param: [admin_oam_ips,3] }}]
        allowed_address_pairs: [{ "ip_address": {get_param: [admin_oam_ips,5]
        }}]
    admin_3_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips: [ { "ip_address": {get_param: [admin_oam_ips,4] }}]
        allowed_address_pairs: [{ "ip_address": {get_param: [admin_oam_ips,5]
        }}]

*Example: A VNF has two load balancers. The pair of load balancers share
two VIPs.*

In this example, there is one load balancer pairs. The pair has two
VIPs. The {network-role} has been defined as oam to represent an oam
network and the {vm-type} has been defined as lb for a load balancer VM.

.. code-block:: yaml

  resources:
    lb_0_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips: [ { "ip_address": {get_param: [lb_oam_ips,0] }}]
        allowed_address_pairs: [{ "ip_address": {get_param: [lb_oam_ips,2] },
        {get_param: [lb_oam_ips,3] }}]
    lb_1_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips: [ { "ip_address": {get_param: [lb_oam_ips,1] }}]
        allowed_address_pairs: [{ "ip_address": {get_param: [lb_oam_ips,2] },
        {get_param: [lb_oam_ips,3] }}]

As a general rule, provide the fixed IPs for the VMs indexed first in
the CDL and then the VIPs as shown in the examples above.

**Option Two**

If there is a need for multiple allowed address pair IPs for a given
'{vm-type}' and '{network-role}' combination within a VNF, then the
parameter names defined for the table below can be used.

**Resource OS::Neutron::Port**

Table 6: Multiple allowed_address_pairs Option 2A

.. csv-table:: **Table 6 OS::Neutron::Port Property allowed_address_pairs map property ip_address Parameter Naming Convention**
   :header: IP Address,Parameter Type,Parameter Name
   :align: center
   :widths: auto

   IPv4, string, {vm-type}_{network-role}_vip_{index}
   IPv4, comma_delimited_list, {vm-type}_{network-role}_vips
   IPv6, string, {vm-type}_{network-role}_v6_vip_{index}
   IPv6, comma_delimited_list, {vm-type}_{network-role}_v6_vips


If there is a need for multiple allowed address pair IPs for a given
'{vm-type}' and '{network-role}' combination within a VNF and the need to
differentiate the VIPs for different traffic types (e.g., 911 VIP,
fail-over VIP), then the parameter names defined for the table below can
be used.

**Resource OS::Neutron::Port**

Table 7: Multiple allowed_address_pairs Option 2B

.. csv-table:: **Table 7 OS::Neutron::Port Property allowed_address_pairs map property ip_address Parameter Naming Convention**
   :header: IP Address,Parameter Type,Parameter Name
   :align: center
   :widths: auto

   IPv4, string, {vm-type}_{network-role}_{vip_type}_vip
   IPv4, comma_delimited_list, {vm-type}_{network-role}_{vip_type}_vips
   IPv6, string, {vm-type}_{network-role}_{vip_type}_v6_vip
   IPv6, comma_delimited_list, {vm-type}_{network-role}_{vip_type}_v6_vips

Internal Networks
_________________

ONAP defines an internal network in relation to
the VNF and not with regard to the Network Cloud site. Internal
networks may also be referred to as "intra-VNF" networks or "private"
networks. An internal network only connects VMs in a single VNF. It
must not connect to other VNFs or an external (to the cloud) gateway or an
external (to the cloud) router.

ONAP internal networks should be created in the base module.

As previously mentioned,
ports that connect to an internal network are assigned IP addresses
via one of two methods

 * Method 1: Cloud assigned by OpenStack's DHCP Service
 * Method 2: Statically assigned.  That is, predetermined by the VNF designer
   and are specified in the VNF's Heat Orchestration Template's
   Environment File

If Cloud assigned IP addressing is being used, output statements
are created in the base module.

If static assigned IP addressing is being used, the  IP addresses
are defined in the environment file.


  * {vm-type}_int_{network-role}_floating_ip
  * {vm-type}_int_{network-role}_floating_v6_ip

  * {vm-type}_int_{network-role}_vip_{index}
  * {vm-type}_int_{network-role}_vips
  * {vm-type}_int_{network-role}_v6_vip_{index}
  * {vm-type}_int_{network-role}_v6_vips


  * {vm-type}_int_{network-role}_{vip_type}_vip
  * {vm-type}_int_{network-role}_{vip_type}_vips
  * {vm-type}_int_{network-role}_{vip_type}_v6_vip
  * {vm-type}_int_{network-role}_{vip_type}_v6_vips



*Example Parameter Definition*

.. code-block:: yaml

  parameters:
    {vm-type}_int_{network-role}_floating_ip:
      type: string
      description: VIP for {vm-type} VMs on the int_{network-role} network

    {vm-type}_int_{network-role}_floating_v6_ip:
      type: string
      description: VIP for {vm-type} VMs on the int_{network-role} network




allowed_address_pair IP Addresses Required in more than one module
__________________________________________________________________

If the IP address {vm-type}_{network-role}_floating_ip and/or
{vm-type}_{network-role}_floating_v6_ip must be used in more than module in the
VNF, the parameter values must be defined as output values in the base
module with output names: {vm-type}_{network-role}_shared_vip or
{vm-type}_{network-role}_v6_shared_vip

.. code-block:: yaml

  outputs:
    {vm-type}_{network-role}_shared_vip:
      description:
      value: { get_param: {vm-type}_{network-role}_floating_ip }

    {vm-type}_{network-role}_v6_shared_vip:
      description:
      value: { get_param: {vm-type}_{network-role}_v6_floating_ip }

The output parameters must be defined as input parameter in the
incremental modules that require the IP addresses. When defining the
allowed_address_pairs: in the OS::Neutron::Port, it should be as
follows:

.. code-block:: yaml

  allowed_address_pairs: [ { "ip_address": {get_param:
  {vm-type}_{network-role}_shared_vip }}, { "ip_address": {get_param:
  {vm-type}_{network-role}_v6_shared_vip }}]

Reserve Port Concept
____________________

A "Reserve Port" is an OS::Neutron::Port that fixed_ips, ip_address
property is assigned one or more IP addresses that are used as Virtual
IP (VIP) Addresses (i.e., allowed_address_pairs) on other ports.

A "Reserve Port" is never attached to a Virtual Machine
(OS::Nova::Server). The reserve port ensures that the intended
allowed_address_pair IP address is not inadvertently assigned as a
fixed_ips to a OS::Neutron::Port that is attached OS::Nova::Server and
thus causing routing issues.

A VNF may have one or more "Reserve Ports". A reserve port maybe created
in the base module or an incremental module. If created in the base
module, parameters may be defined in the outputs: section of the base
template so the IP Address assigned to the reserve port maybe assigned
to the allowed_address_pair property of an OS::Neutron::Port in one or
more incremental modules.

The parameter name of the IP address used in the "Reserve Port" depends
on the allowed_address_pair "option" utilized by the VNF.

When creating a Reserve Port, if only one allowed_address_pair is configured
on a port, then the parameter name depends upon the IP addresses type
(IPv4 or IPv6) and network type (internal or external).
The valid parameter names are:

  * {vm-type}_{network-role}_floating_ip
  * {vm-type}_{network-role}_floating_v6_ip
  * {vm-type}_int_{network-role}_floating_ip
  * {vm-type}_int_{network-role}_floating_v6_ip

When creating a Reserve Port, if more than one (e.g., multiple)
allowed_address_pair is configured on a port, then the parameter name depends
upon the IP addresses type (IPv4 or IPv6) and network type
(internal or external) and the option being used.  The valid parameter
names are:

  * {vm-type}_{network-role}_ip_{index}
  * {vm-type}_{network-role}_ips
  * {vm-type}_{network-role}_v6_ip_{index}
  * {vm-type}_{network-role}_v6_ips
  * {vm-type}_{network-role}_vip_{index}
  * {vm-type}_{network-role}_vips
  * {vm-type}_{network-role}_v6_vip_{index}
  * {vm-type}_{network-role}_v6_vips
  * {vm-type}_{network-role}_{vip-type}_vip
  * {vm-type}_{network-role}_v6_{vip-type}_vip
  * {vm-type}_{network-role}_{vip-type}_vips
  * {vm-type}_{network-role}_v6_{vip-type}_vips

*Example IPv4 Reserve Port Definition: one allowed_address_pair
configured on a port*

.. code-block:: yaml

  Reserve_Port_{vm-type}_{network-role}_floating_ip_{index}:
    type: OS::Neutron::Port
    properties:
      network: { get_param: {network-role}_net_id }
      fixed_ips:
        - ip_address : { get_param: {vm-type}_{network-role}_floating_ip }

*Example IPv6 Reserve Port Definition: one allowed_address_pair
configured on a port*

.. code-block:: yaml

  Reserve_Port_{vm-type}_{network-role}_floating_v6_ip_{index}:
    type: OS::Neutron::Port
    properties:
      network: { get_param: {network-role}_net_id }
      fixed_ips:
        - ip_address : { get_param: {vm-type}_{network-role}_floating_v6_ip }


Resource Property "name"
~~~~~~~~~~~~~~~~~~~~~~~~

The parameter naming convention of the property name for the resource
OS::Nova::Server has been defined in
`Resource:  OS::Nova::Server – Metadata Parameters`_.

This section provides the requirements how the property name for non
OS::Nova::Server resources must be defined when the property is used.
Not all resources require the property name (e.g., it is optional) and
some resources do not support the property.


.. req::
    :id: R-85734
    :target: VNF
    :keyword: MUST

    If a VNF's Heat Orchestration Template contains the property 'name'
    for a non 'OS::Nova::Server' resource, the intrinsic function
    'str_replace' **MUST** be used in conjunction with the ONAP
    supplied metadata parameter 'vnf_name' to generate a unique value.

This prevents the enumeration of a
unique value for the property name in a per instance environment file.


.. req::
    :id: R-99812
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A value for VNF's Heat Orchestration Template's property 'name'
    for a non 'OS::Nova::Server' resource **MUST NOT** be declared
    in the VNF's Heat Orchestration Template's Environment File.

In most cases the use of the metadata value 'vnf_name' is required to create a
unique property name.  If this will not provide a unique value,
additional options include:

 - Using the Heat Orchestration Template pseudo parameter
   'OS::stack_name' in the str_replace construct
 - Resources created in a nested heat file invoked by an
   'OS::Heat::ResourceGroup' can use the 'index' to construct a unique name


.. req::
    :id: R-32408
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF's Heat Orchestration Template property 'name'
    for a non 'OS::Nova::Server' resource uses the intrinsic function
    'str_replace' in conjunction with the ONAP
    supplied metadata parameter 'vnf_name' and does not create
    a unique value, additional data **MUST** be used in the
    'str_replace' to create a unique value, such as 'OS::stack_name'
    and/or the 'OS::Heat::ResourceGroup' 'index'.

*Example: Property 'name' for resource 'OS::Neutron::SecurityGroup'*

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
        rules: [. . . . .]

*Example: Property 'name' for resource 'OS::Cinder::Volume'*

.. code-block:: yaml

  resources:
    dns_volume_0:
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

*Example: Property 'name' for resource 'OS::Cinder::Volume' invoked by a
'OS::Heat::ResourceGroup'*

.. code-block:: yaml

  resources:
    dns_volume_0:
      type: OS::Cinder::Volume
      properties:
        description: Cinder Volume
        name:
          str_replace:
              template: VNF_NAME_STACK_NAME_dns_volume_INDEX
              params:
                  VNF_NAME: { get_param: vnf_name }
                  STACK_NAME: { get_param: 'OS::stack_name' }
                  INDEX: { get_param: index }
  . . . .

Contrail Issue with Values for the Property Name
++++++++++++++++++++++++++++++++++++++++++++++++


.. req::
    :id: R-84517
    :target: VNF
    :keyword: SHOULD
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    The Contrail GUI has a limitation displaying special characters.
    The issue is documented in
    https://bugs.launchpad.net/juniperopenstack/+bug/1590710.
    It is recommended that special **SHOULD** characters be avoided.
    However, if special characters must be used, note that for
    the following resources:

       * Virtual Machine
       * Virtual Network
       * Port
       * Security Group
       * Policies
       * IPAM Creation

    the only special characters supported
    are - \" ! $\ \ ' ( ) = ~ ^ | @ ` { } [ ] > , . _"

ONAP Output Parameter Names
~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP defines three types of Output Parameters as detailed in
`Output Parameters`_.

ONAP Base Module Output Parameters:
+++++++++++++++++++++++++++++++++++

ONAP Base Module Output Parameters do not have an explicit naming
convention.


.. req::
    :id: R-97726
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Base Module Output
    Parameter names **MUST** contain {vm-type} and/or {network-role}
    when appropriate.

ONAP Volume Template Output Parameters:
+++++++++++++++++++++++++++++++++++++++


.. req::
    :id: R-88524
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's Volume Template
    Output Parameter names **MUST** contain {vm-type} when appropriate.

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


.. req::
    :id: R-47874
    :target: VNF
    :keyword: MAY
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF **MAY** have

     * Only an IPv4 OAM Management IP Address
     * Only an IPv6 OAM Management IP Address
     * Both a IPv4 and IPv6 OAM Management IP Addresses

.. req::
    :id: R-18683
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF has one IPv4 OAM Management IP Address and the
    IP Address needs to be inventoried in ONAP's A&AI
    database, an output parameter **MUST** be declared in only one of the
    VNF's Heat Orchestration Templates and the parameter **MUST** be named
    'oam_management_v4_address'.

.. req::
    :id: R-94669
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF has one IPv6 OAM Management IP Address and the
    IP Address needs to be inventoried in ONAP's AAI
    database, an output parameter **MUST** be declared in only one of the
    VNF's Heat Orchestration Templates and the parameter **MUST** be named
    'oam_management_v6_address'.

The OAM Management IP Address maybe assigned either via
  *  ONAP SDN-C
  *  DHCP


.. req::
    :id: R-56287
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If the VNF's OAM Management IP Address is assigned by ONAP SDN-C and
    assigned in the VNF's Heat Orchestration Template's via a heat resource
    'OS::Neutron::Port' property 'fixed_ips' map property
    'ip_adress' parameter (e.g., '{vm-type}_{network-role}_ip_{index}',
    '{vm-type}_{network-role}_v6_ip_{index}')
    and the OAM IP Address is required to be inventoried in ONAP AAI,
    then the parameter **MUST** be echoed in an output statement.

.. code-block:: yaml

   outputs:
       oam_management_v4_address:
         value: {get_param: {vm-type}_{network-role}_ip_{index} }
       oam_management_v6_address:
         value: {get_param: {vm-type}_{network-role}_v6_ip_{index} }

*Example: ONAP SDN-C Assigned IP Address echoed as
oam_management_v4_address*

.. code-block:: yaml

  parameters:
    admin_oam_ip_0:
      type: string
      description: Fixed IPv4 assignment for admin VM 0 on the OAM network
  . . .
  resources:
    admin_0_oam_port_0:
      type: OS::Neutron::Port
      properties:
        name:
          str_replace:
            template: VNF_NAME_admin_oam_port_0
            params:
              VNF_NAME: {get_param: vnf_name}
        network: { get_param: oam_net_id }
        fixed_ips: [{ "ip_address": { get_param: admin_oam_ip_0 }}]
        security_groups: [{ get_param: security_group }]
    admin_server_0:
      type: OS::Nova::Server
      properties:
        name: { get_param: admin_names }
        image: { get_param: admin_image_name }
        flavor: { get_param: admin_flavor_name }
        availability_zone: { get_param: availability_zone_0 }
      networks:
        - port: { get_resource: admin_0_oam_net_port_0 }
      metadata:
        vnf_id: { get_param: vnf_id }
        vf_module_id: { get_param: vf_module_id }
        vnf_name: {get_param: vnf_name }
  outputs:
      oam_management_v4_address:
        value: {get_param: admin_oam_ip_0 }


.. req::
    :id: R-48987
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If the VNF's OAM Management IP Address is Cloud assigned and
    and the OAM IP Address is required to be inventoried in ONAP AAI,
    then the parameter **MUST** be obtained by the resource 'OS::Neutron::Port'
    attribute 'ip_address'.

.. code-block:: yaml

   outputs:
       oam_management_v4_address:
         value: {get_attr: [ {OS::Neutron Port Resource ID}, fixed_ips, 0, ip_address] }

*Example: Cloud Assigned IP Address output as oam_management_v4_address*

.. code-block:: yaml

  parameters:
  . . .
  resources:
    admin_0_oam_port_0:
      type: OS::Neutron::Port
      properties:
        name:
          str_replace:
            template: VNF_NAME_admin_oam_0_port
            params:
              VNF_NAME: {get_param: vnf_name}
        network: { get_param: oam_net_id }
        security_groups: [{ get_param: security_group }]
    admin_server_0:
      type: OS::Nova::Server
      properties:
        name: { get_param: admin_name_0 }
        image: { get_param: admin_image_name }
        flavor: { get_param: admin_flavor_name }
        availability_zone: { get_param: availability_zone_0 }
        networks:
          - port: { get_resource: admin_0_oam_port_0 }
        metadata:
          vnf_id: { get_param: vnf_id }
          vf_module_id: { get_param: vf_module_id }
          vnf_name: {get_param: vnf_name }
  outputs:
    oam_management_v4_address:
      value: {get_attr: [admin_0_oam_port_0, fixed_ips, 0, ip_address] }

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


.. req::
    :id: R-02164
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    When a VNF's Heat Orchestration Template's Contrail resource
    has a property that
    references an external network that requires the network's
    Fully Qualified Domain Name (FQDN), the property parameter

       * **MUST** follow the format '{network-role}_net_fqdn'
       * **MUST** be declared as type 'string'
       * **MUST NOT** be enumerated in the NF's Heat Orchestration Template's
         Environment File

.. req::
    :id: R-73228
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's parameter
    '{network-role}_net_fqdn'
    **MUST** be declared as type 'string'.

.. req::
    :id: R-92193
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A VNF's Heat Orchestration Template's parameter
    '{network-role}_net_fqdn'
    **MUST NOT** be enumerated in the VNF's Heat Orchestration Template's
    Environment File.

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
virtual_network_refs references a contrail network FQDN.

.. code-block:: yaml

  fw_0_oam_vmi_0:
    type: OS::ContrailV2::VirtualMachineInterface
    properties:
      name:
        str_replace:
          template: VM_NAME_virtual_machine_interface_1
          params:
            VM_NAME: { get_param: fw_name_0 }
      virtual_machine_interface_properties:
        virtual_machine_interface_properties_service_interface_type: {
        get_param: oam_protected_interface_type }
      virtual_network_refs:
        - get_param: oam_net_fqdn
      security_group_refs:
        - get_param: fw_sec_grp_id


Interface Route Table Prefixes for Contrail InterfaceRoute Table
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


.. req::
    :id: R-28222
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF's Heat Orchestration Template
    'OS::ContrailV2::InterfaceRouteTable' resource
    'interface_route_table_routes' property
    'interface_route_table_routes_route' map property parameter name
    **MUST** follow the format

       * {vm-type}_{network-role}_route_prefixes

.. req::
    :id: R-19756
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF's Heat Orchestration Template
    'OS::ContrailV2::InterfaceRouteTable' resource
    'interface_route_table_routes' property
    'interface_route_table_routes_route' map property parameter
    '{vm-type}_{network-role}_route_prefixes'
    **MUST** be defined as type 'json'.

.. req::
    :id: R-76682
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF's Heat Orchestration Template
    'OS::ContrailV2::InterfaceRouteTable' resource
    'interface_route_table_routes' property
    'interface_route_table_routes_route' map property parameter
    '{vm-type}_{network-role}_route_prefixes'
    **MUST NOT** be enumerated in the VNF's Heat Orchestration Template's
    Environment File.

The parameter '{vm-type}_{network-role}_route_prefixes'
supports IP addresses in the format:

1. Host IP Address (e.g., 10.10.10.10)

2. CIDR Notation format (e.g., 10.0.0.0/28)


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
    fw_oam_route_prefixes:
      type: json
      description: prefix for the ServiceInstance InterfaceRouteTable
    int_fw_dns_trusted_interface_type:
      type: string
      description: service_interface_type for ServiceInstance

  resources:
    <resource name>:
      type: OS::ContrailV2::InterfaceRouteTable
      depends_on: [resource name of OS::ContrailV2::ServiceInstance]
      properties:
        name:
          str_replace:
            template: VNF_NAME_interface_route_table
            params:
              VNF_NAME: { get_param: vnf_name }
        interface_route_table_routes:
          interface_route_table_routes_route: { get_param: fw_oam_route_prefixes }
        service_instance_refs:
          - get_resource: <resource name of OS::ContrailV2::ServiceInstance>
        service_instance_refs_data:
          - service_instance_refs_data_interface_type: { get_param: oam_interface_type }

Resource OS::ContrailV2::InstanceIp
+++++++++++++++++++++++++++++++++++

The Contrail resource OS::ContrailV2::InstanceIp has two properties
that parameters **MUST** follow an explicit naming convention.  The
properties are 'instance_ip_address' and 'subnet_uuid'.

*Example OS::ContrailV2::InstanceIp Resource*

.. code-block:: yaml

  <resource ID>:
    type: OS::ContrailV2::InstanceIp
    properties:
      name: { get_param: name }
      fq_name: { get_param: fq_name }
      display_name: { get_param: display_name }
      secondary_ip_tracking_ip:
        {
          secondary_ip_tracking_ip_ip_prefix: { get_param: secondary_ip_tracking_ip_ip_prefix },
          secondary_ip_tracking_ip_ip_prefix_len: { get_param: secondary_ip_tracking_ip_ip_prefix_len },
        }
      instance_ip_address: { get_param: instance_ip_address }
      instance_ip_mode: { get_param: instance_ip_mode }
      subnet_uuid: { get_param: subnet_uuid }
      instance_ip_family: { get_param: instance_ip_family }
      annotations:
        {
          annotations_key_value_pair:
            [{
              annotations_key_value_pair_key: { get_param: annotations_key_value_pair_key },
              annotations_key_value_pair_value: { get_param: annotations_key_value_pair_value },
            }],
        }
      instance_ip_local_ip: { get_param: instance_ip_local_ip }
      instance_ip_secondary: { get_param: instance_ip_secondary }
      physical_router_refs: [{ get_param: physical_router_refs }]
      virtual_machine_interface_refs: [{ get_param: virtual_machine_interface_refs }]
      virtual_network_refs: [{ get_param: virtual_network_refs }]

Resource OS::ContrailV2::InstanceIp Property instance_ip_address
________________________________________________________________

A VNF's Heat Orchestration Templates resource 'OS::ContrailV2::InstanceIp'
property 'instance_ip_address' parameter
**MUST** follow the same requirements
that apply to the resource 'OS::Neutron' property 'fixed_ips' map
property 'ip_address' parameter.

*Example: Contrail Resource OS::ContrailV2::InstanceIp, Property
instance_ip_address*

The property instance_ip_address uses the same parameter naming
convention as the property fixed_ips and Map Property ip_address in
OS::Neutron::Port. The resource is assigning an ONAP SDN-C Assigned IP
Address. The {network-role} has been defined as oam_protected to
represent an oam protected network and the {vm-type} has been defined as
fw for firewall.

.. code-block:: yaml

  fw_0_oam_protected_vmi_0_IP_0:
    type: OS::ContrailV2::InstanceIp
    depends_on:
      - fw_0_oam_protected_vmi_0
    properties:
      virtual_machine_interface_refs:
        - get_resource: fw_0_oam_protected_vmi_0
      virtual_network_refs:
        - get_param: oam_protected_net_fqdn
      instance_ip_address: { get_param: [fw_oam_protected_ips, get_param: index ] }

Resource OS::ContrailV2::InstanceIp Property subnet_uuid
________________________________________________________________

A VNF's Heat Orchestration Templates resource 'OS::ContrailV2::InstanceIp'
property 'subnet_uuid' parameter
**MUST** follow the same requirements
that apply to the resource 'OS::Neutron' property 'fixed_ips' map
property 'subnet'/'subnet_id' parameter.

*Example: Contrail Resource OS::ContrailV2::InstanceIp, Property
subnet_uuid*

The property instance_ip_address uses the same parameter naming
convention as the property fixed_ips and Map Property subnet_id in
OS::Neutron::Port. The resource is assigning a Cloud Assigned IP
Address. The {network-role} has been defined as "oam_protected" to
represent an oam protected network and the {vm-type} has been defined as
"fw" for firewall.

.. code-block:: yaml

  fw_0_oam_protected_vmi_0_IP_0:
    type: OS::ContrailV2::InstanceIp
    depends_on:
    - fw_0_oam_protected_vmi_0
    properties:
      virtual_machine_interface_refs:
        - get_resource: fw_0_oam_protected_vmi_0
      virtual_network_refs:
        - get_param: oam_protected_net_fqdn
      subnet_uuid: { get_param: oam_protected_subnet_id }

OS::ContrailV2::VirtualMachineInterface Property virtual_machine_interface_allowed_address_pairs
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


A VNF's Heat Orchestration Templates resource
'OS::ContrailV2::VirtualMachineInterface' map property,
virtual_machine_interface_allowed_address_pairs,
virtual_machine_interface_allowed_address_pairs_allowed_address_pair,
virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip,
virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix
parameter **MUST** follow the same requirements that apply to the
resource 'OS::Neutron::Port' property
'allowed_address_pairs', map property 'ip_address' parameter.

*Example OS::ContrailV2::VirtualMachineInterface*

.. code-block:: yaml

  <resource ID>:
    type: OS::ContrailV2::VirtualMachineInterface
    properties:
      name: { get_param: name }
      fq_name: { get_param: fq_name }
      ecmp_hashing_include_fields:
        {
          ecmp_hashing_include_fields_hashing_configured: { get_param: ecmp_hashing_include_fields_hashing_configured },
          ecmp_hashing_include_fields_source_ip: { get_param: ecmp_hashing_include_fields_source_ip },
          ecmp_hashing_include_fields_destination_ip: { get_param: ecmp_hashing_include_fields_destination_ip },
          ecmp_hashing_include_fields_ip_protocol: { get_param: ecmp_hashing_include_fields_ip_protocol },
          ecmp_hashing_include_fields_source_port: { get_param: ecmp_hashing_include_fields_source_port },
          ecmp_hashing_include_fields_destination_port: { get_param: ecmp_hashing_include_fields_destination_port },
        }
      virtual_machine_interface_host_routes:
        {
          virtual_machine_interface_host_routes_route:
            [{
              virtual_machine_interface_host_routes_route_prefix: { get_param: virtual_machine_interface_host_routes_route_prefix },
              virtual_machine_interface_host_routes_route_next_hop: { get_param: virtual_machine_interface_host_routes_route_next_hop },
              virtual_machine_interface_host_routes_route_next_hop_type: { get_param: virtual_machine_interface_host_routes_route_next_hop_type },
              virtual_machine_interface_host_routes_route_community_attributes:
                {
                  virtual_machine_interface_host_routes_route_community_attributes_community_attribute: [{ get_param: virtual_machine_interface_host_routes_route_community_attributes_community_attribute }],
                },
            }],
        }
      virtual_machine_interface_mac_addresses:
        {
          virtual_machine_interface_mac_addresses_mac_address: [{ get_param: virtual_machine_interface_mac_addresses_mac_address }],
        }
      virtual_machine_interface_dhcp_option_list:
        {
          virtual_machine_interface_dhcp_option_list_dhcp_option:
            [{
              virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_name: { get_param: virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_name },
              virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_value: { get_param: virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_value },
              virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_value_bytes: { get_param: virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_value_bytes },
            }],
        }
      virtual_machine_interface_bindings:
        {
          virtual_machine_interface_bindings_key_value_pair:
            [{
              virtual_machine_interface_bindings_key_value_pair_key: { get_param: virtual_machine_interface_bindings_key_value_pair_key },
              virtual_machine_interface_bindings_key_value_pair_value: { get_param: virtual_machine_interface_bindings_key_value_pair_value },
            }],
        }
      virtual_machine_interface_disable_policy: { get_param: virtual_machine_interface_disable_policy }
      virtual_machine_interface_allowed_address_pairs:
        {
          virtual_machine_interface_allowed_address_pairs_allowed_address_pair:
            [{
              virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip:
                {
                  virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix: { get_param: virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix },
                  virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix_len: { get_param: virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix_len },
                },
              virtual_machine_interface_allowed_address_pairs_allowed_address_pair_mac: { get_param: virtual_machine_interface_allowed_address_pairs_allowed_address_pair_mac },
              virtual_machine_interface_allowed_address_pairs_allowed_address_pair_address_mode: { get_param: virtual_machine_interface_allowed_address_pairs_allowed_address_pair_address_mode },
            }],
        }
      annotations:
        {
          annotations_key_value_pair:
            [{
              annotations_key_value_pair_key: { get_param: annotations_key_value_pair_key },
              annotations_key_value_pair_value: { get_param: annotations_key_value_pair_value },
            }],
        }
      virtual_machine_interface_fat_flow_protocols:
        {
          virtual_machine_interface_fat_flow_protocols_fat_flow_protocol:
            [{
              virtual_machine_interface_fat_flow_protocols_fat_flow_protocol_protocol: { get_param: virtual_machine_interface_fat_flow_protocols_fat_flow_protocol_protocol },
              virtual_machine_interface_fat_flow_protocols_fat_flow_protocol_port: { get_param: virtual_machine_interface_fat_flow_protocols_fat_flow_protocol_port },
            }],
        }
      virtual_machine_interface_device_owner: { get_param: virtual_machine_interface_device_owner }
      port_security_enabled: { get_param: port_security_enabled }
      virtual_machine_interface_properties:
        {
          virtual_machine_interface_properties_service_interface_type: { get_param: virtual_machine_interface_properties_service_interface_type },
          virtual_machine_interface_properties_interface_mirror:
            {
              virtual_machine_interface_properties_interface_mirror_traffic_direction: { get_param: virtual_machine_interface_properties_interface_mirror_traffic_direction },
              virtual_machine_interface_properties_interface_mirror_mirror_to:
                {
                  virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_name: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_name },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_encapsulation: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_encapsulation },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_ip_address: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_ip_address },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_mac_address: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_mac_address },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_routing_instance: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_routing_instance },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_udp_port: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_udp_port },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_juniper_header: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_juniper_header },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_nh_mode: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_nh_mode },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header:
                    {
                      virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header_vtep_dst_ip_address: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header_vtep_dst_ip_address },
                      virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header_vtep_dst_mac_address: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header_vtep_dst_mac_address },
                      virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header_vni: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header_vni },
                    },
                },
            },
          virtual_machine_interface_properties_local_preference: { get_param: virtual_machine_interface_properties_local_preference },
          virtual_machine_interface_properties_sub_interface_vlan_tag: { get_param: virtual_machine_interface_properties_sub_interface_vlan_tag },
        }
      display_name: { get_param: display_name }
      service_health_check_refs: [{ get_param: service_health_check_refs }]
      routing_instance_refs: [{ get_param: routing_instance_refs }]
      routing_instance_refs_data:
        [{
          routing_instance_refs_data_direction: { get_param: routing_instance_refs_data_direction },
          routing_instance_refs_data_vlan_tag: { get_param: routing_instance_refs_data_vlan_tag },
          routing_instance_refs_data_src_mac: { get_param: routing_instance_refs_data_src_mac },
          routing_instance_refs_data_dst_mac: { get_param: routing_instance_refs_data_dst_mac },
          routing_instance_refs_data_mpls_label: { get_param: routing_instance_refs_data_mpls_label },
          routing_instance_refs_data_service_chain_address: { get_param: routing_instance_refs_data_service_chain_address },
          routing_instance_refs_data_ipv6_service_chain_address: { get_param: routing_instance_refs_data_ipv6_service_chain_address },
          routing_instance_refs_data_protocol: { get_param: routing_instance_refs_data_protocol },
        }]
      security_group_refs: [{ get_param: security_group_refs }]
      physical_interface_refs: [{ get_param: physical_interface_refs }]
      port_tuple_refs: [{ get_param: port_tuple_refs }]
      interface_route_table_refs: [{ get_param: interface_route_table_refs }]
      virtual_machine_interface_refs: [{ get_param: virtual_machine_interface_refs }]
      virtual_network_refs: [{ get_param: virtual_network_refs }]
      virtual_machine_refs: [{ get_param: virtual_machine_refs }]
      qos_config_refs: [{ get_param: qos_config_refs }]
      virtual_machine: { get_param: virtual_machine }
      project: { get_param: project }



Suggested Naming Convention for Common Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many VNFs use the parameters in the table below are used in user_data.
The table below provides a suggested naming convention for these common
parameters.

Netmask
+++++++

.. csv-table:: **Table 8: Suggested Naming Convention for Common Parameters:  Netmask**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   {network-role}_subnet_<index>_netmask, string,
   int_<network-role>_subnet_<index>_netmask, string,
   {network-role}_v6_subnet_<index>_netmask , string,
   int_{network-role}_v6_subnet_<index>_netmask, string,

CIDR
++++

.. csv-table:: **Table 9: Suggested Naming Convention for Common Parameters:  CIDR**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   <network-role>_subnet_<index>_cidr, string,
   int_<network-role>_subnet_<index>_cidr, string,
   <network-role>_v6_subnet_<index>_cidr, string,
   int_<network-role>_v6_subnet_<index>_cidr, string,

Default Gateway
+++++++++++++++

.. csv-table:: **Table 10: Suggested Naming Convention for Common Parameters:  Default Gateway**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   {network-role}_subnet_<index>_default_gateway, string,
   {network-role}_v6_subnet_<index>_default_gateway, string,

DCAE Collector IP Address
+++++++++++++++++++++++++

.. csv-table:: **Table 11: Suggested Naming Convention for Common Parameters:  DCAE Collector Address**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   dcae_collector_ip_<index>, string,
   dcae_collector_v6_ip_<index>, string,

NTP Server IP Address
+++++++++++++++++++++

.. csv-table:: **Table 12: Suggested Naming Convention for Common Parameters:  NTP Server IP Address**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   ntp_ip_<index>, string,
   ntp_v6_ip_<index>, string,

DNS
++++++++

.. csv-table:: **Table 13: Suggested Naming Convention for Common Parameters:  DCAE Collector Address**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   dns_{network-role}_ip_<index>, string,
   dns_{network-role}_v6_ip_<index>, string,

Security Group
++++++++++++++

.. csv-table:: **Table 14: Suggested Naming Convention for Common Parameters:  Security Group**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   {vm-type}_security_group, string, Security Group applicable to one {vm-type} and more than one network (internal and/or external)
   {network-role}_security_group, string, Security Group applicable to more than one {vm-type} and one external network
   int_{network-role}_security_group, string, Security Group applicable to more than one {vm-type} and one internal network
   {vm-type}_{network-role}_security_group, string, Security Group applicable to one {vm-type} and one external network
   {vm-type}_int_{network-role}_security_group, string, Security Group applicable to one {vm-type} and one internal network
   shared_security_group, string, Security Group applicable to more than one {vm-type} and more than one network (internal and/or external)

ONAP VNF Modularity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP supports a modular Heat Orchestration Template design pattern,
referred to as *VNF Modularity.* With this approach, a single VNF **MAY** be
composed from one or more Heat Orchestration Templates, each of which
represents a subset of the overall VNF. These component parts are
referred to as *VNF Modules*. During orchestration, these modules
are deployed incrementally to create the complete VNF.

As stated in R-33132, a VNF's Heat Orchestration Template **MAY** be
     1.) Base Module Heat Orchestration Template (also referred to as a
      Base Module),
     2.) Incremental Module Heat Orchestration Template (referred to as
      an Incremental Module), or
     3.) a Cinder Volume Module Heat Orchestration Template (referred to as
      Cinder Volume  Module).

As stated in R-20974, at orchestration time, the VNF's Base Module **MUST**
be deployed first, prior to any incremental modules.

As stated in R-28980, R-86926, and R-91497, a
VNF's incremental module **MAY** be used for

  * initial VNF deployment only
  * scale out only
  * both deployment and scale out

As stated in R-68122, a VNF's incremental module **MAY** be deployed
more than once, either during initial VNF deployment and/or scale out

As stated in R-37028 and R-13196, a VNF **MUST** be composed
of one Base Module and *MAY** be composed of zero to many Incremental
Modules.

ONAP also supports the concept of an optional, independently deployed
Cinder volume via a separate Heat Orchestration Templates, referred to
as a Cinder Volume Module. This allows the volume to persist after a VM
(i.e., OS::Nova::Server) is deleted, allowing the volume to be reused on
another instance (e.g., during a fail over activity).

The scope of a Cinder volume module, when it exists, must be 1:1 with a
Base module or Incremental Module.

A VNF module (base, incremental, cinder) **MAY** support nested templates.

A shared Heat Resource is a resource that **MAY** be used by
other Heat Resources either in the Base Module or an
Incremental Module.



.. req::
    :id: R-61001
    :target: VNF
    :keyword: MUST

    A shared Heat Orchestration Template resource must be defined
    in the base module. A shared resource is a resource that that will
    be referenced by another resource that is defined in the Base Module
    and/or one or more incremental modules. When the shared resource needs
    to be referenced by a resource in an incremental module, the UUID of
    the shared resource **MUST** be exposed by declaring an ONAP Base
    Module Output Parameter.

When the shared resource needs to be referenced by a resource in an
incremental module, the UUID of the shared resource must be exposed by
declaring an ONAP Base Module Output Parameter.

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~

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


Cinder Volumes
^^^^^^^^^^^^^^^^^^^^^^^^

Cinder Volumes are created with the heat resource OS::Cinder::Volume.

As stated in R-46119, R-90748, R-03251, a VNF's Heat Orchestration
Template's Resource OS::Heat::CinderVolume **MAY** be defined in a
Base Module, Incremental Module, or Cinder Volume Module.

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

As stated in R-11200, a VNF's Cinder Volume Module, when it exists,
**MUST** be 1:1 with a Base module or Incremental module.  That is,
A single volume module must create only the volumes required by a
single Incremental module or Base module.

As stated in R-30395, a VNF's Cinder Volume Module **MAY** utilize
nested heat.

As stated in R-89913, a VNF's Heat Orchestration Template's Cinder Volume
Module Output Parameter(s) **MUST** include the
UUID(s) of the Cinder Volumes created in template,
while others **MAY** be included.

As stated in R-07443, a VNF's Heat Orchestration Templates' Cinder Volume
Module Output Parameter's name and type **MUST** match the input parameter
name and type in the corresponding Base Module or Incremental Module unless
the Output Parameter is of the type 'comma_delimited_list',
then the corresponding input parameter **MUST** be declared as type 'json'.

A single volume module must create only the volumes
required by a single Incremental module or Base module.

The following rules apply to independent volume Heat templates:


.. req::
    :id: R-79531
    :target: VNF
    :keyword: MUST

    The VNF Heat Orchestration Template **MUST** define
    "outputs" in the volume template for each Cinder volume
    resource universally unique identifier (UUID) (i.e. ONAP
    Volume Template Output Parameters).

-  The VNF Incremental Module or Base Module must define input
   parameters that match each Volume output parameter (i.e., ONAP Volume
   Template Output Parameters).

   -  ONAP will supply the volume template outputs automatically to the
      bases/incremental template input parameters.

-  Volume modules may utilize nested Heat templates.

Optional Property availability_zone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. req::
    :id: R-25190
    :target: VNF
    :keyword: SHOULD NOT

    A VNF's Heat Orchestration Template's Resource 'OS::Cinder::Volume'
    **SHOULD NOT** declare the property 'availability_zone'.

If the property is used, the value **MUST**
be enumerated in the environment file and must be set to nova', which
is the default. There are no requirements on the parameter naming
convention with the exception that the naming convention **MUST NOT** be the
same as the 'OS::Nova::Server' property 'availability_zone' (i.e.,
'availability_zone_{index}').

Optional Property volume_type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenStack supports multiple volume types. If the OS::Cinder::Volume optional
property volume_type is not specified, the OpenStack default volume type is
used. If a specific volume type is required, the property is used and
the value **MUST** be enumerated in the environment file. There are no
requirements on the parameter naming convention

Cinder Volume Examples
~~~~~~~~~~~~~~~~~~~~~~~~~

*Examples: Volume Template*

A VNF has a Cinder volume module, named incremental\_volume.yaml, that
creates an independent Cinder volume for a VM in the module
incremental.yaml. The incremental\_volume.yaml defines a parameter in
the output section, lb\_volume\_id\_0 which is the UUID of the cinder
volume. lb\_volume\_id\_0 is defined as a parameter in incremental.yaml.
ONAP captures the UUID value of lb\_volume\_id\_0 from the volume module
output statement and provides the value to the incremental module.

Note that the example below is not a complete Heat Orchestration
Template. The {vm-type} has been defined as "lb" for load balancer

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

The use of an environment file in OpenStack is optional.  In ONAP, it is
mandatory. A Heat Orchestration Template uploaded to ONAP must have a
corresponding environment file, even if no parameters are required to
be enumerated.

(Note that ONAP does not programmatically enforce the use of
an environment file.)


.. req::
    :id: R-67205
    :target: VNF
    :keyword: MUST

    The VNF Heat Orchestration Template **MUST** have a corresponding
    environment file for a Base Module.

.. req::
    :id: R-35727
    :target: VNF
    :keyword: MUST

    The VNF Heat Orchestration Template **MUST** have a
    corresponding environment file for an Incremental module.

.. req::
    :id: R-22656
    :target: VNF
    :keyword: MUST

    The VNF Heat Orchestration Template **MUST** have a
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

SDC generates a new environment file for distribution to SO based on
the uploaded environment file and the user provided GUI updates. The
user uploaded environment file is discarded when the new file is
created. Note that if the user did not change any values via GUI
updates, the SDC generated environment file will contain the same values
as the uploaded file.

Use of Environment Files when using OpenStack "heat stack-create" CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When ONAP is instantiating the Heat Orchestration Template, certain
parameter must not be enumerated in the environment file. This document
provides the details of what parameters should not be enumerated.

If the Heat Orchestration Template is to be instantiated from the
OpenStack Command Line Interface (CLI) using the command "heat
stack-create", all parameters must be enumerated in the environment
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


.. req::
    :id: R-00228
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template **MAY**
    reference the nested heat statically by repeated definition.

.. req::
    :id: R-01101
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template **MAY**
    reference the nested heat dynamically using the resource
    'OS::Heat::ResourceGroup'.

.. req::
    :id: R-60011
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template **MUST** have no more than
    two levels of nesting.

As stated in R-67231 a VNF's Heat Orchestration template's
Environment File's **MUST NOT** contain the "resource_registry:" section.

Two levels of nesting is defined as follows:  A base module, incremental
module, or cinder volume module references a nested heat file either
statically or by using the resource 'OS::Heat::ResourceGroup'.
This file is the first level of nesting.
If first level file then references a nested file, that file is
the second level of nesting.


.. req::
    :id: R-89868
    :target: VNF
    :keyword: MUST

    The VNF Heat Orchestration Template **MUST** have unique
    file names within the scope of the VNF for a nested heat yaml file.

.. req::
    :id: R-52530
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's Nested YAML file
    **MUST** be in the same directory hierarchy as the VNF's Heat
    Orchestration Templates.

.. req::
    :id: R-90022
    :target: VNF
    :keyword: MAY

    A VNF's Nested YAML file **MAY** be invoked more than
    once by a VNF's Heat Orchestration Template.

.. req::
    :id: R-04344
    :target: VNF
    :keyword: MAY

    A VNF's Nested YAML file **MAY** be invoked by more than one of
    a VNF's Heat Orchestration Templates (when the VNF is composed of two
    or more Heat Orchestration Templates).

.. req::
    :id: R-11041
    :target: VNF
    :keyword: MUST

    All parameters defined in a VNFs Nested YAML file
    **MUST** be passed in as properties of the resource calling
    the nested yaml file.

Note that:

-  As stated in requirement R-00011, a VNF's Heat Orchestration
   Template's Nested YAML file's parameter's **MUST NOT** have
   a parameter constraint defined.

-  As stated in Requirement R-44491, if a VNF's Heat Orchestration
   Template's OS::Nova::Server Resource metadata map value parameter
   'vnf\_id' is passed into a Nested YAML
   file, the parameter name 'vnf\_id' **MUST NOT** change.

-  As stated in Requirement R-86237, if a VNF's Heat Orchestration
   Template's OS::Nova::Server Resource metadata map value parameter
   'vf\_module\_id' is passed into a Nested YAML
   file, the parameter name 'vf\_module\_id' **MUST NOT** change.

-  As stated in Requirement R-16576, if a VNF's Heat Orchestration
   Template's OS::Nova::Server Resource metadata map value parameter
   'vnf\_name' is passed into a Nested YAML
   file, the parameter name 'vnf\_name' **MUST NOT** change.

-  As stated in Requirement R-49177, if a VNF's Heat Orchestration
   Template's OS::Nova::Server Resource metadata map value parameter
   'vf\_module\_name' is passed into a Nested YAML
   file, the parameter name 'vf\_module\_name' **MUST NOT** change.

-  As stated in Requirement R-70757, if a VNF's Heat Orchestration
   Template's OS::Nova::Server Resource metadata map value parameter
   'vm\_role' is passed into a Nested YAML
   file, the parameter name 'vm\_role' **MUST NOT** change.

-  As stated in Requirement R-22441, if a VNF's Heat Orchestration
   Template's OS::Nova::Server Resource metadata map value parameter
   'vf\_module\_index' is passed into a Nested YAML
   file, the parameter name 'vf\_module\_index' **MUST NOT** change.

-  As stated in Requirement R-75202, if a VNF's Heat Orchestration
   Template's OS::Nova::Server Resource metadata map value parameter
   'workload\_context' is passed into a Nested YAML
   file, the parameter name 'workload\_context' **MUST NOT** change.

-  As stated in Requirement R-62954, if a VNF's Heat Orchestration
   Template's OS::Nova::Server Resource metadata map value parameter
   'environment\_context' is passed into a Nested YAML
   file, the parameter name 'environment\_context' **MUST NOT** change.

-  With nested templates, outputs are required to expose any resource
   properties of the child templates to the parent template. Those would
   not explicitly be declared as parameters but simply referenced as
   get\_attribute targets against the "parent" resource.

-  A parameter declared in the outputs: section of a nested template can
   be accessed from the parent template as an attribute (i.e., via
   get\_attr) of the "pseudo resource" whose type is in the nested
   template. In the case of a OS::Heat::ResourceGroup, an output will be
   an attribute of the OS::Heat::ResourceGroup itself, and will be an
   array from the perspective of the parent template.

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

OS::Heat::ResourceGroup may be used to simplify the structure of a Heat
template that creates multiple instances of the same VM type.

However, there are important caveats to be aware of:

OS::Heat::ResourceGroup does not deal with structured parameters
(comma-delimited-list and json) as one might typically expect. In
particular, when using a list-based parameter, where each list element
corresponds to one instance of the ResourceGroup, it is not possible to
use the intrinsic "loop variable" %index% in the OS::Heat::ResourceGroup
definition.

For instance, the following is **not** valid Heat for
OS::Heat::ResourceGroup:

.. code-block:: yaml

 type: OS::Heat::ResourceGroup
   resource_def:
     type: my_nested_vm_template.yaml
     properties:
       name: {get_param: [vm_name_list, %index%]}

Although this appears to use the nth entry of the vm_name_list list for
the nth element of the OS::Heat::ResourceGroup, it will in fact result
in a Heat exception. When parameters are provided as a list (one for
each element of a OS::Heat::ResourceGroup), you must pass the complete
parameter to the nested template along with the current index as
separate parameters.

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

OS::Heat::ResourceGroup Property count
________________________________________


.. req::
    :id: R-50011
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's 'OS::Heat::ResourceGroup'
    property 'count' **MUST** be enumerated in the VNF's
    Heat Orchestration Template's Environment File and **MUST** be
    assigned a value.

This is required for ONAP to build the TOSCA model for the VNF.

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
has been an "issue" with a few VNFs since ONAP only supports
availability\_zone as a string parameter and not a
comma\_delimited\_list. This makes it difficult to use a
OS::Heat::ResourceGroup to create Virtual Machines in more
than one availability zone.

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

**Option 2:** Create a CDL by passing the availability zone parameter
into a nested heat template. An example is provided below.

base.yaml

.. code-block:: yaml

  availability_zone_list:
     type: az_list_generate.yaml
     properties:
       availability_zone_0: { get_param: availability_zone_0 }
       availability_zone_1: { get_param: availability_zone_1 }

    create_virtual_machines:
      type: OS::Heat::ResourceGroup
      properties:
        count: { get_param: count }
        index_var: $INDEX
        resource_def:
          type: nest_file.yaml
          properties:
            index: $INDEX
            availability_zone_0 : { get_attr: [availability_zone_list, general_zones ] }
            . . .

az_list_generate.yaml

.. code-block:: yaml

  parameters:
    availability_zone_0:
      type: string
      description: availability zone 0

    availability_zone_1:
      type: string
      description: availability zone 1

  outputs:

    general_zones:
      value: [
        { get_param: availability_zone_0 },
        { get_param: availability_zone_1 },
        { get_param: availability_zone_0 },
        { get_param: availability_zone_1 },
        { get_param: availability_zone_0 },
        { get_param: availability_zone_1 },
  ]


Nested Heat Template Example: OS::Heat::ResourceGroup
_________________________________________________________

In this example, ocgapp\_volume.yml creates volumes using a
OS::Heat::ResourceGroup that uses nested heat by calling
ocgapp_nested_volume.yml. ocgapp\_volume.yml has an outputs: parameter
ocgapp\_volume\_ids which is declared a input parameter of type: json in
ocgapp\_volume.yml.


This is an example of requirement R-07443, where
a VNF's Heat Orchestration Templates' Cinder Volume Module Output
Parameter's name and type **MUST** match the input parameter name and type
in the corresponding Base Module or Incremental Module unless the Output
Parameter is of the type 'comma\_delimited\_list', then the corresponding
input parameter **MUST** be declared as type 'json'.

ocgapp\_volume.yml

.. code-block:: yaml

  heat_template_version: 2014-10-16

  description: Template for the volumes

  parameters:
    vnf_name:
      type: string
      label: OCG VNF Name
      description: OCG VNF Name
    ocgapp_volume_size_0:
      type: number
      label: Cinder volume 1 size
      description: the size of the Cinder volume
      constraints:
      - range: { min: 100, max: 400 }
    ocgapp_volume_type_0:
      type: string
      label: app vm 1 volume type
      description: the name of the target volume backend for the first OCG APP
    volume_count:
      type: number
      label: volume count
      description: number of volumes needed

  resources:
    ocgapp_volume_resource_group:
      type: OS::Heat::ResourceGroup
      properties:
        count: {get_param: volume_count}
        index_var: index
        resource_def:
          type: ocgapp_nested_volume.yml
          properties:
            index: index
            size: {get_param: ocgapp_volume_size_0}
            volume_type: {get_param: ocgapp_volume_type_0}
            vnf_name: {get_param: vnf_name}

  outputs:
    ocgapp_volume_ids:
    description: ocgapp volume ids
    value: {get_attr: [ocgapp_volume_resource_group, ocgapp_volume_id_0]}

ocgapp_nested_volume.yml

.. code-block:: yaml

 heat_template_version: 2014-10-16

 description: nested heat

 parameters:
   index:
     type: number
     label: Volume Index
     description: number of volumes to spin up
   size:
     type: number
     label: Volume Size
     description: size of the cinder volumes
   volume_type:
     type: string
     label: Volume Type
     description: type of cinder volumes
   vnf_name:
     type: string
     label: VNF Name
     description: vnf name

 resources:
   ocgapp_volume_0:
     type: OS::Cinder::Volume
     properties:
       size: {get_param: size}
       volume_type: {get_param: volume_type}
       name:
         str_replace:
           template: VF_NAME_STACK_NAME_INDEX
           params:
             VF_NAME: { get_param: vnf_name }
             STACK_NAME: { get_param: 'OS::stack_name' }
             INDEX: {get_param: index}

 outputs:
   ocgapp_volume_id_0:
   description: the ocgapp volume uuid
   value: {get_resource: ocgapp_volume_0}

The heat template below is a partial heat template,

ocgapp.yml

.. code-block:: yaml

  heat_template_version: 2014-10-16

  #file version 1.0
  description: OCG Apps template

  parameters:
    ocgapp_volume_ids:
      type: json
      description: Unique IDs for volumes

  resources:
    ocgapp_server_0:
      type: OS::Nova::Server
      properties:
    . . . .
    ocgapp_server_1:
      type: OS::Nova::Server
      properties:
    . . . .
    ocgapp_volume_attachment_0:
      type: OS::Cinder::VolumeAttachment
      properties:
        volume_id: {get_param: [ocgapp_volume_ids, 0]}
        instance_uuid: {get_resource: ocgapp_server_0}
    ocgapp_volume_attachment_1:
      type: OS::Cinder::VolumeAttachment
      properties:
        volume_id: {get_param: [ocgapp_volume_ids, 1]}
        instance_uuid: {get_resource: ocgapp_server_1}

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

Note that Namespaces in XML (defined at
http://www.w3.org/TR/2009/REC-xml-names-20091208/) are allowed if the
Heat Orchestration Template is describing and storing software
configuration information. An XML namespace is identified by a URI
reference. A Uniform Resource Identifier (URI) is a string of characters
which identifies an Internet Resource. The most common URI is the
Uniform Resource Locator (URL) which identifies an Internet domain
address. Another, not so common type of URI is the Universal Resource
Name (URN). The namespace URI is not used by XML the parser to look up
information. The purpose of using an URI is to give the namespace a
unique name.

Heat Files Support (get\_file)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Heat Templates may contain the inclusion of text files into Heat
templates via the Heat get\_file directive. This may be used, for
example, to define a common "user-data" script, or to inject files into
a VM on startup via the "personality" property.

Support for Heat Files is subject to the following limitations:


.. req::
    :id: R-76718
    :target: VNF
    :keyword: MUST

    If a VNF's Heat Orchestration Template uses the intrinsic function
    'get\_file', the 'get\_file' target **MUST** be referenced in
    the Heat Orchestration Template by file name.

The 'get\_file' target files are on-boarded to SDC in the same package
that contains the VNF's complete Heat Orchestration Template.


.. req::
    :id: R-41888
    :target: VNF
    :keyword: MUST NOT

    A VNF's Heat Orchestration Template intrinsic function
    'get\_file' **MUST NOT** utilize URL-based file retrieval.

.. req::
    :id: R-62177
    :target: VNF
    :keyword: MUST

    When using the intrinsic function get_file, the included files
    **MUST** have unique file names within the scope of the VNF.

.. req::
    :id: R-87848
    :target: VNF
    :keyword: MUST

    A VNF's Heat Orchestration Template's 'get\_file' target files
    **MUST** be in the same directory hierarchy as the VNF's Heat
    Orchestration Templates.

ONAP does not support a hierarchical structure.  A VNF's YAML files
must be in a single, flat directory.


.. req::
    :id: R-05050
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Templates intrinsic function
    'get\_file' <content key> **MAY** be used:

        * more than once in a VNF's Heat Orchestration Template
        * in two or more of a VNF's Heat Orchestration Templates
        * in a VNF's Heat Orchestration Templates nested YAML file

Key Pairs
~~~~~~~~~

When Nova Servers are created via Heat templates, they may be passed a
"keypair" which provides an ssh key to the 'root' login on the newly
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

-  Create a new keypair within The VNF Heat Orchestration Template (in the
   base module) based on an existing public key for use within that VNF

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

*Example: "depends\_on" case*

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

-  The Heat template should spread Nova resources across the
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


