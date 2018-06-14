.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.


Appendix
========

Chef JSON Key Value Description
-------------------------------------

The following provides the key value pairs that must be contained in the
JSON file supporting Chef action.

Table A1. Chef JSON File key value description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------+--------------------------+---------+----------------------+
| **Field Name** | **Description**          | **Type**| **Comment**          |
+================+==========================+=========+======================+
| Environment    | A JSON dictionary        | Optional|Depends on VNF action.|
|                | representing a Chef      |         |                      |
|                | Environment object. If   |         |                      |
|                | the VNF action requires  |         |                      |
|                | loading or modifying Chef|         |                      |
|                | environment attributes   |         |                      |
|                | associated with the VNF, |         |                      |
|                | all the relevant         |         |                      |
|                | information must be      |         |                      |
|                | provided in this JSON    |         |                      |
|                | dictionary in a structure|         |                      |
|                | that conforms to a Chef  |         |                      |
|                | Environment Object.      |         |                      |
+----------------+--------------------------+---------+----------------------+
| Node           | A JSON dictionary        |Mandatory|                      |
|                | representing a Chef Node |         |                      |
|                | Object.                  |         |                      |
|                |                          |         |                      |
|                | The Node JSON dictionary |         |                      |
|                | must include the run list|         |                      |
|                | to be triggered for the  |         |                      |
|                | desired VNF action by the|         |                      |
|                | push job. It should also |         |                      |
|                | include any attributes   |         |                      |
|                | that need to be          |         |                      |
|                | configured on the Node   |         |                      |
|                | Object as part of the VNF|         |                      |
|                | action.                  |         |                      |
+----------------+--------------------------+---------+----------------------+
| NodeList       | Array of FQDNs that      |Mandatory|                      |
|                | correspond to the        |         |                      |
|                | endpoints (VMs) of a VNF |         |                      |
|                | registered with the Chef |         |                      |
|                | Server that need to      |         |                      |
|                | trigger a chef-client run|         |                      |
|                | as part of the desired   |         |                      |
|                | VNF action.              |         |                      |
+----------------+--------------------------+---------+----------------------+
| PushJobFlag    | This field indicates     |Mandatory| If set to “True”,    |
|                | whether the VNF action   |         | ONAP will request a  |
|                | requires a push Job. Push|         | push job. Ignored    |
|                | job object will be       |         | otherwise.           |
|                | created by ONAP if       |         |                      |
|                | required.                |         |                      |
+----------------+--------------------------+---------+----------------------+
| CallbackCapable| This field indicates if  | Optional| If Chef cookbook is  |
|                | the chef-client run      |         | callback capable, VNF|
|                | invoked by push job      |         | owner is required to |
|                | corresponding to the VNF |         | set it to “True”.    |
|                | action is capable of     |         | Ignored otherwise.   |
|                | posting results on a     |         |                      |
|                | callback URL.            |         |                      |
+----------------+--------------------------+---------+----------------------+
| GetOutputFlag  | Flag which indicates     |Mandatory| ONAP will retrieve   |
|                | whether ONAP should      |         | output from          |
|                | retrieve output generated|         | NodeObject attributes|
|                | in a chef-client run from|         | [‘PushJobOutput’] for|
|                | Node object attribute    |         | all nodes in NodeList|
|                | node[‘PushJobOutput’] for|         | if set to “True”.    |
|                | this VNF action (e.g., in|         | Ignored otherwise.   |
|                | Audit).                  |         |                      |
+----------------+--------------------------+---------+----------------------+

Chef Template example:

.. code-block:: chef

 “Environment”:{
      "name": "HAR",
      "description": "VNF Chef environment for HAR",
      "json\_class": "Chef::Environment",
      "chef\_type": "environment",
      "default\_attributes": { },
      "override\_attributes": {
            “Retry\_Time”:”50”,
            “MemCache”: “1024”,
            “Database\_IP”:”10.10.1.5”
      },
 }
 }
 “Node”: {
      “name” : “signal.network.com “
      "chef\_type": "node",
      "json\_class": "Chef::Node",
      "attributes": {
            “IPAddress1”: “192.168.1.2”,
            “IPAddress2”:”135.16.162.5”,
            “MyRole”:”BE”
      },
      "override": {},
      "default": {},
      “normal”:{},
      “automatic”:{},
      “chef\_environment” : “\_default”
      "run\_list": [ "configure\_signal" ]
      },
      “NodeList”:[“node1.vnf\_a.onap.com”, “node2.vnf\_a.onap.com”],
      “PushJobFlag”: “True”
      “CallbackCapable”:True
      “GetOutputFlag” : “False”
 }

The example JSON file provided by the VNF provider for each VNF action will be
turned into a template by ONAP, that can be updated with instance
specific values at run-time.

Some points worth noting regarding the JSON fields:

a. The JSON file must be created for each action for each VNF.

b. If a VNF action involves multiple endpoints (VMs) of a VNF, ONAP will
   replicate the “Node” JSON dictionary in the template and post it to
   each FQDN (i.e., endpoint) in the NodeList after setting the “name”
   field in the Node object to be the respective FQDN [1]_. Hence, it
   is required that all end points (VMs) of a VNF involved in a VNF
   action support the same set of Node Object attributes.

The following table describes the JSON dictionary to post in Callback.

Table A2. JSON Dictionary to Post in Callback
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------+----------------------------+---------+-----------------------+
| **Key**      | **Description**            | **Type**| **Comment**           |
+==============+============================+=========+=======================+
| RequestId    | A unique string associated |Mandatory|                       |
|              | with the original request  |         |                       |
|              | by ONAP. This key-value    |         |                       |
|              | pair will be provided by   |         |                       |
|              | ONAP in the environment of |         |                       |
|              | the push job request and   |         |                       |
|              | must be returned as part of|         |                       |
|              | the POST message.          |         |                       |
+--------------+----------------------------+---------+-----------------------+
| StatusCode   | An integer that must be set|Mandatory|                       |
|              | to 200 if chef-client run  |         |                       |
|              | on the node finished       |         |                       |
|              | successfully 500 otherwise.|         |                       |
+--------------+----------------------------+---------+-----------------------+
| StatusMessage| A string which must be set |Mandatory|                       |
|              | to ‘SUCCESS’ if StatusCode |         |                       |
|              | was 200                    |         |                       |
|              |                            |         |                       |
|              | Appropriate error message  |         |                       |
|              | otherwise.                 |         |                       |
+--------------+----------------------------+---------+-----------------------+
| Name         | A string which corresponds |Mandatory|                       |
|              | to the name of the node    |         |                       |
|              | where push job is run. It  |         |                       |
|              | is required that the value |         |                       |
|              | be retrieved from the node |         |                       |
|              | object attributes (where it|         |                       |
|              | is always defined).        |         |                       |
+--------------+----------------------------+---------+-----------------------+
| PushJobOutput| Any output from the        |Optional | Depends on VNF action.|
|              | chef-client run that needs |         | If empty, it must not |
|              | to be returned to ONAP.    |         | be included.          |
+--------------+----------------------------+---------+-----------------------+

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

VNF License Information Guidelines
------------------------------------------------------------

This Appendix describes the metadata to be supplied for VNF licenses.

1. General Information

Table C1 defines the required and optional fields for licenses.

Table C1. Required Fields for General Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------+-----------------------------------+--------------+----------+
| **Field Name**| **Description**                   | **Data Type**| **Type** |
+===============+===================================+==============+==========+
| VNF Provider  | The name of the VNF provider.     | String       | Mandatory|
| Name          |                                   |              |          |
+---------------+-----------------------------------+--------------+----------+
| VNF Provider  | The name of the product to which  | String       | Mandatory|
| Product       | this agreement applies.           |              |          |
|               |                                   |              |          |
|               | Note: a contract/agreement may    |              |          |
|               | apply to more than one VNF        |              |          |
|               | provider product. In that case,   |              |          |
|               | provide the metadata for each     |              |          |
|               | product separately.               |              |          |
+---------------+-----------------------------------+--------------+----------+
| VNF Provider  | A general description of VNF      | String       | Optional |
| Product       | provider software product.        |              |          |
| Description   |                                   |              |          |
+---------------+-----------------------------------+--------------+----------+
| Export Control| ECCNs are 5-character             | String       | Mandatory|
| Classification| alpha-numeric designations used on|              |          |
| Number (ECCN) | the Commerce Control List (CCL) to|              |          |
|               | identify dual-use items for export|              |          |
|               | control purposes. An ECCN         |              |          |
|               | categorizes items based on the    |              |          |
|               | nature of the product, i.e. type  |              |          |
|               | of commodity, software, or        |              |          |
|               | technology and its respective     |              |          |
|               | technical parameters.             |              |          |
+---------------+-----------------------------------+--------------+----------+
| Reporting     | A list of any reporting           | List of      | Optional |
| Requirements  | requirements on the usage of the  | strings      |          |
|               | software product.                 |              |          |
+---------------+-----------------------------------+--------------+----------+

1. Entitlements

Entitlements describe software license use rights. The use rights may be
quantified by various metrics: # users, # software instances, # units.
The use rights may be limited by various criteria: location (physical or
logical), type of customer, type of device, time, etc.

One or more entitlements can be defined; each one consists of the
following fields:

Table C2. Required Fields for Entitlements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------+-----------------------------------+-------------+-----------+
| **Field Name**| **Description**                   |**Data Type**| **Type**  |
+===============+===================================+=============+===========+
| VNF Provider  | Identifier for the entitlement as | String      | Mandatory |
| Part Number / | described by the VNF provider in  |             |           |
| Manufacture   | their price list / catalog /      |             |           |
| Reference     | contract.                         |             |           |
| Number        |                                   |             |           |
+---------------+-----------------------------------+-------------+-----------+
| Description   | Verbiage that describes the       | String      | Optional  |
|               | entitlement                       |             |           |
+---------------+-----------------------------------+-------------+-----------+
| Entitlement   | Each entitlement defined must be  | String      | Mandatory |
| Identifier    | identified by a unique value (e.g.|             |           |
|               | numbered 1, 2, 3….)               |             |           |
+---------------+-----------------------------------+-------------+-----------+
| Minimum Order | The minimum number of entitlements| Number      | Mandatory |
| Requirement   | that need to be purchased.        |             |           |
|               | For example, the entitlements must|             |           |
|               | be purchased in a block of 100. If|             |           |
|               | no minimum is required, the value |             |           |
|               | will be zero.                     |             |           |
+---------------+-----------------------------------+-------------+-----------+
| Unique        | A list of any reporting           | List of     | Optional  |
| Reporting     | requirements on the usage of the  | Strings     |           |
| Requirements  | software product. (e.g.: quarterly|             |           |
|               | usage reports are required)       |             |           |
+---------------+-----------------------------------+-------------+-----------+
| License Type  | Type of license applicable to the | String      | Mandatory |
|               | software product. (e.g.:          |             |           |
|               | fixed-term, perpetual, trial,     |             |           |
|               | subscription.)                    |             |           |
+---------------+-----------------------------------+-------------+-----------+
| License       | Valid values:                     | String      |Conditional|
| Duration      |                                   |             |           |
|               | **year**, **quarter**, **month**, |             |           |
|               | **day**.                          |             |           |
|               |                                   |             |           |
|               | Not applicable when license type  |             |           |
|               | is Perpetual.                     |             |           |
+---------------+-----------------------------------+-------------+-----------+
| License       | Number of years, quarters, months,| Number      |Conditional|
| Duration      | or days for which the license is  |             |           |
| Quantification| valid.                            |             |           |
|               |                                   |             |           |
|               | Not applicable when license type  |             |           |
|               | is Perpetual.                     |             |           |
+---------------+-----------------------------------+-------------+-----------+
| Limits        | see section C.4 for possible      | List        | Optional  |
|               | values                            |             |           |
+---------------+-----------------------------------+-------------+-----------+

1. License Keys

This section defines information on any License Keys associated with the
Software Product. A license key is a data string (or a file) providing a
means to authorize the use of software. License key does not provide
entitlement information.

License Keys are not required. Optionally, one or more license keys can
be defined; each one consists of the following fields:

Table C3. Required Fields for License Keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------+-----------------------------------+--------------+----------+
| **Field Name**| **Description**                   | **Data Type**| **Type** |
+===============+===================================+==============+==========+
| Description   | Verbiage that describes the       | String       | Mandatory|
|               | license key                       |              |          |
+---------------+-----------------------------------+--------------+----------+
| License Key   | Each license key defined must be  | String       | Mandatory|
| Identifier    | identified by a unique value      |              |          |
|               | (e.g., numbered 1, 2, 3….)        |              |          |
+---------------+-----------------------------------+--------------+----------+
| Key Function  | Lifecycle stage (e.g.,            | String       | Optional |
|               | Instantiation or Activation) at   |              |          |
|               | which the license key is applied  |              |          |
|               | to the software.                  |              |          |
+---------------+-----------------------------------+--------------+----------+
| License Key   | Valid values:                     | String       | Mandatory|
| Type          |                                   |              |          |
|               | **Universal, Unique**             |              |          |
|               |                                   |              |          |
|               | **Universal** - a single license  |              |          |
|               | key value that may be used with   |              |          |
|               | any number of instances of the    |              |          |
|               | software.                         |              |          |
|               |                                   |              |          |
|               | **Unique**- a unique license key  |              |          |
|               | value is required for each        |              |          |
|               | instance of the software.         |              |          |
+---------------+-----------------------------------+--------------+----------+
| Limits        | see section C.4 for possible      | List         | Optional |
|               | values                            |              |          |
+---------------+-----------------------------------+--------------+----------+

1. Entitlement and License Key Limits

Limitations on the use of software entitlements and license keys may be
based on factors such as: features enabled in the product, the allowed
capacity of the product, number of installations, etc... The limits may
generally be categorized as:

-  where (location)

-  when (time)

-  how (usages)

-  who/what (entity)

-  amount (how much)

Multiple limits may be applicable for an entitlement or license key.
Each limit may further be described by limit behavior, duration,
quantification, aggregation, aggregation interval, start date, end date,
and threshold.

When the limit is associated with a quantity, the quantity is relative
to an instance of the entitlement or license key. For example:

-  Each entitlement grants the right to 50 concurrent users. If 10
   entitlements are purchased, the total number of concurrent users
   permitted would be 500. In this example, the limit category is
   **amount**, the limit type is **users**, and the limit
   **quantification** is **50.**

   Each license key may be installed on 3 devices. If 5 license keys are
   acquired, the total number of devices allowed would be 15. In this
   example, the limit category is **usages**, the limit type is
   **device**, and the limit **quantification** is **3.**

1. Location

Locations may be logical or physical location (e.g., site, country). For
example:

-  use is allowed in Canada

Table C4. Required Fields for Location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------+--------------------------------+--------------+----------+
| **Field Name**   | **Description**                | **Data Type**| **Type** |
+==================+================================+==============+==========+
| Limit Identifier | Each limit defined for an      | String       | Mandatory|
|                  | entitlement or license key must|              |          |
|                  | be identified by a unique value|              |          |
|                  | (e.g., numbered 1,2,3…)        |              |          |
+------------------+--------------------------------+--------------+----------+
| Limit Description| Verbiage describing the limit. | String       | Mandatory|
+------------------+--------------------------------+--------------+----------+
| Limit Behavior   | Description of the actions     | String       | Mandatory|
|                  | taken when the limit boundaries|              |          |
|                  | are reached.                   |              |          |
+------------------+--------------------------------+--------------+----------+
| Limit Category   | Valid value: **location**      | String       | Mandatory|
+------------------+--------------------------------+--------------+----------+
| Limit Type       | Valid values: **city, county,  | String       | Mandatory|
|                  | state, country, region, MSA,   |              |          |
|                  | BTA, CLLI**                    |              |          |
+------------------+--------------------------------+--------------+----------+
| Limit List       | List of locations where the VNF| List of      | Mandatory|
|                  | provider Product can be used or| String       |          |
|                  | needs to be restricted from use|              |          |
+------------------+--------------------------------+--------------+----------+
| Limit Set Type   | Indicates if the list is an    | String       | Mandatory|
|                  | inclusion or exclusion.        |              |          |
|                  |                                |              |          |
|                  | Valid Values:                  |              |          |
|                  |                                |              |          |
|                  | **Allowed**                    |              |          |
|                  |                                |              |          |
|                  | **Not allowed**                |              |          |
+------------------+--------------------------------+--------------+----------+
| Limit            | The quantity (amount) the limit| Number       | Optional |
| Quantification   | expresses.                     |              |          |
+------------------+--------------------------------+--------------+----------+

1. Time

Limit on the length of time the software may be used. For example:

-  license key valid for 1 year from activation

-  entitlement valid from 15 May 2018 thru 30 June 2020

Table C5. Required Fields for Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------+-------------------------------+--------------+-----------+
| **Field Name**   | **Description**               | **Data Type**| **Type**  |
+==================+===============================+==============+===========+
| Limit Identifier | Each limit defined for an     | String       | Mandatory |
|                  | entitlement or license key    |              |           |
|                  | must be identified by a unique|              |           |
|                  | value (e.g., numbered)        |              |           |
+------------------+-------------------------------+--------------+-----------+
| Limit Description| Verbiage describing the limit.| String       | Mandatory |
+------------------+-------------------------------+--------------+-----------+
| Limit Behavior   | Description of the actions    | String       | Mandatory |
|                  | taken when the limit          |              |           |
|                  | boundaries are reached.       |              |           |
|                  |                               |              |           |
|                  | The limit behavior may also   |              |           |
|                  | describe when a time limit    |              |           |
|                  | takes effect. (e.g., key is   |              |           |
|                  | valid for 1 year from date of |              |           |
|                  | purchase).                    |              |           |
+------------------+-------------------------------+--------------+-----------+
| Limit Category   | Valid value: **time**         | String       | Mandatory |
+------------------+-------------------------------+--------------+-----------+
| Limit Type       | Valid values:                 | String       | Mandatory |
|                  | **duration, date**            |              |           |
+------------------+-------------------------------+--------------+-----------+
| Limit List       | List of times for which the   | List of      | Mandatory |
|                  | VNF Provider Product can be   | String       |           |
|                  | used or needs to be restricted|              |           |
|                  | from use                      |              |           |
+------------------+-------------------------------+--------------+-----------+
| Duration Units   | Required when limit type is   | String       |Conditional|
|                  | duration. Valid values:       |              |           |
|                  | **perpetual, year, quarter,   |              |           |
|                  | month, day, minute, second,   |              |           |
|                  | millisecond**                 |              |           |
+------------------+-------------------------------+--------------+-----------+
| Limit            | The quantity (amount) the     | Number       | Optional  |
| Quantification   | limit expresses.              |              |           |
+------------------+-------------------------------+--------------+-----------+
| Start Date       | Required when limit type is   | Date         | Optional  |
|                  | date.                         |              |           |
+------------------+-------------------------------+--------------+-----------+
| End Date         | May be used when limit type is| Date         | Optional  |
|                  | date.                         |              |           |
+------------------+-------------------------------+--------------+-----------+

1. Usage

Limits based on how the software is used. For example:

-  use is limited to a specific sub-set of the features/capabilities the
   software supports

-  use is limited to a certain environment (e.g., test, development,
   production…)

-  use is limited by processor (vm, cpu, core)

-  use is limited by software release

Table C6. Required Fields for Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------+-------------------------------+---------------+----------+
| **Field Name**   | **Description**               | **Data Type** | **Type** |
+==================+===============================+===============+==========+
| Limit Identifier | Each limit defined for an     | String        | Mandatory|
|                  | entitlement or license key    |               |          |
|                  | must be identified by a unique|               |          |
|                  | value (e.g., numbered)        |               |          |
+------------------+-------------------------------+---------------+----------+
| Limit Description| Verbiage describing the limit.| String        | Mandatory|
+------------------+-------------------------------+---------------+----------+
| Limit Behavior   | Description of the actions    | String        | Mandatory|
|                  | taken when the limit          |               |          |
|                  | boundaries are reached.       |               |          |
+------------------+-------------------------------+---------------+----------+
| Limit Category   | Valid value: **usages**       | String        | Mandatory|
+------------------+-------------------------------+---------------+----------+
| Limit Type       | Valid values: **feature,      | String        | Mandatory|
|                  | environment, processor,       |               |          |
|                  | version**                     |               |          |
+------------------+-------------------------------+---------------+----------+
| Limit List       | List of usage limits (e.g.,   | List of String| Mandatory|
|                  | test, development, vm, core,  |               |          |
|                  | R1.2.1, R1.3.5…)              |               |          |
+------------------+-------------------------------+---------------+----------+
| Limit Set Type   | Indicates if the list is an   | String        | Mandatory|
|                  | inclusion or exclusion.       |               |          |
|                  |                               |               |          |
|                  | Valid Values:                 |               |          |
|                  |                               |               |          |
|                  | **Allowed**                   |               |          |
|                  |                               |               |          |
|                  | **Not allowed**               |               |          |
+------------------+-------------------------------+---------------+----------+
| Limit            | The quantity (amount) the     | Number        | Optional |
| Quantification   | limit expresses.              |               |          |
+------------------+-------------------------------+---------------+----------+

