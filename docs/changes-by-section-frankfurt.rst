.. Modifications Copyright © 2017-2018 AT&T Intellectual Property.

.. Licensed under the Creative Commons License, Attribution 4.0 Intl.
   (the "License"); you may not use this documentation except in compliance
   with the License. You may obtain a copy of the License at

.. https://creativecommons.org/licenses/by/4.0/

.. Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


Requirement Changes Introduced in Frankfurt
========================================================

This document summarizes the requirement changes by section that were
introduced between the El Alto release and
Frankfurt release. Click on the requirement number to
navigate to the

.. contents::
    :depth: 2

Summary of Changes
------------------

* **Requirements Added:** 22
* **Requirements Changed:** 129
* **Requirements Removed:** 6


Configuration Management
------------------------


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-305645`

    The VNF or PNF MUST support configuration management including
    life cycle management (LCM) using at least one of the following
    protocols a)NETCONF/YANG, b)Ansible and c)Chef.
    

Configuration Management > Ansible Standards and Capabilities > VNF or PNF Configuration via Ansible Requirements > Ansible Client Requirements
-----------------------------------------------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-54373`

    The VNF or PNF Provider **MUST** provide Ansible playbooks that are
    compatible with the Operator’s deployed versions of Ansible and Python.
    As the Ansible runtime itself is not deployed as part of ONAP, the ONAP
    project cannot dictate the specific versions supported.
    

Configuration Management > Ansible Standards and Capabilities > VNF or PNF Configuration via Ansible Requirements > Ansible Playbook Requirements
-------------------------------------------------------------------------------------------------------------------------------------------------


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-09209`

    The VNF or PNF Provider **MUST** store any playbook configuration data
    that requires encryption (passwords, secrets, etc.) in a JSON (.json),
    YAML (.yaml|.yml) or INI (.ini) file, which will be placed in
    <VNF type>/<Version>/ansible/vars directory.
    

.. container:: note

    :need:`R-20988`

    The VNF or PNF provider **MUST** develop playbooks that do not log or
    display passwords and other attributes that must remain secret when
    running playbook in debug mode.

    NOTE: Use "no_log: True"
    

.. container:: note

    :need:`R-39003`

    The VNF or PNF provider **MUST** store passwords and other attributes
    that must remain secret in JSON, YAML or INI files that can be
    encrypted/decrypted using Ansible Vault capabilities.
    

.. container:: note

    :need:`R-42333`

    The VNF or PNF playbooks targeting a subset of VMs (or servers/blades) part
    of a VNF (or PNF) instance **MUST** be designed to use the VNF or PNF
    inventory host file and to use a parameter named target_vm_list to provide
    the subset of VMs in the VNF instance specifically targeted by the
    playbook.

    NOTE: Example of such playbooks would be playbooks used to configure VMs
    added to a VNF instance as part of a scale-out/up or scale-in/down
    operation. Such playbook is expected to also need to perform
    configuration/reconfiguration tasks part of the base VNF instance build.
    

.. container:: note

    :need:`R-46823`

    The VNF or PNF provider **MUST** store passwords and other attributes that
    must remain secret in JSON, YAML or INI with differentiated names when
    passwords and secrets vary from environment to environment. Example, name
    must include <Mechanized user ID>_...json or <Mechanized user ID>_...xml
    when labs and production use different passwords and/or secrets. The
    <Mechanized user ID> is discovered from the environment
    /etc/ansible/ansible.cfg where the playbook runs.
    

.. container:: note

    :need:`R-53245`

    The VNF or PNF provider **MUST** provide playbooks that do not require
    passwords or secrets to be passed in clear text in the command line or
    Rest API request to run the playbook.
    

.. container:: note

    :need:`R-56988`

    The VNF or PNF Provider **MUST** load any playbook configuration data
    that requires encryption (passwords, secrets, etc.) in a JSON (.json),
    YAML (.yaml|.yml) or INI (.ini) file, from the
    <VNF type>/<Version>/ansible/vars directory.
    

.. container:: note

    :need:`R-78640`

    The VNF or PNF provider **SHOULD** provide a single YAML or JSON file
    with all the passwords and secrets to reduce the number of files to be
    decrypted/encrypted before on-boarding into the central repository.
    

.. container:: note

    :need:`R-83092`

    The VNF or PNF provider **MUST** develop playbooks that load passwords
    and other attributes that must remain secret from JSON, YAML or INI files
    that can be encrypted/decrypted using Ansible Vault capabilities.
    

.. container:: note

    :need:`R-88002`

    The VNF or PNF provider **MUST** use a pre-agreed upon password to encrypt
    the Ansible Vault file, or provide the vault password used to encrypt
    the file to the customer, in a secure manner, to allow the customer to
    decrypt/encrypt (rekey) Ansible Vault files before they are checked
    into the central repository for distribution.
    

.. container:: note

    :need:`R-88786`

    The VNF or PNF provider **SHOULD** place the passwords and secrets to
    be edited at the top of the single YAML or JSON file with all the secrets,
    and the (default) ones that are to remain unchanged towards the bottom,
    with commentary separating them.
    

Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-48698`

    The VNF or PNF **MUST** utilize information from key value pairs that will
    be provided by the Ansible Server as "extra-vars" during invocation to
    execute the desired VNF or PNF action. The "extra-vars" attribute-value
    pairs are passed to the Ansible Server by an APPC/SDN-C as part of the
    Rest API request. If the playbook requires files, they must also be
    supplied using the methodology detailed in the Ansible Server API, unless
    they are bundled with playbooks, example, generic templates. Any files
    containing instance specific info (attribute-value pairs), not obtainable
    from any ONAP inventory databases or other sources, referenced and used as
    input by playbooks, shall be provisioned (and distributed) in advance of
    use, e.g., VNF or PNF instantiation. Recommendation is to avoid these
    instance specific, manually created in advance of instantiation, files.
    

.. container:: note

    :need:`R-50252`

    The VNF or PNF **MUST** write to a response file in JSON format that will
    be retrieved and made available by the Ansible Server if, as part of a VNF
    or PNF action (e.g., audit), a playbook is required to return any VNF or
    PNF information/response. The text files must be written in the main
    playbook home directory, in JSON format. The JSON file must be created for
    the VNF or PNF with the name '<VNF or PNF name>_results.txt'. All playbook
    output results, for all VNF VMS or PNF Server/Blades, to be provided as a
    response to the request, must be written to this response file.
    

Configuration Management > NETCONF Standards and Capabilities > VNF or PNF Configuration via NETCONF Requirements > LCM Operations via NETCONF
----------------------------------------------------------------------------------------------------------------------------------------------


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-246519`

    As alternative to Ansible, Chef or REST, a VNF or PNF MAY support YANG models
    allowing execution of standard controller LCM operations including HealthCheck.
    Note: To support vendor YANG models for LCM operations, the controller is responsible
    for performing VNF/PNF specific translation of north-bound API requests into one or more
    south-bound NETCONF requests.
    

Configuration Management > NETCONF Standards and Capabilities > VNF or PNF Configuration via NETCONF Requirements > NETCONF Server Requirements
-----------------------------------------------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-73468`

    The VNF **MUST** allow the NETCONF server connection
    parameters to be configurable during virtual machine instantiation
    through Heat templates where SSH keys, usernames, passwords, SSH
    service and SSH port numbers are Heat template parameters.
    

