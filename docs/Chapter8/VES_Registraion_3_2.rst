.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property, All rights reserved
.. Copyright 2017-2018 Huawei Technologies Co., Ltd.

.. _ves_event_registration_3_2:

Service: VES Event Registration 3.2
------------------------------------

+-----------------------------------------------------------------------------+
| **Legal Disclaimer**                                                        |
|                                                                             |
| Licensed under the Apache License, Version 2.0 (the "License"); you may not |
| use this file except in compliance with the License. You may obtain a copy  |
| of the License at                                                           |
|                                                                             |
| http://www.apache.org/licenses/LICENSE-2.0                                  |
|                                                                             |
| Unless required by applicable law or agreed to in writing, software         |
| distributed under the License is distributed on an "AS IS" BASIS, WITHOUT   |
| WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the    |
| License for the specific language governing permissions and limitations     |
| under the License.                                                          |
+-----------------------------------------------------------------------------+

+-------------------+--------------------------+
| Document Number   | VES Event Registration   |
+-------------------+--------------------------+
| Revision          | 3.2                      |
+-------------------+--------------------------+
| Revision Date     | December 10, 2018        |
+-------------------+--------------------------+
| Author            | Rich Erickson            |
+-------------------+--------------------------+

+-----------------+------------------------------+
| Contributors:   | **Shau-Ann Chang – AT&T**    |
|                 |                              |
|                 | **Min Chen – AT&T**          |
|                 |                              |
|                 | **Marge Hills – Nokia**      |
|                 |                              |
|                 | **Linda Horn – Nokia**       |
|                 |                              |
|                 | **Alok Gupta – AT&T**        |
|                 |                              |
|                 | **Zu Qiang – Ericsson**      |
|                 |                              |
|                 | **Paul Sulewski – Nokia**    |
+-----------------+------------------------------+

Introduction
^^^^^^^^^^^^

This document specifies a YAML format for the registration of VES
Events. The YAML format enables both human designers and applications to
parse and understand the fields that will be sent by event sources in
conjunction with specific types of events, which are identified by their
eventNames.

The semantics of the YAML format are easily extensible to accommodate
processing needs that may arise in the future. Among the types of
information specified in the YAML are field optionality, restrictions on
field values, and event handling recommendations and requirements.

This document should be read in conjunction with the VES Event Listener
service specification, which defines the Common Event Format and
introduces the concept of specific types of events, identified by
eventNames.

Audience
~~~~~~~~

This document is intended to support the following groups:

-  VNF Vendors

-  Service Provider (e.g., AT&T) Teams responsible for deploying VNFs
   within their infrastructure

VNF vendors will provide a YAML file to the Service Provider that
describes the events that their VNFs generate. Using the semantics and
syntax supported by YAML, vendors will indicate specific conditions that
may arise, and recommend actions that should be taken at specific
thresholds, or if specific conditions repeat within a specified time
interval.

Based on the vendor’s recommendations, the Service Provider may create
another YAML, which finalizes their engineering rules for the processing
of the vendor’s events. The Service Provider may alter the threshold
levels recommended by the vendor, and may modify and more clearly
specify actions that should be taken when specified conditions arise.
The Service Provided-created version of the YAML will be distributed to
Service Provider applications at design time.

Goal
~~~~

The goal of the YAML is to completely describe the processing of VNF
events in a way that can be compiled or interpreted by applications
across a Service Provider’s infrastructure.

Relation to the Common Event Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Common Event Format described in the VES Event Listener service
specification defines the structure of VES events including optional
fields that may be provided.

Specific eventNames registered by the YAML (e.g., an InvalidLicense
fault), may require that certain fields, which are optional in the
Common Event Format, be present when events with that eventName are
published. For example, a fault eventName which communicates an
‘InvalidLicense’ condition, may be registered to require that the
configured ‘licenseKey’ be provided as a name-value pair in the Common
Event Format’s ‘additionalFields’ structure, within the ‘faultFields’
block. Anytime an ‘InvalidLicense’ fault event is detected, designers,
applications and microservices across the Service Provider’s
infrastructure can count on that name-value pair being present.

The YAML registration may also restrict ranges or enumerations defined
in the Common Event Format. For example, eventSeverity is an enumerated
string within the Common Event Format with several values ranging from
‘NORMAL’ to ‘CRITICAL’. The YAML registration for a particular eventName
may require that it always be sent with eventSeverity set to a single
value (e.g., ‘MINOR’), or to a subset of the possible enumerated values
allowed by the Common Event Format (e.g., ‘MINOR’ or ‘NORMAL’).

Relation to Service Design and Creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Event registration for a VNF (or other event source) is provided to the
Service Provider’s Service Creation and Design Environment (e.g., ASDC)
as a set of two YAML files consisting of the vendor recommendation YAML
and (optionally) the final Service Provider YAML. These YAML files
describe all the eventNames that that VNF (or other event source)
generates.

Once their events are registered, the Service Creation and Design
Environment can then list the registered eventNames (e.g., as a drop
down list), for each VNF or other event source (e.g., a service), and
enable designers to study the YAML registrations for specific
eventNames. YAML registrations are both human readable and machine
readable.

The final Service Provider YAML is a type of Service Design and Creation
‘artifact’, which can be distributed to Service Provider applications at
design time: notably, to applications involved in the collection and
processing of VNF events. It can be parsed by those applications so they
can support the receipt and processing of VNF events, without the need
for any manual, VNF-specific development.

YAML Files
^^^^^^^^^^

YAML Specification Conformance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

YAML files should conform to version 1.2 of the YAML specification
available at: http://yaml.org/spec/1.2/spec.html.

Filename
~~~~~~~~

