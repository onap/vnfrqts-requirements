.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

.. _ONAP Heat Support of Environment Files:

ONAP Heat Support of Environment Files
-----------------------------------------

The use of an environment file in OpenStack is optional.  In ONAP, it is
mandatory. A Heat Orchestration Template uploaded to ONAP must have a
corresponding environment file, even if no parameters are required to
be enumerated.

(Note that ONAP does not programmatically enforce the use of
an environment file.)

.. req::
    :id: R-67205
    :target: VNF
    :keyword: MUST

    The VNF Heat Orchestration Template **MUST** have a corresponding
    environment file for a Base Module.

.. req::
    :id: R-35727
    :target: VNF
    :keyword: MUST

    The VNF Heat Orchestration Template **MUST** have a
    corresponding environment file for an Incremental module.

.. req::
    :id: R-22656
    :target: VNF
    :keyword: MUST

    The VNF Heat Orchestration Template **MUST** have a
    corresponding environment file for a Cinder Volume Module.

A nested heat template must not have an environment file; OpenStack does
not support it.

The environment file must contain parameter values for the ONAP
Orchestration Constants and VNF Orchestration Constants. These
parameters are identical across all instances of a VNF type, and
expected to change infrequently. The ONAP Orchestration Constants are
associated with OS::Nova::Server image and flavor properties (See
:ref:`Property image` and :ref:`Property flavor`). Examples of VNF
Orchestration Constants are the networking parameters associated
with an internal network (e.g., private IP ranges) and Cinder
volume sizes.

The environment file must not contain parameter values for parameters
that are instance specific (ONAP Orchestration Parameters, VNF
Orchestration Parameters). These parameters are supplied to the Heat by
ONAP at orchestration time.

SDC Treatment of Environment Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parameter values enumerated in the environment file are used by SDC as
the default value. However, the SDC user may use the SDC GUI to
overwrite the default values in the environment file.

SDC generates a new environment file for distribution to SO based on
the uploaded environment file and the user provided GUI updates. The
user uploaded environment file is discarded when the new file is
created. Note that if the user did not change any values via GUI
updates, the SDC generated environment file will contain the same values
as the uploaded file.

Use of Environment Files when using OpenStack "heat stack-create" CLI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When ONAP is instantiating the Heat Orchestration Template, certain
parameter must not be enumerated in the environment file. This document
provides the details of what parameters should not be enumerated.

If the Heat Orchestration Template is to be instantiated from the
OpenStack Command Line Interface (CLI) using the command "heat
stack-create", all parameters must be enumerated in the environment
file.