Contrail Resource Parameters > Contrail Network Parameters > ONAP External Networks
-----------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-02164`

    When a VNF's Heat Orchestration Template's Contrail resource
    ``OS::ContrailV2::InstanceIp`` and/or
    ``OS::ContrailV2::VirtualMachineInterface``
    contains the property ``virtual_network_refs``
    that references an ONAP external network (per the
    ONAP definition, see Requirement R-57424 and R-16968),
    the property value **MUST** be obtained by a ``get_param`` and the
    property parameter

    * **MUST** follow the format ``{network-role}_net_fqdn``
    * **MUST** be declared as type ``string``
    

.. container:: note

    :need:`R-92193`

    A VNF's Heat Orchestration Template's Contrail resource
    ``OS::ContrailV2::InstanceIp`` and/or
    ``OS::ContrailV2::VirtualMachineInterface`` property
    ``virtual_network_refs`` parameter ``{network-role}_net_fqdn``
    **MUST NOT** be enumerated in the VNF's Heat Orchestration Template's
    Environment File.
    

Contrail Resource Parameters > OS::ContrailV2::VirtualMachineInterface Property virtual_machine_interface_allowed_address_pairs > ONAP External Networks
--------------------------------------------------------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-100350`

    When the VNF's Heat Orchestration Template's resource
    ``OS::ContrailV2::VirtualMachineInterface`` is attaching to an
    ONAP external network
    (per the ONAP definition, see Requirement R-57424 and R-16968),
    and the IPv4 VIP address and/or IPv6 VIP address
    is **not** supported by the ONAP data model,
    the map property

    ``virtual_machine_interface_allowed_address_pairs``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``

    * Parameter name **MAY** use any naming convention.  That is, there is no
      ONAP mandatory parameter naming convention.
    * Parameter **MAY** be declared as type ``string`` or type
      ``comma_delimited_list``.

    And the ``OS::ContrailV2::VirtualMachineInterface`` resource
    **MUST** contain resource-level ``metadata`` (not property-level).

    And the ``metadata`` format **MUST**  must contain the
    key value ``aap_exempt`` with a list of all map property

    ``virtual_machine_interface_allowed_address_pairs``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``

    parameters **not** supported by the ONAP data model.
    

.. container:: note

    :need:`R-100310`

    When the VNF's Heat Orchestration Template's resource
    ``OS::ContrailV2::VirtualMachineInterface`` is attaching to an ONAP external
    network (per the
    ONAP definition, see Requirement R-57424 and R-16968),
    and an IPv4 Virtual IP (VIP)
    is required to be supported by the ONAP data model,
    the map property

    ``virtual_machine_interface_allowed_address_pairs``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``

    parameter name **MUST** follow the naming convention

    * ``{vm-type}_{network-role}_floating_ip``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the ONAP external network

    And the parameter **MUST** be declared as type ``string``.

    The ONAP data model can only support one IPv4 VIP address.
    

.. container:: note

    :need:`R-100330`

    When the VNF's Heat Orchestration Template's resource
    ``OS::ContrailV2::VirtualMachineInterface`` is attaching to an ONAP
    external
    network (per the
    ONAP definition, see Requirement R-57424 and R-16968),
    and an IPv6 Virtual IP (VIP)
    is required to be supported by the ONAP data model,
    the map property

    ``virtual_machine_interface_allowed_address_pairs``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``

    parameter name **MUST** follow the naming convention

    * ``{vm-type}_{network-role}_floating_v6_ip``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the ONAP external network

    And the parameter **MUST** be declared as type ``string``.

    The ONAP data model can only support one IPv6 VIP address.
    

.. container:: note

    :need:`R-100280`

    If a VNF's Heat Orchestration Template's resource
    ``OS::ContrailV2::VirtualMachineInterface``
    is attaching to an ONAP external network (per the
    ONAP definition, see Requirement R-57424 and R-16968), the
    map property

    ``virtual_machine_interface_allowed_address_pairs``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip``,

    ``virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``

    parameter
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.
    

Contrail Resource Parameters > OS::ContrailV2::VirtualMachineInterface Property virtual_machine_interface_allowed_address_pairs > ONAP Internal Networks
--------------------------------------------------------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-100360`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualMachineInterface`` is attaching to an
    ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    and an IPv4 Virtual IP (VIP)
    address is assigned using the map property,
    ``virtual_machine_interface_allowed_address_pairs,
    virtual_machine_interface_allowed_address_pairs_allowed_address_pair,
    virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip,
    virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``
    , the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_ip``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the ONAP internal
        network

    And the parameter **MUST** be declared as ``type: string``
    and **MUST** be enumerated in the environment file.

    OR

    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the ONAP internal
        network

    And the parameter **MUST** be declared as ``type: comma_delimited_list``
    and **MUST** be enumerated in the environment file.
    

.. container:: note

    :need:`R-100370`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualMachineInterface`` is attaching to an
    ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    and an IPv6 Virtual IP (VIP)
    address is assigned
    using the map property,
    ``virtual_machine_interface_allowed_address_pairs,
    virtual_machine_interface_allowed_address_pairs_allowed_address_pair,
    virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip,
    virtual_machine_interface_allowed_address_pairs_allowed_address_pair_ip_ip_prefix``
    , the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_v6_ip``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the ONAP internal
        network

    And the parameter **MUST** be declared as ``type: string``
    and **MUST** be enumerated in the environment file

    OR

    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_floating_v6_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the ONAP internal
        network

    And the parameter **MUST** be declared as ``type: comma_delimited_list``
    and **MUST** be enumerated in the environment file.
    

Contrail Resource Parameters > Resource OS::ContrailV2::InstanceIp > Resource OS::ContrailV2::InstanceIp Property instance_ip_address
-------------------------------------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-100150`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address to an
    ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    and an IPv6 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_v6_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the ONAP internal
        network
    

.. container:: note

    :need:`R-100010`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an ONAP external network
    (per the ONAP definition, see Requirement R-57424 and R-16968),
    and an IPv4 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a string,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_{network-role}_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the ONAP external network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one
    

.. container:: note

    :need:`R-100110`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    and an IPv4 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the ONAP internal
        network
    

.. container:: note

    :need:`R-100050`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an ONAP external network
    (per the
    ONAP definition, see Requirement R-57424 and R-16968),
    and an IPv6 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a string,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_{network-role}_v6_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the
      ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the ONAP external network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one
    

.. container:: note

    :need:`R-100030`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an ONAP external network (per the
    ONAP definition, see Requirement R-57424 and R-16968),
    and an IPv4 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_{network-role}_ips``

      where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the ONAP external
        network
    

.. container:: note

    :need:`R-100090`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    and an IPv4 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is
    defined as a ``string``,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_int_{network-role}_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the
      ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the ONAP internal network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one
    

.. container:: note

    :need:`R-100170`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp``
    property ``instance_ip_address``
    parameter associated with an ONAP external network, i.e.,

     * ``{vm-type}_{network-role}_ip_{index}``
     * ``{vm-type}_{network-role}_v6_ip_{index}``
     * ``{vm-type}_{network-role}_ips``
     * ``{vm-type}_{network-role}_v6_ips``


    **MUST NOT** be enumerated in the Heat Orchestration
    Template's Environment File.  ONAP provides the IP address
    assignments at orchestration time.
    

.. container:: note

    :need:`R-100070`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an ONAP external network (per the
    ONAP definition, see Requirement R-57424 and R-16968),
    and an IPv6 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_{network-role}_v6_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the ONAP external
        network
    

.. container:: note

    :need:`R-100130`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` is assigning an IP address to an
    ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    and an IPv6 address is assigned
    using the property ``instance_ip_address``
    and the parameter type is defined as a
    ``string``,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_int_{network-role}_v6_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the ONAP internal network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one
    

.. container:: note

    :need:`R-100180`

    The VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp``
    property ``instance_ip_address``
    parameter associated with an ONAP internal network, i.e.,

     * ``{vm-type}_int_{network-role}_ip_{index}``
     * ``{vm-type}_int_{network-role}_v6_ip_{index}``
     * ``{vm-type}_int_{network-role}_ips``
     * ``{vm-type}_int_{network-role}_v6_ips``


    **MUST** be enumerated in the Heat Orchestration
    Template's Environment File and IP addresses **MUST** be
    assigned.
    

Contrail Resource Parameters > Resource OS::ContrailV2::InstanceIp > Resource OS::ContrailV2::InstanceIp Property subnet_uuid
-----------------------------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-100220`

    When the VNF's Heat Orchestration Template's
    resource ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an ONAP external network (per the ONAP definition, see
    Requirement R-57424 and R-16968),
    and an IPv6 address is being cloud assigned by OpenStack's DHCP Service
    and the ONAP external network IPv6 subnet is to be specified
    using the property ``subnet_uuid``, the parameter
    **MUST** follow the naming convention

      * ``{network-role}_v6_subnet_id``

    where

      * ``{network-role}`` is the network role of the ONAP external network.
    