YAML file names should conform to the following naming convention:

    ``{AsdcModel}\_{AsdcModelType}\_{v#}.yml``

The ‘#’ should be replaced with the current numbered version of the
file.

‘ASDC’ is a reference to the Service Provider’s Service Design and
Creation environment. The AsdcModelType is an enumeration with several
values of which the following three are potentially relevant:

-  Service

-  Vnf

-  VfModule

The AsdcModel is the modelName of the specific modelType whose events
are being registered (e.g., the name of the specific VNF or service as
it appears in the the Service Design and Creation Environment).

For example:

-  ``vMRF\_Vnf\_v1.yml``

-  ``vMRF\_Service\_v1.yml``

-  ``vIsbcSsc\_VfModule\_v1.yml``

File Structure
~~~~~~~~~~~~~~

Each eventType is registered as a distinct YAML ‘document’.

YAML files consist of a series of YAML documents delimited by ‘---‘ and
‘…’ for example:

.. code-block:: ruby

   Some Ruby code.
   ---

   # Event Registration for eventName ‘name1’

   # details omitted

   ...

   ---

   # Event Registration for eventName ‘name2’

   # details omitted

   ...

   ---

   # Event Registration for eventName ‘name3’

   # details omitted

   ...

YAML Syntax and Semantics
^^^^^^^^^^^^^^^^^^^^^^^^^

YAML registration documents show each relevant VES Common Event Model
object and field (i.e., each element) for the eventName being
registered, including any extensible fields (e.g., specific name-value
pairs).

Qualifiers
~~~~~~~~~~

Each object or field name in the eventName being registered is followed
by a ‘qualifier’, which consists of a colon and two curly braces, for
example:

    ``“objectOrFieldName: { }”``

The curly braces contain meta-information about that object or field
name (also known as the ‘element’), such as whether it is required to be
present, what values it may have, what handling it should trigger, etc…

Semantics have been defined for the following types of meta-information
within the curly braces:

Action
++++++

The ‘action’ keyword may be applied to field values or to the event as a
whole. The ‘action’ keyword specifies a set of actions that should be
taken if a specified trigger occurs. For example, the ‘action’ keyword
may specify that a threshold crossing alert (i.e., tca) be generated,
and/or that a specific microservice handler be invoked, and/or that a
specific named-condition be asserted. In the Rules section of the YAML
file, tca’s and microservices may be defined on individual
named-conditions or on logical combinations of named-conditions.

The ‘action:’ keyword is followed by five values in square brackets. The
first two values communicate the trigger, and the last three values
communicate the actions to be taken if that trigger occurs:

1. The first value conveys the trigger level. If the field on which the
   action is defined reaches or passes through that level, then the
   trigger fires. If a specific level is not important to the
   recommended action, the ‘any’ keyword may be used as the first value.
   (Note: ‘any’ is often used when an action is defined on the ‘event’
   structure as a whole).

2. The second value indicates the direction of traversal of the level
   specified in the first value. The second value may be ‘up’, ‘down’,
   ‘at’ or ‘any’. ‘any’ is used if the direction of traversal is not
   important. ‘at’ implies that it traversed (or exactly attained) the
   trigger level but it doesn’t matter if the traversal was in the up
   direction or down direction. Note: If ‘up’, ‘down’ or ‘at’ are used,
   the implication is that the microservices processing the events
   within the service provider are maintaining state (e.g., to know that
   a measurement field traversed a trigger level in an ‘up’ direction,
   the microservice would have to know that the field was previously
   below the trigger level). When initially implementing support for
   YAML actions, a service provider may choose to use and interpret
   these keywords in a simpler way to eliminate the need to handle
   state. Specifically, they may choose to define and interpret all ‘up’
   guidance to mean ‘at the indicated trigger level or greater’, and
   they may choose to define and interpret all ‘down’ guidance to mean
   ‘at the indicated trigger level or lower’.

3. The third value optionally names the condition that has been attained
   when the triggers fires (e.g., ‘invalidLicence’ or
   ‘capacityExhaustion’). Named-conditions should be expressed in upper
   camel case with no underscores, hyphens or spaces. In the Rules
   section of the YAML file, named-conditions may be used to specify
   tca’s that should be generated and/or microservices that should be
   invoked. If it is not important to name a condition, then the keyword
   ‘null’ may be used as the third value.

4. The fourth value recommends a specific microservice (e.g., ‘rebootVm’
   or ‘rebuildVnf’) supported by the Service Provider, be invoked if the
   trigger is attained. Design time processing of the YAML by the
   service provider can use these directives to automatically establish
   policies and configure flows that need to be in place to support the
   recommended runtime behavior.

    If a vendor wants to recommend an action, it can either work with
    the service provider to identify and specify microservices that the
    service provider support, or, the vendor may simply indicate and
    recommend a generic microservice function by prefixing ‘RECO-’ in
    front of the microservice name, which should be expressed in upper
    camel case with no underscores, hyphens or spaces.

    The fourth value may also be set to ‘null’.

1. The fifth value third value indicates a specific threshold crossing
   alert (i.e., tca) that should be generated if the trigger occurs.
   This field may be omitted or provided as ‘null’.

    Tca’s should be indicated by their eventNames.

    When a tca is specified, a YAML registration for that tca eventName
    should be added to the event registrations within the YAML file.

Examples:

.. code-block:: yaml

   event: {
     action: [
       any, any, null, rebootVm
     ]
   }

    # whenever the above event occurs, the VM should be rebooted

   fieldname: {
     action: [ 80, up, null, null, tcaUpEventName ],
     action: [ 60, down, overcapacity, null ]
   }

    # when the value of fieldname crosses 80 in an up direction,
    # tcaUpEventName should be published; if the fieldname crosses 60
    # in a down direction an ‘overCapacity’ named-condition is asserted.

AggregationRole
+++++++++++++++

The ‘aggregationRole’ keyword is applied to the value keyword in a field
of a name-value pair.

AggregationRole may be set to one of the following:

-  cumulativeCounter

-  gauge

-  index

-  reference

“index” identifies a field as an index or a key for aggregation.

“reference” fields have values that typically do not change over
consecutive collection intervals.

“gauge” values may fluctuate from one collection interval to the next,
i.e., increase or decrease.

“cumulativeCounter” values keep incrementing regardless of collection
interval boundaries until they overflow, i.e., until they exceed a
maximum value specified by design. Typically, delta calculation is
needed based on two cumulativeCounter values over two consecutive
collection intervals.

If needed, the aggergationRole setting tells the receiving event
processor how to aggregate the extensible keyValuePair data. Data
aggregation may use a combination of ‘index’ and ‘reference’ data fields
as aggregation keys while applying aggregation formulas, such as
summation or average on the ‘gauge’ fields.

Example 1:

    Interpretation of the below: If additionalMeasurements is supplied,
    it must have key name1 and name1’s value should be interpreted as an
    index:

.. code-block:: yaml

    additionalMeasurements: {
      presence: optional, array: [
        {
          name: {presence: required},
          arrayOfFields: {
            presence: required, array: [
              {
                name: {presence: required, value: name1},
                 value: {presence: required, aggregationRole: index}
              }
            ]
          }
        }
      ]
    }

Example 2:

-  Let’s say a vnf wants to send the following ‘TunnelTraffic’ fields
       through a VES arrayOfFields structure (specifically through
       additionalMeasurements in the VES measurementField block):

+-----------------------------+---------------+----------------------+------------------------+-----------------------+
| Tunnel Name                 | Tunnel Type   | Total Output Bytes   | Total Output Packets   | Total Output Errors   |
+=============================+===============+======================+========================+=======================+
| ST6WA21CRS:TUNNEL-TE40018   | PRIMARY       | 2457205              | 21505                  | 0                     |
+-----------------------------+---------------+----------------------+------------------------+-----------------------+
| ST6WA21CRS:TUNNEL-TE1029    | PRIMARY       | 46677                | 220                    | 0                     |
+-----------------------------+---------------+----------------------+------------------------+-----------------------+
| ST6WA21CRS:TUNNEL-TE1028    | PRIMARY       | 80346                | 577                    | 0                     |
+-----------------------------+---------------+----------------------+------------------------+-----------------------+

-  Tunnel Name is an index, Tunnel Type is reference data and the other
       three columns are counters

-  The first three columns would be sent through VES as follows:

.. code-block:: yaml

    additionalMeasurements: {presence: required, array: [
      {
        name: {presence: required, value: TunnelTraffic},
        arrayOfFields: {presence: required, array: [
          {
             name: {presence: required, value: TunnelName},
             value: {presence: required, aggregationRole: index},
          },
          {
             name: {presence: required, value: TunnelType},
             value: {presence: required, aggregationRole: reference}
          },
          {
             name: {presence: required, value: TotalOutputBytes},
             value: {presence: required, aggregationRole: gauge, castTo:number }
          }
        ]}
      }
    ]}

Array
+++++

The ‘array’ keyword indicates that the element is an array; ‘array:’ is
following by square brackets which contain the elements of the array.
Note that unlike JSON itself, the YAML registration will explicitly
declare the array elements and will not communicate them anonymously.

Examples:

.. code-block:: yaml

    element: { array: [

      firstArrayElement: { },

      secondArrayElement: { }

    ]}

CastTo
++++++

The ‘castTo’ keyword is applied to ‘value’ keywords. It tells the
receiving event processor to cast (or interpret) the supplied value from
its standard VES datatype (typically a string) to some other datatype.
If not supplied the implication is the standard VES datatype applies.

A value may be castTo one and only one of the following data types:

-  boolean

-  integer

-  number (note: this supports decimal values as well as integral
       values)

-  string

Example:

.. code-block:: yaml

    fieldname: { value: [ x, y, z ], castTo: number } # only values ‘x’,
       ‘y’, or ‘z’ allowed

    # each must be cast to a number

.. code-block:: yaml

    additionalMeasurements: {presence: optional, array: [
      {
        name: {presence: required},
        arrayOfFields: {presence: required, array: [
          {
             name: {presence: required, value: name1},
             value: {presence: required, castTo: number}
          }
        ] }
      }
    ] }


**For another example, see the second example under AggregationRole.**

Comment
+++++++

The ‘comment’ keyword enables event registrations to communicate
additional information, in the form of a quoted string, to designers
consuming the event registration. Such additional information might
convey meaning, instructions or potential effects associated with
particular fields or with the event as a whole.

Examples:

.. code-block:: yaml

    fieldname: {
      range: [ 1, unbounded ],
      default: 5,
      comment: “needs further diagnosis; call the TAC”
    }

.. code-block:: yaml

    fieldname: {
      value: [ red, white, blue ],
      default: blue,
      comment: “red indicates degraded quality of service”
    }

.. code-block:: yaml

    event: {
      presence: required,
      comment: “this event only occurs in conditions when the
      ipq has stopped operating; manual reset may be required”,
      structure: { . . . }
    }

Default
+++++++

The ‘default’ keyword specifies a default field value. Note: the default
value must be within the range or enumeration of acceptable values.

Examples:

.. code-block:: yaml

    fieldname: { range: [ 1, unbounded ], default: 5 }

.. code-block:: yaml

    fieldname: { value: [ red, white, blue ], default: blue }


HeartbeatAction
++++++++++++++++

The ‘heartbeatAction’ keyword is provided on the ‘event’ objectName for
heartbeat events only. It provides design time guidance to the service
provider’s heartbeat processing applications (i.e., their watchdog
timers). The syntax and semantics of the ‘heartbeatAction’ keyword are
similar to the ‘action’ keyword except the trigger is specified by the
first field only instead of the first two fields. When the
‘heartbeatAction’ keyword is indicated, the first field is an integer
indicating the number of successively missed heartbeat events. Should
that trigger occur, the remaining fields have the same order, meaning
and optionality as those described for the ‘action’ keyword.

Examples:

.. code-block:: yaml

    event: { heartbeatAction: [ 3, vnfDown, RECO-rebootVnf, tcaEventName] }

    # whenever the above event occurs, a vnfDown condition is asserted
    # and the vnf should be rebooted, plus the indicated tca should be
    # generated.

keyValuePairString
++++++++++++++++++

The ‘keyValuePairString’ keyword describes the key-value pairs to be
communicated through a string (e.g., in the VES Syslog Fields
‘syslogSData’ or ‘additionalFields’ strings). This keyword takes three
parameters:

-  The first parameter specifies the character used to delimit (i.e., to
       separate) the key-value pairs. If a space is used as a delimiter,
       it should be communicated within single quotes as ‘ ‘; otherwise,
       the delimiter character should be provided without any quotes.

-  The second parameter specifies the characters used to separate the
       keys and values. If a space is used as a separator, it should be
       communicated within single quotes as ‘ ‘; otherwise, the
       separator character should be provided without any quotes.

-  The third parameter is a “sub-keyword” (i.e., it is used only within
       ‘keyValuePairString’) called ‘keyValuePairs: [ ]’. Within the
       square brackets, a list of ‘keyValuePair’ keywords can be
       provided as follows:

   -  Each ‘keyValuePair’ is a structure (used only within
          ‘keyValuePairs’) which has a ‘key’ and a ‘value’. Each
          ‘keyValuePair’, ‘key’ and ‘value’ may be decorated with any of
          the other keywords specified in this specification (e.g., with
          ‘presence’, ‘value’, ‘range’ and other keywords).

Examples:

-  The following specifies an additionalFields string which is stuffed
       with ‘key=value’ pairs delimited by the pipe (‘\|’) symbol as in
       (“key1=value1\|key2=value2\|key3=value3…”).

.. code-block:: yaml

    additionalFields: {
      presence: required, keyValuePairString: {\|, =, keyValuePairs: [
        keyValuePair: {
          presence: required, structure: {
            key: {presence: required, value: someKeyName},
            value: {presence: required, range: [0, 100]}
          }
        },
        keyValuePair: {
          presence: optional, structure: {
            key: {presence: required, value: someOtherKeyName},
            value: {presence: required, value [red, white, blue]}
          }
        }
      ]}
    }

Presence
+++++++++

The ‘presence’ keyword may be defined as ‘required’ or ‘optional’. If
not provided, the element is assumed to be ‘optional’.

Examples:

.. code-block:: yaml

    element: { presence: required } # element must be present

.. code-block:: yaml

    element: { presence: optional } # element is optional

.. code-block:: yaml

    element: { value: blue }
    # by omitting a presence definition, the element is assumed to be optional

Range
+++++++

The ‘range’ keyword applies to fields (i.e., simpleTypes); indicates the
value of the field is a number within a specified range of values from
low to high (inclusive of the indicated values). . ‘range:’ is followed
by two parameters in square brackets:

-  the first parameter conveys the minimum value

-  the second parameter conveys the maximum value or ‘unbounded’

The keyword ‘unbounded’ is supported to convey an unbounded upper limit.
Note that the range cannot override any restrictions defined in the VES
Common Event Format.

Examples:

.. code-block:: yaml

    fieldname: { range: [ 1, unbounded ] }

.. code-block:: yaml

    fieldname: { range: [ 0, 3.14 ] }

Structure
++++++++++

The ‘structure’ keyword indicates that the element is a complexType
(i.e., an object) and is followed by curly braces containing that
object.

Example:

.. code-block:: yaml

    objectName: {
      structure: {
        element1: { },
        element2: { },
        anotherObject: {
          structure: {
            element3: { },
            element4: { }
          }
        }
      }
    }

Units
+++++++

The ‘units’ qualifier may be applied to values provided in VES Common
Event Format extensible field structures. The ‘units’ qualifier
communicates the units (e.g., megabytes, seconds, Hz) that the value is
expressed in. Note: the ‘units’ should not contain any space characters
(e.g., use ‘numberOfPorts’ or ‘number\_of\_ports’ but not ‘number of
ports’).

Example:

.. code-block:: yaml

    field: {
      structure: {
      name: { value: pilotNumberPoolSize },
      value: { units: megabytes } # the value will be expressed in megabytes
      }
    }

Value
+++++++

The ‘value’ keyword applies to fields (i.e., simpleTypes); indicates a
single value or an enumeration of possible values. If not provided, it
is assumed the value will be determined at runtime. Note that the
declared value cannot be inconsistent with restrictions defined in the
VES Common Event Format (e.g., it cannot add an enumerated value to an
enumeration defined in the Common Event Format, but it can subset the
defined enumerations in the Common Event Format).

Values that are strings containing spaces should always be indicated in
single quotes.

Examples:

.. code-block:: yaml

    fieldname: { value: x } # the value is ‘x’

.. code-block:: yaml

    fieldname: { value: [ x, y, z ] }
    # the value is either ‘x’, ‘y’, or ‘z’

.. code-block:: yaml

    fieldname: { presence: required }
    # the value will be provided at runtime

.. code-block:: yaml

    fieldname: { value: ‘error state’ }
    # the value is the string within the single quotes

Rules
~~~~~

Rules Document
++++++++++++++

After all events have been defined, the YAML file may conclude with a
final YAML document delimited by ‘---‘ and ‘…’, which defines rules
based on the named ‘conditions’ asserted in action qualifiers in the
preceding event definitions. For example:

.. code-block:: yaml

    ---

    # Event Registration for eventName ‘name1’

    event: {
      presence: required,
      action: [any, any, A, null],
      structure: {# details omitted}
    }
    ...
    ---

    # Event Registration for eventName ‘name2’
    event: {
      presence: required,
      structure: {
        commonEventHeader: {
          presence: required,
          structure: {# details omitted}
        }
        measurements: {
          presence: required,
          structure: {
            cpuUsageArray: {
              presence: required,
              array: {
                cpuUsage: {
                  presence: required,
                  structure: {
                    cpuIdentifier: {
                      presence: required
                    },
                    percentUsage: {
                      presence: required,
                      action: [90, up, B, null]
                    }
                  }
                }
              }
            }, # details omitted
          }
        }
      }
    }
    ...
    ---

    # Rules

    rules: [
      # defined based on conditions ‘A’ and ‘B’ - details omitted
    ]

    ...

Rules Syntax and Semantics
++++++++++++++++++++++++++++

The YAML ‘rules’ document begins with the keyword ‘rules’ followed by a
colon and square brackets. Each rule is then defined within the square
brackets. Commas are used to separate rules.

Each rule is expressed as follows:

.. code-block:: text

    rule: {

      trigger: *logical expression in terms of conditions*,

      microservices: [ *microservice1, microservice2, microservice3…* ]

      alerts: [tcaE*ventName1, tcaEventName2, tcaEventName3…* ],

    }

Notes:

-  All referenced tcaEventNames should be defined within the YAML.

-  For information about microservices, see section 3.1.1 bullet number
   4.

-  At least one microservice or alert should be specified, and both
   microservices and alerts may be specified.

Simple Triggers
++++++++++++++++

The trigger is based on the named ‘conditions’ asserted in the action
qualifiers within the event definitions earlier in the YAML file. The
following logical operators are supported:

-  &: which is a logical AND

-  \|\|, which is a logical OR

In addition parentheses may be used to group expressions.

Example logical expression:

    (A & B) \|\| (C & D)

Where A, B, C and D are named conditions expressed earlier in the YAML
file.

Example rules definition:

.. code-block:: text

    rules: [
      rule: {
        trigger: A,
        alerts: [tcaEventName1],
        microservices: [rebootVm]
      },
      rule: {
        trigger: B \|\| (C & D),
        microservices: [scaleOut]
      }
    ]

Note: when microservices are defined in terms of multiple event
conditions, the designer should take care to consider whether the target
of the microservice is clear (e.g., which VNF or VM instance to perform
the action on). Future versions of this document may provide more
clarity.

Time Based Qualifiers
+++++++++++++++++++++++

Time based rules may be established by following any named condition
with a colon and curly braces. The time based rule is placed in the
curly braces as follows:

trigger: B:{3 times in 300 seconds}

This means that if condition B occurs 3 (or more) times in 300 seconds
(e.g., 5 minutes), the trigger fires.

More complex triggers can be created as follows:

trigger: B:{3 times in 300 seconds} \|\| (C & D:{2 times in 600
seconds}),

This means that the trigger fires if condition B occurs 3 (or more)
times in 5 minutes, OR, if condition D occurs 2 (or more) times in 10
minutes AND condition C is in effect.

PM Dictionary
~~~~~~~~~~~~~~

The Performance Management (PM) Dictionary is used by analytics
applications to interpret and process perf3gpp measurement information
from vendors, including measurement name, measurement family, measured
object class, description, collection method, value ranges, unit of
measure, triggering conditions and other information. The ultimate goal
is for analytics applications to dynamically process new and updated
measurements based on information in the PM Dictionary.

The PM dictionary is supplied by NF vendors in two parts:

-  *PM Dictionary Schema*: specifies meta-information about perf3gpp
   measurement events from that vendor. The meta-information is conveyed
   using standard meta-information keywords, and may be extended to
   include vendor-specific meta-information keywords. The PM Dictionary
   Schema may also convey a range of vendor-specific values for some of
   the keywords. Note: a vendor may provide multiple versions of the PM
   Dictionary Schema and refer to those versions from the PM Dictionary.

-  *PM Dictionary*: defines specific perf3gpp measurements sent by
   vendor NFs (each of which is compliant with a referenced PM
   Dictionary Schema).

PM Dictionary Schema Keywords
+++++++++++++++++++++++++++++++++++

The following is a list of standard PM Dictionary Schema Keywords:

pmDictionaryHeader Keywords:

+------------------+-----------------------------------------------------------------------------------------------------------------------------+-------------+-------------------+
| **Keyword**      | **Description**                                                                                                             | **M / O**   | **Example**       |
+==================+=============================================================================================================================+=============+===================+
| nfType           | NF type to whom this PM Dictionary applies. nfType is vendor defined and should match the string used in eventName.         | M           | gnb               |
+------------------+-----------------------------------------------------------------------------------------------------------------------------+-------------+-------------------+
| pmDefSchemaVsn   | Version of the PM Dictionary Schema used for this PM Dictionary. Schema versions are specified in the VES Specifications.   | M           | 1.0               |
+------------------+-----------------------------------------------------------------------------------------------------------------------------+-------------+-------------------+
| pmDefVsn         | Version of the PM Dictionary. Version is vendor defined.                                                                    | M           | 5G19\_1906\_002   |
+------------------+-----------------------------------------------------------------------------------------------------------------------------+-------------+-------------------+
| vendor           | Vendor of the NF type to whom this PM Dictionary applies.                                                                   | M           | Nokia             |
+------------------+-----------------------------------------------------------------------------------------------------------------------------+-------------+-------------------+

pmDictionaryMeasurements Keywords:

+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|     **Keyword**        |     **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |     **M / O**   |     **Example**                                                                                                                                                       |
+========================+===================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+=================+=======================================================================================================================================================================+
| iMeasInfoId            | Vendor defined integer identifier for measInfoId for efficiency in GPB.                                                                                                                                                                                                                                                                                                                                                                                                                                                           | O               | 2024                                                                                                                                                                  |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| iMeasType              | Vendor defined integer identifier for measType for efficiency in GPB.                                                                                                                                                                                                                                                                                                                                                                                                                                                             | O               | 2                                                                                                                                                                     |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measAdditionalFields   | Hashmap of vendor specific PM Dictionary fields in key value pair format                                                                                                                                                                                                                                                                                                                                                                                                                                                          | O               | measAggregationLevels                                                                                                                                                 |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measChangeType         | For the measLastChange, indicates the type of change made for this measurement. Valid values are added, modified or deleted. Deleted measurements may be kept in the PM Dictionary for one release or more or permanently for historical purposes, if desired.                                                                                                                                                                                                                                                                    | M               | added                                                                                                                                                                 |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measCollectionMethod   | Collection Method for the measurement. 3GPP-defined collection methods are CC, SI, DER and Gauge. Collection Methods for 3GPP-defined 4G measurements are specified in 3GPP TS 32.425 item b). Collection Methods for 3GPP-defined 5G measurements are specified in 3GPP TS 28.552 item c). The measCollectionMethod values supported by a vendor are specified in the PM Dictionary YAML using the “value” attribute and may include vendor-defined collection methods not specified by 3GPP; for example Average.               | M               | SI                                                                                                                                                                    |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measCondition          | Text description of the condition that causes the measurement to be updated. Conditions for 3GPP-defined 4G measurements are specified in 3GPP TS 32.425 item c). Conditions for 3GPP-defined 5G measurements are specified in 3GPP TS 28.552 item c). Vendors are free to augment or modify the 3GPP-provided conditions to more accurately describe their measurements as needed.                                                                                                                                               | M               | This measurement is obtained by sampling at a pre-defined interval, the number of users in RRC connected mode for each NR cell and then taking the arithmetic mean.   |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measDescription        | Text description of the purpose of the measurement, what information does the measurement provide. Descriptions for 3GPP-defined 4G measurements are specified in 3GPP TS 32.425 item a). Descriptions for 3GPP-defined 5G measurements are specified in 3GPP TS 28.552 item a). Vendors are free to augment or modify the 3GPP-provided descriptions to more accurately describe their measurements as needed.                                                                                                                   | M               | This measurement provides the mean number of users in RRC connected mode during each granularity period.                                                              |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measFamily             | Abbreviation for a family of measurements, in 3GPP format where specified, else vendor defined. Family name abbreviations for 3GPP-defined 4G measurements are specified in 3GPP TS 32.425 Section 3.1. Family name abbreviations for 3GPP-defined 5G measurements are specified in 3GPP TS 28.552 Section 3.4.                                                                                                                                                                                                                   | O               | RRC                                                                                                                                                                   |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measInfoId             | Name for a group of related measurements, in 3GPP format where specified, else vendor defined. Family names for 3GPP-defined 4G measurements are specified in 3GPP TS 32.425 Section 3.1. Family names for 3GPP-defined 5G measurements are specified in 3GPP TS 28.552 Section 3.4.                                                                                                                                                                                                                                              | O               | Radio Resource Control                                                                                                                                                |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measLastChange         | PM Dictionary version the last time this measurement was changed, added or deleted.                                                                                                                                                                                                                                                                                                                                                                                                                                               | M               | 5G18A\_1807\_003                                                                                                                                                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measObjClass           | Measurement Object Class. Object classes for 3GPP-defined 4G measurements are specified in 3GPP TS 32.425 item f). Object classes for 3GPP-defined 5G measurements are specified in 3GPP TS 28.552 item f). The measObjClass values supported by a vendor are specified in the PM Dictionary YAML using the “value” attribute and may include vendor-defined objects not specified by 3GPP; for example IPSEC.                                                                                                                    | M               | NRCellCU                                                                                                                                                              |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measResultRange        | Range for the measurement result. The range is specified as a comma separated list of discrete values or a range of values specified as minimum value-maximum value with no spaces. Result ranges for 3GPP-defined 4G measurements are specified in 3GPP TS 32.425 item d) if applicable. Result ranges for 3GPP-defined 5G measurements are specified in 3GPP TS 28.552 item d) if applicable.                                                                                                                                   | O               |                                                                                                                                                                       |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measResultType         | Data type of the measurement result. Result data types for 3GPP-defined 4G measurements are specified in 3GPP TS 32.425 item d). Result data types for 3GPP-defined 5G measurements are specified in 3GPP TS 28.552 item d). The measResultType values supported by a vendor are specified in the PM Dictionary YAML using the “value” attribute and may include vendor-defined data types not specified by 3GPP; for example boolean.                                                                                            | M               |                                                                                                                                                                       |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measResultUnits        | Unit of measure for the result; e.g. milliseconds, bytes, kilobytes, packets, number. Unit of measure for 3GPP-defined 4G measurements are specified in 3GPP TS 32.425 item d) if applicable. Unit of measure for 3GPP-defined 5G measurements are specified in 3GPP TS 28.552 item d) if applicable. The measResultsUnits values supported by a vendor are specified in the PM Dictionary YAML using the “value” attribute and may include vendor-defined units of measure not specified by 3GPP; for example ethernet frames.   | O               |                                                                                                                                                                       |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| measType               | Measurement name used in PM file, in 3GPP format where specified, else vendor defined. Names for 3GPP-defined 4G measurements are specified in 3GPP TS 32.425 item e). Names for 3GPP-defined 5G measurements are specified in 3GPP TS 28.552 item e). Vendor defined names are preceded with VS.                                                                                                                                                                                                                                 | M               | RRC.ConnMean                                                                                                                                                          |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sMeasInfoId            | Vendor defined string identifier for measInfoId; could be the same as measInfoId or shortened version like measFamily for efficiency in GPB.                                                                                                                                                                                                                                                                                                                                                                                      | O               | RRC                                                                                                                                                                   |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sMeasType              | Vendor defined string identifier for measType; could be the same as measType or it could be a shortened version for efficiency in GPB.                                                                                                                                                                                                                                                                                                                                                                                            | O               | RRC.ConnMean                                                                                                                                                          |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

