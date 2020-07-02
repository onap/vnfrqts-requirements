.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

.. _ONAP Heat Orchestration Template Format:

ONAP Heat Orchestration Template Format
---------------------------------------
As stated above, Heat Orchestration templates must be defined in YAML.

.. req::
    :id: R-92635
    :target: VNF
    :keyword: MUST
    :introduced: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template **MUST** be compliant with the
    OpenStack Template Guide.

The OpenStack Template Guide is defined at
https://docs.openstack.org/heat/latest/template_guide/index.html#top.

Heat Orchestration Template Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Heat Orchestration template structure follows the following format, as
defined by OpenStack at
https://docs.openstack.org/developer/heat/template_guide/hot_spec.html.

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
~~~~~~~~~~~~~~~~~~~~~


.. req::
    :id: R-27078
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's Heat Orchestration template **MUST** contain the
    section ``heat_template_version:``.

The section ``heat_template_version:`` must be set to a date that
is supported by the OpenStack environment.

description
~~~~~~~~~~~


.. req::
    :id: R-39402
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's Heat Orchestration Template **MUST** contain the
    section ``description:``.

parameter_groups
~~~~~~~~~~~~~~~~

A VNF Heat Orchestration template may
contain the section "parameter_groups:".

parameters
~~~~~~~~~~

.. req::
    :id: R-35414
    :target: VNF
    :keyword: MUST
    :updated: frankfurt
    :validation_mode: static

    A VNF Heat Orchestration's template
    **MUST** contain the section ``parameters:`` with at least one
    parameter defined.


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

      tags: <list of parameter categories>


This section allows for
specifying input parameters that have to be provided when instantiating
the template. Each parameter is specified in a separate nested block
with the name of the parameters defined in the first line and additional
attributes (e.g., type, label) defined as nested elements.


.. req::
    :id: R-90279
    :target: VNF
    :keyword: MUST
    :updated: frankfurt
    :validation_mode: static

    A VNF Heat Orchestration's template's parameter **MUST** be used

    - in a resource AND/OR
    - in a output parameter (in the outputs section)

    with the exception of the parameters for the ``OS::Nova::Server``
    resource property ``availability_zone`` which is defined in R-98450.

.. req::
    :id: R-91273
    :target: VNF
    :keyword: MAY NOT
    :updated: casablanca
    :validation_mode: none

    A VNF Heat Orchestration's template's parameter for the
    ``OS::Nova::Server`` resource property ``availability_zone``
    **MAY NOT** be used in any ``OS::Nova::Server``.

That is, the parameter associated with the property ``availability_zone``
maybe declared but not used in a resource.

<param name>
++++++++++++

The name of the parameter.


.. req::
    :id: R-25877
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's Heat Orchestration Template's parameter name
    (i.e., <param name>) **MUST** contain only alphanumeric
    characters and underscores ('_').

type
++++


.. req::
    :id: R-36772
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's Heat Orchestration Template's parameter **MUST** include the
    attribute ``type:``.

.. req::
    :id: R-11441
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's parameter type **MUST** be one of
    the following values:

    * ``string``
    * ``number``
    * ``json``
    * ``comma_delimited_list``
    * ``boolean``

label
+++++


.. req::
    :id: R-32094
    :target: VNF
    :keyword: MAY
    :validation_mode: none

    A VNF's Heat Orchestration Template parameter declaration **MAY**
    contain the attribute ``label:``.

description
+++++++++++


.. req::
    :id: R-44001
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's Heat Orchestration Template parameter declaration **MUST**
    contain the attribute ``description``.

Note that the parameter attribute ``description:`` is an OpenStack optional
attribute that provides a description of the parameter.
ONAP implementation requires this attribute.

default
+++++++


.. req::
    :id: R-90526
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static

    A VNF Heat Orchestration Template parameter declaration **MUST NOT**
    contain the ``default`` attribute.

.. req::
    :id: R-26124
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: none

    If a VNF Heat Orchestration Template parameter has a default value,
    it **MUST** be enumerated in the environment file.

