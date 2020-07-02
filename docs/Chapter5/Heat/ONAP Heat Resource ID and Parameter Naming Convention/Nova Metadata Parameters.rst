.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

.. _Nova Server - Metadata Parameters:

Resource: OS::Nova::Server Metadata Parameters
----------------------------------------------

The ``OS::Nova::Server`` resource property ``metadata`` is an optional
OpenStack property.
Table 2 summarizes the mandatory and optional ``metadata`` supported by ONAP.
The sections that follow provides the requirements associated with each
``metadata`` parameter.


.. csv-table:: **Table 2 OS::Nova::Server Mandatory and Optional Metadata**
   :header: Resource, Property, Parameter Name, Parameter Type, Required, Parameter Value Provided to Heat
   :align: center
   :widths: auto

   OS::Nova::Server, metadata, vnf_id, string, **MUST**, ONAP
   OS::Nova::Server, metadata, vf_module_id, string, **MUST**, ONAP
   OS::Nova::Server, metadata, vnf_name, string, **MUST**, ONAP
   OS::Nova::Server, metadata, vf_module_name, string, **SHOULD**, ONAP
   OS::Nova::Server, metadata, vm_role, string, **MAY**, YAML or Environment File
   OS::Nova::Server, metadata, vf_module_index, number, **MAY**, ONAP
   OS::Nova::Server, metadata, workload_context, string, **MUST**, ONAP
   OS::Nova::Server, metadata, environment_context, string, **MUST**, ONAP

vnf_id
^^^^^^

The ``OS::Nova::Server`` resource property ``metadata`` key/value pair
``vnf_id`` is an ONAP generated UUID that identifies the VNF.  The value
is provided by ONAP to the VNF's Heat Orchestration
Template at orchestration time.

.. req::
    :id: R-37437
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource property ``metadata`` **MUST**
    contain the  key/value pair ``vnf_id``
    and the value **MUST** be obtained via a ``get_param``.

.. req::
    :id: R-07507
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource property
    ``metadata`` key/value pair ``vnf_id`` parameter
    **MUST** be declared as ``vnf_id`` and the parameter **MUST**
    be defined as type: ``string``.

.. req::
    :id: R-55218
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource property
    ``metadata`` key/value pair ``vnf_id`` parameter ``vnf_id`` **MUST NOT**
    have parameter constraints defined.

.. req::
    :id: R-20856
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource property
    ``metadata`` key/value pair ``vnf_id`` parameter ``vnf_id`` **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.

*Example 'vnf_id' Parameter Definition*

.. code-block:: yaml

  parameters:

    vnf_id:
      type: string
      description: Unique ID for this VNF instance

vf_module_id
^^^^^^^^^^^^

The OS::Nova::Server Resource ``metadata`` map value parameter ``vf_module_id``
is an ONAP generated UUID that identifies the VF Module (e.g., Heat
Orchestration Template).  The value
is provided by ONAP to the VNF's Heat Orchestration
Template at orchestration time.

