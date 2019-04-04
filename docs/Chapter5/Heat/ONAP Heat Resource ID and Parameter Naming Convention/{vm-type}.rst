.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.


{vm-type}
-----------------


.. req::
    :id: R-01455
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    When a VNF's Heat Orchestration Template creates a Virtual Machine
    (i.e., ``OS::Nova::Server``),
    each "class" of VMs **MUST** be assigned a VNF unique
    ``{vm-type}``; where "class" defines VMs that
    **MUST** have the following identical characteristics:

      1.) ``OS::Nova::Server`` resource property ``flavor`` value

      2.) ``OS::Nova::Server`` resource property ``image`` value

      3.) Cinder Volume attachments

        - Each VM in the "class" **MUST** have the identical Cinder Volume
          configuration

      4.) Network attachments and IP address requirements

        - Each VM in the "class" **MUST** have the identical number of
          ports connecting to the identical networks and requiring the identical
          IP address configuration.

The ``{vm-type}`` will be used in a VNF's Heat Orchestration Template's

* Resource IDs
* Resource property parameter names

A VNF's Heat Orchestration Template's Resource property parameter that is
associated with a unique Virtual Machine type **MUST** include
``{vm-type}`` as part of the parameter name with two exceptions:

1.) The Resource ``OS::Nova::Server`` property ``availability_zone``
parameter **MUST NOT** be prefixed with a common ``{vm-type}`` identifier,

2.) The Resource ``OS::Nova::Server`` mandatory and optional
``metadata`` parameters

 * ``vnf_name``
 * ``vnf_id``
 * ``vf_module_id``
 * ``vf_module_name``
 * ``vf_module_index``
 * ``environment_context``
 * ``workload_context``

**MUST NOT** be prefixed with a common ``{vm-type}`` identifier.

Requirements for specific resource property parameter names can be
found in later sections of this document.


.. req::
    :id: R-98407
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's ``{vm-type}`` **MUST** contain only
    alphanumeric characters and/or underscores '_' and **MUST NOT**
    contain any of the following strings:
    ``_int`` or ``int_`` or ``_int_``.

.. req::
    :id: R-48067
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's ``{vm-type}`` **MUST NOT** be a
    substring
    of ``{network-role}``.

It may cause the VNF Validation Program validation-scripts project
to produce erroneous error messages.


.. req::
    :id: R-32394
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's use of ``{vm-type}`` in all Resource
    property parameter names **MUST** be the same case.

.. req::
    :id: R-46839
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's use of ``{vm-type}``
    in all Resource IDs **MUST** be the same case.

.. req::
    :id: R-36687
    :target: VNF
    :keyword: SHOULD
    :updated: casablanca

    A VNF's Heat Orchestration Template's  ``{vm-type}`` case in Resource
    property parameter names **SHOULD** match the case of ``{vm-type}``
    in Resource IDs and vice versa.