Note that the parameter attribute ``default:`` is an OpenStack optional
attribute that declares the default value of the parameter.
ONAP implementation prohibits the use of this attribute.

hidden
++++++


.. req::
    :id: R-32557
    :target: VNF
    :keyword: MAY
    :validation_mode: none

    A VNF's Heat Orchestration Template parameter declaration **MAY**
    contain the attribute ``hidden:``.

The parameter attribute ``hidden:`` is an OpenStack optional attribute that
defines whether the parameters should be hidden when a user requests
information about a stack created from the template.
This attribute can be used to hide passwords specified as parameters.

constraints
+++++++++++

The parameter attribute ``constraints:`` is an OpenStack optional attribute
that defines a list of constraints to apply to the parameter.


.. req::
    :id: R-88863
    :target: VNF
    :keyword: MAY
    :updated: dublin
    :validation_mode: none

    A VNF's Heat Orchestration Template's parameter defined
    in a non-nested YAML file as type
    ``number`` **MAY** have a parameter constraint defined.

.. req::
    :id: R-40518
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's parameter defined
    in a non-nested YAML file as type
    ``string`` **MAY** have a parameter constraint defined.

.. req::
    :id: R-96227
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's parameter defined
    in a non-nested YAML file as type
    ``json`` **MAY** have a parameter constraint defined.

.. req::
    :id: R-79817
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's parameter defined
    in a non-nested YAML file as
    type ``comma_delimited_list`` **MAY** have a parameter constraint defined.

.. req::
    :id: R-06613
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's parameter defined
    in a non-nested YAML file as type
    ``boolean`` **MAY** have a parameter constraint defined.

.. req::
    :id: R-00011
    :target: VNF
    :keyword: SHOULD NOT
    :updated: dublin
    :validation_mode: static

    A VNF's Heat Orchestration Template's parameter defined
    in a nested YAML file
    **SHOULD NOT** have a parameter constraint defined.

The constraints block of a parameter definition defines additional
validation constraints that apply to the value of the parameter.
The parameter values provided in the VNF Heat Orchestration Template are
validated against the constraints at instantiation time.
The stack creation fails if the parameter value doesn't comply to
the constraints.

The constraints are defined as a list with the following syntax

.. code-block:: yaml

  constraints:
    - <constraint type>: <constraint definition>
      description: <constraint description>

..

**<constraint type>** Provides the type of constraint to apply.
The list of OpenStack supported constraints can be found at
https://docs.openstack.org/heat/latest/template_guide/hot_spec.html .

**<constraint definition>** provides the actual constraint.
The syntax and constraint is dependent of the <constraint type> used.

**description:** is an optional attribute that provides a description of
the constraint. The text is presented to the user when the value the user
defines violates the constraint. If omitted, a default validation message is
presented to the user.



Below is a brief overview of the ``range`` and ``allowed values`` constraints.
For complete details on constraints, see
https://docs.openstack.org/heat/latest/template_guide/hot_spec.html#parameter-constraints


**range**

``range``: The ``range`` constraint applies to parameters of ``type: number``.
It defines a lower and upper limit for the numeric value of the parameter.
The syntax of the ``range`` constraint is

.. code-block:: yaml

    range: { min: <lower limit>, max: <upper limit> }

..

It is possible to define a range constraint with only a lower limit or an
upper limit.

**allowed_values**

``allowed_values``: The ``allowed_values`` constraint applies to parameters of
type ``string`` or type ``number``. It specifies a set of possible values
for a parameter. At deployment time, the user-provided value for the
respective parameter must match one of the elements of the list.
The syntax of the ``allowed_values`` constraint is

.. code-block:: yaml

    allowed_values: [ <value>, <value>, ... ]

Alternatively, the following YAML list notation can be used

.. code-block:: yaml

    allowed_values:
      - <value>
      - <value>
      - ...

immutable
+++++++++


.. req::
    :id: R-22589
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template parameter declaration
    **MAY** contain the attribute ``immutable:``.

The parameter attribute ``immutable`` is an OpenStack optional attribute
that defines whether the parameter is updatable. A Heat Orchestration Template
stack update fails if ``immutable`` is set to ``true`` and the parameter
value is changed.  This attribute ``immutable`` defaults to ``false``.