1. Entity

Limit on the entity (product line, organization, customer) allowed to
make use of the software. For example:

-  allowed to be used in support of wireless products

-  allowed to be used only for government entities

Table C7. Required Fields for Entity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------+--------------------------------+--------------+----------+
| **Field Name**   | **Description**                |**Data Type** | **Type** |
+==================+================================+==============+==========+
| Limit Identifier | Each limit defined for an      | String       | Mandatory|
|                  | entitlement or license key must|              |          |
|                  | be identified by a unique value|              |          |
|                  | (e.g., numbered)               |              |          |
+------------------+--------------------------------+--------------+----------+
| Limit Description| Verbiage describing the limit. | String       | Mandatory|
+------------------+--------------------------------+--------------+----------+
| Limit Behavior   | Description of the actions     | String       | Mandatory|
|                  | taken when the limit boundaries|              |          |
|                  | are reached.                   |              |          |
+------------------+--------------------------------+--------------+----------+
| Limit Category   | Valid value: **entity**        | String       | Mandatory|
+------------------+--------------------------------+--------------+----------+
| Limit Type       | Valid values: **product line,  | String       | Mandatory|
|                  | organization, internal         |              |          |
|                  | customer, external customer**  |              |          |
+------------------+--------------------------------+--------------+----------+
| Limit List       | List of entities for which the |List of String| Mandatory|
|                  | VNF Provider Product can be    |              |          |
|                  | used or needs to be restricted |              |          |
|                  | from use                       |              |          |
+------------------+--------------------------------+--------------+----------+
| Limit Set Type   | Indicates if the list is an    | String       | Mandatory|
|                  | inclusion or exclusion.        |              |          |
|                  |                                |              |          |
|                  | Valid Values:                  |              |          |
|                  |                                |              |          |
|                  | **Allowed**                    |              |          |
|                  |                                |              |          |
|                  | **Not allowed**                |              |          |
+------------------+--------------------------------+--------------+----------+
| Limit            | The quantity (amount) the limit| Number       | Optional |
| Quantification   | expresses.                     |              |          |
+------------------+--------------------------------+--------------+----------+

1. Amount

These limits describe terms relative to utilization of the functions of
the software (for example, number of named users permitted, throughput,
or capacity). Limits of this type may also be relative to utilization of
other resources (for example, a limit for firewall software is not based
on use of the firewall software, but on the number of network
subscribers).