.. container:: note

    :need:`R-100200`

    When the VNF's Heat Orchestration Template's
    resource ``OS::ContrailV2::InstanceIp`` is assigning an IP address
    to an ONAP external network (per the ONAP definition, see
    Requirement R-57424 and R-16968),
    and an IPv4 address is being cloud assigned by OpenStack's DHCP Service
    and the ONAP external network IPv4 subnet is to be specified
    using the property ``subnet_uuid``, the parameter
    **MUST** follow the naming convention

      * ``{network-role}_subnet_id``

    where

      * ``{network-role}`` is the network role of the ONAP external network.
    

.. container:: note

    :need:`R-100260`

    When

      * the VNF's Heat Orchestration Template's
        resource ``OS::ContrailV2::InstanceIp`` in an Incremental Module is
        attaching
        to an ONAP internal network (per the ONAP definition,
        see Requirements R-52425 and R-46461 and R-35666)
        that is created in the Base Module, AND
      * an IPv6 address is being cloud assigned by OpenStack's DHCP Service AND
      * the ONAP internal network IPv6 subnet is to be specified
        using the property ``subnet_uuid``,

    the parameter **MUST** follow the naming convention

      * ``int_{network-role}_v6_subnet_id``

    where ``{network-role}`` is the network role of the ONAP internal network.

    Note that the parameter **MUST** be defined as an ``output`` parameter in
    the base module.
    

.. container:: note

    :need:`R-100240`

    When

      * the VNF's Heat Orchestration Template's
        resource ``OS::ContrailV2::InstanceIp`` in an Incremental Module is
        assigning an IP address
        to an ONAP internal network (per the ONAP definition, see
        Requirements R-52425 and R-46461 and R-35666)
        that is created in the Base Module, AND
      * an IPv4 address is being cloud assigned by OpenStack's DHCP Service AND
      * the ONAP internal network IPv4 subnet is to be specified
        using the property ``subnet_uuid``,

    the parameter **MUST** follow the naming convention

      * ``int_{network-role}_subnet_id``

    where

      * ``{network-role}`` is the network role of the ONAP internal network

    Note that the parameter **MUST** be defined as an ``output`` parameter in
    the base module.
    

Monitoring & Management > Data Structure Specification of the Event Record
--------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-570134`

    The events produced by the VNF or PNF **MUST** be compliant with the
    common event formats defined in either the
    :ref:`VES Event Listener 7.1.1<ves_event_listener_7_1>` or
    :ref:`VES Event Listener 5.4.1<ves_event_listener_5_4_1>`
    specifications. Version 7.1.1 should be preferred, and VES 5.4.1 is only
    provided for backwards compatibility.
    

ONAP Heat Heat Template Constructs > Nested Heat Templates > Nested Heat Template Requirements
----------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-17528`

    A VNF's Heat Orchestration Template's first level Nested YAML file
    **MUST NOT** contain more than one ``OS::Nova::Server`` resource.
    A VNF's Heat Orchestration Template's second level Nested YAML file
    **MUST NOT** contain any heat resources.
    

ONAP Heat Networking > External Networks
----------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-00606`

    A VNF **MAY** be connected to zero, one or more than one ONAP external
    network.
    

.. container:: note

    :need:`R-57424`

    A VNF's port connected to an ONAP external network **MAY**
    use the port for the purpose of

    - Connecting a VM in the VNF to VMs in another VNF and/or
    - Connecting a VM in the VNF to an external gateway or external router
      and/or
    - Connecting a VM in the VNF to other VMs in the same VNF
    

.. container:: note

    :need:`R-99794`

    An ONAP external network **MUST** have one subnet. An external network
    **MAY** have more than one subnet.
    

.. container:: note

    :need:`R-16968`

    A VNF's Heat Orchestration Templates **MUST NOT** include heat
    resources to create an ONAP external network.

    An ONAP external network **MUST** be instantiated by using VID
    or by invoking SO directly.
    

ONAP Heat Networking > Internal Networks
----------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-35666`

    If a VNF has an ONAP internal network, the VNF's Heat Orchestration
    Template **MUST** include the heat resources to create the
    ONAP internal network.

    A VNF's ONAP internal network is created using Neutron Heat Resources
    (e.g., ``OS::Neutron::Net``, ``OS::Neutron::Subnet``,
    ``OS::Neutron::ProviderNet``) and/or
    Contrail Heat Resources (e.g., ``OS::ContrailV2::VirtualNetwork``,
    ``OS::ContrailV2::NetworkIpam``).
    

.. container:: note

    :need:`R-46461`

    A VNF's port connected to an ONAP internal network **MUST NOT**
    use the port
    for the purpose of reaching VMs in another VNF and/or an
    external gateway and/or
    external router.
    

.. container:: note

    :need:`R-16241`

    A VNF's ONAP internal network **MUST** have one subnet.
    A VNF's ONAP internal network **MAY** have more than one subnet.
    

.. container:: note

    :need:`R-86972`

    A VNF **SHOULD** create the ONAP internal network in the VNF's Heat
    Orchestration Template's Base Module.
    

.. container:: note

    :need:`R-52425`

    A VNF's port connected to an ONAP internal network **MUST**
    use the port for the purpose of reaching VMs in the same VNF.
    

.. container:: note

    :need:`R-22688`

    When a VNF's Heat Orchestration Template creates an ONAP internal network
    (per the ONAP definition, see Requirements R-52425 and R-46461
    and R-35666) and the ONAP internal network needs to be shared between
    modules within a VNF, the ONAP
    internal network **MUST** be created either in the

    * the base module
    * a nested YAML file invoked by the base module

    and the base module **MUST** contain an output parameter that provides
    either the network UUID or network name.

    * If the network UUID value is used to reference the network, the output
      parameter name in the base module **MUST** follow the naming convention
      ``int_{network-role}_net_id``
    * If the network name in is used to reference the network, the output
      parameter name in the base template **MUST** follow the naming convention
      ``int_{network-role}_net_name``

    The ``{network-role}`` **MUST** be the network-role of the ONAP
    internal network created in the Base Module.

    The Base Module Output Parameter MUST be declared in the ``parameters:``
    section of the Incremental Module(s) where the ``OS::Neutron::Port``
    resource(s) is attaching to the ONAP internal network.
    

.. container:: note

    :need:`R-87096`

    A VNF **MAY** contain zero, one or more than one ONAP internal network.
    

ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > parameters
--------------------------------------------------------------------------------------------


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-35413`

    A VNF Heat Orchestration's template's base module **MAY** (or **MAY NOT**)
    contain the section ``parameters:``.
    

Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-35414`

    A VNF Heat Orchestration's template's incremental module and volume module
    **MUST** contain the section ``parameters:``.
    

.. container:: note

    :need:`R-90279`

    A VNF Heat Orchestration's template's parameter **MUST** be used

    - in a resource AND/OR
    - in a output parameter (in the outputs section)

    with the exception of the parameters for the ``OS::Nova::Server``
    resource property ``availability_zone``.
    

ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > resources
-------------------------------------------------------------------------------------------


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-23663`

    A VNF's Heat Orchestration template's base module
    **MAY** (or **MAY NOT**)
    contain the section ``resources:``.
    

Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-23664`

    A VNF's Heat Orchestration template's incremental
    module and volume module **MUST**
    contain the section ``resources:``.
    