tags
++++

.. req::
    :id: R-225891
    :target: VNF
    :keyword: MAY
    :introduced: el alto

    A VNF's Heat Orchestration Template parameter declaration
    **MAY** contain the attribute ``tags:``.


.. _resources:

resources
~~~~~~~~~

.. req::
    :id: R-23663
    :target: VNF
    :keyword: MAY
    :introduced: frankfurt

    A VNF's Heat Orchestration template's base module
    **MAY** (or **MAY NOT**)
    contain the section ``resources:``.

When a VNF is composed of two or more Heat Orchestration Templates (i.e., a
base module and one or more incremental modules),
it is valid for the base module to not declare
a resource.


.. req::
    :id: R-23664
    :target: VNF
    :keyword: MUST
    :updated: frankfurt
    :validation_mode: static

    A VNF's Heat Orchestration template's incremental
    module and volume module **MUST**
    contain the section ``resources:``.

.. req::
    :id: R-90152
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's Heat Orchestration Template's
    ``resources:`` section **MUST** contain the declaration of at
    least one resource.

.. req::
    :id: R-40551
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's Nested YAML files **MAY**
    (or **MAY NOT**) contain the section ``resources:``.

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
+++++++++++

.. req::
    :id: R-75141
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's Heat Orchestration Template's resource name
    (i.e., <resource ID>) **MUST** only contain alphanumeric
    characters and underscores ('_').

.. req::
    :id: R-16447
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's <resource ID> **MUST** be unique across all Heat
    Orchestration Templates and all HEAT Orchestration Template
    Nested YAML files that are used to create the VNF.

Note that a VNF can be composed of one or more Heat Orchestration Templates.

Note that OpenStack requires the <resource ID> to be unique to the
Heat Orchestration Template and not unique across all Heat
Orchestration Templates the compose the VNF.

type
++++

The resource attribute ``type`` is an OpenStack required attribute that
defines the resource type, such as ``OS::Nova::Server`` or
``OS::Neutron::Port``.

The resource attribute ``type`` may specify a VNF HEAT
Orchestration Template Nested YAML file.


.. req::
    :id: R-53952
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static

    A VNF's Heat Orchestration Template's Resource
    **MUST NOT** reference a HTTP-based resource definitions.

.. req::
    :id: R-71699
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static

    A VNF's Heat Orchestration Template's Resource
    **MUST NOT** reference a HTTP-based Nested YAML file.

properties
++++++++++

The resource attribute ``properties`` is an OpenStack optional attribute that
provides a list of resource-specific properties. The property value can
be provided in place, or via a function
(e.g., `Intrinsic functions <https://docs.openstack.org/developer/heat/template_guide/hot_spec.html#hot-spec-intrinsic-functions>`__).


.. req::
    :id: R-10834
    :target: VNF
    :keyword: MUST NOT
    :updated: el alto
    :validation_mode: static

    A VNF's Heat Orchestration Template resource attribute ``property:``
    **MUST NOT** use more than two levels of nested ``get_param`` intrinsic
    functions when deriving a property value.  SDC does not support nested
    ``get_param`` with recursive lists (i.e., a list inside list).
    The second ``get_param`` in a nested lookup must directly derive its value
    without further calls to ``get_param`` functions.

    * Example of valid nesting:

      * ``name: {get_param: [ {vm-type}_names, {get_param : index } ] }``

    * Examples of invalid nesting.  SDC will not support these examples since
      there is an array inside array.

      * ``name: {get_param: [ {vm-type}_names, { get_param: [ indexlist, 0 ] } ] }``
      * ``name: {get_param: [ {vm-type}_names, { get_param: [ indexlist1, { get_param: indexlist2 } ] } ] }``


metadata
++++++++

The resource attribute ``metadata`` is an OpenStack optional attribute.

.. req::
    :id: R-67386
    :target: VNF
    :keyword: MAY
    :introduced: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's Resource **MAY** declare the
    attribute ``metadata``.

depends_on
++++++++++

