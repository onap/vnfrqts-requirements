.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

Suggested Naming Convention for Common Parameters
-------------------------------------------------

Many VNFs use the parameters in the table below are used in user_data.
The table below provides a suggested naming convention for these common
parameters.

Netmask
^^^^^^^

.. csv-table:: **Table 8: Suggested Naming Convention for Common Parameters:  Netmask**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   {network-role}_subnet_<index>_netmask, string,
   int_<network-role>_subnet_<index>_netmask, string,
   {network-role}_v6_subnet_<index>_netmask , string,
   int_{network-role}_v6_subnet_<index>_netmask, string,

CIDR
^^^^

.. csv-table:: **Table 9: Suggested Naming Convention for Common Parameters:  CIDR**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   <network-role>_subnet_<index>_cidr, string,
   int_<network-role>_subnet_<index>_cidr, string,
   <network-role>_v6_subnet_<index>_cidr, string,
   int_<network-role>_v6_subnet_<index>_cidr, string,

Default Gateway
^^^^^^^^^^^^^^^

.. csv-table:: **Table 10: Suggested Naming Convention for Common Parameters:  Default Gateway**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   {network-role}_subnet_<index>_default_gateway, string,
   {network-role}_v6_subnet_<index>_default_gateway, string,

DCAE Collector IP Address
^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: **Table 11: Suggested Naming Convention for Common Parameters:  DCAE Collector Address**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   dcae_collector_ip_<index>, string,
   dcae_collector_v6_ip_<index>, string,

NTP Server IP Address
^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: **Table 12: Suggested Naming Convention for Common Parameters:  NTP Server IP Address**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   ntp_ip_<index>, string,
   ntp_v6_ip_<index>, string,

DNS
^^^

.. csv-table:: **Table 13: Suggested Naming Convention for Common Parameters:  DCAE Collector Address**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   dns_{network-role}_ip_<index>, string,
   dns_{network-role}_v6_ip_<index>, string,

Security Group
^^^^^^^^^^^^^^

.. csv-table:: **Table 14: Suggested Naming Convention for Common Parameters:  Security Group**
   :header: Parameter Name,Parameter Type,Notes
   :align: center
   :widths: auto

   {vm-type}_security_group, string, Security Group applicable to one {vm-type} and more than one network (internal and/or external)
   {network-role}_security_group, string, Security Group applicable to more than one {vm-type} and one external network
   int_{network-role}_security_group, string, Security Group applicable to more than one {vm-type} and one internal network
   {vm-type}_{network-role}_security_group, string, Security Group applicable to one {vm-type} and one external network
   {vm-type}_int_{network-role}_security_group, string, Security Group applicable to one {vm-type} and one internal network
   shared_security_group, string, Security Group applicable to more than one {vm-type} and more than one network (internal and/or external)