Resource IDs
------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-82551`

    When a VNF's Heat Orchestration Template's resource is associated with a
    single ``{vm-type}`` and a single ONAP internal network (per the ONAP
    definition, see Requirements R-52425 and R-46461 and R-35666),
    the Resource ID **MUST**
    contain both the ``{vm-type}`` and the ``int_{network-role}`` and

    - the ``{vm-type}`` **MUST** appear before the ``int_{network-role}`` and
      **MUST** be separated by an underscore '_'

      - (e.g., ``{vm-type}_int_{network-role}``,
        ``{vm-type}_{index}_int_{network-role}``)

    - note that an ``{index}`` value **MAY** separate the
      ``{vm-type}`` and the ``int_{network-role}`` and when this occurs
      underscores **MUST** separate the three values.
      (e.g., ``{vm-type}_{index}_int_{network-role}``).
    

.. container:: note

    :need:`R-27970`

    When a VNF's Heat Orchestration Template's resource is associated with
    more than one ``{vm-type}`` and/or more than one ONAP internal network
    (per the ONAP definition, see Requirements R-52425 and R-46461 and R-35666)
    and/or ONAP external network (per the ONAP definition, see Requirement
    R-57424 and R-16968), the Resource ID **MAY** contain the term
    ``shared`` and/or **MAY**
    contain text that identifies the VNF.
    

.. container:: note

    :need:`R-67793`

    When a VNF's Heat Orchestration Template's resource is associated
    with more than one ``{vm-type}`` and/or more than one ONAP internal network
    (per the ONAP definition, see Requirements R-52425 and R-46461 and R-35666)
    and/or
    ONAP external network (per the ONAP definition, see Requirement R-57424
    and R-16968), the Resource ID **MUST NOT** contain the
    ``{vm-type}`` and/or ``{network-role}``/``int_{network-role}``.
    

.. container:: note

    :need:`R-82115`

    When a VNF's Heat Orchestration Template's resource is associated with a
    single ``{vm-type}``
    and a single ONAP
    external network, the Resource ID text **MUST** contain both
    the ``{vm-type}``
    and the ``{network-role}``

    - the ``{vm-type}`` **MUST** appear before the ``{network-role}`` and
      **MUST** be separated by an underscore '_'


      - e.g., ``{vm-type}_{network-role}``, ``{vm-type}_{index}_{network-role}``


    - note that an ``{index}`` value **MAY** separate the ``{vm-type}`` and the
      ``{network-role}`` and when this occurs underscores **MUST** separate the
      three values.  (e.g., ``{vm-type}_{index}_{network-role}``).
    

.. container:: note

    :need:`R-98138`

    When a VNF's Heat Orchestration Template's resource is associated with a
    single ONAP internal network (per the ONAP definition, see
    Requirements R-52425 and R-46461 and R-35666), the Resource ID **MUST**
    contain the text
    ``int_{network-role}``.
    

.. container:: note

    :need:`R-96482`

    When a VNF's Heat Orchestration Template's resource is associated
    with a single ONAP external network, the Resource ID **MUST** contain the
    text ``{network-role}``.
    

Resource IDs > Contrail Heat Resources Resource ID Naming Convention > OS::ContrailV2::InstanceIp
-------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-62187`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` Resource ID
    that is configuring an IPv4 Address on a virtual machine interface
    (i.e., OS::ContrailV2::VirtualMachineInterface)
    attached to an ONAP internal network (per the ONAP definition, see
    Requirements R-52425 and R-46461 and R-35666)
    **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_int_{network-role}_vmi_{vmi_index}_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP internal network
      that the port is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    * ``IP`` signifies that an IPv4 address is being configured
    * ``{index}`` references the instance of the IPv4 address configured
      on the virtual machine interface.  The ``{index}`` is a numeric value
      that **MUST** start at zero on an
      instance of a virtual machine interface and **MUST** increment by one
      each time a new IPv4 address is configured on the
      virtual machine interface.
    

.. container:: note

    :need:`R-87563`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` Resource ID
    that is configuring an IPv6 Address on a virtual machine interface
    (i.e., OS::ContrailV2::VirtualMachineInterface)
    attached to an ONAP internal network (per the ONAP definition, see
    Requirements R-52425 and R-46461 and R-35666)
    **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_int_{network-role}_vmi_{vmi_index}_v6_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP internal network
      that the port is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    * ``v6_IP`` signifies that an IPv6 address is being configured
    * ``{index}`` references the instance of the IPv6 address configured
      on the virtual machine interface.  The ``{index}`` is a numeric value
      that **MUST** start at zero on an
      instance of a virtual machine interface and **MUST** increment by one
      each time a new IPv6 address is configured on the
      virtual machine interface.
    

.. container:: note

    :need:`R-53310`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` Resource ID
    that is configuring an IPv4 Address on a virtual machine interface
    (i.e., OS::ContrailV2::VirtualMachineInterface)
    attached to an ONAP external network (per the ONAP definition,
    see Requirement R-57424 and R-16968)
    **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_{network-role}_vmi_{vmi_index}_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP external
      network that the virtual machine interface is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    * ``IP`` signifies that an IPv4 address is being configured
    * ``{index}`` references the instance of the IPv4 address configured
      on the virtual machine interface.  The ``{index}`` is a numeric value
      that **MUST** start at zero on an
      instance of a virtual machine interface and **MUST** increment by one
      each time a new IPv4 address is configured on the
      virtual machine interface.
    

.. container:: note

    :need:`R-46128`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` Resource ID
    that is configuring an IPv6 Address on a virtual machine interface
    (i.e., OS::ContrailV2::VirtualMachineInterface)
    attached to an ONAP external network (per the ONAP definition,
    see Requirement R-57424 and R-16968)
    **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_{network-role}_vmi_{vmi_index}_v6_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP external network
      that the port is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    * ``v6_IP`` signifies that an IPv6 address is being configured
    * ``{index}`` references the instance of the IPv6 address configured
      on the virtual machine interface.  The ``{index}`` is a numeric value
      that **MUST** start at zero on an
      instance of a virtual machine interface and **MUST** increment by one
      each time a new IPv6 address is configured on the
      virtual machine interface.
    