PM Dictionary Schema Example
++++++++++++++++++++++++++++

The following is a sample PM Dictionary Schema:


# PM Dictionary schema specifying and describing the meta information
used to define perf3gpp measurements in the PM Dictionary

.. code-block:: text

    pmDictionary: {
      presence: required,
      structure: {
        pmDictionaryHeader: {
          presence: required,
          structure: {
            nfType: {
              presence: required,
              comment: "NF type; should match the string used in the perf3gpp eventName"
            },
            pmDefSchemaVsn: {
              presence: required,
              value: 1.0,
              comment: "PM Dictionary Schema Version"
            },
            pmDefVsn: {
              presence: required,
              comment: "vendor-defined PM Dictionary version"
            },
            vendor: {
              presence: required,
              comment: "vendor of the NF type"
            }
          }
        },
        pmDictionaryMeasurements: {
          presence: required,
          array: [
            iMeasInfoId: {
              presence: required,
              comment: "vendor-defined integer measurement group identifier"
            },
            iMeasType: {
              presence: required,
              comment: "vendor-defined integer identifier for the measType; must be combined with measInfoId to identify a specific measurement."
            },
            measAdditionalFields: {
              presence: required,
              comment: "vendor-specific PM Dictionary fields",
              array: [
                keyValuePair: {
                  presence: required,
                  structure: {
                    key: {
                      presence: required,
                      value: measAggregationLevels,
                      comment:"Nokia-specific field"
                    },
                    value: {
                      presence: required,
                      value: [NGBTS, NGCELL, IPNO, IPSEC, ETHIF],
                      comment: "list of one or more aggregation levels that Nokia recommends for this measurement; for example, if the value is NGBTS NGCELL, then Nokia recommends this measurement be aggregated on the 5G BTS level and the 5G Cell level"
                    }
                  }
                }
              ]
            },
            measChangeType: {
              presence: required,
              value: [added, modified, deleted],
              comment: "indicates the type of change that occurred during measLastChange"
            },
            measCollectionMethod: {
              presence: required,
              value: [CC, SI, DER, Gauge, Average],
              comment: "the measurement collection method; CC, SI, DER and Gauge are as defined in 3GPP; average contains the average value of the measurement during the granularity period"
            },
            measCondition: {
              presence: required,
              comment: "description of the condition causing the measurement"
            },
            measDescription: {
              presence: required,
              comment: "description of the measurement information and purpose"
            },
            measFamily: {
              presence: required,
              comment: "abbreviation for a family of measurements, in 3GPP format,or vendor defined"
            },
            measInfoId: {
              presence: required,
              comment: "name for a group of related measurements in 3GPP format or vendor defined"
            },
            measLastChange: {
              presence: required,
              comment: "version of the PM Dictionary the last time this measurement was added, modified or deleted"
            },
            measObjClass: {
              presence: required,
              value: [NGBTS, NGCELL, IPNO, IPSEC, ETHIF],
              comment: "measurement object class"
            },
            measResultRange: {
              presence: optional,
              comment: "range of the measurement result; only necessary when the range is smaller than the full range of the data type"
            },
            measResultType: {
              presence: required,
              value: [float, unit32, uint64],
              comment: "data type of the measurement result"
            },
            measResultUnits: {
              presence: required,
              value: [ seconds, minutes, nanoseconds, microseconds, dB, number, kilobytes, bytes, ethernetFrames, packets, users],
              comment: "units of measure for the measurement result"
            },
            measType: {
              presence: required,
              comment: "measurement name in 3GPP or vendor-specific format; vendor specific names are preceded with VS"
            }
          ]
        }
      }
    }

