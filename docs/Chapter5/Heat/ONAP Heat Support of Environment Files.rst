.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

.. _ONAP Heat Support of Environment Files:

ONAP Heat Support of Environment Files
--------------------------------------


.. req::
    :id: R-599443
    :target: VNF
    :keyword: MUST
    :introduced: dublin
    :validation_mode: static

    A parameter enumerated in a
    VNF's Heat Orchestration Template's environment file **MUST** be declared
    in the
    corresponding VNF's Heat Orchestration Template's YAML file's
    ``parameters:`` section.

Note that this is an ONAP requirement.  This is not required by OpenStack.