Resource IDs > Contrail Heat Resources Resource ID Naming Convention > OS::ContrailV2::NetworkIpam
--------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-30753`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::NetworkIpam``
    Resource ID
    **MUST**
    contain the ``{network-role}`` of the ONAP internal network (per the ONAP
    definition, see Requirements R-52425 and R-46461 and R-35666) that the
    resource is associated with.
    

Resource IDs > Contrail Heat Resources Resource ID Naming Convention > OS::ContrailV2::VirtualMachineInterface
--------------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-50468`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualMachineInterface`` Resource ID
    that is attaching to an ONAP internal network (per the ONAP definition, see
    Requirements R-52425 and R-46461 and R-35666)
    **MUST** use the naming convention

    * ``{vm-type}_{vm-type_index}_int_{network-role}_vmi_{vmi_index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP internal network
      that the port (i.e. virtual machine interface) is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    

.. container:: note

    :need:`R-96253`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualMachineInterface`` Resource ID
    that is attaching to an ONAP external network (per the ONAP definition,
    see Requirement R-57424 and R-16968)
    **MUST** use the naming convention

    * ``{vm-type}_{vm-type_index}_{network-role}_vmi_{vmi_index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP external network
      that the port (i.e. virtual machine interface) is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    

Resource IDs > Contrail Heat Resources Resource ID Naming Convention > OS::ContrailV2::VirtualNetwork
-----------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-99110`

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualNetwork`` Resource ID **MUST** use the naming
    convention

    * ``int_{network-role}_network``

    VNF Heat Orchestration Templates can only create ONAP internal networks
    (per the ONAP definition, see Requirements R-52425 and R-46461 and R-35666).
    There is no ``{index}`` after ``{network-role}`` because ``{network-role}``
    **MUST** be unique in the scope of the VNF's
    Heat Orchestration Template.
    

Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Neutron::Net
----------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-25720`

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Net``
    Resource ID **MUST** use the naming convention

    * ``int_{network-role}_network``

    VNF Heat Orchestration Templates can only create ONAP internal networks
    (per the ONAP definition, see Requirements R-52425 and R-46461 and R-35666).
    There is no ``{index}`` after ``{network-role}`` because ``{network-role}``
    **MUST** be unique in the scope of the VNF's
    Heat Orchestration Template.
    

Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Neutron::Port
-----------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-20453`

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    that is attaching to an ONAP external network (per the ONAP definition,
    see Requirement R-57424 and R-16968), the ``OS::Neutron::Port``
    Resource ID
    **MUST** use the naming convention

    * ``{vm-type}_{vm-type_index}_{network-role}_port_{port-index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP external network
      that the port is attached to
    * ``{port_index}`` references the instance of the port on the ``{vm-type}``
      attached to ``{network-role}`` network.  The
      ``{port_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new port is defined on the instance of the ``{vm-type}`` attached to
      ``{network-role}`` network.
    

.. container:: note

    :need:`R-68520`

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    that is creating a *Reserve Port* with an IPv6 address, the
    ``OS::Neutron::Port`` Resource ID
    **SHOULD** use the naming convention

    * ``reserve_port_{vm-type}_{network-role}_floating_v6_ip_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{network-role}`` is the network-role of the ONAP external network
      that the port is attached to
    * ``{index}`` is the instance of the IPv6 *Reserve Port*
      for the vm-type attached to the network of ``{network-role}``.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).
    

.. container:: note

    :need:`R-26351`

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    that is attaching to an ONAP internal network
    (per the ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    the ``OS::Neutron::Port`` Resource ID **MUST**
    use the naming convention

    * ``{vm-type}_{vm-type_index}_int_{network-role}_port_{port-index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP internal network
      that the port is attached to
    * ``{port_index}`` references the instance of the port on the ``{vm-type}``
      attached to ``{network-role}`` network.  The
      ``{port_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new port is defined on the instance of the ``{vm-type}`` attached to
      ``{network-role}`` network.
    

.. container:: note

    :need:`R-27469`

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    that is creating a *Reserve Port* with an IPv4 address, the
    ``OS::Neutron::Port`` Resource ID
    **SHOULD** use the naming convention

    * ``reserve_port_{vm-type}_{network-role}_floating_ip_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{network-role}`` is the network-role of the ONAP external network
      that the port is attached to
    * ``{index}`` is the instance of the IPv4 *Reserve Port*
      for the vm-type attached to the network of ``{network-role}``.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).
    

Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Neutron::SecurityGroup
--------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-17334`

    A VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::SecurityGroup``
    that is applicable to one ``{vm-type}`` and one ONAP external network
    (per the ONAP definition, see Requirement R-57424 and R-16968),
    the ``OS::Neutron::SecurityGroup`` Resource ID
    **SHOULD** use the naming convention

    * ``{vm-type}_{network-role}_security_group``

    where

    * ``{vm-type}`` is the vm-type
    * ``{network-role}`` is the network-role of the ONAP external network
    

.. container:: note

    :need:`R-08775`

    A VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::SecurityGroup``
    that is applicable to one ``{vm-type}`` and more than one network
    (ONAP internal network
    and/or ONAP external network), the ``OS::Neutron::SecurityGroup``
    Resource ID **SHOULD** use the naming convention

    * ``{vm-type}_security_group``

    where

    * ``{vm-type}`` is the vm-type
    

.. container:: note

    :need:`R-03595`

    A VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::SecurityGroup`` that
    is applicable to more than one ``{vm-type}`` and one ONAP external network
    (per the ONAP definition, see Requirement R-57424 and R-16968),
    the ``OS::Neutron::SecurityGroup`` Resource ID
    **SHOULD** use the naming convention

    * ``{network-role}_security_group``

    where

    * ``{network-role}`` is the network-role of the ONAP external network
    

.. container:: note

    :need:`R-14198`

    A VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::SecurityGroup`` that
    is applicable to one {vm-type} and one ONAP internal network
    (per the ONAP definition, see Requirements R-52425 and R-46461 and
    R-35666), the
    ``OS::Neutron::SecurityGroup`` Resource ID **SHOULD**
    use the naming convention

    * ``{vm-type}_int_{network-role}_security_group``

    where

    * ``{vm-type}`` is the vm-type
    * ``{network-role}`` is the network-role of the ONAP internal network
    

.. container:: note

    :need:`R-30005`

    A VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::SecurityGroup`` that
    is applicable to more than one ``{vm-type}`` and more than one network
    (internal and/or external), the ``OS::Neutron::SecurityGroup`` Resource ID
    **MAY**
    use the naming convention

    * ``shared_security_group``

    or

    * ``{vnf-type}_security_group``

    where

    * ``{vnf-type}`` describes the VNF
    

.. container:: note

    :need:`R-73213`

    A VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::SecurityGroup`` that
    is applicable to more than one ``{vm-type}`` and one ONAP internal network,
    (per the ONAP definition, see Requirements R-52425 and R-46461 and
    R-35666), the ``OS::Neutron::SecurityGroup`` Resource ID
    **SHOULD** use the naming convention

    * ``int_{network-role}_security_group``

    where

    * ``{network-role}`` is the network-role of the ONAP internal network
    

Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Neutron::Subnet
-------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-59434`

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Subnet``
    Resource ID **SHOULD** use the naming convention

    * ``int_{network-role}_subnet_{index}``

    where

    * ``{network-role}`` is the network-role of the ONAP internal network
      (per the ONAP definition, see Requirements R-52425 and R-46461 and
      R-35666).
    * ``{index}`` is the ``{index}`` of the subnet of the ONAP internal network.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).
    

Resource IDs > OpenStack Heat Resources Resource ID Naming Convention > OS::Nova::Keypair
-----------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-24997`

    A VNF's Heat Orchestration Template's Resource ``OS::Nova::Keypair``
    that applies to one ``{vm-type}``, the ``OS::Nova::Keypair``
    Resource ID **SHOULD** use the naming convention

    * ``{vm-type}_keypair_{index}``

    where

    * ``{vm-type}`` is the vm-type of the ``OS::Nova::Server``
    * ``{index}`` is the ``{index}`` of the keypair.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).
    

.. container:: note

    :need:`R-65516`

    A VNF's Heat Orchestration Template's Resource ``OS::Nova::Keypair``
    that applies to all Virtual Machines in the VNF, the
    ``OS::Nova::Keypair`` Resource ID **SHOULD** use the naming
    convention

    * ``{vnf-type}_keypair``

    where

    * ``{vnf-type}`` describes the VNF
    

Resource: OS::Neutron::Port - Parameters > Introduction > Items to Note
-----------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-18001`

    If the VNF's ports connected to a unique ONAP internal network
    (per the ONAP definition, see Requirements R-52425 and R-46461 and R-35666)
    and the port's IP addresses are statically assigned IP addresses,
    the IPv4 addresses **MAY** be from different subnets and the
    IPv6 addresses **MAY** be from different subnets.
    

.. container:: note

    :need:`R-63956`

    If the VNF's ports connected to a unique ONAP external network
    (per the ONAP definition, see Requirement R-57424 and R-16968)
    and the port's IP addresses are ONAP SDN-C assigned IP addresses,
    the IPv4 addresses **MAY** be from different subnets and the IPv6
    addresses **MAY** be from different subnets.
    

.. container:: note

    :need:`R-48880`

    If a VNF's Port is attached to an ONAP external network (per the ONAP
    definition, see Requirement R-57424 and R-16968) and the port's
    IP addresses are assigned by ONAP's SDN-Controller,
    the ``OS::Neutron::Port`` Resource's

    * property ``fixed_ips`` map property ``ip_address`` **MUST** be used
    * property ``fixed_ips`` map property ``subnet``
      **MUST NOT** be used
    

.. container:: note

    :need:`R-70964`

    If a VNF's Port is attached to an ONAP internal network
    (per the ONAP definition, see Requirements R-52425 and R-46461 and R-35666)
    and the port's
    IP addresses are statically assigned by the VNF's Heat Orchestration
    Template (i.e., enumerated in the Heat Orchestration Template's
    environment file), the ``OS::Neutron::Port`` Resource's

    * property ``fixed_ips`` map property ``ip_address`` **MUST** be used
    * property ``fixed_ips`` map property ``subnet``
      **MUST NOT** be used
    

Resource: OS::Neutron::Port - Parameters > Property: allowed_address_pairs, Map Property: ip_address > VIP Assignment, ONAP External Networks
---------------------------------------------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-41492`

    When the VNF's Heat Orchestration Template's resource
    ``OS::Neutron::Port`` is attaching to an ONAP external network
    (per the ONAP definition, see Requirement R-57424 and R-16968),
    and the IPv4 VIP is required to be supported by the ONAP data model,
    the property ``allowed_address_pairs`` map property ``ip_address``
    parameter name **MUST** follow the naming convention

    * ``{vm-type}_{network-role}_floating_ip``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the ONAP external network

    And the parameter **MUST** be declared as type ``string``.

    As noted in the introduction to this section, the ONAP data model
    can only support one IPv4 VIP address.
    

.. container:: note

    :need:`R-83412`

    If a VNF's Heat Orchestration Template's resource
    ``OS::Neutron::Port`` is attaching to an ONAP external network (per the
    ONAP definition, see Requirement R-57424 and R-16968), the
    property ``allowed_address_pairs``
    map property ``ip_address`` parameter(s)
    **MUST NOT** be enumerated in the
    VNF's Heat Orchestration Template's Environment File.
    

.. container:: note

    :need:`R-41493`

    When the VNF's Heat Orchestration Template's resource
    ``OS::Neutron::Port`` is attaching to an ONAP external network
    (per the ONAP definition, see Requirement R-57424 and R-16968),
    and the IPv4 VIP address and/or IPv6 VIP address
    is **not** supported by the ONAP data model,
    the property ``allowed_address_pairs`` map property ``ip_address``

    * Parameter name **MAY** use any naming convention.  That is, there is no
      ONAP mandatory parameter naming convention.
    * Parameter **MAY** be declared as type ``string`` or type
    ``comma_delimited_list``.

    And the ``OS::Neutron::Port`` resource **MUST** contain
    resource-level ``metadata`` (not property-level).

    And the ``metadata`` format **MUST**  must contain the
    key value ``aap_exempt`` with a list of all
    ``allowed_address_pairs`` map property ``ip_address`` parameters
    **not** supported by the ONAP data model.
    

.. container:: note

    :need:`R-35735`

    When the VNF's Heat Orchestration Template's resource
    ``OS::Neutron::Port`` is attaching to an ONAP external network
    (per the ONAP definition, see Requirement R-57424 and R-16968),
    and the IPv6 VIP is required to be supported by the ONAP data model,
    the property ``allowed_address_pairs`` map property ``ip_address``
    parameter name **MUST** follow the naming convention

    * ``{vm-type}_{network-role}_floating_v6_ip``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the ONAP external network

    And the parameter **MUST** be declared as type ``string``.

    As noted in the introduction to this section, the ONAP data model
    can only support one IPv6 VIP address.
    

Resource: OS::Neutron::Port - Parameters > Property: allowed_address_pairs, Map Property: ip_address > VIP Assignment, ONAP Internal Networks
---------------------------------------------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-717227`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    and an IPv4 Virtual IP (VIP)
    address is assigned using the property ``allowed_address_pairs``
    map property ``ip_address``,
    the parameter name **MUST** follow the
    naming convention

    - ``{vm-type}_int_{network-role}_floating_ip``

    where

    - ``{vm-type}`` is the {vm-type} associated with the
      OS::Nova::Server
    - ``{network-role}`` is the {network-role} of the ONAP internal
      network

    And the parameter **MUST** be declared as ``type: string``
    and **MUST** be enumerated in the environment file.

    OR

    the parameter name **MUST** follow the
    naming convention

    - ``{vm-type}_int_{network-role}_floating_ips``

    where

    - ``{vm-type}`` is the {vm-type} associated with the
      OS::Nova::Server
    - ``{network-role}`` is the {network-role} of the ONAP internal
      network

    And the parameter **MUST** be declared as ``type: comma_delimited_list``
    and **MUST** be enumerated in the environment file.
    

.. container:: note

    :need:`R-805572`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    and an IPv6 Virtual IP (VIP)
    address is assigned
    using the property ``allowed_address_pairs``
    map property ``ip_address``,
    the parameter name **MUST** follow the
    naming convention

    - ``{vm-type}_int_{network-role}_floating_v6_ip``

    where

    - ``{vm-type}`` is the {vm-type} associated with the
      OS::Nova::Server
    - ``{network-role}`` is the {network-role} of the ONAP internal
      network

    And the parameter **MUST** be declared as ``type: string``
    and **MUST** be enumerated in the environment file

    OR

    the parameter name **MUST** follow the
    naming convention

    - ``{vm-type}_int_{network-role}_floating_v6_ips``

    where

    - ``{vm-type}`` is the {vm-type} associated with the
      OS::Nova::Server
    - ``{network-role}`` is the {network-role} of the ONAP internal
      network

    And the parameter **MUST** be declared as ``type: comma_delimited_list``
    and **MUST** be enumerated in the environment file.
    

Resource: OS::Neutron::Port - Parameters > Property: fixed_ips, Map Property: ip_address
----------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-27818`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
    ``string``,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_int_{network-role}_v6_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the ONAP internal network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one
    

.. container:: note

    :need:`R-40971`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an ONAP external network (per the
    ONAP definition, see Requirement R-57424 and R-16968),
    and an IPv4 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a string,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_{network-role}_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the ONAP external network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one
    

.. container:: note

    :need:`R-04697`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an ONAP external network (per the
    ONAP definition, see Requirement R-57424 and R-16968),
    and an IPv4 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_{network-role}_ips``

      where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the ONAP external
        network
    

.. container:: note

    :need:`R-78380`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    and an IPv4 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is
    defined as a ``string``,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_int_{network-role}_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the
      ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the ONAP internal network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one
    

.. container:: note

    :need:`R-23503`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an ONAP external network (per the
    ONAP definition, see Requirement R-57424 and R-16968),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_{network-role}_v6_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        OS::Nova::Server
      * ``{network-role}`` is the {network-role} of the ONAP external
        network
    

.. container:: note

    :need:`R-85235`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    and an IPv4 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the ONAP internal
        network
    

.. container:: note

    :need:`R-93496`

    The VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    property ``fixed_ips``
    map property ``ip_address``
    parameter associated with an ONAP internal network, i.e.,

     * ``{vm-type}_int_{network-role}_ip_{index}``
     * ``{vm-type}_int_{network-role}_v6_ip_{index}``
     * ``{vm-type}_int_{network-role}_ips``
     * ``{vm-type}_int_{network-role}_v6_ips``


    **MUST** be enumerated in the Heat Orchestration
    Template's Environment File and IP addresses **MUST** be
    assigned.
    

.. container:: note

    :need:`R-71577`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an ONAP external network (per the
    ONAP definition, see Requirement R-57424 and R-16968),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a string,
    the parameter name **MUST** follow the
    naming convention

    * ``{vm-type}_{network-role}_v6_ip_{index}``

    where

    * ``{vm-type}`` is the {vm-type} associated with the
      ``OS::Nova::Server``
    * ``{network-role}`` is the {network-role} of the ONAP external network
    * ``{index}`` is a numeric value that **MUST** start at zero in a
      VNF's Heat Orchestration Template and **MUST** increment by one
    

.. container:: note

    :need:`R-62590`

    The VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    property ``fixed_ips``
    map property ``ip_address``
    parameter associated with an ONAP external network, i.e.,

     * ``{vm-type}_{network-role}_ip_{index}``
     * ``{vm-type}_{network-role}_v6_ip_{index}``
     * ``{vm-type}_{network-role}_ips``
     * ``{vm-type}_{network-role}_v6_ips``


    **MUST NOT** be enumerated in the Heat Orchestration
    Template's Environment File.  ONAP provides the IP address
    assignments at orchestration time.
    

.. container:: note

    :need:`R-29765`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    and an IPv6 address is assigned
    using the property ``fixed_ips``
    map property ``ip_address`` and the parameter type is defined as a
    ``comma_delimited_list``,
    the parameter name **MUST** follow the
    naming convention

      * ``{vm-type}_int_{network-role}_v6_ips``

    where

      * ``{vm-type}`` is the {vm-type} associated with the
        ``OS::Nova::Server``
      * ``{network-role}`` is the {network-role} of the ONAP internal
        network
    

Resource: OS::Neutron::Port - Parameters > Property: fixed_ips, Map Property: subnet
------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-76160`

    When

    * the VNF's Heat Orchestration Template's
      resource ``OS::Neutron::Port`` in an Incremental Module is attaching
      to an ONAP internal network (per the ONAP definition, see Requirements
      R-52425 and R-46461 and R-35666)
      that is created in the Base Module, AND
    * an IPv6 address is being cloud assigned by OpenStack's DHCP Service AND
    * the ONAP internal network IPv6 subnet is to be specified
      using the property ``fixed_ips`` map property ``subnet``,

    the parameter **MUST** follow the naming convention

    * ``int_{network-role}_v6_subnet_id``

    where ``{network-role}`` is the network role of the ONAP internal network.

    Note that the parameter **MUST** be defined as an ``output`` parameter in
    the base module.
    

.. container:: note

    :need:`R-15287`

    When the VNF's Heat Orchestration Template's
    resource ``OS::Neutron::Port`` is attaching
    to an ONAP external network (per the ONAP definition, see
    Requirement R-57424 and R-16968),
    and an IPv6 address is being cloud assigned by OpenStack's DHCP Service
    and the ONAP external network IPv6 subnet is to be specified
    using the property ``fixed_ips``
    map property ``subnet``, the parameter
    **MUST** follow the naming convention

      * ``{network-role}_v6_subnet_id``

    where

      * ``{network-role}`` is the network role of the ONAP external network.
    

.. container:: note

    :need:`R-62802`

    When the VNF's Heat Orchestration Template's
    resource ``OS::Neutron::Port`` is attaching
    to an ONAP external network (per the ONAP definition, see
    Requirement R-57424 and R-16968),
    and an IPv4 address is being cloud assigned by OpenStack's DHCP Service
    and the ONAP external network IPv4 subnet is to be specified
    using the property ``fixed_ips``
    map property ``subnet``, the parameter
    **MUST** follow the naming convention

      * ``{network-role}_subnet_id``

    where

      * ``{network-role}`` is the network role of the ONAP external network.
    

.. container:: note

    :need:`R-84123`

    When

      * the VNF's Heat Orchestration Template's
        resource ``OS::Neutron::Port`` in an Incremental Module is attaching
        to an ONAP internal network (per the ONAP definition, see
        Requirements R-52425 and R-46461 and R-35666)
        that is created in the Base Module, AND
      * an IPv4 address is being cloud assigned by OpenStack's DHCP Service AND
      * the internal network IPv4 subnet is to be specified
        using the property ``fixed_ips`` map property ``subnet``,

    the parameter **MUST** follow the naming convention

      * ``int_{network-role}_subnet_id``

    where

      * ``{network-role}`` is the network role of the ONAP internal network

    Note that the parameter **MUST** be defined as an ``output`` parameter in
    the base module.
    

Resource: OS::Neutron::Port - Parameters > Property: network
------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-86182`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port``
    is in an incremental module and
    is attaching to an ONAP internal network (per the
    ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    the ``network`` parameter name **MUST**

      * follow the naming convention ``int_{network-role}_net_id`` if the
        network UUID value is used to reference the network
      * follow the naming convention ``int_{network-role}_net_name`` if the
        network name in is used to reference the network.

    where ``{network-role}`` is the network-role of the ONAP internal network
    and a ``get_param`` **MUST** be used as the intrinsic function.
    

.. container:: note

    :need:`R-62983`

    When the VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::Port`` is attaching to an ONAP external network (per the
    ONAP definition, see Requirement R-57424 and R-16968), the
    ``network`` parameter name **MUST**

      * follow the naming convention ``{network-role}_net_id`` if the Neutron
        network UUID value is used to reference the network
      * follow the naming convention ``{network-role}_net_name`` if the
        OpenStack network name is used to reference the network.

    where ``{network-role}`` is the network-role of the ONAP external network
    and a ``get_param`` **MUST** be used as the intrinsic function.
    

Resource: OS::Nova::Server Metadata Parameters > vf_module_index
----------------------------------------------------------------


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-55307`

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
    

VNF Security > VNF General Security Requirements
------------------------------------------------


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-353637`

    Containerized components of VNFs **SHOULD** follow the recommendations for
    Container Base Images and Build File Configuration in the latest available version
    of the CIS Docker Community Edition Benchmarks to ensure that containerized VNFs
    are secure. All non-compliances with the benchmarks MUST be documented.
    

.. container:: note

    :need:`R-381623`

    Containerized components of VNFs **SHOULD** execute in a Docker run-time environment
    that follows the Container Runtime Configuration in the latest available version
    of the CIS Docker Community Edition Benchmarks to ensure that containerized VNFs
    are secure. All non-compliances with the benchmarks MUST be documented.
    

Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-842258`

    The VNF **MUST** include a configuration (e.g. a heat template or CSAR package)
    that specifies the targeted parameters (e.g. a limited set of ports)
    over which the VNF will communicate; including internal, external and
    management communication.
    

.. container:: note

    :need:`R-19082`

    The VNF **MUST** not contain undocumented functionality.
    

.. container:: note

    :need:`R-46986`

    The VNF provider **MUST** follow GSMA vendor practices and SEI CERT Coding
    Standards when developing the VNF in order to minimize the risk of
    vulnerabilities. See GSMA NESAS Network Equipment Security Assurance Scheme –
    Development and Lifecycle Security Requirements Version 1.0 (https://www.gsma.com/
    security/wp-content/uploads/2019/11/FS.16-NESAS-Development-and-Lifecycle-Security-
    Requirements-v1.0.pdf) and SEI CERT Coding Standards (https://wiki.sei.cmu.edu/
    confluence/display/seccode/SEI+CERT+Coding+Standards).
    

.. container:: note

    :need:`R-19768`

    The VNF **SHOULD** support the separation of (1) signaling and payload traffic
    (i.e., customer facing traffic), (2) operations, administration and management
    traffic, and (3) internal VNF traffic (i.e., east-west traffic such as storage
    access) using technologies such as VPN and VLAN.
    

.. container:: note

    :need:`R-86261`

    The VNF **MUST** be able to authenticate and authorize all remote access.
    

.. container:: note

    :need:`R-62498`

    The VNF **MUST** support only encrypted access protocols, e.g., TLS,
    SSH, SFTP.
    

.. container:: note

    :need:`R-56904`

    The VNF **MUST** interoperate with the ONAP (SDN) Controller so that
    it can dynamically modify the firewall rules, ACL rules, QoS rules, virtual
    routing and forwarding rules. This does not preclude the VNF providing other
    interfaces for modifying rules.
    

Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-23882

    The VNF **SHOULD** provide the capability for the Operator to run security
    vulnerability scans of the operating system and all application layers.
    

.. container:: note

    R-343842

    The VNF **MUST**, after a successful login at command line or a GUI,
    display the last valid login date and time and the number of unsuccessful
    attempts since then made with that user's ID. This requirement is only
    applicable when the user account is defined locally in the VNF.
    

.. container:: note

    R-40813

    The VNF **SHOULD** support the use of virtual trusted platform
    module.
    

VNF Security > VNF Identity and Access Management Requirements
--------------------------------------------------------------


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-251639`

    The VNF **MUST** provide explicit confirmation of a session termination
    such as a message, new page, or rerouting to a login page.
    

.. container:: note

    :need:`R-358699`

    The VNF **MUST** support at least the following roles: system administrator,
    application administrator, network function O&M.
    

.. container:: note

    :need:`R-373737`

    The VNF **MUST**, if not integrated with the operator's IAM system, provide
    a mechanism for assigning roles and/or permissions to an identity.
    

Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-86835`

    The VNF **MUST** set the default settings for user access
    to deny authorization, except for a super user type of account.
    

.. container:: note

    :need:`R-814377`

    The VNF **MUST** have the capability of allowing the Operator to create,
    manage, and automatically provision user accounts using one of the protocols
    specified in Chapter 7.
    

.. container:: note

    :need:`R-231402`

    The VNF **MUST** provide a means to explicitly logout, thus ending that session.
    

.. container:: note

    :need:`R-81147`

    The VNF **MUST**, if not integrated with the Operator’s Identity and
    Access Management system, support multifactor authentication on all
    protected interfaces exposed by the VNF for use by human users.
    

.. container:: note

    :need:`R-78010`

    The VNF **MUST** support LDAP in order to integrate with an external identity
    and access manage system. It MAY support other identity and access management
    protocols.
    

.. container:: note

    :need:`R-79107`

    The VNF **MUST**, if not integrated with the Operator’s Identity
    and Access Management system, support the ability to lock out the
    userID after a configurable number of consecutive unsuccessful
    authentication attempts using the same userID. The locking mechanism
    must be reversible by an administrator and should be reversible after
    a configurable time period.
    

.. container:: note

    :need:`R-42874`

    The VNF **MUST** allow the Operator to restrict access to protected
    resources based on the assigned permissions associated with an ID in
    order to support Least Privilege (no more privilege than required to
    perform job functions).
    

.. container:: note

    :need:`R-581188`

    The VNF **MUST NOT** identify the reason for a failed authentication,
    only that the authentication failed.
    

.. container:: note

    :need:`R-23135`

    The VNF **MUST**, if not integrated with the Operator's identity and
    access management system, authenticate all access to protected resources.
    

.. container:: note

    :need:`R-479386`

    The VNF **MUST** provide the capability of setting a configurable message
    to be displayed after successful login. It MAY provide a list of supported
    character sets.
    

.. container:: note

    :need:`R-931076`

    The VNF **MUST** support account names that contain at least A-Z, a-z,
    and 0-9 character sets and be at least 6 characters in length.
    

.. container:: note

    :need:`R-45719`

    The VNF **MUST**, if not integrated with the Operator's Identity and Access
    Management system, enforce a configurable "terminate idle sessions"
    policy by terminating the session after a configurable period of inactivity.
    

Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-15671

    The VNF **MUST** provide access controls that allow the Operator
    to restrict access to VNF functions and data to authorized entities.
    

.. container:: note

    R-71787

    Each architectural layer of the VNF (eg. operating system, network,
    application) **MUST** support access restriction independently of all
    other layers so that Segregation of Duties can be implemented.
    

.. container:: note

    R-85419

    The VNF **SHOULD** support OAuth 2.0 authorization using an external
    Authorization Server.
    

VNF and PNF On-boarding and package management > Resource Configuration
-----------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-89571`

    The VNF or PNF PROVIDER **MUST** provide artifacts for configuration
    management using at least one of the following technologies;
    a) Netconf/YANG, b) Chef, or c) Ansible.
    

