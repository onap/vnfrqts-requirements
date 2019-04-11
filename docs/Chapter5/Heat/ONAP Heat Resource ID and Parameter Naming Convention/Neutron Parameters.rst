.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

Resource: OS::Neutron::Port - Parameters
-------------------------------------------------

The resource OS::Neutron::Port is for managing Neutron ports.

(See https://docs.openstack.org/developer/heat/template_guide/openstack.html#OS::Neutron::Port)

Introduction
^^^^^^^^^^^^^

Four properties of the resource ``OS::Neutron::Port`` must follow the ONAP
naming convention. The four properties are:

1. network
2. fixed_ips, ip_address
3. fixed_ips, subnet

 * Note that earlier versions of this document mentioned the property
   fixed_ips, subnet_id.  This property has been removed from the document
   since it has been deprecated.
   See https://github.com/openstack/heat/blob/stable/ocata/heat/engine/resources/openstack/neutron/port.py

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
networks are defined in :ref:`ONAP Heat Networking`.

When the ``OS::Neutron::Port`` is attaching to an external network, all
property values are parameters that are retrieved via the intrinsic
function ``get_param``.

When the ``OS::Neutron::Port`` is attaching to an internal network, a
property value maybe retrieved via the intrinsic
function ``get_param``, ``get_resource``, or ``get_attr``.

This will be described in the forth coming sections.

Items to Note
~~~~~~~~~~~~~~

A VNF **MAY** have one or more ports connected to a unique
external network. All VNF ports connected to the unique external
network **MUST** have cloud assigned IP Addresses
or **MUST** have ONAP SDN-C assigned IP addresses.

A VNF **MAY** have one or more ports connected to a unique
internal network. All VNF ports connected to the unique internal
network **MUST** have cloud assigned IP Addresses
or **MUST** have statically assigned IP addresses.

.. req::
    :id: R-45602
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: none
    :updated: casablanca

    If a VNF's Port is attached to a network (internal or external)
    and the port's IP addresses are cloud assigned by OpenStack's DHCP
    Service, the ``OS::Neutron::Port`` Resource's

    * property ``fixed_ips`` map property ``ip_address`` **MUST NOT** be used
    * property ``fixed_ips`` map property ``subnet``
      **MAY** be used

.. req::
    :id: R-63956
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    If the VNF's ports connected to a unique external network
    and the port's IP addresses are ONAP SDN-C assigned IP Addresses,
    the IPv4 Addresses **MAY** be from different subnets and the IPv6
    Addresses **MAY** be from different subnets.

.. req::
    :id: R-48880
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    If a VNF's Port is attached to an external network and the port's
    IP addresses are assigned by ONAP's SDN-Controller,
    the ``OS::Neutron::Port`` Resource's

    * property ``fixed_ips`` map property ``ip_address`` **MUST** be used
    * property ``fixed_ips`` map property ``subnet``
      **MUST NOT** be used

.. req::
    :id: R-18001
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    If the VNF's ports connected to a unique internal network
    and the port's IP addresses are statically assigned IP Addresses,
    the IPv4 Addresses **MAY** be from different subnets and the
    IPv6 Addresses **MAY** be from different subnets.

.. req::
    :id: R-70964
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: none
    :updated: casablanca

    If a VNF's Port is attached to an internal network and the port's
    IP addresses are statically assigned by the VNF's Heat Orchestration\
    Template (i.e., enumerated in the Heat Orchestration Template's
    environment file), the ``OS::Neutron::Port`` Resource's

    * property ``fixed_ips`` map property ``ip_address`` **MUST** be used
    * property ``fixed_ips`` map property ``subnet``
      **MUST NOT** be used

.. req::
    :id: R-681859
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Neutron::Port`` resource's

    * Resource ID (defined in R-20453)
    * property ``network`` parameter name (defined in R-62983 and
      R-86182)
    * property ``fixed_ips``, map property ``ip_address`` parameter name
      (defined in R-40971, R-04697, R-71577, R-23503, R-78380, R-85235,
      R-27818, and R-29765)
    * property ``fixed_ips``, map property ``subnet`` parameter name
      (defined in R-62802, R-15287, R-84123, R-76160)
    * property ``allowed_address_pairs`` parameter name (defined in
      R-41492 and R-83418)

    **MUST** contain the identical ``{network-role}``.

