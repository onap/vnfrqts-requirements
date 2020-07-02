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


VNF License Information Guidelines
----------------------------------

This Appendix describes the metadata to be supplied for VNF licenses.

1. General Information

Table C1 defines the required and optional fields for licenses.

Table C1. Required Fields for General Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