The metadata describing this type of limit includes the unit of measure
(e.g., # users, # sessions, # MB, # TB, etc.), the quantity of units,
any aggregation function (e.g., peak or average users), and aggregation
interval (day, month, quarter, year, etc.).

Table C8. Required Fields for Amount
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------+---------------------------------+-------------+----------+
| **Field Name**   | **Description**                 |**Data Type**| **Type** |
+==================+=================================+=============+==========+
| Limit Identifier | Each limit defined for an       | String      | Mandatory|
|                  | entitlement or license key must |             |          |
|                  | be identified by a unique value |             |          |
|                  | (e.g., numbered)                |             |          |
+------------------+---------------------------------+-------------+----------+
| Limit Description| Verbiage describing the limit.  | String      | Mandatory|
+------------------+---------------------------------+-------------+----------+
| Limit Behavior   | Description of the actions taken| String      | Mandatory|
|                  | when the limit boundaries are   |             |          |
|                  | reached.                        |             |          |
+------------------+---------------------------------+-------------+----------+
| Limit Category   | Valid value: **amount**         | String      | Mandatory|
+------------------+---------------------------------+-------------+----------+
| Limit Type       | Valid values: **trunk, user,    | String      | Mandatory|
|                  | subscriber, session, token,     |             |          |
|                  | transactions, seats, KB, MB, TB,|             |          |
|                  | GB**                            |             |          |
+------------------+---------------------------------+-------------+----------+
| Type of          | Is the limit relative to        | String      | Mandatory|
| Utilization      | utilization of the functions of |             |          |
|                  | the software or relative to     |             |          |
|                  | utilization of other resources? |             |          |
|                  |                                 |             |          |
|                  | Valid values:                   |             |          |
|                  |                                 |             |          |
|                  | -  **software functions**       |             |          |
|                  |                                 |             |          |
|                  | -  **other resources**          |             |          |
+------------------+---------------------------------+-------------+----------+
| Limit            | The quantity (amount) the limit | Number      | Optional |
| Quantification   | expresses.                      |             |          |
+------------------+---------------------------------+-------------+----------+
| Aggregation      | Valid values: **peak, average** | String      | Optional |
| Function         |                                 |             |          |
+------------------+---------------------------------+-------------+----------+
| Aggregation      | Time period over which the      | String      | Optional |
| Interval         | aggregation is done (e.g.,      |             |          |
|                  | average sessions per quarter).  |             |          |
|                  | Required when an Aggregation    |             |          |
|                  | Function is specified.          |             |          |
|                  |                                 |             |          |
|                  | Valid values: **day, month,     |             |          |
|                  | quarter, year, minute, second,  |             |          |
|                  | millisecond**                   |             |          |
+------------------+---------------------------------+-------------+----------+
| Aggregation      | Is the limit quantity applicable| String      | Optional |
| Scope            | to a single entitlement or      |             |          |
|                  | license key (each separately)?  |             |          |
|                  | Or may the limit quantity be    |             |          |
|                  | combined with others of the same|             |          |
|                  | type (resulting in limit amount |             |          |
|                  | that is the sum of all the      |             |          |
|                  | purchased entitlements or       |             |          |
|                  | license keys)?                  |             |          |
|                  |                                 |             |          |
|                  | Valid values:                   |             |          |
|                  |                                 |             |          |
|                  | -  **single**                   |             |          |
|                  |                                 |             |          |
|                  | -  **combined**                 |             |          |
+------------------+---------------------------------+-------------+----------+
| Type of User     | Describes the types of users of | String      | Optional |
|                  | the functionality offered by the|             |          |
|                  | software (e.g., authorized,     |             |          |
|                  | named). This field is included  |             |          |
|                  | when Limit Type is user.        |             |          |
+------------------+---------------------------------+-------------+----------+

TOSCA model
-----------------------------

Table D1. ONAP Resource DM TOSCA/YAML constructs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Standard TOSCA/YAML definitions agreed by VNF SDK Modeling team to be used by
VNF vendors to create a standard VNF descriptor.

All definitions are summarized in the table below based on the agreed ONAP
Resource DM TOSCA/YAML constructs for Beijing. Their syntax is specified in
ETSI GS NFV-SOL001 stable draft for VNF-D.

+------------+------------------------------+---------------------------------+
| Requirement| Resource IM Info Elements    | TOSCA Constructs as per SOL001  |
| Number     |                              |                                 |
+============+==============================+=================================+
| R-02454    | VNFD.vnfSoftwareVersion      | For VDU.Compute -               |
|            |                              | tosca.artifacts.nfv.SwImage     |
|            |                              |                                 |
|            | SwImageDesc.Version          | For Virtual Storage -           |
|            |                              | tosca.artifacts.Deployment.Image|
+------------+------------------------------+---------------------------------+
| R-03070    | vnfExtCpd's with virtual     | tosca.nodes.nfv.VnfExtCp with a |
|            | NetworkInterfaceRequirements | property tosca.datatypes.nfv.\  |
|            | (vNIC)                       | VirtualNetworkInterface\        |
|            |                              | Requirements                    |
+------------+------------------------------+---------------------------------+
| R-09467    | VDU.Compute descriptor       | tosca.nodes.nfv.Vdu.Compute     |
+------------+------------------------------+---------------------------------+
| R-16065    | VDU.Compute. Configurable    | tosca.datatypes.nfv.Vnfc        |
|            | Properties                   | ConfigurableProperties          |
+------------+------------------------------+---------------------------------+
| R-30654    | VNFD.lifeCycleManagement     | Interface construct tosca.\     |
|            | Script - IFA011 LifeCycle\   | interfaces.nfv.vnf.lifecycle.Nfv|
|            | ManagementScript             | with a list of standard LCM     |
|            |                              | operations                      |
+------------+------------------------------+---------------------------------+
| R-35851    | CPD: VduCp, VnfExtCp,        | tosca.nodes.nfv.VduCp, tosca.\  |
|            | VnfVirtualLinkDesc, QoS      | nodes.nfv.VnfVirtualLink,       |
|            | Monitoring info element  -   | tosca.nodes.nfv.VnfExtCp        |
|            | TBD                          |                                 |
+------------+------------------------------+---------------------------------+
| R-41215    | VNFD/VDU Profile and scaling | tosca.datatypes.nfv.VduProfile  |
|            | aspect                       | and tosca.datatypes.nfv.\       |
|            |                              | ScalingAspect                   |
+------------+------------------------------+---------------------------------+
| R-66070    |  VNFD meta data              | tosca.datatypes.nfv.            |
|            |                              | VnfInfoModifiableAttributes -   |
|            |                              | metadata?                       |
+------------+------------------------------+---------------------------------+
| R-96634    | VNFD.configurableProperties  | tosca.datatypes.nfv.Vnf\        |
|            | describing scaling           | ConfigurableProperties,         |
|            | characteristics.  VNFD.\     | tosca.datatypes.nfv.ScaleInfo   |
|            | autoscale defines the rules  |                                 |
|            | for scaling based on specific|                                 |
|            | VNF  indications             |                                 |
+------------+------------------------------+---------------------------------+
| ?          |  VDU Virtual Storage         | tosca.nodes.nfv.Vdu.\           |
|            |                              | VirtualStorage                  |
+------------+------------------------------+---------------------------------+
| R-01478    | Monitoring Info Element (TBD)| tosca.capabilities.nfv.Metric - |
|            | - SOL001 per VNF/VDU/VLink   | type for monitoring             |
| R-01556    | memory-consumption,          |                                 |
|            | CPU-utilization,             | monitoring_parameter  of above  |
|            | bandwidth-consumption, VNFC  | type per VNF/VDU/VLink          |
|            | downtime, etc.               |                                 |
+------------+------------------------------+---------------------------------+


Table D2. TOSCA CSAR structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section defines the requirements around the CSAR structure.

The table below describes the numbered requirements for CSAR structure as
agreed with SDC. The format of the CSAR is specified in SOL004.

+------------+-------------------------------------+--------------------------+
| Requirement| Description                         | CSAR artifact directory  |
| Number     |                                     |                          |
+============+=====================================+==========================+
| R-26881    | The VNF provider MUST provide the   | ROOT\\Artifacts\         |
|            | binaries and images needed to       | \\VNF_Image.bin          |
|            | instantiate the VNF (VNF and VNFC   |                          |
|            | images).                            |                          |
+------------+-------------------------------------+--------------------------+
| R-30654    | VNFD.lifeCycleManagementScript that | ROOT\\Artifacts\         |
|            | includes a list of events and       | \\Informational\         |
|            | corresponding management scripts    | \\Install.csh            |
|            | performed for the VNF - SOL001      |                          |
+------------+-------------------------------------+--------------------------+
| R-35851    | All VNF topology related definitions| ROOT\\Definitions\       |
|            | in yaml files VNFD/Main Service     | \\VNFC.yaml              |
|            | template at the ROOT                |                          |
|            |                                     | ROOT\                    |
|            |                                     | \\MainService\           |
|            |                                     | \\Template.yaml          |
+------------+-------------------------------------+--------------------------+
| R-40827    | CSAR License directory - SOL004     | ROOT\\Licenses\          |
|            |                                     | \\License_term.txt       |
+------------+-------------------------------------+--------------------------+
| R-77707    | CSAR Manifest file - SOL004         | ROOT\                    |
|            |                                     | \\MainServiceTemplate.mf |
+------------+-------------------------------------+--------------------------+


Requirement List
--------------------------------

**VNF Development Requirements**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

VNF Design
~~~~~~~~~~~~~

R-58421 The VNF **SHOULD** be decomposed into granular re-usable VNFCs.

R-82223 The VNF **MUST** be decomposed if the functions have
significantly different scaling characteristics (e.g., signaling
versus media functions, control versus data plane functions).

R-16496 The VNF **MUST** enable instantiating only the functionality that
is needed for the decomposed VNF (e.g., if transcoding is not needed it
should not be instantiated).

R-02360 The VNFC **MUST** be designed as a standalone, executable process.

R-34484 The VNF **SHOULD** create a single component VNF for VNFCs
that can be used by other VNFs.

R-23035 The VNF **MUST** be designed to scale horizontally (more
instances of a VNF or VNFC) and not vertically (moving the existing
instances to larger VMs or increasing the resources within a VM)
to achieve effective utilization of cloud resources.

R-30650 The VNF **MUST** utilize cloud provided infrastructure and
VNFs (e.g., virtualized Local Load Balancer) as part of the VNF so
that the cloud can manage and provide a consistent service resiliency
and methods across all VNF's.

R-12709 The VNFC **SHOULD** be independently deployed, configured,
upgraded, scaled, monitored, and administered by ONAP.

R-37692 The VNFC **MUST** provide API versioning to allow for
independent upgrades of VNFC.

R-86585 The VNFC **SHOULD** minimize the use of state within
a VNFC to facilitate the movement of traffic from one instance
to another.

R-65134 The VNF **SHOULD** maintain state in a geographically
redundant datastore that may, in fact, be its own VNFC.

R-75850 The VNF **SHOULD** decouple persistent data from the VNFC
and keep it in its own datastore that can be reached by all instances
of the VNFC requiring the data.

R-88199 The VNF **MUST** utilize a persistent datastore service that
can meet the data performance/latency requirements. (For example:
Datastore service could be a VNFC in VNF or a DBaaS in the Cloud
execution environment)

R-99656 The VNF **MUST** NOT terminate stable sessions if a VNFC
instance fails.

R-84473 The VNF **MUST** enable DPDK in the guest OS for VNF’s requiring
high packets/sec performance.  High packet throughput is defined as greater
than 500K packets/sec.

R-54430 The VNF **MUST** use the NCSP’s supported library and compute
flavor that supports DPDK to optimize network efficiency if using DPDK. [5]_

R-18864 The VNF **MUST** NOT use technologies that bypass virtualization
layers (such as SR-IOV) unless approved by the NCSP (e.g., if necessary
to meet functional or performance requirements).

R-64768 The VNF **MUST** limit the size of application data packets
to no larger than 9000 bytes for SDN network-based tunneling when
guest data packets are transported between tunnel endpoints that
support guest logical networks.

R-74481 The VNF **MUST** NOT require the use of a dynamic routing
protocol unless necessary to meet functional requirements.

VNF Resiliency
~~~~~~~~~~~~~~~~~~~~~~~~~

R-52499 The VNF **MUST** meet their own resiliency goals and not rely
on the Network Cloud.

R-42207 The VNF **MUST** design resiliency into a VNF such that the
resiliency deployment model (e.g., active-active) can be chosen at
run-time.

R-03954 The VNF **MUST** survive any single points of failure within
the Network Cloud (e.g., virtual NIC, VM, disk failure).

R-89010 The VNF **MUST** survive any single points of software failure
internal to the VNF (e.g., in memory structures, JMS message queues).

R-67709 The VNF **MUST** be designed, built and packaged to enable
deployment across multiple fault zones (e.g., VNFCs deployed in
different servers, racks, OpenStack regions, geographies) so that
in the event of a planned/unplanned downtime of a fault zone, the
overall operation/throughput of the VNF is maintained.

R-35291 The VNF **MUST** support the ability to failover a VNFC
automatically to other geographically redundant sites if not
deployed active-active to increase the overall resiliency of the VNF.

R-36843 The VNF **MUST** support the ability of the VNFC to be deployable
in multi-zoned cloud sites to allow for site support in the event of cloud
zone failure or upgrades.

R-00098 The VNF **MUST NOT** impact the ability of the VNF to provide
service/function due to a single container restart.

R-79952 The VNF **SHOULD** support container snapshots if not for rebuild
and evacuate for rollback or back out mechanism.

R-92935 The VNF **SHOULD** minimize the propagation of state information
across multiple data centers to avoid cross data center traffic.

R-26371 The VNF **MUST** detect communication failure for inter VNFC
instance and intra/inter VNF and re-establish communication
automatically to maintain the VNF without manual intervention to
provide service continuity.

R-18725 The VNF **MUST** handle the restart of a single VNFC instance
without requiring all VNFC instances to be restarted.

R-06668 The VNF **MUST** handle the start or restart of VNFC instances
in any order with each VNFC instance establishing or re-establishing
required connections or relationships with other VNFC instances and/or
VNFs required to perform the VNF function/role without requiring VNFC
instance(s) to be started/restarted in a particular order.

R-80070 The VNF **MUST** handle errors and exceptions so that they do
not interrupt processing of incoming VNF requests to maintain service
continuity (where the error is not directly impacting the software
handling the incoming request).

R-32695 The VNF **MUST** provide the ability to modify the number of
retries, the time between retries and the behavior/action taken after
the retries have been exhausted for exception handling to allow the
NCSP to control that behavior, where the interface and/or functional
specification allows for altering behaviour.

R-48356 The VNF **MUST** fully exploit exception handling to the extent
that resources (e.g., threads and memory) are released when no longer
needed regardless of programming language.

R-67918 The VNF **MUST** handle replication race conditions both locally
and geo-located in the event of a data base instance failure to maintain
service continuity.

R-36792 The VNF **MUST** automatically retry/resubmit failed requests
made by the software to its downstream system to increase the success rate.

R-70013 The VNF **MUST NOT** require any manual steps to get it ready for
service after a container rebuild.

R-65515 The VNF **MUST** provide a mechanism and tool to start VNF
containers (VMs) without impacting service or service quality assuming
another VNF in same or other geographical location is processing service
requests.

R-94978 The VNF **MUST** provide a mechanism and tool to perform a graceful
shutdown of all the containers (VMs) in the VNF without impacting service
or service quality assuming another VNF in same or other geographical
location can take over traffic and process service requests.

R-22059 The VNF **MUST NOT** execute long running tasks (e.g., IO,
database, network operations, service calls) in a critical section
of code, so as to minimize blocking of other operations and increase
concurrent throughput.

R-63473 The VNF **MUST** automatically advertise newly scaled
components so there is no manual intervention required.

R-74712 The VNF **MUST** utilize FQDNs (and not IP address) for
both Service Chaining and scaling.

R-41159 The VNF **MUST** deliver any and all functionality from any
VNFC in the pool (where pooling is the most suitable solution). The
VNFC pool member should be transparent to the client. Upstream and
downstream clients should only recognize the function being performed,
not the member performing it.

R-85959 The VNF **SHOULD** automatically enable/disable added/removed
sub-components or component so there is no manual intervention required.

R-06885 The VNF **SHOULD** support the ability to scale down a VNFC pool
without jeopardizing active sessions. Ideally, an active session should
not be tied to any particular VNFC instance.

R-12538 The VNF **SHOULD** support load balancing and discovery
mechanisms in resource pools containing VNFC instances.

R-98989 The VNF **SHOULD** utilize resource pooling (threads,
connections, etc.) within the VNF application so that resources
are not being created and destroyed resulting in resource management
overhead.

R-55345 The VNF **SHOULD** use techniques such as “lazy loading” when
initialization includes loading catalogues and/or lists which can grow
over time, so that the VNF startup time does not grow at a rate
proportional to that of the list.

R-35532 The VNF **SHOULD** release and clear all shared assets (memory,
database operations, connections, locks, etc.) as soon as possible,
especially before long running sync and asynchronous operations, so as
to not prevent use of these assets by other entities.

R-77334 The VNF **MUST** allow configurations and configuration parameters
to be managed under version control to ensure consistent configuration
deployment, traceability and rollback.

R-99766 The VNF **MUST** allow configurations and configuration parameters
to be managed under version control to ensure the ability to rollback to
a known valid configuration.

R-73583 The VNF **MUST** allow changes of configuration parameters
to be consumed by the VNF without requiring the VNF or its sub-components
to be bounced so that the VNF availability is not effected.

R-21558 The VNF **SHOULD** use intelligent routing by having knowledge
of multiple downstream/upstream endpoints that are exposed to it, to
ensure there is no dependency on external services (such as load balancers)
to switch to alternate endpoints.

R-08315 The VNF **SHOULD** use redundant connection pooling to connect
to any backend data source that can be switched between pools in an
automated/scripted fashion to ensure high availability of the connection
to the data source.

R-27995 The VNF **SHOULD** include control loop mechanisms to notify
the consumer of the VNF of their exceeding SLA thresholds so the consumer
is able to control its load against the VNF.

R-73364 The VNF **MUST** support at least two major versions of the
VNF software and/or sub-components to co-exist within production
environments at any time so that upgrades can be applied across
multiple systems in a staggered manner.

R-02454 The VNF **MUST** support the existence of multiple major/minor
versions of the VNF software and/or sub-components and interfaces that
support both forward and backward compatibility to be transparent to
the Service Provider usage.

R-57855 The VNF **MUST** support hitless staggered/rolling deployments
between its redundant instances to allow "soak-time/burn in/slow roll"
which can enable the support of low traffic loads to validate the
deployment prior to supporting full traffic loads.

R-64445 The VNF **MUST** support the ability of a requestor of the
service to determine the version (and therefore capabilities) of the
service so that Network Cloud Service Provider can understand the
capabilities of the service.

R-56793 The VNF **MUST** test for adherence to the defined performance
budgets at each layer, during each delivery cycle with delivered
results, so that the performance budget is measured and the code
is adjusted to meet performance budget.

R-77667 The VNF **MUST** test for adherence to the defined performance
budget at each layer, during each delivery cycle so that the performance
budget is measured and feedback is provided where the performance budget
is not met.

R-49308 The VNF **SHOULD** test for adherence to the defined resiliency
rating recommendation at each layer, during each delivery cycle with
delivered results, so that the resiliency rating is measured and the
code is adjusted to meet software resiliency requirements.

R-16039 The VNF **SHOULD** test for adherence to the defined
resiliency rating recommendation at each layer, during each
delivery cycle so that the resiliency rating is measured and
feedback is provided where software resiliency requirements are
not met.

R-34957 The VNF **MUST** provide a method of metrics gathering for each
layer's performance to identify/document variances in the allocations so
they can be addressed.

R-49224 The VNF **MUST** provide unique traceability of a transaction
through its life cycle to ensure quick and efficient troubleshooting.

R-52870 The VNF **MUST** provide a method of metrics gathering
and analysis to evaluate the resiliency of the software from both
a granular as well as a holistic standpoint. This includes, but is
not limited to thread utilization, errors, timeouts, and retries.

R-92571 The VNF **MUST** provide operational instrumentation such as
logging, so as to facilitate quick resolution of issues with the VNF to
provide service continuity.

R-48917 The VNF **MUST** monitor for and alert on (both sender and
receiver) errant, running longer than expected and missing file transfers,
so as to minimize the impact due to file transfer errors.

R-28168 The VNF **SHOULD** use an appropriately configured logging
level that can be changed dynamically, so as to not cause performance
degradation of the VNF due to excessive logging.

R-87352 The VNF **SHOULD** utilize Cloud health checks, when available
from the Network Cloud, from inside the application through APIs to check
the network connectivity, dropped packets rate, injection, and auto failover
to alternate sites if needed.

R-16560 The VNF **SHOULD** conduct a resiliency impact assessment for all
inter/intra-connectivity points in the VNF to provide an overall resiliency
rating for the VNF to be incorporated into the software design and
development of the VNF.

VNF Security
~~~~~~~~~~~~~~

R-23740 The VNF **MUST** accommodate the security principle of
“least privilege” during development, implementation and operation.
The importance of “least privilege” cannot be overstated and must be
observed in all aspects of VNF development and not limited to security.
This is applicable to all sections of this document.

R-61354 The VNF **MUST** implement access control list for OA&M
services (e.g., restricting access to certain ports or applications).

R-85633 The VNF **MUST** implement Data Storage Encryption
(database/disk encryption) for Sensitive Personal Information (SPI)
and other subscriber identifiable data. Note: subscriber’s SPI/data
must be encrypted at rest, and other subscriber identifiable data
should be encrypted at rest. Other data protection requirements exist
and should be well understood by the developer.

R-92207 The VNF **SHOULD** implement a mechanism for automated and
frequent "system configuration (automated provisioning / closed loop)"
auditing.

R-23882 The VNF **SHOULD** be scanned using both network scanning
and application scanning security tools on all code, including underlying
OS and related configuration. Scan reports shall be provided. Remediation
roadmaps shall be made available for any findings.

R-46986 The VNF **SHOULD** have source code scanned using scanning
tools (e.g., Fortify) and provide reports.

R-55830 The VNF **MUST** distribute all production code from NCSP
internal sources only. No production code, libraries, OS images, etc.
shall be distributed from publically accessible depots.

R-99771 The VNF **MUST** provide all code/configuration files in a
"Locked down" or hardened state or with documented recommendations for
such hardening. All unnecessary services will be disabled. VNF provider
default credentials, community strings and other such artifacts will be
removed or disclosed so that they can be modified or removed during
provisioning.

R-19768 The VNF **SHOULD** support L3 VPNs that enable segregation of
traffic by application (dropping packets not belonging to the VPN) (i.e.,
AVPN, IPSec VPN for Internet routes).

R-33981 The VNF **SHOULD** interoperate with various access control
mechanisms for the Network Cloud execution environment (e.g.,
Hypervisors, containers).

R-40813 The VNF **SHOULD** support the use of virtual trusted platform
module, hypervisor security testing and standards scanning tools.

R-56904 The VNF **MUST** interoperate with the ONAP (SDN) Controller so that
it can dynamically modify the firewall rules, ACL rules, QoS rules, virtual
routing and forwarding rules.

R-26586 The VNF **SHOULD** support the ability to work with aliases
(e.g., gateways, proxies) to protect and encapsulate resources.

R-49956 The VNF **MUST** pass all access to applications (Bearer,
signaling and OA&M) through various security tools and platforms from
ACLs, stateful firewalls and application layer gateways depending on
manner of deployment. The application is expected to function (and in
some cases, interwork) with these security tools.

R-69649 The VNF **MUST** have all vulnerabilities patched as soon
as possible. Patching shall be controlled via change control process
with vulnerabilities disclosed along with mitigation recommendations.

R-78010 The VNF **MUST** use the NCSP’s IDAM API for Identification,
authentication and access control of customer or VNF application users.

R-42681 The VNF **MUST** use the NCSP’s IDAM API or comply with
the requirements if not using the NCSP’s IDAM API, for identification,
authentication and access control of OA&M and other system level
functions.

R-68589 The VNF **MUST**, if not using the NCSP’s IDAM API, support
User-IDs and passwords to uniquely identify the user/application. VNF
needs to have appropriate connectors to the Identity, Authentication
and Authorization systems that enables access at OS, Database and
Application levels as appropriate.

R-52085 The VNF **MUST**, if not using the NCSP’s IDAM API, provide
the ability to support Multi-Factor Authentication (e.g., 1st factor =
Software token on device (RSA SecureID); 2nd factor = User Name+Password,
etc.) for the users.

R-98391 The VNF **MUST**, if not using the NCSP’s IDAM API, support
Role-Based Access Control to permit/limit the user/application to
performing specific activities.

R-63217 The VNF **MUST**, if not using the NCSP’s IDAM API, support
logging via ONAP for a historical view of “who did what and when”.

R-62498 The VNF **MUST**, if not using the NCSP’s IDAM API, encrypt
OA&M access (e.g., SSH, SFTP).

R-79107 The VNF **MUST**, if not using the NCSP’s IDAM API, enforce
a configurable maximum number of Login attempts policy for the users.
VNF provider must comply with "terminate idle sessions" policy.
Interactive sessions must be terminated, or a secure, locking screensaver
must be activated requiring authentication, after a configurable period
of inactivity. The system-based inactivity timeout for the enterprise
identity and access management system must also be configurable.

R-35144 The VNF **MUST**, if not using the NCSP’s IDAM API, comply
with the NCSP’s credential management policy.

R-75041 The VNF **MUST**, if not using the NCSP’s IDAM API, expire
passwords at regular configurable intervals.

R-46908 The VNF **MUST**, if not using the NCSP’s IDAM API, comply
with "password complexity" policy. When passwords are used, they shall
be complex and shall at least meet the following password construction
requirements: (1) be a minimum configurable number of characters in
length, (2) include 3 of the 4 following types of characters:
upper-case alphabetic, lower-case alphabetic, numeric, and special,
(3) not be the same as the UserID with which they are associated or
other common strings as specified by the environment, (4) not contain
repeating or sequential characters or numbers, (5) not to use special
characters that may have command functions, and (6) new passwords must
not contain sequences of three or more characters from the previous
password.

R-39342 The VNF **MUST**, if not using the NCSP’s IDAM API, comply
with "password changes (includes default passwords)" policy. Products
will support password aging, syntax and other credential management
practices on a configurable basis.

R-40521 The VNF **MUST**, if not using the NCSP’s IDAM API, support
use of common third party authentication and authorization tools such
as TACACS+, RADIUS.

R-41994 The VNF **MUST**, if not using the NCSP’s IDAM API, comply
with "No Self-Signed Certificates" policy. Self-signed certificates
must be used for encryption only, using specified and approved
encryption protocols such as TLS 1.2 or higher or equivalent security
protocols such as IPSec, AES.

R-23135 The VNF **MUST**, if not using the NCSP’s IDAM API,
authenticate system to system communications where one system
accesses the resources of another system, and must never conceal
individual accountability.

R-95105 The VNF **MUST** host connectors for access to the application
layer.

R-45496 The VNF **MUST** host connectors for access to the OS
(Operating System) layer.

R-05470 The VNF **MUST** host connectors for access to the database layer.

R-99174 The VNF **MUST** comply with Individual Accountability
(each person must be assigned a unique ID) when persons or non-person
entities access VNFs.

R-42874 The VNF **MUST** comply with Least Privilege (no more
privilege than required to perform job functions) when persons
or non-person entities access VNFs.

R-71787 The VNF **MUST** comply with Segregation of Duties (access to a
single layer and no developer may access production without special
oversight) when persons or non-person entities access VNFs.

R-86261 The VNF **MUST NOT** allow VNF provider access to VNFs remotely.

R-49945 The VNF **MUST** authorize VNF provider access through a
client application API by the client application owner and the resource
owner of the VNF before provisioning authorization through Role Based
Access Control (RBAC), Attribute Based Access Control (ABAC), or other
policy based mechanism.

R-31751 The VNF **MUST** subject VNF provider access to privilege
reconciliation tools to prevent access creep and ensure correct
enforcement of access policies.

R-34552 The VNF **MUST** provide or support the Identity and Access
Management (IDAM) based threat detection data for OWASP Top 10.

R-29301 The VNF **MUST** provide or support the Identity and Access
Management (IDAM) based threat detection data for Password Attacks.

R-72243 The VNF **MUST** provide or support the Identity and Access
Management (IDAM) based threat detection data for Phishing / SMishing.

R-58998 The VNF **MUST** provide or support the Identity and Access
Management (IDAM) based threat detection data for Malware (Key Logger).

R-14025 The VNF **MUST** provide or support the Identity and Access
Management (IDAM) based threat detection data for Session Hijacking.

R-31412 The VNF **MUST** provide or support the Identity and Access
Management (IDAM) based threat detection data for XSS / CSRF.

R-51883 The VNF **MUST** provide or support the Identity and Access
Management (IDAM) based threat detection data for Replay.

R-44032 The VNF **MUST** provide or support the Identity and Access
Management (IDAM) based threat detection data for Man in the Middle (MITM).

R-58977 The VNF **MUST** provide or support the Identity and Access
Management (IDAM) based threat detection data for Eavesdropping.

R-24825 The VNF **MUST** provide Context awareness data (device,
location, time, etc.) and be able to integrate with threat detection system.

R-59391 The VNF provider **MUST**, where a VNF provider requires
the assumption of permissions, such as root or administrator, first
log in under their individual user login ID then switch to the other
higher level account; or where the individual user login is infeasible,
must login with an account with admin privileges in a way that
uniquely identifies the individual performing the function.

R-85028 The VNF **MUST** authenticate system to system access and
do not conceal a VNF provider user’s individual accountability for
transactions.

R-80335 The VNF **MUST** make visible a Warning Notice: A formal
statement of resource intent, i.e., a warning notice, upon initial
access to a VNF provider user who accesses private internal networks
or Company computer resources, e.g., upon initial logon to an internal
web site, system or application which requires authentication.

R-73541 The VNF **MUST** use access controls for VNFs and their
supporting computing systems at all times to restrict access to
authorized personnel only, e.g., least privilege. These controls
could include the use of system configuration or access control
software.

R-64503 The VNF **MUST** provide minimum privileges for initial
and default settings for new user accounts.

R-86835 The VNF **MUST** set the default settings for user access
to sensitive commands and data to deny authorization.

R-77157 The VNF **MUST** conform to approved request, workflow
authorization, and authorization provisioning requirements when
creating privileged users.

R-81147 The VNF **MUST** have greater restrictions for access and
execution, such as up to 3 factors of authentication and restricted
authorization, for commands affecting network services, such as
commands relating to VNFs.

R-49109 The VNF **MUST** encrypt TCP/IP--HTTPS (e.g., TLS v1.2)
transmission of data on internal and external networks.

R-39562 The VNF **MUST** disable unnecessary or vulnerable cgi-bin programs.

R-15671 The VNF **MUST NOT** provide public or unrestricted access
to any data without the permission of the data owner. All data
classification and access controls must be followed.

R-89753 The VNF **MUST NOT** install or use systems, tools or
utilities capable of capturing or logging data that was not created
by them or sent specifically to them in production, without
authorization of the VNF system owner.

R-19082 The VNF **MUST NOT** run security testing tools and
programs, e.g., password cracker, port scanners, hacking tools
in production, without authorization of the VNF system owner.

R-19790 The VNF **MUST NOT** include authentication credentials
in security audit logs, even if encrypted.

R-85419 The VNF **SHOULD** use REST APIs exposed to Client
Applications for the implementation of OAuth 2.0 Authorization
Code Grant and Client Credentials Grant, as the standard interface
for a VNF.

R-48080 The VNF **SHOULD** support SCEP (Simple Certificate
Enrollment Protocol).

R-37608 The VNF **MUST** provide a mechanism to restrict access based
on the attributes of the VNF and the attributes of the subject.

R-43884 The VNF **MUST** integrate with external authentication
and authorization services (e.g., IDAM).

R-25878 The VNF **MUST** use certificates issued from publicly
recognized Certificate Authorities (CA) for the authentication process
where PKI-based authentication is used.

R-19804 The VNF **MUST** validate the CA signature on the certificate,
ensure that the date is within the validity period of the certificate,
check the Certificate Revocation List (CRL), and recognize the identity
represented by the certificate where PKI-based authentication is used.

R-47204 The VNF **MUST** protect the confidentiality and integrity of
data at rest and in transit from unauthorized access and modification.

R-33488 The VNF **MUST** protect against all denial of service
attacks, both volumetric and non-volumetric, or integrate with external
denial of service protection tools.

R-21652 The VNF **MUST** implement the following input validation
control: Check the size (length) of all input. Do not permit an amount
of input so great that it would cause the VNF to fail. Where the input
may be a file, the VNF API must enforce a size limit.

R-54930 The VNF **MUST** implement the following input validation
control: Do not permit input that contains content or characters
inappropriate to the input expected by the design. Inappropriate input,
such as SQL insertions, may cause the system to execute undesirable
and unauthorized transactions against the database or allow other
inappropriate access to the internal network.

R-21210 The VNF **MUST** implement the following input validation
control: Validate that any input file has a correct and valid
Multipurpose Internet Mail Extensions (MIME) type. Input files
should be tested for spoofed MIME types.

R-23772 The VNF **MUST** validate input at all layers implementing VNF APIs.

R-87135 The VNF **MUST** comply with NIST standards and industry
best practices for all implementations of cryptography.

R-02137 The VNF **MUST** implement all monitoring and logging as
described in the Security Analytics section.

R-15659 The VNF **MUST** restrict changing the criticality level of
a system security alarm to administrator(s).

R-19367 The VNF **MUST** monitor API invocation patterns to detect
anomalous access patterns that may represent fraudulent access or
other types of attacks, or integrate with tools that implement anomaly
and abuse detection.

R-78066 The VNF **MUST** support requests for information from law
enforcement and government agencies.

R-48470 The VNF **MUST** support Real-time detection and
notification of security events.

R-22286 The VNF **MUST** support Integration functionality via
API/Syslog/SNMP to other functional modules in the network (e.g.,
PCRF, PCEF) that enable dynamic security control by blocking the
malicious traffic or malicious end users.

R-32636 The VNF **MUST** support API-based monitoring to take care of
the scenarios where the control interfaces are not exposed, or are
optimized and proprietary in nature.

R-61648 The VNF **MUST** support event logging, formats, and delivery
tools to provide the required degree of event data to ONAP.

R-22367 The VNF **MUST** support detection of malformed packets due to
software misconfiguration or software vulnerability.

R-31961 The VNF **MUST** support integrated DPI/monitoring functionality
as part of VNFs (e.g., PGW, MME).

R-20912 The VNF **MUST** support alternative monitoring capabilities
when VNFs do not expose data or control traffic or use proprietary and
optimized protocols for inter VNF communication.

R-73223 The VNF **MUST** support proactive monitoring to detect and
report the attacks on resources so that the VNFs and associated VMs can
be isolated, such as detection techniques for resource exhaustion, namely
OS resource attacks, CPU attacks, consumption of kernel memory, local
storage attacks.

R-58370 The VNF **MUST** coexist and operate normally with commercial
anti-virus software which shall produce alarms every time when there is a
security incident.

R-56920 The VNF **MUST** protect all security audit logs (including
API, OS and application-generated logs), security audit software, data,
and associated documentation from modification, or unauthorized viewing,
by standard OS access control mechanisms, by sending to a remote system,
or by encryption.

R-54520 The VNF **MUST** log successful and unsuccessful login attempts.

R-55478 The VNF **MUST** log logoffs.

R-08598 The VNF **MUST** log successful and unsuccessful changes to
a privilege level.

R-13344 The VNF **MUST** log starting and stopping of security
logging.

R-07617 The VNF **MUST** log creating, removing, or changing the
inherent privilege level of users.

R-94525 The VNF **MUST** log connections to a network listener of the
resource.

R-31614 The VNF **MUST** log the field “event type” in the security
audit logs.

R-97445 The VNF **MUST** log the field “date/time” in the security
audit logs.

R-25547 The VNF **MUST** log the field “protocol” in the security audit logs.

R-06413 The VNF **MUST** log the field “service or program used for
access” in the security audit logs.

R-15325 The VNF **MUST** log the field “success/failure” in the
security audit logs.

R-89474 The VNF **MUST** log the field “Login ID” in the security audit logs.

R-04982 The VNF **MUST NOT** include an authentication credential,
e.g., password, in the security audit logs, even if encrypted.

R-63330 The VNF **MUST** detect when the security audit log storage
medium is approaching capacity (configurable) and issue an alarm via
SMS or equivalent as to allow time for proper actions to be taken to
pre-empt loss of audit data.

R-41252 The VNF **MUST** support the capability of online storage of
security audit logs.

R-41825 The VNF **MUST** activate security alarms automatically when
the following event is detected: configurable number of consecutive
unsuccessful login attempts

R-43332 The VNF **MUST** activate security alarms automatically when
the following event is detected: successful modification of critical
system or application files

R-74958 The VNF **MUST** activate security alarms automatically when
the following event is detected: unsuccessful attempts to gain permissions
or assume the identity of another user

R-15884 The VNF **MUST** include the field “date” in the Security alarms
(where applicable and technically feasible).

R-23957 The VNF **MUST** include the field “time” in the Security alarms
(where applicable and technically feasible).

R-71842 The VNF **MUST** include the field “service or program used for
access” in the Security alarms (where applicable and technically feasible).

R-57617 The VNF **MUST** include the field “success/failure” in the
Security alarms (where applicable and technically feasible).

R-99730 The VNF **MUST** include the field “Login ID” in the Security
alarms (where applicable and technically feasible).

R-29705 The VNF **MUST** restrict changing the criticality level of a
system security alarm to administrator(s).

R-13627 The VNF **MUST** monitor API invocation patterns to detect
anomalous access patterns that may represent fraudulent access or other
types of attacks, or integrate with tools that implement anomaly and
abuse detection.

R-21819 The VNF **MUST** support requests for information from law
enforcement and government agencies.

R-56786 The VNF **MUST** implement “Closed Loop” automatic implementation
(without human intervention) for Known Threats with detection rate in low
false positives.

R-25094 The VNF **MUST** perform data capture for security functions.

R-04492 The VNF **MUST** generate security audit logs that must be sent
to Security Analytics Tools for analysis.

R-19219 The VNF **MUST** provide audit logs that include user ID, dates,
times for log-on and log-off, and terminal location at minimum.

R-30932 The VNF **MUST** provide security audit logs including records
of successful and rejected system access data and other resource access
attempts.

R-54816 The VNF **MUST** support the storage of security audit logs
for agreed period of time for forensic analysis.

R-57271 The VNF **MUST** provide the capability of generating security
audit logs by interacting with the operating system (OS) as appropriate.

R-84160 The VNF **MUST** have security logging for VNFs and their
OSs be active from initialization. Audit logging includes automatic
routines to maintain activity records and cleanup programs to ensure
the integrity of the audit/logging systems.

R-58964 The VNF **MUST** provide the capability to restrict read
and write access to data.

R-99112 The VNF **MUST** provide the capability to restrict access
to data to specific users.

R-83227 The VNF **MUST** Provide the capability to encrypt data in
transit on a physical or virtual network.

R-32641 The VNF **MUST** provide the capability to encrypt data on
non-volatile memory.

R-13151 The VNF **SHOULD** disable the paging of the data requiring
encryption, if possible, where the encryption of non-transient data is
required on a device for which the operating system performs paging to
virtual memory. If not possible to disable the paging of the data
requiring encryption, the virtual memory should be encrypted.

R-93860 The VNF **MUST** provide the capability to integrate with an
external encryption service.

R-73067 The VNF **MUST** use industry standard cryptographic algorithms
and standard modes of operations when implementing cryptography.

R-22645 The VNF **SHOULD** use commercial algorithms only when there
are no applicable governmental standards for specific cryptographic
functions, e.g., public key cryptography, message digests.

R-12467 The VNF **MUST NOT** use the SHA, DSS, MD5, SHA-1 and
Skipjack algorithms or other compromised encryption.

R-02170 The VNF **MUST** use, whenever possible, standard implementations
of security applications, protocols, and format, e.g., S/MIME, TLS, SSH,
IPSec, X.509 digital certificates for cryptographic implementations.
These implementations must be purchased from reputable vendors and must
not be developed in-house.

R-70933 The VNF **MUST** provide the ability to migrate to newer
versions of cryptographic algorithms and protocols with no impact.

R-44723 The VNF **MUST** use symmetric keys of at least 112 bits in length.

R-25401 The VNF **MUST** use asymmetric keys of at least 2048 bits in length.

R-95864 The VNF **MUST** use commercial tools that comply with X.509
standards and produce x.509 compliant keys for public/private key generation.

R-12110 The VNF **MUST NOT** use keys generated or derived from
predictable functions or values, e.g., values considered predictable
include user identity information, time of day, stored/transmitted data.

R-52060 The VNF **MUST** provide the capability to configure encryption
algorithms or devices so that they comply with the laws of the jurisdiction
in which there are plans to use data encryption.

R-69610 The VNF **MUST** provide the capability of using certificates
issued from a Certificate Authority not provided by the VNF provider.

R-83500 The VNF **MUST** provide the capability of allowing certificate
renewal and revocation.

R-29977 The VNF **MUST** provide the capability of testing the validity
of a digital certificate by validating the CA signature on the certificate.

R-24359 The VNF **MUST** provide the capability of testing the validity
of a digital certificate by validating the date the certificate is being
used is within the validity period for the certificate.

R-39604 The VNF **MUST** provide the capability of testing the
validity of a digital certificate by checking the Certificate Revocation
List (CRL) for the certificates of that type to ensure that the
certificate has not been revoked.

R-75343 The VNF **MUST** provide the capability of testing the
validity of a digital certificate by recognizing the identity represented
by the certificate — the "distinguished name".

VNF Modularity
~~~~~~~~~~~~~~~~~~

R-37028 The VNF **MUST** be composed of one “base” module.

R-41215 The VNF **MAY** have zero to many “incremental” modules.

R-20974 The VNF **MUST** deploy the base module first, prior to
the incremental modules.

R-11200 The VNF **MUST** keep the scope of a Cinder volume module,
when it exists, to be 1:1 with the VNF Base Module or Incremental Module.

R-38474 The VNF **MUST** have a corresponding environment file for
a Base Module.

R-81725 The VNF **MUST** have a corresponding environment file for
an Incremental Module.

R-53433 The VNF **MUST** have a corresponding environment file for
a Cinder Volume Module.

VNF Devops
~~~~~~~~~~~~~~

R-46960 NCSPs **MAY** operate a limited set of Guest OS and CPU
architectures and families, virtual machines, etc.

R-23475 VNFCs **SHOULD** be agnostic to the details of the Network Cloud
(such as hardware, host OS, Hypervisor or container technology) and must run
on the Network Cloud with acknowledgement to the paradigm that the Network
Cloud will continue to rapidly evolve and the underlying components of
the platform will change regularly.

R-33846 The VNF **MUST** install the NCSP required software on Guest OS
images when not using the NCSP provided Guest OS images. [5]_

R-09467 The VNF **MUST**  utilize only NCSP standard compute flavors. [5]_

R-02997 The VNF **MUST** preserve their persistent data. Running VMs
will not be backed up in the Network Cloud infrastructure.

R-29760 The VNFC **MUST** be installed on non-root file systems,
unless software is specifically included with the operating system
distribution of the guest image.

R-20860 The VNF **MUST** be agnostic to the underlying infrastructure
(such as hardware, host OS, Hypervisor), any requirements should be
provided as specification to be fulfilled by any hardware.

R-89800 The VNF **MUST NOT** require Hypervisor-level customization
from the cloud provider.

R-86758 The VNF **SHOULD** provide an automated test suite to validate
every new version of the software on the target environment(s). The tests
should be of sufficient granularity to independently test various
representative VNF use cases throughout its lifecycle. Operations might
choose to invoke these tests either on a scheduled basis or on demand to
support various operations functions including test, turn-up and
troubleshooting.

R-39650 The VNF **SHOULD** provide the ability to test incremental
growth of the VNF.

R-14853 The VNF **MUST** respond to a "move traffic" [2]_ command
against a specific VNFC, moving all existing session elsewhere with
minimal disruption if a VNF provides a load balancing function across
multiple instances of its VNFCs. Note: Individual VNF performance
aspects (e.g., move duration or disruption scope) may require further
constraints.

R-06327 The VNF **MUST** respond to a "drain VNFC" [2]_ command against
a specific VNFC, preventing new session from reaching the targeted VNFC,
with no disruption to active sessions on the impacted VNFC, if a VNF
provides a load balancing function across multiple instances of its VNFCs.
This is used to support scenarios such as proactive maintenance with no
user impact.

R-64713 The VNF **SHOULD** support a software promotion methodology
from dev/test -> pre-prod -> production in software, development &
testing and operations.

**VNF Modeling Requirements**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Heat
~~~~

R-95303 A VNF's Heat Orchestration Template **MUST** be defined using valid YAML.

R-27078 A VNF's Heat Orchestration template **MUST** contain
the section "heat_template_version:".

R-39402 A VNF's Heat Orchestration Template **MUST**
contain the section "description:".

R-35414 A VNF Heat Orchestration's template **MUST**
contain the section "parameters:".

R-90279 A VNF Heat Orchestration's template's parameter **MUST**
be used in a resource with the exception of the parameters
for the OS::Nova::Server resource property availability_zone.

R-91273 A VNF Heat Orchestration’s template’s parameter for
the OS::Nova::Server resource property availability_zone
**MAY NOT** be used in any OS::Nova::Resource.

R-25877 A VNF's Heat Orchestration Template's parameter
name (i.e., <param name>) **MUST** contain only
alphanumeric characters and underscores ('_').

R-36772 A VNF’s Heat Orchestration Template’s parameter
**MUST** include the attribute “type:”.

R-11441 A VNF’s Heat Orchestration Template’s parameter
type **MUST** be one of the following values: "string",
"number", "json", "comma_delimited_list" or "boolean".

R-32094 A VNF's Heat Orchestration Template parameter
declaration **MAY** contain the attribute "label:"

R-44001 A VNF's Heat Orchestration Template parameter
declaration **MUST** contain the attribute "description".

R-90526 A VNF Heat Orchestration Template parameter
declaration **MUST** not contain the default attribute.

R-26124 If a VNF Heat Orchestration Template parameter
requires a default value, it **MUST** be enumerated in the environment file.

R-32557 A VNF's Heat Orchestration Template parameter
declaration MAY contain the attribute "hidden:".

R-88863 A VNF's Heat Orchestration Template's parameter defined as
type "number" **MUST** have a parameter constraint of "range" or
"allowed_values" defined.

R-40518 A VNF's Heat Orchestration Template’s parameter defined as
type "string" **MAY** have a parameter constraint defined.

R-96227 A VNF's Heat Orchestration Template’s parameter defined as
type "json" **MAY** have a parameter constraint defined.

R-79817 A VNF's Heat Orchestration Template’s parameter defined as
type "comma_delimited_list" **MAY** have a parameter constraint defined.

R-06613 A VNF's Heat Orchestration Template’s parameter defined as
type "boolean" **MAY** have a parameter constraint defined.

R-00011 A VNF's Heat Orchestration Template's Nested YAML files
parameter's **MUST NOT** have a parameter constraint defined.

R-22589 A VNF’s Heat Orchestration Template parameter declaration
**MAY** contain the attribute "immutable:".

R-23664 A VNF's Heat Orchestration template **MUST** contain
the section "resources:".

R-90152 A VNF's Heat Orchestration Template's "resources:"
section **MUST** contain the declaration of at least one resource.

R-40551 A VNF's Heat Orchestration Template's Nested YAML files
**MAY** contain the section "resources:".

R-75141 A VNF's Heat Orchestration Template's resource name
(i.e., <resource ID>) **MUST** only contain alphanumeric
characters and underscores ('_').

R-16447 A VNF's <resource ID> **MUST** be unique across all
Heat Orchestration Templates and all HEAT Orchestration Template
Nested YAML files that are used to create the VNF.

R-53952 A VNF’s Heat Orchestration Template’s Resource
**MUST NOT** reference a HTTP-based resource definitions.

R-71699 A VNF’s Heat Orchestration Template’s Resource
**MUST NOT** reference a HTTP-based Nested YAML file.

R-10834 If a VNF Heat Orchestration Template resource attribute
"property:" uses a nested "get_param", one level of nesting is
supported and the nested "get_param" **MUST** reference an index

R-97199 A VNF's Heat Orchestration Template's OS::Nova::Server
resource **MUST** contain the attribute "metadata".

R-46968 VNF’s Heat Orchestration Template’s Resource **MAY**
declare the attribute “depends_on:”.

R-63137 VNF’s Heat Orchestration Template’s Resource **MAY**
declare the attribute “update_policy:”.

R-43740 A VNF’s Heat Orchestration Template’s Resource
**MAY** declare the attribute “deletion_policy:”.

R-78569 A VNF’s Heat Orchestration Template’s Resouce **MAY**
declare the attribute “external_id:”.

R-36982 A VNF’s Heat Orchestration template **MAY** contain the “outputs:” section.

R-86285 The VNF Heat Orchestration Template **MUST** have a corresponding
environment file, even if no parameters are required to be enumerated.

R-86285 The VNF Heat Orchestration Template **MUST** have a
corresponding environment file, even if no parameters are required to be
enumerated.

R-03324 The VNF Heat Orchestration Template **MUST** contain the
"parameters" section in the
environment file

R-68198 A VNF’s Heat Orchestration template’s Environment File’s
“parameters:” section **MAY** enumerate parameters.

R-59930 A VNF’s Heat Orchestration template’s Environment
File’s **MAY** contain the “parameter_defaults:” section.

R-46096 A VNF’s Heat Orchestration template’s Environment File’s
**MAY** contain the “encrypted_parameters:” section.

R-24893 A VNF’s Heat Orchestration template’s Environment File’s
**MAY** contain the “event_sinks:” section.

R-42685 A VNF’s Heat Orchestration template’s Environment File’s
**MAY** contain the “parameter_merge_strategies:” section.

R-67231 A VNF’s Heat Orchestration template’s Environment File’s **MUST NOT**
contain the “resource_registry:” section.

R-69663 A VNF **MAY** be composed from one or more Heat Orchestration
Templates, each of which represents a subset of the overall VNF.

R-33132 A VNF’s Heat Orchestration Template **MAY** be 1.) Base Module
Heat Orchestration Template (also referred to as a Base Module), 2.)
Incremental Module Heat Orchestration Template (referred to as an Incremental
Module), or 3.) a Cinder Volume Module Heat Orchestration Template
(referred to as Cinder Volume Module).