VNF or PNF CSAR Package > VNF or PNF Package Contents
-----------------------------------------------------


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-972082`

    If the Manifest file in the PNF CSAR package includes "onap_pnf_sw_information"
    as a non-MANO artifact set identifiers, then the PNF software information file is
    included in the package and it **MUST** be compliant to:

    - The file extension which contains the PNF software version must be .yaml

    - The PNF software version information must be specified as following:

    .. code-block:: yaml

       pnf_software_information:

        - pnf_software_version:  "<version>"
    

Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-40820`

    The VNF or PNF CSAR PACKAGE **MUST** enumerate all of the open source
    licenses their VNF(s) incorporate. CSAR License directory as per ETSI
    SOL004.

    for example ROOT\\Licenses\\ **License_term.txt**
    

.. container:: note

    :need:`R-795126`

    The VNF CSAR package Manifest file **MUST** start with the VNF
    package metadata in the form of a name-value pairs. Each pair shall appear
    on a different line. The name is specified as following:

      - vnf_provider_id

      - vnf_product_name

      - vnf_release_date_time

      - vnf_package_version
    

.. container:: note

    :need:`R-01123`

    The VNF or PNF CSAR package Manifest file **MUST** contain: VNF or PNF
    package meta-data, a list of all artifacts (both internal and
    external) entry's including their respected URI's, as specified
    in ETSI GS NFV-SOL 004
    