The resource attribute ``depends_on`` is an OpenStack optional attribute.
See `Section <https://docs.openstack.org/developer/heat/template_guide/hot_spec.html#hot-spec-resources-dependencies>`__ 9.7 for additional details.

.. req::
    :id: R-46968
    :target: VNF
    :keyword: MAY

    VNF's Heat Orchestration Template's Resource **MAY** declare the
    attribute ``depends_on:``.

update_policy
+++++++++++++


.. req::
    :id: R-63137
    :target: VNF
    :keyword: MAY

    VNF's Heat Orchestration Template's Resource **MAY** declare the
    attribute ``update_policy:``.

deletion_policy
+++++++++++++++


.. req::
    :id: R-43740
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    VNF's Heat Orchestration Template's Resource **MAY** declare the
    attribute ``deletion_policy:``.

If specified, the ``deletion_policy`` attribute for resources allows
values ``Delete``, ``Retain``, and ``Snapshot``.
Starting with heat_template_version 2016-10-14,
lowercase equivalents are also allowed.

The default policy is to delete the physical resource when
deleting a resource from the stack.

external_id
+++++++++++


.. req::
    :id: R-78569
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    VNF's Heat Orchestration Template's Resource **MAY** declare the
    attribute ``external_id:``.

This attribute allows for specifying the resource_id for an existing external
(to the stack) resource. External resources cannot depend on other resources,
but we allow other resources to depend on external resource. This attribute
is optional. Note: when this is specified, properties will not be used for
building the resource and the resource is not managed by Heat. This is not
possible to update that attribute. Also, resource won't be deleted by
heat when stack is deleted.


condition
+++++++++

The resource attribute ``condition`` is an OpenStack optional attribute.

outputs
~~~~~~~


.. req::
    :id: R-36982
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration template **MAY** contain the ``outputs:``
    section.

This section allows for specifying output parameters
available to users once the template has been instantiated. If the
section is specified, it will need to adhere to specific requirements.
See :ref:`Output Parameters` and
:ref:`ONAP Output Parameter Names` for additional details.

Environment File Format
^^^^^^^^^^^^^^^^^^^^^^^

A VNF's Heat Orchestration Template's environment file is a yaml text file.
(https://docs.openstack.org/developer/heat/template_guide/environment.html)


.. req::
    :id: R-86285
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration template **MUST** have a
    corresponding environment file.

The use of an environment file in OpenStack is optional. In ONAP, it is
mandatory. A Heat Orchestration Template uploaded to ONAP must have a
corresponding environment file, even if no parameters are enumerated in
the mandatory parameter section.


.. req::
    :id: R-03324
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration template's Environment File **MUST**
    contain the ``parameters:`` section.

.. req::
    :id: R-68198
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration template's Environment File's
    ``parameters:`` section **MAY** (or **MAY NOT**) enumerate parameters.

ONAP implementation requires the parameters section in the environmental
file to be declared.  The parameters section contains a list of key/value
pairs.


.. req::
    :id: R-59930
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration template's Environment File's
    **MAY** contain the ``parameter_defaults:`` section.

The ``parameter_defaults:`` section contains default parameters that are
passed to all template resources.


.. req::
    :id: R-46096
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration template's Environment File's
    **MAY** contain the ``encrypted_parameters:`` section.

The ``encrypted_parameters:`` section contains a list of encrypted parameters.


.. req::
    :id: R-24893
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration template's Environment File's
    **MAY** contain the ``event_sinks:`` section.

The ``event_sinks:`` section contains the list of endpoints that would receive
stack events.


.. req::
    :id: R-42685
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration template's Environment File's
    **MAY** contain the ``parameter_merge_strategies:`` section.

The ``parameter_merge_strategies:`` section provides the merge strategies for
merging parameters and parameter defaults from the environment file.


.. req::
    :id: R-67231
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static

    A VNF's Heat Orchestration template's Environment File's
    **MUST NOT** contain the ``resource_registry:`` section.

ONAP implementation does not support the Environment File resource_registry
section.  The resource_registry section allows for the definition of custom
resources.