R-13196 A VNF **MAY** be composed of zero to many Incremental Modules

R-28980 A VNF’s incremental module **MAY** be used for initial VNF
deployment only.

R-86926 A VNF’s incremental module **MAY** be used for scale out only.

R-91497 A VNF’s incremental module **MAY** be used for both deployment
and scale out.

R-68122 A VNF’s incremental module **MAY** be deployed more than once,
either during initial VNF deployment and/or scale out.

R-46119 A VNF’s Heat Orchestration Template’s Resource OS::Heat::CinderVolume
**MAY** be defined in a Base Module.

R-90748 A VNF’s Heat Orchestration Template’s Resource OS::Cinder::Volume
**MAY** be defined in an Incremental Module.

R-03251 A VNF’s Heat Orchestration Template’s Resource OS::Cinder::Volume
**MAY** be defined in a Cinder Volume Module.

* R-11200 The VNF **MUST** keep the scope of a Cinder volume module, 
when it exists, to be 1:1 with the VNF Base Module or Incremental Module.

R-11200 The VNF **MUST** keep the scope of a Cinder volume module, when it
exists, to be 1:1 with the VNF Base Module or Incremental Module

R-36582 A VNF’s Base Module **MAY** utilize nested heat.

R-56721 A VNF’s Incremental Module **MAY** utilize nested heat.

R-30395 A VNF’s Cinder Volume Module **MAY** utilize nested heat.

R-87485 A VNF’s Heat Orchestration Template’s file extension **MUST**
be in the lower case format ‘.yaml’ or ‘.yml’.

R-56438 A VNF’s Heat Orchestration Template’s Nested YAML file extension
**MUST** be in the lower case format ‘.yaml’ or ‘.yml’.

R-74304 A VNF’s Heat Orchestration Template’s Environment file extension
**MUST** be in the lower case format ‘.env’.

R-81339 A VNF Heat Orchestration Template’s Base Module file name **MUST**
include ‘base’ in the filename and **MUST** match one of the following four
formats: 1.) ‘base_<text>.y[a]ml’, 2.) ‘<text>_base.y[a]ml’, 3.)
‘base.y[a]ml’, or 4.) ‘<text>_base_<text>’.y[a]ml; where ‘base’ is case
insensitive and where ‘<text>’ **MUST** contain only alphanumeric characters
and underscores ‘_’ and **MUST NOT** contain the case insensitive word ‘base’.

R-91342  A VNF Heat Orchestration Template’s Base Module’s Environment File
**MUST** be named identical to the VNF Heat Orchestration Template’s Base
Module with ‘.y[a]ml’ replaced with ‘.env’.

R-87247 A VNF Heat Orchestration Template’s Incremental Module file name
**MUST** contain only alphanumeric characters and underscores ‘_’ and
**MUST NOT** contain the case insensitive word ‘base’.

R-94509 A VNF Heat Orchestration Template’s Incremental Module’s Environment
File **MUST** be named identical to the VNF Heat Orchestration Template’s
Incremental Module with ‘.y[a]ml’ replaced with ‘.env’.

R-82732 A VNF Heat Orchestration Template’s Cinder Volume Module **MUST** be
named identical to the base or incremental module it is supporting with
‘_volume appended’

R-31141 A VNF Heat Orchestration Template’s Cinder Volume Module’s Environment
File **MUST** be named identical to the VNF Heat Orchestration Template’s
Cinder Volume Module with .y[a]ml replaced with ‘.env’.

R-76057 A VNF Heat Orchestration Template’s Nested YAML file name **MUST**
contain only alphanumeric characters and underscores ‘_’ and **MUST NOT**
contain the case insensitive word ‘base’.

R-18224 The VNF Heat Orchestration Template **MUST** pass in as properties
all parameter values
associated with the nested heat file in the resource definition defined
in the parent heat template.

R-52753 VNF’s Heat Orchestration Template’s Base Module’s output parameter’s
name and type **MUST** match the VNF’s Heat Orchestration Template’s
incremental Module’s name and type unless the output parameter is of type
‘comma_delimited_list’, then the corresponding input parameter **MUST**
be declared as type ‘json’.

R-22608 When a VNF’s Heat Orchestration Template’s Base Module’s output
parameter is declared as an input parameter in an Incremental Module,
the parameter attribute ‘constraints:’ **MUST NOT** be declared.

R-89913 A VNF’s Heat Orchestration Template’s Cinder Volume Module Output
Parameter(s) **MUST** include the UUID(s) of the Cinder Volumes created in
template, while other Output Parameters **MAY** be included.

R-07443 A VNF’s Heat Orchestration Templates’ Cinder Volume Module Output
Parameter’s name and type **MUST** match the input parameter name and type
in the corresponding Base Module or Incremental Module unless the Output
Parameter is of the type ‘comma_delimited_list’, then the corresponding input
parameter **MUST** be declared as type ‘json’.

R-20547 When an ONAP Volume Module Output Parameter is declared as an input
parameter in a base or an incremental module Heat Orchestration Template,
parameter constraints **MUST NOT** be declared.

R-39349 A VNF Heat Orchestration Template **MUST NOT** be designed to
utilize the OpenStack ‘heat stack-update’ command for scaling
(growth/de-growth).

R-43413 A VNF **MUST** utilize a modular Heat Orchestration Template
design to support scaling (growth/de-growth).

R-59482 A VNF’s Heat Orchestration Template **MUST NOT** be VNF instance
specific or Cloud site specific

R-56750 A VNF’s Heat Orchestration Template’s parameter values that are
constant across all deployments **MUST** be declared in a Heat Orchestration
Template Environment File.

R-01896 A VNF’s Heat Orchestration Template’s parameter values that are
constant across all deployments **MUST** be declared in a Heat Orchestration
Template Environment File.

R-16968 A VNF’s Heat Orchestration Templates **MUST NOT** include heat
resources to create external networks.

R-00606 A VNF **MAY** be connected to zero, one or more than one external
networks.

R-57424 A VNF’s port connected to an external network **MUST** connect the
port to VMs in another VNF and/or an external gateway and/or external router.

R-29865 A VNF’s port connected to an external network **MUST NOT** connect
the port to VMs in the same VNF.

R-69014 When a VNF connects to an external network, a network role, referred
to as the ‘{network-role}’ **MUST** be assigned to the external network
for use in the VNF’s Heat Orchestration Template.

R-05201 When a VNF connects to two or more external networks, each external
network **MUST** be assigned a unique ‘{network-role}’ in the context of
the VNF for use in the VNF’s Heat Orchestration Template.

R-83015 A VNF’s ‘{network-role}’ assigned to an external network **MUST**
be different than the ‘{network-role}’ assigned to the VNF’s internal
networks, if internal networks exist.

R-87096 A VNF **MAY** contain zero, one or more than one internal networks.

R-35666 If a VNF has an internal network, the VNF Heat Orchestration
Template **MUST** include the heat resources to create the internal network.

R-86972 A VNF **SHOULD** create the internal network in the VNF’s Heat
Orchestration Template Base Module.

R-52425 A VNF’s port connected to an internal network **MUST** connect
the port to VMs in the same VNF.

R-46461 A VNF’s port connected to an internal network **MUST NOT** connect
the port to VMs in another VNF and/or an external gateway and/or
external router.

R-68936 When a VNF creates an internal network, a network role, referred to
as the ‘{network-role}’ **MUST** be assigned to the internal network for
use in the VNF’s Heat Orchestration Template.

R-32025 When a VNF creates two or more internal networks, each internal
network **MUST** be assigned a unique ‘{network-role}’ in the context of
the VNF for use in the VNF’s Heat Orchestration Template.

R-69874 A VNF’s ‘{network-role}’ assigned to an internal network **MUST**
be different than the ‘{network-role}’ assigned to the VNF’s external
networks.

R-34726 If a VNF’s port is connected to an internal network and the port
is created in the same Heat Orchestration Template as the internal network,
then the port resource **MUST** use a ‘get_resource’ to obtain
the network UUID.

R-22688  If a VNF’s port is connected to an internal network and the
port is created in an Incremental Module and the internal network is created
in the Base Module then the UUID of the internal network **MUST** be exposed
as a parameter in the ‘outputs:’ section of the Base Module and the port
resource **MUST** use a ‘get_param’ to obtain the network UUID.

R-01455 When a VNF's Heat Orchestration Template creates a Virtual Machine  (i.e., 'OS::Nova::Server'),
each 'class' of VMs **MUST** be assigned a VNF unique
'{vm-type}'; where 'class' defines VMs that **MUST** have the following
identical characteristics:

R-82481 A VNF's Heat Orchestration Template's Resource property
parameter that is
associated with a unique Virtual Machine type **MUST**
include '{vm-type}'  as part of the parameter name with two
exceptions:

R-66729 A VNF’s Heat Orchestration Template’s Resource that is
associated with a unique Virtual Machine type **MUST** include
‘{vm-type}’ as part of the resource ID.