.. container:: note

    :need:`R-221914`

    The VNF or PNF CSAR package **MUST** contain a human-readable change log text
    file. The Change Log file keeps a history describing any changes in the VNF
    or PNF package. The Change Log file is kept up to date continuously from
    the creation of the CSAR package.
    

.. container:: note

    :need:`R-57019`

    The PNF CSAR PACKAGE Manifest file **MUST** start with the PNF
    package metadata in the form of a name-value pairs. Each pair shall appear
    on a different line. The name is specified as following:

      - pnfd_provider

      - pnfd_name

      - pnfd_release_date_time

      - pnfd_archive_version
    

.. container:: note

    :need:`R-146092`

    If one or more non-MANO artifact(s) is included in the VNF or PNF CSAR
    package, the Manifest file in this CSAR package **MUST** contain one or more
    of the following ONAP non-MANO artifact set identifier(s):

      - onap_ves_events: contains VES registration files

      - onap_pm_dictionary: contains the PM dictionary files

      - onap_yang_modules: contains Yang module files for configurations

      - onap_ansible_playbooks: contains any ansible_playbooks

      - onap_pnf_sw_information: contains the PNF software information file

      - onap_others: contains any other non_MANO artifacts, e.g. informational
        documents

     *NOTE: According to ETSI SOL004 v.2.6.1, every non-MANO artifact set shall be
     identified by a non-MANO artifact set identifier which shall be registered in
     the ETSI registry. Approved ONAP non-MANO artifact set identifiers are documented
     in the following page* https://wiki.onap.org/display/DW/ONAP+Non-MANO+Artifacts+Set+Identifiers
    