Property: network
^^^^^^^^^^^^^^^^^^

The Resource ``OS::Neutron::Port`` property ``network`` determines what network
the port is attached to.

.. req::
    :id: R-18008
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    property ``network`` parameter **MUST** be declared as type: ``string``.

.. req::
    :id: R-62983
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424), the
    ``network`` parameter name **MUST**

      * follow the naming convention ``{network-role}_net_id`` if the Neutron
        network UUID value is used to reference the network
      * follow the naming convention ``{network-role}_net_name`` if the
        OpenStack network name is used to reference the network.

    where ``{network-role}`` is the network-role of the external network
    and a ``get_param`` **MUST** be used as the intrinsic function.

.. req::
    :id: R-86182
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: dublin

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port``
    is in an incremental module and
    is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    the ``network`` parameter name **MUST**

      * follow the naming convention ``int_{network-role}_net_id`` if the
        network UUID value is used to reference the network
      * follow the naming convention ``int_{network-role}_net_name`` if the
        network name in is used to reference the network.

    where ``{network-role}`` is the network-role of the internal network and
    a ``get_param`` **MUST** be used as the intrinsic function.


In Requirement R-86182, the internal network is created in the VNF's
Base Module (Heat Orchestration Template) and the parameter name is
declared in the Base Module's ``outputs`` section.
The output parameter name will be declared as a parameter in the
``parameters`` section of the incremental module (See Requirement R-22688).


When the VNF's Heat Orchestration Template's resource
``OS::Neutron::Port`` is in the base module and
is attaching to an internal network (per the
ONAP definition, see Requirements R-52425 and R-46461),
and the internal network is

 * created in the base module,
   the ``network`` property value can obtain the UUID
   of the internal network by using the intrinsic function
   ``get_resource`` and referencing the Resource ID of the internal network.
 * created in the base module by invoking a Nested YAML file, the network
   property value can obtain the UUID of the internal network by using the
   intrinsic function get_attr and referencing the Resource ID of the internal
   network.


.. req::
    :id: R-29872
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    property ``network``
    parameter **MUST NOT** be enumerated in the Heat Orchestration
    Template's Environment File.

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The resource ``OS::Neutron::Port`` property ``fixed_ips``
map property ``ip_address``
is used to assign one IPv4 or IPv6
addresses to port.

One ``OS::Neutron::Port`` resource may assign one or more
IPv4 and/or IPv6 addresses.

.. req::
    :id: R-34037
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's
    resource ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    **MUST** be declared as either type ``string`` or type
    ``comma_delimited_list``.

.. req::
    :id: R-40971
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv4 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a string,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_{network-role}_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the external network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one

.. req::
    :id: R-39841
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_{network-role}_ip_{index}``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

ONAP's SDN-Controller assigns the IP Address and ONAP provides
the value at orchestration to the Heat Orchestration Template.

*Example External Network IPv4 Address string Parameter Definition*

.. code-block:: yaml

  parameters:

    {vm-type}_{network-role}_ip_{index}:
      type: string
      description: Fixed IPv4 assignment for {vm-type} VM {index} on the {network-role} network

.. req::
    :id: R-04697
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv4 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_{network-role}_ips``

      where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the external
        network

.. req::
    :id: R-98905
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_{network-role}_ips``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

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
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a string,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_{network-role}_v6_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the
      ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the external network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one

.. req::
    :id: R-87123
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_{network-role}_v6_ip_{index}``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

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
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_{network-role}_v6_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

.. req::
    :id: R-93030
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_{network-role}_v6_ips``
    **MUST NOT** be enumerated in the
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
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv4 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is
    defined as a ``string``,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_int_{network-role}_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the
      ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the internal network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one

.. req::
    :id: R-28795
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_int_{network-role}_ip_{index}``
    **MUST** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

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
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv4 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the internal
        network

.. req::
    :id: R-90206
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_int_{network-role}_int_ips``
    **MUST** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

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
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
    ``string``,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_int_{network-role}_v6_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the internal network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one


.. req::
    :id: R-97201
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_int_{network-role}_v6_ip_{index}``
    **MUST** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

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
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_v6_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the internal
        network

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
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``ip_address`` parameter
    ``{vm-type}_int_{network-role}_v6_ips``
    **MUST** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

