.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

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
|               | values would         |         |variable names: “Variable   |
|               | correspond to        |         |names should be letters,    |
|               | instance specific    |         |numbers, and underscores.   |
|               | parameters that a    |         |Variables should always     |
|               | playbook may need to |         |start with a letter.”       |
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

{

      “Action”:”Configure”,

      "PlaybookName": "<VNFCode>/<Version>/ansible/configure/site.yml",

      "NodeList": ["test1.vnf\_b.onap.com", “test2.vnf\_b.onap.com”],

      "Timeout": 60,

      "EnvParameters": {"Retry": 3, "Wait": 5, “ConfigFile”:”config.txt”},

      “FileParameters”:{“config.txt”:”db\_ip=10.1.1.1, sip\_timer=10000”}

}

In the above example, the Ansible Server will:

a. Process the “FileParameters” dictionary and generate a file named
   ‘config.txt’ with contents set to the value of the ‘config.txt’ key.

b. Execute the playbook named ‘<VNFCode>/<Version>/ansible/configure/site.yml’
   on nodes with    FQDNs test1.vnf\_b.onap.com and test2.vnf\_b.onap.com
   respectively while providing the following key value pairs to the playbook:
   Retry=3, Wait=5, ConfigFile=config.txt


c. If execution time of the playbook exceeds 60 secs (across all hosts),
   it will be terminated.

.. [1]
   The “name” field is a mandatory field in a valid Chef Node Object
   JSON dictionary.

.. [2]
   Not currently supported in ONAP release 1

.. [3]
   https://github.com/mbj4668/pyang

.. [4]
   Upstream elements must provide the appropriate FQDN in the request to
   ONAP for the desired action.

.. [5]
   Refer to NCSP’s Network Cloud specification

.. [6]
   This option is not currently supported in ONAP and it is currently
   under consideration.

.. [7]
   Multiple ONAP actions may map to one playbook.


