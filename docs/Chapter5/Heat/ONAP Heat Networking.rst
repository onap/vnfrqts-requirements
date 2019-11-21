.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

.. _ONAP Heat Networking:

ONAP Heat Networking
-----------------------

ONAP defines two types of networks: External Networks and Internal Networks.

External Networks
^^^^^^^^^^^^^^^^^^^^

An ONAP external network is created by using VID.
External networks are orchestrated separately, independent of VNFs.
A network instantiated via VID is managed by ONAP and is inventoried
in AAI.

An external network can be created by using one of the following
resources:

- ``OS::Neutron::Net``
- ``OS::Neutron::ProviderNet``
- ``OS::ContrailV2::VirtualNetwork``

An external network **MAY** be used to

- Connect a VM in a VNF to VMs in another VNF
- Connect a VM in a VNF to an external gateway or external router
- Connect a VM in a VNF to other VMs in the same VNF

An external network may be designed to perform

- All three functions listed above or
- Perform only two functions listed above or
- Perform only one function listed above

.. req::
    :id: R-16968
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: frankfurt

    A VNF's Heat Orchestration Templates **MUST NOT** include heat
    resources to create external networks.

    A external network **MUST** be instantiated using VID.


.. req::
    :id: R-00606
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF **MAY** be connected to zero, one or more than one external
    network.

.. req::
    :id: R-57424
    :target: VNF
    :keyword: MAY
    :validation_mode: none
    :updated: frankfurt

    A VNF's port connected to an external network **MAY**
    use the port for the purpose of reaching
    VMs in another VNF and/or an external gateway and/or external router.
    A VNF's port connected to an external network **MAY**
    use the port for the purpose of reaching VMs in the same VNF.

    - Connecting a VM in the VNF to VMs in another VNF and/or
    - Connecting a VM in the VNF to an external gateway or external router
      and/or
    - Connecting a VM the VNF to other VMs in the same VNF

.. req::
    :id: R-99794
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    An external network **MUST** have one subnet. An external network
    **MAY** have more than one subnet.

ONAP enforces a naming convention for
resource IDs and resource property
parameters associated with
external networks. :ref:`ONAP Heat Resource ID and Parameter Naming Convention`
provides additional details.

Internal Networks
^^^^^^^^^^^^^^^^^^^^

An ONAP internal network is created by the VNF's Heat Orchestration Template.
That is, the VNF's Heat Orchestration Template contains the heat resources to
instantiate the network.
Am internal network is not inventoried by AAI and can not be managed
independently of the VNF.

An ONAP internal network MUST only be used for connecting a VM the
VNF to other VMs in the same VNF.

An ONAP internal network MUST NOT be used for connecting a VM in the VNF to
VMs in another VNF or connecting a VM in the VNF to an external gateway and/or
external router.

.. req::
    :id: R-87096
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF **MAY** contain zero, one or more than one internal network.

.. req::
    :id: R-35666
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: frankfurt

    If a VNF has an internal network, the VNF Heat Orchestration Template
    **MUST** include the heat resources to create the internal network.

    A VNF's Internal Network is created using Neutron Heat Resources
    (i.e., ``OS::Neutron::Net``, ``OS::Neutron::Subnet``,
    ``OS::Neutron::ProviderNet``) and/or
    Contrail Heat Resources (i.e., ``OS::ContrailV2::VirtualNetwork``,
    ``ContrailV2::NetworkIpam``).


.. req::
    :id: R-52425
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    A VNF's port connected to an internal network **MUST**
    use the port for the purpose of reaching VMs in the same VNF.

.. req::
    :id: R-46461
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: none
    :updated: casablanca

    A VNF's port connected to an internal network **MUST NOT** use the port
    for the purpose of reaching VMs in another VNF and/or an
    external gateway and/or
    external router.

.. req::
    :id: R-16241
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's internal network **MUST** have one subnet.
    A VNF's internal network **MAY** have more than one subnet.

.. req::
    :id: R-86972
    :target: VNF
    :keyword: SHOULD
    :updated: casablanca

    A VNF **SHOULD** create the internal network in the VNF's Heat
    Orchestration Template Base Module.


.. req::
    :id: R-22688
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: dublin

    When a VNF's Heat Orchestration Template creates an internal network
    (per the ONAP definition, see Requirements R-52425 and R-46461
    and R-35666) and the internal network needs to be shared between modules
    within a VNF,  the internal network **MUST** be created either in the

    * the base module
    * a nested YAML file invoked by the base module

    and the base module **MUST** contain an output parameter that provides
    either the network UUID or network name.

    * If the network UUID value is used to reference the network, the output
      parameter name in the base module **MUST** follow the naming convention
      ``int_{network-role}_net_id``
    * If the network name in is used to reference the network, the output
      parameter name in the base template **MUST** follow the naming convention
      ``int_{network-role}_net_name``

    ``{network-role}`` **MUST** be the network-role of the internal network
    created in the Base Module.

    The Base Module Output Parameter MUST be declared in the ``parameters:``
    section of the Incremental Module(s) where the ``OS::Neutron::Port``
    resource(s) is attaching to the internal network.

ONAP does not programmatically enforce a naming convention for
parameters for internal network. However, a naming convention is
provided that must be followed.
:ref:`ONAP Heat Resource ID and Parameter Naming Convention`
provides additional details.