The IP address is local to the VNF's internal network and is (re)used
in every VNF spin up, thus the constant value is declared in the VNF's
Heat Orchestration Template's Environment File.

.. code-block:: yaml

  parameters:

    {vm-type}_int_{network-role}_v6_ips:
      type: comma_delimited_list
      description: Fixed IPv6 assignments for {vm-type} VMs on the int_{network-role} network

.. req::
    :id: R-62590
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    property ``fixed_ips``
    map property ``ip_address``
    parameter associated with an external network, i.e.,

     * ``{vm-type}_{network-role}_ip_{index}``
     * ``{vm-type}_{network-role}_v6_ip_{index}``
     * ``{vm-type}_{network-role}_ips``
     * ``{vm-type}_{network-role}_v6_ips``


    **MUST NOT** be enumerated in the Heat Orchestration
    Template's Environment File.  ONAP provides the IP address
    assignments at orchestration time.

.. req::
    :id: R-93496
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    property ``fixed_ips``
    map property ``ip_address``
    parameter associated with an internal network, i.e.,

     * ``{vm-type}_int_{network-role}_ip_{index}``
     * ``{vm-type}_int_{network-role}_v6_ip_{index}``
     * ``{vm-type}_int_{network-role}_ips``
     * ``{vm-type}_int_{network-role}_v6_ips``


    **MUST** be enumerated in the Heat Orchestration
    Template's Environment File and IP addresses **MUST** be
    assigned.

Summary Table
~~~~~~~~~~~~~~~~~

.. csv-table:: **Table 4 OS::Neutron::Port Property fixed_ips map property ip_address Parameter Naming Convention**
   :header: Resource,Property,Map Property,Network Type,IP Address,Parameter Type,Parameter Name, Environment File
   :align: center
   :widths: auto

   OS::Neutron::Port, fixed_ips, ip_address, external, IPv4, string, {vm-type}_{network-role}_ip_{index}, NO
   OS::Neutron::Port, fixed_ips, ip_address, external, IPv4, comma_delimited_list, {vm-type}_{network-role}_ips, NO
   OS::Neutron::Port, fixed_ips, ip_address, external, IPv6, string, {vm-type}_{network-role}_v6_ip_{index}, NO
   OS::Neutron::Port, fixed_ips, ip_address, external, IPv6, comma_delimited_list, {vm-type}_{network-role}_v6_ips, NO
   OS::Neutron::Port, fixed_ips, ip_address, internal, IPv4, string, {vm-type}_int_{network-role}_ip_{index}, YES
   OS::Neutron::Port, fixed_ips, ip_address, internal, IPv4, comma_delimited_list, {vm-type}_int_{network-role}_ips, YES
   OS::Neutron::Port, fixed_ips, ip_address, internal, IPv6, string, {vm-type}_int_{network-role}_v6_ip_{index}, YES
   OS::Neutron::Port, fixed_ips, ip_address, internal, IPv6, comma_delimited_list, {vm-type}_int_{network-role}_v6_ips, YES


Examples
~~~~~~~~~~~~~~

*Example: comma_delimited_list parameters for IPv4 and IPv6 Address
Assignments to an external network*

In this example, the ``{network-role}`` has been defined as ``oam`` to
represent an oam network and the ``{vm-type}`` has been defined as ``db``
for database.

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

In this example, the ``{network-role}`` has been defined as ``oam`` to
represent an oam network and the ``{vm-type}`` has been defined as ``db`` for
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
        fixed_ips: [ { "ip_address": {get_param: db_oam_ip_0}}, { "ip_address": {get_param: db_oam_v6_ip_0 }}]
    db_1_oam_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: oam_net_id }
        fixed_ips:
          - "ip_address": {get_param: db_oam_ip_1}
          - "ip_address": {get_param: db_oam_v6_ip_1}


*Example*: comma_delimited_list parameters for IPv4 and IPv6 Address
Assignments to an internal network*

In this example, the ``{network-role}`` has been defined as ``ctrl`` to
represent an ctrl network internal to the vnf.
The ``{vm-type}`` has been defined as ``db`` for
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

