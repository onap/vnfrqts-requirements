.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

.. _ONAP Heat Orchestration Templates Overview:

ONAP Heat Orchestration Templates Overview
-----------------------------------------------

ONAP supports a modular Heat Orchestration Template design pattern,
referred to as *VNF Modularity.*

.. _heat_onap_vnf_modularity_overview:

ONAP VNF Modularity Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. req::
    :id: R-69663
    :target: VNF
    :keyword: MAY

    A VNF **MAY** be composed from one or more Heat Orchestration
    Templates, each of which represents a subset of the overall VNF.

The Heat Orchestration Templates can be thought of a components or modules of
the VNF and are referred to as *VNF Modules*. During orchestration,
these modules are
deployed incrementally to create the complete VNF.


.. req::
    :id: R-33132
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template **MAY** be
     1.) Base Module Heat Orchestration Template (also referred to as a
         Base Module),
     2.) Incremental Module Heat Orchestration Template (referred to as
         an Incremental Module), or
     3.) a Cinder Volume Module Heat Orchestration Template (referred to as
         Cinder Volume  Module).

.. req::
    :id: R-37028
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF **MUST** be composed of one Base Module

.. req::
    :id: R-13196
    :target: VNF
    :keyword: MAY

    A VNF **MAY** be composed of zero to many Incremental Modules.

.. req::
    :id: R-28980
    :target: VNF
    :keyword: MAY

    A VNF's incremental module **MAY** be used for initial VNF deployment only.

.. req::
    :id: R-86926
    :target: VNF
    :keyword: MAY

    A VNF's incremental module **MAY** be used for scale out only.

A VNF's Incremental Module that is used for scale out is deployed sometime
after initial VNF deployment to add capacity.


.. req::
    :id: R-91497
    :target: VNF
    :keyword: MAY

    A VNF's incremental module **MAY** be used for both deployment and
    scale out.

.. req::
    :id: R-68122
    :target: VNF
    :keyword: MAY

    A VNF's incremental module **MAY** be deployed more than once,
    either during initial VNF deployment and/or scale out.

.. req::
    :id: R-46119
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's Resource ``OS::Cinder::Volume``
    **MAY** be defined in a Base Module.

.. req::
    :id: R-90748
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's Resource ``OS::Cinder::Volume``
    **MAY** be defined in an Incremental Module.

.. req::
    :id: R-03251
    :target: VNF
    :keyword: MAY

    A VNF's Heat Orchestration Template's Resource ``OS::Cinder::Volume``
    **MAY** be defined in a Cinder Volume Module.

ONAP also supports the concept of an optional, independently deployed Cinder
volume via a separate Heat Orchestration Templates, referred to as a Cinder
Volume Module. This allows the volume to persist after a Virtual Machine
(VM) (i.e., OS::Nova::Server) is deleted, allowing the volume to be reused
on another instance (e.g., during a fail over activity).

.. req::
    :id: R-11200
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Cinder Volume Module, when it exists, **MUST** be 1:1
    with a Base module or Incremental module.

It is strongly recommended that Cinder Volumes be created in a Cinder Volume
Module.

.. req::
    :id: R-38474
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Base Module **MUST** have a corresponding Environment File.

.. req::
    :id: R-81725
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Incremental Module **MUST** have a corresponding Environment File

.. req::
    :id: R-53433
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Cinder Volume Module **MUST** have a corresponding environment file

These concepts will be described in more detail throughout the document.
This overview is provided to set the stage and help clarify the concepts
that will be introduced.

Nested Heat Orchestration Templates Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP supports nested Heat Orchestration Templates per OpenStack
specifications.


.. req::
    :id: R-36582
    :target: VNF
    :keyword: MAY

    A VNF's Base Module **MAY** utilize nested heat.

.. req::
    :id: R-56721
    :target: VNF
    :keyword: MAY

    A VNF's Incremental Module **MAY** utilize nested heat.

.. req::
    :id: R-30395
    :target: VNF
    :keyword: MAY

    A VNF's Cinder Volume Module **MAY** utilize nested heat.

Nested templates may be suitable for larger VNFs that contain many
repeated instances of the same VM type(s). A common usage pattern is to
create a nested template for each VM type along with its supporting
resources. The Heat Orchestration Template may then reference these
nested templates either statically (by repeated definition) or
dynamically (via OS::Heat::ResourceGroup).

See :ref:`Nested Heat Templates` for additional details.

ONAP Heat Orchestration Template Filenames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to enable ONAP to understand the relationship between Heat
files, the following Heat file naming convention must be utilized.

In the examples below, <text> represents any alphanumeric string that
must not contain any special characters and must not contain the word
"base".


.. req::
    :id: R-87485
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's Heat Orchestration Template's file extension **MUST**
    be in the lower case format ``.yaml`` or ``.yml``.

