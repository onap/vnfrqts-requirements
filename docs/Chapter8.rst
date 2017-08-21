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
|                                              | Request API: The Ansible Server must expose a REST endpoint that accepts a POST message to request execution of the playbook (e.g., https://ansible.test.att.com:8080). The POST request must be a JSON block as outlined in Table D2.                                                                                                                                       | Must       | D1060      |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
|                                              | When the Ansible server accepts an authenticated request to execute a playbook, it is required to send back an initial response indicating whether the request is accepted or rejected. The response must be a JSON Object with the key value pairs as described in Table D3.                                                                                                | Must       | D1070      |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------+------------+
|                                              | Result API: If the Ansible Server accepts a request to execute a playbook, it must make available status of the execution of the playbook at a Results REST endpoint indexed by the Id in the request in the form <url>?Id=<RequestId>&Type=GetResult where <url> is the URL used for submitting requests. For example, https://ansible.test.att.com?Id=10&Type=GetResult.   | Must       | D1080      |
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