R-98407 A VNF's Heat Orchestration Template's '{vm-type}' **MUST** contain
only alphanumeric characters and/or underscores '_' and
**MUST NOT** contain any of the following strings: '_int' or 'int\_'
or '\_int\_'.

R-48067 A VNF's Heat Orchestration Template's {vm-type} **MUST NOT** be a
substring of {network-role}.

R-32394 A VNF’s Heat Orchestration Template’s use of ‘{vm-type}’
in all Resource property parameter names **MUST** be the same case.

R-46839 A VNF’s Heat Orchestration Template’s use of
‘{vm-type}’ in all Resource IDs **MUST** be the same case.

R-36687 A VNF’s Heat Orchestration Template’s ‘{vm-type}’ case in
Resource property parameter names **SHOULD** match the case of
‘{vm-type}’ in Resource IDs and vice versa.

R-21330 A VNF’s Heat Orchestration Template’s Resource property parameter
that is associated with external network **MUST** include the ‘{network-role}’’ as part of the parameter name

R-11168 A VNF's Heat Orchestration Template's Resource ID that is
associated with an external network **MUST** include the
'{network-role}' as part of the resource ID.

R-84322 A VNF's Heat Orchestration Template's Resource property
parameter that is associated with an internal network
**MUST** include 'int\_{network-role}' as part of the parameter
name, where 'int\_' is a hard coded string.

R-96983 A VNF's Heat Orchestration Template's Resource ID that is
associated with an internal network **MUST** include
'int\_{network-role}' as part of the Resource ID, where
'int\_' is a hard coded string.

R-26506 A VNF's Heat Orchestration Template's '{network-role}'
**MUST** contain only alphanumeric characters and/or
underscores '_' and **MUST NOT** contain any of the following
strings: '_int' or 'int\_' or '\_int\_'.

R-00977 A VNF’s Heat Orchestration Template’s ‘{network-role}’
**MUST NOT** be a substring of ‘{vm-type}’.

R-58424 A VNF’s Heat Orchestration Template’s use of ‘{network-role}’
in all Resource property parameter names **MUST** be the same case

R-21511 A VNF’s Heat Orchestration Template’s use of ‘{network-role}’
in all Resource IDs **MUST** be the same case.

R-86588 A VNF’s Heat Orchestration Template’s ‘{network-role}’ case
in Resource property parameter names **SHOULD** match the case
of ‘{network-role}’ in Resource IDs and vice versa.

R-54517 When a VNF’s Heat Orchestration Template’s resource is associated
with a single ‘{vm-type}’, the Resource ID **MUST** contain the ‘{vm-type}’.

R-96482 When a VNF’s Heat Orchestration Template’s resource is associated
with a single external network, the Resource ID MUST contain the text
‘{network-role}’.

R-98138 When a VNF’s Heat Orchestration Template’s resource is associated
with a single internal network, the Resource ID MUST contain the text
‘int\_{network-role}’.

R-82115 When a VNF's Heat Orchestration Template's resource is associated
with a single '{vm-type}' and a single external network, the Resource
ID text **MUST** contain both the '{vm-type}' and the '{network-role}'

- the '{vm-type}' **MUST** appear before the '{network-role}' and **MUST**
  be separated by an underscore '_'

   - e.g., '{vm-type}_{network-role}', '{vm-type}_{index}_{network-role}'

- note that an '{index}' value **MAY** separate the '{vm-type}' and the
  '{network-role}' and when this occurs underscores **MUST** separate the
  three values.

R-82551 When a VNF's Heat Orchestration Template's resource is associated
with a single '{vm-type}' and a single internal network, the Resource ID
**MUST** contain both the '{vm-type}' and the 'int\_{network-role}' and

- the '{vm-type}' **MUST** appear before the 'int\_{network-role}' and
  **MUST** be separated by an underscore '_'

   - (e.g., '{vm-type}\_int\_{network-role}', '{vm-type}_{index}\_int\_{network-role}')

- note that an '{index}' value **MAY** separate the '{vm-type}' and the
  'int\_{network-role}' and when this occurs underscores **MUST** separate
  the three values.

R-67793 When a VNF’s Heat Orchestration Template’s resource is associated
with more than one ‘{vm-type}’ and/or more than one internal and/or
external network, the Resource ID **MUST NOT** contain the ‘{vm-type}’
and/or ‘{network-role}’/’int\_{network-role}’. It also should contain the
term ‘shared’ and/or contain text that identifies the VNF

R-27970 When a VNF’s Heat Orchestration Template’s resource is associated
with more than one ‘{vm-type}’ and/or more than one internal and/or
external network, the Resource ID **MAY** contain the term ‘shared’
and/or **MAY** contain text that identifies the VNF.

R-11690 When a VNF’s Heat Orchestration Template’s Resource ID contains
an {index} value (e.g. multiple VMs of same {vm-type}), the ‘{index}’
**MUST** start at zero and increment by one.

R-71152 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘image’ parameter **MUST** be declared as
type: ‘string’.

R-58670 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘image’ parameter name **MUST** follow the
naming convention ‘{vm-type}_image_name’.

R-91125 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘image’ parameter **MUST** be enumerated in
the Heat Orchestration Template’s Environment File and a value **MUST** be
assigned.

R-57282 Each VNF’s Heat Orchestration Template’s ‘{vm-type}’
**MUST** have a unique parameter name for the ‘OS::Nova::Server’
property ‘image’ even if more than one {vm-type} shares the same image.

R-50436 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘flavor’ parameter **MUST** be declared as
type: ‘string’.

R-45188 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘flavor’ parameter name **MUST** follow the
naming convention ‘{vm-type}_flavor_name’.

R-69431 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘flavor’ parameter **MUST** be enumerated in the
Heat Orchestration Template’s Environment File and a value **MUST** be
assigned.

R-40499 Each VNF’s Heat Orchestration Template’s ‘{vm-type}’ **MUST**
have a unique parameter name for the ‘OS::Nova::Server’ property
‘flavor’ even if more than one {vm-type} shares the same flavor.

R-51430 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘name’ parameter **MUST** be declared as
either type ‘string’ or type ‘comma_delimited_list”.

R-54171 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘name’ parameter is defined as a ‘string’,
the parameter name **MUST** follow the naming convention
‘{vm-type}\_name\_{index}’, where {index} is a numeric value that starts
at zero and increments by one.

R-40899 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘name’ parameter is defined as a ‘string’,
a parameter **MUST** be declared for each ‘OS::Nova::Server’ resource
associated with the ‘{vm-type}’.

R-87817 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘name’ parameter is defined as a
‘comma_delimited_list’, the parameter name **MUST** follow the naming
convention ‘{vm-type}_names’.

R-85800 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘name’ parameter is defined as a
‘comma_delimited_list’, a parameter **MUST** be delcared once for all
‘OS::Nova::Server’ resources associated with the ‘{vm-type}’.

R-22838 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘name’ parameter **MUST NOT** be enumerated
in the Heat Orchestration Template’s Environment File.

R-44271 The VNF's Heat Orchestration Template's Resource 'OS::Nova::Server' property
'name' parameter value **SHOULD NOT** contain special characters
since the Contrail GUI has a limitation displaying special characters.

R-98450 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘availability_zone’ parameter name
**MUST** follow the naming convention ‘availability\_zone\_{index}’
where the ‘{index}’ **MUST** start at zero and increment by one.

R-23311 The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘availability_zone’ parameter **MUST**
be declared as type: ‘string’.

R-59568  The VNF’s Heat Orchestration Template’s Resource
‘OS::Nova::Server’ property ‘availability_zone’ parameter **MUST NOT**
be enumerated in the Heat Orchestration Template’s Environment File.

R-01359 A VNF’s Heat Orchstration Template that contains an
‘OS::Nova:Server’ Resource **MAY** define a parameter for the property
‘availability_zone’ that is not utilized in any ‘OS::Nova::Server’
resources in the Heat Orchestration Template.

R-99798 A VNF’s Heat Orchestration Template’s Virtual Machine
(i.e., OS::Nova::Server Resource) **MAY** boot from an image or **MAY**
boot from a Cinder Volume.

R-83706 When a VNF’s Heat Orchestration Template’s Virtual Machine
(i.e., ‘OS::Nova::Server’ Resource) boots from an image, the
‘OS::Nova::Server’ resource property ‘image’ **MUST** be used.

R-69588 When a VNF’s Heat Orchestration Template’s Virtual Machine
(i.e., ‘OS::Nova::Server’ Resource) boots from Cinder Volume, the
‘OS::Nova::Server’ resource property ‘block_device_mapping’ or
‘block_device_mapping_v2’ **MUST** be used.

R-37437 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **MUST** contain the metadata map value parameter ‘vnf_id’.

R-07507 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_id’ **MUST** be declared
as type: ‘string’.

R-55218 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_id’ **MUST NOT** have
parameter contraints defined.

R-20856 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_id’ **MUST NOT** be
enumerated in the Heat Orchestration Template’s environment file.

R-44491 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_id’ is passed into a
Nested YAML file, the parameter name ‘vnf_id’ **MUST NOT** change.

R-71493 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **MUST** contain the metadata map value parameter
‘vf\_module\_id’.

R-82134 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_id’ **MUST**
be declared as type: ‘string’.

R-98374 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_id’ **MUST NOT**
have parameter contraints defined.

R-72871 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_id’ **MUST NOT**
be enumerated in the Heat Orchestration Template’s environment file.

R-86237 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf_module_id’ is passed
into a Nested YAML file, the parameter name ‘vf\_module\_id’
**MUST NOT** change.

R-72483 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **MUST** contain the metadata map value parameter
‘vnf_name’.

R-62428 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_name’ **MUST** be
declared as type: ‘string’.

R-44318 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_name’ **MUST NOT** have
parameter contraints defined.

R-36542 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_name’ **MUST NOT** be
enumerated in the Heat Orchestration Template’s environment file.

R-16576 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_name’ is passed into a
Nested YAML file, the parameter name ‘vnf_name’ **MUST NOT** change.

R-68023 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **SHOULD** contain the metadata map value parameter
‘vf\_module\_name’.

R-39067 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_name’ **MUST**
be declared as type: ‘string’.

R-15480 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_name’
**MUST NOT** have parameter contraints defined.

R-80374 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_name’
**MUST NOT** be enumerated in the Heat Orchestration Template’s
environment file.

R-49177 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_name’ is passed
into a Nested YAML file, the parameter name ‘vf\_module\_name’
**MUST NOT** change.

R-85328 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **MAY** contain the metadata map value parameter ‘vm_role’.

R-95430 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vm_role’ **MUST** be
declared as type: ‘string’.

R-67597 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vm_role’ **MUST NOT** have
parameter contraints defined.

R-46823 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vnf_name’ **MUST** be
either

 - enumerated in the VNF’s Heat Orchestration
   Template’s environment file.

 - hard coded in the VNF’s Heat Orchestration
   Template’s OS::Nova::Resource metadata property.

R-86476 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vm_role’ value **MUST only**
contain alphanumeric characters and underscores ‘_’.

R-70757 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vm_role’ is passed into a
Nested YAML file, the parameter name ‘vm_role’ **MUST NOT** change.

R-50816 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **MAY** contain the metadata map value parameter
‘vf\_module\_index’.

R-54340 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_index’ **MUST** be
declared as type: ‘number’.

R-09811 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_index’ **MUST NOT**
have parameter contraints defined.

R-37039 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_index’ **MUST NOT**
be enumerated in the Heat Orchestration Template’s environment file.

R-22441 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_index’ is passed
into a Nested YAML file, the parameter name ‘vf\_module\_index’
**MUST NOT** change.

R-55306 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘vf\_module\_index’ **MUST NOT** be
used in a VNF’s Volume Template; it is not supported.

R-47061 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **SHOULD** contain the metadata map value parameter
‘workload_context’.

R-74978 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘workload_context’ **MUST** be
declared as type: ‘string’.

R-34055 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘workload_context’ **MUST NOT**
have parameter contraints defined.

R-02691 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘workload_context’ **MUST NOT**
be enumerated in the Heat Orchestration Template’s environment file.

R-75202 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘workload_context’ is passed
into a Nested YAML file, the parameter name ‘workload_context’
**MUST NOT** change.

R-88536 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource **SHOULD** contain the metadata map value parameter
‘environment_context’.

R-20308 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘environment_context’ **MUST**
be declared as type: ‘string’.

R-56183 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘environment_context’ **MUST NOT**
have parameter contraints defined.

R-13194 A VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘environment_context’ **MUST NOT**
be enumerated in the Heat Orchestration Template’s environment file.

R-62954 If a VNF’s Heat Orchestration Template’s OS::Nova::Server
Resource metadata map value parameter ‘environment_context’ is
passed into a Nested YAML file, the parameter name
‘environment_context’ **MUST NOT** change.

R-18008 The VNF’s Heat Orchestration Template’s Resource ‘OS::Neutron::Port’
property ‘network’ parameter **MUST** be declared as type: ‘string’.

R-62983 When the VNF’s Heat Orchestration Template’s Resource ‘OS::Neutron::Port’
is attaching to an external network, the ‘network’ parameter name **MUST**

- follow the naming convention ‘{network-role}_net_id’ if the Neutron
  network UUID value is used to reference the network
- follow the naming convention ‘{network-role}_net_name’ if the OpenStack
  network name is used to reference the network.

where ‘{network-role}’ is the network-role of the external network and
a ‘get_param’ **MUST** be used as the intrinsic function.

R-86182 When the VNF’s Heat Orchestration Template’s Resource ‘OS::Neutron::Port’
is attaching to an internal network, and the internal network is created in a different
Heat Orchestration Template than the ‘OS::Neutron::Port’, the ‘network’
parameter name **MUST**

- follow the naming convention ‘int\_{network-role}_net_id’ if the Neutron
  network UUID value is used to reference the network
- follow the naming convention ‘int\_{network-role}_net_name’ if the
  OpenStack network name in is used to reference the network.

where ‘{network-role}’ is the network-role of the internal network and a ‘get_param’ **MUST** be used as the intrinsic function.

R-93177 When the VNF’s Heat Orchestration Template’s Resource ‘OS::Neutron::Port’
is attaching to an internal network, and the internal network is created in the same Heat
Orchestration Template than the ‘OS::Neutron::Port’, the ‘network’
parameter name **MUST** obtain the UUID of the internal network by using
the intrinsic function ‘get_resource’ or ‘get_attr’ and referencing the
Resource ID of the internal network.

R-29872 The VNF’s Heat Orchestration Template’s Resource ‘OS::Nova::Server’
property ‘network’ parameter **MUST NOT** be enumerated in the Heat
Orchestration Template’s Environment File.

R-34037 The VNF’s Heat Orchestration Template’s resource ‘OS::Neutron::Port’
property ‘fixed_ips’ map property ‘ip_address’ parameter **MUST** be declared as
either type ‘string’ or type ‘comma_delimited_list’.

R-40971 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an external network, and an IPv4 address is
assigned using the property
‘fixed_ips’ map property ‘ip_address’ and the parameter type is defined
as a string, the parameter name **MUST** follow the naming
convention ‘{vm-type}_{network-role}\_ip\_{index}’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the external network
- the value for {index} must start at zero (0) and increment by one

R-39841 The VNF’s Heat Orchestration Template’s Resource ‘OS::Neutron::Port’
property ‘fixed_ips’ map property ‘ip_address’ parameter
‘{vm-type}_{network-role}\_ip\_{index}’ **MUST NOT** be enumerated in the
VNF’s Heat Orchestration Template’s Environment File.

R-04697 When the VNF’s Heat Orchestration Template’s Resource ‘OS::Neutron::Port’
is attaching to an external network, and an IPv4 address is assigned using
the property ‘fixed_ips’ map property ‘ip_address’ and the parameter type
is defined as a comma_delimited_list, the parameter name **MUST** follow the
naming convention ‘{vm-type}_{network-role}_ips’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the external network

R-98905 The VNF’s Heat Orchestration Template’s Resource ‘OS::Neutron::Port’
property ‘fixed_ips’ map property ‘ip_address’ parameter
‘{vm-type}_{network-role}_ips’ **MUST NOT** be enumerated in the VNF’s
Heat Orchestration Template’s Environment File.

R-71577 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an external network, and an IPv6 address
is assigned using the property ‘fixed_ips’ map property ‘ip_address’ and
the parameter type is defined as a string, the parameter name **MUST** follow
the naming convention ‘{vm-type}_{network-role}\_v6\_ip\_{index}’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the external network
- the value for {index} must start at zero (0) and increment by one

R-87123 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter ‘{vm-type}_{network-role}\_v6\_ip\_{index}’ **MUST NOT** be enumerated
in the VNF’s Heat Orchestration Template’s Environment File.

R-23503 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an external network, and an IPv6
address is assigned using the property ‘fixed_ips’ map property ‘ip_address’
and the parameter type is defined as a comma_delimited_list, the parameter
name **MUST** follow the naming convention ‘{vm-type}_{network-role}_v6_ips’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the external network

R-93030 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter ‘{vm-type}_{network-role}_v6_ips’ **MUST NOT** be enumerated in the
VNF’s Heat Orchestration Template’s Environment File.

R-78380 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an internal network, and an IPv4 address
is assigned using the property ‘fixed_ips’ map property ‘ip_address’ and
the parameter type is defined as a string, the parameter name **MUST** follow
the naming convention ‘{vm-type}\_int\_{network-role}\_ip\_{index}’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the internal network
- the value for {index} must start at zero (0) and increment by one

R-28795 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter ‘{vm-type}\_int\_{network-role}\_ip\_{index}’ **MUST** be enumerated
in the VNF’s Heat Orchestration Template’s Environment File.

R-85235 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an internal network, and an IPv4
address is assigned using the property ‘fixed_ips’ map property ‘ip_address’
and the parameter type is defined as a comma_delimited_list, the parameter
name **MUST** follow the naming convention ‘{vm-type}\_int\_{network-role}_ips’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the internal network

R-90206 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter ‘{vm-type}\_int\_{network-role}_int_ips’ **MUST** be enumerated in
the VNF’s Heat Orchestration Template’s Environment File.

R-27818 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an internal network, and an IPv6 address
is assigned using the property ‘fixed_ips’ map property ‘ip_address’ and
the parameter type is defined as a string, the parameter name **MUST** follow
the naming convention ‘{vm-type}\_int\_{network-role}\_v6\_ip\_{index}’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the internal network
- the value for {index} must start at zero (0) and increment by one

R-97201 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter ‘{vm-type}\_int\_{network-role}\_v6\_ip\_{index}’ **MUST** be enumerated
in the VNF’s Heat Orchestration Template’s Environment File.

R-29765 When the VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ is attaching to an internal network, and an IPv6
address is assigned using the property ‘fixed_ips’ map property ‘ip_address’
and the parameter type is defined as a comma_delimited_list, the parameter
name **MUST** follow the naming convention ‘{vm-type}\_int\_{network-role}_v6_ips’, where

- ‘{vm-type}’ is the {vm-type} associated with the OS::Nova::Server
- ‘{network-role}’ is the {network-role} of the internal network

R-98569 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter ‘{vm-type}\_int\_{network-role}_v6_ips’ **MUST** be enumerated in
the VNF’s Heat Orchestration Template’s Environment File.

R-62590 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter associated with an external network, i.e.,

- {vm-type}_{network-role}\_ip\_{index}
- {vm-type}_{network-role}\_ip\_v6\_{index}
- {vm-type}_{network-role}_ips
- {vm-type}_{network-role}_v6_ips

**MUST NOT** be enumerated in the Heat Orchestration Template’s Environment File.
ONAP provides the IP address assignments at orchestration time.

R-93496 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property ‘ip_address’
parameter associated with an internal network, i.e.,

- {vm-type}\_int\_{network-role}\_ip\_{index}
- {vm-type}\_int\_{network-role}\_ip\_v6\_{index}
- {vm-type}\_int\_{network-role}_ips
- {vm-type}\_int\_{network-role}_v6_ips

**MUST** be enumerated in the Heat Orchestration Template’s Environment
File and IP addresses **MUST** be assigned.

R-38236 The VNF’s Heat Orchestration Template’s resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property
‘subnet’/’subnet_id’ parameter **MUST** be declared type ‘string’.

R-62802 When the VNF’s Heat Orchestration Template’s resource
‘OS::Neutron::Port’ is attaching to an external network, and an IPv4
address is being Cloud Assigned by OpenStack’s DHCP Service and the
external network IPv4 subnet is to be specified using the property
‘fixed_ips’ map property ‘subnet’/’subnet_id’, the parameter **MUST**
follow the naming convention ‘{network-role}_subnet_id’, where
‘{network-role}’ is the network role of the network.

R-83677 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property
subnet’/’subnet_id’ parameter ‘{network-role}_subnet_id’
**MUST NOT** be enumerated in the VNF’s Heat Orchestration Template’s
Environment File.