In this example, the ``int_{network-role}`` has been defined as
``int_ctrl`` to represent a control network internal to the vnf.
The ``{vm-type}`` has been defined as ``db`` for database.

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
        "ip_address": {get_param: db_oam_int_v6_ip_0 }}]
    db_1_int_ctrl_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: int_oam_int_net_id }
        fixed_ips:
          - "ip_address": {get_param: db_oam_int_ip_1}
          - "ip_address": {get_param: db_oam_int_v6_ip_1}


Property: fixed_ips, Map Property: subnet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The resource ``OS::Neutron::Port`` property ``fixed_ips`` map
property ``subnet`` is used when a
port is requesting an IP assignment via
OpenStack’s DHCP Service (i.e., cloud assigned).

The IP address assignment will be made from the specified subnet.

Specifying the subnet is not required; it is optional.

If the network (external or internal) that the port is attaching
to only contains one subnet, specifying the subnet is
superfluous.  The IP address will be assigned from the one existing
subnet.

If the network (external or internal) that the port is attaching
to contains two or more subnets, specifying the subnet in the
``fixed_ips`` map property ``subnet`` determines which
subnet the IP address will be assigned from.

If the network (external or internal) that the port is attaching
to contains two or more subnets, and the subnet is not is not
specified, OpenStack will randomly determine which subnet
the IP address will be assigned from.

The property ``fixed_ips`` is used to assign IPs to a port. The Map Property
``subnet`` specifies the subnet the IP is assigned from.

.. req::
    :id: R-38236
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's
    resource ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``subnet`` parameter
    **MUST** be declared type ``string``.

.. req::
    :id: R-62802
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's
    resource ``OS::Neutron::Port`` is attaching
    to an external network (per the ONAP definition, see
    Requirement R-57424),
    and an IPv4 address is being cloud assigned by OpenStack's DHCP Service
    and the external network IPv4 subnet is to be specified
    using the property ``fixed_ips``
    map property ``subnet``, the parameter
    **MUST** follow the naming convention

      * ``{network-role}_subnet_id``

    where

      * ``{network-role}`` is the network role of the network.


Note that ONAP only supports cloud assigned IP addresses from one IPv4 subnet
of a given network.

.. req::
    :id: R-83677
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca


    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``subnet`` parameter
    ``{network-role}_subnet_id``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

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
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's
    resource ``OS::Neutron::Port`` is attaching
    to an external network (per the ONAP definition, see
    Requirement R-57424),
    and an IPv6 address is being cloud assigned by OpenStack's DHCP Service
    and the external network IPv6 subnet is to be specified
    using the property ``fixed_ips``
    map property ``subnet``, the parameter
    **MUST** follow the naming convention

      * ``{network-role}_v6_subnet_id``

    where

      * ``{network-role}`` is the network role of the network.

Note that ONAP only supports cloud assigned IP addresses from one IPv6 subnet
of a given network.

.. req::
    :id: R-80829
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``subnet`` parameter
    ``{network-role}_v6_subnet_id``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

*Example: One Cloud Assigned IPv4 Address (DHCP) assigned to a network
that has two or more IPv4 subnets*

In this example, the ``{network-role}`` has been defined as ``oam`` to
represent an oam network and the ``{vm-type}`` has been defined as ``lb``
for load balancer. The cloud assigned IP Address uses the OpenStack
DHCP service to assign IP addresses.

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
            - subnet: { get_param: oam_subnet_id }

*Example: One Cloud Assigned IPv4 address and one Cloud Assigned IPv6
address assigned to a network that has at least one IPv4 subnet and one
IPv6 subnet*

In this example, the ``{network-role}`` has been defined as ``oam`` to
represent an oam network and the ``{vm-type}`` has been defined as
``lb`` for load balancer.

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
          - subnet: { get_param: oam_subnet_id }
          - subnet: { get_param: oam_v6_subnet_id }

.. req::
    :id: R-84123
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    When

      * the VNF's Heat Orchestration Template's
        resource ``OS::Neutron::Port`` in an Incremental Module is attaching
        to an internal network (per the ONAP definition, see
        Requirements R-52425 and R-46461)
        that is created in the Base Module, AND
      * an IPv4 address is being cloud assigned by OpenStack's DHCP Service AND
      * the internal network IPv4 subnet is to be specified
        using the property ``fixed_ips`` map property ``subnet``,

    the parameter **MUST** follow the naming convention

      * ``int_{network-role}_subnet_id``

    where

      * ``{network-role}`` is the network role of the internal network

    Note that the parameter **MUST** be defined as an ``output`` parameter in
    the base module.

