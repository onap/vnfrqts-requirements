.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

.. _General Guidelines for Heat:

General Guidelines for Heat
---------------------------

This section contains general Heat Orchestration Template guidelines
and requirements.

Heat Template Compliance
^^^^^^^^^^^^^^^^^^^^^^^^

The Heat Orchestration Template requirements with RFC 2119
keywords **MUST** and **MUST NOT** can be validated against a set of Heat
Templates via the VNF Validation Program (VVP).

**NOTE**: Not all requirements are currently testable via VVP.

The VVP *validation scripts* project contains python validation
scripts that will parse Heat Orchestration Templates in a given directory
to ensure that they comply with ONAP Heat Orchestration Template requirements.

For instructions on how to use the VVP validation scripts,
please see the validation scripts
`README <https://github.com/onap/vvp-validation-scripts>`__


YAML Format
^^^^^^^^^^^

.. req::
    :id: R-95303
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's Heat Orchestration Template **MUST** be defined using valid YAML.

YAML (YAML Ain't
Markup Language) is a human friendly data serialization standard for all
programming languages. See http://www.yaml.org/.

YAML rules include:

 - Tabs are not allowed, use spaces ONLY
 - You must indent your properties and lists with 1 or more spaces
 - All Resource IDs and resource property parameters are case-sensitive.
   (e.g., "ThIs", is not the same as "thiS")