.. req::
    :id: R-56438
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's Heat Orchestration Template's Nested YAML file extension **MUST**
    be in the lower case format ``.yaml`` or ``.yml``.

.. req::
    :id: R-74304
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's Heat Orchestration Template's Environment file extension **MUST**
    be in the lower case format ``.env``.

.. req::
    :id: R-99646
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF's YAML files (i.e, Heat Orchestration Template files and
    Nested files) **MUST** have a unique name in the scope of the VNF.

Base Modules
~~~~~~~~~~~~


.. req::
    :id: R-81339
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF Heat Orchestration Template's Base Module file name **MUST** include
    case insensitive 'base' in the filename and
    **MUST** match one of the following four
    formats:

     1.) ``base_<text>.y[a]ml``

     2.) ``<text>_base.y[a]ml``

     3.) ``base.y[a]ml``

     4.) ``<text>_base_<text>``.y[a]ml

    where ``<text>`` **MUST** contain only alphanumeric characters and
    underscores '_' and **MUST NOT** contain the case insensitive word ``base``.

.. req::
    :id: R-91342
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF Heat Orchestration Template's Base Module's Environment File
    **MUST** be named identical to the VNF Heat Orchestration Template's
    Base Module with ``.y[a]ml`` replaced with ``.env``.

Incremental Modules
~~~~~~~~~~~~~~~~~~~


.. req::
    :id: R-87247
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    VNF Heat Orchestration Template's Incremental Module file name
    **MUST** contain only alphanumeric characters and underscores
    '_' and **MUST NOT** contain the case insensitive word ``base``.

.. req::
    :id: R-94509
    :target: VNF
    :keyword: MUST
    :validation_mode: static

    A VNF Heat Orchestration Template's Incremental Module's Environment File
    **MUST** be named identical to the VNF Heat Orchestration Template's
    Incremental Module with ``.y[a]ml`` replaced with ``.env``.

To clearly identify the incremental module, it is recommended to use the
following naming options for modules:

 -  ``module_<text>.y[a]ml``

 -  ``<text>_module.y[a]ml``

 -  ``module.y[a]ml``

 -  ``<text>_module_<text>.y[a]ml``

Cinder Volume Modules
~~~~~~~~~~~~~~~~~~~~~


.. req::
    :id: R-82732
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF Heat Orchestration Template's Cinder Volume Module **MUST**
    be named identical to the base or incremental module it is supporting with
    ``_volume`` appended.


.. req::
    :id: R-589037
    :keyword: MUST
    :validation_mode: static
    :introduced: dublin

    A VNF Heat Orchestration Template's Cinder Volume Module resources section
    **MUST** only be defined using one of the following:

    * one of more ``OS::Cinder::Volume`` resources
    * one or more ``OS::Heat::ResourceGroup`` resources that call a nested YAML
      file that contains only ``OS::Cinder::Volume`` resources
    * a resource that calls a nested YAML file (static nesting) that contains
      only ``OS::Cinder::Volume`` resources

.. req::
    :id: R-31141
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    VNF Heat Orchestration Template's Cinder Volume Module's Environment File
    **MUST** be named identical to the VNF Heat Orchestration Template's
    Cinder Volume Module with ``.y[a]ml`` replaced with ``.env``.

Nested Heat file
~~~~~~~~~~~~~~~~


.. req::
    :id: R-76057
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    VNF Heat Orchestration Template's Nested YAML file name **MUST** contain
    only alphanumeric characters and underscores '_' and
    **MUST NOT** contain the case insensitive word ``base``.

.. req::
    :id: R-70276
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static

    A VNF HEAT's Orchestration Nested Template's YAML file name **MUST NOT**
    be in the format ``{vm-type}.y[a]ml`` where ``{vm-type}`` is defined
    in the Heat Orchestration Template.

Examples include

 -  ``<text>.y[a]ml``

 -  ``nest_<text>.y[a]ml``

 -  ``<text>_nest.y[a]ml``

 -  ``nest.y[a]ml``

 -  ``<text>_nest_<text>.y[a]ml``

VNF Heat Orchestration Template's Nested YAML file does not have a
corresponding environment files, per OpenStack specifications.

.. _Output Parameters:

Output Parameters
^^^^^^^^^^^^^^^^^^^^^^

The output parameters are parameters defined in the output section of a
Heat Orchestration Template. The ONAP output parameters are subdivided
into three categories:

1. ONAP Base Module Output Parameters

2. ONAP Volume Module Output Parameters

3. ONAP Predefined Output Parameters.

ONAP Base Module Output Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP Base Module Output Parameters are declared in the ``outputs:`` section
of the VNF's Heat Orchestration Template's Base Module. A Base Module Output
Parameter is available as an input parameter (i.e., declared in
the ``parameters:`` section) to all Incremental Modules in the VNF.