.. req::
    :id: R-69634
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``subnet`` parameter
    ``int_{network-role}_subnet_id``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

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
    :validation_mode: static
    :updated: casablanca

    When

      * the VNF's Heat Orchestration Template's
        resource ``OS::Neutron::Port`` in an Incremental Module is attaching
        to an internal network (per the ONAP definition, see Requirements
        R-52425 and R-46461)
        that is created in the Base Module, AND
      * an IPv6 address is being cloud assigned by OpenStack's DHCP Service AND
      * the internal network IPv6 subnet is to be specified
        using the property ``fixed_ips`` map property ``subnet``,

    the parameter **MUST** follow the naming convention
    ``int_{network-role}_v6_subnet_id``,
    where ``{network-role}`` is the network role of the internal network.

    Note that the parameter **MUST** be defined as an ``output`` parameter in
    the base module.

.. req::
    :id: R-22288
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``fixed_ips``
    map property ``subnet`` parameter
    ``int_{network-role}_v6_subnet_id``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.


*Example Parameter Definition*

.. code-block:: yaml

  parameters:

    int_{network-role}_v6_subnet_id:
      type: string
      description: Neutron subnet UUID for the int_{network-role} network

Property: allowed\_address\_pairs, Map Property: ip\_address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The property ``allowed_address_pairs`` in the resource ``OS::Neutron::Port``
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


If a VNF has two or more ports that require a Virtual IP Address (VIP),
a VNF's Heat Orchestration Template's Resource
``OS::Neutron::Port`` property ``allowed_address_pairs``
map property ``ip_address`` parameter
must be used.

The ``allowed_address_pairs`` is an optional property. It is not required.

ONAP automation supports the assignment of VIP addresses
for external networks.  ONAP support the assignment of one IPv4 VIP address
and/or one IPv6 VIP address to a set of ports associated with a
``{vm-type}`` and ``{network-role}``.

If a VNF requires more than one IPv4 VIP address
and/or more than one IPv6 VIP address to a set of ports associated with a
``{vm-type}`` and ``{network-role}``, there are "manual" work-around
procedures that can be utilized.

VIP Assignment, External Networks, Supported by Automation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-91810
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    If a VNF requires ONAP to assign a Virtual IP (VIP) Address to
    ports connected an external network, the port
    **MUST NOT** have more than one IPv4 VIP address.

.. req::
    :id: R-41956
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    If a VNF requires ONAP to assign a Virtual IP (VIP) Address to
    ports connected an external network, the port
    **MUST NOT** have more than one IPv6 VIP address.

.. req::
    :id: R-10754
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    If a VNF has two or more ports that
    attach to an external network that require a Virtual IP Address (VIP),
    and the VNF requires ONAP automation to assign the IP address,
    all the Virtual Machines using the VIP address **MUST**
    be instantiated in the same Base Module Heat Orchestration Template
    or in the same Incremental Module Heat Orchestration Template.


.. req::
    :id: R-41492
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv4 Virtual IP (VIP)
    address is assigned via ONAP automation
    using the property ``allowed_address_pairs``
    map property ``ip_address`` and
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_{network-role}_floating_ip``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as type ``string``.

.. req::
    :id: R-83412
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``allowed_address_pairs``
    map property ``ip_address`` parameter
    ``{vm-type}_{network-role}_floating_ip``
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
    :validation_mode: static
    :updated: casablanca

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv6 Virtual IP (VIP)
    address is assigned via ONAP automation
    using the property ``allowed_address_pairs``
    map property ``ip_address``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_{network-role}_floating_v6_ip``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as type ``string``.

