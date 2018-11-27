.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

Contrail Resource Parameters
----------------------------------------------------------------------

ONAP requires the parameter names of certain Contrail Resources to
follow specific naming conventions. This section provides these
requirements.

Contrail Network Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Contrail based resources may require references to a Contrail network
using the network FQDN.

External Networks
~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-02164
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    When a VNF's Heat Orchestration Template's Contrail resource
    has a property that
    references an external network that requires the network's
    Fully Qualified Domain Name (FQDN), the property parameter

    * **MUST** follow the format ``{network-role}_net_fqdn``
    * **MUST** be declared as type ``string``
    * **MUST NOT** be enumerated in the VNF's Heat Orchestration Template's
      Environment File

.. req::
    :id: R-92193
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static

    A VNF's Heat Orchestration Template's parameter
    ``{network-role}_net_fqdn``
    **MUST NOT** be enumerated in the VNF's Heat Orchestration Template's
    Environment File.

*Example: Parameter declaration*

.. code-block:: yaml

  parameters:
    {network-role}_net_fqdn:
      type: string
      description: Contrail FQDN for the {network-role} network

*Example: Contrail Resource OS::ContrailV2::VirtualMachineInterface
Reference to a Network FQDN.*

In this example, the {network-role} has been defined as oam to represent
an oam network and the {vm-type} has been defined as fw for firewall.
The Contrail resource OS::ContrailV2::VirtualMachineInterface property
virtual_network_refs references a contrail network FQDN.

.. code-block:: yaml

  fw_0_oam_vmi_0:
    type: OS::ContrailV2::VirtualMachineInterface
    properties:
      name:
        str_replace:
          template: VM_NAME_virtual_machine_interface_1
          params:
            VM_NAME: { get_param: fw_name_0 }
      virtual_machine_interface_properties:
        virtual_machine_interface_properties_service_interface_type: {
        get_param: oam_protected_interface_type }
      virtual_network_refs:
        - get_param: oam_net_fqdn
      security_group_refs:
        - get_param: fw_sec_grp_id

Interface Route Table Prefixes for Contrail InterfaceRoute Table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. req::
    :id: R-28222
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    If a VNF's Heat Orchestration Template
    ``OS::ContrailV2::InterfaceRouteTable`` resource
    ``interface_route_table_routes`` property
    ``interface_route_table_routes_route`` map property parameter name
    **MUST** follow the format

    * ``{vm-type}_{network-role}_route_prefixes``

.. req::
    :id: R-19756
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    If a VNF's Heat Orchestration Template
    ``OS::ContrailV2::InterfaceRouteTable`` resource
    ``interface_route_table_routes`` property
    ``interface_route_table_routes_route`` map property parameter
    ``{vm-type}_{network-role}_route_prefixes``
    **MUST** be defined as type ``json``.

.. req::
    :id: R-76682
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: static
    :updated: casablanca

    If a VNF's Heat Orchestration Template
    ``OS::ContrailV2::InterfaceRouteTable`` resource
    ``interface_route_table_routes`` property
    ``interface_route_table_routes_route`` map property parameter
    ``{vm-type}_{network-role}_route_prefixes``
    **MUST NOT** be enumerated in the VNF's Heat Orchestration Template's
    Environment File.

The parameter ``{vm-type}_{network-role}_route_prefixes``
supports IP addresses in the format:

1. Host IP Address (e.g., 10.10.10.10)

2. CIDR Notation format (e.g., 10.0.0.0/28)


*Example Parameter Definition*

.. code-block:: yaml

  parameters:
    {vm-type}_{network-role}_route_prefixes:
      type: json
      description: JSON list of Contrail Interface Route Table route prefixes

*Example:*

.. code-block:: yaml

  parameters:
    vnf_name:
      type: string
      description: Unique name for this VF instance
    fw_oam_route_prefixes:
      type: json
      description: prefix for the ServiceInstance InterfaceRouteTable
    int_fw_dns_trusted_interface_type:
      type: string
      description: service_interface_type for ServiceInstance

  resources:
    <resource name>:
      type: OS::ContrailV2::InterfaceRouteTable
      depends_on: [resource name of OS::ContrailV2::ServiceInstance]
      properties:
        name:
          str_replace:
            template: VNF_NAME_interface_route_table
            params:
              VNF_NAME: { get_param: vnf_name }
        interface_route_table_routes:
          interface_route_table_routes_route: { get_param: fw_oam_route_prefixes }
        service_instance_refs:
          - get_resource: <resource name of OS::ContrailV2::ServiceInstance>
        service_instance_refs_data:
          - service_instance_refs_data_interface_type: { get_param: oam_interface_type }


