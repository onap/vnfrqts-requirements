.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

.. _ONAP Heat Cinder Volumes:

ONAP Heat Cinder Volumes
----------------------------

Cinder Volumes are created with the heat resource OS::Cinder::Volume.

As stated in :need:`R-46119`, :need:`R-90748`, :need:`R-03251`, a
VNF's Heat Orchestration Template's Resource ``OS::Cinder::Volume``
**MAY** be defined in a Base Module, Incremental Module, or Cinder
Volume Module.

ONAP supports the independent deployment of a Cinder volume via separate
Heat Orchestration Templates, the Cinder Volume module. This allows the
volume to persist after VNF deletion so that they can be reused on
another instance (e.g., during a failover activity).

A Base Module or Incremental Module may have a corresponding volume
module. Use of separate volume modules is optional. A Cinder volume may
be embedded within the Base Module or Incremental Module if persistence
is not required.

If a VNF Base Module or Incremental Module has an independent volume
module, the scope of volume templates must be 1:1 with Base module or
Incremental module. A single volume module must create only the volumes
required by a single Incremental module or Base module.

As stated in :need:`R-11200`, a VNF's Cinder Volume Module, when it exists,
**MUST** be 1:1 with a Base module or Incremental module.  That is,
A single volume module must create only the volumes required by a
single Incremental module or Base module.

As stated in :need:`R-30395`, a VNF's Cinder Volume Module **MAY** utilize
nested heat.

As stated in :need:`R-89913`, a VNF's Heat Orchestration Template's Cinder
Volume Module Output Parameter(s) **MUST** include the
UUID(s) of the Cinder Volumes created in template,
while others **MAY** be included.

As stated in :need:`R-07443`, a VNF's Heat Orchestration Templates' Cinder
Volume Module Output Parameter's name and type **MUST** match the input
parameter name and type in the corresponding Base Module or Incremental
Module.

A volume template must define ``outputs`` for each Cinder volume resource
universally unique identifier (UUID) (i.e. ONAP Volume Template Output
Parameters.

-  The VNF Incremental Module or Base Module must define input
   parameters that match each Volume output parameter (i.e., ONAP Volume
   Template Output Parameters).

   -  ONAP will supply the volume template outputs automatically to the
      bases/incremental template input parameters.

-  Volume modules may utilize nested Heat templates.

.. req::
    :id: R-270358
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :introduced: casablanca

    A VNF's Heat Orchestration Template's Cinder Volume Template **MUST**
    contain either

    * An ``OS::Cinder::Volume`` resource
    * An ``OS::Heat::ResourceGroup`` resource that references a Nested YAML
      file that contains an ``OS::Cinder::Volume`` resource
    * A resource that defines the property ``type`` as a Nested YAML file
      (i.e., static nesting) and the Nested YAML contains
      an ``OS::Cinder::Volume`` resource

Optional Property availability_zone
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. req::
    :id: R-25190
    :target: VNF
    :keyword: SHOULD NOT
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource ``OS::Cinder::Volume``
    **SHOULD NOT** declare the property ``availability_zone``.

If the property is used, the value **MUST**
be enumerated in the environment file and must be set to ``nova``, which
is the default. There are no requirements on the parameter naming
convention with the exception that the naming convention **MUST NOT** be the
same as the ``OS::Nova::Server`` property ``availability_zone`` (i.e.,
``availability_zone_{index}``).

Optional Property volume_type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenStack supports multiple volume types. If the ``OS::Cinder::Volume``
optional property ``volume_type`` is not specified, the OpenStack default
``volume type`` is used. If a specific volume type is required, the property
is used and the value **MUST** be enumerated in the environment file. There
are no requirements on the parameter naming convention.

Cinder Volume Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Examples: Volume Template*

A VNF has a Cinder volume module, named incremental_volume.yaml,
that creates an independent Cinder volume for a VM in the module
incremental.yaml. The incremental_volume.yaml defines a parameter in
the output section, dns_volume_id_0 which is the UUID of the cinder volume.
dns_volume_id_0 is defined as a parameter in incremental.yaml.
ONAP captures the UUID value of dns_volume_id_0 from the volume module
output statement and provides the value to the incremental module.

Note that the example below is not a complete Heat Orchestration
Template. The {vm-type} has been defined as "dns".

incremental_volume.yaml

.. code-block:: yaml

  parameters:
    vnf_name:
      type: string
    dns_volume_size_0:
      type: number
  ...

  resources:
    dns_volume_0:
      type: OS::Cinder::Volume
      properties:
        name:
          str_replace:
            template: VNF_NAME_volume_0
            params:
              VNF_NAME: { get_param: vnf_name }
        size: {get_param: dns_volume_size_0}
  ...
  outputs:
    dns_volume_id_0:
      value: {get_resource: dns_volume_0}
  ...

incremental.yaml

.. code-block:: yaml

  parameters:
    dns_server_0:
      type: string
    dns_volume_id_0:
      type: string
  ...

  resources:
    dns_server_0:
      type: OS::Nova::Server
      properties:
        name: {get_param: dns_name_0}
        networks:
  ...
    dns_volume_attach_0:
      type: OS::Cinder::VolumeAttachment
      properties:
        instance_uuid: { get_resource: dns_server_0 }
        volume_id: { get_param: dns_volume_id_0 }
