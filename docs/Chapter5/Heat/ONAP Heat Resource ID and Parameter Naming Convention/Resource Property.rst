.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

Resource Property "name"
----------------------------

The parameter naming convention of the property name for the
resource OS::Nova::Server has been defined in
:ref:`Nova Server - Metadata Parameters`.

This section provides the requirements how the property name for non
OS::Nova::Server resources must be defined when the property is used.
Not all resources require the property name (e.g., it is optional) and
some resources do not support the property.

.. req::
    :id: R-85734
    :target: VNF
    :keyword: MUST

    If a VNF's Heat Orchestration Template contains the property 'name'
    for a non 'OS::Nova::Server' resource, the intrinsic function
    'str_replace' **MUST** be used in conjunction with the ONAP
    supplied metadata parameter 'vnf_name' to generate a unique value.

This prevents the enumeration of a
unique value for the property name in a per instance environment file.

.. req::
    :id: R-99812
    :target: VNF
    :keyword: MUST NOT
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    A value for VNF's Heat Orchestration Template's property 'name'
    for a non 'OS::Nova::Server' resource **MUST NOT** be declared
    in the VNF's Heat Orchestration Template's Environment File.

In most cases the use of the metadata value 'vnf_name' is required to create a
unique property name.  If this will not provide a unique value,
additional options include:

 - Using the Heat Orchestration Template pseudo parameter
   'OS::stack_name' in the str_replace construct
 - Resources created in a nested heat file invoked by an
   'OS::Heat::ResourceGroup' can use the 'index' to construct a unique name


.. req::
    :id: R-32408
    :target: VNF
    :keyword: MUST
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    If a VNF's Heat Orchestration Template property 'name'
    for a non 'OS::Nova::Server' resource uses the intrinsic function
    'str_replace' in conjunction with the ONAP
    supplied metadata parameter 'vnf_name' and does not create
    a unique value, additional data **MUST** be used in the
    'str_replace' to create a unique value, such as 'OS::stack_name'
    and/or the 'OS::Heat::ResourceGroup' 'index'.

*Example: Property 'name' for resource 'OS::Neutron::SecurityGroup'*

.. code-block:: yaml

  resources:
    DNS_SECURITY_GROUP:
      type: OS::Neutron::SecurityGroup
      properties:
        description: vDNS security group
        name:
          str_replace:
            template: VNF_NAME_sec_grp_DNS
            params:
              VNF_NAME: {get_param: vnf_name}
        rules: [. . . . .]

*Example: Property 'name' for resource 'OS::Cinder::Volume'*

.. code-block:: yaml

  resources:
    dns_volume_0:
      type: OS::Cinder::Volume
      properties:
        description: Cinder Volume
        name:
          str_replace:
            template: VNF_NAME_STACK_NAME_dns_volume
            params:
              VNF_NAME: {get_param: vnf_name}
              STACK_NAME: { get_param: 'OS::stack_name' }
  . . . .

*Example: Property 'name' for resource 'OS::Cinder::Volume' invoked by a
'OS::Heat::ResourceGroup'*

.. code-block:: yaml

  resources:
    dns_volume_0:
      type: OS::Cinder::Volume
      properties:
        description: Cinder Volume
        name:
          str_replace:
              template: VNF_NAME_STACK_NAME_dns_volume_INDEX
              params:
                  VNF_NAME: { get_param: vnf_name }
                  STACK_NAME: { get_param: 'OS::stack_name' }
                  INDEX: { get_param: index }
  . . . .

Contrail Issue with Values for the Property Name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. req::
    :id: R-84517
    :target: VNF
    :keyword: SHOULD
    :test: no test found
    :test_case: no test found
    :test_file: no test found

    The Contrail GUI has a limitation displaying special characters.
    The issue is documented in
    https://bugs.launchpad.net/juniperopenstack/+bug/1590710.
    It is recommended that special **SHOULD** characters be avoided.
    However, if special characters must be used, note that for
    the following resources:

       * Virtual Machine
       * Virtual Network
       * Port
       * Security Group
       * Policies
       * IPAM Creation

    the only special characters supported
    are - \" ! $\ \ ' ( ) = ~ ^ | @ ` { } [ ] > , . _"