VNF or PNF CSAR Package > VNF or PNF Package Structure and Format
-----------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-506221`

    The VNF or PNF CSAR file **MUST** be a zip file with .csar extension.
    

.. container:: note

    :need:`R-87234`

    The VNF or PNF CSAR package provided by a VNF or PNF vendor **MUST** be with
    TOSCA-Metadata directory (CSAR Option 1) as specified in
    ETSI GS NFV-SOL004.

    **Note:** SDC supports only the CSAR Option 1 in Dublin. The Option 2
    will be considered in future ONAP releases.
    

{network-role}
--------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-21330`

    A VNF's Heat Orchestration Template's Resource property parameter that is
    associated with an ONAP
    external network **MUST** include the ``{network-role}``
    as part of the parameter name.
    

.. container:: note

    :need:`R-84322`

    A VNF's Heat Orchestration Template's Resource property parameter that
    is associated with an ONAP internal network (per the ONAP definition, see
    Requirements R-52425 and R-46461 and R-35666)
    **MUST** include
    ``int_{network-role}`` as part of the parameter name,
    where ``int_`` is a hard coded string.
    

.. container:: note

    :need:`R-96983`

    A VNF's Heat Orchestration Template's Resource ID that is associated
    with an ONAP internal network (per the ONAP definition, see Requirements
    R-52425 and R-46461 and R-35666)
    **MUST** include ``int_{network-role}`` as part
    of the Resource ID, where ``int_`` is a hard coded string.
    

.. container:: note

    :need:`R-11168`

    A VNF's Heat Orchestration Template's Resource ID that is associated with
    an ONAP external network **MUST** include the ``{network-role}`` as part
    of the resource ID.
    

.. container:: note

    :need:`R-69014`

    When a VNF's port connects to an ONAP internal network or ONAP
    external network,
    a network role, referred to
    as the ``{network-role}`` **MUST** be assigned to the network for
    use in the VNF's Heat Orchestration Template.  The ``{network-role}``
    is used in the VNF's Heat Orchestration Template's resource IDs
    and resource property parameter names.
    
