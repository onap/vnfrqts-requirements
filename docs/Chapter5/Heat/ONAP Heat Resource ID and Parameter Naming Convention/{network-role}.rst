.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

{network-role}
-----------------------------

.. req::
    :id: R-69014
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    When a VNF's port connects to an internal network or external network,
    a network role, referred to
    as the ``{network-role}`` **MUST** be assigned to the network for
    use in the VNF's Heat Orchestration Template.  The ``{network-role}``
    is used in the VNF's Heat Orchestration Template resource IDs
    and resource property parameter names.

.. req::
    :id: R-05201
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    When a VNF connects to two or more unique networks, each
    network **MUST** be assigned a unique ``{network-role}``
    in the context of the VNF for use in the VNF's Heat Orchestration
    Template.

.. req::
    :id: R-21330
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource property parameter that is
    associated with external network **MUST** include the ``{network-role}``
    as part of the parameter name.

.. req::
    :id: R-11168
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource ID that is associated with
    an external network **MUST** include the ``{network-role}`` as part
    of the resource ID.

.. req::
    :id: R-84322
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource property parameter that
    is associated with an internal network **MUST** include
    ``int_{network-role}`` as part of the parameter name,
    where ``int_`` is a hard coded string.

.. req::
    :id: R-96983
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource ID that is associated
    with an internal network **MUST** include ``int_{network-role}`` as part
    of the Resource ID, where ``int_`` is a hard coded string.

.. req::
    :id: R-26506
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: dublin

    A VNF's Heat Orchestration Template's ``{network-role}`` **MUST** contain
    only alphanumeric characters and/or underscores '_' and

    * **MUST NOT** contain any of the following strings: ``_int`` or ``int_``
      or ``_int_``
    * **MUST NOT** end in the string: ``_v6``
    * **MUST NOT** contain the strings ``_#_``,  where ``#`` is a number
    * **MUST NOT** end in the string: ``_#``, where ``#`` is a number


.. req::
    :id: R-00977
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's ``{network-role}``
    **MUST NOT** be a substring of ``{vm-type}``.

For example, if a VNF has a '{vm-type}' of 'oam' and a
'{network-role}' of 'oam\_protected' would be a violation of the requirement.


.. req::
    :id: R-58424
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    A VNF's Heat Orchestration Template's use of ``{network-role}``
    in all Resource property parameter names **MUST** be the same case.

.. req::
    :id: R-21511
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    A VNF's Heat Orchestration Template's use of ``{network-role}``
    in all Resource IDs **MUST** be the same case.

.. req::
    :id: R-86588
    :target: VNF
    :keyword: SHOULD
    :updated: casablanca

    A VNF's Heat Orchestration Template's ``{network-role}`` case in Resource
    property parameter names **SHOULD** match the case of ``{network-role}``
    in Resource IDs and vice versa.


Note that this document refers to ``{network-role}`` which in reality
is the ``{network-role-tag}``.  The value of the
``{network-role}`` / ``{network-role-tag}``
is determined by the designer of the VNF's Heat Orchestration Template and
there is no requirement for ``{network-role}`` / ``{network-role-tag}``
uniqueness across Heat Orchestration Templates for
different VNFs.

When an external network is created by ONAP, the network is also assigned a
``{network-role}``.  The ``{network-role}`` of the network is not required to
match the ``{network-role}`` of the VNF Heat Orchestration Template.

For example, the VNF Heat Orchestration Template can assign a
``{network-role}``
of ``oam`` to a network which attaches to an external network with a
``{network-role}`` of ``oam_protected`` .

When the Heat Orchestration Template is on-boarded into ONAP
  * each ``{network-role}`` value in the Heat Orchestration Template
    is mapped to the ``{network-role-tag}`` in the ONAP
    data structure.
  * each ``OS::Neutron::Port`` is associated with the external network it is
    connecting to, thus creating the VNF Heat Orchestration Template
    ``{network-role}`` / ``{network-role-tag}``
    to external network ``{network-role}`` mapping.