...

PM Dictionary Example
+++++++++++++++++++++

The following is a sample PM Dictionary in both bracketed and
indent-style YAML formats


# PM Dictionary perf3gpp measurements for the Nokia gnb NF (bracket
style yaml)

.. code-block:: yaml


    pmDictionary: {

      pmDictionaryHeader: {
        nfType: gnb,
        pmDefSchemaVsn: 1.0,
        pmDefVsn: 5G19\_1906\_002,
        vendor: Nokia },
      pmDictionaryMeasurements: [
      {
        iMeasInfoId: 2204,
        iMeasType: 1,
        measAdditionalFields: { measAggregationLevels: "NGBTS NGCELL"},
        measCollectionMethod: CC,
        measCondition: "This measurement is updated when X2AP: SgNB Modification Required message is sent to MeNB with the SCG Change Indication set as PSCellChange.",
        measDescription: "This counter indicates the number of intra gNB intra frequency PSCell change attempts.",
        measFamily: NINFC,
        measInfoId: "NR Intra Frequency PSCell Change",
        measLastChange: 5G18A\_1807\_003,
        measObjClass: NGCELL,
        measResultRange: 0..4096,
        measResultType: integer,
        measResultUnits: number,
        measType: VS.NINFC.IntraFrPscelChAttempt},
      {
        iMeasInfoId: 2204,
        iMeasType: 2,
        measAdditionalFields: {measAggregationLevels: "NGBTS NGCELL"},
        measCollectionMethod: CC,
        measCondition: "This measurement is updated when the TDCoverall timer has elapsed before gNB receives the X2AP: SgNB Modification Confirm message.",
        measDescription: "This measurement the number of intra gNB intra frequency PSCell change failures due to TDCoverall timer expiry.",
        measFamily: NINFC,
        measInfoId: "NR Intra Frequency PSCell Change",
        measLastChange: 5G18A\_1807\_003,
        measObjClass: NGCELL,
        measResultRange: 0..4096,
        measResultType: integer,
        measResultUnits: number,
        measType: VS.NINFC.IntraFrPscelChFailTdcExp},
      {
        iMeasInfoId: 2204,
        iMeasType: 3,
        measAdditionalFields: { measAggregationLevels: "NGBTS NGCELL"},
        measCondition: "This measurement is updated when MeNB replies to X2AP: SgNB Modification Required message with the X2AP: SgNB Modification Refuse message.",
        measCollectionMethod: CC,
        measDescription: "This counter indicates the number of intra gNB intra frequency PSCell change failures due to MeNB refusal.",
        measFamily: NINFC,
        measInfoId: "NR Intra Frequency PSCell Change",
        measLastChange: 5G19\_1906\_002,
        measObjClass: NGCELL,
        measResultRange: 0..4096,
        measResultType: integer,
        measResultUnits: number,
        measType: VS.NINFC.IntraFrPscelChFailMenbRef }
      ]
    }


.. code-block:: yaml

    # PM Dictionary perf3gpp measurements for the Nokia gnb NF (indented
    style yaml)

    pmDictionary:

      pmDictionaryHeader:

      nfType: gnb

      pmDefSchemaVsn: 1.0

      pmDefVsn: 5G19\_1906\_002

      vendor: Nokia

      pmDictionaryMeasurements:

      -

      iMeasInfoId: 2204

      iMeasType: 1

      measAdditionalFields:

      measAggregationLevels: "NGBTS NGCELL"

      measCollectionMethod: CC

      measCondition: "This measurement is updated when X2AP: SgNB Modification Required message is sent to MeNB with the SCG Change Indication set as PSCellChange."

      measDescription: "This counter indicates the number of intra gNB intra frequency PSCell change attempts."

      measFamily: NINFC

      measInfoId: "NR Intra Frequency PSCell Change"

      measLastChange: 5G18A\_1807\_003

      measObjClass: NGCELL

      measResultRange: "0..4096"

      measResultType: integer

      measResultUnits: number

      measType: VS.NINFC.IntraFrPscelChAttempt

      -

      iMeasInfoId: 2204

      iMeasType: 2

      measAdditionalFields:

      measAggregationLevels: "NGBTS NGCELL"

      measCollectionMethod: CC

      measCondition: "This measurement is updated when the TDCoverall timer has elapsed before gNB receives the X2AP: SgNB Modification Confirm message."

      measDescription: "This measurement the number of intra gNB intra frequency PSCell change failures due to TDCoverall timer expiry."

      measFamily: NINFC

      measInfoId: "NR Intra Frequency PSCell Change"

      measLastChange: 5G18A\_1807\_003

      measObjClass: NGCELL

      measResultRange: "0..4096"

      measResultType: integer

      measResultUnits: number

      measType: VS.NINFC.IntraFrPscelChFailTdcExp

      -

      iMeasInfoId: 2204

      iMeasType: 3

      measAdditionalFields:

      measAggregationLevels: "NGBTS NGCELL"

      measCollectionMethod: CC

      measCondition: "This measurement is updated when MeNB replies to X2AP: SgNB Modification Required message with the X2AP: SgNB Modification Refuse message."

      measDescription: "This counter indicates the number of intra gNB intra frequency PSCell change failures due to MeNB refusal."

      measFamily: NINFC

      measInfoId: "NR Intra Frequency PSCell Change"

      measLastChange: 5G19\_1906\_002

      measObjClass: NGCELL

      measResultRange: "0..4096"

      measResultType: integer

      measResultUnits: number

      measType: VS.NINFC.IntraFrPscelChFailMenbRef


FM Meta Data
~~~~~~~~~~~~~

FM Meta Data enables vendors to provide meta information about FM events
using a set of standard keywords. FM Meta Data is conveyed in the YAML
event registration using the YAML Comment qualifier.

The FM Meta Data section is optional. FM Meta Data includes Alarm Meta
Data and Fault Meta Data:

-  Alarm Meta Data, if provided, shall be placed in the YAML comments
   qualifier at the top of the event registration for the alarm.

-  Fault Meta Data, if provided, shall be placed in the YAML comments
   qualifier of faultFields.alarmAdditionalInformation within each
   alarm.

FM Meta Data keywords must be provided in ‘hash format’ as Keyword:
Value. Values containing whitespace must be enclosed in single quotes.
Successive keywords must be separated by commas. These conventions will
make machine processing of FM Meta Data Keywords easier to perform.

Alarm Meta Data Keywords
++++++++++++++++++++++++++++

The following is a list of standard Alarm Meta Data Keywords. Note: the
keywords are in CAPS so they can be easily found within the YAML
comments. R / O refers to recommended / optional.

+---------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Keyword**               | **R / O**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                               |
+===========================+=============+===============================================================================================================================================================================================================================================================================================================================================================================================================================================+
| ALARM ID                  | O           | Gives a unique numerical Identifier for the alarm.                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ALARM NAME                | R           | Gives a short, concise meaningful name of the alarm in camel format with no spaces, for example baseStationSynchronizationProblem. Note: Alarm Name meta data must match the name used in alarmCondition in the faultFields of the VES Fault Event to provide the cross reference between the Fault Event and its associated FM Meta Data.                                                                                                    |
+---------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ALARM DESCRIPTION         | R           | Provides a descriptive meaning of the alarm condition. This is intended to be read by an operator to give an idea of what happened.                                                                                                                                                                                                                                                                                                           |
+---------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ALARM EFFECT              | R           | Provides a description of the consequences when this alarm condition occurs. This is intended to be read by an operator to give a sense of the effects, consequences, and other impacted areas of the system.                                                                                                                                                                                                                                 |
+---------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ADDITIONAL TEXT           | O           | This field Contains further information on the alarm in free form text.See ITU-T Recommendation X.733 clause 8.1.2.13.                                                                                                                                                                                                                                                                                                                        |
+---------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ASSOCIATED FAULTS         | O           | Indicates the associated faults that triggered this alarm. List of Fault IDs associated with the alarm which can be cross indexed against a vendor provided fault information.                                                                                                                                                                                                                                                                |
+---------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CLEARING TYPE             | R           | Indicates whether the alarm is automatically or manually cleared. Valid values are Automatic or Manual.                                                                                                                                                                                                                                                                                                                                       |
+---------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EVENT TYPE                | O           | Indicates the type of alarm. Event Types are found in 3GPP TS 32.111 Annex A. The types are: Communications Alarm, Processing Error Alarm, Environmental Alarm, Quality of Service Alarm, Equipment Alarm, Integrity Violation, Operational Violation, Physical Violation, Security Service or Mechanism Violation, or Time Domain Violation. Note that eventCategory in the faultFields of the VES Fault Event may contain the event type.   |
+---------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MANAGED OBJECT CLASSES    | R           | Indicates the list of possible managed object classes (MOCs) associated with this alarm. Note that *eventSourceType* in the *faultFields* of the VES Fault Event contains the specific MOC against which the particular alarm occurrence was raised.                                                                                                                                                                                          |
+---------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PROBABLE CAUSE            | O           | Provides the probable cause qualifier for the alarm. Probable causes are found in 3GPP TS 32.111 Annex B, drawn from ITU-T M.3100 and from ITU-T Recommendation X.721, X.733, and X.736.                                                                                                                                                                                                                                                      |
+---------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PROPOSED REPAIR ACTIONS   | R           | Indicates proposed repair actions. May be used to provide recovery instructions to the operator in free form text.                                                                                                                                                                                                                                                                                                                            |
+---------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Fault Meta Data Keywords
+++++++++++++++++++++++++

The following is a list of standard Fault Meta Data Keywords. Note: the
keywords are in CAPS so they can be easily found within the YAML
comments. R / O refers to recommended / optional.

+---------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Keyword**               | **R / O**   | **Description**                                                                                                                                                                                       |
+===========================+=============+=======================================================================================================================================================================================================+
| FAULT ID                  | O           | Gives a unique numerical Identifier for the fault.                                                                                                                                                    |
+---------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FAULT NAME                | O           | Gives a short name for the fault.                                                                                                                                                                     |
+---------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FAULT DESCRIPTION         | O           | Provides a descriptive meaning of the fault condition. This is intended to be read by an operator to give an idea of what happened.                                                                   |
+---------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FAULT EFFECT              | O           | Provides a description of the consequences when this fault occurs. This is intended to be read by an operator to give a sense of the effects, consequences, and other impacted areas of the system.   |
+---------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PROPOSED REPAIR ACTIONS   | O           | Indicates proposed repair actions. May be used to provide recovery instructions to the operator in free form text..                                                                                   |
+---------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ADDITIONAL TEXT           | O           | Contains further information on the fault in free form text. See ITU-T Recommendation X.733 clause 8.1.2.13.                                                                                          |
+---------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

FM Meta Data Example
+++++++++++++++++++++

The following is a snippet of a fault event registration showing use of
the FM Meta Data keywords. Note: it is recommended the information be
conveyed in a human readable form similar to the example below:

.. code-block:: text

    event: {

      presence: required,

      action: {any, any, baseStationSynchronizationProblem,
    RECO-ContactNokiaTechnicalSupport},

      comment: "

        ALARM NAME: baseStationSynchronizationProblem,

        ALARM ID: 7108,

        ALARM DESCRIPTION: 'A fault has occurred in the base station
    synchronization. For example: the base station reference clock signal is
    lost or is unstable or inaccurate.',

        ALARM EFFECT: 'The effect of the fault on the functioning of the network element depends on the fault id raised. See FAULT EFFECT below.',

        MANAGED OBJECT CLASSES: NRBTS,

        EVENT TYPE: 'Equipment Alarm',

        PROBABLE CAUSE: 'Timing Problem',

        PROPOSED REPAIR ACTIONS: 'See PROPOSED REPAIR ACTIONS for the underlying fault under alarmAdditionalInformation.',

        ASSOCIATED FAULTS: 9, 1818,

        CLEARING TYPE: Automatic

      ",

    structure: {

      commonEventHeader: {presence: required, structure: {

      version: {presence: required, value: 3.0},

      domain: {presence: required, value: fault},

      eventName: {presence: required, value:
    Fault\_gnb-Nokia\_baseStationSynchronizationProblem},

      eventId: {presence: required},

      sourceName: {presence: required},

      reportingEntityName: {presence: required},

      priority: {presence: required},

      startEpochMicrosec: {presence: required},

      lastEpochMicrosec: {presence: required},

      timeZoneOffset: {presence: required},

      sequence: {presence: required}

      }},

      faultFields: {presence: required, structure: {

      faultFieldsVersion: {presence: required, value: 3.0},

      eventCategory: {presence: optional, comment: "Equipment Alarm"},

      alarmCondition: {presence: required, value: 'baseStationSynchronizationProblem'},

      eventSourceType: {presence: required},

      alarminterfaceA: {presence: required},

      specificProblem: {presence: required},

      eventSeverity: {presence: required, value: [MINOR, NORMAL]},

      nfStatus: {default: Active},

      alarmAdditionalInformation: {presence: required, array: [

      keyValuePair: {

        presence: required,

        structure: {

         key: {presence: required, value: faultId},

         value: {presence: required}

       },

      comment: "

        FAULT ID: 9,

        FAULT NAME: 'BTS time not corrected',

        FAULT DESCRIPTION: 'The reference frequency that the BTS master clock
    receives has changed by about 200 ppb or more (which equals the change
    magnitude of 204 DAC steps or more (with 12bit DAC)) during the
    measurement period, compared to the BTS master clock frequency.

       Causes can be:

         1. The reference frequency …..

         2. The reference frequency fluctuates …',

       FAULT EFFECT: 'This fault does not immediately affect the operations of the BTS, but it is a notification …',

       PROPOSED REPAIR ACTION: 'access the ….follow the instructions below:

         1. In case of a fault in the transmission network synchronization, …

         2. If the basic accuracy of the signal used for synch is correct…

         3. In case of a BTS equipment fault, the location might be:

         4. After the fault situation has been cleared, ….',

       FAULT ID: 1818,

       FAULT NAME: 'BTS master clock tuning failure',

       FAULT DESCRIPTON: 'Master clock frequency is tuned to within 5% of its
    minimum or maximum tuning limit.',

       FAULT EFFECT: 'The BTS can operate properly for months …'

       Effects in Frequency Synchronization mode: …

       Effects in Phase Synchronization mode: ….',

       PROPOSED REPAIR ACTION: 'Perform the steps below in the listed order
    until the fault disappears.

       Not tracking satellites:

        1. The most common reason ….

        2. There might be a malfunction in the GPS receiver. Perform a (remote)power reset for the GPS receiver.

        3. There might be a HW fault in the GPS receiver. Check the operation
    and change the GPS module, if needed.'

      "

      },

       keyValuePair: {

         presence: required,

         structure: {

           key: {presence: required, value: alarmId},

           value: {presence: required}

        }},

        keyValuePair: {

         presence: required,

         structure: {

            key: {presence: required, value: 'application additional information fields'},

            value: {presence: optional}

         }}

      ]}

    }}

    }

    }

YAML Examples
^^^^^^^^^^^^^

An example YAML file is provided below which registers some events for a
hypothetical VNF. Note: some of the lines have been manually
wrapped/indented to make it easier to read. Please ignore the section
breaks that interrupt this single file; they were added to make it
easier to rapidly find examples of different types of events.

Fault
~~~~~~

