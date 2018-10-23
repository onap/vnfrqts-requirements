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
JSON file supporting Ansible action.

Table B1. Ansible JSON File key value description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------+----------------------+---------+----------------------------+
| **Field Name**| **Description**      | **Type**| **Comment**                |
+===============+======================+=========+============================+
| PlaybookName  | VNF providor must    |Mandatory|Currently following         |
|               | list name of the     |         |Ansible standard            |
|               | playbook relative    |         |naming, where main          |
|               | path used to         |         |playbook is always          |
|               | execute the VNF      |         |named site.yml, and         |
|               | action.              |         |directory name where        |
|               |                      |         |this main playbook resides, |
|               |                      |         |is named after the          |
|               |                      |         |command/action playbook     |
|               |                      |         |performs, in lower case,    |
|               |                      |         |example, configure.         |
+---------------+----------------------+---------+----------------------------+
| Action        | Name of VNF action.  | Optional|                            |
+---------------+----------------------+---------+----------------------------+
| EnvParameters | A JSON dictionary    | Optional|Depends on the VNF action.  |
|               | which should list key|         |                            |
|               | value pairs to be    |         |Attribute names (variable   |
|               | passed to the Ansible|         |names) passed to Ansible    |
|               | playbook. These      |         |shall follow Ansible valid  |
|               | values would         |         |variable names: "Variable   |
|               | correspond to        |         |names should be letters,    |
|               | instance specific    |         |numbers, and underscores.   |
|               | parameters that a    |         |Variables should always     |
|               | playbook may need to |         |start with a letter."       |
|               | execute an action.   |         |                            |
+---------------+----------------------+---------+----------------------------+
| NodeList      |Ansible inventory     | Optional|If not provided, pre-loaded |
|               |hosts file with       |         |(VNF) inventory hosts       |
|               |VNF groups and        |         |file must exist in the      |
|               |respective IP         |         |Ansible Server otherwise    |
|               |addresses or DNS      |         |request fails.              |
|               |supported FQDNs       |         |                            |
|               |that the playbook must|         |                            |
|               |be executed against.  |         |                            |
+---------------+----------------------+---------+----------------------------+
| FileParameters| A JSON dictionary    | Optional| Depends on the VNF action  |
|               | where keys are       |         | and playbook design.       |
|               | filenames and values |         |                            |
|               | are contents of      |         |                            |
|               | files. The Ansible   |         |                            |
|               | Server will utilize  |         |                            |
|               | this feature to      |         |                            |
|               | generate files with  |         |                            |
|               | keys as filenames and|         |                            |
|               | values as content.   |         |                            |
|               | This attribute can be|         |                            |
|               | used to generate     |         |                            |
|               | files that a playbook|         |                            |
|               | may require as part  |         |                            |
|               | of execution.        |         |                            |
+---------------+----------------------+---------+----------------------------+
| Timeout       | Time (in seconds)    | Optional|                            |
|               | that a playbook is   |         |                            |
|               | expected to take to  |         |                            |
|               | finish execution for |         |                            |
|               | the VNF. If playbook |         |                            |
|               | execution time       |         |                            |
|               | exceeds this value,  |         |                            |
|               | Ansible Server will  |         |                            |
|               | terminate the        |         |                            |
|               | playbook process.    |         |                            |
+---------------+----------------------+---------+----------------------------+

Ansible JSON file example:

.. code-block:: json

  {

    "Action":"Configure",

    "PlaybookName": "<VNFCode>/<Version>/ansible/configure/site.yml",

    "NodeList": ["test1.vnf_b.onap.com", "test2.vnf_b.onap.com"],

    "Timeout": 60,

    "EnvParameters": {"Retry": 3, "Wait": 5, "ConfigFile":"config.txt"},

    "FileParameters": {"config.txt":"db_ip=10.1.1.1, sip_timer=10000"}

  }

In the above example, the Ansible Server will:

a. Process the "FileParameters" dictionary and generate a file named
   ‘config.txt’ with contents set to the value of the ‘config.txt’ key.

b. Execute the playbook named ‘<VNFCode>/<Version>/ansible/configure/site.yml’
   on nodes with    FQDNs test1.vnf\_b.onap.com and test2.vnf\_b.onap.com
   respectively while providing the following key value pairs to the playbook:
   Retry=3, Wait=5, ConfigFile=config.txt


c. If execution time of the playbook exceeds 60 secs (across all hosts),
   it will be terminated.

