**8. Appendix**
===============

a. Data Record Formats
======================

**Appendix A – Chef JSON Key Value Description**

The following provides the key value pairs that must be contained in the
JSON file supporting Chef action.

Table A1. Chef JSON File key value description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| **Field Name**    | **Description**                                                                                                                                                                                                                                                                                   | **Type**    | **Comment**                                                                                                                             |
+===================+===================================================================================================================================================================================================================================================================================================+=============+=========================================================================================================================================+
| Environment       | A JSON dictionary representing a Chef Environment object. If the VNF action requires loading or modifying Chef environment attributes associated with the VNF, all the relevant information must be provided in this JSON dictionary in a structure that conforms to a Chef Environment Object.   | Optional    | Depends on VNF action.                                                                                                                  |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Node              | A JSON dictionary representing a Chef Node Object.                                                                                                                                                                                                                                                | Mandatory   |                                                                                                                                         |
|                   |                                                                                                                                                                                                                                                                                                   |             |                                                                                                                                         |
|                   | The Node JSON dictionary must include the run list to be triggered for the desired VNF action by the push job. It should also include any attributes that need to be configured on the Node Object as part of the VNF action.                                                                     |             |                                                                                                                                         |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| NodeList          | Array of FQDNs that correspond to the endpoints (VMs) of a VNF registered with the Chef Server that need to trigger a chef-client run as part of the desired VNF action.                                                                                                                          | Mandatory   |                                                                                                                                         |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| PushJobFlag       | This field indicates whether the VNF action requires a push Job. Push job object will be created by ONAP if required.                                                                                                                                                                             | Mandatory   | If set to “True”, ONAP will request a push job. Ignored otherwise.                                                                      |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| CallbackCapable   | This field indicates if the chef-client run invoked by push job corresponding to the VNF action is capable of posting results on a callback URL.                                                                                                                                                  | Optional    | If Chef cookbook is callback capable, VNF owner is required to set it to “True”. Ignored otherwise.                                     |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| GetOutputFlag     | Flag which indicates whether ONAP should retrieve output generated in a chef-client run from Node object attribute node[‘PushJobOutput’] for this VNF action (e.g., in Audit).                                                                                                                    | Mandatory   | ONAP will retrieve output from NodeObject attributes [‘PushJobOutput’] for all nodes in NodeList if set to “True”. Ignored otherwise.   |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+

Chef Template example:

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

The example JSON file provided by the vendor for each VNF action will be
turned into a template by ONAP, that can be updated with instance
specific values at run-time.

Some points worth noting regarding the JSON fields:

a. The JSON file must be created for each action for each VNF.

b. If a VNF action involves multiple endpoints (VMs) of a VNF, ONAP will
   replicate the “Node” JSON dictionary in the template and post it to
   each FQDN (i.e., endpoint) in the NodeList after setting the “name”
   field in the Node object to be the respective FQDN [10]_. Hence, it
   is required that all end points (VMs) of a VNF involved in a VNF
   action support the same set of Node Object attributes.

The following table describes the JSON dictionary to post in Callback.

Table A2. JSON Dictionary to Post in Callback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------------------------------------------------+
| **Key**         | **Description**                                                                                                                                                                                           | **Type**    | **Comment**                                                 |
+=================+===========================================================================================================================================================================================================+=============+=============================================================+
| RequestId       | A unique string associated with the original request by ONAP. This key-value pair will be provided by ONAP in the environment of the push job request and must be returned as part of the POST message.   | Mandatory   |                                                             |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------------------------------------------------+
| StatusCode      | An integer that must be set to                                                                                                                                                                            | Mandatory   |                                                             |
|                 |                                                                                                                                                                                                           |             |                                                             |
|                 | 200 if chef-client run on the node finished successfully                                                                                                                                                  |             |                                                             |
|                 |                                                                                                                                                                                                           |             |                                                             |
|                 | 500 otherwise.                                                                                                                                                                                            |             |                                                             |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------------------------------------------------+
| StatusMessage   | A string which must be set to                                                                                                                                                                             | Mandatory   |                                                             |
|                 |                                                                                                                                                                                                           |             |                                                             |
|                 | ‘SUCCESS’ if StatusCode was 200                                                                                                                                                                           |             |                                                             |
|                 |                                                                                                                                                                                                           |             |                                                             |
|                 | Appropriate error message otherwise.                                                                                                                                                                      |             |                                                             |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------------------------------------------------+
| Name            | A string which corresponds to the name of the node where push job is run. It is required that the value be retrieved from the node object attributes (where it is always defined).                        | Mandatory   |                                                             |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------------------------------------------------+
| PushJobOutput   | Any output from the chef-client run that needs to be returned to ONAP.                                                                                                                                    | Optional    | Depends on VNF action. If empty, it must not be included.   |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+-------------------------------------------------------------+


**Appendix B – Ansible JSON Key Value Description**

The following provides the key value pairs that must be contained in the
JSON file supporting Ansible action.

Table B1. Ansible JSON File key value description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+
| **Field Name**   | **Description**                                                                                                                                                                                                                                                                            | **Type**    | **Comment**                                                         |
+==================+============================================================================================================================================================================================================================================================================================+=============+=====================================================================+
| PlaybookName     | VNF Vendor must list name of the playbook used to execute the VNF action.                                                                                                                                                                                                                  | Mandatory   |                                                                     |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+
| Action           | Name of VNF action.                                                                                                                                                                                                                                                                        | Optional    |                                                                     |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+
| EnvParameters    | A JSON dictionary which should list key value pairs to be passed to the Ansible playbook. These values would correspond to instance specific parameters that a playbook may need to execute an action.                                                                                     | Optional    | Depends on the VNF action.                                          |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+
| NodeList         | A JSON array of FQDNs that the playbook must be executed on.                                                                                                                                                                                                                               | Optional    | If not provided, playbook will be executed on the Ansible Server.   |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+
| FileParameters   | A JSON dictionary where keys are filenames and values are contents of files. The Ansible Server will utilize this feature to generate files with keys as filenames and values as content. This attribute can be used to generate files that a playbook may require as part of execution.   | Optional    | Depends on the VNF action and playbook design.                      |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+
| Timeout          | Time (in seconds) that a playbook is expected to take to finish execution for the VNF. If playbook execution time exceeds this value, Ansible Server will terminate the playbook process.                                                                                                  | Optional    |                                                                     |
+------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+---------------------------------------------------------------------+

Ansible JSON file example:

{

      “Action”:”Configure”,

      "PlaybookName": "Ansible\_configure.yml",

      "NodeList": ["test1.vnf\_b.onap.com", “test2.vnf\_b.onap.com”],

      "Timeout": 60,

      "EnvParameters": {"Retry": 3, "Wait": 5, “ConfigFile”:”config.txt”},

      “FileParameters”:{“config.txt”:”db\_ip=10.1.1.1, sip\_timer=10000”}

}

In the above example, the Ansible Server will:

a. Process the “FileParameters” dictionary and generate a file named
   ‘config.txt’ with contents set to the value of the ‘config.txt’ key.

b. Execute the playbook named ‘Ansible\_configure.yml’ on nodes with
   FQDNs test1.vnf\_b.onap.com and test2.vnf\_b.onap.com respectively
   while providing the following key value pairs to the playbook:
   Retry=3, Wait=5, ConfigFile=config.txt

c. If execution time of the playbook exceeds 60 secs (across all hosts),
   it will be terminated.

**Appendix C – VNF License Information Guidelines**

This Appendix describes the metadata to be supplied for VNF licenses.

1. General Information

Table C1 defines the required and optional fields for licenses.

Table C1. Required Fields for General Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| **Field Name**                 | **Description**                                                                                                                                                                                                                                                                                           | **Data Type**     | **Type**    |
+================================+===========================================================================================================================================================================================================================================================================================================+===================+=============+
| Vendor Name                    | The name of the vendor.                                                                                                                                                                                                                                                                                   | String            | Mandatory   |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| Vendor Product                 | The name of the product to which this agreement applies.                                                                                                                                                                                                                                                  | String            | Mandatory   |
|                                |                                                                                                                                                                                                                                                                                                           |                   |             |
|                                | Note: a contract/agreement may apply to more than one vendor product. In that case, provide the metadata for each product separately.                                                                                                                                                                     |                   |             |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| Vendor Product Description     | A general description of vendor software product.                                                                                                                                                                                                                                                         | String            | Optional    |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| Export Control                 | ECCNs are 5-character alpha-numeric designations used on the Commerce Control List (CCL) to identify dual-use items for export control purposes. An ECCN categorizes items based on the nature of the product, i.e. type of commodity, software, or technology and its respective technical parameters.   | String            | Mandatory   |
|                                |                                                                                                                                                                                                                                                                                                           |                   |             |
| Classification Number (ECCN)   |                                                                                                                                                                                                                                                                                                           |                   |             |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+
| Reporting Requirements         | A list of any reporting requirements on the usage of the software product.                                                                                                                                                                                                                                | List of strings   | Optional    |
+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+-------------+

1. Entitlements

Entitlements describe software license use rights. The use rights may be
quantified by various metrics: # users, # software instances, # units.
The use rights may be limited by various criteria: location (physical or
logical), type of customer, type of device, time, etc.

One or more entitlements can be defined; each one consists of the
following fields:

Table C2. Required Fields for Entitlements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| **Field Name**                                      | **Description**                                                                                                                                                                       | **Data Type**     | **Type**      |
+=====================================================+=======================================================================================================================================================================================+===================+===============+
| Vendor Part Number / Manufacture Reference Number   | Identifier for the entitlement as described by the vendor in their price list / catalog / contract.                                                                                   | String            | Mandatory     |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| Description                                         | Verbiage that describes the entitlement.                                                                                                                                              | String            | Optional      |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| Entitlement Identifier                              | Each entitlement defined must be identified by a unique value (e.g., numbered 1, 2, 3….)                                                                                              | String            | Mandatory     |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| Minimum Order Requirement                           | The minimum number of entitlements that need to be purchased. For example, the entitlements must be purchased in a block of 100. If no minimum is required, the value will be zero.   | Number            | Mandatory     |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| Unique Reporting Requirements                       | A list of any reporting requirements on the usage of the software product. (e.g.: quarterly usage reports are required)                                                               | List of Strings   | Optional      |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| License Type                                        | Type of license applicable to the software product. (e.g.: fixed-term, perpetual, trial, subscription.)                                                                               | String            | Mandatory     |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| License Duration                                    | Valid values:                                                                                                                                                                         | String            | Conditional   |
|                                                     |                                                                                                                                                                                       |                   |               |
|                                                     | **year**, **quarter**, **month**, **day**.                                                                                                                                            |                   |               |
|                                                     |                                                                                                                                                                                       |                   |               |
|                                                     | Not applicable when license type is Perpetual.                                                                                                                                        |                   |               |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| License Duration Quantification                     | Number of years, quarters, months, or days for which the license is valid.                                                                                                            | Number            | Conditional   |
|                                                     |                                                                                                                                                                                       |                   |               |
|                                                     | Not applicable when license type is Perpetual.                                                                                                                                        |                   |               |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+
| Limits                                              | see section C.4 for possible values                                                                                                                                                   | List              | Optional      |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+---------------+

1. License Keys

This section defines information on any License Keys associated with the
Software Product. A license key is a data string (or a file) providing a
means to authorize the use of software. License key does not provide
entitlement information.

License Keys are not required. Optionally, one or more license keys can
be defined; each one consists of the following fields:

Table C3. Required Fields for License Keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------+---------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| **Field Name**           | **Description**                                                                                               | **Data Type**   | **Type**    |
+==========================+===============================================================================================================+=================+=============+
| Description              | Verbiage that describes the license key                                                                       | String          | Mandatory   |
+--------------------------+---------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| License Key Identifier   | Each license key defined must be identified by a unique value (e.g., numbered 1, 2, 3….)                      | String          | Mandatory   |
+--------------------------+---------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Key Function             | Lifecycle stage (e.g., Instantiation or Activation) at which the license key is applied to the software.      | String          | Optional    |
+--------------------------+---------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| License Key Type         | Valid values:                                                                                                 | String          | Mandatory   |
|                          |                                                                                                               |                 |             |
|                          | **Universal, Unique**                                                                                         |                 |             |
|                          |                                                                                                               |                 |             |
|                          | **Universal** - a single license key value that may be used with any number of instances of the software.     |                 |             |
|                          |                                                                                                               |                 |             |
|                          | **Unique**- a unique license key value is required for each instance of the software.                         |                 |             |
+--------------------------+---------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Limits                   | see section C.4 for possible values                                                                           | List            | Optional    |
+--------------------------+---------------------------------------------------------------------------------------------------------------+-----------------+-------------+

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| **Field Name**         | **Description**                                                                                                     | **Data Type**    | **Type**    |
+========================+=====================================================================================================================+==================+=============+
| Limit Identifier       | Each limit defined for an entitlement or license key must be identified by a unique value (e.g., numbered 1,2,3…)   | String           | Mandatory   |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Description      | Verbiage describing the limit.                                                                                      | String           | Mandatory   |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Behavior         | Description of the actions taken when the limit boundaries are reached.                                             | String           | Mandatory   |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Category         | Valid value: **location**                                                                                           | String           | Mandatory   |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Type             | Valid values: **city, county, state, country, region, MSA, BTA, CLLI**                                              | String           | Mandatory   |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit List             | List of locations where the Vendor Product can be used or needs to be restricted from use                           | List of String   | Mandatory   |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Set Type         | Indicates if the list is an inclusion or exclusion.                                                                 | String           | Mandatory   |
|                        |                                                                                                                     |                  |             |
|                        | Valid Values:                                                                                                       |                  |             |
|                        |                                                                                                                     |                  |             |
|                        | **Allowed**                                                                                                         |                  |             |
|                        |                                                                                                                     |                  |             |
|                        | **Not allowed**                                                                                                     |                  |             |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Quantification   | The quantity (amount) the limit expresses.                                                                          | Number           | Optional    |
+------------------------+---------------------------------------------------------------------------------------------------------------------+------------------+-------------+

1. Time

Limit on the length of time the software may be used. For example:

-  license key valid for 1 year from activation

-  entitlement valid from 15 May 2018 thru 30 June 2020

Table C5. Required Fields for Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| **Field Name**         | **Description**                                                                                                               | **Data Type**    | **Type**      |
+========================+===============================================================================================================================+==================+===============+
| Limit Identifier       | Each limit defined for an entitlement or license key must be identified by a unique value (e.g., numbered)                    | String           | Mandatory     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Limit Description      | Verbiage describing the limit.                                                                                                | String           | Mandatory     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Limit Behavior         | Description of the actions taken when the limit boundaries are reached.                                                       | String           | Mandatory     |
|                        |                                                                                                                               |                  |               |
|                        | The limit behavior may also describe when a time limit takes effect. (e.g., key is valid for 1 year from date of purchase).   |                  |               |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Limit Category         | Valid value: **time**                                                                                                         | String           | Mandatory     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Limit Type             | Valid values: **duration, date**                                                                                              | String           | Mandatory     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Limit List             | List of times for which the Vendor Product can be used or needs to be restricted from use                                     | List of String   | Mandatory     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Duration Units         | Required when limit type is duration. Valid values: **perpetual, year, quarter, month, day, minute, second, millisecond**     | String           | Conditional   |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Limit Quantification   | The quantity (amount) the limit expresses.                                                                                    | Number           | Optional      |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| Start Date             | Required when limit type is date.                                                                                             | Date             | Optional      |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| End Date               | May be used when limit type is date.                                                                                          | Date             | Optional      |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+

1. Usage

Limits based on how the software is used. For example:

-  use is limited to a specific sub-set of the features/capabilities the
   software supports

-  use is limited to a certain environment (e.g., test, development,
   production…)

-  use is limited by processor (vm, cpu, core)

-  use is limited by software release

Table C6. Required Fields for Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| **Field Name**         | **Description**                                                                                              | **Data Type**    | **Type**    |
+========================+==============================================================================================================+==================+=============+
| Limit Identifier       | Each limit defined for an entitlement or license key must be identified by a unique value (e.g., numbered)   | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Description      | Verbiage describing the limit.                                                                               | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Behavior         | Description of the actions taken when the limit boundaries are reached.                                      | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Category         | Valid value: **usages**                                                                                      | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Type             | Valid values: **feature, environment, processor, version**                                                   | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit List             | List of usage limits (e.g., test, development, vm, core, R1.2.1, R1.3.5…)                                    | List of String   | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Set Type         | Indicates if the list is an inclusion or exclusion.                                                          | String           | Mandatory   |
|                        |                                                                                                              |                  |             |
|                        | Valid Values:                                                                                                |                  |             |
|                        |                                                                                                              |                  |             |
|                        | **Allowed**                                                                                                  |                  |             |
|                        |                                                                                                              |                  |             |
|                        | **Not allowed**                                                                                              |                  |             |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Quantification   | The quantity (amount) the limit expresses.                                                                   | Number           | Optional    |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+

1. Entity

Limit on the entity (product line, organization, customer) allowed to
make use of the software. For example:

-  allowed to be used in support of wireless products

-  allowed to be used only for government entities

Table C7. Required Fields for Entity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| **Field Name**         | **Description**                                                                                              | **Data Type**    | **Type**    |
+========================+==============================================================================================================+==================+=============+
| Limit Identifier       | Each limit defined for an entitlement or license key must be identified by a unique value (e.g., numbered)   | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Description      | Verbiage describing the limit.                                                                               | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Behavior         | Description of the actions taken when the limit boundaries are reached.                                      | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Category         | Valid value: **entity**                                                                                      | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Type             | Valid values: **product line, organization, internal customer, external customer**                           | String           | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit List             | List of entities for which the Vendor Product can be used or needs to be restricted from use                 | List of String   | Mandatory   |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Set Type         | Indicates if the list is an inclusion or exclusion.                                                          | String           | Mandatory   |
|                        |                                                                                                              |                  |             |
|                        | Valid Values:                                                                                                |                  |             |
|                        |                                                                                                              |                  |             |
|                        | **Allowed**                                                                                                  |                  |             |
|                        |                                                                                                              |                  |             |
|                        | **Not allowed**                                                                                              |                  |             |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+
| Limit Quantification   | The quantity (amount) the limit expresses.                                                                   | Number           | Optional    |
+------------------------+--------------------------------------------------------------------------------------------------------------+------------------+-------------+

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| **Field Name**         | **Description**                                                                                                                                                                                                                                                | **Data Type**   | **Type**    |
+========================+================================================================================================================================================================================================================================================================+=================+=============+
| Limit Identifier       | Each limit defined for an entitlement or license key must be identified by a unique value (e.g., numbered)                                                                                                                                                     | String          | Mandatory   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Limit Description      | Verbiage describing the limit.                                                                                                                                                                                                                                 | String          | Mandatory   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Limit Behavior         | Description of the actions taken when the limit boundaries are reached.                                                                                                                                                                                        | String          | Mandatory   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Limit Category         | Valid value: **amount**                                                                                                                                                                                                                                        | String          | Mandatory   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Limit Type             | Valid values: **trunk, user, subscriber, session, token, transactions, seats, KB, MB, TB, GB**                                                                                                                                                                 | String          | Mandatory   |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Type of Utilization    | Is the limit relative to utilization of the functions of the software or relative to utilization of other resources?                                                                                                                                           | String          | Mandatory   |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | Valid values:                                                                                                                                                                                                                                                  |                 |             |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | -  **software functions**                                                                                                                                                                                                                                      |                 |             |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | -  **other resources**                                                                                                                                                                                                                                         |                 |             |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Limit Quantification   | The quantity (amount) the limit expresses.                                                                                                                                                                                                                     | Number          | Optional    |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Aggregation Function   | Valid values: **peak, average**                                                                                                                                                                                                                                | String          | Optional    |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Aggregation Interval   | Time period over which the aggregation is done (e.g., average sessions per quarter). Required when an Aggregation Function is specified.                                                                                                                       | String          | Optional    |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | Valid values: **day, month, quarter, year, minute, second, millisecond**                                                                                                                                                                                       |                 |             |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Aggregation Scope      | Is the limit quantity applicable to a single entitlement or license key (each separately)? Or may the limit quantity be combined with others of the same type (resulting in limit amount that is the sum of all the purchased entitlements or license keys)?   | String          | Optional    |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | Valid values:                                                                                                                                                                                                                                                  |                 |             |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | -  **single**                                                                                                                                                                                                                                                  |                 |             |
|                        |                                                                                                                                                                                                                                                                |                 |             |
|                        | -  **combined**                                                                                                                                                                                                                                                |                 |             |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+
| Type of User           | Describes the types of users of the functionality offered by the software (e.g., authorized, named). This field is included when Limit Type is user.                                                                                                           | String          | Optional    |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------+


**Appendix D – Ansible Server Specification**

This section outlines the specifications for an ONAP compliant Ansible
Server that can optionally be provided by the VNF Vendor. The Ansible
Server will be used as a repository to store Ansible playbooks as well
as an execution engine which upon a REST API request, will execute
Ansible playbook against VNFs.