.. code-block:: yaml

    # registration for Fault\_vMrf\_alarm003

    # Constants: the values of domain, eventName, priority, vfstatus

    # , version, alarmCondition, eventSeverity, eventSourceType,

    # faultFieldsVersion, specificProblem,

    # Variables (to be supplied at runtime) include: eventId,
    lastEpochMicrosec,

    # reportingEntityId, reportingEntityName, sequence, sourceId,
    sourceName,

    # startEpochMicrosec

    event: {presence: required, action: [ any, any, alarm003,
    RECO-rebuildVnf ],

    structure: {

    commonEventHeader: {presence: required, structure: {

    domain: {presence: required, value: fault},

    eventName: {presence: required, value: Fault\_vMrf\_alarm003},

    eventId: {presence: required},

    nfNamingCode: {value: mrfx},

    priority: {presence: required, value: Medium},

    reportingEntityId: {presence: required},

    reportingEntityName: {presence: required},

    sequence: {presence: required},

    sourceId: {presence: required},

    sourceName: {presence: required},

    startEpochMicrosec: {presence: required},

    lastEpochMicrosec: {presence: required},

    version: {presence: required, value: 3.0}

    }},

    faultFields: {presence: required, structure: {

    alarmCondition: {presence: required, value: alarm003},

    eventSeverity: {presence: required, value: MAJOR},

    eventSourceType: {presence: required, value: virtualNetworkFunction},

    faultFieldsVersion: {presence: required, value: 2.0},

    specificProblem: {presence: required, value: "Configuration file was
    corrupt or

    not present"},

    vfStatus: {presence: required, value: "Requesting Termination"}

    }}

    }}


.. code-block:: yaml

    # registration for clearing Fault\_vMrf\_alarm003Cleared

    # Constants: the values of domain, eventName, priority,

    # , version, alarmCondition, eventSeverity, eventSourceType,

    # faultFieldsVersion, specificProblem,

    # Variables (to be supplied at runtime) include: eventId,
    lastEpochMicrosec,

    # reportingEntityId, reportingEntityName, sequence, sourceId,

    # sourceName, startEpochMicrosec, vfStatus

    event: {presence: required, action: [ any, any, alarm003, Clear ],
    structure: {

    commonEventHeader: {presence: required, structure: {

    domain: {presence: required, value: fault},

    eventName: {presence: required, value: Fault\_vMrf\_alarm003Cleared},

    eventId: {presence: required},

    nfNamingCode: {value: mrfx},

    priority: {presence: required, value: Medium},

    reportingEntityId: {presence: required},

    reportingEntityName: {presence: required},

    sequence: {presence: required},

    sourceId: {presence: required},

    sourceName: {presence: required},

    startEpochMicrosec: {presence: required},

    lastEpochMicrosec: {presence: required},

    version: {presence: required, value: 3.0}

    }},

    faultFields: {presence: required, structure: {

    alarmCondition: {presence: required, value: alarm003},

    eventSeverity: {presence: required, value: NORMAL},

    eventSourceType: {presence: required, value: virtualNetworkFunction},

    faultFieldsVersion: {presence: required, value: 2.0},

    specificProblem: {presence: required, value: "Valid configuration file
    found"},

    vfStatus: {presence: required, value: "Requesting Termination"}

    }}

    }}

Heartbeat
~~~~~~~~~~

.. code-block:: yaml

    # registration for Heartbeat\_vMRF

    # Constants: the values of domain, eventName, priority, version

    # Variables (to be supplied at runtime) include: eventId,
    lastEpochMicrosec,

    # reportingEntityId, reportingEntityName, sequence, sourceId,
    sourceName,

    # startEpochMicrosec

    event: {presence: required, heartbeatAction: [3, vnfDown,
    RECO-rebuildVnf],

    structure: {

    commonEventHeader: {presence: required, structure: {

    domain: {presence: required, value: heartbeat},

    eventName: {presence: required, value: Heartbeat\_vMrf},

    eventId: {presence: required},

    nfNamingCode: {value: mrfx},

    priority: {presence: required, value: Normal},

    reportingEntityId: {presence: required},

    reportingEntityName: {presence: required},

    sequence: {presence: required},

    sourceId: {presence: required},

    sourceName: {presence: required},

    startEpochMicrosec: {presence: required},

    lastEpochMicrosec: {presence: required},

    version: {presence: required, value: 3.0}

    }},

    heartbeatFields: {presence: optional, structure:{

            heartbeatFieldsVersion: {presence: required, value: 1.0},

            heartbeatInterval: {presence: required, range: [ 15, 300 ],
    default: 60 }

    }}

    }}


Measurements
~~~~~~~~~~~~~

.. code-block:: yaml

    # registration for Mfvs\_vMRF

    # Constants: the values of domain, eventName, priority, version,

    # measurementFieldsVersion,
    additionalMeasurements.namedArrayOfFields.name,

    # Variables (to be supplied at runtime) include: eventId,
    reportingEntityName, sequence,

    # sourceName, start/lastEpochMicrosec, measurementInterval,

    # concurrentSessions, requestRate, numberOfMediaPortsInUse,

    # cpuUsageArray.cpuUsage,cpuUsage.cpuIdentifier, cpuUsage.percentUsage,

    # additionalMeasurements.namedArrayOfFields.arrayOfFields,

    # vNicPerformance.receivedOctetsAccumulated,

    # vNicPerformance.transmittedOctetsAccumulated,

    # vNicPerformance.receivedTotalPacketsAccumulated,

    # vNicPerformance.transmittedTotalPacketsAccumulated,

    # vNicPerformance.vNicIdentifier, vNicPerformance.receivedOctetsDelta,

    # vNicPerformance.receivedTotalPacketsDelta,

    # vNicPerformance.transmittedOctetsDelta,

    # vNicPerformance.transmittedTotalPacketsDelta,

    # vNicPerformance.valuesAreSuspect, memoryUsageArray.memoryUsage,

    # memoryUsage.memoryConfigured, memoryUsage.vmIdentifier,

    # memoryUsage.memoryUsed, memoryUsage.memoryFree

    event: {presence: required, structure: {

    commonEventHeader: {presence: required, structure: {

    domain: {presence: required, value: measurementsForVfScaling},

    eventName: {presence: required, value: Mfvs\_vMrf},

    eventId: {presence: required},

    nfNamingCode: {value: mrfx},

    priority: {presence: required, value: Normal},

    reportingEntityId: {presence: required},

    reportingEntityName: {presence: required},

    sequence: {presence: required},

    sourceId: {presence: required},

    sourceName: {presence: required},

    startEpochMicrosec: {presence: required},

    lastEpochMicrosec: {presence: required},

    version: {presence: required, value: 3.0}

    }},

    measurementsForVfScalingFields: {presence: required, structure: {

    measurementFieldsVersion: {presence: required, value: 2.0},

    measurementInterval: {presence: required, range: [ 60, 3600 ], default:
    300},

    concurrentSessions: {presence: required, range: [ 0, 100000 ]},

    requestRate: {presence: required, range: [ 0, 100000 ]},

    numberOfMediaPortsInUse: {presence: required, range: [ 0, 100000 ]},

    cpuUsageArray: {presence: required, array: [

    cpuUsage: {presence: required, structure: {

    cpuIdentifier: {presence: required},

    percentUsage: {presence: required, range: [ 0, 100 ],

    action: [80, up, CpuUsageHigh, RECO-scaleOut],

    action: [10, down, CpuUsageLow, RECO-scaleIn]}

    }}

    ]},

    memoryUsageArray: {presence: required, array: [

    memoryUsage: {presence: required, structure: {

    memoryConfigured: {presence: required, value: 33554432},

    memoryFree: {presence: required, range: [ 0, 33554432 ],

    action: [100, down, FreeMemLow, RECO-scaleOut],

    action: [30198989, up, FreeMemHigh, RECO-scaleIn]},

    memoryUsed: {presence: required, range: [ 0, 33554432 ]},

    vmIdentifier: {presence: required}

    }}

    ]},

    additionalMeasurements: {presence: required, array: [

    namedArrayOfFields: {presence: required, structure: {

    name: {presence: required, value: licenseUsage},

    arrayOfFields: {presence: required, array: [

    field: {presence: required, structure: {

    name: {presence: required, value: G711AudioPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: G729AudioPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: G722AudioPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: AMRAudioPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: AMRWBAudioPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: OpusAudioPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: H263VideoPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: H264NonHCVideoPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: H264HCVideoPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: MPEG4VideoPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: VP8NonHCVideoPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: VP8HCVideoPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: PLC},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: AEC},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: NR},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: NG},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: NLD},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: G711FaxPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: T38FaxPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: RFactor},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: T140TextPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: EVSAudioPort},

    value: {presence: required, range: [ 0, 100000 ],

    units: numberOfPorts }

    }}

    ]}

    }},

    namedArrayOfFields: {presence: required, structure: {

    name: {presence: required, value: mediaCoreUtilization},

    arrayOfFields: {presence: required, array: [

    field: {presence: required, structure: {

    name: {presence: required, value: actualAvgAudio},

    value: {presence: required, range: [ 0, 255 ],

    action: [80, up, AudioCoreUsageHigh, RECO-scaleOut],

    action: [10, down, AudioCoreUsageLow, RECO-scaleIn]}

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: modelAvgAudio},

    value: {presence: required, range: [ 0, 100 ],

    action: [80, up, AudioCoreUsageHigh, RECO-scaleOut],

    action: [10, down, AudioCoreUsageLow, RECO-scaleIn]}

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: actualMaxAudio},

    value: {presence: required, range: [ 0, 255 ]}

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: modelMaxAudio},

    value: {presence: required, range: [ 0, 100 ]}

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: actualAvgVideo},

    value: {presence: required, range: [ 0, 255 ],

    action: [80, up, VideoCoreUsageHigh, RECO-scaleOut],

    action: [10, down, VideoCoreUsageLow, RECO-scaleIn]}

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: modelAvgVideo},

    value: {presence: required, range: [ 0, 100 ],

    action: [80, up, VideoCoreUsageHigh, RECO-scaleOut],

    action: [10, down, VideoCoreUsageLow, RECO-scaleIn]}

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: actualMaxVideo},

    value: {presence: required, range: [ 0, 255 ]}

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: modelMaxVideo},

    value: {presence: required, range: [ 0, 100 ]}

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: actualAvgHcVideo},

    value: {presence: required, range: [ 0, 255 ],

    action: [80, up, HcVideoCoreUsageHigh, RECO-scaleOut],

    action: [10, down, HcVideoCoreUsageLow, RECO-scaleIn]}

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: modelAvgHcVideo},

    value: {presence: required, range: [ 0, 100 ],

    action: [80, up, HcVideoCoreUsageHigh, RECO-scaleOut],

    action: [10, down, HcVideoCoreUsageLow, RECO-scaleIn]}

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: actualMaxHcVideo},

    value: {presence: required, range: [ 0, 255 ]}

    }},

    field: {presence: required, structure: {

    name: {presence: required, value: modelMaxHcVideo},

    value: {presence: required, range: [ 0, 100 ]}

    }}

    ]}

    }}

    ]},

    vNicPerformanceArray: {presence: required, array: [

    vNicPerformance: {presence: required, structure: {

    receivedOctetsAccumulated: {presence: required,

    range: [ 0, 18446744073709551615 ]},

    receivedTotalPacketsAccumulated: {presence: required,

    range: [ 0, 18446744073709551615 ]},

    receivedOctetsDelta: {presence: required},

    range: [ 0, 18446744073709551615 ],

    receivedTotalPacketsDelta: {presence: required,

    range: [ 0, 18446744073709551615 ]},

    transmittedOctetsDelta: {presence: required,

    range: [ 0, 18446744073709551615 ]},

    transmittedOctetsAccumulated: {presence: required,

    range: [ 0, 18446744073709551615 ]},

    transmittedTotalPacketsAccumulated: {presence: required,

    range: [ 0, 18446744073709551615 ]},

    transmittedTotalPacketsDelta: {presence: required,

    range: [ 0, 18446744073709551615 ]},

    valuesAreSuspect: {presence: required, value: [ true, false ]},

    vNicIdentifier: {presence: required}

    }}

    ]}

    }}

    }}


Syslog
~~~~~~

