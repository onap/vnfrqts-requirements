.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.


Resource: OS::Nova::Server - Parameters
-----------------------------------------------------------------------

The OS::Nova::Server resource manages the running virtual machine (VM)
instance within an OpenStack cloud. (See
https://docs.openstack.org/developer/heat/template_guide/openstack.html#OS::Nova::Server)

The following four properties of the ``OS::Nova::Server``
resource must follow an
ONAP specified naming convention.

1. ``image``

2. ``flavor``

3. ``name``

4. ``availability_zone``

Requirement R-01455 defines how the ``{vm-type]`` is defined.

.. req::
    :id: R-304011
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :introduced: casablanca
    :updated: el alto

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource's

    * Resource ID (defined in R-29751)
    * property ``image`` parameter name (defined in R-58670)
    * property ``flavor`` parameter name (defined in R-45188)
    * property ``name`` parameter name (defined in R-54171 & R-87817)
    * property ``networks`` map property ``port`` value which is a
      ``OS::Neutron::Port`` Resource ID (defined in R-20453)
      referenced using the intrinsic function ``get_attr``

    **MUST** contain the identical ``{vm-type}``
    and **MUST** follow the naming conventions defined
    in R-58670, R-45188, R-54171, R-87817, and R-29751.  And the ``{index}`` in
    the ``OS::Nova::Server`` Resource ID (defined in R-29751) **MUST** match
    the ``{vm-type_index}`` defined in
    the ``OS::Nova::Server`` property ``networks`` map property ``port``
    referenced ``OS::Neutron::Port`` Resource ID (defined in R-20453).


The table below provides a summary. The sections that follow provides
the detailed requirements.

.. csv-table:: **Table 1 OS::Nova::Server Resource Property Parameter Naming Convention**
   :header: Resource,Property,Parameter Type,Parameter Name,Parameter Value Provided to Heat
   :align: center
   :widths: auto

   OS::Nova::Server, image, string, {vm-type}_image_name, Environment File
   OS::Nova::Server, flavor, string, {vm-type}_flavor_name, Environment File
   OS::Nova::Server, name, string, {vm-type}_name_{index}, ONAP
   OS::Nova::Server, name, CDL, {vm-type}_names, ONAP
   OS::Nova::Server, availability_zone, string, availability_zone_{index}, ONAP

.. _Property image:

Property: image
^^^^^^^^^^^^^^^


.. req::
    :id: R-901331
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :introduced: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``image`` value **MUST** be be obtained via a ``get_param``.

.. req::
    :id: R-71152
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property
    ``image`` parameter **MUST** be declared as type: ``string``.

.. req::
    :id: R-58670
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property
    ``image`` parameter name **MUST** follow the naming convention
    ``{vm-type}_image_name``.

.. req::
    :id: R-91125
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property
    ``image`` parameter **MUST** be enumerated in the Heat Orchestration
    Template's Environment File and a value **MUST** be assigned.

.. req::
    :id: R-57282
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    Each VNF's Heat Orchestration Template's ``{vm-type}`` **MUST**
    have a unique parameter name for the ``OS::Nova::Server`` property
    ``image`` even if more than one ``{vm-type}`` shares the same image.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     {vm-type}_image_name:
         type: string
         description: {vm-type} server image

.. _Property flavor:

Property: flavor
^^^^^^^^^^^^^^^^^^


.. req::
    :id: R-481670
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :introduced: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``flavor`` value **MUST** be be obtained via a ``get_param``.

.. req::
    :id: R-50436
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property
    ``flavor`` parameter **MUST** be declared as type: ``string``.

.. req::
    :id: R-45188
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource 'OS::Nova::Server' property
    ``flavor`` parameter name **MUST** follow the naming convention
    ``{vm-type}_flavor_name``.

.. req::
    :id: R-69431
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property
    ``flavor`` parameter **MUST** be enumerated in the Heat Orchestration
    Template's Environment File and a value **MUST** be assigned.

.. req::
    :id: R-40499
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    Each VNF's Heat Orchestration Template's ``{vm-type}`` **MUST**
    have a unique parameter name for the ``OS::Nova::Server`` property
    ``flavor`` even if more than one ``{vm-type}`` shares the same flavor.

*Example Parameter Definition*

.. code-block:: yaml

 parameters:
     {vm-type}_flavor_name:
         type: string
         description: {vm-type} flavor

Property: Name
^^^^^^^^^^^^^^^^^


.. req::
    :id: R-663631
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :introduced: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``name`` value **MUST** be be obtained via a ``get_param``.

.. req::
    :id: R-51430
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property
    ``name`` parameter **MUST** be declared as either type ``string``
    or type ``comma_delimited_list``.

.. req::
    :id: R-54171
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: dublin

    When the VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``name`` parameter is defined as a ``string``,
    the parameter name **MUST** follow the naming convention

    * ``{vm-type}_name_{index}``

    where ``{index}`` is a numeric value that **MUST** start at
    zero in a VNF's Heat Orchestration Template and **MUST** increment by one.

.. req::
    :id: R-87817
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``name`` parameter is defined as a ``comma_delimited_list``,
    the parameter name **MUST** follow the naming convention
    ``{vm-type}_names``.

.. req::
    :id: R-22838
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property
    ``name`` parameter **MUST NOT** be enumerated in the Heat Orchestration
    Template's Environment File.

If a VNF's Heat Orchestration Template's contains more than three
OS::Nova::Server resources of a given ``{vm-type}``, the comma_delimited_list
form of the parameter name (i.e., ``{vm-type}_names``) should be used to
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. req::
    :id: R-44271
    :target: VNF
    :keyword: SHOULD NOT
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property
    ``name`` parameter value **SHOULD NOT** contain special characters
    since the Contrail GUI has a limitation displaying special characters.

    However, if special characters must be used, the only special characters
    supported are: --- \" ! $ ' (\ \ ) = ~ ^ | @ ` { } [ ] > , . _


Property: availability_zone
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. req::
    :id: R-98450
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: el alto

    A VNF's Heat Orchestration Template's base module or incremental module
    resource ``OS::Nova::Server``
    property ``availability_zone`` parameter
    **MUST** follow the naming convention

    * ``availability_zone_{index}``

    where ``{index}`` is a numeric value that **MUST** start at zero
    in a VNF's Heat Orchestration Templates and **MUST**
    increment by one.

.. req::
    :id: R-23311
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: el alto

    The VNF's Heat Orchestration Template's base module or incremental module
    resource ``OS::Nova::Server`` property
    ``availability_zone`` parameter **MUST** be declared as type: ``string``.

The parameter must not be declared as type ``comma_delimited_list``, ONAP does
not support it.

.. req::
    :id: R-59568
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property
    ``availability_zone`` parameter **MUST NOT** be enumerated in the Heat
    Orchestration
    Template's Environment File.


.. req::
    :id: R-256790
    :target: VNF
    :keyword: MAY
    :validation_mode: none
    :introduced: el alto

    A VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``availability_zone`` parameter name **MAY** change when
    past into a nested YAML file.


Example Parameter Definition

.. code-block:: yaml

  parameters:
    availability_zone_{index}:
      type: string
      description: availability zone {index} name

Requirement :need:`R-90279` states that a VNF Heat Orchestration's template's
parameter MUST be used in a resource with the exception of the parameters
for the OS::Nova::Server resource property availability_zone.


.. req::
    :id: R-01359
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template that contains an ``OS::Nova:Server``
    resource **MAY** define a parameter for the property
    ``availability_zone`` that is not utilized in any ``OS::Nova::Server``
    resources in the Heat Orchestration Template.

Example
^^^^^^^^^^^

The example below depicts part of a Heat Orchestration Template that
uses the four ``OS::Nova::Server`` properties discussed in this section.

In the Heat Orchestration Template below, four Virtual Machines
(``OS::Nova::Server``) are created: two dns servers with ``{vm-type}`` set to
``dns`` and two oam servers with ``{vm-type}`` set to ``oam``.
Note that the parameter
associated with the property name is a ``comma_delimited_list`` for ``dns`` and
a string for ``oam``.

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
^^^^^^^^^^^^^^^


.. req::
    :id: R-99798
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's Virtual Machine
    (i.e., ``OS::Nova::Server`` resource) **MAY** boot from an image or
    **MAY** boot from a Cinder Volume.

.. req::
    :id: R-83706
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    When a VNF's Heat Orchestration Template's Virtual Machine
    (i.e., ``OS::Nova::Server`` resource) boots from an image, the
    ``OS::Nova::Server`` resource property ``image`` **MUST** be used.

The requirements associated with
the 'image' property are detailed in `Property: image`_


.. req::
    :id: R-69588
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    When a VNF's Heat Orchestration Template's Virtual Machine
    (i.e., ``OS::Nova::Server`` Resource) boots from Cinder Volume, the
    ``OS::Nova::Server`` resource property
    ``block_device_mapping`` or ``block_device_mapping_v2``
    **MUST** be used.

There are currently no heat guidelines
associated with these two properties:
'block_device_mapping' and 'block_device_mapping_v2'.