R-15287 When the VNF’s Heat Orchestration Template’s resource
‘OS::Neutron::Port’ is attaching to an external network, and an IPv6
address is being Cloud Assigned by OpenStack’s DHCP Service and the
external network IPv6 subnet is to be specified using the property
‘fixed_ips’ map property ‘subnet’/’subnet_id’, the parameter **MUST**
follow the naming convention ‘{network-role}_subnet_v6_id’, where
‘{network-role}’ is the network role of the network.

R-80829 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property
subnet’/’subnet_id’ parameter ‘{network-role}_subnet_v6_id’
**MUST NOT** be enumerated in the VNF’s Heat Orchestration Template’s
Environment File.

R-84123 When

- the VNF’s Heat Orchestration Template’s resource ‘OS::Neutron::Port’
  in an Incremental Module is attaching to an internal network
  that is created in the Base Module, AND
- an IPv4 address is being Cloud Assigned by OpenStack’s DHCP Service AND
- the internal network IPv4 subnet is to be specified using the
  property ‘fixed_ips’ map property ‘subnet’/’subnet_id’,

the parameter **MUST** follow the naming convention
‘int\_{network-role}_subnet_id’, where ‘{network-role}’ is the
network role of the internal network

- Note that the parameter **MUST** be defined as an ‘output’ parameter in
  the base module.

R-69634 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property
subnet’/’subnet_id’ parameter ‘int\_{network-role}_subnet_id’
**MUST NOT** be enumerated in the VNF’s Heat Orchestration Template’s
Environment File.

R-76160 When

- the VNF’s Heat Orchestration Template’s resource
  ‘OS::Neutron::Port’ in an Incremental Module is attaching to an
  internal network that is created in the Base Module, AND
- an IPv6 address is being Cloud Assigned by OpenStack’s DHCP Service AND
- the internal network IPv6 subnet is to be specified using the property
  ‘fixed_ips’ map property ‘subnet’/’subnet_id’,

the parameter **MUST** follow the naming convention
‘int\_{network-role}_v6_subnet_id’, where ‘{network-role}’
is the network role of the internal network

- Note that the parameter **MUST** be defined as an ‘output’ parameter in
  the base module.

R-22288 The VNF’s Heat Orchestration Template’s Resource
‘OS::Neutron::Port’ property ‘fixed_ips’ map property
‘subnet’/’subnet_id’ parameter ‘int\_{network-role}_v6_subnet_id’
**MUST NOT** be enumerated in the VNF’s Heat Orchestration Template’s
Environment File.

R-61282 The VNF Heat Orchestration Template **MUST**
adhere to the following naming convention for the property
allowed\_address\_pairs and Map Property ip\_address parameter,
when the parameter is referencing an “external” network:

-  {vm-type}\_{network-role}\_floating\_ip for an IPv4 address

-  {vm-type}\_{network-role}\_floating\_v6\_ip for an IPv6 address

R-16805 The VNF Heat Orchestration Template **MUST** adhere to the following naming convention
for the property allowed\_address\_pairs and Map Property ip\_address
parameter when the parameter is referencing an “internal” network.

R-85734 The VNF Heat Orchestration Template **MUST** use the intrinsic function str\_replace
in conjunction with the ONAP supplied metadata parameter
vnf\_name to generate a unique value,
when the property name for a non OS::Nova::Server resources is defined
in a Heat Orchestration Template.

R-47788 The VNF Heat Orchestration Template **MUST** have a 1:1 scope of a cinder volume module,
when it exists, with the Base Module or Incremental Module

R-86285 The VNF Heat Orchestration Template **MUST** have a corresponding
environment file, even if no parameters are required to be enumerated.

R-86285 The VNF Heat Orchestration Template **MUST** have a
corresponding environment file, even if no parameters are required to be
enumerated.

R-67205 The VNF Heat Orchestration Template **MUST** have a corresponding
environment file for a Base Module.

R-35727 The VNF Heat Orchestration Template **MUST** have a
corresponding environment file for an Incremental module.

R-22656 The VNF Heat Orchestration Template **MUST** have a corresponding environment file
for a Cinder Volume Module.

R-89868 The VNF Heat Orchestration Template **MUST** have unique file names within the scope
of the VNF for a nested heat yaml file.

R-52530 The VNF Heat Orchestration Template **MUST NOT** use a directory hierarchy for
nested templates. All templates must be in a single, flat directory
(per VNF).

R-76718 The VNF Heat Orchestration Template **MUST** reference the get\_files targets in
Heat templates by file name, and the corresponding files should be
delivered to ONAP along with the Heat templates.

R-41888 The VNE Heat **MUST NOT** use URL-based file retrieval.

R-62177 The VNF Heat Orchestration Template **MUST** have unique file names for the included
files within the scope of the VNF.

**ONAP Management Requirements**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


VNF On-boarding and package management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


R-77707 The xNF provider **MUST** include a Manifest File that
contains a list of all the components in the xNF package.

R-66070 The xNF Package **MUST** include xNF Identification Data to
uniquely identify the resource for a given xNF provider. The identification
data must include: an identifier for the xNF, the name of the xNF as was
given by the xNF provider, xNF description, xNF provider, and version.

R-69565 The xNF Package **MUST** include documentation describing xNF
Management APIs, which must include information and tools for ONAP to
deploy and configure (initially and ongoing) the xNF application(s)
(e.g., NETCONF APIs) which includes a description of configurable
parameters for the xNF and whether the parameters can be configured
after xNF instantiation.

R-00156 The xNF Package **MUST** include documentation describing xNF
Management APIs, which must include information and tools for ONAP
to monitor the health of the xNF (conditions that require healing
and/or scaling responses).

R-00068 The xNF Package **MUST** include documentation which includes
a description of parameters that can be monitored for the xNF and
event records (status, fault, flow, session, call, control plane,
etc.) generated by the xNF after instantiation.

R-12678 The xNF Package **MUST** include documentation which includes a
description of runtime lifecycle events and related actions (e.g.,
control responses, tests) which can be performed for the xNF.

R-84366 The xNF Package **MUST** include documentation describing
xNF Functional APIs that are utilized to build network and
application services. This document describes the externally exposed
functional inputs and outputs for the xNF, including interface
format and protocols supported.

R-36280 The xNF provider **MUST** provide documentation describing
xNF Functional Capabilities that are utilized to operationalize the
xNF and compose complex services.

R-98617 The xNF provider **MUST** provide information regarding any
dependency (e.g., affinity, anti-affinity) with other xNFs and resources.

R-89571 The xNF **MUST** support and provide artifacts for configuration
management using at least one of the following technologies;
a) Netconf/YANG, b) Chef, or c) Ansible.

R-30278 The xNF provider **MUST** provide a Resource/Device YANG model
as a foundation for creating the YANG model for configuration. This will
include xNF attributes/parameters and valid values/attributes configurable
by policy.

R-13390 The xNF provider **MUST** provide cookbooks to be loaded
on the appropriate Chef Server.

R-18525 The xNF provider **MUST** provide a JSON file for each
supported action for the xNF.  The JSON file must contain key value
pairs with all relevant values populated with sample data that illustrates
its usage. The fields and their description are defined in Tables A1 and A2 in the Appendix.

R-75608 The xNF provider **MUST** provide playbooks to be loaded
on the appropriate Ansible Server.

R-16777 The xNF provider **MUST** provide a JSON file for each
supported action for the xNF.  The JSON file must contain key value
pairs with all relevant values populated with sample data that illustrates
its usage. The fields and their description are defined in Table B1 in the Appendix.

R-46567 The xNF Package **MUST** include configuration scripts
for boot sequence and configuration.

R-16065 The xNF provider **MUST** provide configurable parameters
(if unable to conform to YANG model) including xNF attributes/parameters
and valid values, dynamic attributes and cross parameter dependencies
(e.g., customer provisioning data).

R-22888 The xNF provider **MUST** provide documentation for the xNF
Policy Description to manage the xNF runtime lifecycle. The document
must include a description of how the policies (conditions and actions)
are implemented in the xNF.

R-01556 The xNF Package **MUST** include documentation describing the
fault, performance, capacity events/alarms and other event records
that are made available by the xNF.

R-16875 The xNF Package **MUST** include documentation which must include
a unique identification string for the specific xNF, a description of
the problem that caused the error, and steps or procedures to perform
Root Cause Analysis and resolve the issue.

R-35960 The xNF Package **MUST** include documentation which must include
all events, severity level (e.g., informational, warning, error) and
descriptions including causes/fixes if applicable for the event.

R-42018 The xNF Package **MUST** include documentation which must include
all events (fault, measurement for xNF Scaling, Syslogs, State Change
and Mobile Flow), that need to be collected at each VM, VNFC (defined in `VNF Guidelines <http://onap.readthedocs.io/en/latest/submodules/vnfrqts/guidelines.git/docs/vnf_guidelines/vnf_guidelines.html#a-glossary>`__ ) and for the overall xNF.

R-27711 The xNF provider **MUST** provide an XML file that contains a
list of xNF error codes, descriptions of the error, and possible
causes/corrective action.

R-01478 The xNF Package **MUST** include documentation describing all
parameters that are available to monitor the xNF after instantiation
(includes all counters, OIDs, PM data, KPIs, etc.) that must be
collected for reporting purposes.

R-73560 The xNF Package **MUST** include documentation about monitoring
parameters/counters exposed for virtual resource management and xNF
application management.

R-90632 The xNF Package **MUST** include documentation about KPIs and
metrics that need to be collected at each VM for capacity planning
and performance management purposes.

R-86235 The xNF Package **MUST** include documentation about the monitoring
parameters that must include latencies, success rates, retry rates, load
and quality (e.g., DPM) for the key transactions/functions supported by
the xNF and those that must be exercised by the xNF in order to perform
its function.

R-33904 The xNF Package **MUST** include documentation for each KPI, provide
lower and upper limits.

R-53598 The xNF Package **MUST** include documentation to, when relevant,
provide a threshold crossing alert point for each KPI and describe the
significance of the threshold crossing.

R-69877 The xNF Package **MUST** include documentation for each KPI,
identify the suggested actions that need to be performed when a
threshold crossing alert event is recorded.

R-22680 The xNF Package **MUST** include documentation that describes
any requirements for the monitoring component of tools for Network
Cloud automation and management to provide these records to components
of the xNF.

R-33694 The xNF Package **MUST** include documentation to when applicable,
provide calculators needed to convert raw data into appropriate reporting
artifacts.

R-56815 The xNF Package **MUST** include documentation describing
supported xNF scaling capabilities and capacity limits (e.g., number
of users, bandwidth, throughput, concurrent calls).

R-48596 The xNF Package **MUST** include documentation describing
the characteristics for the xNF reliability and high availability.

R-74763 The xNF provider **MUST** provide an artifact per xNF that contains
all of the xNF Event Records supported. The artifact should include reference
to the specific release of the xNF Event Stream Common Event Data Model
document it is based on. (e.g., `VES Event Listener <https://github.com/att/evel-test-collector/tree/master/docs/att_interface_definition>`__)

R-35851 The xNF Package **MUST** include xNF topology that describes
basic network and application connectivity internal and external to the
xNF including Link type, KPIs, Bandwidth, latency, jitter, QoS (if
applicable) for each interface.

R-97102 The VNF Package **MUST** include VM requirements via a Heat
template that provides the necessary data for VM specifications
for all VNF components - for hypervisor, CPU, memory, storage.

R-20204 The VNF Package **MUST** include VM requirements via a Heat
template that provides the necessary data for network connections,
interface connections, internal and external to VNF.

R-44896 The VNF Package **MUST** include VM requirements via a Heat
template that provides the necessary data for high availability
redundancy model.

R-55802 The VNF Package **MUST** include VM requirements via a Heat
template that provides the necessary data for scaling/growth VM
specifications.

R-26881 The xNF provider **MUST** provide the binaries and images
needed to instantiate the xNF (xNF and VNFC images).

R-96634 The xNF provider **MUST** describe scaling capabilities
to manage scaling characteristics of the xNF.

R-43958 The xNF Package **MUST** include documentation describing
the tests that were conducted by the xNF providor and the test results.

R-04298 The xNF provider **MUST** provide their testing scripts to
support testing.

R-58775 The xNF provider **MUST** provide software components that
can be packaged with/near the xNF, if needed, to simulate any functions
or systems that connect to the xNF system under test. This component is
necessary only if the existing testing environment does not have the
necessary simulators.

R-85653 The xNF **MUST** provide metrics (e.g., number of sessions,
number of subscribers, number of seats, etc.) to ONAP for tracking
every license.

R-44125 The xNF provider **MUST** agree to the process that can
be met by Service Provider reporting infrastructure. The Contract
shall define the reporting process and the available reporting tools.

R-40827 The xNF provider **MUST** enumerate all of the open
source licenses their xNF(s) incorporate.

R-97293 The xNF provider **MUST NOT** require audits of
Service Provider’s business.

R-44569 The xNF provider **MUST NOT** require additional
infrastructure such as a xNF provider license server for xNF provider
functions and metrics.

R-13613 The VNF **MUST** provide clear measurements for licensing
purposes to allow automated scale up/down by the management system.

R-27511 The VNF provider **MUST** provide the ability to scale
up a VNF provider supplied product during growth and scale down a
VNF provider supplied product during decline without “real-time”
restrictions based upon VNF provider permissions.

R-85991 The xNF provider **MUST** provide a universal license key
per xNF to be used as needed by services (i.e., not tied to a VM
instance) as the recommended solution. The xNF provider may provide
pools of Unique xNF License Keys, where there is a unique key for
each xNF instance as an alternate solution. Licensing issues should
be resolved without interrupting in-service xNFs.

R-47849 The xNF provider **MUST** support the metadata about
licenses (and their applicable entitlements) as defined in this
document for xNF software, and any license keys required to authorize
use of the xNF software.  This metadata will be used to facilitate
onboarding the xNF into the ONAP environment and automating processes
for putting the licenses into use and managing the full lifecycle of
the licenses. The details of this license model are described in
Tables C1 to C8 in the Appendix. Note: License metadata support in 
  ONAP is not currently available and planned for 1Q 2018.

Configuration Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

R-20741 The xNF **MUST** support ONAP Controller’s **Configure** command.

R-19366 The xNF **MUST** support ONAP Controller’s **ConfigModify** command.

R-32981 The xNF **MUST** support ONAP Controller’s **ConfigBackup** command.

R-48247 The xNF **MUST** support ONAP Controller’s **ConfigRestore** command.

R-94084 The xNF **MUST** support ONAP Controller’s **ConfigScaleOut**
command.

R-56385 The xNF **MUST** support ONAP Controller’s **Audit** command.

R-12706 The xNF **MUST** support ONAP Controller’s **QuiesceTraffic**
command.

R-07251 The xNF **MUST** support ONAP Controller’s **ResumeTraffic**
command.

R-83146 The xNF **MUST** support ONAP Controller’s **StopApplication**
command.

R-82811 The xNF **MUST** support ONAP Controller’s **StartApplication**
command.

R-19922 The xNF **MUST** support ONAP Controller’s **UpgradePrecheck**
command.

R-49466 The xNF **MUST** support ONAP Controller’s **UpgradeSoftware**
command.

R-45856 The xNF **MUST** support ONAP Controller’s **UpgradePostCheck**
command.

R-97343 The xNF **MUST** support ONAP Controller’s **UpgradeBackup**
command.

R-65641 The xNF **MUST** support ONAP Controller’s **UpgradeBackOut**
command.

R-11790 The VNF **MUST** support ONAP Controller’s
**Restart (stop/start or reboot)** command.

R-56218 The VNF **MUST** support ONAP Controller’s Migrate command that
moves container (VM) from a live Physical Server / Compute Node to
another live Physical Server / Compute Node.
  
R-38001 The VNF MUST support ONAP Controller’s **Rebuild** command.

R-76901 VNF MUST support a container rebuild mechanism based on existing
image (e.g. Glance image in Openstack environment) or a snapshot.

R-41430 The xNF **MUST** support ONAP Controller’s **HealthCheck**
command.

R-88026 The xNF **MUST** include a NETCONF server enabling
runtime configuration and lifecycle management capabilities.

R-95950 The xNF **MUST** provide a NETCONF interface fully defined
by supplied YANG models for the embedded NETCONF server.

R-73468 The xNF **MUST** allow the NETCONF server connection
parameters to be configurable during virtual machine instantiation
through Heat templates where SSH keys, usernames, passwords, SSH
service and SSH port numbers are Heat template parameters.

R-90007 The xNF **MUST** implement the protocol operation:
**close-session()**- Gracefully close the current session.

R-70496 The xNF **MUST** implement the protocol operation:
**commit(confirmed, confirm-timeout)** - Commit candidate
configuration datastore to the running configuration.

R-18733 The xNF **MUST** implement the protocol operation:
**discard-changes()** - Revert the candidate configuration
datastore to the running configuration.

R-44281 The xNF **MUST** implement the protocol operation:
**edit-config(target, default-operation, test-option, error-option,
config)** - Edit the target configuration datastore by merging,
replacing, creating, or deleting new config elements.

R-60106 The xNF **MUST** implement the protocol operation:
**get(filter)** - Retrieve (a filtered subset of) the running
configuration and device state information. This should include
the list of xNF supported schemas.

R-29488 The xNF **MUST** implement the protocol operation:
**get-config(source, filter)** - Retrieve a (filtered subset of
a) configuration from the configuration datastore source.

R-11235 The xNF **MUST** implement the protocol operation:
**kill-session(session)** - Force the termination of **session**.

R-02597 The xNF **MUST** implement the protocol operation:
**lock(target)** - Lock the configuration datastore target.

R-96554 The xNF **MUST** implement the protocol operation:
**unlock(target)** - Unlock the configuration datastore target.

R-29324 The xNF **SHOULD** implement the protocol operation:
**copy-config(target, source) -** Copy the content of the
configuration datastore source to the configuration datastore target.

R-88031 The xNF **SHOULD** implement the protocol operation:
**delete-config(target) -** Delete the named configuration
datastore target.

R-97529 The xNF **SHOULD** implement the protocol operation:
**get-schema(identifier, version, format) -** Retrieve the YANG schema.

R-62468 The xNF **MUST** allow all configuration data to be
edited through a NETCONF <edit-config> operation. Proprietary
NETCONF RPCs that make configuration changes are not sufficient.

R-01382 The xNF **MUST** allow the entire configuration of the
xNF to be retrieved via NETCONF's <get-config> and <edit-config>,
independently of whether it was configured via NETCONF or other
mechanisms.

R-28756 The xNF **MUST** support **:partial-lock** and
**:partial-unlock** capabilities, defined in RFC 5717. This
allows multiple independent clients to each write to a different
part of the <running> configuration at the same time.

R-83873 The xNF **MUST** support **:rollback-on-error** value for
the <error-option> parameter to the <edit-config> operation. If any
error occurs during the requested edit operation, then the target
database (usually the running configuration) will be left unaffected.
This provides an 'all-or-nothing' edit mode for a single <edit-config>
request.

R-68990 The xNF **MUST** support the **:startup** capability. It
will allow the running configuration to be copied to this special
database. It can also be locked and unlocked.

R-68200 The xNF **MUST** support the **:url** value to specify
protocol operation source and target parameters. The capability URI
for this feature will indicate which schemes (e.g., file, https, sftp)
that the server supports within a particular URL value. The 'file'
scheme allows for editable local configuration databases. The other
schemes allow for remote storage of configuration databases.

R-20353 The xNF **MUST** implement both **:candidate** and
**:writable-running** capabilities. When both **:candidate** and
**:writable-running** are provided then two locks should be supported.

R-11499 The xNF **MUST** fully support the XPath 1.0 specification
for filtered retrieval of configuration and other database contents.
The 'type' attribute within the <filter> parameter for <get> and
<get-config> operations may be set to 'xpath'. The 'select' attribute
(which contains the XPath expression) will also be supported by the
server. A server may support partial XPath retrieval filtering, but
it cannot advertise the **:xpath** capability unless the entire XPath
1.0 specification is supported.

R-83790 The xNF **MUST** implement the **:validate** capability

R-49145 The xNF **MUST** implement **:confirmed-commit** If
**:candidate** is supported.

R-58358 The xNF **MUST** implement the **:with-defaults** capability
[RFC6243].

R-59610 The xNF **MUST** implement the data model discovery and
download as defined in [RFC6022].

R-93443 The xNF **MUST** define all data models in YANG [RFC6020],
and the mapping to NETCONF shall follow the rules defined in this RFC.

R-26115 The xNF **MUST** follow the data model upgrade rules defined
in [RFC6020] section 10. All deviations from section 10 rules shall
be handled by a built-in automatic upgrade mechanism.

R-10716 The xNF **MUST** support parallel and simultaneous
configuration of separate objects within itself.

R-29495 The xNF **MUST** support locking if a common object is
being manipulated by two simultaneous NETCONF configuration operations
on the same xNF within the context of the same writable running data
store (e.g., if an interface parameter is being configured then it
should be locked out for configuration by a simultaneous configuration
operation on that same interface parameter).

