.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

.. _ONAP Heat Networking:

ONAP Heat Networking
-----------------------

ONAP defines two types of networks: External Networks and Internal Networks.

External Networks
^^^^^^^^^^^^^^^^^^^^

ONAP defines an external network in relation to the VNF and not with regard
to the Network Cloud site. External networks may also be referred to as
"inter-VNF" networks.  An external network must connect VMs in a VNF to
VMs in another VNF or an external gateway or external router.

An External Network may be a Neutron Network or a Contrail Network.


.. req::
    :id: R-16968
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static

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
    :validation_mode: static

    A VNF's port connected to an external network **MUST**
    use the port for the purpose of reaching
    VMs in another VNF and/or an external gateway and/or external router.
    A VNF's port connected to an external network **MAY**
    use the port for the purpose of reaching VMs in the same VNF.

.. req::
    :id: R-69014
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    When a VNF connects to an external network, a network role, referred to
    as the ``{network-role}`` **MUST** be assigned to the external network for
    use in the VNF's Heat Orchestration Template.

.. req::
    :id: R-05201
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    When a VNF connects to two or more external networks, each external
    network **MUST** be assigned a unique ``{network-role}``
    in the context of the VNF for use in the VNF's Heat Orchestration
    Template.

.. req::
    :id: R-83015
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's ``{network-role}`` assigned to an external network **MUST**
    be different than the ``{network-role}`` assigned to the VNF's
    internal networks, if internal networks exist.

.. req::
    :id: R-99794
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    An external network **MUST** have one subnet. An external network
    **MAY** have more than one subnet.

Note that this document refers to ``{network-role}`` which in reality
is the ``{network-role-tag}``.  The value of the
``{network-role}`` / ``{network-role-tag}``
is determined by the designer of the VNF's Heat Orchestration Template and
there is no requirement for ``{network-role}`` / ``{network-role-tag}``
uniqueness across Heat Orchestration Templates for
different VNFs.

When an external network is created by ONAP, the network is assigned a
``{network-role}``.  The ``{network-role}`` of the network is not required to
match the ``{network-role}`` of the VNF Heat Orchestration Template.

For example, the VNF Heat Orchestration Template can assign a
``{network-role}``
of ``oam`` to a network which attaches to an external network with a
``{network-role}`` of ``oam_protected_1`` .

When the Heat Orchestration Template is on-boarded into ONAP
  * each ``{network-role}`` value in the Heat Orchestration Template
    is mapped to the ``{network-role-tag}`` in the ONAP
    data structure.
  * each ``OS::Neutron::Port`` is associated with the external network it is
    connecting to, thus creating the VNF Heat Orchestration Template
    ``{network-role}`` / ``{network-role-tag}``
    to external network ``{network-role}`` mapping.

ONAP enforces a naming convention for parameters associated with
external networks. :ref:`ONAP Heat Resource ID and Parameter Naming Convention`
provides additional details.

Internal Networks
^^^^^^^^^^^^^^^^^^^^

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
    :validation_mode: static

    If a VNF has an internal network, the VNF Heat Orchestration Template
    **MUST** include the heat resources to create the internal network.

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
    :validation_mode: static

    A VNF's port connected to an internal network **MUST**
    use the port for the purpose of reaching VMs in the same VNF.

.. req::
    :id: R-46461
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static

    A VNF's port connected to an internal network **MUST NOT** connect
    the port to VMs in another VNF and/or an external gateway and/or
    external router.

.. req::
    :id: R-68936
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    When a VNF creates an internal network, a network role, referred to as
    the ``{network-role}`` **MUST** be assigned to the internal network
    for use in the VNF's Heat Orchestration Template.

.. req::
    :id: R-32025
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    When a VNF creates two or more internal networks, each internal
    network **MUST** be assigned a unique ``{network-role}`` in the context
    of the VNF for use in the VNF's Heat Orchestration Template.

.. req::
    :id: R-69874
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's ``{network-role}`` assigned to an internal network **MUST**
    be different than the ``{network-role}`` assigned to the VNF's external
    networks.

.. req::
    :id: R-16241
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's internal network **MUST** have one subnet.
    A VNF's internal network **MAY** have more than one subnet.

.. req::
    :id: R-22688
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    If a VNF's port is connected to an internal network and the port is
    created in an Incremental Module and the internal network is created
    in the Base Module then the UUID of the internal network **MUST** be
    exposed as a parameter in the ``outputs:`` section of the Base Module
    and the port resource **MUST** use a ``get_param`` to obtain the network
    UUID.

ONAP does not programmatically enforce a naming convention for
parameters for internal network. However, a naming convention is
provided that must be followed.
:ref:`ONAP Heat Resource ID and Parameter Naming Convention`
provides additional details.