Resource OS::ContrailV2::InstanceIp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Contrail resource ``OS::ContrailV2::InstanceIp`` has two properties
that parameters **MUST** follow an explicit naming convention.  The
properties are ``instance_ip_address`` and ``subnet_uuid``.

*Example OS::ContrailV2::InstanceIp Resource*

.. code-block:: yaml

  <resource ID>:
    type: OS::ContrailV2::InstanceIp
    properties:
      name: { get_param: name }
      fq_name: { get_param: fq_name }
      display_name: { get_param: display_name }
      secondary_ip_tracking_ip:
        {
          secondary_ip_tracking_ip_ip_prefix: { get_param: secondary_ip_tracking_ip_ip_prefix },
          secondary_ip_tracking_ip_ip_prefix_len: { get_param: secondary_ip_tracking_ip_ip_prefix_len },
        }
      instance_ip_address: { get_param: instance_ip_address }
      instance_ip_mode: { get_param: instance_ip_mode }
      subnet_uuid: { get_param: subnet_uuid }
      instance_ip_family: { get_param: instance_ip_family }
      annotations:
        {
          annotations_key_value_pair:
            [{
              annotations_key_value_pair_key: { get_param: annotations_key_value_pair_key },
              annotations_key_value_pair_value: { get_param: annotations_key_value_pair_value },
            }],
        }
      instance_ip_local_ip: { get_param: instance_ip_local_ip }
      instance_ip_secondary: { get_param: instance_ip_secondary }
      physical_router_refs: [{ get_param: physical_router_refs }]
      virtual_machine_interface_refs: [{ get_param: virtual_machine_interface_refs }]
      virtual_network_refs: [{ get_param: virtual_network_refs }]


Resource OS::ContrailV2::InstanceIp Property instance_ip_address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A VNF's Heat Orchestration Templates resource ``OS::ContrailV2::InstanceIp``
property ``instance_ip_address`` parameter
**MUST** follow the same requirements
that apply to the resource ``OS::Neutron`` property ``fixed_ips`` map
property ``ip_address`` parameter.


*Example: Contrail Resource OS::ContrailV2::InstanceIp, Property
instance_ip_address*

The property instance_ip_address uses the same parameter naming
convention as the property fixed_ips and Map Property ip_address in
OS::Neutron::Port. The resource is assigning an ONAP SDN-C Assigned IP
Address. The {network-role} has been defined as oam_protected to
represent an oam protected network and the {vm-type} has been defined as
fw for firewall.

.. code-block:: yaml

  fw_0_oam_protected_vmi_0_IP_0:
    type: OS::ContrailV2::InstanceIp
    depends_on:
      - fw_0_oam_protected_vmi_0
    properties:
      virtual_machine_interface_refs:
        - get_resource: fw_0_oam_protected_vmi_0
      virtual_network_refs:
        - get_param: oam_protected_net_fqdn
      instance_ip_address: { get_param: [fw_oam_protected_ips, get_param: index ] }

Resource OS::ContrailV2::InstanceIp Property subnet_uuid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A VNF's Heat Orchestration Templates resource ``OS::ContrailV2::InstanceIp``
property ``subnet_uuid`` parameter
**MUST** follow the same requirements
that apply to the resource ``OS::Neutron`` property ``fixed_ips`` map
property ``subnet``/``subnet_id`` parameter.

*Example: Contrail Resource OS::ContrailV2::InstanceIp, Property
subnet_uuid*

The property instance_ip_address uses the same parameter naming
convention as the property fixed_ips and Map Property subnet_id in
OS::Neutron::Port. The resource is assigning a cloud assigned IP
Address. The {network-role} has been defined as "oam_protected" to
represent an oam protected network and the {vm-type} has been defined as
"fw" for firewall.

