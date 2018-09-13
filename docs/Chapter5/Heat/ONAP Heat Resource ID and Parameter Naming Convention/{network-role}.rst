.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

{network-role}
-----------------------------

The assignment of a {network-role} is discussed in
:ref:`ONAP Heat Networking`.

.. req::
    :id: R-21330
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource property parameter that is
    associated with external network **MUST** include the ``{network-role}``
    as part of the parameter name.

.. req::
    :id: R-11168
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource ID that is associated with
    an external network **MUST** include the ``{network-role}`` as part
    of the resource ID.

.. req::
    :id: R-84322
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource property parameter that
    is associated with an internal network **MUST** include
    ``int_{network-role}`` as part of the parameter name,
    where ``int_`` is a hard coded string.

.. req::
    :id: R-96983
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource ID that is associated
    with an internal network **MUST** include ``int_{network-role}`` as part
    of the Resource ID, where ``int_`` is a hard coded string.

.. req::
    :id: R-26506
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's ``{network-role}`` **MUST** contain
    only alphanumeric characters and/or underscores '_' and
    **MUST NOT** contain any of the following strings:
    ``_int`` or ``int_`` or ``_int_``.

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
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's use of ``{network-role}``
    in all Resource property parameter names **MUST** be the same case.

.. req::
    :id: R-21511
    :target: VNF
    :keyword: MUST
    :validation_mode: static
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