Table D1. Ansible Server Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
| **Principle**                                | **Description**                                                                                                                                                                                                                                                                                                                                                              | **Type**   | **ID #**   |
+==============================================+==============================================================================================================================================================================================================================================================================================================================================================================+============+============+
| Ansible Server Scope                         |     The Ansible Server is required to support storage and execution of playbooks that are in yaml format or a collection of playbooks compressed and uploaded in tar-ball format.                                                                                                                                                                                            | Must       | D1000      |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
|                                              |     The Ansible Server must accept requests for execution of playbooks via a REST interface. The scope of each request will involve exactly one action and will request execution of one playbook.                                                                                                                                                                           | Must       | D1010      |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
|                                              |     The playbook executed by the Ansible Server will be responsible for execution of the entire action against the VNF (e.g., calling other playbooks, running tasks on multiple VMs in the VNF) and return back the status of the action as well as any necessary output in its entirety after the action is finished.                                                      | Must       | D1020      |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
|                                              |     The Ansible Server must support simultaneous execution of multiple playbooks against different VNFs in parallel (i.e., process multiple requests).                                                                                                                                                                                                                       | Must       | D1030      |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
|                                              | The Ansible Server will be loaded with all necessary credentials to invoke playbooks against target VNF(s).                                                                                                                                                                                                                                                                  | Must       | D1040      |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
| Ansible Server/ONAP Interface                | Load Playbook\ **:** The Ansible Server must expose an authenticated interface to allow loading all necessary playbooks for a target VNF. It should impose an identification mechanism that allows each playbook to be uniquely identified.                                                                                                                                  | Must       | D1050      |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  It is recommended that the load Playbook API be a REST API.                                                                                                                                                                                                                                                                                                               |            |            |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
|                                              | Request API: The Ansible Server must expose a REST endpoint that accepts a POST message to request execution of the playbook. The POST request must be a JSON block as outlined in Table D2.                                                                                                                                                                                 | Must       | D1060      |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
|                                              | When the Ansible server accepts an authenticated request to execute a playbook, it is required to send back an initial response indicating whether the request is accepted or rejected. The response must be a JSON Object with the key value pairs as described in Table D3.                                                                                                | Must       | D1070      |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
|                                              | Result API: If the Ansible Server accepts a request to execute a playbook, it must make available status of the execution of the playbook at a Results REST endpoint indexed by the Id in the request in the form <url>?Id=<RequestId>&Type=GetResult where <url> is the URL used for submitting requests.                                                                   | Must       | D1080      |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
|                                              | When a GET is invoked against the Results REST endpoint, the Ansible Server must reply with an appropriate response:                                                                                                                                                                                                                                                         | Must       | D1090      |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  If the Endpoint is invalid (no request, or request expired), reply with a standard HTTP 404 error.                                                                                                                                                                                                                                                                        |            |            |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  If the playbook execution is still ongoing, then the Ansible Server is required to block on the GET request till the execution finishes or terminates.                                                                                                                                                                                                                    |            |            |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  Upon completion of execution, the Ansible Server is required to respond to the GET request with the result of the playbook execution in the form of a JSON message as outlined in the Table D4.                                                                                                                                                                           |            |            |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
|                                              | The dictionary associated with the ‘Results’ key in the Result Response must be a key-value pair where each key corresponds to an entry in the NodeList and the value is a dictionary with the format as outlined in Table D5.                                                                                                                                               | Must       | D1100      |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
| Ansible Server Actions                       | The Ansible Server must take the following actions when triggered by a request to execute a playbook:                                                                                                                                                                                                                                                                        | Must       | D1110      |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  Determine if the request is valid, and if so, must send back an initial response message accepting the request.                                                                                                                                                                                                                                                           |            |            |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  If the request contains a “FileParameters” key that is not NULL, create all the necessary files.                                                                                                                                                                                                                                                                          |            |            |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  Invoke the ansible playbook while providing it all appropriate parameters listed in EnvParameters and inventory information listed in NodeList. The playbook will be responsible for execution of all necessary steps required by the VNF action.                                                                                                                         |            |            |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  If the playbook finishes, use the PLAY\_RECAP functionality to determine whether playbook finished successfully on each endpoint identified in the NodeList.                                                                                                                                                                                                              |            |            |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  If the playbook finishes, collect any output returned by the playbook. A playbook conforming to the ONAP vendor requirements document will write out any necessary output to a file named ‘<hostname>\_results.txt’ in the working directory, where ‘hostname’ is an element of the NodeList where the playbook is being executed.                                        |            |            |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  If the playbook execution exceeds the Timeout value, the playbook execution process is terminated and ansible log that captures the last task executed is stored.                                                                                                                                                                                                         |            |            |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  Make results available on the Results REST Endpoint as documented in Table D3.                                                                                                                                                                                                                                                                                            |            |            |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  If Callback url was provided in initial request, post the final response message on the Callback URL along with an additional key additional key “Id “: which corresponds to the request Id sent in the request.                                                                                                                                                          |            |            |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
| Ansible Server Result Storage Requirements   | The Ansible Server must cache and provide results of an execution as well as retain logs for debugging purposes as outlined below:                                                                                                                                                                                                                                           | Must       | D1120      |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  The results from a playbook execution result must be retained by the Ansible Server and made available through the respective REST endpoint for a duration that is configurable.                                                                                                                                                                                          |            |            |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              |    -  Recommended duration is 2 x Timeout.                                                                                                                                                                                                                                                                                                                                   |            |            |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  The log from a playbook must be stored by the Ansible Server, tagged with the Id along with all other parameters in the initial request in a format that allows for examination for debugging purposes.                                                                                                                                                                   |            |            |
|                                              |                                                                                                                                                                                                                                                                                                                                                                              |            |            |
|                                              | -  The results from playbook execution and log files shall be removed after a configurable defined retention period for this type of file.                                                                                                                                                                                                                                   |            |            |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
| Ansible Server Locking Mechanism             | The Ansible Server shall lock VNF while running playbooks that require exclusive use of a VNF (Configure is an example) and not accept requests to run other playbooks or queue those requests until playbook that requires exclusivity completes                                                                                                                            | Must       | D1130      |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+

Table D2. Request Message
~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| **Key**           | **Description**                                                                                                                                                                                                                                                                                                                                         | **Type**    | **Comment**                                                                                                                        |
+===================+=========================================================================================================================================================================================================================================================================================================================================================+=============+====================================================================================================================================+
| Id                | A unique string that identifies this request. For e.g., a UUID                                                                                                                                                                                                                                                                                          | Mandatory   | NOT NULL                                                                                                                           |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| PlaybookName      | A string which contains the name of the playbook to execute.                                                                                                                                                                                                                                                                                            | Mandatory   | NOT NULL                                                                                                                           |
|                   |                                                                                                                                                                                                                                                                                                                                                         |             |                                                                                                                                    |
|                   | Example: memthres.yaml                                                                                                                                                                                                                                                                                                                                  |             |                                                                                                                                    |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| Action            | Name of action                                                                                                                                                                                                                                                                                                                                          | Optional    |                                                                                                                                    |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| NodeList          | List of endpoints of the VNF against which the playbook should be executed.                                                                                                                                                                                                                                                                             | Optional    | If not specified, playbook executed within Ansible Server (localhost)                                                              |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| Timeout           | Time the Ansible Server should wait (in seconds), before terminating playbook execution. The Ansible Server will apply the timeout for the entire playbook execution (i.e., independent of number of endpoints against which the playbook is executing). If playbook execution time exceeds the timeout value, the server will terminate the process.   | Optional    | If not specified, Ansible server will use internal default value (configurable)                                                    |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| LocalParameters   | A JSON dictionary that can be used to provide key value pairs that are specific to each individual VNF/VM instance. Key must be endpoint FQDN and value a JSON dictionary with key-value pairs for the playbook run associated with that host/group.                                                                                                    | Optional    |                                                                                                                                    |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| EnvParameters     | A JSON dictionary that can be used to specify key value pairs passed at run time to the playbook that are common across all hosts against which the playbook will run.                                                                                                                                                                                  | Optional    |                                                                                                                                    |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| CallbackUrl       | A callback URL that Ansible Server can POST results to once playbook finishes execution or is terminated.                                                                                                                                                                                                                                               | Optional    | If present, Ansible Server is required to POST response back on the Callback URL                                                   |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| FileParameters    | A dictionary where keys correspond to file names to be generated and values correspond to contents of files.                                                                                                                                                                                                                                            | Optional    | If present, Ansible Server will first process this and write out contents to appropriate files and then process other parameters   |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+

Table D3. Initial Response Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+------------------------------------------------------------------------------------------+-------------+---------------+
| **Key**            | **Description**                                                                          | **Type**    | **Comment**   |
+====================+==========================================================================================+=============+===============+
| StatusCode         | An integer indicating status of the request. It MUST take one of the following values:   | Mandatory   |               |
|                    |                                                                                          |             |               |
|                    | 100 if request is accepted                                                               |             |               |
|                    |                                                                                          |             |               |
|                    | 101 if request is rejected                                                               |             |               |
+--------------------+------------------------------------------------------------------------------------------+-------------+---------------+
| StatusMessage      | A string describing Server’s response                                                    | Mandatory   |               |
|                    |                                                                                          |             |               |
|                    | It MUST be set to ‘PENDING’ if StatusCode=100                                            |             |               |
|                    |                                                                                          |             |               |
|                    | It MUST be set to appropriate error exception message if StatusCode=101                  |             |               |
+--------------------+------------------------------------------------------------------------------------------+-------------+---------------+
| ExpectedDuration   | Time the server expects (in seconds) to finish the playbook execution.                   | Optional    |               |
+--------------------+------------------------------------------------------------------------------------------+-------------+---------------+

Table D4. Final Response Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+-------------------------------------------------------------------------------------------------------+-------------+------------------------+
| **Key**         | **Description**                                                                                       | **Type**    | **Comment**            |
+=================+=======================================================================================================+=============+========================+
| StatusCode      | 200 if Execution finished normally                                                                    | Mandatory   |                        |
|                 |                                                                                                       |             |                        |
|                 | 500 otherwise.                                                                                        |             |                        |
+-----------------+-------------------------------------------------------------------------------------------------------+-------------+------------------------+
| StatusMessage   | A string which be set to either of the TWO values:                                                    | Mandatory   |                        |
|                 |                                                                                                       |             |                        |
|                 | -  ‘FINISHED’ if StatusCode=200                                                                       |             |                        |
|                 |                                                                                                       |             |                        |
|                 | -  Appropriate error exception message if StatusCode=500                                              |             |                        |
+-----------------+-------------------------------------------------------------------------------------------------------+-------------+------------------------+
| Duration        | Time it took for execution to finish (in seconds).                                                    | Optional    |                        |
+-----------------+-------------------------------------------------------------------------------------------------------+-------------+------------------------+
| Result          | A JSON dictionary that lists the status of playbook execution for each VM (or VNF) in the NodeList.   | Optional    | Not present if empty   |
+-----------------+-------------------------------------------------------------------------------------------------------+-------------+------------------------+

Table D5. Result Block Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------+----------------------------------------------------------+-------------+------------------------+
| **Key**         | **Description**                                          | **Type**    | **Comment**            |
+=================+==========================================================+=============+========================+
| GroupName       | Group under which the VM (or VNF) falls in a playbook.   | Optional    |                        |
+-----------------+----------------------------------------------------------+-------------+------------------------+
| StatusCode      | A string which must have the following values:           | Mandatory   |                        |
|                 |                                                          |             |                        |
|                 | -  200 if SUCCESS                                        |             |                        |
|                 |                                                          |             |                        |
|                 | -  500 otherwise                                         |             |                        |
+-----------------+----------------------------------------------------------+-------------+------------------------+
| StatusMessage   | An integer with the following values:                    | Mandatory   |                        |
|                 |                                                          |             |                        |
|                 | -  ‘SUCCESS’ if StatusCode=200                           |             |                        |
|                 |                                                          |             |                        |
|                 | -  Error exception message otherwise                     |             |                        |
+-----------------+----------------------------------------------------------+-------------+------------------------+
| Output          | Any output the playbook is required to return.           | Optional    | Not present if empty   |
+-----------------+----------------------------------------------------------+-------------+------------------------+

Some illustrative examples are shown below:

1. An example POST for requesting execution of a Playbook :

   {"Id": "10", “Action”:”HealthCheck”, "PlaybookName":
   "ansible\_getresource.yml", "NodeList":
   ["interface1.vnf\_b.onap.com", ["interface2.vnf\_b.onap.com"],
   "Timeout": 60, "EnvParameters": {"Retry": 3, "Wait": 5}}

2. Potential examples of Ansible Server initial response.

   a. Successfully accepted request: {"StatusCode": "100",
      "ExpectedDuration": "60sec", "StatusMessage": "PENDING"}

   b. Request rejected: {"StatusCode": "101", "StatusMessage": "PLAYBOOK
      NOT FOUND "}

3. Potential examples of final response by Ansible Server to a GET on

   a. Playbook successful execution: {"Duration": "4.864815sec",
      “StatusCode”: 200, “StatusMessage”:”FINISHED”, "Results":
      {"interface\_1.vnf\_b.onap.com": {"StatusCode": "200",
      "GroupName": "vnf-x-oam", "StatusMessage": "SUCCESS",
      “Output”:{“CPU”:30, “Memory”:”5Gb”},
      "interface\_1.vnf\_b.onap.com": {"StatusCode": "200", "GroupName":
      "vnf-x-oam", "StatusMessage": "SUCCESS", “Output”:{“CPU”:60,
      “Memory”:”10Gb”}}}

   b. Playbook failed execution on one of the hosts: {"Duration":
      "10.8sec", “StatusCode”: 200, “StatusMessage”:”FINISHED”,
      "Results": {"interface\_1.vnf\_b.onap.com": {"StatusCode": "500",
      "GroupName": "vnf-x-oam", "StatusMessage": "Error executing
      command ", "interface\_1.vnf\_b.onap.com": {"StatusCode": "200",
      "GroupName": "vnf-x-oam", "StatusMessage": "SUCCESS",
      “Output”:{“CPU”:60, “Memory”:”10Gb”}}}

   c. Playbook terminated: {"Duration": "61 sec", “StatusCode”: 500,
      “StatusMessage”:”TERMINATED” }

b. Requirement List
===================

R-11200: The VNF MUST keep the scope of a Cinder volume module, when it exists, to be 1:1 with the VNF Base Module or Incremental Module.

R-01334: The VNF **MUST** conform to the NETCONF RFC 5717, “Partial Lock Remote Procedure Call”.

R-51910: The VNF **MUST** provide all telemetry (e.g., fault event records, syslog records, performance records etc.) to ONAP using the model, format and mechanisms described in this section.

R-29324: The VNF **SHOULD** implement the protocol operation: **copy-config(target, source) -** Copy the content of the configuration datastore source to the configuration datastore target.

R-72184: The VNF **MUST** have routable FQDNs for all the endpoints (VMs) of a VNF that contain chef-clients which are used to register with the Chef Server.  As part of invoking VNF actions, ONAP will trigger push jobs against FQDNs of endpoints for a VNF, if required.

R-23740: The VNF **MUST** accommodate the security principle of “least privilege” during development, implementation and operation. The importance of “least privilege” cannot be overstated and must be observed in all aspects of VNF development and not limited to security. This is applicable to all sections of this document.

R-12709: The VNFC **SHOULD** be independently deployed, configured, upgraded, scaled, monitored, and administered by ONAP.

R-88031: The VNF **SHOULD** implement the protocol operation: **delete-config(target) -** Delete the named configuration datastore target.

R-42207: The VNF **MUST** design resiliency into a VNF such that the resiliency deployment model (e.g., active-active) can be chosen at run-time.

R-98617: The VNF Vendor **MUST** provide information regarding any dependency (e.g., affinity, anti-affinity) with other VNFs and resources.

R-62498: The VNF **MUST**, if not using the NCSP’s IDAM API, encrypt OA&M access (e.g., SSH, SFTP).

R-42366: The VNF **MUST** support secure connections and transports.

R-33955: The VNF **SHOULD** conform its YANG model to \*\*RFC 6991, “Common YANG Data Types”.

R-33488: The VNF **MUST** protect against all denial of service attacks, both volumetric and non-volumetric, or integrate with external denial of service protection tools.

R-57617: The VNF **MUST** include the field “success/failure” in the Security alarms (where applicable and technically feasible).

R-57271: The VNF **MUST** provide the capability of generating security audit logs by interacting with the operating system (OS) as appropriate.

R-44569: The VNF Vendor **MUST NOT** require additional infrastructure such as a vendor license server for Vendor functions and metrics..

R-67918: The VNF **MUST** handle replication race conditions both locally and geo-located in the event of a data base instance failure to maintain service continuity.

R-35532: The VNF **SHOULD** release and clear all shared assets (memory, database operations, connections, locks, etc.) as soon as possible, especially before long running sync and asynchronous operations, so as to not prevent use of these assets by other entities.

R-37692: The VNFC **MUST** provide API versioning to allow for independent upgrades of VNFC.

R-50252: The VNF **MUST** write to a specific set of text files that will be retrieved and made available by the Ansible Server If, as part of a VNF action (e.g., audit), a playbook is required to return any VNF information.

R-58977: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Eavesdropping.

R-59391: The VNF vendor **MUST**, where a VNF vendor requires the assumption of permissions, such as root or administrator, first log in under their individual user login ID then switch to the other higher level account; or where the individual user login is infeasible, must login with an account with admin privileges in a way that uniquely identifies the individual performing the function.

R-93443: The VNF **MUST** define all data models in YANG [RFC6020], and the mapping to NETCONF shall follow the rules defined in this RFC.

R-72243: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Phishing / SMishing.

R-33280: The VNF **MUST NOT** use any instance specific parameters in a playbook.

R-73468: The VNF **MUST** allow the NETCONF server connection parameters to be configurable during virtual machine instantiation through Heat templates where SSH keys, usernames, passwords, SSH service and SSH port numbers are Heat template parameters.

R-46908: The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "password complexity" policy. When passwords are used, they shall be complex and shall at least meet the following password construction requirements: (1) be a minimum configurable number of characters in length, (2) include 3 of the 4 following types of characters: upper-case alphabetic, lower-case alphabetic, numeric, and special, (3) not be the same as the UserID with which they are associated or other common strings as specified by the environment, (4) not contain repeating or sequential characters or numbers, (5) not to use special characters that may have command functions, and (6) new passwords must not contain sequences of three or more characters from the previous password.

R-86261: The VNF **MUST NOT** allow vendor access to VNFs remotely.

R-75343: The VNF **MUST** provide the capability of testing the validity of a digital certificate by recognizing the identity represented by the certificate — the "distinguished name".

R-40813: The VNF **SHOULD** support the use of virtual trusted platform module, hypervisor security testing and standards scanning tools.

R-02454: The VNF **MUST** support the existence of multiple major/minor versions of the VNF software and/or sub-components and interfaces that support both forward and backward compatibility to be transparent to the Service Provider usage.

R-20353: The VNF **MUST** implement at least one of the capabilities **:candidate** or **:writable-running**. If both **:candidate** and **:writable-running** are provided then two locks should be supported.

R-01556: The VNF Package **MUST** include documentation describing the fault, performance, capacity events/alarms and other event records that are made available by the VNF. The document must include:

R-56815: The VNF Package **MUST** include documentation describing supported VNF scaling capabilities and capacity limits (e.g., number of users, bandwidth, throughput, concurrent calls).

R-56793: The VNF **MUST** test for adherence to the defined performance budgets at each layer, during each delivery cycle with delivered results, so that the performance budget is measured and the code is adjusted to meet performance budget.

R-54520: The VNF **MUST** log successful and unsuccessful login attempts.

R-10173: The VNF **MUST** allow another NETCONF session to be able to initiate the release of the lock by killing the session owning the lock, using the <kill-session> operation to guard against hung NETCONF sessions.

R-36280: The VNF Vendor **MUST** provide documentation describing VNF Functional Capabilities that are utilized to operationalize the VNF and compose complex services.

R-15671: The VNF **MUST NOT** provide public or unrestricted access to any data without the permission of the data owner. All data classification and access controls must be followed.

R-39342: The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "password changes (includes default passwords)" policy. Products will support password aging, syntax and other credential management practices on a configurable basis.

R-21558: The VNF **SHOULD** use intelligent routing by having knowledge of multiple downstream/upstream endpoints that are exposed to it, to ensure there is no dependency on external services (such as load balancers) to switch to alternate endpoints.

R-07545: The VNF **MUST** support all operations, administration and management (OAM) functions available from the supplier for VNFs using the supplied YANG code and associated NETCONF servers.

R-73541: The VNF **MIST** use access controls for VNFs and their supporting computing systems at all times to restrict access to authorized personnel only, e.g., least privilege. These controls could include the use of system configuration or access control software.

R-97102: The VNF Package **MUST** include VM requirements via a Heat template that provides the necessary data for:

R-44013: The VNF **MUST** populate an attribute, defined as node[‘PushJobOutput’] with the desired output on all nodes in the push job that execute chef-client run if the VNF action requires the output of a chef-client run be made available (e.g., get running configuration).

R-40521: The VNF **MUST**, if not using the NCSP’s IDAM API, support use of common third party authentication and authorization tools such as TACACS+, RADIUS.

R-41829: The VNF **MUST** be able to specify the granularity of the lock via a restricted or full XPath expression.

R-19768: The VNF **SHOULD** support L3 VPNs that enable segregation of traffic by application (dropping packets not belonging to the VPN) (i.e., AVPN, IPSec VPN for Internet routes).

R-55478: The VNF **MUST** log logoffs.

R-14853: The VNF **MUST** respond to a "move traffic" [3]_ command against a specific VNFC, moving all existing session elsewhere with minimal disruption if a VNF provides a load balancing function across multiple instances of its VNFCs. Note: Individual VNF performance aspects (e.g., move duration or disruption scope) may require further constraints.

R-68165: The VNF **MUST** encrypt any content containing Sensitive Personal Information (SPI) or certain proprietary data, in addition to applying the regular procedures for securing access and delivery.

R-31614: The VNF **MUST** log the field “event type” in the security audit logs.

R-87662: The VNF **SHOULD** implement the NETCONF Event Notifications [RFC5277].

R-26508: The VNF **MUST** support NETCONF server that can be mounted on OpenDaylight (client) and perform the following operations:

R-26567: The VNF Package **MUST** include a run list of roles/cookbooks/recipes, for each supported VNF action, that will perform the desired VNF action in its entirety as specified by ONAP (see Section 8.c, ONAP Controller APIs and Behavior, for list of VNF actions and requirements), when triggered by a chef-client run list in JSON file.

R-04158: The VNF **MUST** conform to the NETCONF RFC 4742, “Using the NETCONF Configuration Protocol over Secure Shell (SSH)”.

R-49109: The VNF **MUST** encrypt TCP/IP--HTTPS (e.g., TLS v1.2) transmission of data on internal and external networks.

R-15884: The VNF **MUST** include the field “date” in the Security alarms (where applicable and technically feasible).

R-15885: The VNF **MUST** Upon completion of the chef-client run, POST back on the callback URL, a JSON object as described in Table A2 if the chef-client run list includes a cookbook/recipe that is callback capable. Failure to POST on the Callback Url should not be considered a critical error. That is, if the chef-client successfully completes the VNF action, it should reflect this status on the Chef Server regardless of whether the Callback succeeded or not.

R-82223: The VNF **MUST** be decomposed if the functions have significantly different scaling characteristics (e.g., signaling versus media functions, control versus data plane functions).

R-37608: The VNF **MUST** provide a mechanism to restrict access based on the attributes of the VNF and the attributes of the subject.

R-02170: The VNF **MUST** use, whenever possible, standard implementations of security applications, protocols, and format, e.g., S/MIME, TLS, SSH, IPSec, X.509 digital certificates for cryptographic implementations. These implementations must be purchased from reputable vendors and must not be developed in-house.

R-11235: The VNF **MUST** implement the protocol operation: **kill-session(session)** - Force the termination of **session**.

R-87564: The VNF **SHOULD** conform its YANG model to RFC 7317, “A YANG Data Model for System Management”.

R-69649: The VNF **MUST** have all vulnerabilities patched as soon as possible. Patching shall be controlled via change control process with vulnerabilities disclosed along with mitigation recommendations.

R-75041: The VNF **MUST**, if not using the NCSP’s IDAM API, expire passwords at regular configurable intervals.

R-23035: The VNF **MUST** be designed to scale horizontally (more instances of a VNF or VNFC) and not vertically (moving the existing instances to larger VMs or increasing the resources within a VM) to achieve effective utilization of cloud resources.

R-97445: The VNF **MUST** log the field “date/time” in the security audit logs.

R-16777: The VNF Vendor **MUST** provide a JSON file for each supported action for the VNF.  The JSON file must contain key value pairs with all relevant values populated with sample data that illustrates its usage. The fields and their description are defined in Appendix B.

R-08134: The VNF **MUST** conform to the NETCONF RFC 6241, “NETCONF Configuration Protocol”.

R-01382: The VNF **MUST** allow the entire configuration of the VNF to be retrieved via NETCONF's <get-config> and <edit-config>, independently of whether it was configured via NETCONF or other mechanisms.

R-98929: The VNF **MAY** have a single endpoint.

R-48356: The VNF **MUST** fully exploit exception handling to the extent that resources (e.g., threads and memory) are released when no longer needed regardless of programming language.

R-90007: The VNF **MUST** implement the protocol operation: **close-session()**- Gracefully close the current session.

R-42140: The VNF **MUST** respond to data requests from ONAP as soon as those requests are received, as a synchronous response.

R-27511: The VNF Vendor **MUST** provide the ability to scale up a vendor supplied product during growth and scale down a vendor supplied product during decline without “real-time” restrictions based upon vendor permissions.

R-05470: The VNF **MUST** host connectors for access to the database layer.

R-85633: The VNF **MUST** implement Data Storage Encryption (database/disk encryption) for Sensitive Personal Information (SPI) and other subscriber identifiable data. Note: subscriber’s SPI/data must be encrypted at rest, and other subscriber identifiable data should be encrypted at rest. Other data protection requirements exist and should be well understood by the developer.

R-36792: The VNF **MUST** automatically retry/resubmit failed requests made by the software to its downstream system to increase the success rate.

R-49036: The VNF **SHOULD** conform its YANG model to RFC 7277, “A YANG Data Model for IP Management”.

R-63217: The VNF **MUST**, if not using the NCSP’s IDAM API, support logging via ONAP for a historical view of “who did what and when”.

R-44125: The VNF Vendor **MUST** agree to the process that can be met by Service Provider reporting infrastructure. The Contract shall define the reporting process and the available reporting tools.

R-22700: The VNF **MUST** conform its YANG model to RFC 6470, “NETCONF Base Notifications”.

R-74958: The VNF **MUST** activate security alarms automatically when the following event is detected: unsuccessful attempts to gain permissions or assume the identity of another user

R-44281: The VNF **MUST** implement the protocol operation: **edit-config(target, default-operation, test-option, error-option, config)** - Edit the target configuration datastore by merging, replacing, creating, or deleting new config elements.

R-81777: The VNF **MUST** be configured with initial address(es) to use at deployment time. After that the address(es) may be changed through ONAP-defined policies delivered from ONAP to the VNF using PUTs to a RESTful API, in the same way that other controls over data reporting will be controlled by policy.

R-07879: The VNF Package **MUST** include all relevant playbooks to ONAP to be loaded on the Ansible Server.

R-57855: The VNF **MUST** support hitless staggered/rolling deployments between its redundant instances to allow "soak-time/burn in/slow roll" which can enable the support of low traffic loads to validate the deployment prior to supporting full traffic loads.

R-73285: The VNF **MUST** must encode the delivered data using JSON or Avro, addressed and delivered as described in the previous paragraphs.

R-85028: The VNF **MUST** authenticate system to system access and do not conceal a VNF vendor user’s individual accountability for transactions.

R-28545: The VNF **MUST** conform its YANG model to RFC 6060, “YANG - A Data Modeling Language for the Network Configuration Protocol (NETCONF)”

R-74712: The VNF **MUST** utilize FQDNs (and not IP address) for both Service Chaining and scaling.

R-29760: The VNFC **MUST** be installed on non-root file systems, unless software is specifically included with the operating system distribution of the guest image.

R-08315: The VNF **SHOULD** use redundant connection pooling to connect to any backend data source that can be switched between pools in an automated/scripted fashion to ensure high availability of the connection to the data source.

R-42874: The VNF **MUST** comply with Least Privilege (no more privilege than required to perform job functions) when persons or non-person entities access VNFs.

R-08312: The VNF **MAY** use other options which are expected to include

R-19082: The VNF **MUST NOT** run security testing tools and programs, e.g., password cracker, port scanners, hacking tools in production, without authorization of the VNF system owner.

R-39650: The VNF **SHOULD** provide the ability to test incremental growth of the VNF.

R-15325: The VNF **MUST** log the field “success/failure” in the security audit logs.

R-07617: The VNF **MUST** log creating, removing, or changing the inherent privilege level of users.

R-53015: The VNF **MUST** apply locking based on the sequence of NETCONF operations, with the first configuration operation locking out all others until completed.

R-83500: The VNF **MUST** provide the capability of allowing certificate renewal and revocation.

R-23772: The VNF **MUST** validate input at all layers implementing VNF APIs.

R-83227: The VNF **MUST** Provide the capability to encrypt data in transit on a physical or virtual network.

R-36843: The VNF **MUST** support the ability of the VNFC to be deployable in multi-zoned cloud sites to allow for site support in the event of cloud zone failure or upgrades.

R-10129: The VNF **SHOULD** conform its YANG model to RFC 7223, “A YANG Data Model for Interface Management”.

R-18733: The VNF **MUST** implement the protocol operation: **discard-changes()** - Revert the candidate configuration datastore to the running configuration.

R-21819: The VNF **MUST** support requests for information from law enforcement and government agencies.

R-92207: The VNF **SHOULD** implement a mechanism for automated and frequent "system configuration (automated provisioning / closed loop)" auditing.

R-63935: The VNF **MUST** release locks to prevent permanent lock-outs when a user configured timer has expired forcing the NETCONF SSH Session termination (i.e., product must expose a configuration knob for a user setting of a lock expiration timer)

R-79224: The VNF **MUST** have the chef-client be preloaded with validator keys and configuration to register with the designated Chef Server as part of the installation process.

R-12467: The VNF **MUST NOT** use the SHA, DSS, MD5, SHA-1 and Skipjack algorithms or other compromised encryption.

R-68589: The VNF **MUST**, if not using the NCSP’s IDAM API, support User-IDs and passwords to uniquely identify the user/application. VNF needs to have appropriate connectors to the Identity, Authentication and Authorization systems that enables access at OS, Database and Application levels as appropriate.

R-26115: The VNF **MUST** follow the data model upgrade rules defined in [RFC6020] section 10. All deviations from section 10 rules shall be handled by a built-in automatic upgrade mechanism.

R-49145: The VNF **MUST** implement **:confirmed-commit** If **:candidate** is supported.

R-04298: The VNF Vendor **MUST** provide their testing scripts to support testing.

R-92935: The VNF **SHOULD** minimize the propagation of state information across multiple data centers to avoid cross data center traffic.

R-47204: The VNF **MUST** protect the confidentiality and integrity of data at rest and in transit from unauthorized access and modification.

R-32695: The VNF **MUST** provide the ability to modify the number of retries, the time between retries and the behavior/action taken after the retries have been exhausted for exception handling to allow the NCSP to control that behavior.

R-58964: The VNF **MUST** provide the capability to restrict read and write access to data.

R-73364: The VNF **MUST** support at least two major versions of the VNF software and/or sub-components to co-exist within production environments at any time so that upgrades can be applied across multiple systems in a staggered manner.

R-33946: The VNF **MUST** conform to the NETCONF RFC 4741, “NETCONF Configuration Protocol”.

R-24269: The VNF **SHOULD** conform its YANG model to RFC 7407, “A YANG Data Model for SNMP Configuration”.

R-16039: The VNF **SHOULD** test for adherence to the defined resiliency rating recommendation at each layer, during each delivery cycle so that the resiliency rating is measured and feedback is provided where software resiliency requirements are not met.

R-46290: The VNF **MUST** respond to an ONAP request to deliver granular data on device or subsystem status or performance, referencing the YANG configuration model for the VNF by returning the requested data elements.

R-11240: The VNF **MUST** respond with content encoded in JSON, as described in the RESTCONF specification. This way the encoding of a synchronous communication will be consistent with Avro.

R-83790: The VNF **MUST** implement the **:validate** capability

R-83873: The VNF **MUST** support **:rollback-on-error** value for the <error-option> parameter to the <edit-config> operation. If any error occurs during the requested edit operation, then the target database (usually the running configuration) will be left affected. This provides an 'all-or-nothing' edit mode for a single <edit-config> request.

R-25238: The VNF PACKAGE **MUST** validated YANG code using the open source pyang [2]_ program using the following commands:

R-58370: The VNF **MUST** coexist and operate normally with commercial anti-virus software which shall produce alarms every time when there is a security incident.

R-39604: The VNF **MUST** provide the capability of testing the validity of a digital certificate by checking the Certificate Revocation List (CRL) for the certificates of that type to ensure that the certificate has not been revoked.

R-06617: The VNF **MUST** support get-schema (ietf-netconf-monitoring) to pull YANG model over session.

R-13344: The VNF **MUST** log starting and stopping of security logging

R-02360: The VNFC **MUST** be designed as a standalone, executable process.

R-80070: The VNF **MUST** handle errors and exceptions so that they do not interrupt processing of incoming VNF requests to maintain service continuity.

R-02137: The VNF **MUST** implement all monitoring and logging as described in the Security Analytics section.

R-16496: The VNF **MUST** enable instantiating only the functionality that is needed for the decomposed VNF (e.g., if transcoding is not needed it should not be instantiated).

R-32217: The VNF **MUST** have routable FQDNs that are reachable via the Ansible Server for the endpoints (VMs) of a VNF on which playbooks will be executed. ONAP will initiate requests to the Ansible Server for invocation of playbooks against these end points [6]_.

R-47849: The VNF Vendor **MUST** support the metadata about licenses (and their applicable entitlements) as defined in this document for VNF software, and any license keys required to authorize use of the VNF software.  This metadata will be used to facilitate onboarding the VNF into the ONAP environment and automating processes for putting the licenses into use and managing the full lifecycle of the licenses. The details of this license model are described in Appendix C. Note: License metadata support in ONAP is not currently available and planned for 1Q 2018.

R-85419: The VNF **SHOULD** use REST APIs exposed to Client Applications for the implementation of OAuth 2.0 Authorization Code Grant and Client Credentials Grant, as the standard interface for a VNF.

R-34660: The VNF **MUST** use the RESTCONF/NETCONF framework used by the ONAP configuration subsystem for synchronous communication.

R-88026: The VNF **MUST** include a NETCONF server enabling runtime configuration and lifecycle management capabilities.

R-48080: The VNF **SHOULD** support SCEP (Simple Certificate Enrollment Protocol).

R-43884: The VNF **MUST** integrate with external authentication and authorization services (e.g., IDAM).

R-70933: The VNF **MUST** provide the ability to migrate to newer versions of cryptographic algorithms and protocols with no impact.

R-48917: The VNF **MUST** monitor for and alert on (both sender and receiver) errant, running longer than expected and missing file transfers, so as to minimize the impact due to file transfer errors.

R-79107: The VNF **MUST**, if not using the NCSP’s IDAM API, enforce a configurable maximum number of Login attempts policy for the users. VNF vendor must comply with "terminate idle sessions" policy. Interactive sessions must be terminated, or a secure, locking screensaver must be activated requiring authentication, after a configurable period of inactivity. The system-based inactivity timeout for the enterprise identity and access management system must also be configurable.

R-75850: The VNF **SHOULD** decouple persistent data from the VNFC and keep it in its own datastore that can be reached by all instances of the VNFC requiring the data.

R-46960: The VNF **MUST** utilize only the Guest OS versions that are supported by the NCSP’s Network Cloud. [1]_

R-21210: The VNF **MUST** implement the following input validation control: Validate that any input file has a correct and valid Multipurpose Internet Mail Extensions (MIME) type. Input files should be tested for spoofed MIME types.

R-23823: The VNF Package **MUST** include appropriate credentials so that ONAP can interact with the Chef Server.

R-24359: The VNF **MUST** provide the capability of testing the validity of a digital certificate by validating the date the certificate is being used is within the validity period for the certificate.

R-49224: The VNF **MUST** provide unique traceability of a transaction through its life cycle to ensure quick and efficient troubleshooting.

R-04982: The VNF **MUST NOT** include an authentication credential, e.g., password, in the security audit logs, even if encrypted.

R-74481: The VNF **MUST** NOT require the use of a dynamic routing protocol unless necessary to meet functional requirements.

R-98911: The VNF **MUST NOT** use any instance specific parameters for the VNF in roles/cookbooks/recipes invoked for a VNF action.

R-89571: The VNF **MUST** support and provide artifacts for configuration management using at least one of the following technologies:

R-87135: The VNF **MUST** comply with NIST standards and industry best practices for all implementations of cryptography.

R-04492: The VNF **MUST** generate security audit logs that must be sent to Security Analytics Tools for analysis.

R-02597: The VNF **MUST** implement the protocol operation: **lock(target)** - Lock the configuration datastore target.

R-13800: The VNF **MUST** conform to the NETCONF RFC 5277, “NETCONF Event Notification”.

R-64445: The VNF **MUST** support the ability of a requestor of the service to determine the version (and therefore capabilities) of the service so that Network Cloud Service Provider can understand the capabilities of the service.

R-64768: The VNF **MUST** limit the size of application data packets to no larger than 9000 bytes for SDN network-based tunneling when guest data packets are transported between tunnel endpoints that support guest logical networks.

R-75608: The VNF Vendor **MUST** provide playbooks to be loaded on the appropriate Ansible Server.

R-61354: The VNF **MUST** implement access control list for OA&M services (e.g., restricting access to certain ports or applications).

R-62468: The VNF **MUST** allow all configuration data shall to be edited through a NETCONF <edit-config> operation. Proprietary NETCONF RPCs that make configuration changes are not sufficient.

R-34552: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for OWASP Top 10.

R-29977: The VNF **MUST** provide the capability of testing the validity of a digital certificate by validating the CA signature on the certificate.

R-67709: The VNF **MUST** be designed, built and packaged to enable deployment across multiple fault zones (e.g., VNFCs deployed in different servers, racks, OpenStack regions, geographies) so that in the event of a planned/unplanned downtime of a fault zone, the overall operation/throughput of the VNF is maintained.

R-46567: The VNF Package **MUST** include configuration scripts for boot sequence and configuration.

R-55345: The VNF **SHOULD** use techniques such as “lazy loading” when initialization includes loading catalogues and/or lists which can grow over time, so that the VNF startup time does not grow at a rate proportional to that of the list.

R-88482: The VNF **SHOULD** use REST using HTTPS delivery of plain text JSON for moderate sized asynchronous data sets, and for high volume data sets when feasible.

R-56786: The VNF **MUST** implement “Closed Loop” automatic implementation (without human intervention) for Known Threats with detection rate in low false positives.

R-94525: The VNF **MUST** log connections to a network listener of the resource.

R-85428: The VNF **MUST** meet the same guidelines as Chef Server hosted by ONAP.

R-26371: The VNF **MUST** detect connectivity failure for inter VNFC instance and intra/inter VNF and re-establish connectivity automatically to maintain the VNF without manual intervention to provide service continuity.

R-35851: The VNF Package **MUST** include VNF topology that describes basic network and application connectivity internal and external to the VNF including Link type, KPIs, Bandwidth, latency, jitter, QoS (if applicable) for each interface.

R-29301: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Password Attacks.

R-23957: The VNF **MUST** include the field “time” in the Security alarms (where applicable and technically feasible).

R-32636: The VNF **MUST** support API-based monitoring to take care of the scenarios where the control interfaces are not exposed, or are optimized and proprietary in nature.

R-39562: The VNF **MUST** disable unnecessary or vulnerable cgi-bin programs.

R-77334: The VNF **MUST** allow configurations and configuration parameters to be managed under version control to ensure consistent configuration deployment, traceability and rollback.

R-44723: The VNF **MUST** use symmetric keys of at least 112 bits in length.

R-86585: The VNFC **SHOULD** minimize the use of state within a VNFC to facilitate the movement of traffic from one instance to another.

R-18725: The VNF **MUST** handle the restart of a single VNFC instance without requiring all VNFC instances to be restarted.

R-53317: The VNF **MUST** conform its YANG model to RFC 6087, “Guidelines for Authors and Reviewers of YANG Data Model Documents”.

R-67114: The VNF **MUST** be installed with:

R-28168: The VNF **SHOULD** use an appropriately configured logging level that can be changed dynamically, so as to not cause performance degradation of the VNF due to excessive logging.

R-54930: The VNF **MUST** implement the following input validation control: Do not permit input that contains content or characters inappropriate to the input expected by the design. Inappropriate input, such as SQL insertions, may cause the system to execute undesirable and unauthorized transactions against the database or allow other inappropriate access to the internal network.

R-55830: The VNF **MUST** distribute all production code from NCSP internal sources only. No production code, libraries, OS images, etc. shall be distributed from publically accessible depots.

R-22367: The VNF **MUST** support detection of malformed packets due to software misconfiguration or software vulnerability.

R-93860: The VNF **MUST** provide the capability to integrate with an external encryption service.

R-09467: The VNF **MUST**  utilize only NCSP standard compute flavors. [2]_

R-62170: The VNF **MUST** over-ride any default values for configurable parameters that can be set by ONAP in the roles, cookbooks and recipes.

R-41994: The VNF **MUST**, if not using the NCSP’s IDAM API, comply with "No Self-Signed Certificates" policy. Self-signed certificates must be used for encryption only, using specified and approved encryption protocols such as LS 1.1 or higher or equivalent security protocols such as IPSec, AES.

R-nnnnn: The VNF MUST have a corresponding environment file for a Cinder Volume Module.

R-84160: The VNF **MUST** have security logging for VNFs and their OSs be active from initialization. Audit logging includes automatic routines to maintain activity records and cleanup programs to ensure the integrity of the audit/logging systems.

R-99656: The VNF **MUST** NOT terminate stable sessions if a VNFC instance fails.

R-80898: The VNF **MUST** support heartbeat via a <get> with null filter.

R-20974: The VNF **MUST** deploy the base module first, prior to the incremental modules.

R-69610: The VNF **MUST** provide the capability of using certificates issued from a Certificate Authority not provided by the VNF vendor.

R-27310: The VNF Package **MUST** include all relevant Chef artifacts (roles/cookbooks/recipes) required to execute VNF actions requested by ONAP for loading on appropriate Chef Server.

R-98191: The VNF **MUST** vary the frequency that asynchronous data is delivered based on the content and how data may be aggregated or grouped together. For example, alarms and alerts are expected to be delivered as soon as they appear. In contrast, other content, such as performance measurements, KPIs or reported network signaling may have various ways of packaging and delivering content. Some content should be streamed immediately; or content may be monitored over a time interval, then packaged as collection of records and delivered as block; or data may be collected until a package of a certain size has been collected; or content may be summarized statistically over a time interval, or computed as a KPI, with the summary or KPI being delivered.

R-31412: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for XSS / CSRF.

R-58775: The VNF Vendor **MUST** provide software components that can be packaged with/near the VNF, if needed, to simulate any functions or systems that connect to the VNF system under test. This component is necessary only if the existing testing environment does not have the necessary simulators.

R-45496: The VNF **MUST** host connectors for access to the OS (Operating System) layer.

R-13151: The VNF **SHOULD** disable the paging of the data requiring encryption, if possible, where the encryption of non-transient data is required on a device for which the operating system performs paging to virtual memory. If not possible to disable the paging of the data requiring encryption, the virtual memory should be encrypted.

R-49308: The VNF **SHOULD** test for adherence to the defined resiliency rating recommendation at each layer, during each delivery cycle with delivered results, so that the resiliency rating is measured and the code is adjusted to meet software resiliency requirements.

R-74763: The VNF Vendor **MUST** provide an artifact per VNF that contains all of the VNF Event Records supported. The artifact should include reference to the specific release of the VNF Event Stream Common Event Data Model document it is based on. (e.g., `VES Event Listener <https://github.com/att/evel-test-collector/tree/master/docs/att_interface_definition>`__)

R-77786: The VNF Package **MUST** include all relevant cookbooks to be loaded on the ONAP Chef Server.

R-54373: The VNF **MUST** have Python >= 2.7 on the endpoint VM(s) of a VNF on which an Ansible playbook will be executed.

R-60106: The VNF **MUST** implement the protocol operation: **get(filter)** - Retrieve (a filtered subset of) the running configuration and device state information. This should include the list of VNF supported schemas.

R-35305: The VNF **MUST** meet the same guidelines as the Ansible Server hosted by ONAP.

R-95864: The VNF **MUST** use commercial tools that comply with X.509 standards and produce x.509 compliant keys for public/private key generation.

R-23475: The VNF **SHOULD** utilize only NCSP provided Guest OS images. [2]_

R-64503: The VNF **MUST** provide minimum privileges for initial and default settings for new user accounts.

R-42681: The VNF **MUST** use the NCSP’s IDAM API or comply with the requirements if not using the NCSP’s IDAM API, for identification, authentication and access control of OA&M and other system level functions.

R-19219: The VNF **MUST** provide audit logs that include user ID, dates, times for log-on and log-off, and terminal location at minimum.

R-73067: The VNF **MUST** use industry standard cryptographic algorithms and standard modes of operations when implementing cryptography.

R-25878: The VNF **MUST** use certificates issued from publicly recognized Certificate Authorities (CA) for the authentication process where PKI-based authentication is used.

R-70266: The VNF **MUST** respond to an ONAP request to deliver the current data for any of the record types defined in Section 8.d “Data Model for Event Records” by returning the requested record, populated with the current field values. (Currently the defined record types include the common header record, technology independent records such as Fault, Heartbeat, State Change, Syslog, and technology specific records such as Mobile Flow, Signaling and Voice Quality records.  Additional record types will be added in the future as they are standardized and become available.)

R-70496: The VNF **MUST** implement the protocol operation: **commit(confirmed, confirm-timeout)** - Commit candidate configuration datastore to the running configuration.

R-19624: The VNF **MUST** encode and serialize content delivered to ONAP using JSON (option 1). High-volume data is to be encoded and serialized using Avro, where Avro data format are described using JSON (option 2) [8]_.

R-25094: The VNF **MUST** perform data capture for security functions.

R-44032: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Man in the Middle (MITM).

R-47068: The VNF **MAY** expose a single endpoint that is responsible for all functionality.

R-49396: The VNF **MUST** support each VNF action by invocation of **one** playbook [7]_. The playbook will be responsible for executing all necessary tasks (as well as calling other playbooks) to complete the request.

R-63953: The VNF **MUST** have the echo command return a zero value otherwise the validation has failed

R-56904: The VNF **MUST** interoperate with the ONAP (SDN) Controller so that it can dynamically modify the firewall rules, ACL rules, QoS rules, virtual routing and forwarding rules.

R-37929: The VNF **MUST** accept all necessary instance specific data from the environment or node object attributes for the VNF in roles/cookbooks/recipes invoked for a VNF action.

R-84366: The VNF Package **MUST** include documentation describing VNF Functional APIs that are utilized to build network and application services. This document describes the externally exposed functional inputs and outputs for the VNF, including interface format and protocols supported.

R-58421: The VNF **SHOULD** be decomposed into granular re-usable VNFCs.

R-27711: The VNF Vendor **MUST** provide an XML file that contains a list of VNF error codes, descriptions of the error, and possible causes/corrective action.

R-78282: The VNF **MUST** conform to the NETCONF RFC 6242, “Using the Network Configuration Protocol over Secure Shell”.

R-99766: The VNF **MUST** allow configurations and configuration parameters to be managed under version control to ensure the ability to rollback to a known valid configuration.

R-89010: The VNF **MUST** survive any single points of software failure internal to the VNF (e.g., in memory structures, JMS message queues).

R-77667: The VNF **MUST** test for adherence to the defined performance budget at each layer, during each delivery cycle so that the performance budget is measured and feedback is provided where the performance budget is not met.

R-21652: The VNF **MUST** implement the following input validation control: Check the size (length) of all input. Do not permit an amount of input so great that it would cause the VNF to fail. Where the input may be a file, the VNF API must enforce a size limit.

R-54190: The VNF **MUST** release locks to prevent permanent lock-outs when/if a session applying the lock is terminated (e.g., SSH session is terminated).

R-12271: The VNF **SHOULD** conform its YANG model to RFC 7223, “IANA Interface Type YANG Module”.

R-25547: The VNF **MUST** log the field “protocol” in the security audit logs.

R-22286: The VNF **MUST** support Integration functionality via API/Syslog/SNMP to other functional modules in the network (e.g., PCRF, PCEF) that enable dynamic security control by blocking the malicious traffic or malicious end users

R-16560: The VNF **MUST** conduct a resiliency impact assessment for all inter/intra-connectivity points in the VNF to provide an overall resiliency rating for the VNF to be incorporated into the software design and development of the VNF.

R-99112: The VNF **MUST** provide the capability to restrict access to data to specific users.

R-02997: The VNF **MUST** preserve their persistent data. Running VMs will not be backed up in the Network Cloud infrastructure.

R-19367: The VNF **MUST** monitor API invocation patterns to detect anomalous access patterns that may represent fraudulent access or other types of attacks, or integrate with tools that implement anomaly and abuse detection.

R-33981: The VNF **SHOULD** interoperate with various access control mechanisms for the Network Cloud execution environment (e.g., Hypervisors, containers).

R-26881: The VNF Vendor **MUST** provide the binaries and images needed to instantiate the VNF (VNF and VNFC images).

R-69565: The VNF Package **MUST** include documentation describing VNF Management APIs. The document must include information and tools for:

R-92571: The VNF **MUST** provide operational instrumentation such as logging, so as to facilitate quick resolution of issues with the VNF to provide service continuity.

R-77737: The VNF **MUST**

R-29488: The VNF **MUST** implement the protocol operation: **get-config(source, filter)** - Retrieve a (filtered subset of a) configuration from the configuration datastore source.

R-03070: The VNF **MUST**, by ONAP Policy, provide the ONAP addresses as data destinations for each VNF, and may be changed by Policy while the VNF is in operation. We expect the VNF to be capable of redirecting traffic to changed destinations with no loss of data, for example from one REST URL to another, or from one TCP host and port to another.

R-89800: The VNF **MUST NOT** require Hypervisor-level customization from the cloud provider.

R-12110: The VNF **MUST NOT** use keys generated or derived from predictable functions or values, e.g., values considered predictable include user identity information, time of day, stored/transmitted data.

R-03954: The VNF **MUST** survive any single points of failure within the Network Cloud (e.g., virtual NIC, VM, disk failure).

R-98391: The VNF **MUST**, if not using the NCSP’s IDAM API, support Role-Based Access Control to permit/limit the user/application to performing specific activities.

R-29967: The VNF **MUST** conform its YANG model to RFC 6022, “YANG module for NETCONF monitoring”.

R-80335: The VNF **MUST** make visible a Warning Notices: A formal statement of resource intent, i.e., a warning notice, upon initial access to a VNF vendor user who accesses private internal networks or Company computer resources, e.g., upon initial logon to an internal web site, system or application which requires authentication.

R-48596: The VNF Package **MUST** include documentation describing the characteristics for the VNF reliability and high availability.

R-49956: The VNF **MUST** pass all access to applications (Bearer, signaling and OA&M) through various security tools and platforms from ACLs, stateful firewalls and application layer gateways depending on manner of deployment. The application is expected to function (and in some cases, interwork) with these security tools.

R-02616: The VNF **MUST** permit locking at the finest granularity if a VNF needs to lock an object for configuration to avoid blocking simultaneous configuration operations on unrelated objects (e.g., BGP configuration should not be locked out if an interface is being configured or entire Interface configuration should not be locked out if a non-overlapping parameter on the interface is being configured).

R-15659: The VNF **MUST** restrict changing the criticality level of a system security alarm to administrator(s).

R-96634: The VNF Vendor **MUST** describe scaling capabilities to manage scaling characteristics of the VNF.

R-32641: The VNF **MUST** provide the capability to encrypt data on non-volatile memory.

R-48470: The VNF **MUST** support Real-time detection and notification of security events.

R-91681: The VNF **MUST** meet the ONAP Ansible Server API Interface requirements.

R-41825: The VNF **MUST** activate security alarms automatically when the following event is detected: configurable number of consecutive unsuccessful login attempts

R-52870: The VNF **MUST** provide a method of metrics gathering and analysis to evaluate the resiliency of the software from both a granular as well as a holistic standpoint. This includes, but is not limited to thread utilization, errors, timeouts, and retries.

R-89474: The VNF **MUST** log the field “Login ID” in the security audit logs.

R-13390: The VNF Vendor **MUST** provide cookbooks to be loaded on the appropriate Chef Server.

R-24825: The VNF **MUST** provide Context awareness data (device, location, time, etc.) and be able to integrate with threat detection system.

R-23882: The VNF **SHOULD** be scanned using both network scanning and application scanning security tools on all code, including underlying OS and related configuration. Scan reports shall be provided. Remediation roadmaps shall be made available for any findings.

R-22946: The VNF **SHOULD** conform its YANG model to RFC 6536, “NETCONF Access Control Model”.

R-89753: The VNF **MUST NOT** install or use systems, tools or utilities capable of capturing or logging data that was not created by them or sent specifically to them in production, without authorization of the VNF system owner.

R-88899: The VNF **MUST** support simultaneous <commit> operations within the context of this locking requirements framework.

R-96554: The VNF **MUST** implement the protocol operation: **unlock(target)** - Unlock the configuration datastore target.

R-27995: The VNF **SHOULD** include control loop mechanisms to notify the consumer of the VNF of their exceeding SLA thresholds so the consumer is able to control its load against the VNF.

R-31809: The VNF **MUST** support the HealthCheck RPC. The HealthCheck RPC, executes a vendor-defined VNF Healthcheck over the scope of the entire VNF (e.g., if there are multiple VNFCs, then run a health check, as appropriate, for all VNFCs). It returns a 200 OK if the test completes. A JSON object is returned indicating state (healthy, unhealthy), scope identifier, time-stamp and one or more blocks containing info and fault information. If the VNF is unable to run the HealthCheck, return a standard http error code and message.

R-25401: The VNF **MUST** use asymmetric keys of at least 2048 bits in length.

R-31961: The VNF **MUST** support integrated DPI/monitoring functionality as part of VNFs (e.g., PGW, MME).

R-47597: The VNF **MUST** carry data in motion only over secure connections.

R-43253: The VNF **MUST** use playbooks designed to allow Ansible Server to infer failure or success based on the “PLAY_RECAP” capability.

R-23135: The VNF **MUST**, if not using the NCSP’s IDAM API, authenticate system to system communications were one system accesses the resources of another system, and must never conceal individual accountability.

R-99730: The VNF **MUST** include the field “Login ID” in the Security alarms (where applicable and technically feasible).

R-88199: The VNF **MUST** utilize virtualized, scalable open source database software that can meet the performance/latency requirements of the service for all datastores.

R-08598: The VNF **MUST** log successful and unsuccessful changes to a privilege level.

R-87352: The VNF **SHOULD** utilize Cloud health checks, when available from the Network Cloud, from inside the application through APIs to check the network connectivity, dropped packets rate, injection, and auto failover to alternate sites if needed.

R-56920: The VNF **MUST** protect all security audit logs (including API, OS and application-generated logs), security audit software, data, and associated documentation from modification, or unauthorized viewing, by standard OS access control mechanisms, by sending to a remote system, or by encryption.

R-35291: The VNF **MUST** support the ability to failover a VNFC automatically to other geographically redundant sites if not deployed active-active to increase the overall resiliency of the VNF.

R-43332: The VNF **MUST** activate security alarms automatically when the following event is detected: successful modification of critical system or application files

R-81147: The VNF **MUST** have greater restrictions for access and execution, such as up to 3 factors of authentication and restricted authorization, for commands affecting network services, such as commands relating to VNFs, must.

R-60656: The VNF **MUST** support sub tree filtering.

R-51883: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Replay.

R-66070: The VNF Package **MUST** include VNF Identification Data to uniquely identify the resource for a given Vendor. The identification data must include: an identifier for the VNF, the name of the VNF as was given by the VNF Vendor, VNF description, VNF Vendor, and version.

R-19804: The VNF **MUST** validate the CA signature on the certificate, ensure that the date is within the validity period of the certificate, check the Certificate Revocation List (CRL), and recognize the identity represented by the certificate where PKI-based authentication is used.

R-06327: The VNF **MUST** respond to a "drain VNFC" [2]_ command against a specific VNFC, preventing new session from reaching the targeted VNFC, with no disruption to active sessions on the impacted VNFC, if a VNF provides a load balancing function across multiple instances of its VNFCs. This is used to support scenarios such as proactive maintenance with no user impact,

R-85653: The VNF **MUST** provide metrics (e.g., number of sessions, number of subscribers, number of seats, etc.) to ONAP for tracking every license.

R-63330: The VNF **MUST** detect when the security audit log storage medium is approaching capacity (configurable) and issue an alarm via SMS or equivalent as to allow time for proper actions to be taken to pre-empt loss of audit data.

R-22645: The VNF **SHOULD** use commercial algorithms only when there are no applicable governmental standards for specific cryptographic functions, e.g., public key cryptography, message digests.

R-22888: The VNF Vendor **MUST** provide documentation for the VNF Policy Description to manage the VNF runtime lifecycle. The document must include a description of how the policies (conditions and actions) are implemented in the VNF.

R-78066: The VNF **MUST** support requests for information from law enforcement and government agencies.

R-35144: The VNF **MUST**, if not using the NCSP’s IDAM API, comply with the NCSP’s credential management policy.

R-85959: The VNF **SHOULD** automatically enable/disable added/removed sub-components or component so there is no manual intervention required.

R-28756: The VNF **MUST** support **:partial-lock** and **:partial-unlock** capabilities, defined in RFC 5717. This allows multiple independent clients to each write to a different part of the <running> configuration at the same time.

R-41252: The VNF **MUST** support the capability of online storage of security audit logs.

R-77707: The VNF Vendor **MUST** include a Manifest File that contains a list of all the components in the VNF package.

R-20860: The VNF **MUST** be agnostic to the underlying infrastructure (such as hardware, host OS, Hypervisor), any requirements should be provided as specification to be fulfilled by any hardware.

R-01478: The VNF Package **MUST** include documentation describing all parameters that are available to monitor the VNF after instantiation (includes all counters, OIDs, PM data, KPIs, etc.) that must be collected for reporting purposes. The documentation must include a list of:

R-22059: The VNF **MUST NOT** execute long running tasks (e.g., IO, database, network operations, service calls) in a critical section of code, so as to minimize blocking of other operations and increase concurrent throughput.

R-30650: The VNF **MUST** utilize cloud provided infrastructure and VNFs (e.g., virtualized Local Load Balancer) as part of the VNF so that the cloud can manage and provide a consistent service resiliency and methods across all VNF's.

R-30654: The VNF Package **MUST** have appropriate cookbooks that are designed to automatically ‘rollback’ to the original state in case of any errors for actions that change state of the VNF (e.g., configure).

R-29705: The VNF **MUST** restrict changing the criticality level of a system security alarm to administrator(s).

R-71787: The VNF **MUST** comply with Segregation of Duties (access to a single layer and no developer may access production without special oversight) when persons or non-person entities access VNFs.

R-86758: The VNF **SHOULD** provide an automated test suite to validate every new version of the software on the target environment(s). The tests should be of sufficient granularity to independently test various representative VNF use cases throughout its lifecycle. Operations might choose to invoke these tests either on a scheduled basis or on demand to support various operations functions including test, turn-up and troubleshooting.

R-06885: The VNF **SHOULD** support the ability to scale down a VNFC pool without jeopardizing active sessions. Ideally, an active session should not be tied to any particular VNFC instance.

R-06924: The VNF **MUST** deliver asynchronous data as data becomes available, or according to the configured frequency.

R-65134: The VNF **SHOULD** maintain state in a geographically redundant datastore that may, in fact, be its own VNFC.

R-13627: The VNF **MUST** monitor API invocation patterns to detect anomalous access patterns that may represent fraudulent access or other types of attacks, or integrate with tools that implement anomaly and abuse detection.

R-86455: The VNF **SHOULD** support hosting connectors for OS Level and Application Access.

R-68990: The VNF **MUST** support the **:startup** capability. It will allow the running configuration to be copied to this special database. It can also be locked and unlocked.

R-78010: The VNF **MUST** use the NCSP’s IDAM API for Identification, authentication and access control of customer or VNF application users.

R-46986: The VNF **SHOULD** have source code scanned using scanning tools (e.g., Fortify) and provide reports.

R-97293: The VNF Vendor **MUST NOT** require audits of Service Provider’s business.

R-16065: The VNF Vendor **MUST** provide configurable parameters (if unable to conform to YANG model) including VNF attributes/parameters and valid values, dynamic attributes and cross parameter dependencies (e.g., customer provisioning data).

R-34484: The VNF **SHOULD** create a single component VNF for VNFCs that can be used by other VNFs.

R-30278: The VNF Vendor **MUST** provide a Resource/Device YANG model as a foundation for creating the YANG model for configuration. This will include VNF attributes/parameters and valid values/attributes configurable by policy.

R-35401: The VNF **MUST** must support SSH and allow SSH access to the Ansible server for the endpoint VM(s) and comply with the  Network Cloud Service Provider guidelines for authentication and access.

R-68200: The VNF **MUST** support the **:url** value to specify protocol operation source and target parameters. The capability URI for this feature will indicate which schemes (e.g., file, https, sftp) that the server supports within a particular URL value. The 'file' scheme allows for editable local configuration databases. The other schemes allow for remote storage of configuration databases.

R-41159: The VNF **MUST** deliver any and all functionality from any VNFC in the pool. The VNFC pool member should be transparent to the client. Upstream and downstream clients should only recognize the function being performed, not the member performing it.

R-18864: The VNF **MUST** NOT use technologies that bypass virtualization layers (such as SR-IOV) unless approved by the NCSP (e.g., if necessary to meet functional or performance requirements).

R-37028: The VNF **MUST** be composed of one “base” module.

R-40827: The VNF Vendor **MUST** enumerate all of the open source licenses their VNF(s) incorporate.

R-95950: The VNF **MUST** provide a NETCONF interface fully defined by supplied YANG models for the embedded NETCONF server.

R-10716: The VNF **MUST** support parallel and simultaneous configuration of separate objects within itself.

R-71842: The VNF **MUST** include the field “service or program used for access” in the Security alarms (where applicable and technically feasible).

R-54430: The VNF **MUST** use the NCSP’s supported library and compute flavor that supports DPDK to optimize network efficiency if using DPDK. [1]_

R-03465: The VNF **MUST** release locks to prevent permanent lock-outs when the corresponding <partial-unlock> operation succeeds.

R-65755: The VNF **SHOULD** support callback URLs to return information to ONAP upon completion of the chef-client run for any chef-client run associated with a VNF action.

R-11499: The VNF **MUST** fully support the XPath 1.0 specification for filtered retrieval of configuration and other database contents. The 'type' attribute within the <filter> parameter for <get> and <get-config> operations may be set to 'xpath'. The 'select' attribute (which contains the XPath expression) will also be supported by the server. A server may support partial XPath retrieval filtering, but it cannot advertise the **:xpath** capability unless the entire XPath 1.0 specification is supported.

R-95105: The VNF **MUST** host connectors for access to the application layer.

R-77157: The VNF **MUST** conform to approved request, workflow authorization, and authorization provisioning requirements when creating privileged users.

R-63473: The VNF **MUST** automatically advertise newly scaled components so there is no manual intervention required.

R-13613: The VNF **MUST** provide clear measurements for licensing purposes to allow automated scale up/down by the management system.

R-66793: The VNF **MUST** guarantee the VNF configuration integrity for all simultaneous configuration operations (e.g., if a change is attempted to the BUM filter rate from multiple interfaces on the same EVC, then they need to be sequenced in the VNF without locking either configuration method out).

R-19790: The VNF **MUST NOT** include authentication credentials in security audit logs, even if encrypted.

R-97529: The VNF **SHOULD** implement the protocol operation: **get-schema(identifier, version, format) -** Retrieve the YANG schema.

R-84473: The VNF **MUST** enable DPDK in the guest OS for VNF’s requiring high packets/sec performance.  High packet throughput is defined as greater than 500K packets/sec.

R-54816: The VNF **MUST** support the storage of security audit logs for agreed period of time for forensic analysis.

R-34957: The VNF **MUST** provide a method of metrics gathering for each layer's performance to identify/document variances in the allocations so they can be addressed.

R-43958: The VNF Package **MUST** include documentation describing the tests that were conducted by the Vendor and the test results.

R-61648: The VNF **MUST** support event logging, formats, and delivery tools to provide the required degree of event data to ONAP

R-18525: The VNF Vendor **MUST** provide a JSON file for each supported action for the VNF.  The JSON file must contain key value pairs with all relevant values populated with sample data that illustrates its usage. The fields and their description are defined in Appendix A.

R-99174: The VNF **MUST** comply with Individual Accountability (each person must be assigned a unique ID) when persons or non-person entities access VNFs.

R-99771: The VNF **MUST** provide all code/configuration files in a “Locked down” or hardened state or with documented recommendations for such hardening. All unnecessary services will be disabled. Vendor default credentials, community strings and other such artifacts will be removed or disclosed so that they can be modified or removed during provisioning.

R-58358: The VNF **MUST** implement the **:with-defaults** capability [RFC6243].

R-78116: The VNF **MUST** update status on the Chef Server appropriately (e.g., via a fail or raise an exception) if the chef-client run encounters any critical errors/failures when executing a VNF action.

R-84879: The VNF **MUST** have the capability of maintaining a primary and backup DNS name (URL) for connecting to ONAP collectors, with the ability to switch between addresses based on conditions defined by policy such as time-outs, and buffering to store messages until they can be delivered. At its discretion, the service provider may choose to populate only one collector address for a VNF. In this case, the network will promptly resolve connectivity problems caused by a collector or network failure transparently to the VNF.

R-06413: The VNF **MUST** log the field “service or program used for access” in the security audit logs.

R-51442: The VNF **SHOULD** use playbooks that are designed to automatically ‘rollback’ to the original state in case of any errors for actions that change state of the VNF (e.g., configure).

R-98989: The VNF **SHOULD** utilize resource pooling (threads, connections, etc.) within the VNF application so that resources are not being created and destroyed resulting in resource management overhead.

R-58998: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Malware (Key Logger).

R-52499: The VNF **MUST** meet their own resiliency goals and not rely on the Network Cloud.

R-43327: The VNF **SHOULD** use “Modeling JSON text with YANG”, https://trac.tools.ietf.org/id/draft-lhotka-netmod-yang-json-00.html, If YANG models need to be translated to and from JSON. YANG configuration and content can be represented via JSON, consistent with Avro, as described in “Encoding and Serialization” section.

R-52060: The VNF **MUST** provide the capability to configure encryption algorithms or devices so that they comply with the laws of the jurisdiction in which there are plans to use data encryption.

R-10353: The VNF **MUST** conform its YANG model to RFC 6244, “An Architecture for Network Management Using NETCONF and YANG”.

R-26586: The VNF **SHOULD** support the ability to work with aliases (e.g., gateways, proxies) to protect and encapsulate resources.

R-14025: The VNF **MUST** provide or support the Identity and Access Management (IDAM) based threat detection data for Session Hijacking.

R-86835: The VNF **MUST** set the default settings for user access to sensitive commands and data to deny authorization.

R-73583: The VNF **MUST** allow changes of configuration parameters to be consumed by the VNF without requiring the VNF or its sub-components to be bounced so that the VNF availability is not effected.

R-73223: The VNF **MUST** support proactive monitoring to detect and report the attacks on resources so that the VNFs and associated VMs can be isolated, such as detection techniques for resource exhaustion, namely OS resource attacks, CPU attacks, consumption of kernel memory, local storage attacks.

R-06668: The VNF **MUST** handle the start or restart of VNFC instances in any order with each VNFC instance establishing or re-establishing required connections or relationships with other VNFC instances and/or VNFs required to perform the VNF function/role without requiring VNFC instance(s) to be started/restarted in a particular order.

R-41215: The VNF **MAY** have zero to many “incremental” modules.

R-85991: The VNF Vendor **MUST** provide a universal license key per VNF to be used as needed by services (i.e., not tied to a VM instance) as the recommended solution. The vendor may provide pools of Unique VNF License Keys, where there is a unique key for each VNF instance as an alternate solution. Licensing issues should be resolved without interrupting in-service VNFs.

R-52085: The VNF **MUST**, if not using the NCSP’s IDAM API, provide the ability to support Multi-Factor Authentication (e.g., 1st factor = Software token on device (RSA SecureID); 2nd factor = User Name+Password, etc.) for the users.

R-29495: The VNF **MUST** support locking if a common object is being manipulated by two simultaneous NETCONF configuration operations on the same VNF within the context of the same writable running data store (e.g., if an interface parameter is being configured then it should be locked out for configuration by a simultaneous configuration operation on that same interface parameter).

R-31751: The VNF **MUST** subject vendor VNF access to privilege reconciliation tools to prevent access creep and ensure correct enforcement of access policies.

R-48698: The VNF **MUST** utilize   information from key value pairs that will be provided by the Ansible Server as extra-vars during invocation to execute the desired VNF action. If the playbook requires files, they must also be supplied using the methodology detailed in the Ansible Server API.

R-44290: The VNF **MUST** control access to ONAP and to VNFs, and creation of connections, through secure credentials, log-on and exchange mechanisms.

R-40293: The VNF **MUST** make available (or load on VNF Ansible Server) playbooks that conform to the ONAP requirement.

R-30932: The VNF **MUST** provide security audit logs including records of successful and rejected system access data and other resource access attempts.

R-12538: The VNF **SHOULD** support load balancing and discovery mechanisms in resource pools containing VNFC instances.

R-59610: The VNF **MUST** implement the data model discovery and download as defined in [RFC6022].

R-49945: The VNF **MUST** authorize vendor access through a client application API by the client application owner and the resource owner of the VNF before provisioning authorization through Role Based Access Control (RBAC), Attribute Based Access Control (ABAC), or other policy based mechanism.

R-20912: The VNF **MUST** support alternative monitoring capabilities when VNFs do not expose data or control traffic or use proprietary and optimized protocols for inter VNF communication.



.. [1]
   ECOMP (Enhanced Control Orchestration, Management & Policy)
   Architecture White Paper
   (http://about.att.com/content/dam/snrdocs/ecomp.pdf)

.. [2]
   https://github.com/mbj4668/pyang

.. [3]
   Decision on which Chef Server instance associates with a VNF will be
   made on a case-by-case basis depending on VNF, access requirements,
   etc. and are outside the scope of this document. The specific
   criteria for this would involve considerations like connectivity and
   access required by the VNF, security, VNF topology and proprietary
   cookbooks.

.. [4]
   Recall that the Node Object **is required** to be identical across
   all VMs of a VNF invoked as part of the action except for the “name”.

.. [5]
   Decision on which Ansible Server to use may happen on a case-by-case
   basis depending on VNF, access requirements etc. and are outside the
   scope of this document. The specific criteria for this could involve
   considerations like connectivity and access required by the VNF,
   security, VNF topology and proprietary playbooks.

.. [6]
   Upstream elements must provide the appropriate FQDN in the request to
   ONAP for the desired action.

.. [7]
   Multiple ONAP actions may map to one playbook.

.. [8]
   This option is not currently supported in ONAP and it is currently
   under consideration.

.. [9]
   https://wiki.opnfv.org/display/PROJ/VNF+Event+Stream

.. [10]
   The “name” field is a mandatory field in a valid Chef Node Object
   JSON dictionary.