.. code-block:: yaml

    # registration for Syslog\_vMRF

    # Constants: the values of domain, eventName, priority,
    lastEpochMicrosec, version,

    # syslogFields.syslogFieldsVersion, syslogFields.syslogTag

    # Variables include: eventId, lastEpochMicrosec, reportingEntityId,
    reportingEntityName,

    # sequence, sourceId, sourceName, startEpochMicrosec,

    # syslogFields.eventSourceHost, syslogFields.eventSourceType,

    # syslogFields.syslogFacility, syslogFields.syslogMsg

    event: {presence: required, structure: {

    commonEventHeader: {presence: required, structure: {

    domain: {presence: required, value: syslog},

    eventName: {presence: required, value: Syslog\_vMrf},

    eventId: {presence: required},

    nfNamingCode: {value: mrfx},

    priority: {presence: required, value: Normal},

    reportingEntityId: {presence: required},

    reportingEntityName: {presence: required},

    sequence: {presence: required},

    sourceId: {presence: required},

    sourceName: {presence: required},

    startEpochMicrosec: {presence: required},

    lastEpochMicrosec: {presence: required},

    version: {presence: required, value: 3.0},

    }},

    syslogFields: {presence: required, structure: {

    eventSourceHost: {presence: required},

    eventSourceType: {presence: required, value: virtualNetworkFunction},

    syslogFacility: {presence: required, range: [16, 23]},

    syslogSev: {presence: required, value: [Emergency, Alert, Critical,
    Error]},

    syslogFieldsVersion: {presence: required, value: 3.0},

    syslogMsg: {presence: required},

    syslogSData: {presence: required, keyValuePairString: {‘ ‘, =,
    keyValuePairs: [

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: ATTEST},

    value: {presence: required}

    }},

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: DATE\_IN},

    value: {presence: required}

    }},

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: DATE\_OUT},

    value: {presence: required}

    }},

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: DEST\_IN},

    value: {presence: required}

    }},

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: FUNCTION},

    value: {presence: required}

    }},

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: ICID},

    value: {presence: required}

    }},

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: ORIGID},

    value: {presence: required}

    }},

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: ORIG\_TN},

    value: {presence: required}

    }},

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: SIP\_REASON\_HEADER},

    value: {presence: required}

    }},

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: STATE},

    value: {presence: required}

    }},

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: STATUS},

    value: {presence: required}

    }},

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: VERSTAT},

    value: {presence: required}

    }}

    ]}} }]

    syslogTag: {presence: required, value: vMRF},

    additionalFields: {presence: required, keyValuePairString: {\|, =,
    keyValuePairs: [

    keyValuePair: {presence: required, structure: {

    key: {presence: required, value: someKeyName},

    value: {presence: required}

    }},

    keyValuePair: {presence: optional, structure: {

    key: {presence: required, value: someOtherKeyName},

    value: {presence: required}

    }}

    ]}}

    }}

    }}


Mobile Flow
~~~~~~~~~~~

.. code-block:: yaml

    # registration for mobileFlow

    # Constants: the values of domain, eventName, priority, version

    #

    # Variables (to be supplied at runtime) include: eventId,
    reportingEntityName,

    # sequence, sourceName, start/lastEpochMicrosec

    #

    event: {presence: required, structure: {

    commonEventHeader: {presence: required, structure: {

    domain: {presence: required, value: mobileFlow},

    eventName: {presence: required, value: mobileFlow},

    eventId: {presence: required},

    nfType: {presence: required, value: sbcx},

    priority: {presence: required, value: Normal},

    reportingEntityName: {presence: required},

    sequence: {presence: required},

    sourceName: {presence: required},

    startEpochMicrosec: {presence: required},

    lastEpochMicrosec: {presence: required},

    version: {presence: required, value: 3.0}

    }},

    mobileFlowFieldsVersion: {presence: required, structure: {

    applicationType: {presence: optional},

    appProtocolType: {presence: optional},

    appProtocolVersion: {presence: optional},

    cid: {presence: optional},

    connectionType: {presence: optional},

    ecgi: {presence: optional},

    flowDirection: {presence: required},

    gtpPerFlowMetrics: {presence: required, structure: {

    avgBitErrorRate: {presence: required},

    avgPacketDelayVariation: {presence: required},

    avgPacketLatency: {presence: required},

    avgReceiveThroughput: {presence: required},

    avgTransmitThroughput: {presence: required},

    durConnectionFailedStatus: {presence: optional},

    durTunnelFailedStatus: {presence: optional},

    flowActivatedBy: {presence: optional},

    flowActivationEpoch: {presence: required},

    flowActivationMicrosec: {presence: required},

    flowActivationTime: {presence: optional},

    flowDeactivatedBy: {presence: optional},

    flowDeactivationEpoch: {presence: required},

    flowDeactivationMicrosec: {presence: required},

    flowDeactivationTime: {presence: required},

    flowStatus: {presence: required},

    gtpConnectionStatus: {presence: optional},

    gtpTunnelStatus: {presence: optional},

    ipTosCountList: {presence: optional},

    ipTosList: {presence: optional},

    largePacketRtt: {presence: optional},

    largePacketThreshold: {presence: optional},

    maxPacketDelayVariation: {presence: required},

    maxReceiveBitRate: {presence: optional},

    maxTransmitBitRate: {presence: optional},

    mobileQciCosCountList: {presence: optional},

    mobileQciCosList: {presence: optional},

    numActivationFailures: {presence: required},

    numBitErrors: {presence: required},

    numBytesReceived: {presence: required},

    numBytesTransmitted: {presence: required},

    numDroppedPackets: {presence: required},

    numGtpEchoFailures: {presence: optional},

    numGtpTunnelErrors: {presence: optional},

    numHttpErrors: {presence: optional},

    numL7BytesReceived: {presence: required},

    numL7BytesTransmitted: {presence: required},

    numLostPackets: {presence: required},

    numOutOfOrderPackets: {presence: required},

    numPacketErrors: {presence: required},

    numPacketsReceivedExclRetrans: {presence: required},

    numPacketsReceivedInclRetrans: {presence: required},

    numPacketsTransmittedInclRetrans: {presence: required},

    numRetries: {presence: required},

    numTimeouts: {presence: required},

    numTunneledL7BytesReceived: {presence: required},

    roundTripTime: {presence: required},

    tcpFlagCountList: {presence: optional},

    tcpFlagList: {presence: optional},

    timeToFirstByte: {presence: required}

    }},

    gtpProtocolType: {presence: optional},

    gtpVersion: {presence: optional},

    httpHeader: {presence: optional},

    imei: {presence: optional},

    imsi: {presence: optional},

    ipProtocolType: {presence: required},

    ipVersion: {presence: required},

    lac: {presence: optional},

    mcc: {presence: optional},

    mnc: {presence: optional},

    msisdn: {presence: optional},

    otherEndpointIpAddress: {presence: required},

    otherEndpointPort: {presence: required},

    otherFunctionalRole: {presence: optional},

    rac: {presence: optional},

    radioAccessTechnology: {presence: optional},

    reportingEndpointIpAddr: {presence: required},

    reportingEndpointPort: {presence: required},

    sac: {presence: optional},

    samplingAlgorithm: {presence: optional},

    tac: {presence: optional},

    tunnelId: {presence: optional},

    vlanId: {presence: optional},

    additionalInformation: {presence: optional, array: {

    field: {presence: required, structure: {

    name: {presence: required, value: name1},

    value: {presence: required}

    }},

    field: {presence: optional, structure: {

    name: {presence: required, value: name2},

    value: {presence: required}

    }}

    }}

    }}

    }}


Sip Signaling
~~~~~~~~~~~~~~

.. code-block:: yaml

    # registration for sipSignaling

    # Constants: the values of domain, eventName, priority, version

    #

    # Variables (to be supplied at runtime) include: eventId,
    reportingEntityName,

    # sequence, sourceName, start/lastEpochMicrosec

    #

    event: {presence: required, structure: {

    commonEventHeader: {presence: required, structure: {

    domain: {presence: required, value: sipSignaling},

    eventName: {presence: required, value: sipSignaling\_modelName},

    eventId: {presence: required},

    nfType: {presence: required, value: sbcx},

    priority: {presence: required, value: Normal},

    reportingEntityName: {presence: required},

    sequence: {presence: required},

    sourceName: {presence: required},

    startEpochMicrosec: {presence: required},

    lastEpochMicrosec: {presence: required},

    version: {presence: required, value: 3.0}

    }},

    sipSignalingFields: {presence: required, structure: {

    compressedSIP: {presence: optional},

    correlator: {presence: required},

    localIpAaddress: {presence: required},

    localPort: {presence: required},

    remoteIpAddress: {presence: required},

    remotePort: {presence: required},

    sipSignalingFieldsVersion: {presence: required},

    summarySip: {presence: optional},

    vnfVendorNameFields: {presence: required, structure: {

    vendorName: {presence: required},

    vfModuleName: {presence: optional},

    vnfName: {presence: optional}

    }},

    additionalInformation: {presence: optional, array: {

    field: {presence: required, structure: {

    name: {presence: required, value: name1},

    value: {presence: required}

    }},

    field: {presence: optional, structure: {

    name: {presence: required, value: name2},

    value: {presence: required}

    }}

    }}

    }}

    }}


Voice Quality
~~~~~~~~~~~~~~

.. code-block:: yaml

    # registration for voiceQuality

    # Constants: the values of domain, eventName, priority, version

    #

    # Variables (to be supplied at runtime) include: eventId,
    lastEpochMicrosec,

    # reportingEntityId, reportingEntityName, sequence, sourceId,

    # sourceName, startEpochMicrosec

    event: {presence: required, structure: {

    commonEventHeader: {presence: required, structure: {

    domain: {presence: required, value: voiceQualityFields},

    eventName: {presence: required, value: voiceQualityFields\_modelName},

    eventId: {presence: required},

    nfType: {presence: required, value: sbcx},

    priority: {presence: required, value: Normal},

    reportingEntityName: {presence: required},

    sequence: {presence: required},

    sourceName: {presence: required},

    startEpochMicrosec: {presence: required},

    lastEpochMicrosec: {presence: required},

    version: {presence: required, value: 3.0}

    }},

    voiceQualityFieldsVersion: {presence: required, structure: {

    calleeSideCodec: {presence: required},

    callerSideCodec: {presence: required},

    correlator: {presence: required},

    remoteIpAddress: {presence: required},

    endOfCallVqmSummaries: {presence: required, structure: {

    adjacencyName: {presence: required},

    endpointDescription: {presence: required},

    endpointAverageJitter: {presence: optional},

    endpointMaxJitter: {presence: optional},

    endpointRtpOctetsLost: {presence: optional},

    endpointRtpPacketsLost: {presence: optional},

    endpointRtpOctetsDiscarded: {presence: optional},

    endpointRtpOctetsReceived: {presence: optional},

    endpointRtpOctetsSent: {presence: optional},

    endpointRtpPacketsDiscarded: {presence: optional},

    endpointRtpPacketsReceived: {presence: optional},

    endpointRtpPacketsSent: {presence: optional},

    localAverageJitter: {presence: optional},

    localMaxJitter: {presence: optional},

    localAverageJitterBufferDelay: {presence: optional},

    localMaxJitterBufferDelay: {presence: optional},

    localRtpOctetsDiscarded: {presence: optional},

    localRtpOctetsLost: {presence: optional},

    localRtpOctetsReceived: {presence: optional},

    localRtpOctetsSent: {presence: optional},

    localRtpPacketsDiscarded: {presence: optional},

    localRtpPacketsLost: {presence: optional},

    localRtpPacketsReceived: {presence: optional},

    localRtpPacketsSent: {presence: optional},

    mosCqe: {presence: optional},

    packetLossPercent: {presence: optional},

    rFactor: {presence: optional},

    roundTripDelay: {presence: optional},

    oneWayDelay: {presence: optional}

    }},

    phoneNumber: {presence: required},

    midCallRtcp: {presence: required},

    vendorVnfNameFields: {presence: required, structure: {

    vendorName: {presence: required},

    vfModuleName: {presence: optional},

    vnfName: {presence: optional}

    }},

    additionalInformation: {presence: optional, array: {

    field: {presence: required, structure: {

    name: {presence: required, value: name1},

    value: {presence: required}

    }},

    field: {presence: optional, structure: {

    name: {presence: required, value: name2},

    value: {presence: required}

    }}

    }}

    }}

    }}


