.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

.. _ONAP Output Parameter Names:

ONAP Output Parameter Names
---------------------------

ONAP defines three types of Output Parameters as detailed in
:ref:`Output Parameters`.

ONAP Base Module Output Parameters:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP Base Module Output Parameters do not have an explicit naming
convention.

.. req::
    :id: R-97726
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: none

    A VNF's Heat Orchestration Template's Base Module Output Parameter names
    **MUST** contain ``{vm-type}`` and/or ``{network-role}`` when appropriate.

ONAP Volume Template Output Parameters:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. req::
    :id: R-88524
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: none

    A VNF's Heat Orchestration Template's Volume Template
    Output Parameter names
    **MUST** contain ``{vm-type}`` when appropriate.

Predefined Output Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ONAP currently defines one predefined output parameter the OAM
Management IP Addresses.

.. _OAM Management IP Addresses:

OAM Management IP Addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A VNF may have a management interface for application controllers to
interact with and configure the VNF. Typically, this will be via a
specific VM that performs a VNF administration function. The IP address
of this interface must be captured and inventoried by ONAP. The IP
address might be a VIP if the VNF contains an HA pair of management VMs,
or may be a single IP address assigned to one VM.

.. req::
    :id: R-47874
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF **MAY** have
      * Only an IPv4 OAM Management IP Address
      * Only an IPv6 OAM Management IP Address
      * Both a IPv4 and IPv6 OAM Management IP Addresses

.. req::
    :id: R-18683
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    If a VNF has one IPv4 OAM Management IP Address and the
    IP Address needs to be inventoried in ONAP's A&AI
    database, an output parameter **MUST** be declared in only one of the
    VNF's Heat Orchestration Templates and the parameter **MUST** be named
    ``oam_management_v4_address``.

.. req::
    :id: R-94669
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: static

    If a VNF has one IPv6 OAM Management IP Address and the
    IP Address needs to be inventoried in ONAP's A&AI
    database, an output parameter **MUST** be declared in only one of the
    VNF's Heat Orchestration Templates and the parameter **MUST** be named
    ``oam_management_v6_address``.

The OAM Management IP Address maybe assigned either via
  *  ONAP SDN-C
  *  DHCP

.. req::
    :id: R-56287
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: none

    If the VNF's OAM Management IP Address is assigned by ONAP SDN-C and
    assigned in the VNF's Heat Orchestration Template's via a heat resource
    ``OS::Neutron::Port`` property ``fixed_ips`` map property
    ``ip_adress`` parameter (e.g., ``{vm-type}_{network-role}_ip_{index}``,
    ``{vm-type}_{network-role}_v6_ip_{index}``)
    and the OAM IP Address is required to be inventoried in ONAP A&AI,
    then the parameter **MUST** be echoed in an output statement.

    .. code-block:: yaml

      outputs:
          oam_management_v4_address:
            value: {get_param: {vm-type}_{network-role}_ip_{index} }
          oam_management_v6_address:
            value: {get_param: {vm-type}_{network-role}_v6_ip_{index} }


*Example: ONAP SDN-C Assigned IP Address echoed as
oam_management_v4_address*

.. code-block:: yaml

  parameters:
    admin_oam_ip_0:
      type: string
      description: Fixed IPv4 assignment for admin VM 0 on the OAM network
  . . .
  resources:
    admin_0_oam_port_0:
      type: OS::Neutron::Port
      properties:
        name:
          str_replace:
            template: VNF_NAME_admin_oam_port_0
            params:
              VNF_NAME: {get_param: vnf_name}
        network: { get_param: oam_net_id }
        fixed_ips: [{ "ip_address": { get_param: admin_oam_ip_0 }}]
        security_groups: [{ get_param: security_group }]
    admin_server_0:
      type: OS::Nova::Server
      properties:
        name: { get_param: admin_names }
        image: { get_param: admin_image_name }
        flavor: { get_param: admin_flavor_name }
        availability_zone: { get_param: availability_zone_0 }
      networks:
        - port: { get_resource: admin_0_oam_net_port_0 }
      metadata:
        vnf_id: { get_param: vnf_id }
        vf_module_id: { get_param: vf_module_id }
        vnf_name: {get_param: vnf_name }
  outputs:
      oam_management_v4_address:
        value: {get_param: admin_oam_ip_0 }

.. req::
    :id: R-48987
    :target: VNF
    :keyword: MUST
    :updated: casablanca
    :validation_mode: none

    If the VNF's OAM Management IP Address is cloud assigned and
    and the OAM IP Address is required to be inventoried in ONAP A&AI,
    then the parameter **MUST** be obtained by the
    resource ``OS::Neutron::Port``
    attribute ``ip_address``.

.. code-block:: yaml

   outputs:
       oam_management_v4_address:
         value: {get_attr: [ {OS::Neutron Port Resource ID}, fixed_ips, 0, ip_address] }

*Example: Cloud Assigned IP Address output as oam_management_v4_address*

.. code-block:: yaml

  parameters:
  . . .
  resources:
    admin_0_oam_port_0:
      type: OS::Neutron::Port
      properties:
        name:
          str_replace:
            template: VNF_NAME_admin_oam_0_port
            params:
              VNF_NAME: {get_param: vnf_name}
        network: { get_param: oam_net_id }
        security_groups: [{ get_param: security_group }]
    admin_server_0:
      type: OS::Nova::Server
      properties:
        name: { get_param: admin_name_0 }
        image: { get_param: admin_image_name }
        flavor: { get_param: admin_flavor_name }
        availability_zone: { get_param: availability_zone_0 }
        networks:
          - port: { get_resource: admin_0_oam_port_0 }
        metadata:
          vnf_id: { get_param: vnf_id }
          vf_module_id: { get_param: vf_module_id }
          vnf_name: {get_param: vnf_name }
  outputs:
    oam_management_v4_address:
      value: {get_attr: [admin_0_oam_port_0, fixed_ips, 0, ip_address] }
