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


Ansible JSON Key Value Description
-------------------------------------------------------------

The following provides the key value pairs that must be contained in the
JSON file supporting APPC/SDN-C Ansible action.

Table B1. Ansible JSON File key value description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: **TOSCA Definition**
   :file: Ansible JSON File Key Value Description.csv
   :header-rows: 1
   :align: center
   :widths: auto

Ansible JSON file example:

.. code-block:: json

  {
    "Action":"Configure",
    "PlaybookName": "<VNFCode>/<Version>/ansible/configure/site.yml",
    "NodeList": [
      {
        "vnfc_type": "oam",
        "ne_id_vip": "vfdb9904vm001oam001",
        "floating_ip_address_vip": "1xx.2yy.zzz.109",
        "site": "wp0ny",
        "vm_info": [
          {
            "ne_id": "vfdb9904vm001oam001",
            "fixed_ip_address": "1xx.2yy.zzz.109"
          },
          {
            "ne_id": "vfdb9904vm002oam001",
            "fixed_ip_address": "1xx.2yy.zzz.110"
          }
        ]
      },
      {
        "vnfc_type": "rdb",
        "site": "wp0ny",
        "vm_info": [
          {
            "ne_id": "vfdb9904vm003rdb001",
            "fixed_ip_address": "1xx.2yy.zzz.105"
          },
          {
            "ne_id": "vfdb9904vm004rdb001",
            "fixed_ip_address": "1xx.2yy.zzz.106"
          }
        ]
      }
    ],
    "Timeout": 60,
    "InventoryNames": "None",
    "EnvParameters": {"vnf_instance": "$vnf-instance", "Retry": 3, "Wait": 5, "ConfigFile":"config.txt", "healthcheck_type": "$healthcheck_type",  "target_vm_list": ["$ne-id1","..."] },
    "FileParameters": {"config.txt":"db_ip=10.1.1.1, sip_timer=10000"}
  }

In the above example, the Ansible Server Rest API code will:

#. Process the "FileParameters" dictionary and generate a file named
   'config.txt' with contents set to the value of the 'config.txt' key.

#. Execute the playbook named '<VNFCode>/<Version>/ansible/configure/site.yml'
   on nodes with listed IP addresses (or FQDNs) respectively while providing
   the following key value pairs to the playbook: Retry=3, Wait=5,
   ConfigFile=config.txt

#. If execution time of the playbook exceeds 60 secs (across all hosts),
   it will be terminated.

#. Inventory hosts file to be build with only IP addresses (or FQDNs), IP
   addresses and VM names, or IP addresses and VNFC names depending on
   InventoryNames setting in the template(s) passed to Ansible Server as part
   of the Rest API request. In a later section with Ansible examples, examples
   of supported inventory hosts file formats are shared.