Rules
~~~~~~

.. code-block:: yaml

    #Rules

    Rules: [

    rule: {

    trigger: CpuUsageHigh \|\| FreeMemLow \|\| AudioCoreUsageHigh \|\|

    VideoCoreUsageHigh \|\| HcVideoCoreUsageHigh,

    microservices: [scaleOut]

    },

    rule: {

    trigger: CpuUsageLow && FreeMemHigh && AudioCoreUsageLow &&

    VideoCoreUsageLow && HcVideoCoreUsageLow,

    microservices: [scaleIn]

    }

    ]


Appendix: Historical Change Log
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the latest changes, see the Change Block just before the Table of
Contents.

+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Date         | Revision   | Description                                                                                                                                                                                                          |
+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3/15/2017    | 1.0        | This is the initial release of the VES Event Registration document.                                                                                                                                                  |
+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3/22/2017    | 1.1        | -  Changed the ‘alert’ qualifier to ‘action’ and added support for conditions that will trigger rules.                                                                                                               |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Formatted the document with more sections and subsections.                                                                                                                                                        |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Defined the syntax and semantics for condition based rules.                                                                                                                                                       |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Fixed the YAML examples.                                                                                                                                                                                          |
+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3/27/2017    | 1.2        | -  Clarified the audience of the document and the expectations for vendors.                                                                                                                                          |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Changed the order of fields in the action keyword.                                                                                                                                                                |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Updated the YAML examples.                                                                                                                                                                                        |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Wordsmithed throughout.                                                                                                                                                                                           |
+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3/31/2017    | 1.3        | -  Generalized the descriptions from an ASDC, ECOMP and AT&T-specific interaction with a VNF vendor, to a generic Service Provider interaction with a VNF vendor.                                                    |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Wordsmithed throughout.                                                                                                                                                                                           |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Added a ‘default’ qualifier                                                                                                                                                                                       |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Fixed syntax and semantic inconsistencies in the Rules section                                                                                                                                                    |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Brought all examples into compliance with v5.0                                                                                                                                                                    |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Added a heartbeat example                                                                                                                                                                                         |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Modified the mfvs example                                                                                                                                                                                         |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Modified the syslog example                                                                                                                                                                                       |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Added two complex rules                                                                                                                                                                                           |
+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4/14/2017    | 1.4        | -  Wordsmithed throughout                                                                                                                                                                                            |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Action keyword: clarified use of ‘up’, ‘down’ and ‘at’ triggers; clarified the specification and use of microservices directives at design time and runtime, clarified the use of tca’s                           |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  HeartbeatAction keyword: Added the heartbeatAction keyword                                                                                                                                                        |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Value keyword: clarified the communicaton of strings containing spaces.                                                                                                                                           |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Rules: corrected the use of quotes in examples                                                                                                                                                                    |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Examples: added the heartbeatAction keyword on the heartbeat event example; also corrected use of quotes throughout.                                                                                              |
+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 10/3/2017    | 1.5        | -  Back of Cover Page: updated the license and copyright notice to comply with ONAP guidelines                                                                                                                       |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Section 3.1: Added a ‘Units’ qualifier                                                                                                                                                                            |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Examples: updated the examples to align with VES 5.4.1                                                                                                                                                            |
+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 10/31/2017   | 1.6        | -  Added KeyValuePairString keyword to handle strings which have delimited key-value pairs within them.                                                                                                              |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Updated the syslog example to show the use of KeyValuePairString                                                                                                                                                  |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Updated the syslog example to align syslogSev with VES 5.4.1                                                                                                                                                      |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Added examples for mobile flow, sip signaling and voice quality                                                                                                                                                   |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Added sections within the examples to facilitate rapid access to specific types of example events                                                                                                                 |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Wordsmithed the Introduction                                                                                                                                                                                      |
+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 6/28/2018    | 2.0        | -  Updated to align with the change of the ‘measurementsForVfScaling’ domain to ‘measurement’                                                                                                                        |
|              |            |                                                                                                                                                                                                                      |
|              |            |    -  measurementsForVfScaling measurement                                                                                                                                                                           |
|              |            |                                                                                                                                                                                                                      |
|              |            |    -  measurementsForVfScalingFields measurementFields                                                                                                                                                               |
|              |            |                                                                                                                                                                                                                      |
|              |            |    -  measurementsForVfScalingVersion measurementFieldsVersion                                                                                                                                                       |
|              |            |                                                                                                                                                                                                                      |
|              |            |    -  the ‘mfvs’ abbreviation measurement                                                                                                                                                                            |
|              |            |                                                                                                                                                                                                                      |
|              |            | 1.  Clarified YAML file naming                                                                                                                                                                                       |
|              |            |                                                                                                                                                                                                                      |
|              |            | 2.  Clarified the Action keyword.                                                                                                                                                                                    |
|              |            |                                                                                                                                                                                                                      |
|              |            | 3.  Added an aggregationRole keyword.                                                                                                                                                                                |
|              |            |                                                                                                                                                                                                                      |
|              |            | 4.  Added a castTo keyword.                                                                                                                                                                                          |
|              |            |                                                                                                                                                                                                                      |
|              |            | 5.  Added an isHomogeneous keyword.                                                                                                                                                                                  |
|              |            |                                                                                                                                                                                                                      |
|              |            | 6.  Added a 'key' keyword                                                                                                                                                                                            |
|              |            |                                                                                                                                                                                                                      |
|              |            | 7.  Add a 'keyValuePair' keyword                                                                                                                                                                                     |
|              |            |                                                                                                                                                                                                                      |
|              |            | 8.  Modified the existing 'keyValuePairString' keyword description to reference the 'keyValuePair' keyword.                                                                                                          |
|              |            |                                                                                                                                                                                                                      |
|              |            | 9.  Added a section on Complex Conditions and modified the Rules section                                                                                                                                             |
|              |            |                                                                                                                                                                                                                      |
|              |            | 10. Modified the Examples as follows:                                                                                                                                                                                |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  changed ‘faultFieldsVersion’ to 3.0                                                                                                                                                                               |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  changed ‘heartbeatFieldsVersion’ to 2.0                                                                                                                                                                           |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  provided guidance at the top of the Measurements examples as to how to send extensible fields through arrayOfNamedHashMap in a way that will eliminate the need for custom development at the service provider.   |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  changed ‘measurementFieldsVersion’ to 3.0                                                                                                                                                                         |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  changed measurementFields.additionalMeasurements to reference a ‘namedHashMap’                                                                                                                                    |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  ‘field’ is replaced by ‘keyValuePair’                                                                                                                                                                             |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  ‘name’ is replaced by ‘key’                                                                                                                                                                                       |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  changed ‘namedArrayOfFields’ to ‘namedHashMap’                                                                                                                                                                    |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  fixed the mobile Flow example to show the ‘mobileFlowFields’, show the ‘mobileFlowFieldsVersion’ at 3.0, modify ‘additionalInformation’ to use a hashMap                                                          |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  ‘field’ is replaced by ‘keyValuePair’                                                                                                                                                                             |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  ‘name’ is replaced by ‘key’                                                                                                                                                                                       |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  changed ‘sipSignalingFieldsVersion’ to 2.0                                                                                                                                                                        |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  changed ‘additionalInformation’ to use a hashmap                                                                                                                                                                  |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  ‘field’ is replaced by ‘keyValuePair’                                                                                                                                                                             |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  ‘name’ is replaced by ‘key’                                                                                                                                                                                       |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  fixed the voiceQuality example to show the ‘voiceQualityFields’, show the ‘voiceQualityFieldsVersion’ at 2.0 and modify ‘additionalInformation’ to use a hashMap                                                  |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  ‘field’ is replaced by ‘keyValuePair’                                                                                                                                                                             |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  ‘name’ is replaced by ‘key’                                                                                                                                                                                       |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Modified the rules example to conform to the Complex Conditions and Rules sections.                                                                                                                               |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Numerous clarifications made to address issues with previous drafts of this version including:                                                                                                                    |
|              |            |                                                                                                                                                                                                                      |
|              |            |    -  Fixed arrays followed by other than square brackets                                                                                                                                                            |
|              |            |                                                                                                                                                                                                                      |
|              |            |    -  Section 2.2: clarified format of v# in filename                                                                                                                                                                |
|              |            |                                                                                                                                                                                                                      |
|              |            |    -  Section 3.1.11: clarified use of camel casing                                                                                                                                                                  |
|              |            |                                                                                                                                                                                                                      |
|              |            |    -  Section 3.2.1: corrected and clarified                                                                                                                                                                         |
|              |            |                                                                                                                                                                                                                      |
|              |            |    -  Section 3.2.3 Clarified number of conditions that may be and’d or or’d                                                                                                                                         |
|              |            |                                                                                                                                                                                                                      |
|              |            |    -  Section 3.2.4: fixed reference to PersistentB1                                                                                                                                                                 |
|              |            |                                                                                                                                                                                                                      |
|              |            |    -  Section 3.2.6: fixed math in example                                                                                                                                                                           |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Section 3.3.2: changed reference from ‘alerts’ to ‘events’                                                                                                                                                        |
+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 7/30/2018    | 3.0        | -  Removed the isHomogeneous keyword.                                                                                                                                                                                |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Modified the types of aggregationRoles.                                                                                                                                                                           |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Clarified castTo                                                                                                                                                                                                  |
|              |            |                                                                                                                                                                                                                      |
|              |            | -  Added comment keyword                                                                                                                                                                                             |
+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 9/14/2018    | 3.1        | -  Added keywords: CastTo, Comment, Aggregation Role. These were modified versions of the keywords already defined in version 3.0.                                                                                   |
+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 12/10/2018   | 3.2        | -  Added the PM Data Dictionary and FM Meta Data sections.                                                                                                                                                           |
+--------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