.. req::
    :id: R-71493
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` **MUST**
    contain the key/value pair ``vf_module_id``
    and the value MUST be obtained via a ``get_param``.

.. req::
    :id: R-82134
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource property
    ``metadata`` key/value pair ``vf_module_id`` parameter **MUST**
    be declared as ``vf_module_id`` and the parameter **MUST**
    be defined as type: ``string``.

.. req::
    :id: R-98374
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource property
    ``metadata`` key/value pair ``vf_module_id`` parameter ``vf_module_id``
    **MUST NOT**
    have parameter constraints defined.

.. req::
    :id: R-72871
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource property
    ``metadata`` key/value pair ``vf_module_id`` parameter ``vf_module_id``
    **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.

*Example 'vf_module_id' Parameter Definition*

.. code-block:: yaml

  parameters:

    vnf_module_id:
      type: string
      description: Unique ID for this VNF module instance


vnf_name
^^^^^^^^

The ``OS::Nova::Server`` Resource ``metadata`` map value parameter ``vnf_name``
is the ONAP (SDN-C) generated alphanumeric name of the deployed VNF instance.
The value
is provided by ONAP to the VNF's Heat Orchestration
Template at orchestration time.

.. req::
    :id: R-72483
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource property
    ``metadata`` **MUST** contain the key/value pair ``vnf_name`` and the
    value **MUST** be obtained via a ``get_param``.

.. req::
    :id: R-62428
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vnf_name`` parameter **MUST**
    be declared as ``vnf_name`` and the parameter **MUST** be defined as
    type: ``string``.

.. req::
    :id: R-44318
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vnf_name``
    parameter ``vnf_name`` **MUST NOT**
    have parameter constraints defined.

.. req::
    :id: R-36542
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vnf_name`` parameter
    ``vnf_name`` **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.


*Example 'vnf_name' Parameter Definition*

.. code-block:: yaml

  parameters:

    vnf_name:
      type: string
      description: Unique name for this VNF instance

vf_module_name
^^^^^^^^^^^^^^

The ``OS::Nova::Server`` Resource ``metadata`` map value parameter
``vf_module_name``
is the deployment name of the heat stack created (e.g., ``<STACK_NAME>``)
from the
VNF's Heat Orchestration template
in the command ``Heat stack-create``
(e.g., ``Heat stack-create [-f <FILE>] [-e <FILE>] <STACK_NAME>``).
The ``vf_module_name`` (e.g., ``<STACK_NAME>`` is specified as
part of the orchestration process.

.. req::
    :id: R-100400
    :target: VNF
    :keyword: SHOULD
    :introduced: dublin

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property metadata **SHOULD** contain the key/value pair ``vf_module_name``.


.. req::
    :id: R-68023
    :target: VNF
    :keyword: MUST
    :updated: dublin
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vf_module_name``
    value **MUST**
    be obtained via a ``get_param``.

.. req::
    :id: R-39067
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vf_module_name`` parameter **MUST** be
    declared as ``vf_module_name`` and the parameter **MUST**
    be defined as type: ``string``.

.. req::
    :id: R-15480
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vf_module_name`` parameter ``vf_module_name``
    **MUST NOT** have parameter constraints defined.

.. req::
    :id: R-80374
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static


    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vf_module_name``
    parameter ``vf_module_name`` **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.


*Example 'vf_module_name' Parameter Definition*

.. code-block:: yaml

  parameters:

    vf_module_name:
      type: string
      description: Unique name for this VNF Module instance

vm_role
^^^^^^^

The ``OS::Nova::Server`` Resource ``metadata`` map value parameter ``vm_role``
is a ``metadata`` tag that describes the role of the Virtual Machine.

.. req::
    :id: R-85328
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource property
    ``metadata`` **MAY**
    contain the key/value pair ``vm_role`` and the value **MUST** be
    obtained either via

    - ``get_param``
    - hard coded in the key/value pair ``vm_role``.

.. req::
    :id: R-95430
    :target: VNF
    :keyword: MAY
    :updated: dublin
    :validation_mode: none

    If a VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource property
    ``metadata`` key/value pair ``vm_role`` value is obtained via
    ``get_param``, the parameter **MAY** be declared as

    * ``vm_role`` and the parameter defined as ``type: string``.
    * ``vm_roles`` and the parameter defined as ``type: comma_delimited_list``.
    * ``{vm-type}_vm_role`` and the parameter defined as ``type: string``.

.. req::
    :id: R-67597
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vm_role`` parameter ``vm_role``
    **MUST NOT** have parameter constraints defined.

Defining the ``vm_role`` as the ``{vm-type}`` is a recommended convention


.. req::
    :id: R-86476
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vm_role`` value **MUST**
    only contain alphanumeric characters and underscores (i.e., '_').


*Example 'vm_role' Parameter Definition*

.. code-block:: yaml

  parameters:

    vm_role:
      type: string
      description: Unique role for this VM

*Example: 'vm_role' Definition: Hard Coded in
OS::Nova::Resource metadata property*

.. code-block:: yaml

  resources:

    dns_server_0
      type: OS::Nova::Server
      properties:
        . . . .
        metadata:
          vm_role: dns

*Example 'vm_role' Definition: Defined in Environment file
and retrieved via 'get_param'*

.. code-block:: yaml

  resources:

    dns_server_0:
      type: OS::Nova::Server
      properties:
        . . . .
        metadata:
          vm_role: { get_param: vm_role }

Example vnf_id, vf_module_id, vnf_name, vf_module_name, vm_role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The example below depicts part of a Heat Orchestration Template that
uses the five of the ``OS::Nova::Server`` resource
``metadata`` map value parameters discussed in this
section. The ``{vm-type}`` has been defined as ``lb`` for load balancer.

.. code-block:: yaml

  parameters:
    lb_name_0
      type: string
      description: VM Name for lb VM 0
    vnf_name:
      type: string
      description: Unique name for this VNF instance
    vnf_id:
      type: string
      description: Unique ID for this VNF instance
    vf_module_name:
      type: string
      description: Unique name for this VNF Module instance
    vf_module_id:
      type: string
      description: Unique ID for this VNF Module instance
    vm_role:
      type: string
      description: Unique role for this VM
  resources:
    lb_server_0:
      type: OS::Nova::Server
      properties:
        name: { get_param: lb_name_0 }
        ...
        metadata:
          vnf_name: { get_param: vnf_name }
          vnf_id: { get_param: vnf_id }
          vf_module_name: { get_param: vf_module_name }
          vf_module_id: { get_param: vf_module_id }
          vm_role: lb

vf_module_index
^^^^^^^^^^^^^^^


.. req::
    :id: R-100410
    :target: VNF
    :keyword: MAY
    :introduced: dublin

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource  property ``metadata`` **MAY**
    contain the key/value pair ``vf_module_index``.


.. req::
    :id: R-50816
    :target: VNF
    :keyword: MUST
    :updated: dublin
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server``
    resource  property ``metadata``
    key/value pair ``vf_module_index``
    value **MUST** be obtained via a ``get_param``.

.. req::
    :id: R-54340
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vf_module_index`` parameter **MUST**
    be declared as ``vf_module_index`` and the parameter **MUST** be
    defined as type: ``number``.


.. req::
    :id: R-09811
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static


    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vf_module_index`` **MUST NOT**
    have parameter constraints defined.

.. req::
    :id: R-37039
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``vf_module_index`` parameter
    ``vf_module_index`` **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.

.. req::
    :id: R-55306
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``vf_module_index`` **MUST NOT**
    be used in a ``OS::Cinder::Volume`` resource and **MUST NOT** be
    used in VNF's Volume template;
    it is not supported.

The ``vf_module_index`` parameter indicates which instance of the module is
being deployed into the VNF.
This parameter may be used in cases where multiple instances of the same
incremental module are being instantiated for scaling purposes. The index
can be used in the Heat Orchestration Template for indexing into a
``comma_delimited_list`` defined parameter to provide a unique value
for each module instance.
The parameter list may be defined in the VNF's Heat Orchestration
Template's environmental file or be provided by SDN-C.

ONAP does not support the ``vf_module_index`` to be utilized as an index by all
parameters defined as ``comma_delimited_list``.
The ``vf_module_index`` must not be used for indexing the following
resource property parameters:

- ``OS::Nova::Server`` property ``name`` parameter (defined as a
  ``comma_delimited_list``).
- ``OS::Neutron::Port`` property ``fixed_ips`` map property ``ip_address``
  parameter (defined as a ``comma_delimited_list``) when the port is
  attaching to an ONAP external network (per the ONAP
  definition, see Requirement R-57424 and R-16968)

The ``vf_module_index`` may be used for indexing ``OS::Neutron::Port`` property
``fixed_ips`` map property ``ip_address`` parameter (defined as a
``comma_delimited_list``) when the port is attaching to an
ONAP internal network (per the ONAP definition, see Requirements R-52425 and
R-46461 and R-35666).  An example is provided below.

.. req::
    :id: R-55307
    :target: VNF
    :keyword: MUST NOT
    :introduced: frankfurt
    :validation_mode: static

    A VNF's Heat Orchestration Template's parameter ``vf_module_index``
    **MUST NOT** be used for indexing an:

    - ``OS::Nova::Server`` property ``name`` parameter (when defined as a
      ``comma_delimited_list``).
    - ``OS::Neutron::Port`` property ``fixed_ips`` map property ``ip_address``
      parameter (when defined as a ``comma_delimited_list``) when the port is
      attaching to an ONAP external network (per the ONAP
      definition, see Requirement R-57424 and R-16968)
    - ``OS::ContrailV2::InstanceIp`` property ``instance_ip_address``
      parameter (when defined as a ``comma_delimited_list``) when the port
      (i.e, ``OS::ContrailV2::VirtualMachineInterface``) is
      attaching to an ONAP external network (per the ONAP
      definition, see Requirement R-57424 and R-16968)

The ``vf_module_index`` will start at 0 for the first instance of a module
type. Subsequent instances of the same module type will receive the
lowest unused index. This means that indexes will be reused if a module
is deleted and re-added. As an example, if three copies of a module are
deployed with ``vf_module_index`` values of 0, 1, and 2 then subsequently
the second one is deleted (index 1), and then re-added, index 1 will be
reused.

*Example*

In this example, the ``{vm-type}`` has been defined as ``oam_vm`` to represent
an OAM VM. An incremental heat module is used to deploy the OAM VM. The
OAM VM attaches to an ONAP internal network which has a
``{network-role}`` of ``ctrl``. A maximum of four OAM VMs can be deployed. The
environment file contains the four IP addresses that each successive OAM
VM will be assigned. The ``vf_module_index`` is used as the index to
determine the IP assignment.

Environment File

.. code-block:: yaml

  parameters:
    oam_vm_int_ctrl_ips: 10.10.10.1,10.10.10.2,10.10.10.3,10.10.10.4

YAML File

.. code-block:: yaml

  parameters:
    vf_module_index:
      type: number
      description: Unique index for this VNF Module instance
    oam_vm_name_0:
      type: string
      description: VM Name for lb VM 0
    int_ctrl_net_id:
      type: string
      description: Neutron UUID for the internal control network
    oam_vm_int_ctrl_ips:
      type: comma_delimited_list
      description: Fixed IP assignments for oam VMs on the internal control
                   network
  resources:
    oam_vm_server_0:
      type: OS::Nova::Server
      properties:
        name: { get_param: oam_vm_name_0 }
        networks:
          - port: { get_resource: oam_vm_0_int_ctrl_port_0 }
  #     . . .
        metadata:
          vf_module_index: { get_param: vf_module_index }
    oam_vm_0_int_ctrl_port_0:
      type: OS::Neutron::Port
      properties:
        network: { get_param: int_ctrl_net_id }
        fixed_ips: [ { "ip_address": {get_param: [ oam_vm_int_ctrl_ips, { get_param: vf_module_index} ]}}]

workload_context
^^^^^^^^^^^^^^^^

.. req::
    :id: R-47061
    :target: VNF
    :keyword: SHOULD
    :updated: casablanca

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource **SHOULD** contain the metadata map value parameter
    'workload_context'.

.. req::
    :id: R-74978
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``workload_context``
    parameter **MUST**
    be declared as ``workload_context`` and the parameter **MUST**
    be defined as type: ``string``.

.. req::
    :id: R-34055
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``workload_context``
    parameter ``workload_context`` **MUST NOT**
    have parameter constraints defined.

.. req::
    :id: R-02691
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static


    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``workload_context``
    parameter ``workload_context`` **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.

The 'workload\_context' parameter value will be chosen by the Service Model
Distribution context client in VID and will be supplied to the
Heat Orchestration Template by ONAP at orchestration time.

*Example Parameter Definition*

.. code-block:: yaml

  parameters:
    workload_context:
      type: string
      description: Workload Context for this VNF instance


*Example OS::Nova::Server with metadata*

.. code-block:: yaml

  resources:
    . . .

    {vm-type}_server_{index}:
       type: OS::Nova::Server
       properties:
         name:
         flavor:
         image:
        ...
       metadata:
          vnf_name: { get_param: vnf_name }
          vnf_id: { get_param: vnf_id }
          vf_module_name: { get_param: vf_module_name }
          vf_module_id: { get_param: vf_module_id }
          workload_context: {get_param: workload_context}

environment_context
^^^^^^^^^^^^^^^^^^^

.. req::
    :id: R-88536
    :target: VNF
    :keyword: SHOULD
    :updated: casablanca

    A VNF's Heat Orchestration Template's OS::Nova::Server
    Resource **SHOULD** contain the metadata map value parameter
    'environment_context'.

.. req::
    :id: R-20308
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata`` key/value pair ``environment_context``
    parameter **MUST** be declared as ``environment_context`` and the
    parameter type **MUST** be defined as type: ``string``.

.. req::
    :id: R-56183
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property ``metadata``key/value pair ``environment_context``
    parameter ``environment_context`` **MUST NOT**
    have parameter constraints defined.

.. req::
    :id: R-13194
    :target: VNF
    :keyword: MUST NOT
    :updated: casablanca
    :validation_mode: static

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource
    property
    ``metadata`` key/value pair ``environment_context`` **MUST NOT**
    be enumerated in the Heat Orchestration Template's environment file.

The 'environment_context' parameter value will be defined by the
service designer as part of the service model during the SDC
on-boarding process and will be supplied to the Heat Orchestration
Template by ONAP at orchestration time.


*Example Parameter Definition*

.. code-block:: yaml

  parameters:
    environment_context:
      type: string
      description: Environment Context for this VNF instance


*Example OS::Nova::Server with metadata*

.. code-block:: yaml

  resources:
    . . .

    {vm-type}_server_{index}:
       type: OS::Nova::Server
       properties:
         name:
         flavor:
         image:
        ...
       metadata:
          vnf_name: { get_param: vnf_name }
          vnf_id: { get_param: vnf_id }
          vf_module_name: { get_param: vf_module_name }
          vf_module_id: { get_param: vf_module_id }
          workload_context: {get_param: workload_context}
          environment_context: {get_param: environment_context }