R-53015 The xNF **MUST** apply locking based on the sequence of
NETCONF operations, with the first configuration operation locking
out all others until completed.

R-02616 The xNF **MUST** permit locking at the finest granularity
if a xNF needs to lock an object for configuration to avoid blocking
simultaneous configuration operations on unrelated objects (e.g., BGP
configuration should not be locked out if an interface is being
configured or entire Interface configuration should not be locked out
if a non-overlapping parameter on the interface is being configured).

R-41829 The xNF **MUST** be able to specify the granularity of the
lock via a restricted or full XPath expression.

R-66793 The xNF **MUST** guarantee the xNF configuration integrity
for all simultaneous configuration operations (e.g., if a change is
attempted to the BUM filter rate from multiple interfaces on the same
EVC, then they need to be sequenced in the xNF without locking either
configuration method out).

R-54190 The xNF **MUST** release locks to prevent permanent lock-outs
when/if a session applying the lock is terminated (e.g., SSH session
is terminated).

R-03465 The xNF **MUST** release locks to prevent permanent lock-outs
when the corresponding <partial-unlock> operation succeeds.

R-63935 The xNF **MUST** release locks to prevent permanent lock-outs
when a user configured timer has expired forcing the NETCONF SSH Session
termination (i.e., product must expose a configuration knob for a user
setting of a lock expiration timer)

R-10173 The xNF **MUST** allow another NETCONF session to be able to
initiate the release of the lock by killing the session owning the lock,
using the <kill-session> operation to guard against hung NETCONF sessions.

R-88899 The xNF **MUST** support simultaneous <commit> operations
within the context of this locking requirements framework.

R-07545 The xNF **MUST** support all operations, administration and
management (OAM) functions available from the supplier for xNFs using
the supplied YANG code and associated NETCONF servers.

R-60656 The xNF **MUST** support sub tree filtering.

R-80898 The xNF **MUST** support heartbeat via a <get> with null filter.

R-25238 The xNF PACKAGE **MUST** validated YANG code using the open
source pyang [3]_ program using the following commands:

R-63953 The xNF **MUST** have the echo command return a zero value
otherwise the validation has failed

R-26508 The xNF **MUST** support a NETCONF server that can be mounted on
OpenDaylight (client) and perform the operations of: modify, update,
change, rollback configurations using each configuration data element,
query each state (non-configuration) data element, execute each YANG
RPC, and receive data through each notification statement.

R-28545 The xNF **MUST** conform its YANG model to RFC 6060,
“YANG - A Data Modeling Language for the Network Configuration
Protocol (NETCONF)”

R-22700 The xNF **MUST** conform its YANG model to RFC 6470,
“NETCONF Base Notifications”.

R-10353 The xNF **MUST** conform its YANG model to RFC 6244,
“An Architecture for Network Management Using NETCONF and YANG”.

R-53317 The xNF **MUST** conform its YANG model to RFC 6087,
“Guidelines for Authors and Reviewers of YANG Data Model Documents”.

R-33955 The xNF **SHOULD** conform its YANG model to RFC 6991,
“Common YANG Data Types”.

R-22946 The xNF **SHOULD** conform its YANG model to RFC 6536,
“NETCONF Access Control Model”.

R-10129 The xNF **SHOULD** conform its YANG model to RFC 7223,
“A YANG Data Model for Interface Management”.

R-12271 The xNF **SHOULD** conform its YANG model to RFC 7223,
“IANA Interface Type YANG Module”.

R-49036 The xNF **SHOULD** conform its YANG model to RFC 7277,
“A YANG Data Model for IP Management”.

R-87564 The xNF **SHOULD** conform its YANG model to RFC 7317,
“A YANG Data Model for System Management”.

R-24269 The xNF **SHOULD** conform its YANG model to RFC 7407,
“A YANG Data Model for SNMP Configuration”, if Netconf used to
configure SNMP engine.

R-33946 The xNF **MUST** conform to the NETCONF RFC 4741,
“NETCONF Configuration Protocol”.

R-04158 The xNF **MUST** conform to the NETCONF RFC 4742,
“Using the NETCONF Configuration Protocol over Secure Shell (SSH)”.

R-13800 The xNF **MUST** conform to the NETCONF RFC 5277,
“NETCONF Event Notification”.

R-01334 The xNF **MUST** conform to the NETCONF RFC 5717,
“Partial Lock Remote Procedure Call”.

R-08134 The xNF **MUST** conform to the NETCONF RFC 6241,
“NETCONF Configuration Protocol”.

R-78282 The xNF **MUST** conform to the NETCONF RFC 6242,
“Using the Network Configuration Protocol over Secure Shell”.

R-31809 The xNF **MUST** support the HealthCheck RPC. The HealthCheck
RPC executes a xNF Provider-defined xNF HealthCheck over the scope of
the entire xNF (e.g., if there are multiple VNFCs, then run a health check,
as appropriate, for all VNFCs). It returns a 200 OK if the test completes.
A JSON object is returned indicating state (healthy, unhealthy), scope
identifier, time-stamp and one or more blocks containing info and fault
information. If the xNF is unable to run the HealthCheck, return a
standard http error code and message.

R-79224 The xNF **MUST** have the chef-client be preloaded with
validator keys and configuration to register with the designated
Chef Server as part of the installation process.

R-72184 The xNF **MUST** have routable FQDNs for all the endpoints
(VMs) of a xNF that contain chef-clients which are used to register
with the Chef Server.  As part of invoking xNF actions, ONAP will
trigger push jobs against FQDNs of endpoints for a xNF, if required.

R-47068 The xNF **MAY** expose a single endpoint that is
responsible for all functionality.

R-67114 The xNF **MUST** be installed with Chef-Client >= 12.0 and
Chef push jobs client >= 2.0.

R-27310 The xNF Package **MUST** include all relevant Chef artifacts
(roles/cookbooks/recipes) required to execute xNF actions requested by
ONAP for loading on appropriate Chef Server.

R-26567 The xNF Package **MUST** include a run list of
roles/cookbooks/recipes, for each supported xNF action, that will
perform the desired xNF action in its entirety as specified by ONAP
(see Section 7.c, ONAP Controller APIs and Behavior, for list of xNF
actions and requirements), when triggered by a chef-client run list
in JSON file.

R-98911 The xNF **MUST NOT** use any instance specific parameters
for the xNF in roles/cookbooks/recipes invoked for a xNF action.

R-37929 The xNF **MUST** accept all necessary instance specific
data from the environment or node object attributes for the xNF
in roles/cookbooks/recipes invoked for a xNF action.

R-62170 The xNF **MUST** over-ride any default values for
configurable parameters that can be set by ONAP in the roles,
cookbooks and recipes.

R-78116 The xNF **MUST** update status on the Chef Server
appropriately (e.g., via a fail or raise an exception) if the
chef-client run encounters any critical errors/failures when
executing a xNF action.

R-44013 The xNF **MUST** populate an attribute, defined as node
[‘PushJobOutput’] with the desired output on all nodes in the push job
that execute chef-client run if the xNF action requires the output of a
chef-client run be made available (e.g., get running configuration).

R-30654 The xNF Package **MUST** have appropriate cookbooks that are
designed to automatically ‘rollback’ to the original state in case of
any errors for actions that change state of the xNF (e.g., configure).

R-65755 The xNF **SHOULD** support callback URLs to return information
to ONAP upon completion of the chef-client run for any chef-client run
associated with a xNF action.

R-15885 The xNF **MUST** Upon completion of the chef-client run,
POST back on the callback URL, a JSON object as described in Table
A2 if the chef-client run list includes a cookbook/recipe that is
callback capable. Failure to POST on the Callback Url should not be
considered a critical error. That is, if the chef-client successfully
completes the xNF action, it should reflect this status on the Chef
Server regardless of whether the Callback succeeded or not.

R-32217 The xNF **MUST** have routable FQDNs that are reachable via
the Ansible Server for the endpoints (VMs) of a xNF on which playbooks
will be executed. ONAP will initiate requests to the Ansible Server
for invocation of playbooks against these end points [4]_.

R-54373 The xNF **MUST** have Python >= 2.6 on the endpoint VM(s)
of a xNF on which an Ansible playbook will be executed.

R-35401 The xNF **MUST** support SSH and allow SSH access by the
Ansible server for the endpoint VM(s) and comply with the Network
Cloud Service Provider guidelines for authentication and access.

R-82018 The xNF **MUST** load the Ansible Server SSH public key onto xNF
VM(s) as part of instantiation. This will allow the Ansible Server
to authenticate to perform post-instantiation configuration without
manual intervention and without requiring specific xNF login IDs
and passwords.

R-92866 The xNF **MUST** include as part of post-instantiation configuration
done by Ansible Playbooks the removal/update of the SSH public key from
/root/.ssh/authorized_keys, and  update of SSH keys loaded through
instantiation to support Ansible. This may include download and install of
new SSH keys and new mechanized IDs.

R-91745 The xNF **MUST** update the Ansible Server and other entities
storing and using the SSH keys for authentication when the SSH keys used
by Ansible are regenerated/updated.

R-40293 The xNF **MUST** make available playbooks that conform
to the ONAP requirement.

R-49396 The xNF **MUST** support each ONAP (APPC) xNF action by invocation
of **one** playbook [7]_. The playbook will be responsible
for executing all necessary tasks (as well as calling other playbooks)
to complete the request.

R-33280 The xNF **MUST NOT** use any instance specific parameters
in a playbook.

R-48698 The xNF **MUST** utilize information from key value pairs
that will be provided by the Ansible Server as "extra-vars" during
invocation to execute the desired xNF action. If the playbook requires
files, they must also be supplied using the methodology detailed in
the Ansible Server API, unless they are bundled with playbooks, example,
generic templates.

R-43253 The xNF **MUST** use playbooks designed to allow Ansible
Server to infer failure or success based on the “PLAY_RECAP” capability.
NOTE: There are cases where playbooks need to interpret results of a task
and then determine success or failure and return result accordingly
(failure for failed tasks).

R-50252 The xNF **MUST** write to a specific one text files that
will be retrieved and made available by the Ansible Server if, as part
of a xNF action (e.g., audit), a playbook is required to return any
xNF information. The text files must be written in the same directory as
the one from which the playbook is being executed. A text file must be
created for the xNF playbook run targets/affects, with the name
‘<VNFname>_results.txt’ into which any desired output from each
respective VM/xNF must be written.

R-51442 The xNF **SHOULD** use playbooks that are designed to
automatically ‘rollback’ to the original state in case of any errors
for actions that change state of the xNF (e.g., configure).

R-58301 The xNF **SHOULD NOT** use playbooks that make requests to
Cloud resources e.g. Openstack (nova, neutron, glance, heat, etc.);
therefore, there is no use for Cloud specific variables like Openstack
UUIDs in Ansible Playbooks.

R-02651 The xNF **SHOULD** use the Ansible backup feature to save a
copy of configuration files before implementing changes to support
operations such as backing out of software upgrades, configuration
changes or other work as this will help backing out of configuration
changes when needed.

R-43353 The xNF **MUST** return control from Ansible Playbooks only
after tasks are fully complete, signaling that the playbook completed
all tasks. When starting services, return control only after all services
are up. This is critical for workflows where the next steps are dependent

R-51910 The xNF **MUST** provide all telemetry (e.g., fault event
records, syslog records, performance records etc.) to ONAP using the
model, format and mechanisms described in this section.

R-19624 The xNF **MUST** encode and serialize content delivered to
ONAP using JSON (RFC 7159) plain text format. High-volume data is to
be encoded and serialized using `Avro <http://avro.apache.org/>`_,
where the Avro [6]_ data format are described using JSON.

Note:

- JSON plain text format is preferred for moderate volume data sets
  (option 1), as JSON has the advantage of having well-understood simple
  processing and being human-readable without additional decoding. Examples
  of moderate volume data sets include the fault alarms and performance
  alerts, heartbeat messages, measurements used for xNF scaling and syslogs.
- Binary format using Avro is preferred for high volume data sets
  (option 2) such as mobility flow measurements and other high-volume
  streaming events (such as mobility signaling events or SIP signaling)
  or bulk data, as this will significantly reduce the volume of data
  to be transmitted. As of the date of this document, all events are
  reported using plain text JSON and REST.