.. code-block:: yaml

  fw_0_oam_protected_vmi_0_IP_0:
    type: OS::ContrailV2::InstanceIp
    depends_on:
    - fw_0_oam_protected_vmi_0
    properties:
      virtual_machine_interface_refs:
        - get_resource: fw_0_oam_protected_vmi_0
      virtual_network_refs:
        - get_param: oam_protected_net_fqdn
      subnet_uuid: { get_param: oam_protected_subnet_id }

OS::ContrailV2::VirtualMachineInterface Property virtual_machine_interface_allowed_address_pairs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A VNF's Heat Orchestration Templates resource
``OS::ContrailV2::VirtualMachineInterface`` map property,
``virtual_machine_interface_allowed_address_pairs,
virtual_machine_interface_allowed_address_pairs_allowed_address_pair,
virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip,
virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``
parameter **MUST** follow the same requirements that apply to the
resource ``OS::Neutron::Port`` property
``allowed_address_pairs``, map property ``ip_address`` parameter.

*Example OS::ContrailV2::VirtualMachineInterface*

.. code-block:: yaml

  <resource ID>:
    type: OS::ContrailV2::VirtualMachineInterface
    properties:
      name: { get_param: name }
      fq_name: { get_param: fq_name }
      ecmp_hashing_include_fields:
        {
          ecmp_hashing_include_fields_hashing_configured: { get_param: ecmp_hashing_include_fields_hashing_configured },
          ecmp_hashing_include_fields_source_ip: { get_param: ecmp_hashing_include_fields_source_ip },
          ecmp_hashing_include_fields_destination_ip: { get_param: ecmp_hashing_include_fields_destination_ip },
          ecmp_hashing_include_fields_ip_protocol: { get_param: ecmp_hashing_include_fields_ip_protocol },
          ecmp_hashing_include_fields_source_port: { get_param: ecmp_hashing_include_fields_source_port },
          ecmp_hashing_include_fields_destination_port: { get_param: ecmp_hashing_include_fields_destination_port },
        }
      virtual_machine_interface_host_routes:
        {
          virtual_machine_interface_host_routes_route:
            [{
              virtual_machine_interface_host_routes_route_prefix: { get_param: virtual_machine_interface_host_routes_route_prefix },
              virtual_machine_interface_host_routes_route_next_hop: { get_param: virtual_machine_interface_host_routes_route_next_hop },
              virtual_machine_interface_host_routes_route_next_hop_type: { get_param: virtual_machine_interface_host_routes_route_next_hop_type },
              virtual_machine_interface_host_routes_route_community_attributes:
                {
                  virtual_machine_interface_host_routes_route_community_attributes_community_attribute: [{ get_param: virtual_machine_interface_host_routes_route_community_attributes_community_attribute }],
                },
            }],
        }
      virtual_machine_interface_mac_addresses:
        {
          virtual_machine_interface_mac_addresses_mac_address: [{ get_param: virtual_machine_interface_mac_addresses_mac_address }],
        }
      virtual_machine_interface_dhcp_option_list:
        {
          virtual_machine_interface_dhcp_option_list_dhcp_option:
            [{
              virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_name: { get_param: virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_name },
              virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_value: { get_param: virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_value },
              virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_value_bytes: { get_param: virtual_machine_interface_dhcp_option_list_dhcp_option_dhcp_option_value_bytes },
            }],
        }
      virtual_machine_interface_bindings:
        {
          virtual_machine_interface_bindings_key_value_pair:
            [{
              virtual_machine_interface_bindings_key_value_pair_key: { get_param: virtual_machine_interface_bindings_key_value_pair_key },
              virtual_machine_interface_bindings_key_value_pair_value: { get_param: virtual_machine_interface_bindings_key_value_pair_value },
            }],
        }
      virtual_machine_interface_disable_policy: { get_param: virtual_machine_interface_disable_policy }
      virtual_machine_interface_allowed_address_pairs:
        {
          virtual_machine_interface_allowed_address_pairs_allowed_address_pair:
            [{
              virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip:
                {
                  virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix: { get_param: virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix },
                  virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix_len: { get_param: virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix_len },
                },
              virtual_machine_interface_allowed_address_pairs_allowed_address_pair_mac: { get_param: virtual_machine_interface_allowed_address_pairs_allowed_address_pair_mac },
              virtual_machine_interface_allowed_address_pairs_allowed_address_pair_address_mode: { get_param: virtual_machine_interface_allowed_address_pairs_allowed_address_pair_address_mode },
            }],
        }
      annotations:
        {
          annotations_key_value_pair:
            [{
              annotations_key_value_pair_key: { get_param: annotations_key_value_pair_key },
              annotations_key_value_pair_value: { get_param: annotations_key_value_pair_value },
            }],
        }
      virtual_machine_interface_fat_flow_protocols:
        {
          virtual_machine_interface_fat_flow_protocols_fat_flow_protocol:
            [{
              virtual_machine_interface_fat_flow_protocols_fat_flow_protocol_protocol: { get_param: virtual_machine_interface_fat_flow_protocols_fat_flow_protocol_protocol },
              virtual_machine_interface_fat_flow_protocols_fat_flow_protocol_port: { get_param: virtual_machine_interface_fat_flow_protocols_fat_flow_protocol_port },
            }],
        }
      virtual_machine_interface_device_owner: { get_param: virtual_machine_interface_device_owner }
      port_security_enabled: { get_param: port_security_enabled }
      virtual_machine_interface_properties:
        {
          virtual_machine_interface_properties_service_interface_type: { get_param: virtual_machine_interface_properties_service_interface_type },
          virtual_machine_interface_properties_interface_mirror:
            {
              virtual_machine_interface_properties_interface_mirror_traffic_direction: { get_param: virtual_machine_interface_properties_interface_mirror_traffic_direction },
              virtual_machine_interface_properties_interface_mirror_mirror_to:
                {
                  virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_name: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_name },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_encapsulation: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_encapsulation },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_ip_address: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_ip_address },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_mac_address: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_analyzer_mac_address },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_routing_instance: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_routing_instance },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_udp_port: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_udp_port },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_juniper_header: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_juniper_header },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_nh_mode: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_nh_mode },
                  virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header:
                    {
                      virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header_vtep_dst_ip_address: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header_vtep_dst_ip_address },
                      virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header_vtep_dst_mac_address: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header_vtep_dst_mac_address },
                      virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header_vni: { get_param: virtual_machine_interface_properties_interface_mirror_mirror_to_static_nh_header_vni },
                    },
                },
            },
          virtual_machine_interface_properties_local_preference: { get_param: virtual_machine_interface_properties_local_preference },
          virtual_machine_interface_properties_sub_interface_vlan_tag: { get_param: virtual_machine_interface_properties_sub_interface_vlan_tag },
        }
      display_name: { get_param: display_name }
      service_health_check_refs: [{ get_param: service_health_check_refs }]
      routing_instance_refs: [{ get_param: routing_instance_refs }]
      routing_instance_refs_data:
        [{
          routing_instance_refs_data_direction: { get_param: routing_instance_refs_data_direction },
          routing_instance_refs_data_vlan_tag: { get_param: routing_instance_refs_data_vlan_tag },
          routing_instance_refs_data_src_mac: { get_param: routing_instance_refs_data_src_mac },
          routing_instance_refs_data_dst_mac: { get_param: routing_instance_refs_data_dst_mac },
          routing_instance_refs_data_mpls_label: { get_param: routing_instance_refs_data_mpls_label },
          routing_instance_refs_data_service_chain_address: { get_param: routing_instance_refs_data_service_chain_address },
          routing_instance_refs_data_ipv6_service_chain_address: { get_param: routing_instance_refs_data_ipv6_service_chain_address },
          routing_instance_refs_data_protocol: { get_param: routing_instance_refs_data_protocol },
        }]
      security_group_refs: [{ get_param: security_group_refs }]
      physical_interface_refs: [{ get_param: physical_interface_refs }]
      port_tuple_refs: [{ get_param: port_tuple_refs }]
      interface_route_table_refs: [{ get_param: interface_route_table_refs }]
      virtual_machine_interface_refs: [{ get_param: virtual_machine_interface_refs }]
      virtual_network_refs: [{ get_param: virtual_network_refs }]
      virtual_machine_refs: [{ get_param: virtual_machine_refs }]
      qos_config_refs: [{ get_param: qos_config_refs }]
      virtual_machine: { get_param: virtual_machine }
      project: { get_param: project }