A Base Module Output Parameter may be used as an input parameter in any
incremental module in the VNF.  Note that the parameter is not available to
other VNFs.


.. req::
    :id: R-52753
    :target: VNF
    :keyword: MUST
    :validation_mode: none

    VNF's Heat Orchestration Template's Base Module's output parameter's
    name and type **MUST** match the VNF's Heat Orchestration Template's
    incremental Module's name and type.

.. req::
    :id: R-22608
    :target: VNF
    :keyword: SHOULD NOT
    :validation_mode: static

    When a VNF's Heat Orchestration Template's Base Module's output
    parameter is declared as an input parameter in an Incremental Module,
    the parameter attribute ``constraints:`` **SHOULD NOT** be declared.

Additional details on ONAP Base Module Output Parameters are provided in
:ref:`ONAP Output Parameter Names` and ONAP VNF Modularity.

ONAP Volume Module Output Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. req::
    :id: R-89913
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's Cinder Volume Module Output
    Parameter(s)
    **MUST** include the
    UUID(s) of the Cinder Volumes created in template.

A VNF's Heat Orchestration Template's Cinder Volume Module Output Parameter(s)
are only available for the module (base or incremental) that the volume
template is associated with.


.. req::
    :id: R-07443
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Templates' Cinder Volume Module Output
    Parameter's name and type **MUST** match the input parameter name and type
    in the corresponding Base Module or Incremental Module.

.. req::
    :id: R-20547
    :target: VNF
    :keyword: SHOULD NOT
    :validation_mode: static

    When an ONAP Volume Module Output Parameter is declared as an input
    parameter in a base or an incremental module Heat Orchestration
    Template, parameter constraints **SHOULD NOT** be declared.

Additional details on ONAP Base Module Output Parameters are provided in
:ref:`ONAP Output Parameter Names` and :ref:`ONAP Heat Cinder Volumes`.

ONAP Predefined Output Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ONAP will look for a small set of pre-defined Heat output parameters to
capture resource attributes for inventory in ONAP. These output parameters
are optional and currently only two parameters are supported. These output
parameters are optional and are specified in
:ref:`OAM Management IP Addresses`.

Support of heat stack update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP does not support the use of heat stack-update command for scaling
(growth/de-growth).


.. req::
    :id: R-39349
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: none

    A VNF Heat Orchestration Template **MUST NOT** be designed to utilize the
    OpenStack ``heat stack-update`` command for scaling (growth/de-growth).

.. req::
    :id: R-43413
    :target: VNF
    :keyword: MUST
    :validation_mode: none

    A VNF **MUST** utilize a modular Heat Orchestration Template design to
    support scaling (growth/de-growth).

It is important to note that ONAP only supports heat stack-update for
image upgrades.

Scope of a Heat Orchestration Template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. req::
    :id: R-59482
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: none

    A VNF's Heat Orchestration Template **MUST NOT** be VNF instance
    specific or cloud site specific.

ONAP provides the instance specific parameter values to the Heat
Orchestration Template at orchestration time.


.. req::
    :id: R-01896
    :target: VNF
    :keyword: MUST
    :validation_mode: none

    A VNF's Heat Orchestration Template's parameter values that are constant
    across all deployments **MUST** be declared in a Heat Orchestration
    Template Environment File.

ONAP VNF On-Boarding
^^^^^^^^^^^^^^^^^^^^

.. req::
    :id: R-511776
    :keyword: MUST
    :validation_mode: static

    When a VNF's Heat Orchestration Template is ready
    to be on-boarded to ONAP,
    all files composing the VNF Heat Orchestration Template
    **MUST** be placed in a flat (i.e., non-hierarchical) directory and
    archived using ZIP.  The resulting ZIP file is uploaded into ONAP.

The VNF's Heat Orchestration Template's ZIP file must include
the base module YAML file (R-37028) and corresponding environment file
(R-38474).

The VNF's Heat Orchestration Template's ZIP file **MAY** include

* One or more incremental module YAML files (R-13196) and corresponding
  environment files (R-81725).
* One or more volume module YAML files (R-03251) and corresponding
  environment files (R-53433).
* One or more nested YAML files (R-36582, R-56721, R-30395).
* One or more files that are retrieved via the intrinsic function
  ``get_file``.  The ``get_file`` function returns the content of a file
  into a Heat Orchestration Template. It is generally used as a file
  inclusion mechanism for files containing scripts or configuration files.
  (See Section 9.3)

.. req::
    :id: R-348813
    :keyword: MUST
    :validation_mode: static

    The VNF's Heat Orchestration Template's ZIP file **MUST NOT** include
    a binary image file.