- Avro content is self-documented, using a JSON schema. The JSON schema is
  delivered along with the data content
  (http://avro.apache.org/docs/current/ ). This means the presence and
  position of data fields can be recognized automatically, as well as the
  data format, definition and other attributes. Avro content can be
  serialized as JSON tagged text or as binary. In binary format, the
  JSON schema is included as a separate data block, so the content is
  not tagged, further compressing the volume. For streaming data, Avro
  will read the schema when the stream is established and apply the
  schema to the received content.

R-98191 The xNF **MUST** vary the frequency that asynchronous data is
delivered based on the content and how data may be aggregated or grouped
together.

Note:

- For example, alarms and alerts are expected to be delivered as soon
  as they appear. In contrast, other content, such as performance
  measurements, KPIs or reported network signaling may have various ways
  of packaging and delivering content. Some content should be streamed
  immediately; or content may be monitored over a time interval, then packaged
  as collection of records and delivered as block; or data may be collected
  until a package of a certain size has been collected; or content may be
  summarized statistically over a time interval, or computed as a KPI, with
  the summary or KPI being delivered.
- We expect the reporting frequency to be configurable depending
  on the virtual network function’s needs for management. For example,
  Service Provider may choose to vary the frequency of collection between
  normal and trouble-shooting scenarios.
- Decisions about the frequency of data reporting will affect the
  size of delivered data sets, recommended delivery method, and how the
  data will be interpreted by ONAP. These considerations should not
  affect deserialization and decoding of the data, which will be guided
  by the accompanying JSON schema or GPB definition files.

R-88482 The xNF **SHOULD** use REST using HTTPS delivery of plain
text JSON for moderate sized asynchronous data sets, and for high
volume data sets when feasible.

R-84879 The xNF **MUST** have the capability of maintaining a primary
and backup DNS name (URL) for connecting to ONAP collectors, with the
ability to switch between addresses based on conditions defined by policy
such as time-outs, and buffering to store messages until they can be
delivered. At its discretion, the service provider may choose to populate
only one collector address for a xNF. In this case, the network will
promptly resolve connectivity problems caused by a collector or network
failure transparently to the xNF.

R-81777 The xNF **MUST** be configured with initial address(es) to use
at deployment time. Subsequently, address(es) may be changed through
ONAP-defined policies delivered from ONAP to the xNF using PUTs to a
RESTful API, in the same manner that other controls over data reporting
will be controlled by policy.

R-08312 The xNF **MAY** use another option which is expected to include REST
delivery of binary encoded data sets.

R-79412 The xNF **MAY** use another option which is expected to include TCP
for high volume streaming asynchronous data sets and for other high volume
data sets. TCP delivery can be used for either JSON or binary encoded data
sets.

R-01033 The xNF **MAY** use another option which is expected to include SFTP
for asynchronous bulk files, such as bulk files that contain large volumes of
data collected over a long time interval or data collected across many xNFs.
(Preferred is to reorganize the data into more frequent or more focused data
sets, and deliver these by REST or TCP as appropriate.)

R-63229 The xNF **MAY** use another option which is expected to include REST
for synchronous data, using RESTCONF (e.g., for xNF state polling).

R-03070 The xNF **MUST**, by ONAP Policy, provide the ONAP addresses
as data destinations for each xNF, and may be changed by Policy while
the xNF is in operation. We expect the xNF to be capable of redirecting
traffic to changed destinations with no loss of data, for example from
one REST URL to another, or from one TCP host and port to another.

R-06924 The xNF **MUST** deliver asynchronous data as data becomes
available, or according to the configured frequency.

R-73285 The xNF **MUST** must encode, address and deliver the data
as described in the previous paragraphs.

R-42140 The xNF **MUST** respond to data requests from ONAP as soon
as those requests are received, as a synchronous response.

R-34660 The xNF **MUST** use the RESTCONF/NETCONF framework used by
the ONAP configuration subsystem for synchronous communication.

R-86586 The xNF **MUST** use the YANG configuration models and RESTCONF
[RFC8040] (https://tools.ietf.org/html/rfc8040).

R-11240 The xNF **MUST** respond with content encoded in JSON, as
described in the RESTCONF specification. This way the encoding of a
synchronous communication will be consistent with Avro.

R-70266 The xNF **MUST** respond to an ONAP request to deliver the
current data for any of the record types defined in
Event Records - Data Structure Description by returning the requested
record, populated with the current field values. (Currently the defined
record types include fault fields, mobile flow fields, measurements for
xNF scaling fields, and syslog fields. Other record types will be added
in the future as they become standardized and are made available.)

R-46290 The xNF **MUST** respond to an ONAP request to deliver granular
data on device or subsystem status or performance, referencing the YANG
configuration model for the xNF by returning the requested data elements.

R-43327 The xNF **SHOULD** use `Modeling JSON text with YANG
<https://tools.ietf.org/html/rfc7951>`_, If YANG models need to be
translated to and from JSON[RFC7951]. YANG configuration and content can
be represented via JSON, consistent with Avro, as described in “Encoding
and Serialization” section.

R-42366 The xNF **MUST** support secure connections and transports such as
Transport Layer Security (TLS) protocol
[`RFC5246 <https://tools.ietf.org/html/rfc5246>`_] and should adhere to
the best current practices outlined in
`RFC7525 <https://tools.ietf.org/html/rfc7525>`_.

R-44290 The xNF **MUST** control access to ONAP and to xNFs, and creation
of connections, through secure credentials, log-on and exchange mechanisms.

R-47597 The xNF **MUST** carry data in motion only over secure connections.

R-68165 The xNF **MUST** encrypt any content containing Sensitive Personal
Information (SPI) or certain proprietary data, in addition to applying the
regular procedures for securing access and delivery.


Ansible Playbook Examples
-----------------------------------------------

The following sections contain examples of Ansible playbooks
which follow the guidelines.

Guidelines for Playbooks to properly integrate with APPC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NOTE: To support concurrent requests to multiple VNF instances of same
or different type, VNF hosts and other files with VNF specific default
values are kept or created in separate directories.

Example of an Ansible command (after pwd) to run playbook again
vfdb9904v VNF instance:

.. code-block:: none

 $ pwd
 /storage/vfdb/V16.1/ansible/configure
 $ ansible-playbook -i ../inventory/vfdb9904vhosts site.yml --extra-vars "vnf_instance=vfdb9904v"

 NOTE: To preserve Ansible inventory/group_vars capability, that makes
 group_vars contents global variables available to all playbooks, when they
 reside in the inventory directory, guidelines are being updated to name the
 VNF inventory hosts file as (a flat file) <VNFName>hosts, stored in the
 inventory directory, not a subdirectory under inventory. In the above
 example: vfdb9904vhosts (removed / VNF name and hosts vfdb9904/vhosts)

Example of corresponding APPC API Call from ONAP – Ansible Server
Specifications:

An example of a curl request simulating a Rest API POST requesting execution
of configure Playbook (using playbook relative path):

.. code-block:: none

 curl -u APIUser:APIPassword -H "Content-type:application/json" -X POST
 -d '{"Id": "8412", "PlaybookName": "vfdb/V5.x.x/ansible/configure/site.yml",
 "Timeout":"600", "EnvParameters": { "vnf_instance": "vfdb9904v" }}'
 http://ansible.server.com:5000/Dispatch

Rest API GET request to obtain response/results for prior request
(same Id as POST request above):

.. code-block:: none

 curl -u APIUser:APIPassword -H 'Content-type: application/json' -X GET
 'http://ansible.server.com:5000/Dispatch/?Id=8412&Type=GetResult'

Comments:

-  An ID number is assigned to each request. This ID number is used to
   track request down to completion and provide status to APPC when
   requested.

-  Playbook Name relative path provided in the request as PlaybookName

-  Ansible Server Rest API is aware of playbook’s root directory which may
   vary from instance to instance or Ansible Server cluster to cluster.

Ansible Playbooks will use the VNF instance name (passed using
--extra-vars "vnf\_instance=vfdb9904v") to identify other default values
to run the playbook(s) against the target VNF instance. Same example as
above:

.. code-block:: none

 $ ansible-playbook -i ../inventory/vfdb9904vhosts site.yml --extra-vars "vnf_instance=vfdb9904v"

Each Ansible Server or cluster is assigned its own identification to be used
to authenticate to VNF VMs using Ansible Server or cluster specific set of
SSH keys that may be rotated regularly. Here hosts file, no longer referencing
file with SSH key credentials, to run ansible-playbook listed in this example
above (IP addresses were scrubbed):

.. code-block:: none

 $ more ../inventory/vfdb9904v/hosts
 [host]
 localhost ansible_connection=local

 [oam]
 1xx.2yy.zzz.109
 1xx.2yy.zzz.110

 [rdb]
 1xx.2yy.zzz.105
 1xx.2yy.zzz.106

NOTE: APPC requests to run Playbooks/Cookbooks are specific to a VNF,
but could be more limited to one VM or one type of VM by the request
parameters. Actions that may impact a site (LCP), a service, or an
entire platform must be orchestrated by MSO in order to execute requests
via APPC which then invoke VNF level playbooks. Playbooks that impact
more than a single VNF are not the current focus of these guidelines.

Since last release of these guidelines, based on recent learnings,
moving VNF Type global variables under inventory/group_vars files, this
way variables and respective values are available to all playbooks without
being explicitly referenced though an include statement. Also creating
templates that are VNF Type specific, but moving away from static files
that are VNF instance specific, working to obtain VNF instance specific
from other sources, inventory database, etc.

And here the scrubbed default arguments for this VNF instance(originated
from previously re-factored playbooks now being phased out):

.. code-block:: none

 vnf_instance=vfdb9904v

 $ more ../vars/vfdb9904v/default_args.yml
 vm_config_oam_vnfc_name: vfdb9904vm001oam001
 vm_config_oam_hostname: vfdb9904vm001
 vm_config_oam_provider_ip_address: 1xx.2yy.zzz.109
 …

IMPORTANT: The APPC and default file attribute name for
vm\_config\_oam\_vnfc\_name, as an example, is derived from vm\_config
array structure (list) in the CSAR package ENV file, with dots replaced
by underscore:

.. code-block:: none

 vm_config:

 oam: {vnfc_name: {{ vm_config_oam_vnfc_name }}, hostname: {{
 vm_config_oam_hostname }}, provider_ip_address: {{
 vm_config_oam_provider_ip_address }
 },
 …

Parameters like VNF names, VNFC names, OA&M IP addresses, after
February, 2018 ONAP release, will be extracted from A&AI by APPC and
then passed down to Ansible Server, as part of APPC request through REST
API. In the meantime, VNF instance specific required values, will
be stored on VNF instance directory, default arguments file and will be
used as defaults. For parameterized playbooks attribute-value pairs
passed down by APPC to Ansible Server always take precedence over
template or VNF instance specific defaults stored in defaults file(s).

.. code-block:: none

 $ pwd
 /storage/vfdb/latest/ansible
 Again, originated from previously re-factored playbooks now being phased out:

 $ more vars/vfdb9904v/default_args.yml

 vm_config_oam1_vnfc_name: vfdb9904vm001oam001
 vm_config_oam1_hostname: vfdb9904vm001
 vm_config_oam1_provider_ip_address: 1xx.2yy.zzz.109

 vm_config_oam2_vnfc_name: vfdb9904vm002oam001
 vm_config_oam2_hostname: vfdb9904vm002
 vm_config_oam2_provider_ip_address: 1xx.2yy.zzz.110

 vm_config_rdb1_vnfc_name: vfdb9904vm003rdb001
 vm_config_rdb1_hostname: vfdb9904vm003
 vm_config_rdb1_provider_ip_address: 1xx.2yy.zzz.105

 vm_config_rdb2_vnfc_name: vfdb9904vm004rdb001
 vm_config_rdb2_hostname: vfdb9904vm004
 vm_config_rdb2_provider_ip_address: 1xx.2yy.zzz.106

 vm_config_rdb3_vnfc_name: vfdb9904vm005rdb001
 vm_config_rdb3_hostname: vfdb9904vm005
 vm_config_rdb3_provider_ip_address: 1xx.2yy.zzz.xxx

 vm_config_rdb4_vnfc_name: vfdb9904vm006rdb001
 vm_config_rdb4_hostname: vfdb9904vm006
 vm_config_rdb4_provider_ip_address: 1xx.2yy.zzz.yyy

One of the first tasks on the Ansible Playbooks is to combine the VNF
type generic template, derived from ENV files in CSAR or other files,
with these default values stored on the Ansible Server, together with
the overriding parameters passed down from APPC, to create the VNF
instance specific set of attribute-value pairs to be used for the run, in
INI format. Here is an excerpt from such a file that should look
somewhat similar to ENV files:

.. code-block:: none

 $ more tmp/vfdb9904v/all.yml

 deployment_prefix: vfdb9904v
 …
 timezone: Etc/UTC
 …
 template_version: '2014-10-16'
 stack_name: vfdb9904v
 c3dbtype: OAM
 stackName: vfdb9904v
 juno_base: true
 …

# logins list contain 'login name', 'login group', 'login password'

.. code-block:: none

 logins:
 - { name: 'm99999', group: 'm99999', password: 'abcdefgha' }
 - { name: 'gsuser', group: 'gsuser', password: ' abcdefgha' }
 - { name: 'peruser', group: 'peruser', password: ' abcdefgha' }
 - { name: 'dbuser', group: 'dbuser', password: ' abcdefgha' }

NOTE: Arguments passed by APPC to Ansible Server to run a playbook take
precedence over any defaults stored in Ansible Server.

Ansible Playbooks – Notes On Artifacts Required to Run Playbooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inventory hosts file: should be VNF instance specific.

Default variables: should be VNF instance specific.

NOTE: Some playbooks may rely on inventory directory contents to target
the collection of VNFs in the Services Platform supported through
Ansible.

Playbooks and paths to referenced files: Playbooks shall not use
absolute paths in include or import entries (variables or playbooks) or
other types of references.

For this to work properly, when running playbooks, the directory where
the main playbook resides shall be the current directory.

Playbook imports, when used, shall use paths relative to the main
playbook directory.

Root directory named ansible - Any files provided with playbooks,
included, imported, or referenced by playbooks, shall reside under the ansible
playbooks (root) directory, containing all playbook subdirectories, or
below that ansible root directory, in other subdirectories to support
on-boarding and portability of VNF collection of playbooks and related
artifacts.

Designing for a shared environment, concurrently running playbooks,
targeting multiple VNF instances – inventory hosts file:

To avoid inventory hosts file overwrites or collisions between multiple
concurrently running VNF instance requests, chosen approach is for each
VNF instance hosts file, to be stored under the Ansible Server Playbooks
root directory, under the inventory subdirectory, and under a directory
for each VNF instance, named after the VNF instance, as follows:

ansible/inventory/<VNF\_instance\_name>/hosts

Example of inventory hosts file path, relative to ansible playbooks root
directory (playbooks\_dir): ansible/inventory/vnfx0001v/hosts

**Designing for a shared environment, concurrently running multiple playbooks,
targeting multiple VNF instances – default argument variables for
specific VNF instances:**

Files containing attribute name value pairs (variable name and default
values), referenced/included by playbooks – Files containing VNF
instance specific default values – in a later APPC release, some or all
the default attribute value pairs contained in the defaults file, may be
passed down by APPC, to the Ansible Server, overriding these defaults:

VNF instance specific files
referenced/included by playbooks, containing default values, example,
default\_args.yml, shall be stored under a directory with VNF instance
name on the path.

Example:

ansible/vars/<VNF\_instance\_name>/default\_args.yml

Example of include statement:

- include_vars: ../vars/{{ vnf_instance }}/default_args.yml

Again, this was originated from previously re-factored playbooks, now being
phased out, to move away from having to create VNF instance specific files
with VNF instance default variables. Moving to extract these values from
inventory databases and provide them to Ansible Server as part of the APPC
request, but may be used in a transition from having everything stored in the
Ansible Server to APPC extracting and providing VNF instance specific
attribute-value pairs to the Ansible Server as part of the request.

Files containing attribute name value pairs (variable name and default
values), referenced/included by playbooks – created dynamically by
playbooks:

To avoid
overwrites or collisions of multiple concurrently running VNF instance
requests, files created dynamically by playbooks, based on VNF generic
templates, combined with default values and arguments passed down by
APPC (as part of the request), shall be stored under a directory with
VNF instance name on the path.

Example:

tmp/<VNF\_instance\_name>/all.yml

Files containing site specific (Openstack location non-instance
specific) attribute name value pairs, like NTP server and DNS server’s
IP addresses and other parameters, referenced/included by playbooks, not
VNF specific – Could/should be stored under inventory/group_vars directory,
in a subdirectory named after the string used to identify the site (nyc1,
lax2,…).

Examples:

ansible/inventory/group_vars/<Site>

ansible/inventory/group_vars/nyc1

ansible/inventory/group_vars/lax2


\ **Ansible Server Design - Directory Structure**

To help understanding the contents of this section, here are few basic
definitions:

**VNF type a.k.a VNF Function Code** - Based on current Services
Platform naming convention, each Virtual Network Function is assigned a
4 character string (example vfdb), these are 4 characters in
the VNF instance name, followed by (4) numbers, ending in a "v", but the
naming convention is evolving. VNF instance name in
some cases corresponds to the stack name for the VNF when VNF instance
is built based on a single module, single stack. Example of VNF instance
name: vfdb9904v. All VNF performing this function, running the same
software, coming from the same VNF provider will have the same 4
characters in the VNF instance name, in this example, vfdb.

NOTE: New naming convention includes a prefix indicating geographical
location where VNF is instantiated.

VNF type, determined through these 4 characters, is also known as VNF
Function Code and is assigned by inventory team. All Services Platform
VNF Function Codes can be found in inventory database and/or A&AI as
well as Services Platform Network Design Documents.

Version – As in VNF software version is the release of the software
running on the VNF for which the playbooks were developed. VNF
configuration steps may change from release to release and this
<Version> in the path will allow the Ansible Server to host playbooks
associated with each software release. And run the playbooks that match
the software release running on each VNF instance. APPC initially will
not support playbook versioning only latest playbook is supported or a hard
coded version that later should become a variable to allow multiple
actively in use playbook versions according to VNF release.

Playbook Function - Is a name associated with a life cycle management
task(s) performed by the playbook(s) stored in this directory. It should
clearly identify the type of action(s) performed by the main playbook
and possibly other playbooks stored in this same directory. Ideally,
playbook function would match APPC corresponding command or function that
is performed by the main playbook in this directory. Following Ansible naming
standards main playbook is usually named site.yml. There can be other
playbooks on the same directory that use a subset of the roles used by the
main playbook site.yml. Examples of Playbook Function directory names:

-  configure – Contains post-instantiation (bulk) configuration
   playbooks, roles,…

-  healthcheck – Contains VNF health check playbook(s), roles,…

-  stop – Contains VNF application stop  (stopApplication) playbook(s),
   roles,…

-  start – Contains VNF application start (startApplication) playbook(s),
   roles,…

Directory structure to allow hosting multiple version sets of playbooks,
for the same VNF type, to be hosted in the runtime environment on the
Ansible Servers. Generic directory structure:

Ansible Playbooks – Function directory and main playbook:

.. code-block:: none

 <VNF type>/<Version>/ansible/<Playbook Function>/site.yml

Example – Post-instantiation (bulk) configuration –APPC Function -
Configure:

.. code-block:: none

 <VNF type>/<Version>/ansible/configure/site.yml

Example – Post-instantiation (bulk) configuration –APPC Function
– Configure – VNF software version 16.1:

.. code-block:: none

 vfdb/V16.1/ansible/configure/site.yml

Example – Health-check –APPC Function - HealthCheck:

.. code-block:: none

 <VNF type>/<Version>/ansible/healthcheck/site.yml

OR (Function directory name does not need to match APPC function name)

.. code-block:: none

 <VNF type>/<Version>/ansible/check/site.yml

Ansible Directories for other artifacts – VNF inventory hosts file -
Required:

.. code-block:: none

 <VNF type>/<Version>/ansible/inventory/<VNF instance name>hosts

Ansible Directories for other artifacts – VNF instance specific default
arguments – Optional:

.. code-block:: none

 <VNF type>/<Version>/ansible/group_vars/<VNF instance name>

NOTE: This requirement is expected to be deprecated all or in part in the
future, for automated actions, once APPC can pass down all VNF specific
arguments for each action. Requirement remains while manual actions are
to be supported. Other automated inventory management mechanisms may be
considered in the future, Ansible supports many automated inventory
management mechanisms/tools/solutions.

Ansible Directories for other artifacts – VNF (special) groups –
Optional:

.. code-block:: none

 <VNF type>/<Version>/ansible/inventory/group_vars/<VNF instance name>

NOTE: Default groups will be created based on VNFC type, 3 characters,
on VNFC name. Example: “oam”, “rdb”, “dbs”, “man”, “iox”, “app”,…

Ansible Directories for other artifacts – VNF (special) other files –
Optional – Example – License file:

.. code-block:: none

 <VNF type>/<Version>/ansible/<Other directory(s)>

CAUTION: On referenced files used/required by playbooks.

-  To avoid missing files, during on-boarding or uploading of Ansible
   Playbooks and related artifacts, all permanent files (not generated
   by playbooks as part of execution), required to run any playbook,
   shall reside under the ansible root directory or below on other
   subdirectories.

-  Any references to files, on includes or other playbook entries, shall
   use relative paths.

-  This is the ansible (root) directory referenced on this
   note (Ansible Server mount point not included):

.. code-block:: none

     <VNF type>/<Version>/ansible/

There will be a soft link to the latest set of Ansible Playbooks for
each VNF type.

VNF type directories use A&AI inventory VNF function code. Ansible
Playbooks will be stored on a Cinder Volume mounted on the Ansible
Servers as /storage. Example:

/storage/vfdb/latest/ansible – This soft link point to the latest set of
playbooks (or the only set)

/storage/vfdb/V16.1/ansible – Root directory for database VNF Ansible
Playbooks for release 16.1

CAUTION: To support this directory structure as the repository to store
Ansible Playbooks run by APPC, APPC API in the Ansible Server side needs
to be configured to run playbooks from directory, not MySQL database.

Ansible Server HTTP will be configured to support APPC REST API requests
to run playbooks as needed, against specific VNF instances, or specific
VM(s) as specified in the request.

ONAP APPC REST API to Ansible Server is documented separately and can be
found under ONAP (onap.org).

**Ansible Server – On-boarding Ansible Playbooks**

Once playbooks are developed following the guidelines listed in prior
section(s), playbooks need to be on-boarded onto Ansible Server(s). In
the future, they’ll be on-boarded and distributed through ONAP, at least
that is the proposed plan, but for now they need to be uploaded
manually. There is work in progress to use a Git as the playbook
repository to store and track playbooks by version, version control.

These are the basic steps to on-board playbooks manually onto the
Ansible Server.

1. Upload CSAR, zip, or tar file containing VNF playbooks and related
   artifacts.

2. Create full directory (using –p option below) to store Ansible
   Playbooks and other artifacts under /storage (or other configured)
   file system.

   a. Includes VNF type using VNF function code 4 characters under
      /storage.

   b. Includes VNF “Version” directory as part of the path to store
      playbooks for this VNF version.

   c. Include generic ansible root directory. Creating full directory
      path as an example:

.. code-block:: none

     $ mkdir –p /storage/vfdb/V16.1/ansible**/**

3. Make this directory (VNF ansible root directory) current directory
   for next few steps:

.. code-block:: none

     cd /storage/vfdb/V16.1/ansible/

4. Extract Ansible Playbooks and other Ansible artifacts associated with
   the playbooks onto the ansible directory. Command depends on the type
   of file uploaded, examples would be:

.. code-block:: none

     tar xvf ..
     unzip …
     bunzip ..

5. Create VNF inventory hosts file with all VMs and
   OA&M IP addresses for all VNF instances with known OA&M IP addresses
   for respective VMs, example:

.. code-block:: none

    $ mkdir inventory

    $ touch inventory/vfdb9904vhosts

    $ cat inventory/vfdb9904vhosts

    [host]
    localhost ansible\_connection=local

    [oam]
    1xx.2yy.zzz.109
    1xx.2yy.zzz.110

    [rdb]
    1xx.2yy.zzz.105
    1xx.2yy.zzz.106

6. (Optional, being deprecated) Create directory to hold default
arguments for each VNF instance,
example:

.. code-block:: none

   $ mkdir –p vars/vfdb9904v
   $ touch vars/vfdb9904v/default\_args.yml
   $ cat vars/vfdb9904v/default\_args.yml
   vm\_config\_oam1\_vnfc\_name: vfdb9904vm001oam001
   vm\_config\_oam1\_hostname: vfdb9904vm001
   vm\_config\_oam1\_provider\_ip\_address: 1xx.2yy.zzz.109

   vm\_config\_oam2\_vnfc\_name: vfdb9904vm002oam001
   vm\_config\_oam2\_hostname: vfdb9904vm002
   vm\_config\_oam2\_provider\_ip\_address: 1xx.2yy.zzz.110

   vm\_config\_rdb1\_vnfc\_name: vfdb9904vm003rdb001
   vm\_config\_rdb1\_hostname: vfdb9904vm003
   vm\_config\_rdb1\_provider\_ip\_address: 1xx.2yy.zzz.105

   vm\_config\_rdb2\_vnfc\_name: vfdb9904vm004rdb001
   vm\_config\_rdb2\_hostname: vfdb9904vm004
   vm\_config\_rdb2\_provider\_ip\_address: 1xx.2yy.zzz.106

   vm\_config\_rdb3\_vnfc\_name: vfdb9904vm005rdb001
   vm\_config\_rdb3\_hostname: vfdb9904vm005
   vm\_config\_rdb3\_provider\_ip\_address: 1xx.2yy.zzz.xxx

   vm\_config\_rdb4\_vnfc\_name: vfdb9904vm006rdb001
   vm\_config\_rdb4\_hostname: vfdb9904vm006
   vm\_config\_rdb4\_provider\_ip\_address: 1xx.2yy.zzz.yyy

NOTE: Please note names in this file shall use underscore “\_” not dots
“.” or dashes “-“.

7. Perform some basic playbook validation running with “--check” option,
   running dummy playbooks or other.

NOTE: Each Ansible Server or cluster of Ansible Server will have its own
credentials to authenticate to VNF VMs. Ansible Server SSH public key(s)
have to be loaded onto VNF VMs during instantiation or other way before
Ansible Server can access VNF VMs and run playbooks. HOT templates used
by heat to instantiate VNFs to be configured by these Ansible Servers running
playbooks shall include the same SSH public key and load them onto VNF VM(s)
as part of instantiation.

Other non-vendor specific playbook tasks need to be incorporated in overall
post-instantiation configuration playbook. Alternative is for company
developed playbooks to be uploaded and executed, after VNF vendor provided
playbooks are run.

**A couple of playbooks used for proof-of-concept testing as examples:**

UpgradePreCheck:

.. code-block:: none

 $ pwd
 /storage/comx/V5.3.1.3/ansible/upgradeprecheck

 $ more site.yml
 ---

 - import_playbook: ../common/create_vars.yml
 - import_playbook: ../common/create_hosts.yml

 - name: upgrade software pre check
   hosts: oam,dbs,cpm
   gather_facts: no
   become: true
   become_method: sudo
   become_user: root
   max_fail_percentage: 0
   any_errors_fatal: True
   roles:
     - precheck
   tags: precheck

 $ more roles/precheck/tasks/main.yml
 ---

 - include_vars: /tmp/{{ vnf_instance }}/all.yml

 - name: get software version installed on vnf
   shell: grep "^SW_VERSION =" /vendor/software/config/param_common.cfg | grep -c "{{ existing_software_version }}"
   register: version_line
   ignore_errors: yes

 - name: send msg when matches expected version
   debug:  msg="*** OK *** VNF software release matches (old) release to be upgraded."
    verbosity=1
   when: version_line.stdout.find('1') != -1

 # send warning message and failure when release is not a match
 - fail:
     msg="*** WARNING *** VNF software release does not match expected (pre-upgrade) release."
   when: (version_line | failed) or version_line.stdout.find('1') == -1


UpgradePostCheck:

.. code-block:: none

 $ pwd
 /storage/comx/V5.3.1.3/ansible/upgradepostcheck

 $ more site.yml
 ---

 - import_playbook: ../common/create_vars.yml
 - import_playbook: ../common/create_hosts.yml

 - name: upgrade software post check
   hosts: oam,dbs,cpm
   gather_facts: no
   become: true
   become_method: sudo
   become_user: root
   max_fail_percentage: 0
   any_errors_fatal: True
   roles:
     - postcheck
   tags: postcheck

 $ more roles/postcheck/tasks/main.yml
 ---

 - include_vars: /tmp/{{ vnf_instance }}/all.yml

 - name: get post upgrade software version installed on vnf
   shell: grep "^SW_VERSION =" /vendor/software/config/param_common.cfg | grep -c "{{ new_software_version }}"
   register: version_line
   ignore_errors: yes

 - name: send msg when matches expected version
   debug:  msg="*** OK *** VNF software release matches new release."
     verbosity=1
   when: version_line.stdout.find('1') != -1

 # send warning message and failure when release is not a match
 - fail:
     msg="*** WARNING *** VNF software release does not match expected new (post-upgrade) release."
   when: (version_line | failed) or version_line.stdout.find('1') == -1


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