.. req::
    :id: R-83418
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    The VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` property ``allowed_address_pairs``
    map property ``ip_address`` parameter
    ``{vm-type}_{network-role}_floating_v6_ip``
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.

*Example Parameter Definition*

.. code-block:: yaml

  parameters:

    {vm-type}_{network-role}_floating_v6_ip:
      type: string
      description: VIP for {vm-type} VMs on the {network-role} network

.. req::
    :id: R-159016
    :keyword: MUST NOT
    :updated: dublin
    :validation_mode: static
    :target: VNF

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an external network (per the
    ONAP definition, see Requirement R-57424),
    and an IPv4 and/or IPv6 Virtual IP (VIP)
    address is assigned via ONAP automation
    using the property ``allowed_address_pairs``
    map property ``ip_address``, the
    parameter **MUST NOT** be declared as ``type: comma_deliited_list``.



.. req::
    :id: R-717227
    :keyword: MUST
    :updated: dublin
    :validation_mode: static
    :target: VNF

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv4 Virtual IP (VIP)
    address is assigned using the property ``allowed_address_pairs``
    map property ``ip_address``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_ip``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network
    
    And the parameter **MUST** be declared as ``type: string``
    and **MUST** be enumerated in the environment file.

    OR 

    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network
    
    And the parameter **MUST** be declared as ``type: comma_delimited_list``
    and **MUST** be enumerated in the environment file.


.. req::
    :id: R-805572
    :keyword: MUST
    :updated: dublin
    :validation_mode: static
    :target: VNF

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461),
    and an IPv6 Virtual IP (VIP)
    address is assigned
    using the property ``allowed_address_pairs``
    map property ``ip_address``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_v6_ip``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as ``type: string``
    and **MUST** be enumerated in the environment file

    OR

    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_v6_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the external
        network

    And the parameter **MUST** be declared as ``type: comma_delimited_list``
    and **MUST** be enumerated in the environment file.


Note that these parameters are **not** intended to represent an OpenStack
"Floating IP", for which OpenStack manages a pool of public IP
addresses that are mapped to specific VM ports. In that case, the
individual VMs are not even aware of the public IPs, and all assignment
of public IPs to VMs is via OpenStack commands. ONAP does not support
Neutron-style Floating IPs.  That is, ONAP does not support the
resources ``OS::Neutron::FloatingIP``
and ``OS::Neutron::FloatingIPAssociation``.


.. req::
    :id: R-05257
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's **MUST NOT**
    contain the Resource ``OS::Neutron::FloatingIP``.

.. req::
    :id: R-76449
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's **MUST NOT**
    contain the Resource ``OS::Neutron::FloatingIPAssociation``.

The Floating IP functions as a NAT.  They are allocated within
Openstack, and always "terminate" within the Openstack infrastructure.
When Openstack receives packets on a Floating IP, the packets will
be forwarded to the
Port that has been mapped to the Floating IP, using the private address of the
port.  The VM never sees or knows about the Openstack Floating IP.
The process to use is:

  - User allocates a floating IP from the Openstack pool.
  - User ‘attaches’ that floating IP to one of the VM ports.

If there is a high-availability VNF that wants to "float" the IP to a
different VM, it requires a Neutron command to request Openstack to ‘attach’
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
Openstack to ‘float’ such an IP from one VM to another).

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The parameter ``{vm-type}_{network-role}_floating_ip`` allows for only one
allowed address pair IPv4 address per ``{vm-type}`` and ``{network-role}``
combination.

The parameter ``{vm-type}_{network-role}_floating_v6_ip`` allows for only one
allowed address pair IPv6 address per ``{vm-type}`` and ``{network-role}``
combination.

If there is a need for multiple allowed address pair IPs for a given
{vm-type} and {network-role} combination within a VNF, there are two
options.

**Option One**

If there is a need for multiple allowed address pair IPs for a given
``{vm-type}`` and ``{network-role}`` combination within a VNF, then the
parameter names defined for the Property ``fixed_ips`` Map Property
``ip_address`` should be used or the Property ``allowed_address_pairs``
Map Property ``ip_address``. The
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
``{vm-type}`` and ``{network-role}`` combination within a VNF, then the
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
``{vm-type}`` and ``{network-role}`` combination within a VNF and the need to
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
~~~~~~~~~~~~~~~~~~~~~~~

ONAP defines an internal network in relation to
the VNF and not with regard to the cloud site. Internal
networks may also be referred to as "intra-VNF" networks or "private"
networks. An internal network only connects VMs in a single VNF. It
must not connect to other VNFs or an external (to the cloud) gateway or an
external (to the cloud) router.

ONAP internal networks should be created in the base module.

As previously mentioned, ports that connect to an internal network are assigned
IP addresses via one of two methods

 * Method 1: Cloud assigned by OpenStack's DHCP Service
 * Method 2: Statically assigned.  That is, predetermined by the VNF designer
   and are specified in the VNF's Heat Orchestration Template's
   Environment File

If cloud assigned IP addressing is being used, output statements
are created in the base module.

If static assigned IP addressing is being used, the  IP addresses
are defined in the environment file.


  * ``{vm-type}_int_{network-role}_floating_ip``
  * ``{vm-type}_int_{network-role}_floating_v6_ip``

  * ``{vm-type}_int_{network-role}_vip_{index}``
  * ``{vm-type}_int_{network-role}_vips``
  * ``{vm-type}_int_{network-role}_v6_vip_{index}``
  * ``{vm-type}_int_{network-role}_v6_vips``


  * ``{vm-type}_int_{network-role}_{vip_type}_vip``
  * ``{vm-type}_int_{network-role}_{vip_type}_vips``
  * ``{vm-type}_int_{network-role}_{vip_type}_v6_vip``
  * ``{vm-type}_int_{network-role}_{vip_type}_v6_vips``



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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the IP address ``{vm-type}_{network-role}_floating_ip`` and/or
``{vm-type}_{network-role}_floating_v6_ip`` must be used in more than module
in the
VNF, the parameter values must be defined as output values in the base module
with
output names: ``{vm-type}_{network-role}_shared_vip`` or
``{vm-type}_{network-role}_v6_shared_vip``.


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
``allowed_address_pairs`` in the ``OS::Neutron::Port``, it should be as
follows:

.. code-block:: yaml

  allowed_address_pairs: [ { "ip_address": {get_param:
  {vm-type}_{network-role}_shared_vip }}, { "ip_address": {get_param:
  {vm-type}_{network-role}_v6_shared_vip }}]

Reserve Port Concept
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A "Reserve Port" is an ``OS::Neutron::Port`` that ``fixed_ips``, ip_address
property is assigned one or more IP addresses that are used as Virtual
IP (VIP) Addresses (i.e., allowed_address_pairs) on other ports.

A "Reserve Port" is never attached to a Virtual Machine
(``OS::Nova::Server``). The reserve port ensures that the intended
``allowed_address_pair`` IP address is not inadvertently assigned as a
fixed_ips to a ``OS::Neutron::Port`` that is attached ``OS::Nova::Server`` and
thus causing routing issues.

A VNF may have one or more "Reserve Ports". A reserve port maybe created
in the base module or an incremental module. If created in the base
module, parameters may be defined in the outputs: section of the base
template so the IP Address assigned to the reserve port maybe assigned
to the allowed_address_pair property of an ``OS::Neutron::Port`` in one or
more incremental modules.

The parameter name of the IP address used in the "Reserve Port" depends
on the ``allowed_address_pair`` "option" utilized by the VNF.

When creating a Reserve Port, if only one allowed_address_pair is configured
on a port, then the parameter name depends upon the IP addresses type
(IPv4 or IPv6) and network type (internal or external).
The valid parameter names are:

  * ``{vm-type}_{network-role}_floating_ip``
  * ``{vm-type}_{network-role}_floating_v6_ip``
  * ``{vm-type}_int_{network-role}_floating_ip``
  * ``{vm-type}_int_{network-role}_floating_v6_ip``

When creating a Reserve Port, if more than one (e.g., multiple)
``allowed_address_pair`` is configured on a port, then the parameter name
depends
upon the IP addresses type (IPv4 or IPv6) and network type
(internal or external) and the option being used.  The valid parameter
names are:

  * ``{vm-type}_{network-role}_ip_{index}``
  * ``{vm-type}_{network-role}_ips``
  * ``{vm-type}_{network-role}_v6_ip_{index}``
  * ``{vm-type}_{network-role}_v6_ips``
  * ``{vm-type}_{network-role}_vip_{index}``
  * ``{vm-type}_{network-role}_vips``
  * ``{vm-type}_{network-role}_v6_vip_{index}``
  * ``{vm-type}_{network-role}_v6_vips``
  * ``{vm-type}_{network-role}_{vip-type}_vip``
  * ``{vm-type}_{network-role}_v6_{vip-type}_vip``
  * ``{vm-type}_{network-role}_{vip-type}_vips``
  * ``{vm-type}_{network-role}_v6_{vip-type}_vips``


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
