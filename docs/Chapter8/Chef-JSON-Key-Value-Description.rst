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
| PushJobFlag    | This field indicates     |Mandatory| If set to "True",    |
|                | whether the VNF action   |         | ONAP will request a  |
|                | requires a push Job. Push|         | push job. Ignored    |
|                | job object will be       |         | otherwise.           |
|                | created by ONAP if       |         |                      |
|                | required.                |         |                      |
+----------------+--------------------------+---------+----------------------+
| CallbackCapable| This field indicates if  | Optional| If Chef cookbook is  |
|                | the chef-client run      |         | callback capable, VNF|
|                | invoked by push job      |         | owner is required to |
|                | corresponding to the VNF |         | set it to "True".    |
|                | action is capable of     |         | Ignored otherwise.   |
|                | posting results on a     |         |                      |
|                | callback URL.            |         |                      |
+----------------+--------------------------+---------+----------------------+
| GetOutputFlag  | Flag which indicates     |Mandatory| ONAP will retrieve   |
|                | whether ONAP should      |         | output from          |
|                | retrieve output generated|         | NodeObject attributes|
|                | in a chef-client run from|         | [‘PushJobOutput’] for|
|                | Node object attribute    |         | all nodes in NodeList|
|                | node[‘PushJobOutput’] for|         | if set to "True".    |
|                | this VNF action (e.g., in|         | Ignored otherwise.   |
|                | Audit).                  |         |                      |
+----------------+--------------------------+---------+----------------------+

Chef Template example:

.. code-block:: erb

 "Environment":{
      "name": "HAR",
      "description": "VNF Chef environment for HAR",
      "json_class": "Chef::Environment",
      "chef_type": "environment",
      "default_attributes": { },
      "override_attributes": {
            "Retry_Time":"50",
            "MemCache": "1024",
            "Database_IP":"10.10.1.5"
      },
 }
 }
 "Node": {
      "name" : "signal.network.com "
      "chef_type": "node",
      "json_class": "Chef::Node",
      "attributes": {
            "IPAddress1": "192.168.1.2",
            "IPAddress2":"135.16.162.5",
            "MyRole":"BE"
      },
      "override": {},
      "default": {},
      "normal":{},
      "automatic":{},
      "chef_environment" : "_default"
      "run_list": [ "configure_signal" ]
      },
      "NodeList":["node1.vnf_a.onap.com", "node2.vnf_a.onap.com"],
      "PushJobFlag": "True"
      "CallbackCapable":True
      "GetOutputFlag" : "False"
 }

The example JSON file provided by the VNF provider for each VNF action will be
turned into a template by ONAP, that can be updated with instance
specific values at run-time.

Some points worth noting regarding the JSON fields:

a. The JSON file must be created for each action for each VNF.

b. If a VNF action involves multiple endpoints (VMs) of a VNF, ONAP will
   replicate the "Node" JSON dictionary in the template and post it to
   each FQDN (i.e., endpoint) in the NodeList after setting the "name"
   field in the Node object to be the respective FQDN [#8.1.1]_. Hence, it
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

.. [#8.1.1]
   The "name" field is a mandatory field in a valid Chef Node Object
   JSON dictionary.
