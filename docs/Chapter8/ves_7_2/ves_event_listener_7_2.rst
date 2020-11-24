.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property, All rights reserved
.. Copyright 2017-2018 Huawei Technologies Co., Ltd.
.. Copyright 2020 Nokia Solutions and Networks

.. _ves_event_listener_7_2:

Service: VES Event Listener 7.2
-------------------------------

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


:Document: VES Event Listener
:Revision: 7.2
:Revision Date: May 6th, 2020
:Author: Trevor Lovett

+-----------------+-----------------------------+
| Contributors:   | **Min Chen – AT&T**         |
|                 |                             |
|                 | **Fred Delaplace - AT&T**   |
|                 |                             |
|                 | **Andrew Egan – AT&T**      |
|                 |                             |
|                 | **Alok Gupta – AT&T**       |
|                 |                             |
|                 | **Marge Hillis – Nokia**    |
|                 |                             |
|                 | **Gerard Hynes – AT&T**     |
|                 |                             |
|                 | **Ken Kelly – AT&T**        |
|                 |                             |
|                 | **Damian Nowak - Nokia**    |
|                 |                             |
|                 | **Mark Scott – Ericsson**   |
|                 |                             |
|                 | **Tim Verall – Intel**      |
|                 |                             |
|                 | **Sumit Verdi – VMWare**    |
|                 |                             |
|                 | **Trevor Lovett – AT&T**    |
|                 |                             |
|                 | **Rich Erickson – AT&T**    |
+-----------------+-----------------------------+

.. contents:: Table of Contents

Introduction
^^^^^^^^^^^^

This document describes the RESTful interface for the VES Event
Listener. The VES acronym originally stood for Virtual-function Event
Streaming, but VES has been generalized to support network-function
event streaming, whether virtualized or not. The VES Event Listener is
capable of receiving any event sent in the VES
:ref:`ves_common_event_format_7_2`. In the VES Common Event Format, an event
consists of a required
:ref:`Common Event Header <ves_common_event_header_7_2>` (i.e., object)
accompanied by zero or more event domain blocks.

It should be understood that events are well structured packages of
information, identified by an ``eventName``, which are asynchronously
communicated to subscribers who are interested in the ``eventName``. Events
can convey measurements, faults, syslogs, threshold crossing alerts and
other types of information. Events are simply a way of communicating
well-structured packages of information to one or more instances of an
VES Event Listener service.

This document describes a RESTful, connectionless, push event listener
that can receive single events or batches of events in the
:ref:`ves_common_event_format_7_2`.

Versioning
^^^^^^^^^^

Three types of version numbers supported by this specification:

- The API specification itself is versioned. Going forward, the major
  number of the specification version will be incremented whenever any
  change could break an existing client (e.g., a field name is deleted
  or changed). All other changes to the spec (e.g., a field name is
  added, or text changes are made to the specification itself) will
  increment only the minor number or patch number. Note that the major
  number appears in REST resource URLs as v# (where ‘#’ is the major
  number). Minor and patch numbers are communicated in HTTP headers.
  For more information, see the API Versioning writeup in section 6.1.

- The JSON schema is versioned. Going forward, the major number of the
  JSON schema will be incremented whenever any change could break an
  existing client (e.g., a field name is deleted or changed). All other
  changes to the schema (e.g., a field name is added or text changes
  are made to the field descriptions) will increment only the minor
  number or patch number.

- The field blocks are versioned. Field blocks include the
  commonEventHeader and the domain blocks (e.g., the faultFields
  block). Going forward, the major number of each field block will be
  incremented whenever any change to that block could break an existing
  client (e.g., a field name is deleted or changed). All other changes
  to that block (e.g., a field name is added or text changes are made
  to the field descriptions) will increment only the minor number.

Client Requirements
^^^^^^^^^^^^^^^^^^^

Any NF or client library that is responsible for delivering VES events
to a VES Event Listener must comply with this specification to ensure events are
received, accepted, and processed properly.

Because the VES specification relies on clients to push events to the
VES Event Listener, the client assumes certain responsibilities such as:

- Providing configuration options supporting integration into a
  Service Provider environment
- Ensuring reliable delivery of events
- Customization of default behaviors based on Service Provider needs

While the documentation of these expectations are beyond the Event Listener
specification, these requirements are documented in the ONAP VNF Requirements
for :ref:`VES Monitoring Requirements <ves_monitoring_requirements>`.


Compatibility with ONAP
^^^^^^^^^^^^^^^^^^^^^^^

Unless otherwise stated, this version of the Event Listener specification is
compatible with the release of ONAP the specification is released under.  In
other words, if the specification is released under the Guilin ONAP release,
then the VES Event Listeners provided by DCAE will also be compatible with
this specification.

Support for Protocols Other Than HTTPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This API specification describes an HTTPS RESTful interface using the
JSON content-type.

Alternative API specifications may be provided in future using Google
Protocol Buffers, WebSockets, or Apache Avro.

Field Block Versions
^^^^^^^^^^^^^^^^^^^^

A summary of the latest field block version enums as of this version of
the API spec is provided below:

- commonEventHeader version 4.1 (note: the enum with support 4.0,
  4.0.1, 4.1 to avoid breaking clients of earlier versions of major
  version 4)

- commonEventHeader vesEventListenerVersion enum: 7.2 (note: the enum
  will support 7.0, 7.0.1, 7.1, 7.1.1, 7.2 to avoid breaking clients of earlier
  versions of major version 7)

- faultFieldsVersion:4.0

- heartbeatFieldsVersion: 3.0

- measurementFieldsVersion: 4.0

- mobileFlowFieldsVersion: 4.0

- notificationFieldsVersion: 2.0

- otherFieldsVersion: 3.0

- perf3gppFieldsVersion: 1.0

- pnfRegistrationFieldsVersion: 2.0

- sigSignalingFieldsVersion: 3.0

- stateChangeFieldsVersion: 4.0

- stndDefinedFieldsVersion: 1.0

- syslogFieldsVersion: 4.0

- thresholdCrossingFieldsVersion: 4.0

- voiceQualityFieldsVersion: 4.0

.. _ves_common_event_format_7_2:

Common Event Format
^^^^^^^^^^^^^^^^^^^

A JSON schema describing the Common Event Format is provided below and
is reproduced in the tables that follow.

:download:`JSON <CommonEventFormat_30.2_ONAP.json>`


Note on optional fields:

    If the event publisher collects a field that is identified as
    optional in the data structures below, then the event publisher
    *must* send that field.

Note on extensible fields:

    VES contains various extensible structures (e.g., hashMap) that
    enable event publishers to send information that has not been
    explicitly defined in VES data structures.

-  Event publishers *must not* send information through extensible
   structures where VES has explicitly defined fields for that
   information. For example, event publishers *must not* send
   information like cpuIdle, through an extensible structure, because
   VES has explicitly defined a cpuUsage.cpuIdle field for the
   communication of that information.

-  Keys sent through extensible fields should use camel casing to separate
   words and acronyms; only the first letter of each acronym shall be
   capitalized.

Common Event Datatypes
~~~~~~~~~~~~~~~~~~~~~~

Datatype: arrayOfJsonObject
+++++++++++++++++++++++++++

The arrayOfJsonObject datatype provides an array of json objects, each
of which is describ ed by name, schema and other meta-information. It
consists of the following fields:

+---------------------+------------------+----------+----------------------+
| Field               | Type             | Required?| Description          |
+=====================+==================+==========+======================+
| arrayOfJsonObject   | jsonObject [ ]   | Yes      | Array of jsonObject  |
+---------------------+------------------+----------+----------------------+

Datatype: arrayOfNamedHashMap
+++++++++++++++++++++++++++++

The arrayOfNamedHashMap datatype provides an array of hashMaps, each of
which is associated with a descriptive name. It consists of the
following fields:

+---------------------+------------------+-----------+-----------------------+
| Field               | Type             | Required? | Description           |
+=====================+==================+===========+=======================+
| arrayOfNamedHashMap | namedHashMap [ ] | Yes       | Array of namedHashMap |
+---------------------+------------------+-----------+-----------------------+

Datatype: event
+++++++++++++++

The event datatype consists of the following fields which constitute the
‘root level’ of the common event format:

+--------------+--------------+-----------+-----------------------------------+
| Field        | Type         | Required? | Description                       |
+==============+==============+===========+===================================+
| commonEvent\ | commonEvent\ | Yes       | Fields common to all events       |
| Header       | Header       |           |                                   |
+--------------+--------------+-----------+-----------------------------------+
| faultFields  | faultFields  | No        | Fields specific to fault events   |
+--------------+--------------+-----------+-----------------------------------+
| heartbeat\   | heartbeat\   | No        | Fields specific to heartbeat      |
| Fields       | Fields       |           | events                            |
+--------------+--------------+-----------+-----------------------------------+
| measurement\ | measurement\ | No        | Fields specific to measurement    |
| Fields       | Fields       |           | events                            |
+--------------+--------------+-----------+-----------------------------------+
| mobileFlow\  | mobileFlow\  | No        | Fields specific to mobility flow  |
| Fields       | Fields       |           | events                            |
+--------------+--------------+-----------+-----------------------------------+
| notification\| notification\| No        | Fields specific to notification   |
| Fields       | Fields       |           | events                            |
+--------------+--------------+-----------+-----------------------------------+
| otherFields  | otherFields  | No        | Fields specific to other types of |
|              |              |           | events                            |
+--------------+--------------+-----------+-----------------------------------+
| perf3gpp\    | perf3gpp\    | No        | Fields specific to perf3gpp       |
| Fields       | Fields       |           | events                            |
+--------------+--------------+-----------+-----------------------------------+
| pnf\         | pnf\         | No        | Fields specific to pnfRegistration|
| Registration\| Registration\|           | events                            |
| Fields       | Fields       |           |                                   |
+--------------+--------------+-----------+-----------------------------------+
| sipSignaling\| sipSignaling\| No        | Fields specific to sipSignaling   |
| Fields       | Fields       |           | events                            |
+--------------+--------------+-----------+-----------------------------------+
| stateChange\ | stateChange\ | No        | Fields specific to state change   |
| Fields       | Fields       |           | events                            |
+--------------+--------------+-----------+-----------------------------------+
| stndDefined\ | stndDefined\ | No        | Fields specific to standards      |
| Fields       | Fields       |           | defined events                    |
+--------------+--------------+-----------+-----------------------------------+
| syslogFields | syslogFields | No        | Fields specific to syslog events  |
+--------------+--------------+-----------+-----------------------------------+
| threshold\   | threshold\   | No        | Fields specific to threshold      |
| Crossing\    | Crossing\    |           | crossing alert events             |
| AlertFields  | AlertFields  |           |                                   |
+--------------+--------------+-----------+-----------------------------------+
| voiceQuality\| voiceQuality\| No        | Fields specific to voiceQuality   |
| Fields       | Fields       |           | events                            |
+--------------+--------------+-----------+-----------------------------------+

Datatype: eventList
+++++++++++++++++++

The eventList datatype consists of the following fields:

+-------------+-------------+----------+-------------------+
| Field       | Type        | Required?| Description       |
+=============+=============+==========+===================+
| eventList   | event [ ]   | Yes      | Array of events   |
+-------------+-------------+----------+-------------------+

Datatype: hashMap
+++++++++++++++++

The hashMap datatype is an ‘associative array’, which is an unordered
collection of key-value pairs of the form "key": "value", where each key
and value are strings. Keys should use camel casing to separate words and
acronyms; only the first letter of each acronym should be capitalized.

Datatype: jsonObject
++++++++++++++++++++

The jsonObject datatype provides a json object schema, name and other
meta-information along with one or more object instances that conform to
the schema:

+--------------+--------------+-----------+----------------------------------+
| Field        | Type         | Required? | Description                      |
+==============+==============+===========+==================================+
| object\      | JsonObject\  | Yes       | Contains one or more instances of|
| Instances    | Instance [ ] |           | the json object                  |
+--------------+--------------+-----------+----------------------------------+
| objectName   | string       | Yes       | Name of the json object          |
+--------------+--------------+-----------+----------------------------------+
| objectSchema | string       | No        | json schema for the object       |
+--------------+--------------+-----------+----------------------------------+
| objectSchema\| string       | No        | URL to the json schema for the   |
| Url          |              |           | object                           |
+--------------+--------------+-----------+----------------------------------+
| nfSubscribed\| string       | No        | Name of the object associated    |
| ObjectName   |              |           | with the nfSubscriptionId        |
+--------------+--------------+-----------+----------------------------------+
| nf\          | string       | No        | Identifies an openConfig         |
| Subscription\|              |           | telemetry subscription on a      |
| Id           |              |           | network function, which          |
|              |              |           | configures the network function  |
|              |              |           | to send complex object data      |
|              |              |           | associated with the jsonObject   |
+--------------+--------------+-----------+----------------------------------+

Datatype: jsonObjectInstance
++++++++++++++++++++++++++++

The jsonObjectInstance datatype provides meta-information about an
instance of a jsonObject along with the actual object instance:

+----------------+------------+----------+-----------------------------------+
| Field          | Type       | Required?| Description                       |
+================+============+==========+===================================+
| jsonObject     | jsonObject | No       | Optional recursive specification  |
|                |            |          | of jsonObject                     |
+----------------+------------+----------+-----------------------------------+
| objectInstance | object     | No       | Contains an instance conforming to|
|                |            |          | the jsonObject schema             |
+----------------+------------+----------+-----------------------------------+
| objectInstance\| number     | No       | the unix time, aka epoch time,    |
| EpochMicrosec  |            |          | associated with this              |
|                |            |          | objectInstance--as microseconds   |
|                |            |          | elapsed since 1 Jan 1970 not      |
|                |            |          | including leap seconds            |
+----------------+------------+----------+-----------------------------------+
| objectKeys     | key [ ]    | No       | An ordered set of keys that       |
|                |            |          | identifies this particular        |
|                |            |          | instance of jsonObject (e.g., that|
|                |            |          | places it in a hierarchy)         |
+----------------+------------+----------+-----------------------------------+

Datatype: key
+++++++++++++

The key datatype is a tuple which provides the name of a key along with
its value and relative order; it consists of the following fields:

+----------+---------+-----------+-------------------------------------------+
| Field    | Type    | Required? | Description                               |
+==========+=========+===========+===========================================+
| keyName  | string  | Yes       | Name of the key                           |
+----------+---------+-----------+-------------------------------------------+
| keyOrder | Integer | No        | Relative sequence or order of the key     |
|          |         |           | (with respect to other keys)              |
+----------+---------+-----------+-------------------------------------------+
| keyValue | string  | No        | Value of the key                          |
+----------+---------+-----------+-------------------------------------------+

Datatype: namedHashMap
++++++++++++++++++++++

The namedHashMap datatype is a hashMap which is associated with and
described by a name; it consists of the following fields:

+---------+---------+-----------+--------------------------------------------+
| Field   | Type    | Required? | Description                                |
+=========+=========+===========+============================================+
| name    | string  | Yes       | Name associated with or describing the     |
|         |         |           | hashmap                                    |
+---------+---------+-----------+--------------------------------------------+
| hashMap | hashMap | Yes       | One or more key:value pairs                |
+---------+---------+-----------+--------------------------------------------+

Datatype: requestError
++++++++++++++++++++++

The requestError datatype defines the standard request error data
structure:

+-----------+--------+-----------+-------------------------------------------+
| Field     | Type   | Required? | Description                               |
+===========+========+===========+===========================================+
| messageId | string | Yes       | Unique message identifier of the format   |
|           |        |           | ‘ABCnnnn’ where ‘ABC’ is either ‘SVC’ for |
|           |        |           | Service Exceptions or ‘POL’ for Policy    |
|           |        |           | Exception. Exception numbers may be in the|
|           |        |           | range of 0001 to 9999 where 0001 to 2999  |
|           |        |           | are defined by OMA (see section 5.1) and  |
|           |        |           | 3000-9999 are available and undefined.    |
+-----------+--------+-----------+-------------------------------------------+
| text      | string | Yes       | Message text, with replacement variables  |
|           |        |           | marked with %n, where n is an index into  |
|           |        |           | the list of <variables> elements, starting|
|           |        |           | at 1                                      |
+-----------+--------+-----------+-------------------------------------------+
| url       | string | No        | Hyperlink to a detailed error resource    |
|           |        |           | e.g., an HTML page for browser user agents|
+-----------+--------+-----------+-------------------------------------------+
| variables | string | No        | List of zero or more strings that         |
|           |        |           | represent the contents of the variables   |
|           |        |           | used by the message text                  |
+-----------+--------+-----------+-------------------------------------------+

Datatype: vendorNfNameFields
++++++++++++++++++++++++++++

The vendorNfNameFields provides vendor, nf and nfModule identifying
information:

+--------------+--------+-----------+----------------------------------------+
| Field        | Type   | Required? | Description                            |
+==============+========+===========+========================================+
| vendorName   | string | Yes       | Network function vendor name           |
+--------------+--------+-----------+----------------------------------------+
| nfModuleName | string | No        | Name of the nfModule generating the    |
|              |        |           | event                                  |
+--------------+--------+-----------+----------------------------------------+
| nfName       | string | No        | Name of the network function generating|
|              |        |           | the event                              |
+--------------+--------+-----------+----------------------------------------+

Common Event Header Data Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _ves_common_event_header_7_2:

Datatype: commonEventHeader
+++++++++++++++++++++++++++

The commonEventHeader datatype consists of the following fields common
to all events:

+-----------+----------+-----------+-----------------------------------------+
| Field     | Type     | Required? |  Description                            |
+===========+==========+===========+=========================================+
| domain    | string   | Yes       | Event domain enumeration: ‘fault’,      |
|           |          |           | ‘heartbeat’, ‘measurement’, ‘mobileFlow’|
|           |          |           | , ‘notification’, ‘other’, ‘perf3gpp’,  |
|           |          |           | ‘pnfRegistration’, ‘sipSignaling’,      |
|           |          |           | ‘stateChange’,‘stndDefined’, ‘syslog’,  |
|           |          |           | ‘thresholdCrossingAlert’, ‘voiceQuality’|
+-----------+----------+-----------+-----------------------------------------+
| eventId   | string   | Yes       | Event key that is unique to the event   |
|           |          |           | source. The key must be unique within   |
|           |          |           | notification life cycle similar to      |
|           |          |           | EventID from 3GPP. It could be a        |
|           |          |           | sequential number, or a composite key   |
|           |          |           | formed from the event fields, such as   |
|           |          |           | domain\_sequence. The eventId should not|
|           |          |           | include whitespace. For fault events,   |
|           |          |           | eventId is the eventId of the initial   |
|           |          |           | alarm; if the same alarm is raised again|
|           |          |           | for changed, acknowledged or cleared    |
|           |          |           | cases, eventId must be the same as the  |
|           |          |           | initial alarm (along with the same      |
|           |          |           | startEpochMicrosec but with a different |
|           |          |           | sequence number).                       |
|           |          |           | See :ref:`ves_eventid_usecases_7_2` for |
|           |          |           | additional guidance on eventId usage.   |
+-----------+----------+-----------+-----------------------------------------+
| eventName | string   | Yes       |  See :ref:`ves_eventname_guidelines_7_2`|
|           |          |           |  for additional information on naming   |
|           |          |           |  events                                 |
+-----------+----------+-----------+-----------------------------------------+
| eventType | string   | No        |                                         |
+-----------+----------+-----------+-----------------------------------------+
| internal\ | internal\| No        | Fields (not supplied by event sources)  |
| Header    | Header   |           | that the VES Event Listener service can |
| Fields    | Fields   |           | use to enrich the event if needed for   |
|           |          |           | efficient internal processing. This is  |
|           |          |           | an empty object which is intended to be |
|           |          |           | defined separately by each service      |
|           |          |           | provider (e.g., AT&T) implementing the  |
|           |          |           | VES Event Listener.                     |
+-----------+----------+-----------+-----------------------------------------+
| lastEpoch\| number   | Yes       | the latest unix time aka epoch time     |
| Microsec  |          |           | associated with the event from any      |
|           |          |           | component--as microseconds elapsed since|
|           |          |           | 1 Jan 1970 not including leap seconds   |
+-----------+----------+-----------+-----------------------------------------+
| nfcNaming\| string   | No        | Network function component type: 3      |
| Code      |          |           | characters (aligned with vfc naming     |
|           |          |           | standards)                              |
+-----------+----------+-----------+-----------------------------------------+
| nfNaming\ | string   | No        | Network function type: 4 characters     |
| Code      |          |           | (aligned with vnf and pnf naming        |
|           |          |           | standards)                              |
+-----------+----------+-----------+-----------------------------------------+
| nfVendor\ | string   | No        |                                         |
| Name      |          |           |                                         |
+-----------+----------+-----------+-----------------------------------------+
| priority  | string   | Yes       |                                         |
+-----------+----------+-----------+-----------------------------------------+
| reporting\| string   | No        | UUID identifying the entity reporting   |
| EntityId  |          |           | the event or detecting a problem in     |
|           |          |           | another vnf/vm or pnf which is          |
|           |          |           | experiencing the problem. (Note: the    |
|           |          |           | AT&T internal enrichment process shall  |
|           |          |           | ensure that this field is populated).   |
|           |          |           | The reportingEntityId is an id for the  |
|           |          |           | reportingEntityName. See                |
|           |          |           | ‘reportingEntityName’ for more          |
|           |          |           | information.                            |
+-----------+----------+-----------+-----------------------------------------+
| reporting\| string   | Yes       | Name of the entity reporting the event  |
| EntityName|          |           | or detecting a problem in another vnf/vm|
|           |          |           | or pnf which is experiencing the        |
|           |          |           | problem. May be the same as the         |
|           |          |           | sourceName. For synthetic events        |
|           |          |           | generated by DCAE, it is the name of the|
|           |          |           | app generating the event.               |
+-----------+----------+-----------+-----------------------------------------+
| sequence  | integer  | Yes       | Ordering of events communicated by an   |
|           |          |           | event source instance (or 0 if not      |
|           |          |           | needed)                                 |
+-----------+----------+-----------+-----------------------------------------+
| sourceId  | string   | No        | UUID identifying the entity experiencing|
|           |          |           | the event issue, which may be detected  |
|           |          |           | and reported by a separate reporting    |
|           |          |           | entity (note: the AT&T internal         |
|           |          |           | enrichment process shall ensure that    |
|           |          |           | this field is populated). The sourceId  |
|           |          |           | is an id for the sourceName. See        |
|           |          |           | ‘sourceName’ for more information.      |
+-----------+----------+-----------+-----------------------------------------+
| sourceName| string   | Yes       | Name of the entity experiencing the     |
|           |          |           | event issue, which may be detected and  |
|           |          |           | reported by a separate reporting entity.|
|           |          |           | The sourceName identifies the device for|
|           |          |           | which data is collected. A valid        |
|           |          |           | sourceName must be inventoried in A&AI. |
|           |          |           | If sourceName is a xNF (vnf or pnf),    |
|           |          |           | xNFC or VM, then the event must be      |
|           |          |           | reporting data for that particular xNF, |
|           |          |           | xNFC or VM. If the sourceName is a xNF, |
|           |          |           | comprised of multiple xNFCs, the data   |
|           |          |           | must be reported/aggregated at the xNF  |
|           |          |           | level. Data for individual xNFC must not|
|           |          |           | be included in the xNF sourceName event.|
+-----------+----------+-----------+-----------------------------------------+
| start\    | number   | Yes       | the earliest unix time aka epoch time   |
| Epoch\    |          |           | associated with the event from any      |
| Microsec  |          |           | component--as microseconds elapsed since|
|           |          |           | 1 Jan 1970 not including leap seconds.  |
|           |          |           | For measurements and heartbeats, where  |
|           |          |           | events are collected over predefined    |
|           |          |           | intervals, startEpochMicrosec shall be  |
|           |          |           | rounded to the nearest interval boundary|
|           |          |           | (e.g., the epoch equivalent of 3:00PM,  |
|           |          |           | 3:10PM, 3:20PM, etc…). For fault events,|
|           |          |           | startEpochMicrosec is the timestamp of  |
|           |          |           | the initial alarm; if the same alarm is |
|           |          |           | raised again for changed, acknowledged  |
|           |          |           | or cleared cases, startEpoch Microsec   |
|           |          |           | must be the same as the initial alarm   |
|           |          |           | (along with the same eventId and an     |
|           |          |           | incremental sequence number). For       |
|           |          |           | devices with no timing source (clock),  |
|           |          |           | the default value will be 0 and the VES |
|           |          |           | collector will replace it with Collector|
|           |          |           | time stamp (when the event is received) |
+-----------+----------+-----------+-----------------------------------------+
| stnd\     | string   | No        | Standards-organization defined event    |
| Defined\  |          |           | namespace; expected usage includes event|
| Namespace |          |           | routing by the event listener           |
+-----------+----------+-----------+-----------------------------------------+
| timeZone\ | string   | No        | Offset to GMT to indicate local time    |
| Offset    |          |           | zone for device formatted as            |
|           |          |           | ‘UTC+/-hh:mm’; see                      |
|           |          |           | time_zone_abbreviations_ for UTC offset |
|           |          |           | examples                                |
+-----------+----------+-----------+-----------------------------------------+
| version   | string   | Yes       | Version of the event header as "#.#"    |
|           |          |           | where # is a digit; see section 1 for   |
|           |          |           | the correct digits to use.              |
+-----------+----------+-----------+-----------------------------------------+
| vesEvent\ | string   | Yes       | Version of the ves event listener api   |
| Listener\ |          |           | spec that this event is compliant with  |
| Version   |          |           | (as "#" or "#.#" or "#.#.#" where # is a|
|           |          |           | digit; see section 1 for the correct    |
|           |          |           | digits to use).                         |
+-----------+----------+-----------+-----------------------------------------+

Datatype: internalHeaderFields
++++++++++++++++++++++++++++++

The internalHeaderFields datatype is an undefined object which can
contain arbitrarily complex JSON structures. It is intended to be
defined separately by each service provider (e.g., AT&T) implementing
the VES Event Listener. The fields in internalHeaderFields are not
provided by any event source but instead are added by the VES Event
Listener service itself as part of an event enrichment process necessary
for efficient internal processing of events received by the VES Event
Listener.


.. _ves_eventname_guidelines_7_2:

Best Practices for eventName
++++++++++++++++++++++++++++

To prevent naming collisions, eventNames sent as part of the
commonEventHeader, should conform to the following naming convention
designed to summarize the purpose and type of the event, and to ensure
the uniqueness of the eventName:

    ``{DomainAbbreviation}_{PublisherName}_{Description}``

Each underscore-separated subfield above should start with a capital
letter and use camel-casing to separate words and acronyms. Acronyms
should capitalize only the first letter of the acronym. Spaces and
underscores should not appear within any subfield.

The DomainAbbreviation subfield derives from the ‘domain’ field in the
commonEventHeader, as specified below:

-  ‘Fault’ for the fault domain

-  ‘Heartbeat’ for the heartbeat domain

-  ‘Measurement’ for the measurement domain

-  ‘MobileFlow’ for the mobileFlow domain

-  ‘Notification’ for the notification domain

-  ‘Other’ for the other domain

-  ‘Perf3gpp’ for the perf3gpp domain

-  ‘PnfReg’ for the pnfRegistration domain

-  ‘SipSignaling’ for the sipSignaling domain

-  ‘StateChange’ for the stateChange domain

-  ‘StndDefined’ for the stndDefined domain

-  ‘Syslog’ for the syslog domain

-  ‘Tca’ for the thresholdCrossingAlert domain

-  ‘VoiceQuality’ for the voiceQuality domain

The PublisherName subfield describes the vendor product or application
publishing the event. This subfield conforms to the following
conventions:

-   Vendor products are specified as: ``{productName}-{vendorName}``

    For example: ``Visbc-Metaswitch`` or ``Vdbe-Juniper``, where a hyphen is
    used to separate the ``productName`` and ``vendorName`` subfields. Note that
    the ``productName`` and ``vendorName`` subfields must not include hyphens
    themselves.

    Organizing the information in this way will cause an alphabetical
    listing of eventNames to sort similar network functions together,
    rather than to sort them by vendor.

    The ``productName`` subfield may describe a NF or a NFC. Where NFC names
    may be reused across different NF’s, they should be specified as:

    ``{NfName}:{NfcName}``

    where a colon is used to separate the ``NfName`` and ``NfcName`` subfields.
    Note that the ``NfName`` and ``NfcName`` subfields must not include colons
    themselves.

    The ``productName`` may also describe other types of vendor modules or
    components such as a VM, application or hostname. As with NFs and
    NFCs, parent:child relationships may be communicated using colon as
    a subfield delimiter.

-   Service providers who adopt the VES Common Event Format for internal
    use, may provide PublisherName without the vendorName subfield. They
    would typically identify an application, system, service or
    microservice publishing the event (e.g., ‘Policy’, ‘So’,
    ‘MobileCallRecording’ or ‘Dkat’). As with NFs and NFCs, parent:child
    relationships may be communicated using colon as a subfield delimiter
    (e.g., ApplicationName:ApplicationComponent).

The final subfield of the eventName name should describe, in a compact
camel case format the specific information being conveyed by the event.
In some cases, this final subfield may not be required (e.g., in the
case of certain heartbeats).

Examples of event names following the naming standards are provided
below:

- ``Tca_Vdbe-Ericsson_CpuThresholdExceeded``

- ``Heartbeat_Visbc:Mmc-Metaswitch``

- ``Syslog_Vdbe-Ericsson``

- ``Fault_MobileCallRecording_PilotNumberPoolExhaustion``

- ``Other_So:WanBonding_InstantiationPart1Complete``

.. _ves_eventid_usecases_7_2:

EventId Use Cases Examples
++++++++++++++++++++++++++

``eventId`` Examples:

**NOTE**: Please note, the following are only *examples*, and other formats
can be used provided they meet the requirement that the ``eventId`` is unique
for all events or unique fault occurrence.

**Example 1**: assumes a unique key for each domain consisting of domain
followed by an integer domain<n> or domainId<n>, where <n> is a positive integer,
e.g. fault000001, heartbeat000001, measurement000005,
notification3gppPerfFileReady0005

**Example 2**: assumes a unique integer key for all events across all domains
<n>: 000000001, 00000002, 000000003

Rules:

1. All domains except Fault: each time a subsequent event is sent the
   integer part of eventId will increment by 1. Repeat of eventId
   assumes duplicate event. Sequence number is set to 0 for all domains
   except fault.

2. eventId construction for Fault Events:

   a. Most likely scenario

      *    The sourceName on each Fault event is the NF Instance Name
           (pnf-name or vnf-name or vm-name) as entered in A&AI uniquely
           identifying this instance of the NF.

      *    The eventId on Fault events is the same every time a given
           fault is raised (including onset and re-raise)

            1. The startEpochMicrosec value for the Fault event is the
               timestamp for when the fault onset occurs. Subsequent
               events for the same fault will keep the same startEpochMicrosec
               value.

            2. lastEpochMicrosec indicates the current event time. This value
               will be updated for each subsequent event for a given fault.

            3. The sequence number for each Fault event is set to 1 when the
               fault is raised and increments each time the same
               fault event is raised, until a clear is sent.

      *    After the fault is cleared, a new eventId is used.

   .. image:: Use-Case-1.png

   b. **Alternative Scenario**: Network Function When Fault Event Status is Not
      Maintained.

      *    The sourceName on each Fault event is the NF Instance Name
           (pnf-name or vnf-name or vm-name) as entered in A&AI uniquely
           identifying this instance of the NF.

      *    The eventId on Fault events is the same every time a given
           fault is raised or cleared, even if it is re-raised after it
           had previously cleared.  So, for example, if EMS loses
           contact with a particular device then a Fault event might be
           sent for a raise, re-raise (because EMS has re-tried and
           still can’t contact the device), clear (because EMS has
           re-tried and it can contact the device) and then raise again
           (because EMS has lost contact with the device again).  The
           same eventId is used for all 4 of those Fault events.

      *    The startEpochMicrosec value for each Fault event is the
           timestamp for when that event is generated, not when the
           fault first occurred.  So all 4 of the Fault events in the
           previous bullet point would have a different timestamp.

      *    lastEpochMicrosec indicates the current event time.

      *    The sequence number for each Fault event is currently set to
           0 on a raise and 1 on a clear.  We could change that so that
           each Fault event is given a new monotonically increasing
           sequence number whether it is a raise or a clear if that is
           helpful (which is reset to 0 if the VM restarts) but they
           won’t be consecutive.

      *    Normally, a clear is expected for each fault to be sent from a
           network function. However a few fault notification types will never
           be re-raised or cleared. In this case, general rules for VES events
           shall be followed with a new eventId for each event and sequence
           number set to 0.

   .. image:: Use-Case-2.png

**Example 3**: Exceptions from eventId uniqueness requirement:
In certain scenarios such as restarts, the xNF might be unable to assure eventId
uniqueness as information about the latest used eventID value might not have been
persisted. When such eventId information is unavailable, the xNF should reset the
eventID numbering following the "EventId use-case examples".

Technology Independent Datatypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

‘Fault’ Domain Datatypes
++++++++++++++++++++++++

Datatype: faultFields
*********************

The faultFields datatype consists of the following fields:

+-----------------+---------+-----------+-------------------------------------+
| Field           | Type    | Required? | Description                         |
+=================+=========+===========+=====================================+
| alarmAdditional | hashMap | No        | Additional alarm information.       |
| Information     |         |           |                                     |
|                 |         |           |                                     |
|                 |         |           | - Note1: for SNMP mapping to VES,   |
|                 |         |           |   for hash key use OID of varbind,  |
|                 |         |           |   for value use incoming data for   |
|                 |         |           |   that varbind).                    |
|                 |         |           |                                     |
|                 |         |           | - Note2: Alarm ID for 3GPP should be|
|                 |         |           |   included (if applicable) in       |
|                 |         |           |   alarmAdditonalInformation as      |
|                 |         |           |   ‘alarmId’:’alarmIdValue’.         |
|                 |         |           |                                     |
|                 |         |           | Could contain managed object        |
|                 |         |           | instance as separate key:value;     |
|                 |         |           | could add probable cause as separate|
|                 |         |           | key:value.                          |
+-----------------+---------+-----------+-------------------------------------+
| alarmCondition  | string  | Yes       | Short name of the alarm             |
|                 |         |           | condition/problem, such as a trap   |
|                 |         |           | name. Should not have white space   |
|                 |         |           | (e.g., tpLgCgiNotInConfig,          |
|                 |         |           | BfdSessionDown, linkDown, etc…)     |
+-----------------+---------+-----------+-------------------------------------+
| alarmInterfaceA | string  | No        | Card, port, channel or interface    |
|                 |         |           | name of the device generating the   |
|                 |         |           | alarm. This could reflect managed   |
|                 |         |           | object.                             |
+-----------------+---------+-----------+-------------------------------------+
| eventCategory   | string  | No        | Event category, for example:        |
|                 |         |           | ‘license’, ‘link’, ‘routing’,       |
|                 |         |           | ‘security’, ‘signaling’             |
+-----------------+---------+-----------+-------------------------------------+
| eventSeverity   | string  | Yes       | Event severity enumeration:         |
|                 |         |           | ‘CRITICAL’, ‘MAJOR’, ‘MINOR’,       |
|                 |         |           | ‘WARNING’, ‘NORMAL’. NORMAL is used |
|                 |         |           | to represent clear.                 |
+-----------------+---------+-----------+-------------------------------------+
| eventSourceType | string  | Yes       | Examples: ‘card’, ‘host’, ‘other’,  |
|                 |         |           | ‘port’, ‘portThreshold’, ‘router’,  |
|                 |         |           | ‘slotThreshold’, ‘switch’,          |
|                 |         |           | ‘virtualMachine’,                   |
|                 |         |           | ‘virtualNetworkFunction’. This could|
|                 |         |           | be managed object class.            |
+-----------------+---------+-----------+-------------------------------------+
| faultFields\    | string  | Yes       | Version of the faultFields block as |
| Version         |         |           | "#.#" where # is a digit; see       |
|                 |         |           | section 1 for the correct digits to |
|                 |         |           | use.                                |
+-----------------+---------+-----------+-------------------------------------+
| specificProblem | string  | Yes       | Description of the alarm or problem |
|                 |         |           | (e.g., ‘eNodeB 155197 in PLMN       |
|                 |         |           | 310-410 with eNodeB name KYL05197 is|
|                 |         |           | lost’). 3GPP probable cause would be|
|                 |         |           | included in this field.             |
+-----------------+---------+-----------+-------------------------------------+
| vfStatus        | string  | Yes       | Virtual function status enumeration:|
|                 |         |           | ‘Active’, ‘Idle’, ‘Preparing to     |
|                 |         |           | terminate’, ‘Ready to terminate’,   |
|                 |         |           | ‘Requesting Termination’            |
+-----------------+---------+-----------+-------------------------------------+

Heartbeat’ Domain Datatypes
+++++++++++++++++++++++++++

Datatype: heartbeatFields
*************************

The heartbeatFields datatype is an optional field block for fields
specific to heartbeat events; it consists of the following fields:

+---------------+---------+-----------+---------------------------------------+
| Field         | Type    | Required? | Description                           |
+===============+=========+===========+=======================================+
| additional\   | hashMap | No        | Additional expansion fields if needed |
| Fields        |         |           |                                       |
+---------------+---------+-----------+---------------------------------------+
| heartbeat\    | string  | Yes       | Version of the heartbeatFields block  |
| FieldsVersion |         |           | as "#.#" where # is a digit; see      |
|               |         |           | section 1 for the correct digits to   |
|               |         |           | use.                                  |
+---------------+---------+-----------+---------------------------------------+
| heartbeat\    | Integer | Yes       | Current heartbeatInterval in seconds  |
| Interval      |         |           |                                       |
+---------------+---------+-----------+---------------------------------------+

‘Measurements’ Domain Datatypes
+++++++++++++++++++++++++++++++

Note: NFs are required to report exactly one Measurement event per
period per sourceName.

Datatype: codecsInUse
*********************

The codecsInUse datatype consists of the following fields describing the
number of times an identified codec was used over the
measurementInterval:

+------------------+-----------+----------+--------------------------------+
| Field            | Type      | Required?| Description                    |
+==================+===========+==========+================================+
| codecIdentifer   | string    | Yes      | Description of the codec       |
+------------------+-----------+----------+--------------------------------+
| numberInUse      | integer   | Yes      | Number of such codecs in use   |
+------------------+-----------+----------+--------------------------------+

Datatype: cpuUsage
******************

The cpuUsage datatype defines the usage of an identifier CPU and
consists of the following fields:

+------------+--------+-----------+-------------------------------------------+
| Field      | Type   | Required? | Description                               |
+============+========+===========+===========================================+
| cpu\       | number | No        | The amount of time the CPU cannot run due |
| Capacity\  |        |           | to contention, in milliseconds over the   |
| Contention |        |           | measurementInterval                       |
+------------+--------+-----------+-------------------------------------------+
| cpu\       | number | No        | The total CPU time that the NF/NFC/VM     |
| Demand\    |        |           | could use if there was no contention, in  |
| Avg        |        |           | milliseconds over the measurementInterval |
+------------+--------+-----------+-------------------------------------------+
| cpu\       | number | No        | CPU demand in MHz                         |
| Demand\    |        |           |                                           |
| Mhz        |        |           |                                           |
+------------+--------+-----------+-------------------------------------------+
| cpu\       | number | No        | CPU demand as a percentage of the         |
| Demand\    |        |           | provisioned capacity                      |
| Pct        |        |           |                                           |
+------------+--------+-----------+-------------------------------------------+
| cpu\       | string | Yes       | CPU Identifier                            |
| Identifier |        |           |                                           |
+------------+--------+-----------+-------------------------------------------+
| cpu\       | number | No        | Percentage of CPU time spent in the idle  |
| Idle       |        |           | task                                      |
+------------+--------+-----------+-------------------------------------------+
| cpu\       | number | No        | Percentage of time the VM is unable to run|
| Latency\   |        |           | because it is contending for access to the|
| Avg        |        |           | physical CPUs                             |
+------------+--------+-----------+-------------------------------------------+
| cpu\       | number | No        | The overhead demand above available       |
| Overhead\  |        |           | allocations and reservations, in          |
| Avg        |        |           | milliseconds over the measurementInterval |
+------------+--------+-----------+-------------------------------------------+
| cpuSwap\   | number | No        | Swap wait time, in milliseconds over the  |
| WaitTime   |        |           | measurementInterval                       |
+------------+--------+-----------+-------------------------------------------+
| cpuUsage\  | number | No        | Percentage of time spent servicing        |
| Interrupt  |        |           | interrupts                                |
+------------+--------+-----------+-------------------------------------------+
| cpuUsage\  | number | No        | Percentage of time spent running user     |
| Nice       |        |           | space processes that have been niced      |
+------------+--------+-----------+-------------------------------------------+
| cpuUsage\  | number | No        | Percentage of time spent handling soft irq|
| SoftIrq    |        |           | interrupts                                |
+------------+--------+-----------+-------------------------------------------+
| cpuUsage\  | number | No        | Percentage of time spent in involuntary   |
| Steal      |        |           | wait which is neither user, system or idle|
|            |        |           | time and is effectively time that went    |
|            |        |           | missing                                   |
+------------+--------+-----------+-------------------------------------------+
| cpuUsage\  | number | No        | Percentage of time spent on system tasks  |
| System     |        |           | running the kernel                        |
+------------+--------+-----------+-------------------------------------------+
| cpuUsage\  | number | No        | Percentage of time spent running un-niced |
| User       |        |           | user space processes                      |
+------------+--------+-----------+-------------------------------------------+
| cpuWait    | number | No        | Percentage of CPU time spent waiting for  |
|            |        |           | I/O operations to complete                |
+------------+--------+-----------+-------------------------------------------+
| percent\   | number | Yes       | Aggregate cpu usage of the virtual machine|
| Usage      |        |           | on which the xNFC reporting the event is  |
|            |        |           | running                                   |
+------------+--------+-----------+-------------------------------------------+

Datatype: diskUsage
*******************

The diskUsage datatype defines the usage of a disk and consists of the
following fields:

+-------------+-------+----------+--------------------------------------------+
| Field       | Type  | Required?| Description                                |
+=============+=======+==========+============================================+
| diskBus\    | number| No       | Number of bus resets over the              |
| Resets      |       |          | measurementInterval                        |
+-------------+-------+----------+--------------------------------------------+
| disk\       | number| No       | Number of disk commands aborted over the   |
| Commands\   |       |          | measurementInterval                        |
| Aborted     |       |          |                                            |
+-------------+-------+----------+--------------------------------------------+
| disk\       | number| No       | Average number of commands per second over |
| CommandsAvg |       |          | the measurementInterval                    |
+-------------+-------+----------+--------------------------------------------+
| diskFlush\  | number| No       | Total flush requests of the disk cache over|
| Requests    |       |          | the measurementInterval                    |
+-------------+-------+----------+--------------------------------------------+
| diskFlush\  | number| No       | Milliseconds spent on disk cache flushing  |
| Time        |       |          | over the measurementInterval               |
+-------------+-------+----------+--------------------------------------------+
| disk\       | string| Yes      | Disk Identifier                            |
| Identifier  |       |          |                                            |
+-------------+-------+----------+--------------------------------------------+
| diskIo\     | number| No       | Milliseconds spent doing input/output      |
| TimeAvg     |       |          | operations over 1 sec; treat this metric as|
|             |       |          | a device load percentage where 1000ms      |
|             |       |          | matches 100% load; provide the average over|
|             |       |          | the measurement interval                   |
+-------------+-------+----------+--------------------------------------------+
| diskIoTime\ | number| No       | Milliseconds spent doing input/output      |
| Last        |       |          | operations over 1 sec; treat this metric as|
|             |       |          | a device load percentage where 1000ms      |
|             |       |          | matches 100% load; provide the last value  |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskIo\     | number| No       | Milliseconds spent doing input/output      |
| TimeMax     |       |          | operations over 1 sec; treat this metric as|
|             |       |          | a device load percentage where 1000ms      |
|             |       |          | matches 100% load; provide the maximum     |
|             |       |          | value measurement within the measurement   |
|             |       |          | interval                                   |
+-------------+-------+----------+--------------------------------------------+
| diskIo\     | number| No       | Milliseconds spent doing input/output      |
| TimeMin     |       |          | operations over 1 sec; treat this metric as|
|             |       |          | a device load percentage where 1000ms      |
|             |       |          | matches 100% load; provide the minimum     |
|             |       |          | value measurement within the measurement   |
|             |       |          | interval                                   |
+-------------+-------+----------+--------------------------------------------+
| diskMerged\ | number| No       | Number of logical read operations that were|
| ReadAvg     |       |          | merged into physical read operations, e.g.,|
|             |       |          | two logical reads were served by one       |
|             |       |          | physical disk access; provide the average  |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskMerged\ | number| No       | Number of logical read operations that were|
| ReadLast    |       |          | merged into physical read operations, e.g.,|
|             |       |          | two logical reads were served by one       |
|             |       |          | physical disk access; provide the last     |
|             |       |          | value measurement within the measurement   |
|             |       |          | interval                                   |
+-------------+-------+----------+--------------------------------------------+
| diskMerged\ | number| No       | Number of logical read operations that were|
| ReadMax     |       |          | merged into physical read operations, e.g.,|
|             |       |          | two logical reads were served by one       |
|             |       |          | physical disk access; provide the maximum  |
|             |       |          | value measurement within the measurement   |
|             |       |          | interval                                   |
+-------------+-------+----------+--------------------------------------------+
| diskMerged\ | number| No       | Number of logical read operations that were|
| ReadMin     |       |          | merged into physical read operations, e.g.,|
|             |       |          | two logical reads were served by one       |
|             |       |          | physical disk access; provide the minimum  |
|             |       |          | value measurement within the measurement   |
|             |       |          | interval                                   |
+-------------+-------+----------+--------------------------------------------+
| diskMerged\ | number| No       | Number of logical write operations that    |
| WriteAvg    |       |          | were merged into physical write operations,|
|             |       |          | e.g., two logical writes were served by one|
|             |       |          | physical disk access; provide the average  |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskMerged\ | number| No       | Number of logical write operations that    |
| WriteLast   |       |          | were merged into physical write operations,|
|             |       |          | e.g., two logical writes were served by one|
|             |       |          | physical disk access; provide the last     |
|             |       |          | value measurement within the measurement   |
|             |       |          | interval                                   |
+-------------+-------+----------+--------------------------------------------+
| diskMerged\ | number| No       | Number of logical write operations that    |
| WriteMax    |       |          | were merged into physical write operations,|
|             |       |          | e.g., two logical writes were served by one|
|             |       |          | physical disk access; provide the maximum  |
|             |       |          | value measurement within the measurement   |
|             |       |          | interval                                   |
+-------------+-------+----------+--------------------------------------------+
| diskMerged\ | number| No       | Number of logical write operations that    |
| WriteMin    |       |          | were merged into physical write operations,|
|             |       |          | e.g., two logical writes were served by one|
|             |       |          | physical disk access; provide the minimum  |
|             |       |          | value measurement within the measurement   |
|             |       |          | interval                                   |
+-------------+-------+----------+--------------------------------------------+
| diskOctets\ | number| No       | Number of octets per second read from a    |
| Read Avg    |       |          | disk or partition; provide the average     |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOctets\ | number| No       | Number of octets per second read from a    |
| Read        |       |          | disk or partition; provide the last        |
|             |       |          | measurement within the measurement interval|
| Last        |       |          |                                            |
+-------------+-------+----------+--------------------------------------------+
| diskOctets\ | number| No       | Number of octets per second read from a    |
| Read Max    |       |          | disk or partition; provide the maximum     |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOctets\ | number| No       | Number of octets per second read from a    |
| Read Min    |       |          | disk or partition; provide the minimum     |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOctets\ | number| No       | Number of octets per second written to a   |
| Write Avg   |       |          | disk or partition; provide the average     |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOctets\ | number| No       | Number of octets per second written to a   |
| Write Last  |       |          | disk or partition; provide the last        |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOctets\ | number| No       | Number of octets per second written to a   |
| WriteMax    |       |          | disk or partition; provide the maximum     |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOctets\ | number| No       | Number of octets per second written to a   |
| WriteMin    |       |          | disk or partition; provide the minimum     |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOps\    | number| No       | Number of read operations per second issued|
| ReadAvg     |       |          | to the disk; provide the average           |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOps\    | number| No       | Number of read operations per second issued|
| ReadLast    |       |          | to the disk; provide the last measurement  |
|             |       |          | within the measurement interval            |
+-------------+-------+----------+--------------------------------------------+
| diskOps\    | number| No       | Number of read operations per second issued|
| ReadMax     |       |          | to the disk; provide the maximum           |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOps\    | number| No       | Number of read operations per second issued|
| ReadMin     |       |          | to the disk; provide the minimum           |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOps\    | number| No       | Number of write operations per second      |
| WriteAvg    |       |          | issued to the disk; provide the average    |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOps\    | number| No       | Number of write operations per second      |
| WriteLast   |       |          | issued to the disk; provide the last       |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOps\    | number| No       | Number of write operations per second      |
| Write Max   |       |          | issued to the disk; provide the maximum    |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskOps\    | number| No       | Number of write operations per second      |
| WriteMin    |       |          | issued to the disk; provide the minimum    |
|             |       |          | measurement within the measurement interval|
+-------------+-------+----------+--------------------------------------------+
| diskPending\| number| No       | Queue size of pending I/O operations per   |
| Operations\ |       |          | second; provide the average measurement    |
| Avg         |       |          | within the measurement interval            |
+-------------+-------+----------+--------------------------------------------+
| diskPending\| number| No       | Queue size of pending I/O operations per   |
| Operations\ |       |          | second; provide the last measurement within|
| Last        |       |          | the measurement interval                   |
+-------------+-------+----------+--------------------------------------------+
| diskPending\| number| No       | Queue size of pending I/O operations per   |
| Operations\ |       |          | second; provide the maximum measurement    |
| Max         |       |          | within the measurement interval            |
+-------------+-------+----------+--------------------------------------------+
| diskPending\| number| No       | Queue size of pending I/O operations per   |
| Operations\ |       |          | second; provide the minimum measurement    |
| Min         |       |          | within the measurement interval            |
+-------------+-------+----------+--------------------------------------------+
| diskRead\   | number| No       | Average number of read commands issued per |
| CommandsAvg |       |          | second to the disk over the                |
|             |       |          | measurementInterval                        |
+-------------+-------+----------+--------------------------------------------+
| diskTime    | number| No       | Nanoseconds spent on disk cache            |
|             |       |          | reads/writes within the measurement        |
|             |       |          | interval                                   |
+-------------+-------+----------+--------------------------------------------+
| diskTime\   | number| No       | Milliseconds a read operation took to      |
| ReadAvg     |       |          | complete; provide the average measurement  |
|             |       |          | within the measurement interval            |
+-------------+-------+----------+--------------------------------------------+
| diskTime\   | number| No       | Milliseconds a read operation took to      |
| Read Last   |       |          | complete; provide the last measurement     |
|             |       |          | within the measurement interval            |
+-------------+-------+----------+--------------------------------------------+
| diskTime\   | number| No       | Milliseconds a read operation took to      |
| Read Max    |       |          | complete; provide the maximum measurement  |
|             |       |          | within the measurement interval            |
+-------------+-------+----------+--------------------------------------------+
| diskTime\   | number| No       | Milliseconds a read operation took to      |
| Read Min    |       |          | complete; provide the minimum measurement  |
|             |       |          | within the measurement interval            |
+-------------+-------+----------+--------------------------------------------+
| diskTime\   | number| No       | Milliseconds a write operation took to     |
| Write Avg   |       |          | complete; provide the average measurement  |
|             |       |          | within the measurement interval            |
+-------------+-------+----------+--------------------------------------------+
| diskTime\   | number| No       | Milliseconds a write operation took to     |
| Write Last  |       |          | complete; provide the last measurement     |
|             |       |          | within the measurement interval            |
+-------------+-------+----------+--------------------------------------------+
| diskTime\   | number| No       | Milliseconds a write operation took to     |
| Write Max   |       |          | complete; provide the maximum measurement  |
|             |       |          | within the measurement interval            |
+-------------+-------+----------+--------------------------------------------+
| diskTime\   | number| No       | Milliseconds a write operation took to     |
| Write Min   |       |          | complete; provide the minimum measurement  |
|             |       |          | within the measurement interval            |
+-------------+-------+----------+--------------------------------------------+
| diskTotal\  | number| No       | Average read time from the perspective of a|
| ReadLatency\|       |          | Guest OS: sum of the Kernel Read Latency   |
| Avg         |       |          | and Physical Device Read Latency in        |
|             |       |          | milliseconds over the measurement interval |
+-------------+-------+----------+--------------------------------------------+
| diskTotal\  | number| No       | Average write time from the perspective of |
| Write\      |       |          | a Guest OS: sum of the Kernel Write Latency|
| LatencyAvg  |       |          | and Physical Device Write Latency in       |
|             |       |          | milliseconds over the measurement interval |
+-------------+-------+----------+--------------------------------------------+
| disk\       | number| No       | Measure in ms over 1 sec of both I/O       |
| WeightedIo\ |       |          | completion time and the backlog that may be|
| TimeAvg     |       |          | accumulating. Value is the average within  |
|             |       |          | the collection interval.                   |
+-------------+-------+----------+--------------------------------------------+
| disk\       | number| No       | Measure in ms over 1 sec of both I/O       |
| WeightedIo\ |       |          | completion time and the backlog that may be|
| TimeLast    |       |          | accumulating. Value is the last within the |
|             |       |          | collection interval.                       |
+-------------+-------+----------+--------------------------------------------+
| disk\       | number| No       | Measure in ms over 1 sec of both I/O       |
| WeightedIo\ |       |          | completion time and the backlog that may be|
| TimeMax     |       |          | accumulating. Value is the maximum within  |
|             |       |          | the collection interval.                   |
+-------------+-------+----------+--------------------------------------------+
| disk\       | number| No       | Measure in ms over 1 sec of both I/O       |
| WeightedIo\ |       |          | completion time and the backlog that may be|
| TimeMin     |       |          | accumulating. Value is the minimum within  |
|             |       |          | the collection interval.                   |
+-------------+-------+----------+--------------------------------------------+
| diskWrite\  | number| No       | Average number of write commands issued per|
| CommandsAvg |       |          | second to the disk over the                |
|             |       |          | measurementInterval                        |
+-------------+-------+----------+--------------------------------------------+

Datatype: filesystemUsage
*************************

The filesystemUsage datatype consists of the following fields:

+-------------+--------+-----------+------------------------------------------+
| Field       | Type   | Required? | Description                              |
+=============+========+===========+==========================================+
| filesystem\ | string | Yes       | File system name                         |
| Name        |        |           |                                          |
+-------------+--------+-----------+------------------------------------------+
| block\      | number | Yes       | Configured block storage capacity in GB  |
| Configured  |        |           |                                          |
+-------------+--------+-----------+------------------------------------------+
| blockIops   | number | Yes       | Block storage input-output operations per|
|             |        |           | second                                   |
+-------------+--------+-----------+------------------------------------------+
| blockUsed   | number | Yes       | Used block storage capacity in GB        |
+-------------+--------+-----------+------------------------------------------+
| ephemeral\  | number | Yes       | Configured ephemeral storage capacity in |
| Configured  |        |           | GB                                       |
+-------------+--------+-----------+------------------------------------------+
| ephemeral\  | number | Yes       | Ephemeral storage input-output operations|
| Iops        |        |           | per second                               |
+-------------+--------+-----------+------------------------------------------+
| ephemeral\  | number | Yes       | Used ephemeral storage capacity in GB    |
| Used        |        |           |                                          |
+-------------+--------+-----------+------------------------------------------+

Datatype: hugePages
*******************

The hugePages datatype provides metrics on system hugePages; it consists
of the following fields:

+--------------------+--------+----------+------------------------------------+
| Field              | Type   | Required?| Description                        |
+====================+========+==========+====================================+
| bytesFree          | number | No       | Number of free hugePages in bytes  |
+--------------------+--------+----------+------------------------------------+
| bytesUsed          | number | No       | Number of used hugePages in bytes  |
+--------------------+--------+----------+------------------------------------+
| hugePagesIdentifier| string | Yes      | HugePages identifier               |
+--------------------+--------+----------+------------------------------------+
| percentFree        | number | No       | Number of free hugePages in percent|
+--------------------+--------+----------+------------------------------------+
| percentUsed        | number | No       | Number of used hugePages in percent|
+--------------------+--------+----------+------------------------------------+
| vmPageNumberFree   | number | No       | Number of free vmPages in numbers  |
+--------------------+--------+----------+------------------------------------+
| vmPageNumberUsed   | number | No       | Number of used vmPages in numbers  |
+--------------------+--------+----------+------------------------------------+

Datatype: ipmi (Intelligent Platform Management Interface)
**********************************************************

The ipmi datatype provides intelligent platform management interface
metrics; it consists of the following fields:

+-------------+---------------------+-----------+-----------------------------+
| Field       | Type                | Required? | Description                 |
+=============+=====================+===========+=============================+
| exitAir\    | number              | No        | System fan exit air flow    |
| Temperature |                     |           | temperature in Celsius      |
+-------------+---------------------+-----------+-----------------------------+
| frontPanel\ | number              | No        | Front panel temp in Celsius |
| Temperature |                     |           |                             |
+-------------+---------------------+-----------+-----------------------------+
| ioModule\   | number              | No        | Io module temp in Celsius   |
| Temperature |                     |           |                             |
+-------------+---------------------+-----------+-----------------------------+
| ipmi\       | ipmiBaseboard       | No        | Array of ipmiBaseboard      |
| Baseboard\  | Temperature [ ]     |           | Temperature objects         |
| Temperature\|                     |           |                             |
| Array       |                     |           |                             |
+-------------+---------------------+-----------+-----------------------------+
| ipmi\       | ipmiBaseboard       | No        | Array of ipmiBaseboard      |
| Baseboard\  | VoltageRegulator [ ]|           | VoltageRegulator objects    |
| Voltage\    |                     |           |                             |
| Regulator   |                     |           |                             |
| Array       |                     |           |                             |
+-------------+---------------------+-----------+-----------------------------+
| ipmiBattery\| ipmiBattery [ ]     | No        | Array of ipmiBattery objects|
| Array       |                     |           |                             |
+-------------+---------------------+-----------+-----------------------------+
| ipmiFanArray| ipmiFan [ ]         | No        | Array of ipmiFan objects    |
+-------------+---------------------+-----------+-----------------------------+
| ipmiGlobal\ | ipmiGlobalAggregate\| No        | ipmi global aggregate       |
| Aggregate\  | TemperatureMargin []|           | temperature margin          |
| Temperature\|                     |           |                             |
| MarginArray |                     |           |                             |
+-------------+---------------------+-----------+-----------------------------+
| ipmiHsbp\   | ipmiHsbp [ ]        | No        | Array of ipmiHsbp objects   |
| Array       |                     |           |                             |
+-------------+---------------------+-----------+-----------------------------+
| ipmiNicArray| ipmiNic [ ]         | No        | Array of ipmiNic objects    |
+-------------+---------------------+-----------+-----------------------------+
| ipmiPower\  | ipmiPowerSupply [ ] | No        | Array of ipmiPowerSupply    |
| SupplyArray |                     |           | objects                     |
+-------------+---------------------+-----------+-----------------------------+
| ipmi\       | ipmiProcessor [ ]   | No        | Array of ipmiProcessor      |
| Processor\  |                     |           | objects                     |
| Array       |                     |           |                             |
+-------------+---------------------+-----------+-----------------------------+
| system\     | number              | No        | Airflow in cubic feet per   |
| Airflow     |                     |           | minute (cfm)                |
+-------------+---------------------+-----------+-----------------------------+

Datatype: ipmiBaseboardTemperature
**********************************

The ipmiBaseboardTemperature datatype consists of the following fields
which describe ipmi baseboard temperature metrics:

+-------------+--------+-----------+------------------------------------------+
| Field       | Type   | Required? | Description                              |
+=============+========+===========+==========================================+
| baseboard\  | number | No        | Baseboard temperature in celsius         |
| Temperature |        |           |                                          |
+-------------+--------+-----------+------------------------------------------+
| baseboard\  | string | Yes       | Identifier for the location where the    |
| Temperature\|        |           | temperature is taken                     |
| Identifier  |        |           |                                          |
+-------------+--------+-----------+------------------------------------------+

Datatype: ipmiBaseboardVoltageRegulator
***************************************

The ipmiBaseboardVoltageRegulator datatype consists of the following
fields which describe ipmi baseboard voltage regulator metrics:

+--------------------+-------+----------+-------------------------------------+
| Field              | Type  | Required?| Description                         |
+====================+=======+==========+=====================================+
| baseboardVoltage\  | string| Yes      | Identifier for the baseboard voltage|
| RegulatorIdentifier|       |          | regulator                           |
+--------------------+-------+----------+-------------------------------------+
| voltageRegulator\  | number| No       | Voltage regulator temperature in    |
| Temperature        |       |          | celsius                             |
+--------------------+-------+----------+-------------------------------------+

Datatype: ipmiBattery
*********************

The ipmiBattery datatype consists of the following fields which describe
ipmi battery metrics:

+---------------------+--------+----------+------------------------------+
| Field               | Type   | Required?| Description                  |
+=====================+========+==========+==============================+
| batteryIdentifier   | string | Yes      | Identifier for the battery   |
+---------------------+--------+----------+------------------------------+
| batteryType         | string | No       | Type of battery              |
+---------------------+--------+----------+------------------------------+
| batteryVoltageLevel | number | No       | Battery voltage level        |
+---------------------+--------+----------+------------------------------+

Datatype: ipmiFan
*****************

The ipmiFan datatype consists of the following fields which describe
ipmi fan metrics:

+--------------+-------+----------+-------------------------------------------+
| Field        | Type  | Required?| Description                               |
+==============+=======+==========+===========================================+
| fanIdentifier| string| Yes      | Identifier for the fan                    |
+--------------+-------+----------+-------------------------------------------+
| fanSpeed     | number| No       | Fan speed in revolutions per minute (rpm) |
+--------------+-------+----------+-------------------------------------------+

Datatype: ipmiGlobalAggregateTemperatureMargin
**********************************************

The ipmiGlobalAggregateTemperatureMargin datatype consists of the
following fields:

+-------------+-------+----------+--------------------------------------------+
| Field       | Type  | Required?| Description                                |
+=============+=======+==========+============================================+
| global\     | number| No       | Temperature margin in Celsius relative to a|
| Aggregate\  |       |          | throttling thermal trip point              |
| Temperature\|       |          |                                            |
| Margin      |       |          |                                            |
+-------------+-------+----------+--------------------------------------------+
| global\     | string| Yes      | Identifier for the ipmi global aggregate   |
| Aggregate\  |       |          | temperature margin metrics                 |
| Temperature\|       |          |                                            |
| Margin\     |       |          |                                            |
| Identifier  |       |          |                                            |
+-------------+-------+----------+--------------------------------------------+

Datatype: ipmiHsbp
******************

The ipmiHsbp datatype provides ipmi hot swap backplane power metrics; it
consists of the following fields:

+------------+-------+----------+---------------------------------------------+
| Field      | Type  | Required?| Description                                 |
+============+=======+==========+=============================================+
| hsbp\      | string| Yes      | Identifier for the hot swap backplane power |
| Identifier |       |          | unit                                        |
+------------+-------+----------+---------------------------------------------+
| hsbp\      | number| No       | Hot swap backplane power temperature in     |
| Temperature|       |          | celsius                                     |
+------------+-------+----------+---------------------------------------------+

Datatype: ipmiNic
*****************

The ipmiNic datatype provides network interface control care metrics; it
consists of the following fields:

+------------+-------+----------+---------------------------------------------+
| Field      | Type  | Required?| Description                                 |
+============+=======+==========+=============================================+
| nic\       | string| Yes      | Identifier for the network interface control|
| Identifier |       |          | card                                        |
+------------+-------+----------+---------------------------------------------+
| nic\       | number| No       | nic temperature in Celsius                  |
| Temperature|       |          |                                             |
+------------+-------+----------+---------------------------------------------+

Datatype: ipmiPowerSupply
*************************

The ipmiPowerSupply datatype provides ipmi power supply metrics; it
consists of the following fields:

+-----------+-------+----------+----------------------------------------------+
|Field      | Type  | Required?| Description                                  |
+===========+=======+==========+==============================================+
|power\     | number| No       | Current output voltage as a percentage of the|
|Supply\    |       |          | design specified level                       |
|Current\   |       |          |                                              |
|Output\    |       |          |                                              |
|Percent    |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
|power\     | string| Yes      | Identifier for the power supply              |
|Supply\    |       |          |                                              |
|Identifier |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
|power\     | number| No       | Input power in watts                         |
|Supply\    |       |          |                                              |
|Input\     |       |          |                                              |
|Power      |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
|power\     | number| No       | Power supply temperature in Celsius          |
|Supply\    |       |          |                                              |
|Temperature|       |          |                                              |
+-----------+-------+----------+----------------------------------------------+

Datatype: ipmiProcessor
***********************

The ipmiProcessor datatype provides ipmi processor metrics; it consists
of the following fields:

+------------+------------------+-----------+---------------------------------+
| Field      | Type             | Required? | Description                     |
+============+==================+===========+=================================+
| processor\ | processorDimm    | No        | Array of processorDimmAggregate |
| Dimm\      | AggregateThermal |           | ThermalMargin objects           |
| Aggregate\ | Margin [ ]       |           |                                 |
| Thermal\   |                  |           |                                 |
| MarginArray|                  |           |                                 |
+------------+------------------+-----------+---------------------------------+
| processor\ | number           | No        | Front panel temperature in      |
| DtsThermal\|                  |           | celsius                         |
| Margin     |                  |           |                                 |
+------------+------------------+-----------+---------------------------------+
| processor\ | string           | Yes       | Identifier for the power supply |
| Identifier |                  |           |                                 |
+------------+------------------+-----------+---------------------------------+
| processor\ | number           | No        | Io module temperatue in celsius |
| Thermal\   |                  |           |                                 |
| Control\   |                  |           |                                 |
| Percent    |                  |           |                                 |
+------------+------------------+-----------+---------------------------------+

Datatype: latencyBucketMeasure
******************************

The latencyBucketMeasure datatype consists of the following fields which
describe the number of counts falling within a defined latency bucket:

+-----------+-------+----------+----------------------------------------------+
| Field     | Type  | Required?| Description                                  |
+===========+=======+==========+==============================================+
| counts\   | number| Yes      | Number of counts falling within a defined    |
| InThe\    |       |          | latency bucket                               |
| Bucket    |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| highEnd\  | number| No       | High end of bucket range (typically in ms)   |
| OfLatency\|       |          |                                              |
| Bucket    |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| lowEndOf\ | number| No       | Low end of bucket range (typically in ms)    |
| Latency\  |       |          |                                              |
| Bucket    |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+

Datatype: load
**************

The load datatype provides metrics on system cpu and io utilization
obtained using /proc/loadavg; it consists of the following fields:

+----------+-------+----------+-----------------------------------------------+
| Field    | Type  | Required?| Description                                   |
+==========+=======+==========+===============================================+
| longTerm | number| No       | number of jobs in the run queue (state R, cpu |
|          |       |          | utilization) or waiting for disk I/O (state D,|
|          |       |          | io utilization) averaged over 15 minutes using|
|          |       |          | /proc/loadavg                                 |
+----------+-------+----------+-----------------------------------------------+
| midTerm  | number| No       | number of jobs in the run queue (state R, cpu |
|          |       |          | utilization) or waiting for disk I/O (state D,|
|          |       |          | io utilization) averaged over 5 minutes using |
|          |       |          | /proc/loadavg                                 |
+----------+-------+----------+-----------------------------------------------+
| shortTerm| number| No       | number of jobs in the run queue (state R, cpu |
|          |       |          | utilization) or waiting for disk I/O (state D,|
|          |       |          | io utilization) averaged over 1 minute using  |
|          |       |          | /proc/loadavg                                 |
+----------+-------+----------+-----------------------------------------------+

Datatype: machineCheckException
*******************************

The machineCheckException datatype describes machine check exceptions;
it consists of the following fields:

+-------------+-------+----------+--------------------------------------------+
| Field       | Type  | Required?| Description                                |
+=============+=======+==========+============================================+
| corrected\  | number| No       | Total hardware errors that were corrected  |
| Memory\     |       |          | by the hardware (e.g. data corruption      |
| Errors      |       |          | corrected via  ECC) over the               |
|             |       |          | measurementInterval. These errors do not   |
|             |       |          | require immediate software actions, but are|
|             |       |          | still reported for accounting and          |
|             |       |          | predictive failure analysis                |
+-------------+-------+----------+--------------------------------------------+
| corrected\  | number| No       | Total hardware errors that were corrected  |
| Memory\     |       |          | by the hardware over the last one hour     |
| Errors      |       |          |                                            |
| In1Hr       |       |          |                                            |
+-------------+-------+----------+--------------------------------------------+
| uncorrected\| number| No       | Total uncorrected hardware errors that were|
| Memory\     |       |          | detected by the hardware (e.g., causing    |
| Errors      |       |          | data corruption) over the                  |
|             |       |          | measurementInterval. These errors require a|
|             |       |          | software response.                         |
+-------------+-------+----------+--------------------------------------------+
| uncorrected\| number| No       | Total uncorrected hardware errors that were|
| Memory\     |       |          | detected by the hardware over the last one |
| Errors      |       |          | hour                                       |
| In1Hr       |       |          |                                            |
+-------------+-------+----------+--------------------------------------------+
| vm\         | string| Yes      | Virtual machine identifier associated with |
| Identifier  |       |          | the machine check exception                |
+-------------+-------+----------+--------------------------------------------+

Datatype: measurementFields
***************************

The ``measurementFields`` datatype consists of the following fields:

+-------------+--------------+----------+-------------------------------------+
| Field       | Type         | Required?| Description                         |
+=============+==============+==========+=====================================+
| additional\ | hashMap      | No       | Additional measurement fields if    |
| Fields      |              |          | needed                              |
+-------------+--------------+----------+-------------------------------------+
| additional\ | arrayOfNamed\| No       | Array of named hashMap if needed    |
| Measurements| HashMap      |          |                                     |
+-------------+--------------+----------+-------------------------------------+
| additional\ | arrayOf\     | No       | Array of JSON objects described by  |
| Objects     | JsonObject   |          | name, schema and other              |
|             |              |          | meta-information, if needed         |
+-------------+--------------+----------+-------------------------------------+
| codec\      | codecs\      | No       | Array of codecs in use              |
| Usage\      | InUse []     |          |                                     |
| Array       |              |          |                                     |
+-------------+--------------+----------+-------------------------------------+
| concurrent\ | integer      | No       | Peak concurrent sessions for the VM |
| Sessions    |              |          | or xNF (depending on the context)   |
|             |              |          | over the measurementInterval        |
+-------------+--------------+----------+-------------------------------------+
| configured\ | integer      | No       | Depending on the context over the   |
| Entities    |              |          | measurementInterval: peak total     |
|             |              |          | number of users, subscribers,       |
|             |              |          | devices, adjacencies, etc., for the |
|             |              |          | VM, or peak total number of         |
|             |              |          | subscribers, devices, etc., for the |
|             |              |          | xNF                                 |
+-------------+--------------+----------+-------------------------------------+
| cpuUsage\   | cpuUsage []  | No       | Usage of an array of CPUs           |
| Array       |              |          |                                     |
+-------------+--------------+----------+-------------------------------------+
| diskUsage\  | diskUsage [] | No       | Usage of an array of disks          |
| Array       |              |          |                                     |
+-------------+--------------+----------+-------------------------------------+
| feature\    | hashMap      | No       | The hashMap key should identify the |
| UsageArray  |              |          | feature, while the value defines the|
|             |              |          | number of times the identified      |
|             |              |          | feature was used                    |
+-------------+--------------+----------+-------------------------------------+
| filesystem\ | filesystem\  | No       | Filesystem usage of the VM on which |
| UsageArray  | Usage [ ]    |          | the xNFC reporting the event is     |
|             |              |          | running                             |
+-------------+--------------+----------+-------------------------------------+
| hugePages\  | hugePages [ ]| No       | Array of metrics on hugePages       |
| Array       |              |          |                                     |
+-------------+--------------+----------+-------------------------------------+
| ipmi        | ipmi         | No       | Intelligent platform management     |
|             |              |          | interface metrics                   |
+-------------+--------------+----------+-------------------------------------+
| latency\    | latency\     | No       | Array of integers representing      |
| Distribution| Bucket\      |          | counts of requests whose latency in |
|             | Measure [ ]  |          | milliseconds falls within per-xNF   |
|             |              |          | configured ranges; where latency is |
|             |              |          | the duration between a service      |
|             |              |          | request and its fulfillment.        |
+-------------+--------------+----------+-------------------------------------+
| loadArray   | load [ ]     | No       | Array of system load metrics        |
+-------------+--------------+----------+-------------------------------------+
| machine\    | machine\     | No       | Array of machine check exceptions   |
| Check\      | Check\       |          |                                     |
| Exception\  | Exception [ ]|          |                                     |
| Array       |              |          |                                     |
+-------------+--------------+----------+-------------------------------------+
| mean\       | number       | No       | Mean seconds required to respond to |
| Request\    |              |          | each request for the VM on which the|
| Latency     |              |          | xNFC reporting the event is running |
+-------------+--------------+----------+-------------------------------------+
| measurement\| string       | Yes      | Version of the measurementFields    |
| Fields\     |              |          | block as "#.#" where # is a digit;  |
| Version     |              |          | see section 1 for the correct digits|
|             |              |          | to use.                             |
+-------------+--------------+----------+-------------------------------------+
| measurement\| number       | Yes      | Interval over which measurements are|
| Interval    |              |          | being reported in seconds           |
+-------------+--------------+----------+-------------------------------------+
| memoryUsage\| memory\      | No       | Memory usage of an array of VMs     |
| Array       | Usage []     |          |                                     |
+-------------+--------------+----------+-------------------------------------+
| nfcScaling\ | integer      | No       | Represents busy-ness of the network |
| Metric      |              |          | function from 0 to 100 as reported  |
|             |              |          | by the nfc                          |
+-------------+--------------+----------+-------------------------------------+
| nic\        | nic\         | No       | Performance metrics of an array of  |
| Performance\| Performance  |          | network interface cards             |
| Array       | [ ]          |          |                                     |
+-------------+--------------+----------+-------------------------------------+
| numberOf\   | integer      | No       | Number of media ports in use        |
| MediaPorts\ |              |          |                                     |
| InUse       |              |          |                                     |
+-------------+--------------+----------+-------------------------------------+
| process\    | process\     | No       | Array of metrics on system processes|
| StatsArray  | Stats [ ]    |          |                                     |
+-------------+--------------+----------+-------------------------------------+
| request\    | number       | No       | Peak rate of service requests per   |
| Rate        |              |          | second to the xNF over the          |
|             |              |          | measurementInterval                 |
+-------------+--------------+----------+-------------------------------------+


Note on Measurement Expansion Fields
""""""""""""""""""""""""""""""""""""

The ``measurementFields`` data type provides fields that can be used to
pass additional data with the event. These fields are listed below and
referred to as expansion fields:

* ``additionalFields``
* ``additionalObjects``
* ``additionalMeasurements``

When expansion fields are used, the goal is to avoid custom development
by the service provider collecting the fields, since custom development
adds obvious cost, delay and resource overhead. In the domain of
measurements, it is expected that a high percentage of use cases for
extensible fields can be satisfied by using the ``additionalMeasurements``
``arrayOfNamedHashMap`` data structure in combination with a YAML registration
file (provided at design time). The YAML registration file conveys
metadata about the processing of ``additionalMeasurements``. For more
information, please see the VES Event Registration specification and in
particular the ``aggregationRole``, ``castTo``, and ``isHomogeneous`` keywords.

Datatype: memoryUsage
*********************

The memoryUsage datatype defines the memory usage of a virtual machine
and consists of the following fields:

+-----------+-------+----------+----------------------------------------------+
| Field     | Type  | Required?| Description                                  |
+===========+=======+==========+==============================================+
| memory\   | number| No       | Kibibytes of temporary storage for raw disk  |
| Buffered  |       |          | blocks                                       |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| No       | Kibibytes of memory used for cache           |
| Cached    |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| No       | Kibibytes of memory configured in the virtual|
| Configured|       |          | machine on which the xNFC reporting the event|
|           |       |          | is running                                   |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| No       | Host demand in kibibytes                     |
| Demand    |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| Yes      | Kibibytes of physical RAM left unused by the |
| Free      |       |          | system                                       |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| No       | Percentage of time the VM is waiting to      |
| Latency\  |       |          | access swapped or compressed memory          |
| Avg       |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| No       | Shared memory in kilobytes                   |
| Shared\   |       |          |                                              |
| Avg       |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| No       | The part of the slab that can be reclaimed   |
| SlabRecl  |       |          | such as caches measured in kibibytes         |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| No       | The part of the slab that cannot be reclaimed|
| Slab\     |       |          | even when lacking memory measure in kibibytes|
| Unrecl    |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| No       | Amount of memory swapped-in from host cache  |
| SwapIn\   |       |          | in kibibytes                                 |
| Avg       |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| No       | Rate at which memory is swapped from disk    |
| SwapIn\   |       |          | into active memory during the interval in    |
| RateAvg   |       |          | kilobytes per second                         |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| No       | Amount of memory swapped-out to host cache in|
| SwapOut\  |       |          | kibibytes                                    |
| Avg       |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| No       | Rate at which memory is being swapped from   |
| SwapOut\  |       |          | active memory to disk during the current     |
| RateAvg   |       |          | interval in kilobytes per second             |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| No       | Space used for caching swapped pages in the  |
| Swap\     |       |          | host cache in kibibytes                      |
| UsedAvg   |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| memory\   | number| Yes      | Total memory minus the sum of free, buffered,|
| Used      |       |          | cached and slab memory measured in kibibytes |
+-----------+-------+----------+----------------------------------------------+
| percent\  | number| No       | Percentage of memory usage; value =          |
| Memory\   |       |          | (memoryUsed / (memoryUsed + memoryFree) x 100|
| Usage     |       |          | if denomintor is nonzero, or 0, if otherwise.|
+-----------+-------+----------+----------------------------------------------+
| vm\       | string| Yes      | Virtual Machine identifier associated with   |
| Identifier|       |          | the memory metrics                           |
+-----------+-------+----------+----------------------------------------------+

Datatype: nicPerformance
************************

The nicPerformance datatype consists of the following fields which
describe the performance and errors of an of an identified virtual
network interface card:

+----------------+-------+----------+-----------------------------------------+
| Field          | Type  | Required?| Description                             |
+================+=======+==========+=========================================+
| administrative\| string| No       | Administrative state: enum: ‘inService’,|
| State          |       |          | ‘outOfService’                          |
+----------------+-------+----------+-----------------------------------------+
| nicIdentifier  | string| Yes      | Network interface card identifier       |
+----------------+-------+----------+-----------------------------------------+
| operational\   | string| No       | Operational state: enum: ‘inService’,   |
| State          |       |          | ‘outOfService’                          |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Cumulative count of broadcast packets   |
| Broadcast\     |       |          | received as read at the end of the      |
| Packets\       |       |          | measurement interval                    |
| Accumulated    |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Count of broadcast packets received     |
| Broadcast\     |       |          | within the measurement interval         |
| PacketsDelta   |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Cumulative count of discarded packets   |
| Discarded\     |       |          | received as read at the end of the      |
| Packets\       |       |          | measurement interval                    |
| Accumulated    |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Count of discarded packets received     |
| Discarded\     |       |          | within the measurement interval         |
| PacketsDelta   |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Cumulative count of error packets       |
| ErrorPackets\  |       |          | received as read at the end of the      |
| Accumulated    |       |          | measurement interval                    |
+----------------+-------+----------+-----------------------------------------+
| receivedError\ | number| No       | Count of error packets received within  |
| PacketsDelta   |       |          | the measurement interval                |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Cumulative count of multicast packets   |
| Multicast\     |       |          | received as read at the end of the      |
| Packets\       |       |          | measurement interval                    |
| Accumulated    |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Count of multicast packets received     |
| Multicast\     |       |          | within the measurement interval         |
| PacketsDelta   |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Cumulative count of octets received as  |
| Octets\        |       |          | read at the end of the measurement      |
| Accumulated    |       |          | interval                                |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Count of octets received within the     |
| OctetsDelta    |       |          | measurement interval                    |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Percentage of discarded packets         |
| Percent\       |       |          | received; value =                       |
| Discard        |       |          | (receivedDiscardedPacketsDelta /        |
|                |       |          | receivedTotalPacketsDelta) x 100, if    |
|                |       |          | denominator is nonzero, or 0, if        |
|                |       |          | otherwise.                              |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Percentage of error packets received;   |
| PercentError   |       |          | value = (receivedErrorPacketsDelta /    |
|                |       |          | receivedTotalPacketsDelta) x 100, if    |
|                |       |          | denominator is nonzero, or 0, if        |
|                |       |          | otherwise.                              |
+----------------+-------+----------+-----------------------------------------+
| receivedTotal\ | number| No       | Cumulative count of all packets received|
| Packets\       |       |          | as read at the end of the measurement   |
| Accumulated    |       |          | interval                                |
+----------------+-------+----------+-----------------------------------------+
| receivedTotal\ | number| No       | Count of all packets received within the|
| PacketsDelta   |       |          | measurement interval                    |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Cumulative count of unicast packets     |
| Unicast\       |       |          | received as read at the end of the      |
| Packets\       |       |          | measurement interval                    |
| Accumulated    |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Count of unicast packets received within|
| Unicast\       |       |          | the measurement interval                |
| PacketsDelta   |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| received\      | number| No       | Percentage of utilization received;     |
| Utilization    |       |          | value = (receivedOctetsDelta / (speed x |
|                |       |          | (lastEpochMicrosec - startEpochMicrosec)|
|                |       |          | )) x 100, if denominator is nonzero, or |
|                |       |          | 0, if otherwise.                        |
+----------------+-------+----------+-----------------------------------------+
| speed          | number| No       | Speed configured in mbps.               |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Cumulative count of broadcast packets   |
| Broadcast\     |       |          | transmitted as read at the end of the   |
| Packets\       |       |          | measurement interval                    |
| Accumulated    |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Count of broadcast packets transmitted  |
| Broadcast\     |       |          | within the measurement interval         |
| PacketsDelta   |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Cumulative count of discarded packets   |
| Discarded\     |       |          | transmitted as read at the end of the   |
| Packets\       |       |          | measurement interval                    |
| Accumulated    |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Count of discarded packets transmitted  |
| Discarded\     |       |          | within the measurement interval         |
| PacketsDelta   |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Cumulative count of error packets       |
| ErrorPackets\  |       |          | transmitted as read at the end of the   |
| Accumulated    |       |          | measurement interval                    |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Count of error packets transmitted      |
| ErrorPackets\  |       |          | within the measurement interval         |
| Delta          |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Cumulative count of multicast packets   |
| Multicast\     |       |          | transmitted as read at the end of the   |
| Packets\       |       |          | measurement interval                    |
| Accumulated    |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Count of multicast packets transmitted  |
| Multicast\     |       |          | within the measurement interval         |
| PacketsDelta   |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Cumulative count of octets transmitted  |
| Octets\        |       |          | as read at the end of the measurement   |
| Accumulated    |       |          | interval                                |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Count of octets transmitted within the  |
| OctetsDelta    |       |          | measurement interval                    |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Percentage of discarded packets         |
| PercentDiscard |       |          | transmitted; value =                    |
|                |       |          | (transmittedDiscardedPacketsDelta /     |
|                |       |          | transmittedTotalPacketsDelta) x 100, if |
|                |       |          | denominator is nonzero, or 0, if        |
|                |       |          | otherwise.                              |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Percentage of error packets received;   |
| PercentError   |       |          | value = (transmittedErrorPacketsDelta / |
|                |       |          | transmittedTotalPacketsDelta) x 100, if |
|                |       |          | denominator is nonzero, or 0, if        |
|                |       |          | otherwise.                              |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Cumulative count of all packets         |
| TotalPackets\  |       |          | transmitted as read at the end of the   |
| Accumulated    |       |          | measurement interval                    |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Count of all packets transmitted within |
| TotalPackets\  |       |          | the measurement interval                |
| Delta          |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Cumulative count of unicast packets     |
| Unicast\       |       |          | transmitted as read at the end of the   |
| Packets\       |       |          | measurement interval                    |
| Accumulated    |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Count of unicast packets transmitted    |
| Unicast\       |       |          | within the measurement interval         |
| PacketsDelta   |       |          |                                         |
+----------------+-------+----------+-----------------------------------------+
| transmitted\   | number| No       | Percentage of utilization transmitted;  |
| Utilization    |       |          | value = (transmittedOctetsDelta / (speed|
|                |       |          | x (lastEpochMicrosec -                  |
|                |       |          | startEpochMicrosec))) x 100, if         |
|                |       |          | denominator is nonzero, or 0, if        |
|                |       |          | otherwise.                              |
+----------------+-------+----------+-----------------------------------------+
| values\        | string| Yes      | Enumeration: ‘true’ or ‘false’. If      |
| AreSuspect     |       |          | ‘true’ then the vNicPerformance values  |
|                |       |          | are likely inaccurate due to counter    |
|                |       |          | overflow or other conditions.           |
+----------------+-------+----------+-----------------------------------------+

Datatype: processorDimmAggregateThermalMargin
*********************************************

The processorDimmAggregateThermalMargin datatype provides intelligent
platform management interface (ipmi) processor dual inline memory module
aggregate thermal margin metrics; it consists of the following fields:

+-----------------+-------+----------+----------------------------------------+
| Field           | Type  | Required?| Description                            |
+=================+=======+==========+========================================+
| processor\      | string| Yes      | identifier for the aggregate thermal   |
| DimmAggregate\  |       |          | margin metrics from the processor dual |
| Thermal         |       |          | inline memory module                   |
| MarginIdentifier|       |          |                                        |
+-----------------+-------+----------+----------------------------------------+
| thermalMargin   | number| Yes      | the difference between the DIMM's      |
|                 |       |          | current temperature, in celsius, and   |
|                 |       |          | the DIMM's throttling thermal trip     |
+-----------------+-------+----------+----------------------------------------+

Datatype: processStats
**********************

The processStats datatype provides metrics on system processes; it
consists of the following fields:


+-----------+-------+----------+----------------------------------------------+
| Field     | Type  | Required?| Description                                  |
+===========+=======+==========+==============================================+
| forkRate  | number| No       | The number of threads created since the last |
|           |       |          | reboot                                       |
+-----------+-------+----------+----------------------------------------------+
| process\  | string| Yes      | processIdentifier                            |
| Identifier|       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| psState\  | number| No       | The number of processes in a blocked state   |
| Blocked   |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| psState\  | number| No       | The number of processes in a paging state    |
| Paging    |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| psState\  | number| No       | The number of processes in a running state   |
| Running   |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| psState\  | number| No       | The number of processes in a sleeping state  |
| Sleeping  |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| psState\  | number| No       | The number of processes in a stopped state   |
| Stopped   |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+
| psState\  | number| No       | The number of processes in a zombie state    |
| Zombie    |       |          |                                              |
+-----------+-------+----------+----------------------------------------------+

‘Notification’ Domain Datatypes
+++++++++++++++++++++++++++++++

Datatype: notificationFields
****************************

The notificationFields datatype consists of the following fields:

+--------------+-----------+----------+---------------------------------------+
| Field        | Type      | Required?| Description                           |
+==============+===========+==========+=======================================+
| additional\  | hashMap   | No       | Additional notification fields if     |
| Fields       |           |          | needed                                |
+--------------+-----------+----------+---------------------------------------+
| arrayOfNamed\| namedHash\| No       | Array of named hashMaps               |
| HashMap      | Map [ ]   |          |                                       |
+--------------+-----------+----------+---------------------------------------+
| change\      | string    | No       | Identifier for a contact related to   |
| Contact      |           |          | the change                            |
+--------------+-----------+----------+---------------------------------------+
| change\      | string    | Yes      | System or session identifier          |
| Identifier   |           |          | associated with the change            |
+--------------+-----------+----------+---------------------------------------+
| changeType   | string    | Yes      | Describes what has changed for the    |
|              |           |          | entity, for example: configuration    |
|              |           |          | changed, capability added, capability |
|              |           |          | removed…                              |
+--------------+-----------+----------+---------------------------------------+
| newState     | string    | No       | New state of the entity, for example: |
|              |           |          | ‘inService’, ‘maintenance’,           |
|              |           |          | ‘outOfService’                        |
+--------------+-----------+----------+---------------------------------------+
| notification\| string    | Yes      | Version of the notificationFields     |
| FieldsVersion|           |          | block as "#.#" where # is a digit; see|
|              |           |          | section 1 for the correct digits to   |
|              |           |          | use.                                  |
+--------------+-----------+----------+---------------------------------------+
| oldState     | string    | No       | Previous state of the entity, for     |
|              |           |          | example: ‘inService’, ‘maintenance’,  |
|              |           |          | ‘outOfService’                        |
+--------------+-----------+----------+---------------------------------------+
| state\       | string    | No       | Card or port name of the entity that  |
| Interface    |           |          | changed state                         |
+--------------+-----------+----------+---------------------------------------+

The fileReady notification event is used by 3GPP-compliant NFs to notify
ONAP that a PM file is available for upload. The notificationFields are
populated as follows:

**arrayOfNamedHashMap:** The array is named for the PM file as defined
in 3GPP TS 28.550. The array contains the following key value pairs:

-  **location** in the form protocol://ipAddress:port/path/filename;
   e.g. "location" :
   "ftpes://135.3.1.44:21/pmfiles/A20180531.1030+0600-1045+0600\A20000626.2315+0200-2330+0200_NodeBId.gz"

-  **compression** containing the compression type used for the PM file;
   e.g. "compression" : "gzip"

-  **fileFormatType** containing the format type of the PM file; e.g.
   "fileFormatType" : "org.3GPP.32.435#measCollec"

-  **fileFormatVersion** containing the format version of the PM file;
   e.g. "fileFormatVersion" : "V10"

-  other vendor-defined key-value pairs as needed

**changeIdentifier:** set to PM\_MEAS\_FILES

**changeType:** set to fileReady

Other notificationFields are not used for fileReady.

‘Other’ Domain Datatypes
++++++++++++++++++++++++

Datatype: otherFields
*********************

The otherFields datatype defines fields for events belonging to the
'other' domain of the commonEventHeader domain enumeration; it consists
of the following fields:

+-------------+-------------+----------+--------------------------------------+
| Field       | Type        | Required?| Description                          |
+=============+=============+==========+======================================+
| arrayOf\    | arrayOf\    | No       | Array of named hashMaps              |
| NamedHashMap| NamedHashMap|          |                                      |
+-------------+-------------+----------+--------------------------------------+
| hashMap     | hashMap     | No       | Array of name-value pairs            |
+-------------+-------------+----------+--------------------------------------+
| jsonObjects | arrayOf\    | No       | Array of JSON objects described by   |
|             | JsonObject  |          | name, schema and other               |
|             |             |          | meta-information                     |
+-------------+-------------+----------+--------------------------------------+
| otherFields\| string      | Yes      | Version of the otherFields block as  |
| Version     |             |          | "#.#" where # is a digit; see section|
|             |             |          | 1 for the correct digits to use.     |
+-------------+-------------+----------+--------------------------------------+

‘perf3gpp’ Domain Datatypes
+++++++++++++++++++++++++++

Datatype: measDataCollection
****************************

The measDataCollection datatype defines a 3GPP measurement collection
structure aligned with the 3GPP PM format; it consists of the following
fields:

+----------------+---------+----------+---------------------------------------+
| Field          | Type    | Required?| Description                           |
+================+=========+==========+=======================================+
| format\        | string  | No       | 3GPP PM reporting file format version |
| Version        |         |          | from pre-standard TS 28.550 v2.0.0    |
+----------------+---------+----------+---------------------------------------+
| granularity\   | string  | Yes      | Granularity period for the PM report  |
| Period         |         |          | in seconds                            |
+----------------+---------+----------+---------------------------------------+
| measInfoList   | measInfo| Yes      | Array of measInfo measurements        |
|                | [ ]     |          |                                       |
+----------------+---------+----------+---------------------------------------+
| measObjInst\   | string  | No       | Array of monitored object local       |
| IdList         | [ ]     |          | distinguished name ids per 3GPP TS    |
|                |         |          | 32.300                                |
+----------------+---------+----------+---------------------------------------+
| measured\      | string  | Yes      | Distinguished name per 3GPP TS 28.532 |
| EntityDn       |         |          |                                       |
+----------------+---------+----------+---------------------------------------+
| measuredEntity\| string  | No       | Software version for the NF providing |
| SoftwareVersion|         |          | the PM data as specified in 3GPP TS   |
|                |         |          | 28.532                                |
+----------------+---------+----------+---------------------------------------+
| measuredEntity\| string  | No       | User Definable name for the measured  |
| UserName       |         |          | object per 3GPP TS 28.532             |
+----------------+---------+----------+---------------------------------------+

Datatype: measInfo
******************

The measInfo datatype provides measurement information; it consists of
the following fields:

+-------+--------------------------+----------+-------------------------------+
| Field | Type                     | Required?| Description                   |
+=======+==========================+==========+===============================+
| jobId | string                   | No       | Name of the measurement job   |
+-------+--------------------------+----------+-------------------------------+
| meas\ | oneOf [ measInfoIdInteger| No       | Measurement group Identifier  |
| InfoId| , measInfoIdString ]     |          |                               |
+-------+--------------------------+----------+-------------------------------+
| meas\ | oneOf [ measTypesInteger | Yes      | Array of measurement          |
| Types | , measTypesString ]      |          | identifiers associated with   |
|       |                          |          | the measurement results       |
|       |                          |          | expressed as integers for     |
|       |                          |          | efficiency rather than strings|
+-------+--------------------------+----------+-------------------------------+
| meas\ | measValues [ ]           | Yes      | Array of measValues           |
| Values|                          |          |                               |
+-------+--------------------------+----------+-------------------------------+

Datatype: measInfoIdInteger
***************************

The measInfoIdInteger datatype provides an integer measurement group
identifier; it consists of the following fields:

+---------------+---------+----------+--------------------------------------+
| Field         | Type    | Required?| Description                          |
+===============+=========+==========+======================================+
| iMeasInfoId   | integer | Yes      | Integer measurement group Identifier |
+---------------+---------+----------+--------------------------------------+

Datatype: measInfoIdString
**************************

The measInfoIdString datatype provides a string measurement group
identifier; it consists of the following fields:

+---------------+-----------+----------+--------------------------------------+
| Field         | Type      | Required?| Description                          |
+===============+===========+==========+======================================+
| sMeasInfoId   | integer   | Yes      | String measurement group Identifier  |
+---------------+-----------+----------+--------------------------------------+

Datatype: measResultInteger
***************************

The measResultInteger datatype provides an integer 3GPP PM measurement
result; it consists of the following fields:

+----------+-----------+-------------+------------------------------------+
| Field    | Type      | Required?   | Description                        |
+==========+===========+=============+====================================+
| p        | integer   | Yes         | Integer reference to the counter   |
+----------+-----------+-------------+------------------------------------+
| iValue   | integer   | Yes         | Integer counter value              |
+----------+-----------+-------------+------------------------------------+

Datatype: measResultNull
************************

The measResultNull datatype provides a null 3GPP PM measurement result;
it consists of the following fields:

+----------+-----------+-------------+------------------------------------+
| Field    | Type      | Required?   | Description                        |
+==========+===========+=============+====================================+
| p        | integer   | Yes         | Integer reference to the counter   |
+----------+-----------+-------------+------------------------------------+
| isNull   | string    | Yes         | Enumeration: ‘true’ or ‘false’     |
+----------+-----------+-------------+------------------------------------+

Datatype: measResultNumber
**************************

The measResultNumber datatype provides a number 3GPP PM measurement
result; it consists of the following fields:

+----------+-----------+-------------+------------------------------------+
| Field    | Type      | Required?   | Description                        |
+==========+===========+=============+====================================+
| p        | integer   | Yes         | Integer reference to the counter   |
+----------+-----------+-------------+------------------------------------+
| rValue   | number    | Yes         | Number counter value               |
+----------+-----------+-------------+------------------------------------+

Datatype: measResultString
**************************

The measResultString datatype provides a string 3GPP PM measurement
result; it consists of the following fields:

+----------+-----------+-------------+------------------------------------+
| Field    | Type      | Required?   | Description                        |
+==========+===========+=============+====================================+
| p        | integer   | Yes         | Integer reference to the counter   |
+----------+-----------+-------------+------------------------------------+
| sValue   | string    | Yes         | String counter value               |
+----------+-----------+-------------+------------------------------------+

Datatype: measTypesInteger
**************************

The measTypesInteger datatype provides an array of integer measurement
identifiers associated with the measurement results; it consists of the
following fields:

+----------+--------+----------+----------------------------------------------+
| Field    | Type   | Required?| Description                                  |
+==========+========+==========+==============================================+
| iMeas\   | integer| Yes      | Array of integer measurement identifiers     |
| TypesList| [ ]    |          | associated with the measurement results      |
+----------+--------+----------+----------------------------------------------+

Datatype: measTypesString
*************************

The measTypesString datatype provides an array of string measurement
identifiers associated with the measurement results; it consists of the
following fields:

+----------+-------+----------+-----------------------------------------------+
| Field    | Type  | Required?| Description                                   |
+==========+=======+==========+===============================================+
| sMeas\   | string| Yes      | Array of string measurement identifiers       |
| TypesList| [ ]   |          | associated with the measurement results       |
+----------+-------+----------+-----------------------------------------------+

Datatype: measValues
********************

The measValues datatype provides 3GPP measurement values; it consists of
the following fields:

+---------+----------------------------------+----------+---------------------+
| Field   | Type                             | Required?| Description         |
+=========+==================================+==========+=====================+
| measObj\| hashMap                          | No       | Additional key-value|
| AddlFlds|                                  |          | pairs if needed     |
+---------+----------------------------------+----------+---------------------+
| measObj\| measDataCollection               | Yes      | Monitored object    |
| InstId  |                                  |          | local distinguished |
|         |                                  |          | name per 3GPP TS    |
|         |                                  |          | 32.300 and 3GPP TS  |
|         |                                  |          | 32.432              |
+---------+----------------------------------+----------+---------------------+
| meas\   | Array of items where each item is| Yes      | Array of results    |
| Results | oneOf [ measResultInteger,       |          |                     |
|         | measResultNull, measResultNumber,|          |                     |
|         | measResultString ]               |          |                     |
+---------+----------------------------------+----------+---------------------+
| suspect\| string                           | No       | Enumeration: ‘true’,|
| Flag    |                                  |          | ‘false’. Indicates  |
|         |                                  |          | if the values are   |
|         |                                  |          | suspect             |
+---------+----------------------------------+----------+---------------------+

Datatype: perf3gppFields
************************

The perf3gppFields datatype defines fields for 3GPP PM format events,
based on 3GPP TS 28.550, belonging to the 'perf3gpp' domain of the
commonEventHeader domain enumeration; it consists of the following
fields:

+--------------+-----------+----------+---------------------------------------+
| Field        | Type      | Required?| Description                           |
+==============+===========+==========+=======================================+
| eventAddl\   | hashMap   | No       | Additional key-value pairs if needed  |
| Fields       |           |          |                                       |
+--------------+-----------+----------+---------------------------------------+
| measData\    | measData  | Yes      | 3GPP measurement collection structure |
| Collection   | Collection|          |                                       |
+--------------+-----------+----------+---------------------------------------+
| perf3gpp\    | string    | Yes      | Version of the perf3gpp event         |
| FieldsVersion|           |          |                                       |
+--------------+-----------+----------+---------------------------------------+

‘pnfRegistration’ Domain Datatypes
++++++++++++++++++++++++++++++++++

Datatype: pnfRegistrationFields
*******************************

The pnfRegistrationFields datatype defines fields for events belonging
to the 'pnfRegistration' domain of the commonEventHeader domain
enumeration; it consists of the following fields:

+-----------------+--------+----------+---------------------------------------+
| Field           | Type   | Required?| Description                           |
+=================+========+==========+=======================================+
| additional\     | hashMap| No       | Additional pnfRegistration fields if  |
| Fields          |        |          | needed                                |
+-----------------+--------+----------+---------------------------------------+
| last\           | string | No       | TS 32.692 dateOfLastService = date of |
| ServiceDate     |        |          | last service; e.g. 15022017           |
+-----------------+--------+----------+---------------------------------------+
| macAddress      | string | No       | MAC address of OAM interface of the   |
|                 |        |          | unit                                  |
+-----------------+--------+----------+---------------------------------------+
| manufacture\    | string | No       | TS 32.692 dateOfManufacture =         |
| Date            |        |          | manufacture date of the unit; 24032016|
+-----------------+--------+----------+---------------------------------------+
| modelNumber     | string | No       | TS 32.692 versionNumber = version of  |
|                 |        |          | the unit from vendor; e.g. AJ02. Maps |
|                 |        |          | to AAI equip-model                    |
+-----------------+--------+----------+---------------------------------------+
| oamV4\          | string | No       | IPv4 m-plane IP address to be used by |
| IpAddress       |        |          | the manager to contact the PNF        |
+-----------------+--------+----------+---------------------------------------+
| oamV6\          | string | No       | IPv6 m-plane IP address to be used by |
| IpAddress       |        |          | the manager to contact the PNF        |
+-----------------+--------+----------+---------------------------------------+
| pnfRegistration\| string | Yes      | Version of the pnfRegistrationFields  |
| FieldsVersion   |        |          | block as "#.#" where # is a digit; see|
|                 |        |          | section 1 for the correct digits to   |
|                 |        |          | use.                                  |
+-----------------+--------+----------+---------------------------------------+
| serialNumber    | string | No       | TS 32.692 serialNumber = serial number|
|                 |        |          | of the unit; e.g. 6061ZW3             |
+-----------------+--------+----------+---------------------------------------+
| software\       | string | No       | TS 32.692 swName = active SW running  |
| Version         |        |          | on the unit; e.g. 5gDUv18.05.201      |
+-----------------+--------+----------+---------------------------------------+
| unitFamily      | string | No       | TS 32.692 vendorUnitFamilyType =      |
|                 |        |          | general type of HW unit; e.g. BBU     |
+-----------------+--------+----------+---------------------------------------+
| unitType        | string | No       | TS 32.692 vendorUnitTypeNumber =      |
|                 |        |          | vendor name for the unit; e.g.        |
|                 |        |          | Airscale                              |
+-----------------+--------+----------+---------------------------------------+
| vendorName      | string | No       | TS 32.692 vendorName = name of        |
|                 |        |          | manufacturer; e.g. Nokia. Maps to AAI |
|                 |        |          | equip-vendor                          |
+-----------------+--------+----------+---------------------------------------+

‘State Change’ Domain Datatypes
+++++++++++++++++++++++++++++++

Datatype: stateChangeFields
***************************

The stateChangeFields datatype consists of the following fields:

+--------------+--------+----------+------------------------------------------+
| Field        | Type   | Required?| Description                              |
+==============+========+==========+==========================================+
| additional\  | hashMap| No       | Additional stateChange fields if needed  |
| Fields       |        |          |                                          |
+--------------+--------+----------+------------------------------------------+
| newState     | string | Yes      | New state of the entity: ‘inService’,    |
|              |        |          | ‘maintenance’, ‘outOfService’            |
+--------------+--------+----------+------------------------------------------+
| oldState     | string | Yes      | Previous state of the entity: ‘inService’|
|              |        |          | , ‘maintenance’, ‘outOfService’          |
+--------------+--------+----------+------------------------------------------+
| stateChange\ | string | Yes      | Version of the stateChangeFields block as|
| FieldsVersion|        |          | "#.#" where # is a digit; see section 1  |
|              |        |          | for the correct digits to use.           |
+--------------+--------+----------+------------------------------------------+
| state\       | string | Yes      | Card or port name of the entity that     |
| Interface    |        |          | changed state                            |
+--------------+--------+----------+------------------------------------------+

‘StndDefined’ Domain Datatypes
++++++++++++++++++++++++++++++

Datatype: stndDefinedFields
***************************

The stndDefinedFields datatype consists of the following fields:

+--------------+--------+----------+------------------------------------------+
| Field        | Type   | Required?| Description                              |
+==============+========+==========+==========================================+
| data         | object | Yes      | Expected to contain a notification       |
|              |        |          | defined by relevant standards group/body |
|              |        |          | Must be a JSON object.                   |
+--------------+--------+----------+------------------------------------------+
| schema\      | string | No       | A reference to standards defined schema, |
| Reference    |        |          | against which the contents of data       |
|              |        |          | property will be validated               |
+--------------+--------+----------+------------------------------------------+
| stndDefined\ | string | Yes      | Version of the stndDefinedFields block as|
| FieldsVersion|        |          | "#.#" where # is a digit; see section 1  |
|              |        |          | for the correct digits to use.           |
+--------------+--------+----------+------------------------------------------+

Additional rules, when using stndDefined domain
***********************************************

Following rules shall be followed, when using the StndDefined domain:

If the VNF or PNF is using VES StndDefined domain, then the VNF or PNF MUST
fill the VES.commonEventHeader.stndDefinedNamespace with a value defined by
relevant standards organization.

If the VNF or PNF is using VES StndDefined domain, then the VNF or PNF MAY
fill the VES.stndDefinedFields.schemaReference property with a URI
corresponding to the specific JSON schema object, against which validation
of VES.stndDefinedFields.data will be executed.

If the VNF or PNF is using VES StndDefined domain and eventBatch is sent,
then each and every event within eventBatch must have exactly the same
VES.commonEventHeader.stndDefinedNamespace set.

‘Syslog’ Domain Datatypes
+++++++++++++++++++++++++

Datatype: syslogFields
**********************

The syslogFields datatype consists of the following fields:

+------------+--------+----------+--------------------------------------------+
| Field      | Type   | Required?| Description                                |
+============+========+==========+============================================+
| additional\| hashMap| No       | Additional syslog fields if needed Ex:     |
| Fields     |        |          | {"name1": "value1", "name2: "value2" … }   |
+------------+--------+----------+--------------------------------------------+
| event\     | string | No       | Hostname of the device                     |
| SourceHost |        |          |                                            |
+------------+--------+----------+--------------------------------------------+
| event\     | string | Yes      | Examples: ‘other’, ‘router’, ‘switch’,     |
| SourceType |        |          | ‘host’, ‘card’, ‘port’, ‘slotThreshold’,   |
|            |        |          | ‘portThreshold’, ‘virtualMachine’,         |
|            |        |          | ‘virtualNetworkFunction’                   |
+------------+--------+----------+--------------------------------------------+
| syslog\    | integer| No       | Numeric code from 0 to 23 for facility:    |
| Facility   |        |          |                                            |
|            |        |          |                                            |
|            |        |          | 0 kernel messages                          |
|            |        |          |                                            |
|            |        |          | 1 user-level messages                      |
|            |        |          |                                            |
|            |        |          | 2 mail system                              |
|            |        |          |                                            |
|            |        |          | 3 system daemons                           |
|            |        |          |                                            |
|            |        |          | 4 security/authorization messages          |
|            |        |          |                                            |
|            |        |          | 5 messages generated internally by syslogd |
|            |        |          |                                            |
|            |        |          | 6 line printer subsystem                   |
|            |        |          |                                            |
|            |        |          | 7 network news subsystem                   |
|            |        |          |                                            |
|            |        |          | 8 UUCP subsystem                           |
|            |        |          |                                            |
|            |        |          | 9 clock daemon                             |
|            |        |          |                                            |
|            |        |          | 10 security/authorization messages         |
|            |        |          |                                            |
|            |        |          | 11 FTP daemon                              |
|            |        |          |                                            |
|            |        |          | 12 NTP subsystem                           |
|            |        |          |                                            |
|            |        |          | 13 log audit                               |
|            |        |          |                                            |
|            |        |          | 14 log alert                               |
|            |        |          |                                            |
|            |        |          | 15 clock daemon (note 2)                   |
|            |        |          |                                            |
|            |        |          | 16 local use 0 (local0)                    |
|            |        |          |                                            |
|            |        |          | 17 local use 1 (local1)                    |
|            |        |          |                                            |
|            |        |          | 18 local use 2 (local2)                    |
|            |        |          |                                            |
|            |        |          | 19 local use 3 (local3)                    |
|            |        |          |                                            |
|            |        |          | 20 local use 4 (local4)                    |
|            |        |          |                                            |
|            |        |          | 21 local use 5 (local5)                    |
|            |        |          |                                            |
|            |        |          | 22 local use 6 (local6)                    |
|            |        |          |                                            |
|            |        |          | 23 local use 7 (local7 )                   |
+------------+--------+----------+--------------------------------------------+
| syslog\    | string | Yes      | Version of the syslogFields block as "#.#" |
| Fields\    |        |          | where # is a digit; see section 1 for the  |
| Version    |        |          | correct digits to use.                     |
+------------+--------+----------+--------------------------------------------+
| syslogMsg  | string | Yes      | Syslog message                             |
+------------+--------+----------+--------------------------------------------+
| syslog\    | string | No       | Hostname parsed from non-VES syslog message|
| MsgHost    |        |          |                                            |
+------------+--------+----------+--------------------------------------------+
| syslogPri  | integer| No       | 0-192                                      |
|            |        |          |                                            |
|            |        |          | Combined Severity and Facility(see rfc5424)|
+------------+--------+----------+--------------------------------------------+
| syslogProc | string | No       | Identifies the application that originated |
|            |        |          | the message                                |
+------------+--------+----------+--------------------------------------------+
| syslog\    | number | No       | The process number assigned by the OS when |
| ProcId     |        |          | the application was started                |
+------------+--------+----------+--------------------------------------------+
| syslog\    | string | No       | A <space> separated list of key="value"    |
| SData      |        |          | pairs following the rfc5424 standard for   |
|            |        |          | SD-ELEMENT.                                |
|            |        |          |                                            |
|            |        |          | ***Deprecated ***                          |
|            |        |          |                                            |
|            |        |          | The entire rfc5424 syslogSData object,     |
|            |        |          | including square brackets [ ], SD-ID and   |
|            |        |          | list of SD-PARAMs                          |
+------------+--------+----------+--------------------------------------------+
| syslogSdId | string | No       | 0-32 char in format name@number,           |
|            |        |          |                                            |
|            |        |          | i.e., ourSDID@32473                        |
+------------+--------+----------+--------------------------------------------+
| syslogSev  | string | No       | Level-of-severity text enumeration defined |
|            |        |          | below:                                     |
|            |        |          |                                            |
|            |        |          | *Text* *Sev* *Description*                 |
|            |        |          |                                            |
|            |        |          | Emergency 0 system is unusable             |
|            |        |          |                                            |
|            |        |          | Alert 1 action must be taken immediately   |
|            |        |          |                                            |
|            |        |          | Critical 2 critical conditions             |
|            |        |          |                                            |
|            |        |          | Error 3 error conditions                   |
|            |        |          |                                            |
|            |        |          | Warning 4 warning conditions               |
|            |        |          |                                            |
|            |        |          | Notice 5 normal but significant condition  |
|            |        |          |                                            |
|            |        |          | Info 6 Informational messages              |
|            |        |          |                                            |
|            |        |          | Debug 7 debug-level messages               |
+------------+--------+----------+--------------------------------------------+
| syslogTag  | string | Yes      | Also known as MsgId. Brief non-spaced text |
|            |        |          | indicating the type of message such as     |
|            |        |          | ‘TCPOUT’ or ‘BGP\_STATUS\_CHANGE’;         |
|            |        |          | ‘NILVALUE’ should be used when no other    |
|            |        |          | value can be provided                      |
+------------+--------+----------+--------------------------------------------+
| syslogTs   | string | No       | Timestamp parsed from non-VES syslog       |
|            |        |          | message                                    |
+------------+--------+----------+--------------------------------------------+
| syslogVer  | number | No       | IANA assigned version of the syslog        |
|            |        |          | protocol specification:                    |
|            |        |          |                                            |
|            |        |          | 0: VES                                     |
|            |        |          |                                            |
|            |        |          | 1: IANA RFC5424                            |
+------------+--------+----------+--------------------------------------------+

Examples of syslogSData :

Preferred

    ts="1985-04-12T23:20:50.52Z" tag="BGP\_NEIGHBOR\_DOWN" msg="The BGP
    session to neighbor 10.10.10.10 is down"

Deprecated

    [attinc@1234 ts="1985-04-12T23:20:50.52Z" tag="BGP\_NEIGHBOR\_DOWN"
    msg="The BGP session to neighbor 10.10.10.10 is down"]

Syslog references:

https://tools.ietf.org/html/rfc5424#section-6

    https://www.iana.org/assignments/syslog-parameters/syslog-parameters.xhtml

‘Threshold Crossing Alert’ Domain Datatypes
+++++++++++++++++++++++++++++++++++++++++++

Datatype: counter
*****************

The counter datatype consists of the following fields:

+------------+--------+----------+--------------------------------------------+
| Field      | Type   | Required?| Description                                |
+============+========+==========+============================================+
| criticality| string | Yes      | Enumeration: ‘CRIT’, ‘MAJ’                 |
+------------+--------+----------+--------------------------------------------+
| hashMap    | hashMap| Yes      | Key is the name of the counter and value is|
|            |        |          | the current value of the counter           |
+------------+--------+----------+--------------------------------------------+
| threshhold\| string | Yes      | Last threshold that was crossed            |
| Crossed    |        |          |                                            |
+------------+--------+----------+--------------------------------------------+

Datatype: thresholdCrossingAlertFields
**************************************

The thresholdCrossingAlertFields datatype consists of the following
fields:

+------------+------------+----------+----------------------------------------+
| Field      | Type       | Required?| Description                            |
+============+============+==========+========================================+
| additional\| hashMap    | No       | Additional threshold crossing alert    |
| Fields     |            |          | fields if needed                       |
+------------+------------+----------+----------------------------------------+
| additional\| counter [ ]| Yes      | Array of performance counters          |
| Parameters |            |          |                                        |
+------------+------------+----------+----------------------------------------+
| alert\     | string     | Yes      | Enumeration: ‘SET’, ‘CONT’, ‘CLEAR’    |
| Action     |            |          |                                        |
+------------+------------+----------+----------------------------------------+
| alert\     | string     | Yes      | Unique short alert description (e.g.,  |
| Description|            |          | NE-CPUMEM)                             |
+------------+------------+----------+----------------------------------------+
| alertType  | string     | Yes      | Enumeration: ‘CARD-ANOMALY’,           |
|            |            |          | ‘INTERFACE-ANOMALY’, ELEMENT-ANOMALY’, |
|            |            |          | ‘SERVICE-ANOMALY’                      |
+------------+------------+----------+----------------------------------------+
| alertValue | string     | No       | Calculated API value (if applicable)   |
+------------+------------+----------+----------------------------------------+
| associated\| string [ ] | No       | List of eventIds associated with the   |
| AlertIdList|            |          | event being reported                   |
+------------+------------+----------+----------------------------------------+
| collection\| string     | Yes      | Time when the performance collector    |
| Timestamp  |            |          | picked up the data; with RFC 2822      |
|            |            |          | compliant format: ‘Sat, 13 Mar 2010    |
|            |            |          | 11:29:05 -0800’                        |
+------------+------------+----------+----------------------------------------+
| data\      | string     | No       | Specific performance collector instance|
| Collector  |            |          | used                                   |
+------------+------------+----------+----------------------------------------+
| elementType| string     | No       | Type of network element (internal AT&T |
|            |            |          | field)                                 |
+------------+------------+----------+----------------------------------------+
| event\     | string     | Yes      | Event severity or priority enumeration:|
| Severity   |            |          | ‘CRITICAL’, ‘MAJOR’, ‘MINOR’, ‘WARNING’|
|            |            |          | , ‘NORMAL’                             |
+------------+------------+----------+----------------------------------------+
| eventStart\| string     | Yes      | Time closest to when the measurement   |
| Timestamp  |            |          | was made; with RFC 2822 compliant      |
|            |            |          | format: ‘Sat, 13 Mar 2010 11:29:05     |
|            |            |          | -0800’                                 |
+------------+------------+----------+----------------------------------------+
| interface\ | string     | No       | Physical or logical port or card (if   |
| Name       |            |          | applicable)                            |
+------------+------------+----------+----------------------------------------+
| network\   | string     | No       | Network name (internal AT&T field)     |
| Service    |            |          |                                        |
+------------+------------+----------+----------------------------------------+
| possible\  | string     | No       | Reserved for future use                |
| RootCause  |            |          |                                        |
+------------+------------+----------+----------------------------------------+
| threshold\ | string     | Yes      | Version of the                         |
| Crossing   |            |          | thresholdCrossingAlertFields block as  |
| Fields\    |            |          | "#.#" where # is a digit; see section 1|
| Version    |            |          | for the correct digits to use.         |
+------------+------------+----------+----------------------------------------+

Technology Specific Datatypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mobile Flow’ Domain Datatypes
+++++++++++++++++++++++++++++

Datatype: gtpPerFlowMetrics
***************************

The gtpPerFlowMetrics datatype consists of the following fields:

+---------------+--------+----------+-----------------------------------------+
| Field         | Type   | Required?| Description                             |
+===============+========+==========+=========================================+
| avgBit\       | number | Yes      | Average bit error rate                  |
| ErrorRate     |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| avgPacket\    | number | Yes      | Average packet delay variation or jitter|
| Delay\        |        |          | in milliseconds for received packets:   |
| Variation     |        |          | Average difference between the packet   |
|               |        |          | timestamp and time received for all     |
|               |        |          | pairs of consecutive packets            |
+---------------+--------+----------+-----------------------------------------+
| avgPacket\    | number | Yes      | Average delivery latency                |
| Latency       |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| avgReceive\   | number | Yes      | Average receive throughput              |
| Throughput    |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| avgTransmit\  | number | Yes      | Average transmit throughput             |
| Throughput    |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| dur\          | number | No       | Duration of failed state in milliseconds|
| Connection\   |        |          | , computed as the cumulative time       |
| FailedStatus  |        |          | between a failed echo request and the   |
|               |        |          | next following successful error request,|
|               |        |          | over this reporting interval            |
+---------------+--------+----------+-----------------------------------------+
| durTunnel\    | number | No       | Duration of errored state, computed as  |
| FailedStatus  |        |          | the cumulative time between a tunnel    |
|               |        |          | error indicator and the next following  |
|               |        |          | non-errored indicator, over this        |
|               |        |          | reporting interval                      |
+---------------+--------+----------+-----------------------------------------+
| flow\         | string | No       | Endpoint activating the flow            |
| ActivatedBy   |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| flow\         | number | Yes      | Time the connection is activated in the |
| Activation\   |        |          | flow (connection) being reported on, or |
| Epoch         |        |          | transmission time of the first packet if|
|               |        |          | activation time is not available        |
+---------------+--------+----------+-----------------------------------------+
| flow\         | number | Yes      | Integer microseconds for the start of   |
| Activation\   |        |          | the flow connection                     |
| Microsec      |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| flow\         | string | No       | Time the connection is activated in the |
| Activation\   |        |          | flow being reported on, or transmission |
| Time          |        |          | time of the first packet if activation  |
|               |        |          | time is not available; with RFC 2822    |
|               |        |          | compliant format: ‘Sat, 13 Mar 2010     |
|               |        |          | 11:29:05 -0800’                         |
+---------------+--------+----------+-----------------------------------------+
| flow\         | string | No       | Endpoint deactivating the flow          |
| Deactivated\  |        |          |                                         |
| By            |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| flow\         | number | Yes      | Time for the start of the flow          |
| Deactivation\ |        |          | connection, in integer UTC epoch time   |
| Epoch         |        |          | aka UNIX time                           |
+---------------+--------+----------+-----------------------------------------+
| flow\         | number | Yes      | Integer microseconds for the start of   |
| Deactivation\ |        |          | the flow connection                     |
| Microsec      |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| flow\         | string | Yes      | Transmission time of the first packet in|
| Deactivation\ |        |          | the flow connection being reported on;  |
| Time          |        |          | with RFC 2822 compliant format: ‘Sat, 13|
|               |        |          | Mar 2010 11:29:05 -0800’                |
+---------------+--------+----------+-----------------------------------------+
| flowStatus    | string | Yes      | Connection status at reporting time as a|
|               |        |          | working / inactive / failed indicator   |
|               |        |          | value                                   |
+---------------+--------+----------+-----------------------------------------+
| gtp\          | string | No       | Current connection state at reporting   |
| Connection\   |        |          | time                                    |
| Status        |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| gtpTunnel\    | string | No       | Current tunnel state at reporting time  |
| Status        |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| ipTos\        | hashMap| No       | Array of key: value pairs where the keys|
| CountList     |        |          | are drawn from the IP Type-of-Service   |
|               |        |          | identifiers which range from '0' to     |
|               |        |          | '255', and the values are the count of  |
|               |        |          | packets that had those ToS identifiers  |
|               |        |          | in the flow                             |
+---------------+--------+----------+-----------------------------------------+
| ipTosList     | string | No       | Array of unique IP Type-of-Service      |
|               |        |          | values observed in the flow where values|
|               |        |          | range from '0' to '255'                 |
+---------------+--------+----------+-----------------------------------------+
| large\        | number | No       | large packet round trip time            |
| PacketRtt     |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| largePacket\  | number | No       | large packet threshold being applied    |
| Threshold     |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| maxPacket\    | number | Yes      | Maximum packet delay variation or jitter|
| Delay\        |        |          | in milliseconds for received packets:   |
| Variation     |        |          | Maximum of the difference between the   |
|               |        |          | packet timestamp and time received for  |
|               |        |          | all pairs of consecutive packets        |
+---------------+--------+----------+-----------------------------------------+
| maxReceive\   | number | No       | maximum receive bit rate"               |
| BitRate       |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| maxTransmit\  | number | No       | maximum transmit bit rate               |
| BitRate       |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| mobileQci\    | hashMap| No       | array of key: value pairs where the keys|
| CosCountList  |        |          | are drawn from LTE QCI or UMTS class of |
|               |        |          | service strings, and the values are the |
|               |        |          | count of packets that had those strings |
|               |        |          | in the flow                             |
+---------------+--------+----------+-----------------------------------------+
| mobileQci\    | string | No       | Array of unique LTE QCI or UMTS         |
| CosList       |        |          | class-of-service values observed in the |
|               |        |          | flow                                    |
+---------------+--------+----------+-----------------------------------------+
| num\          | number | Yes      | Number of failed activation requests, as|
| Activation\   |        |          | observed by the reporting node          |
| Failures      |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| numBit\       | number | Yes      | number of errored bits                  |
| Errors        |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| numBytes\     | number | Yes      | number of bytes received, including     |
| Received      |        |          | retransmissions                         |
+---------------+--------+----------+-----------------------------------------+
| numBytes\     | number | Yes      | number of bytes transmitted, including  |
| Transmitted   |        |          | retransmissions                         |
+---------------+--------+----------+-----------------------------------------+
| numDropped\   | number | Yes      | number of received packets dropped due  |
| Packets       |        |          | to errors per virtual interface         |
+---------------+--------+----------+-----------------------------------------+
| numGtp\       | number | No       | Number of Echo request path failures    |
| EchoFailures  |        |          | where failed paths are defined in 3GPP  |
|               |        |          | TS 29.281 sec 7.2.1 and 3GPP TS 29.060  |
|               |        |          | sec. 11.2                               |
+---------------+--------+----------+-----------------------------------------+
| numGtp\       | number | No       | Number of tunnel error indications where|
| TunnelErrors  |        |          | errors are defined in 3GPP TS 29.281 sec|
|               |        |          | 7.3.1 and 3GPP TS 29.060 sec. 11.1      |
+---------------+--------+----------+-----------------------------------------+
| numHttp\      | number | No       | Http error count                        |
| Errors        |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| numL7Bytes\   | number | Yes      | number of tunneled layer 7 bytes        |
| Received      |        |          | received, including retransmissions     |
+---------------+--------+----------+-----------------------------------------+
| numL7Bytes\   | number | Yes      | number of tunneled layer 7 bytes        |
| Transmitted   |        |          | transmitted, excluding retransmissions  |
+---------------+--------+----------+-----------------------------------------+
| numLost\      | number | Yes      | number of lost packets                  |
| Packets       |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| numOutOf\     | number | Yes      | number of out-of-order packets          |
| OrderPackets  |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| numPacket\    | number | Yes      | number of errored packets               |
| Errors        |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| numPackets\   | number | Yes      | number of packets received, excluding   |
| ReceivedExcl\ |        |          | retransmission                          |
| Retrans       |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| numPackets\   | number | Yes      | number of packets received, including   |
| ReceivedIncl\ |        |          | retransmission                          |
| Retrans       |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| numPackets\   | number | Yes      | number of packets transmitted, including|
| Transmitted\  |        |          | retransmissions                         |
| InclRetrans   |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| numRetries    | number | Yes      | number of packet retrie                 |
+---------------+--------+----------+-----------------------------------------+
| numTimeouts   | number | Yes      | number of packet timeouts               |
+---------------+--------+----------+-----------------------------------------+
| numTunneled\  | number | Yes      | number of tunneled layer 7 bytes        |
| L7Bytes\      |        |          | received, excluding retransmissions     |
| Received      |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| roundTrip\    | number | Yes      | Round Trip time                         |
| Time          |        |          |                                         |
+---------------+--------+----------+-----------------------------------------+
| tcpFlag\      | hashMap| No       | Array of key: value pairs where the keys|
| CountList     |        |          | are drawn from TCP Flags and the values |
|               |        |          | are the count of packets that had that  |
|               |        |          | TCP Flag in the flow                    |
+---------------+--------+----------+-----------------------------------------+
| tcpFlag\      | string | No       | Array of unique TCP Flags observed in   |
| List          |        |          | the flow                                |
+---------------+--------+----------+-----------------------------------------+
| timeTo\       | number | Yes      | Time in milliseconds between the        |
| FirstByte     |        |          | connection activation and first byte    |
|               |        |          | received                                |
+---------------+--------+----------+-----------------------------------------+

Datatype: mobileFlowFields
**************************

The mobileFlowFields datatype consists of the following fields:

+-------------+------------+----------+---------------------------------------+
| Field       | Type       | Required?| Description                           |
+=============+============+==========+=======================================+
| additional\ | hashMap    | No       | Additional mobileFlow fields if needed|
| Fields      |            |          |                                       |
+-------------+------------+----------+---------------------------------------+
| application\| string     | No       | Application type inferred             |
| Type        |            |          |                                       |
+-------------+------------+----------+---------------------------------------+
| appProtocol\| string     | No       | Application protocol                  |
| Type        |            |          |                                       |
+-------------+------------+----------+---------------------------------------+
| appProtocol\| string     | No       | Application version                   |
| Version     |            |          |                                       |
+-------------+------------+----------+---------------------------------------+
| cid         | string     | No       | Cell Id                               |
+-------------+------------+----------+---------------------------------------+
| connection\ | string     | No       | Abbreviation referencing a 3GPP       |
| Type        |            |          | reference point e.g., S1-U, S11, etc  |
+-------------+------------+----------+---------------------------------------+
| ecgi        | string     | No       | Evolved Cell Global Id                |
+-------------+------------+----------+---------------------------------------+
| flow\       | string     | Yes      | Flow direction, indicating if the     |
| Direction   |            |          | reporting node is the source of the   |
|             |            |          | flow or destination for the flow      |
+-------------+------------+----------+---------------------------------------+
| gtpPer\     | gtpPer     | Yes      | Mobility GTP Protocol per flow metrics|
| FlowMetrics | FlowMetrics|          |                                       |
+-------------+------------+----------+---------------------------------------+
| gtpProtocol\| string     | No       | GTP protocol                          |
| Type        |            |          |                                       |
+-------------+------------+----------+---------------------------------------+
| gtpVersion  | string     | No       | GTP protocol version                  |
+-------------+------------+----------+---------------------------------------+
| httpHeader  | string     | No       | HTTP request header, if the flow      |
|             |            |          | connects to a node referenced by HTTP |
+-------------+------------+----------+---------------------------------------+
| imei        | string     | No       | IMEI for the subscriber UE used in    |
|             |            |          | this flow, if the flow connects to a  |
|             |            |          | mobile device                         |
+-------------+------------+----------+---------------------------------------+
| imsi        | string     | No       | IMSI for the subscriber UE used in    |
|             |            |          | this flow, if the flow connects to a  |
|             |            |          | mobile device                         |
+-------------+------------+----------+---------------------------------------+
| ipProtocol\ | string     | Yes      | IP protocol type e.g.,TCP, UDP, RTP...|
| Type        |            |          |                                       |
+-------------+------------+----------+---------------------------------------+
| ipVersion   | string     | Yes      | IP protocol version e.g., IPv4, IPv6  |
+-------------+------------+----------+---------------------------------------+
| lac         | string     | No       | Location area code                    |
+-------------+------------+----------+---------------------------------------+
| mcc         | string     | No       | Mobile country code                   |
+-------------+------------+----------+---------------------------------------+
| mnc         | string     | No       | Mobile network code                   |
+-------------+------------+----------+---------------------------------------+
| mobileFlow\ | string     | Yes      | Version of the mobileFlowFields block |
| Fields\     |            |          | as "#.#" where # is a digit; see      |
| Version     |            |          | section 1 for the correct digits to   |
|             |            |          | use.                                  |
+-------------+------------+----------+---------------------------------------+
| msisdn      | string     | No       | MSISDN for the subscriber UE used in  |
|             |            |          | this flow, as an integer, if the flow |
|             |            |          | connects to a mobile device           |
+-------------+------------+----------+---------------------------------------+
| other\      | string     | Yes      | IP address for the other endpoint, as |
| EndpointIp\ |            |          | used for the flow being reported on   |
| Address     |            |          |                                       |
+-------------+------------+----------+---------------------------------------+
| other\      | integer    | Yes      | IP Port for the reporting entity, as  |
| Endpoint\   |            |          | used for the flow being reported on   |
| Port        |            |          |                                       |
+-------------+------------+----------+---------------------------------------+
| other\      | string     | No       | Functional role of the other endpoint |
| Functional\ |            |          | for the flow being reported on e.g.,  |
| Role        |            |          | MME, S-GW, P-GW, PCRF...              |
+-------------+------------+----------+---------------------------------------+
| rac         | string     | No       | Routing area code                     |
+-------------+------------+----------+---------------------------------------+
| radioAccess\| string     | No       | Radio Access Technology e.g., 2G, 3G, |
| Technology  |            |          | LTE                                   |
+-------------+------------+----------+---------------------------------------+
| reporting\  | string     | Yes      | IP address for the reporting entity,  |
| EndpointIp\ |            |          | as used for the flow being reported on|
| Addr        |            |          |                                       |
+-------------+------------+----------+---------------------------------------+
| reporting\  | integer    | Yes      | IP port for the reporting entity, as  |
| EndpointPort|            |          | used for the flow being reported on   |
+-------------+------------+----------+---------------------------------------+
| sac         | string     | No       | Service area code                     |
+-------------+------------+----------+---------------------------------------+
| sampling\   | integer    | No       | Integer identifier for the sampling   |
| Algorithm   |            |          | algorithm or rule being applied in    |
|             |            |          | calculating the flow metrics if       |
|             |            |          | metrics are calculated based on a     |
|             |            |          | sample of packets, or 0 if no sampling|
|             |            |          | is applied                            |
+-------------+------------+----------+---------------------------------------+
| tac         | string     | No       | Transport area code                   |
+-------------+------------+----------+---------------------------------------+
| tunnelId    | string     | No       | Tunnel identifier                     |
+-------------+------------+----------+---------------------------------------+
| vlanId      | string     | No       | VLAN identifier used by this flow     |
+-------------+------------+----------+---------------------------------------+

‘SipSignaling’ Domain Datatypes
+++++++++++++++++++++++++++++++

Datatype: sipSignalingFields
****************************

The sipSignalingFields datatype communicates information about sip
signaling messages, parameters and signaling state; it consists of the
following fields:

+--------------+-----------+----------+---------------------------------------+
| Field        | Type      | Required?| Description                           |
+==============+===========+==========+=======================================+
| additional\  | hashMap   | No       | Additional sipSignaling fields        |
| Information  |           |          |                                       |
+--------------+-----------+----------+---------------------------------------+
| compressed\  | string    | No       | The full SIP request/response         |
| Sip          |           |          | including headers and bodies          |
+--------------+-----------+----------+---------------------------------------+
| correlator   | string    | Yes      | Constant across all events on this    |
|              |           |          | call                                  |
+--------------+-----------+----------+---------------------------------------+
| local\       | string    | Yes      | Ip address on xNF                     |
| IpAddress    |           |          |                                       |
+--------------+-----------+----------+---------------------------------------+
| localPort    | string    | Yes      | Port on xNF                           |
+--------------+-----------+----------+---------------------------------------+
| remote\      | string    | Yes      | IP address of peer endpoint           |
| IpAddress    |           |          |                                       |
+--------------+-----------+----------+---------------------------------------+
| remotePort   | string    | Yes      | Port of peer endpoint                 |
+--------------+-----------+----------+---------------------------------------+
| sipSignaling\| string    | Yes      | Version of the sipSignalingFields     |
| FieldsVersion|           |          | block as "#.#" where # is a digit; see|
|              |           |          | section 1 for the correct digits to   |
|              |           |          | use.                                  |
+--------------+-----------+----------+---------------------------------------+
| summarySip   | string    | No       | The SIP Method or Response (‘INVITE’, |
|              |           |          | ‘200 OK’, ‘BYE’, etc)                 |
+--------------+-----------+----------+---------------------------------------+
| vendorNf\    | vendorNf  | Yes      | Vendor, NF and nfModule names         |
| NameFields   | NameFields|          |                                       |
+--------------+-----------+----------+---------------------------------------+

‘Voice Quality’ Domain Datatypes
++++++++++++++++++++++++++++++++

Datatype: endOfCallVqmSummaries
*******************************

The endOfCallVqmSummaries datatype provides end of call voice quality
metrics; it consists of the following fields:

+--------------+-------+----------+-------------------------------------------+
| Field        | Type  | Required?| Description                               |
+==============+=======+==========+===========================================+
| adjacency\   | string| Yes      | Adjacency name                            |
| Name         |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| endpoint\    | number| No       | Endpoint average jitter                   |
| AverageJitter|       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| endpoint\    | string| Yes      | Enumeration: ‘Caller’, ‘Callee’           |
| Description  |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| endpoint\    | number| No       | Endpoint maximum jitter                   |
| MaxJitter    |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| endpointRtp\ | number| No       | Endpoint RTP octets discarded             |
| Octets\      |       |          |                                           |
| Discarded    |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| endpointRtp\ | number| No       | Endpoint RTP octets lost                  |
| OctetsLost   |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| endpointRtp\ | number| No       | Endpoint RTP octets received              |
| Octets\      |       |          |                                           |
| Received     |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| endpointRtp\ | number| No       | Endpoint RTP octets sent                  |
| OctetsSent   |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| endpointRtp\ | number| No       | Endpoint RTP packets discarded            |
| Packets\     |       |          |                                           |
| Discarded    |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| endpointRtp\ | number| No       | Endpoint RTP packets lost                 |
| PacketsLost  |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| endpointRtp\ | number| No       | Endpoint RTP packets received             |
| Packets\     |       |          |                                           |
| Received     |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| endpointRtp\ | number| No       | Endpoint RTP packets sent                 |
| PacketsSent  |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| local\       | number| No       | Local average jitter                      |
| Average\     |       |          |                                           |
| Jitter       |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| localAverage\| number| No       | Local average jitter buffer delay         |
| JitterBuffer\|       |          |                                           |
| Delay        |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| localMax\    | number| No       | Local maximum jitter                      |
| Jitter       |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| localMax\    | number| No       | Local max jitter buffer delay             |
| JitterBuffer\|       |          |                                           |
| Delay        |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| localRtp\    | number| No       | Local RTP octets discarded                |
| Octets\      |       |          |                                           |
| Discarded    |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| localRtp\    | number| No       | Local RTP octets lost                     |
| OctetsLost   |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| localRtp\    | number| No       | Local RTP octets received                 |
| Octets\      |       |          |                                           |
| Received     |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| localRtp\    | number| No       | Local RTP octets sent                     |
| OctetsSent   |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| localRtp\    | number| No       | Local RTP packets discarded               |
| Packets\     |       |          |                                           |
| Discarded    |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| localRtp\    | number| No       | Local RTP packets lost                    |
| PacketsLost  |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| localRtp\    | number| No       | Local RTP packets received                |
| Packets\     |       |          |                                           |
| Received     |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| localRtp\    | number| No       | Local RTP packets sent                    |
| PacketsSent  |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+
| mosCqe       | number| No       | Decimal range from 1 to 5(1 decimal place)|
+--------------+-------+----------+-------------------------------------------+
| oneWayDelay  | number| No       | one-way path delay in milliseconds        |
+--------------+-------+----------+-------------------------------------------+
| packet\      | number| No       | Calculated percentage packet loss based on|
| LossPercent  |       |          | endpoint RTP packets lost (as reported in |
|              |       |          | RTCP) and local RTP packets sent.         |
|              |       |          | Direction is based on endpoint description|
|              |       |          | (Caller, Callee). Decimal (2 decimal      |
|              |       |          | places)                                   |
+--------------+-------+----------+-------------------------------------------+
| rFactor      | number| No       | rFactor from 0 to 100                     |
+--------------+-------+----------+-------------------------------------------+
| round\       | number| No       | Round trip delay in milliseconds          |
| TripDelay    |       |          |                                           |
+--------------+-------+----------+-------------------------------------------+

Datatype: voiceQualityFields
****************************

The voiceQualityFields datatype provides statistics related to customer
facing voice products; consists of the following fields:

+--------------+-------------+----------+-------------------------------------+
| Field        | Type        | Required?| Description                         |
+==============+=============+==========+=====================================+
| additional\  | hashMap     | No       | Additional voice quality fields     |
| Information  |             |          |                                     |
+--------------+-------------+----------+-------------------------------------+
| callee\      | string      | Yes      | Callee codec for the call           |
| SideCodec    |             |          |                                     |
+--------------+-------------+----------+-------------------------------------+
| caller\      | string      | Yes      | Caller codec for the call           |
| SideCodec    |             |          |                                     |
+--------------+-------------+----------+-------------------------------------+
| correlator   | string      | Yes      | Constant across all events on this  |
|              |             |          | call                                |
+--------------+-------------+----------+-------------------------------------+
| endOfCall\   | endOfCallVqm| No       | End of call voice quality metric    |
| VqmSummaries | Summaries   |          | summaries                           |
+--------------+-------------+----------+-------------------------------------+
| phoneNumber  | string      | No       | Phone number associated with the    |
|              |             |          | correlator                          |
+--------------+-------------+----------+-------------------------------------+
| midCallRtcp  | string      | Yes      | Base64 encoding of the binary RTCP  |
|              |             |          | data (excluding Eth/IP/UDP headers) |
+--------------+-------------+----------+-------------------------------------+
| vendorNf\    | vendorNf    | Yes      | Vendor, NF and nfModule names       |
| NameFields   | NameFields  |          |                                     |
+--------------+-------------+----------+-------------------------------------+
| voiceQuality\| string      | Yes      | Version of the voiceQualityFields   |
| FieldsVersion|             |          | block as "#.#" where # is a digit;  |
|              |             |          | see section 1 for the correct digits|
|              |             |          | to use.                             |
+--------------+-------------+----------+-------------------------------------+


RESTful Web Services Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Security
~~~~~~~~

Event sources must identify themselves to the VES Event Listener.

There are 2 methods of HTTP authentication supported: Certificate Authentication
and Basic Authentication.

Basic authentication is supported in VES Event Listener for backward
compatibility for existing NFs that are already managed by ONAP. New NFs should
support Certificate Authentication. Because the security is better, NFs may
choose to only support Certificate Authentication and not support Basic
Authentication.

Basic Authentication
++++++++++++++++++++

When using Basic Authentication, the event source must not pass credentials on
the query string.  Credentials must be sent in an Authorization header as
follows:

1. The username and password are formed into one string as
   ``username:password``
2. The resulting string is Base64 encoded to produce the encoded credential.
3. The encoded credential is communicated in the header after the string
   ``Authorization: Basic``

Because the credentials are merely encoded but not encrypted, HTTPS (rather
than HTTP) should be used.  HTTPS will also encrypt and protect event contents.

Sample Request and Response
+++++++++++++++++++++++++++

Sample Request
**************

.. code-block:: http

    POST /eventListener/v7 HTTP/1.1
    Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
    content-type: application/json
    content-length: 12345
    {
        "event": {
            "commonEventHeader": {
                "version": "4.1",
                "vesEventListenerVersion": "7.2",
                "domain": "heartbeat",
                "eventName": "Heartbeat_vIsbcMmc",
                "eventId": "heartbeat0000249",
                "sequence": 0,
                "priority": "Normal",
                "reportingEntityId": "cc305d54-75b4-431b-adb2-eb6b9e541234",
                "reportingEntityName": "ibcx0001vm002oam001",
                "sourceId": "de305d54-75b4-431b-adb2-eb6b9e546014",
                "sourceName": "ibcx0001vm002ssc001",
                "nfVendorName": "Ericsson",
                "nfNamingCode": "ibcx",
                "nfcNamingCode": "ssc",
                "startEpochMicrosec": 1413378172000000,
                "lastEpochMicrosec": 1413378172000000,
                "timeZoneOffset": "UTC-05:30"
            }
        }
    }


Sample Success Response
***********************

.. code-block:: http

    HTTPS/1.1 202 Accepted
    X-MinorVersion: 2
    X-PatchVersion: 0
    X-LatestVersion: 7.2


Mutual TLS Certificate Authentication
+++++++++++++++++++++++++++++++++++++

When using Certificate Authentication, the event source must initialize the
HTTPS connection with TLS 1.2 or higher and execute mutual authentication
procedures according to `RFC5246 <https://tools.ietf.org/html/rfc5246#section-7.4.6>`__.
The event source must authenticate the VES Listener certificate and must
provide its own X.509v3 end-entity certificate to the VES Listener for
authentication. The Subject Name in the end-entity certificate must be used
according to `RFC5280 <https://www.ietf.org/rfc/rfc5280.txt>`__. If a
certificate is provided by the NF but it is invalid, the VES Listener is
expected to reject the connection and not fall back to basic authentication.

Resource Structure
~~~~~~~~~~~~~~~~~~

REST resources are defined with respect to a ServerRoot:

ServerRoot = https://{Domain|IP}:{Port}/{optionalRoutingPath}

The resource structure is provided below::

    {ServerRoot}
        |
        |--- /eventListener/v{apiVersion}
                 |
                 |--- /eventBatch

**Figure 1**: REST Resource Structure

Exceptions
~~~~~~~~~~

RESTful Web Services Exceptions
+++++++++++++++++++++++++++++++

RESTful services generate and send exceptions to clients in response to
invocation errors. Exceptions send HTTP status codes (specified later in
this document for each operation). HTTP status codes may be followed by
an optional JSON exception structure described below. Two types of
exceptions may be defined: service exceptions and policy exceptions.

+-----------+---------------+-------------+-----------------------------------+
| Field Name| Data Type     | Required?   | Description                       |
+===========+===============+=============+===================================+
| messageId | xs:string     | Yes         | Unique message identifier of the  |
|           |               |             | format ‘ABCnnnn’ where ‘ABC’ is   |
|           |               |             | either ‘SVC’ for Service          |
|           |               |             | Exceptions or ‘POL’ for Policy    |
|           |               |             | Exception.                        |
|           |               |             |                                   |
|           |               |             | Exception numbers may be in the   |
|           |               |             | range of 0001 to 9999 where :     |
|           |               |             |                                   |
|           |               |             | -  0001 to 2999 are defined by OMA|
|           |               |             |    (see OMA’s Common_definitions_ |
|           |               |             |    for details)                   |
|           |               |             |                                   |
|           |               |             | -  3000-9999 are available and    |
|           |               |             |    undefined                      |
+-----------+---------------+-------------+-----------------------------------+
| text      | xs:string     | Yes         | Message text, with replacement    |
|           |               |             | variables marked with %n, where n |
|           |               |             | is an index into the list of      |
|           |               |             | <variables> elements, starting at |
|           |               |             | 1                                 |
+-----------+---------------+-------------+-----------------------------------+
| variables | xs:string     | No          | List of zero or more strings that |
|           | [0..unbounded]|             | represent the contents of the     |
|           |               |             | variables used by the message text|
+-----------+---------------+-------------+-----------------------------------+
| url       | xs:anyUrl     | No          | Hyperlink to a detailed error     |
|           |               |             | resource (e.g., an HTML page for  |
|           |               |             | browser user agents).             |
+-----------+---------------+-------------+-----------------------------------+

Service Exceptions
++++++++++++++++++

When a service is not able to process a request, and retrying the
request with the same information will also result in a failure, and
the issue is not related to a service policy issue, then the service
will issue a fault using the service exception fault message.
Examples of service exceptions include invalid input, lack of
availability of a required resource or a processing error.

A service exception uses the letters 'SVC' at the beginning of the
message identifier. ‘SVC’ service exceptions used by the VES Event
Listener API are defined below.

+----------+--------------+-----------------------+----------------+----------+
| MessageId| Description  | Text                  | Variables      | Parent   |
|          | / Comment    |                       |                | HTTP Code|
+==========+==============+=======================+================+==========+
| SVC0001  | General      | <custom error message>| None           | 400      |
|          | service error|                       |                |          |
|          | (see SVC2000)|                       |                |          |
+----------+--------------+-----------------------+----------------+----------+
| SVC0002  | Bad parameter| Invalid input value   | %1: message    | 400      |
|          |              | for message part %1   | part           |          |
+----------+--------------+-----------------------+----------------+----------+
| SVC1000  | No server    | No server resources   | None           | 500      |
|          | resources    | available to process  |                |          |
|          |              | the request           |                |          |
+----------+--------------+-----------------------+----------------+----------+
| SVC2000  | More         | The following service | %1: human      | 400      |
|          | elaborate    | error occurred: %1.   | readable       |          |
|          | version of   |                       | description of |          |
|          | SVC0001      |                       | the error      |          |
|          |              |                       |                |          |
|          |              |  Error code is %2.    | %2: error code |          |
+----------+--------------+-----------------------+----------------+----------+
| SVC2004  | Invalid input| Invalid input value   | %1: attribute  | 400      |
|          | value        | for %1 %2: %3         |                |          |
|          |              |                       | %2: event.com\ |          |
|          |              |                       | monEventHeader\|          |
|          |              |                       | .stndDefined\  |          |
|          |              |                       | Namespace      |          |
|          |              |                       |                |          |
|          |              |                       | %3: Unable to  |          |
|          |              |                       | route event    |          |
|          |              |                       |                |          |
+----------+--------------+-----------------------+----------------+----------+
| SVC2006  | Mandatory    | Mandatory input %1 %2 | %1: attribute  | 400      |
|          | input missing| is missing from       |                |          |
|          |              | request               | %2: event.com\ |          |
|          |              |                       | monEventHeader\|          |
|          |              |                       | .stndDefined\  |          |
|          |              |                       | Namespace      |          |
+----------+--------------+-----------------------+----------------+----------+


Table - Service Exceptions

Policy Exceptions
+++++++++++++++++

When a service is not able to complete because the request fails to
meet a policy criteria, then the service will issue a fault using the
policy exception fault message. To clarify how a policy exception
differs from a service exception, consider that all the input to an
operation may be valid as meeting the required input for the
operation (thus no service exception), but using that input in the
execution of the service may result in conditions that require the
service not to complete. Examples of policy exceptions include
privacy violations, requests not permitted under a governing service
agreement or input content not acceptable to the service provider.

A Policy Exception uses the letters 'POL' at the beginning of the
message identifier. ‘POL’ policy exceptions used by the VES Event
Listener API are defined below.

+----------+---------------+-----------------------+---------------+----------+
| MessageId| Description   |Text                   | Variables     | Parent   |
|          | / Comment     |                       |               | HTTP Code|
+==========+===============+=======================+===============+==========+
| POL0001  | General policy| A policy error        | None          | 401      |
|          | error (see    | occurred.             |               |          |
|          | POL2000)      |                       |               |          |
+----------+---------------+-----------------------+---------------+----------+
| POL1009  | User not      | User has not been     | None          | 401      |
|          | provisioned   | provisioned for       |               |          |
|          | for service   | service               |               |          |
+----------+---------------+-----------------------+---------------+----------+
| POL1010  | User suspended| User has been         | None          | 401      |
|          | from service  | suspended from service|               |          |
+----------+---------------+-----------------------+---------------+----------+
| POL2000  | More elaborate| The following policy  | %1: human     | 401      |
|          | version of    | error occurred: %1.   | readable      |          |
|          | POL0001       | Error code is %2.     | description of|          |
|          |               |                       | the error     |          |
|          |               |                       |               |          |
|          |               |                       | %2: error code|          |
+----------+---------------+-----------------------+---------------+----------+
| POL9003  | Message size  | Message content size  | None          | 400      |
|          | exceeds limit | exceeds the allowable |               |          |
|          |               | limit                 |               |          |
+----------+---------------+-----------------------+---------------+----------+

Table - Policy Exceptions

REST Operation Overview
~~~~~~~~~~~~~~~~~~~~~~~

REST Operation Summary
++++++++++++++++++++++

+---------------------+---------+------------------------------------------+
| **Operation Action**| **HTTP**| Resource URL relative to {ServerRoot}\   |
|                     |         | , which is defined in section 3          |
|                     | **Verb**|                                          |
+---------------------+---------+------------------------------------------+
| publishAnyEvent     | POST    | /eventListener/v{apiVersion}             |
+---------------------+---------+------------------------------------------+
| publishEventBatch   | POST    | /eventListener/v{apiVersion}/eventBatch  |
+---------------------+---------+------------------------------------------+

Table - REST Operation Summary

Api Versioning
++++++++++++++

``apiVersion`` is used to describe the major version number of the event
listener API (which is the same as the major version number of this
specification). When this number changes, the implication is: the new
major version will break clients of older major versions in some way, if
they try to use the new API without modification (e.g., unmodified v1
clients would not be able to use v2 without error).

The Event Listener shall provide the following HTTP headers in response
to all requests. Additionally, clients may populate these headers on
requests to indicate the specific version they are interested in.

-  X-MinorVersion: 2

-  X-PatchVersion: 0

-  X-LatestVersion: 7.2

If a client requests major version 7 (per the REST resource URL) and
does not specify the above headers, then they will be provided with the
latest patch version of 7.0.x (which is 7.0.1). If the client wants a
minor version of major version 7, then they need to supply
the X-MinorVersion header with their request. For example, if they
request major version 7 with X-MinorVersion: 1, they will get the latest
patch version of 7.1, which is 7.1.1.

.. _ves_msg_size_7_2:

Message Size
++++++++++++

The maximum allowed message size is 2 megabytes of uncompressed text.
However, messages of this size have been known to cause performance and data
loss. It is strongly recommended, that messages not exceed 1 megabyte.
In a future version of the specification, a 1 megabyte limit will become
a mandatory requirement.

Operation: publishAnyEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~

Functional Behavior
+++++++++++++++++++

Allows authorized clients to publish any single event to the VES event
listener.

-  Supports only HTTPS access.

-  Uses the HTTP verb POST

-  Supports JSON content types

-  Provides HTTP response codes as well as Service and Policy error
   messages

Call Flow
+++++++++

.. seqdiag::
    :caption: ``publishAnyEvent`` Call Flow

    seqdiag {
      edge_length = 250;
      client  -> listener [label = "POST /eventlistener/v7"];
      client <- listener [label = "HTTP 202 Accepted", note = "sync response"];
      === Error Scenario ===
      client  -> listener [label = "POST /eventlistener/v7"];
      client <- listener [label = "HTTP 4XX/5XX", note = "sync response"];
    }

Input Parameters
++++++++++++++++

Header Fields (note: all parameter names shall be treated as
case-insensitive):

+---------------+----------+----------+---------------------------------------+
| Parameter     | Data Type| Required?| Brief description                     |
+---------------+----------+----------+---------------------------------------+
| Accept        | string   | No       | Determines the format of the body of  |
|               |          |          | the response. Valid values are:       |
|               |          |          |                                       |
|               |          |          | -  application/json                   |
+---------------+----------+----------+---------------------------------------+
| Authorization | string   | No       | The username and password are formed  |
|               |          |          | into one string as                    |
|               |          |          | ``username:password``. This string is |
|               |          |          | then Base64 encoded to produce the    |
|               |          |          | encoded credential which is           |
|               |          |          | communicated in the header after the  |
|               |          |          | string "Authorization: Basic ". See   |
|               |          |          | examples below. If the Authorization  |
|               |          |          | header is missing, then an HTTP 400   |
|               |          |          | Invalid Request message shall be      |
|               |          |          | returned. If the string supplied is   |
|               |          |          | invalid, then an HTTP 401 Unauthorized|
|               |          |          | message shall be returned.            |
+---------------+----------+----------+---------------------------------------+
| Content-length| integer  | No       | Note that content length is limited to|
|               |          |          | 2 Megabyte                            |
|               |          |          | (see :ref:`ves_msg_size_7_2`)         |
+---------------+----------+----------+---------------------------------------+
| Content-type  | string   | Yes      | Must be set to one of the following   |
|               |          |          | values:                               |
|               |          |          |                                       |
|               |          |          | -  application/json                   |
+---------------+----------+----------+---------------------------------------+
| X-MinorVersion| integer  | No       | The minor version of the API requested|
|               |          |          | by the client                         |
+---------------+----------+----------+---------------------------------------+
| X-PatchVersion| integer  | No       | The patch version of the API requested|
|               |          |          | by the client                         |
+---------------+----------+----------+---------------------------------------+
| X-Latest\     | string   | No       | The full version of the API requested |
| Version       |          |          | by the client expressed as            |
|               |          |          | {major}.{minor}.{patch}               |
+---------------+----------+----------+---------------------------------------+

Body Fields:

+--------------+--------------+--------------+-------------------------------+
| **Parameter**| **Data Type**| **Required?**| **Brief description**         |
+--------------+--------------+--------------+-------------------------------+
| Event        | event        | Yes          | Contains the JSON structure of|
|              |              |              | the common event format.      |
+--------------+--------------+--------------+-------------------------------+

Output Parameters
+++++++++++++++++

Header fields:

+----------------+--------------+--------------+------------------------------+
| **Parameter**  | **Data Type**| **Required?**| **Brief description**        |
+----------------+--------------+--------------+------------------------------+
| Content-length | integer      | No           | Used only in error conditions|
+----------------+--------------+--------------+------------------------------+
| Content-type   | string       | No           | Used only in error conditions|
+----------------+--------------+--------------+------------------------------+
| Date           | datetime     | No           | Date time of the response in |
|                |              |              | GMT                          |
+----------------+--------------+--------------+------------------------------+
| X-MinorVersion | integer      | Yes          | The minor version of the API |
|                |              |              | service                      |
+----------------+--------------+--------------+------------------------------+
| X-PatchVersion | integer      | Yes          | The patch version of the API |
|                |              |              | service                      |
+----------------+--------------+--------------+------------------------------+
| X-LatestVersion| string       | Yes          | The full version of the API  |
|                |              |              | service expressed as {major}.|
|                |              |              | {minor}.{patch}              |
+----------------+--------------+--------------+------------------------------+

Body Fields (for success responses): no content is provided.

Body Fields (for error responses):

+--------------+--------------+----------------+------------------------------+
| **Parameter**| **Data Type**| **Required?**  | **Brief description**        |
+--------------+--------------+----------------+------------------------------+
| requestError | requestError | Yes(for errors)| Used only in error conditions|
+--------------+--------------+----------------+------------------------------+

HTTP Status Codes
+++++++++++++++++

+-----+--------------+--------------------------------------------------------+
| Code| Reason Phrase| Description                                            |
+=====+==============+========================================================+
| 202 | Accepted     | The request has been accepted for processing           |
+-----+--------------+--------------------------------------------------------+
| 400 | Bad Request  | Many possible reasons not specified by the other codes |
|     |              | (e.g., missing required parameters or incorrect format)|
|     |              | . The response body may include a further exception    |
|     |              | code and text. HTTP 400 errors may be mapped to SVC0001|
|     |              | (general service error), SVC0002 (bad parameter),      |
|     |              | SVC2004 (Invalid input value), SVC2006 (Mandatory input|
|     |              | is missing from request), SVC2000 (general service     |
|     |              | error with details) or PO9003 (message content size    |
|     |              | exceeds the allowable limit).                          |
+-----+--------------+--------------------------------------------------------+
| 401 | Unauthorized | Authentication failed or was not provided. HTTP 401    |
|     |              | errors may be mapped to POL0001 (general policy error) |
|     |              | or POL2000 (general policy error with details).        |
+-----+--------------+--------------------------------------------------------+
| 404 | Not Found    | The server has not found anything matching the         |
|     |              | Request-URI. No indication is given of whether the     |
|     |              | condition is temporary or permanent.                   |
+-----+--------------+--------------------------------------------------------+
| 405 | Method Not   | A request was made of a resource using a request method|
|     | Allowed      | not supported by that resource (e.g., using PUT on a   |
|     |              | REST resource that only supports POST).                |
+-----+--------------+--------------------------------------------------------+
| 500 | Internal     | The server encountered an internal error or timed out; |
|     | Server Error | please retry (general catch-all server-side error).HTTP|
|     |              | 500 errors may be mapped to SVC1000 (no server         |
|     |              | resources).                                            |
+-----+--------------+--------------------------------------------------------+

Sample Request and Response
+++++++++++++++++++++++++++

Sample Request
**************

.. code-block:: http

    POST  /eventListener/v7 HTTP/1.1
    Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
    content-type: application/json
    content-length: 12345
    X-MinorVersion: 1

    {
        "event": {
            "commonEventHeader": {
                "version": "4.1",
                "vesEventListenerVersion": "7.2",
                "domain": "fault",
                "eventName": "Fault_Vscf:Acs-Ericcson_PilotNumberPoolExhaustion",
                "eventId": "fault0000245",
                "sequence": 1,
                "priority": "High",
                "reportingEntityId": "cc305d54-75b4-431b-adb2-eb6b9e541234",
                "reportingEntityName": "ibcx0001vm002oam001",
                "sourceId": "de305d54-75b4-431b-adb2-eb6b9e546014",
                "sourceName": "scfx0001vm002cap001",
                "nfVendorName": "Ericsson",
                "nfNamingCode": "scfx",
                "nfcNamingCode": "ssc",
                "startEpochMicrosec": 1413378172000000,
                "lastEpochMicrosec": 1413378172000000,
                "timeZoneOffset": "UTC-05:30"
            },
            "faultFields": {
                "faultFieldsVersion": 4.0,
                "alarmCondition": "PilotNumberPoolExhaustion",
                "eventSourceType": "other",
                "specificProblem": "Calls cannot complete - pilot numbers are unavailable",
                "eventSeverity": "CRITICAL",
                "vfStatus": "Active",
                "alarmAdditionalInformation": {
                    "PilotNumberPoolSize": "1000"
                }
            }
        }
    }



Sample Success Response
***********************

.. code-block:: http

    HTTPS/1.1 202 Accepted
    X-MinorVersion: 2
    X-PatchVersion: 0
    X-LatestVersion: 7.2

Sample Error Responses
**********************

Sample Policy Exception
"""""""""""""""""""""""

.. code-block:: http

    HTTPS/1.1 400 Bad Request
    content-type: application/json
    content-length: 12345
    Date: Thu, 04 Jun 2009 02:51:59 GMT
    X-MinorVersion: 2
    X-PatchVersion: 0
    X-LatestVersion: 7.2

    {
      "requestError": {
        "policyException": {
          "messageId": "POL9003",
          "text": "Message content size exceeds the allowable limit",
        }
      }
    }


Sample Service Exception
""""""""""""""""""""""""

.. code-block:: http

    HTTPS/1.1 400 Bad Request
    content-type: application/json
    content-length: 12345
    Date: Thu, 04 Jun 2009 02:51:59 GMT
    X-MinorVersion: 2
    X-PatchVersion: 0
    X-LatestVersion: 7.2

    {
      "requestError": {
        "serviceException": {
          "messageId": "SVC2000",
          "text": "Missing Parameter: %1. Error code is %2"
          "variables": [
            "severity",
            "400"
          ]
        }
      }
    }

Operation: publishEventBatch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Functional Behavior
+++++++++++++++++++

Allows authorized clients to publish a batch of events to the VES event
listener.

- Supports only HTTPS access.

- Uses the HTTP verb POST

- Supports JSON content types

- Provides HTTP response codes as well as Service and Policy error
  messages

``publishEventBatch`` events are handled similarly to a single event. The
acknowledgement from the VES Event Listener is for the ``publishEventBatch`` and
not individual events within the ``publishEventBatch``.

Call Flow
+++++++++

.. seqdiag::
    :caption: ``publishEventBatch`` Call Flow

    seqdiag {
      edge_length = 250;
      client  -> listener [label = "POST /eventlistener/v7/eventBatch"];
      client <- listener [label = "HTTP 202 Accepted", note = "sync response"];
      === Error Scenario ===
      client  -> listener [label = "POST /eventlistener/v7/eventBatch"];
      client <- listener [label = "HTTP 4XX/5XX", note = "sync response"];
    }

Input Parameters
++++++++++++++++

Header Fields (note: all parameter names shall be treated as
case-insensitive):

+---------------+----------+----------+---------------------------------------+
| Parameter     | Data Type| Required?| Brief description                     |
+---------------+----------+----------+---------------------------------------+
| Accept        | string   | No       | Determines the format of the body of  |
|               |          |          | the response. Valid values are:       |
|               |          |          |                                       |
|               |          |          | -  application/json                   |
+---------------+----------+----------+---------------------------------------+
| Authorization | string   | No       | The username and password are formed  |
|               |          |          | into one string as "username:password"|
|               |          |          | . This string is then Base64 encoded  |
|               |          |          | to produce the encoded credential     |
|               |          |          | which is communicated in the header   |
|               |          |          | after the string "Authorization:      |
|               |          |          | Basic". See examples below. If the    |
|               |          |          | Authorization header is missing, then |
|               |          |          | an HTTP 400 Invalid Request message   |
|               |          |          | shall be returned. If the string      |
|               |          |          | supplied is invalid, then an HTTP 401 |
|               |          |          | Unauthorized message shall be         |
|               |          |          | returned.                             |
+---------------+----------+----------+---------------------------------------+
| Content-length| integer  | No       | Note that content length is limited to|
|               |          |          | 2 megabyte                            |
|               |          |          | (see :ref:`ves_msg_size_7_2`).        |
+---------------+----------+----------+---------------------------------------+
| Content-type  | string   | Yes      | Must be set to one of the following   |
|               |          |          | values:                               |
|               |          |          |                                       |
|               |          |          | -  application/json                   |
+---------------+----------+----------+---------------------------------------+
| X-MinorVersion| integer  | No       | The minor version of the API requested|
|               |          |          | by the client                         |
+---------------+----------+----------+---------------------------------------+
| X-PatchVersion| integer  | No       | The patch version of the API requested|
|               |          |          | by the client                         |
+---------------+----------+----------+---------------------------------------+
| X-Latest\     | string   | No       | The full version of the API requested |
| Version       |          |          | by the client expressed as            |
|               |          |          | {major}.{minor}.{patch}               |
+---------------+----------+----------+---------------------------------------+

Body Fields:

+--------------+--------------+--------------+-------------------------------+
| **Parameter**| **Data Type**| **Required?**| **Brief description**         |
+--------------+--------------+--------------+-------------------------------+
| eventList    | eventList    | Yes          | Array of events conforming to |
|              |              |              | the common event format. All  |
|              |              |              | events must belong to a       |
|              |              |              | single domain.                |
|              |              |              | In case of stndDefined domain |
|              |              |              | all events must have the same |
|              |              |              | stndDefinedNamespace value    |
|              |              |              | set.                          |
+--------------+--------------+--------------+-------------------------------+

Output Parameters
+++++++++++++++++

Header fields:

+----------------+--------------+--------------+------------------------------+
| **Parameter**  | **Data Type**| **Required?**| **Brief description**        |
+----------------+--------------+--------------+------------------------------+
| Content-length | integer      | No           | Used only in error conditions|
+----------------+--------------+--------------+------------------------------+
| Content-type   | string       | No           | Used only in error conditions|
+----------------+--------------+--------------+------------------------------+
| Date           | datetime     | No           | Date time of the response in |
|                |              |              | GMT                          |
+----------------+--------------+--------------+------------------------------+
| X-MinorVersion | integer      | Yes          | The minor version of the API |
|                |              |              | service                      |
+----------------+--------------+--------------+------------------------------+
| X-PatchVersion | integer      | Yes          | The patch version of the API |
|                |              |              | service                      |
+----------------+--------------+--------------+------------------------------+
| X-LatestVersion| string       | Yes          | The full version of the API  |
|                |              |              | service expressed as         |
|                |              |              | {major}.{minor}.{patch}      |
+----------------+--------------+--------------+------------------------------+

Body Fields (for success responses: no content is provided.

Body Fields (for error responses):

+--------------+--------------+----------------+------------------------------+
| **Parameter**| **Data Type**| **Required?**  | **Brief description**        |
+--------------+--------------+----------------+------------------------------+
| requestError | requestError | Yes(for errors)| Used only in error conditions|
+--------------+--------------+----------------+------------------------------+

HTTP Status Codes
+++++++++++++++++

+-----+--------------+--------------------------------------------------------+
| Code| Reason Phrase| Description                                            |
+=====+==============+========================================================+
| 202 | Accepted     | The request has been accepted for processing           |
+-----+--------------+--------------------------------------------------------+
| 400 | Bad Request  | Many possible reasons not specified by the other codes |
|     |              | (e.g., missing required parameters or incorrect format)|
|     |              | . The response body may include a further exception    |
|     |              | code and text. HTTP 400 errors may be mapped to SVC0001|
|     |              | (general service error), SVC0002 (bad parameter),      |
|     |              | SVC2000 (general service error with details) or PO9003 |
|     |              | (message content size exceeds the allowable limit).    |
+-----+--------------+--------------------------------------------------------+
| 401 | Unauthorized | Authentication failed or was not provided. HTTP 401    |
|     |              | errors may be mapped to POL0001 (general policy error) |
|     |              | or POL2000 (general policy error with details).        |
+-----+--------------+--------------------------------------------------------+
| 404 | Not Found    | The server has not found anything matching the         |
|     |              | Request-URI. No indication is given of whether the     |
|     |              | condition is temporary or permanent.                   |
+-----+--------------+--------------------------------------------------------+
| 405 | Method Not   | A request was made of a resource using a request method|
|     | Allowed      | not supported by that resource (e.g., using PUT on a   |
|     |              | REST resource that only supports POST).                |
+-----+--------------+--------------------------------------------------------+
| 500 | Internal     | The server encountered an internal error or timed out; |
|     | Server Error | please retry (general catch-all server-side error).HTTP|
|     |              | 500 errors may be mapped to SVC1000 (no server         |
|     |              | resources).                                            |
+-----+--------------+--------------------------------------------------------+

Sample Request and Response
+++++++++++++++++++++++++++

Sample Request
**************

.. code-block:: http

    POST /eventListener/v7/eventBatch HTTP/1.1
    Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
    content-type: application/json
    content-length: 12345
    X-MinorVersion: 1

    {
       "eventList": [
          {
             "commonEventHeader": {
                "version": "4.1",
                "vesEventListenerVersion": "7.2",
                "domain": "fault",
                "eventName": "Fault_Vscf:Acs-Ericcson_PilotNumberPoolExhaustion",
                "eventId": "fault0000250",
                "sequence": 1,
                "priority": "High",
                "reportingEntityId": "cc305d54-75b4-431b-adb2-eb6b9e541234",
                "reportingEntityName": "ibcx0001vm002oam0011234",
                "sourceId": "de305d54-75b4-431b-adb2-eb6b9e546014",
                "sourceName": "scfx0001vm002cap001",
                "nfVendorName": "Ericsson",
                "nfNamingCode": "scfx",
                "nfcNamingCode": "ssc",
                "startEpochMicrosec": 1413378172000000,
                "lastEpochMicrosec": 1413378172000000,
                "timeZoneOffset": "UTC-05:30"
             },
             "faultFields": {
                "faultFieldsVersion": 4.0,
                "alarmCondition": "PilotNumberPoolExhaustion",
                "eventSourceType": "other",
                "specificProblem": "Calls cannot complete - pilot numbers are unavailable",
                "eventSeverity": "CRITICAL",
                "vfStatus": "Active",
                "alarmAdditionalInformation": {
                    "PilotNumberPoolSize": "1000"
                }
             }
          },
          {
             "commonEventHeader": {
                "version": "4.1",
                "vesEventListenerVersion": "7.2",
                "domain": "fault",
                "eventName": " Fault_Vscf:Acs-Ericcson_RecordingServerUnreachable",
                "eventId": "fault0000251",
                "sequence": 0,
                "priority": "High",
                "reportingEntityId": "cc305d54-75b4-431b-adb2-eb6b9e541234",
                "reportingEntityName": "ibcx0001vm002oam0011234",
                "sourceId": "de305d54-75b4-431b-adb2-eb6b9e546014",
                "sourceName": "scfx0001vm002cap001",
                "nfVendorName": "Ericsson",
                "nfNamingCode": "scfx",
                "nfcNamingCode": "ssc",
                "startEpochMicrosec": 1413378172000010,
                "lastEpochMicrosec": 1413378172000010,
                "timeZoneOffset": "UTC-05:30"
             },
             "faultFields": {
                "faultFieldsVersion": 4.0,
                "alarmCondition": "RecordingServerUnreachable",
                "eventSourceType": "other",
                "specificProblem": "Recording server unreachable",
                "eventSeverity": "CRITICAL",
                "vfStatus": "Active"
             }
          }
       ]
    }

Sample Success Response
***********************

.. code-block:: http

    HTTPS/1.1 202 Accepted
    X-MinorVersion: 2
    X-PatchVersion: 0
    X-LatestVersion: 7.2

Sample Error Responses
**********************

Sample Policy Exception
"""""""""""""""""""""""

.. code-block:: http

    HTTPS/1.1 400 Bad Request
    content-type: application/json
    content-length: 12345
    Date: Thu, 04 Jun 2009 02:51:59 GMT
    X-MinorVersion: 2
    X-PatchVersion: 0
    X-LatestVersion: 7.2

    {
      "requestError": {
        "policyException": {
          "messageId": "POL9003",
          "text": "Message content size exceeds the allowable limit",
        }
      }
    }



Sample Service Exception
""""""""""""""""""""""""

.. code-block:: http

    HTTPS/1.1 400 Bad Request
    content-type: application/json
    content-length: 12345
    Date: Thu, 04 Jun 2009 02:51:59 GMT
    X-MinorVersion: 2
    X-PatchVersion: 0
    X-LatestVersion: 7.2

    {
      "requestError": {
        "serviceException": {
          "messageId": "SVC2000",
          "text": "Missing Parameter: %1. Error code is %2"
          "variables": [
            "severity",
            "400"
          ]
        }
      }
    }


Terminology
^^^^^^^^^^^

Terminology used in this document is summarized below:

**A&AI**. Active & Available Inventory is the ONAP component that
provides data views of Customer Subscriptions, Products, Services,
Resources, and their relationships.

**Alarm Condition**. Short name of the alarm condition/problem, such as
a trap name.

**APPC (formerly APP-C)**. Application Controller. Handles the life
cycle management of Virtual Network Functions (VNFs).

**Common Event Format**. A JSON schema describing events sent to the VES
Event Listener.

**Common Event Header**. A component of the Common Event Format JSON
structure. This datatype consists of fields common to all events.

**DCAE**. Data Collection Analysis and Events. DCAE is the ONAP
subsystem that supports closed loop control and higher-level correlation
for business and operations activities. DCAE collects performance,
usage, and configuration data, provides computation of analytics, aids
in trouble-shooting and management, and publishes event, data, and
analytics to the rest of the ONAP system for FCAPS functionality.

**DMaaP.** Data Movement as a Platform. A set of common services
provided by ONAP, including a Message Router, Data Router, and a Data
Bus Controller.

**Domain**. In VES, an event ‘domain’ identifies a broad category of
events (e.g., ‘fault’ or ‘measurement’), each of which is associated
with a VES domain field block, which is sent with the commonEventHeader
when events of that category are generated.

**Epoch**. The number of seconds that have elapsed since
00:00:00 \ `Coordinated Universal
Time <https://en.wikipedia.org/wiki/Coordinated_Universal_Time>`__ (UTC),
Thursday, 1 January 1970. Every day is treated as if it contains exactly
86400 seconds, so \ `leap
seconds <https://en.wikipedia.org/wiki/Leap_second>`__ are not applied
to seconds since the Epoch. In VES Epoch times are measured in
microseconds.

**Event.** A well-structured packet of network management information
identified by an eventName which is asynchronously communicated to one
or more instances of an Event Listener service to subscribers interested
in that eventName. Events can convey measurements, faults, syslogs,
threshold crossing alerts, and others types of information.

**Event Id**. Event key that is unique to the event source. The key must
be unique within notification life cycle similar to EventID from 3GPP.
It could be a sequential number, or a composite key formed from the
event fields, such as sourceName\_alarmCondition\_startEpoch. The
eventId should not include whitespace. For fault events, eventId is the
eventId of the initial alarm; if the same alarm is raised again for
changed, acknowledged or cleared cases, eventId must be the same as the
initial alarm (along with the same startEpochMicrosec and an incremental
sequence number.

**Event Name**. Identifier for specific types of events. Specific
eventNames registered by the YAML may require that certain fields, which
are optional in the Common Event Format, be present when events with
that eventName are published.

**Event Streaming**. The delivery of network management event
information in real time.

**Extensible Data Structures**. Data structures (e.g., hashMap) that
allow event sources to send information not specifically identified in
the VES schema.

**Hash Map**. A hash table, or data structure, used to implement an
associative array, a structure than can map keys to values. In VES 6.0,
all name-value pair structures were changed to hash maps (i.e., {‘name’:
‘keyName’, ‘value’: ‘keyValue’} was replaced with {‘keyName’:
‘keyValue’}).

**IPMI**. The `Intelligent Platform Management
Interface <https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface>`__.

**JSON**. Java Script Object Notation. JSON is an
`open-standard <https://en.wikipedia.org/wiki/Open_standard>`__ `file
format <https://en.wikipedia.org/wiki/File_format>`__ that uses
`human-readable <https://en.wikipedia.org/wiki/Human-readable_medium>`__
text to transmit data objects consisting of `attribute–value
pairs <https://en.wikipedia.org/wiki/Attribute%E2%80%93value_pair>`__
and `array data types <https://en.wikipedia.org/wiki/Array_data_type>`__
(or any other
`serializable <https://en.wikipedia.org/wiki/Serialization>`__ value).
It is a very common `data <https://en.wikipedia.org/wiki/Data>`__ format
used for
`asynchronous <https://en.wikipedia.org/wiki/Asynchronous_I/O>`__
browser–server communication.

**NF**. Network Function. Generalized name for a VNF or PNF.

**NFC**. Network Function Component. Generalized name for a VNFC or a
component of a PNF.

**ONAP**. `Open Network Automation Platform <https://www.onap.org/>`__.

**PNF**. Physical Network Function.

**Policy**. Course of action for the management of the network. The ONAP
Policy Framework is a comprehensive policy design, deployment, and
execution environment. The Policy Framework is the ***decision making***
component in `an ONAP
system <https://www.onap.org/wp-content/uploads/sites/20/2017/12/ONAP_CaseSolution_Architecture_120817_FNL.pdf>`__.
It allows you to specify, deploy, and execute the governance of the
features and functions in your ONAP system, be they closed loop,
orchestration, or more traditional open loop use case implementations.
The Policy Framework is the component that is the source of truth for
all policy decisions.

**Reporting Entity Name**. Name of the entity reporting the event or
detecting a problem in another vnf/vm or pnf which is experiencing the
problem. May be the same as the sourceName. Not used for performance
measurements currently.

**SDC**. Service Design and Creation Platform: The ONAP visual modeling
and design tool. It creates internal metadata that describes assets used
by all ONAP components, both at design time and run time. The SDC
manages the content of a catalog, and assemblies of selected catalog to
define how and when VNFs are realized in a target environment.

**Source Name**: Name of the entity experiencing the event issue, which
may be detected and reported by a separate reporting entity. The
sourceName identifies the device for which data is collected. A valid
sourceName must be inventoried in A&AI.

**Specific Problem**. Description of the alarm or problem.

**VES**. Virtual Function Event Stream. In 6.0, the definition of VES
was expanded to include event streaming for VNF, PNF and infrastructure.
The VES Event Listener can receive any event sent in the VES Common
Event Format.

**VES Event Listener**. A RESTful connectionless push event listener
capable of receiving single events or batches of events sent in the
Common Event Format.

**VM**. Virtual Machine.

**VNF**. Virtual Network Function. A VNF is a virtualized task formerly
carried out by proprietary, dedicated network hardware. (Examples:
virtual firewall, virtual DNS). A VNF can also be defined as a specific
kind of Vendor Software Product.

**YAML**. A `data serialization
language <https://en.wikipedia.org/wiki/Data_serialization_language>`__
and superset of JSON.

**VNFC**. Virtual Network Function Component. A VNFC is a part of a VNF.
It is a stand-alone executable that is loosely-coupled, granular,
re-usable, and responsible for a single capability.

Appendix: Historical Change Log
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the latest changes, see the Change Block just before the Table of
Contents.

+-----------+---------+-------------------------------------------------------+
| Date      | Revision| Description                                           |
+-----------+---------+-------------------------------------------------------+
| 5/22/2015 | 0.1     | Initial Release - Draft                               |
+-----------+---------+-------------------------------------------------------+
| 5/29/2015 | 0.2     | -  Introduction: removed all system names and         |
|           |         |    references to internal AT&T components             |
|           |         |                                                       |
|           |         | -  Security: changed ‘event publisher’ to             |
|           |         |    ‘event source’                                     |
|           |         |                                                       |
|           |         | -  Generic Event Format: updated the JSON schema per  |
|           |         |    the below:                                         |
|           |         |                                                       |
|           |         | -  eventHeader: clarified the description of id, made |
|           |         |    sourceId a required field, changed the datatype of |
|           |         |    timestamps to timestamp [ ]                        |
|           |         |                                                       |
|           |         | -  performanceFields: removed overflowFields          |
|           |         |                                                       |
|           |         | -  tmestamp: added a description of this datatype     |
|           |         |                                                       |
|           |         | -  Exceptions: fixed indentation of sections          |
|           |         |                                                       |
|           |         | -  Approvers: updated the list of approvers and added |
|           |         |    attuids                                            |
+-----------+---------+-------------------------------------------------------+
| 6/3/2015  | 0.3     | -  Updated the security section to use HTTP Basic     |
|           |         |    Authentication per AT&T REST standards. Updated the|
|           |         |    input parameters and messaging examples to use the |
|           |         |    new security scheme.                               |
+-----------+---------+-------------------------------------------------------+
| 6/5/2015  | 0.4     | -  Added otherFields sub section to the defined       |
|           |         |    datatypes                                          |
|           |         |                                                       |
|           |         | -  Added locale field to the eventHeader.             |
+-----------+---------+-------------------------------------------------------+
| 6/5/2015  | 0.5     | -  Updated the embedded event format json schema to   |
|           |         |    match the changes made in v0.4                     |
+-----------+---------+-------------------------------------------------------+
| 6/10/2015 | 0.6     | -  Updated the {ServerRoot} format to contain an      |
|           |         |    optional routing path (for D2 service modules).    |
+-----------+---------+-------------------------------------------------------+
| 7/7/2015  | 0.7     |     Common Event Format updates:                      |
|           |         |                                                       |
|           |         | -  EventHeader: added ‘measurement’ to the ‘domain’   |
|           |         |    enumeration; changed ‘locale’ to ‘location’ and    |
|           |         |    clarified in the description that this should be a |
|           |         |    clli code                                          |
|           |         |                                                       |
|           |         | -  Added a MeasurementFields datatype, which required |
|           |         |    the addition of the following datatypes:           |
|           |         |    codecsInUse, cpuUsage, diskUsage, featuresInUse,   |
|           |         |    memoryUsage                                        |
+-----------+---------+-------------------------------------------------------+
| 7/15/2015 | 1.0     | -  Changed sourceInstance in the eventHeader to be an |
|           |         |    array of name value pairs                          |
|           |         |                                                       |
|           |         | -  Changed the performanceFields block to             |
|           |         |    thresholdCrossingAlertFields. Updated the domain   |
|           |         |    field of the eventHeader to match.                 |
+-----------+---------+-------------------------------------------------------+
| 7/23/2015 | v1.1    | Changes to eventHeader data format:                   |
|           |         |                                                       |
|           |         | -  moved sourceInstance to internalHeaderFields       |
|           |         |                                                       |
|           |         | -  moved serviceInstanceId to internalHeaderFields    |
|           |         |                                                       |
|           |         | -  moved productId to internalHeaderFields            |
|           |         |                                                       |
|           |         | -  moved subscriberId to internalHeaderFields         |
|           |         |                                                       |
|           |         | -  moved location to internalHeaderFields             |
|           |         |                                                       |
|           |         | -  added the following new fields in                  |
|           |         |    internalHeaderFields: policyType, policyName,      |
|           |         |    correlationEventType, correlationType,             |
|           |         |    correlationName, correlationRootEventId            |
|           |         |                                                       |
|           |         | Changes to faultFields data format:                   |
|           |         |                                                       |
|           |         | -  moved the eventSourceDeviceDescription to          |
|           |         |    internalFaultFields and renamed it                 |
|           |         |    equipmentVendorModel                               |
|           |         |                                                       |
|           |         | -  moved eventSourceHostname to internalFaultFields   |
|           |         |                                                       |
|           |         | -  changed alarmObjectInterface to alarmInterfaceA    |
|           |         |                                                       |
|           |         | -  changed alarmRemoteObject to alarmRemoteObjectZ and|
|           |         |     moved it to internalFaultFields                   |
|           |         |                                                       |
|           |         | -  changed alarmRemoteObjectInterface to              |
|           |         |    alarmInterfaceZ and moved it to internalFaultFields|
|           |         |                                                       |
|           |         | Changes to thresholdCrossingFields data format:       |
|           |         |                                                       |
|           |         | -  changed several references from the old            |
|           |         |    ‘performanceFields’ block to the new               |
|           |         |    ‘thresholdCrossingFields’ block                    |
|           |         |                                                       |
|           |         | Other:                                                |
|           |         |                                                       |
|           |         | -  Fixed several comma and colon syntax errors in the |
|           |         |    JSON schema as detected by a JSON schema syntax    |
|           |         |    checker.                                           |
+-----------+---------+-------------------------------------------------------+
| 8/11/2015 | v1.2    | Timestamp format:                                     |
|           |         |                                                       |
|           |         | -  Section 4.18: added a note in the datetime field of|
|           |         |    the Timestamp datatype specifying the (GMT) format |
|           |         |    required                                           |
|           |         |                                                       |
|           |         | -  Updated the JSON schema with the same information  |
|           |         |                                                       |
|           |         | Event Header Severity Enumeration:                    |
|           |         |                                                       |
|           |         | -  Section 4.8: modified the severity enumeration to  |
|           |         |    remove the numbers in parentheses that followed the|
|           |         |    names. The names were not changed.                 |
|           |         |                                                       |
|           |         | -  Updated the JSON schema with the same information. |
+-----------+---------+-------------------------------------------------------+
| 8/20/2015 | v1.3    | JSON Schema rev’d to v9:                              |
|           |         |                                                       |
|           |         | -  Alphabetized all fields in the JSON schema         |
|           |         |                                                       |
|           |         | -  Fixed the way arrays were specified (JSON schema   |
|           |         |    syntax issue)                                      |
|           |         |                                                       |
|           |         | Sample Responses:                                     |
|           |         |                                                       |
|           |         | -  2.1.1.1: alphabetized fields, fixed timestamps     |
|           |         |    array depiction, fixed severity enum value to      |
|           |         |    conform to latest format                           |
|           |         |                                                       |
|           |         | -  6.2.6.1: alphabetized fields, fixed timestamps     |
|           |         |    array depiction, fixed severity enum value to      |
|           |         |    conform to latest format                           |
|           |         |                                                       |
|           |         | -  6.3.6.1: alphabetized fields, fixed timestamps     |
|           |         |    array depiction, fixed severity enum value to      |
|           |         |    conform to latest format                           |
|           |         |                                                       |
|           |         | -  6.4.6.1: alphabetized fields, fixed timestamps     |
|           |         |    array depiction, fixed eventList array depection,  |
|           |         |    fixed severity enum value to conform to latest     |
|           |         |    format                                             |
+-----------+---------+-------------------------------------------------------+
| 9/16/2015 | v1.4    | JSON Schema rev’d to v10:                             |
|           |         |                                                       |
|           |         | - Fixed an error in the way that the top level        |
|           |         |   "event" object was specified in the v9 json schema. |
|           |         |   This was discovered when validating examples        |
|           |         |   against the schema using this site:                 |
|           |         |   http://json-schema-validator.herokuapp.com/index.jsp|
|           |         |                                                       |
|           |         | - Changed the embedded json file in section 4         |
|           |         |                                                       |
|           |         | Sample Responses:                                     |
|           |         |                                                       |
|           |         | - Removed an extra comma after the timestamp brace in |
|           |         |   section 6.2.6 and 6.3.6.                            |
+-----------+---------+-------------------------------------------------------+
| 11/11/2015| v1.5    | Section 4 was the only section changed: JSON Schema   |
|           |         | rev’d to v11 and Datatype tables were updated to match|
|           |         | . Numerous data structure changes were made based on  |
|           |         | VNF vendor proof of concept feedback. Modified sample |
|           |         | requests and responses to match.                      |
+-----------+---------+-------------------------------------------------------+
| 11/12/2015| v1.6    | -  The internalFaultFields were merged into the       |
|           |         |    internalHeaderFields; then the internalFaultFields |
|           |         |    datatype was deleted.                              |
|           |         |                                                       |
|           |         | -  Updated the JSON schema to v12.                    |
|           |         |                                                       |
|           |         | -  Also corrected some background color issues in the |
|           |         |    sample requests and responses.                     |
+-----------+---------+-------------------------------------------------------+
| 1/18/2016 | v1.7    | -  Section 2 changes: updated the sample request to   |
|           |         |    conform with the changes below                     |
|           |         |                                                       |
|           |         | -  Section 4 datatype changes:                        |
|           |         |                                                       |
|           |         | -  Changed 'eventHeader' to 'commonEventHeader'       |
|           |         |                                                       |
|           |         | -  Moved 'eventSeverity' from the 'commonEventHeader' |
|           |         |    to 'faultFields'                                   |
|           |         |                                                       |
|           |         | -  Added 'priority' to 'commonEventHeader'            |
|           |         |                                                       |
|           |         | -  moved 'vFstatus' to 'faultFields'                  |
|           |         |                                                       |
|           |         | -  removed 'firstDateTime' and 'lastDateTime' and     |
|           |         |    changed 'firstEpoch' to 'startEpochMicrosec' and   |
|           |         |    changed 'lastEpoch' to 'lastEpochMicrosec'.        |
|           |         |                                                       |
|           |         | -  Added 'functionalRole' to the commonEventHeader    |
|           |         |                                                       |
|           |         | -  In the commonEventHeader, changed the 'eventDomain'|
|           |         |    enumeration to remove 'measurements' and add       |
|           |         |    'measurementsForVfScaling'.                        |
|           |         |                                                       |
|           |         | -  Changed the 'measurementFields' to                 |
|           |         |    'measurementsForVfScalingFields'                   |
|           |         |                                                       |
|           |         | -  In the commonEventHeader, changed the following    |
|           |         |    fields:                                            |
|           |         |                                                       |
|           |         | -  'eventDomain' to 'domain'                          |
|           |         |                                                       |
|           |         | -  'eventSequence' to 'sequence'                      |
|           |         |                                                       |
|           |         | -  'eventSourceId' to 'sourceId'                      |
|           |         |                                                       |
|           |         | -  'eventSounceName' to 'sourceName'                  |
|           |         |                                                       |
|           |         | -  Updated the JSON schema to v13                     |
|           |         |                                                       |
|           |         | -  Section 6 changes: updated the input parameters and|
|           |         |    sample requests to conform to the changes above.   |
|           |         |                                                       |
|           |         | -  Section 7: changed the section from Approvers to   |
|           |         |    Contributors.                                      |
+-----------+---------+-------------------------------------------------------+
| 1/22/2016 | v1.8    | -  Section 4: Added support for ‘mobileFlow’ in the   |
|           |         |    commonEventHeader ‘domain’ enumeration. Added the  |
|           |         |    mobileFlowFields datatype and the gtpPerFlowMetrics|
|           |         |    datatype referenced by that datatype.              |
|           |         |                                                       |
|           |         | -  Section 7: alphabetized the contributors           |
+-----------+---------+-------------------------------------------------------+
| 2/11/2016 | v1.9    | -  Added section 1.3: Naming Standard for Event Types |
+-----------+---------+-------------------------------------------------------+
| 2/12/2016 | v2.0    | -  Updated request – response examples to reflect the |
|           |         |    naming standards for event types introduced in v1.9|
|           |         |                                                       |
|           |         | -  Added a paragraph on use of Avro as a transport in |
|           |         |    section 1.4                                        |
+-----------+---------+-------------------------------------------------------+
| 3/11/2016 | v2.1    | -  Updated the embedded JSON schema to v15 to fix a   |
|           |         |    typo in the required fields for the                |
|           |         |    measurementsForVfScalingFields, namely, changed    |
|           |         |    ‘configuredEntites’ to ‘configuredEntities’.       |
|           |         |    Additionally, added an ‘Event Listener’ title block|
|           |         |    at the bottom of the file with a single required   |
|           |         |    event object.                                      |
+-----------+---------+-------------------------------------------------------+
| 3/15/2016 | v2.2    | -  Added mobileFlowFields to the event datatype       |
|           |         |    definition in section 4.7 and updated the embedded |
|           |         |    json schema at the top of section 4 to v16.        |
+-----------+---------+-------------------------------------------------------+
| 4/26/2016 | v2.3    | -  Generic Event Format updates: 1) made ‘priority’   |
|           |         |    lowercase in the Word doc table for                |
|           |         |    commonEventHeader; 2) added ‘requestError’ data    |
|           |         |    structure to the Word doc and JSON schema (which is|
|           |         |    now at v17)                                        |
+-----------+---------+-------------------------------------------------------+
| 4/27/2016 | v2.4    | -  JSON Schema: In the 'event' data structure, changed|
|           |         |    'thresholdCrossingFields' to                       |
|           |         |    'thresholdCrossingAlertFields' to product v18 of   |
|           |         |    the schema.                                        |
|           |         |                                                       |
|           |         | -  'codecsInUse' data structure: changed 'numberInUse'|
|           |         |     to 'codecUtilization’                             |
+-----------+---------+-------------------------------------------------------+
| 5/26/2016 | v2.5    | -  Changed responses from ‘204 No Content’ to ‘202    |
|           |         |    Accepted’ and added a body to the response that    |
|           |         |    enable AT&T to throttle the events being sent      |
|           |         |    and/or to request the current state of throttling  |
|           |         |    at the event source.                               |
|           |         |                                                       |
|           |         | -  Added new datatypes to support the above:          |
|           |         |    eventDomainThrottleSpecification,                  |
|           |         |    eventDomainThrottleSpecificationList,              |
|           |         |    eventThrottlingState, suppressedNvPairs            |
|           |         |                                                       |
|           |         | -  Modifed the commonEventFormat json schema to v19   |
|           |         |                                                       |
|           |         | -  Note: for the VendorEventListener: added new       |
|           |         |    licensing language on the back of the title page;  |
|           |         |    added an "attCopyrightNotice" definition at the top|
|           |         |    of the commonEventFormat\_Vendors.json file; also  |
|           |         |    removed all references to internalHeaderFields from|
|           |         |    this file and from the VendorEventListener spec.   |
+-----------+---------+-------------------------------------------------------+
| 8/9/2016  | v2.6    | -  commonHeader: added a note on the description of   |
|           |         |    sourceId and sourceName in the commonHeader: "use  |
|           |         |    reportingEntity for domains that provide more      |
|           |         |    detailed source info"                              |
|           |         |                                                       |
|           |         | -  commonHeader: deleted the capacity,                |
|           |         |    measurementsForVfScaling and usage domains in the  |
|           |         |    domain enumeration                                 |
|           |         |                                                       |
|           |         | -  commonHeader: added the following domains to the   |
|           |         |    domain enumeration: licensingKci, scalingKpi,      |
|           |         |    stateChange                                        |
|           |         |                                                       |
|           |         | -  event: removed references to capacityFields,       |
|           |         |    measurementsForVfScalingFields and usageFields and |
|           |         |    added references to licensingKciFields,            |
|           |         |    scalingKpiFields, stateChangeFields                |
|           |         |                                                       |
|           |         | -  licensingKciFields: added this section along with  |
|           |         |    'additionalMeasurements', which is an optional list|
|           |         |    of measurementGroup structures. Changed the name of|
|           |         |    kciFieldsVersion to licensingKciFieldsVersion.     |
|           |         |                                                       |
|           |         | -  scalingKpiFields: added this section but changed   |
|           |         |    measurementFieldsVersion to scalingKpiFieldsVersion|
|           |         |                                                       |
|           |         | -  stateChangeFields: added this section along with   |
|           |         |    'additionalFields', which is an optional list of   |
|           |         |    name-value pairs. Other fields included newState   |
|           |         |    and oldState which were enumerations of the        |
|           |         |    following possible states: 'inService',            |
|           |         |    'maintenance', 'outOfService'                      |
|           |         |                                                       |
|           |         | -  sysLogFields: added 'additionalFields', which is an|
|           |         |    optional list of name-value pairs                  |
|           |         |                                                       |
|           |         | -  vNicUsage: added two required fields to the        |
|           |         |    vNicUsage data structure: packetsIn and packetsOut |
+-----------+---------+-------------------------------------------------------+
| 8/10/2016 | v2.7    | -  commonHeader: removed the note on the description  |
|           |         |    of sourceId and sourceName in the commonHeader:    |
|           |         |    "use reportingEntity for domains that provide more |
|           |         |    detailed source info"                              |
|           |         |                                                       |
|           |         | -  commonHeader: added measurementsForVfScaling domain|
|           |         |    back and removed the licensingKci and scalingKpi   |
|           |         |    domains                                            |
|           |         |                                                       |
|           |         | -  event: removed references to licensingKciFields and|
|           |         |    scalingKpiFields; added references to              |
|           |         |    measurementsForVfScalingFields                     |
|           |         |                                                       |
|           |         | -  measurementsForVfScalingFields: combined the       |
|           |         |    kciDetail and kpiDetail structures into the        |
|           |         |    measurementsForVfScalingFields structure;          |
|           |         |    referenced the errors structure                    |
|           |         |                                                       |
|           |         | -  errors: added a new structure to capture the       |
|           |         |    receive and transmit errors for the measurements   |
|           |         |    domain                                             |
|           |         |                                                       |
|           |         | -  removed the following structures: kci, kpi,        |
|           |         |    scalingKpiFields and licensingKciFields            |
|           |         |                                                       |
|           |         | -  eventDomainThrottleSpecification: updated the      |
|           |         |    reference to commonEventHeader domain field        |
|           |         |                                                       |
|           |         | -  faultFields: removed the numbers from the          |
|           |         |    enumerated strings for eventSourceType             |
|           |         |                                                       |
|           |         | -  vNicUsage: made the broadcast, multicast and       |
|           |         |    unicast fields optional                            |
|           |         |                                                       |
|           |         | -  contributors: updated Alok’s organizational area   |
+-----------+---------+-------------------------------------------------------+
| 8/12/2016 | v2.8    | -  commonHeader: copied the descriptions of sourceId  |
|           |         |    and sourceName from the JSON schema into the word  |
|           |         |    document tables.                                   |
|           |         |                                                       |
|           |         | -  sample request examples: moved the                 |
|           |         |    reportingEntityId and reportingEntityNames to the  |
|           |         |    same relative place in all sample requests in the  |
|           |         |    document                                           |
|           |         |                                                       |
|           |         | -  Fixed the sample request shown for                 |
|           |         |    publishEventBatch to take an eventList as input.   |
|           |         |                                                       |
|           |         | -  Fixed the sample request shown for                 |
|           |         |    publishSpecificTopic to put the topic in the URL   |
|           |         |                                                       |
|           |         | -  errors: changed the receiveErrors and              |
|           |         |    transmitErrors fields to be datatype number        |
|           |         |                                                       |
|           |         | -  codesInUse: changed 'codecUtilization' to          |
|           |         |    'numberinUse'                                      |
|           |         |                                                       |
|           |         | -  vNicUsage: updated the description of the fields   |
+-----------+---------+-------------------------------------------------------+
| 8/27/2016 | v2.9    | -  Added a note "(currently: 1.1)" in the descriptions|
|           |         |    of the following fields: commonEventHeader:version,|
|           |         |    faultFields:faultFieldsVersion,                    |
|           |         |    measurementsForVfScalingFields:measurementsForVf\  |
|           |         |    ScalingFieldsVersion, stateChangeFields:state\     |
|           |         |    ChangeFieldsVersion, sysLogFields:syslogFields\    |
|           |         |    Version, thresholdCrossingAlertFields:threshold\   |
|           |         |    CrossingFieldsVersion                              |
|           |         |                                                       |
|           |         | -  stateChangeFields: made stateInterface mandatory   |
|           |         |                                                       |
|           |         | -  changed 'enum' to 'enumeration' throughout section |
|           |         |    4 of the document (note: this can't be done in the |
|           |         |    JSON schema).                                      |
|           |         |                                                       |
|           |         | -  measurementsForVfScalingFields: made the following |
|           |         |    fields optional: conurrentSessions, configured\    |
|           |         |    Entitites, cpuUsageArray, fileSystemUsageArray,    |
|           |         |    memoryConfigured, memoryUsed, requestRate,         |
|           |         |    vNicUsageArray                                     |
|           |         |                                                       |
|           |         | -  measurementsForVfScalingFields: concurrentSessions |
|           |         |    and configuredEntities: changed the description to |
|           |         |    support both VMs and VNFs                          |
|           |         |                                                       |
|           |         | -  measurementsFor VfScalingFields: clarified the     |
|           |         |    descriptions of latencyDistribution, measurement\  |
|           |         |    Inverval and requestRate                           |
|           |         |                                                       |
|           |         | -  syslogFields: clarified the descriptions of        |
|           |         |    syslogSData, syslogTag, syslogVer                  |
|           |         |                                                       |
|           |         | -  thresholdCrossingAlertFields: made the following   |
|           |         |    fields optional and clarified their descriptions:  |
|           |         |    elementType, networkService                        |
|           |         |                                                       |
|           |         | -  command and commandList: created a list of command |
|           |         |    structures to enable the event collector to request|
|           |         |    changes of event sources. Commands consist of a    |
|           |         |    commandType along with optional fields (whose      |
|           |         |    presence is indicated by the commandType). Three   |
|           |         |    command types are currently supported:             |
|           |         |    'measurementIntevalChange',                        |
|           |         |    ‘provideThrottlingState’ and                       |
|           |         |    'throttlingSpecification'.                         |
|           |         |                                                       |
|           |         | -  eventDomainThrottleSpecificationList: removed this |
|           |         |    and replaced it with commandList.                  |
|           |         |                                                       |
|           |         | -  Operations and Sample Requests: modified the       |
|           |         |    operations and samples to support the new command  |
|           |         |    and commandList structures.                        |
+-----------+---------+-------------------------------------------------------+
| 9/1/2016  | v2.10   | -  measurementsForVfScaling block: made the following |
|           |         |    fields optional: latencyDistribution (which is an  |
|           |         |    array of latencyBucketMeasure structures) and      |
|           |         |    meanRequestLatency. Updated the JSON schemas (now  |
|           |         |    v24) to match.                                     |
+-----------+---------+-------------------------------------------------------+
| 9/16/2016 | v2.11   | -  1 Introduction: updated the introduction to clarify|
|           |         |    the usage of eventTypes and the possibility of     |
|           |         |    support for other protocols.                       |
|           |         |                                                       |
|           |         | -  6.1 REST Operation Overview: added two new         |
|           |         |    subsections (6.1.2 and 6.1.3) discussing Api       |
|           |         |    Version and Commands Toward Event Source Clients.  |
|           |         |                                                       |
|           |         | -  6.2 publishAnyEvent: fixed the sample to conform to|
|           |         |    the latest changes                                 |
|           |         |                                                       |
|           |         | -  6.3 publishSpecificTopic: fixed the sample to      |
|           |         |    conform to the latest changes                      |
|           |         |                                                       |
|           |         | -  6.4 publishEventBatch: fixed the sample to conform |
|           |         |    to the latest changes                              |
|           |         |                                                       |
|           |         | -  6.5 provideThrottlingState operation: added the    |
|           |         |    Input Parameters section heading back and fixed the|
|           |         |    sample request to provide eventThrottlingState     |
|           |         |    (instead of eventThrottlingClientState).           |
|           |         |                                                       |
|           |         | -  The remaining bullets describe changes made to     |
|           |         |    section 4 datatypes in alphabetical order:         |
|           |         |                                                       |
|           |         | -  command datatype: referenced the new section 6.1.3 |
|           |         |    which provides an explanation of command state     |
|           |         |    expectations and requirements for a given          |
|           |         |    eventSource:                                       |
|           |         |                                                       |
|           |         | -  commonEventHeader datatype:                        |
|           |         |                                                       |
|           |         |    -  made sourceId and reportingEntityId fields      |
|           |         |       optional (although the internal Generic Event   |
|           |         |       Listener spec indicates, in the field           |
|           |         |       descriptions, that the AT&T enrichment process  |
|           |         |       shall ensure that these fields are populated)   |
|           |         |                                                       |
|           |         |    -  domain enumeration: changed measurementsForVf\  |
|           |         |       ScalingFields to measurementsForVfScaling       |
|           |         |                                                       |
|           |         | -  eventDomainThrottleSpecificationList: added this   |
|           |         |    array of eventDomainThrottleSpecification stuctures|
|           |         |    back to the schema because it is used by the       |
|           |         |    provideThrottlingState operation.                  |
|           |         |                                                       |
|           |         | -  eventList: added eventList back to the vendor      |
|           |         |    version of the commonEventFormat. This is used by  |
|           |         |    the publishEventBatch operation.                   |
|           |         |                                                       |
|           |         | -  faultFields datatype:                              |
|           |         |                                                       |
|           |         |    -  eventSourceType: made this a string (and        |
|           |         |       provided the previous enumerated values as      |
|           |         |       examples)                                       |
|           |         |                                                       |
|           |         | -  filesystemUsage datatype:                          |
|           |         |                                                       |
|           |         |    -  changed vmIdentifier to filesystemName          |
|           |         |                                                       |
|           |         | -  gtpPerFlowMetrics datatype:                        |
|           |         |                                                       |
|           |         |    -  flowActivationTime: changed the format and      |
|           |         |       description to be compliant with RFC 2822.      |
|           |         |                                                       |
|           |         |    -  flowDeactivationTime: changed the format and    |
|           |         |       description to be compliant with RFC 2822.      |
|           |         |                                                       |
|           |         | -  internalHeaderFields datatype:                     |
|           |         |                                                       |
|           |         |    -  Added the following optional fields: firstDate\ |
|           |         |       Time, lastDateTime compliant with RFC 2822.     |
|           |         |       Noted in the description that these fields must |
|           |         |       be supplied for events in the following domains:|
|           |         |       fault, thresholdCrossingAlerts and              |
|           |         |       measurementsForVfScaling.                       |
|           |         |                                                       |
|           |         |    -  ticketingTimestamp: changed the format and      |
|           |         |       description to be compliant with RFC 2822.      |
|           |         |                                                       |
|           |         | -  syslogFields datatype:                             |
|           |         |                                                       |
|           |         |    -  eventSourceType: made this a string (and        |
|           |         |       provided the previous enumerated values, without|
|           |         |       the numbers, as examples)                       |
|           |         |                                                       |
|           |         | -  thresholdCrossingAlerts dataypte:                  |
|           |         |                                                       |
|           |         |    -  collectionTimestamp: changed the format and     |
|           |         |       description to be compliant with RFC 2822.      |
|           |         |                                                       |
|           |         |    -  eventStartTimestamp: changed the format and     |
|           |         |       description to be compliant with RFC 2822.      |
|           |         |                                                       |
|           |         |    -  added the same eventSeverity field as from the  |
|           |         |       faultFields and made it required                |
+-----------+---------+-------------------------------------------------------+
| 9/23/2016 | v2.12   | -  Section 4 Datatypes: commonEventHeader: made       |
|           |         |    reportingEntityName a required field (note: the    |
|           |         |    JSON schema already had this field as required)    |
+-----------+---------+-------------------------------------------------------+
| 11/29/2016| v3.0    | -  Introduction:                                      |
|           |         |                                                       |
|           |         |    -  Introductory paragraph: changed '...Common Event|
|           |         |       Header Block followed by zero or more event     |
|           |         |       domain blocks' to '...Common Event Header Block |
|           |         |       accompanied by zero or more event domain blocks'|
|           |         |       since the order of the blocks on the wire is    |
|           |         |       not guaranteed.                                 |
|           |         |                                                       |
|           |         |    -  Added Section 1.5 Versioning                    |
|           |         |                                                       |
|           |         | -  Section 4: codec processing:                       |
|           |         |                                                       |
|           |         |    -  CommonEventFormat\_Vendors schema only:         |
|           |         |       codesInUse: changed required field from         |
|           |         |       "codecUtilization" which was removed previously |
|           |         |       to "numberInUse" which is the new field name.   |
|           |         |                                                       |
|           |         |    -  added ‘codecSelected’ datatype                  |
|           |         |                                                       |
|           |         |    -  added ‘codecSelectedTranscoding’ datatype       |
|           |         |                                                       |
|           |         | -  Section 4 and section 6: command processing:       |
|           |         |                                                       |
|           |         |    -  Added commandListEntry which is an object that  |
|           |         |       references the command object.                  |
|           |         |                                                       |
|           |         |    -  commandList: changed commandList to contain an  |
|           |         |       array of commandListEntry objects.              |
|           |         |                                                       |
|           |         |    -  Updated sample responses in section 6 where     |
|           |         |       commands are used                               |
|           |         |                                                       |
|           |         | -  Section 4: commonEventHeader:                      |
|           |         |                                                       |
|           |         |    -  Incremented version to 1.2                      |
|           |         |                                                       |
|           |         |    -  added two new values to the ‘domain’            |
|           |         |       enumeration: ‘serviceEvents’ and ‘signaling     |
|           |         |                                                       |
|           |         | -  Section 4: added endOfCallVqmSummaries datatype    |
|           |         |                                                       |
|           |         | -  Section 4: ‘event’: added two fields:              |
|           |         |    ‘serviceEventsFields’ and ‘signalingFields’        |
|           |         |                                                       |
|           |         | -  Section 4: added ‘eventInstanceIdentifier’datatype |
|           |         |                                                       |
|           |         | -  Section 4: CommonEventListener only:               |
|           |         |    internalHeaderFields:                              |
|           |         |                                                       |
|           |         |    -  added ‘internalHeaderFieldsVersion’(initially   |
|           |         |       set to 1.1)                                     |
|           |         |                                                       |
|           |         |    -  added ‘correlationFirstEpoch’                   |
|           |         |                                                       |
|           |         |    -  added 'closedLoopControlName'                   |
|           |         |                                                       |
|           |         |    -  added 'closedLoopFlag'                          |
|           |         |                                                       |
|           |         |    -  added 'collectorTimeStamp'                      |
|           |         |                                                       |
|           |         |    -  added 'eventTag'                                |
|           |         |                                                       |
|           |         |    -  added ‘tenantName’                              |
|           |         |                                                       |
|           |         |    -  changed 'operationalStatus' to 'inMaint'        |
|           |         |                                                       |
|           |         |    -  added required fields in the schema to match the|
|           |         |       word doc: 'equipmentNameCode', 'equipmentType', |
|           |         |       'equipmentVendor', 'inMaint', 'provStatus'      |
|           |         |                                                       |
|           |         | -  Section 4: added ‘marker’datatype                  |
|           |         |                                                       |
|           |         | -  Section 4: added ‘midCallRtcp’ datatype            |
|           |         |                                                       |
|           |         | -  Section 4: mobileFlowFields:                       |
|           |         |                                                       |
|           |         |    -  added ‘mobileFlowFieldsVersion’(initially set to|
|           |         |       1.1)                                            |
|           |         |                                                       |
|           |         | -  Section 4: added ‘serviceEventsFields’datatype     |
|           |         |                                                       |
|           |         | -  Section 4: added ‘signalingFields’ datatype        |
|           |         |                                                       |
|           |         | -  Section 4: syslogFields:                           |
|           |         |                                                       |
|           |         |    -  Incremented syslogFieldsVersion to 1.2          |
|           |         |                                                       |
|           |         |    -  added 'syslogPri'                               |
|           |         |                                                       |
|           |         |    -  added 'syslogSev'                               |
|           |         |                                                       |
|           |         |    -  added ‘syslogSdId’                              |
|           |         |                                                       |
|           |         | -  Section 4: thresholdCrossingAlertFields:           |
|           |         |                                                       |
|           |         |    -  Incremented thresholdCrossingFieldsVersion to   |
|           |         |       1.2                                             |
|           |         |                                                       |
|           |         |    -  added 'additionalFields' which is an optional   |
|           |         |       list of name value pairs.                       |
|           |         |                                                       |
|           |         | -  Section 4: schema v26.0 embedded reflecting the    |
|           |         |    above changes.                                     |
|           |         |                                                       |
|           |         | -  Section 6 and Section 2: changed all sample        |
|           |         |    requests to use /v3 in the REST Resource URL.      |
+-----------+---------+-------------------------------------------------------+
| 12/1/2016 | v3.1    | -  Section 6: Updated the call flow diagrams to show  |
|           |         |    ‘v3’                                               |
+-----------+---------+-------------------------------------------------------+
| 1/5/2017  | v4.0    | -  Combined the Generic Event Listener and Vendor     |
|           |         |    Event Listener into a single API service           |
|           |         |    specification with version 4.0.                    |
|           |         |                                                       |
|           |         | -  Changed the title to VES (Virtual Function Event   |
|           |         |    Streaming) Listener.                               |
|           |         |                                                       |
|           |         | -  Changed references to 'generic event' to 'common   |
|           |         |    event' or 'VES event' (depending on the context)   |
|           |         |    throughout the document.                           |
|           |         |                                                       |
|           |         | -  Used the Legal Disclaimer from the Vendor Event    |
|           |         |    Listener on the back of the title page.            |
|           |         |                                                       |
|           |         | -  Section 1: Introduction changes:                   |
|           |         |                                                       |
|           |         |    -  modified wording to reference 'VES'             |
|           |         |                                                       |
|           |         |    -  removed the 'Audience' section, which described |
|           |         |       various AT&T groups the documented was intended |
|           |         |       for                                             |
|           |         |                                                       |
|           |         |    -  tweaked the naming standards for event types to |
|           |         |       clarify the purpose of the naming conventions   |
|           |         |                                                       |
|           |         | -  Section 3: Resource Structure: added a sentence    |
|           |         |    describing the FQDN and port used in the resource  |
|           |         |    URL.                                               |
|           |         |                                                       |
|           |         | -  Section 4: Common Event Format changes:            |
|           |         |                                                       |
|           |         |    -  renamed the section to 'Common Event Format'    |
|           |         |       from 'Generic Event Format'                     |
|           |         |                                                       |
|           |         |    -  reorganized the datatypes into separate sections|
|           |         |       ; sections were defined for each of the domains |
|           |         |       as well as for common event, common event header|
|           |         |       and command list processing                     |
|           |         |                                                       |
|           |         |    -  codecSelected datatype: removed this datatype   |
|           |         |                                                       |
|           |         |    -  codecSelectedTranscoding datatype: removed this |
|           |         |       datatype                                        |
|           |         |                                                       |
|           |         |    -  command datatype: added an enumerated value to  |
|           |         |       commandType: 'heartbeatIntervalChange'          |
|           |         |                                                       |
|           |         |    -  commonEventHeader: added internalHeaderFields to|
|           |         |       the commonEventHeader, defined as "Fields (not  |
|           |         |       supplied by event sources) that the VES Event   |
|           |         |       Listener service can use to enrich the event if |
|           |         |       needed for efficient internal processing. This  |
|           |         |       is an empty object which is intended to be      |
|           |         |       defined separately by each provider implementing|
|           |         |       the VES Event Listener."                        |
|           |         |                                                       |
|           |         |    -  commonEventHeader: removed two enumerated values|
|           |         |       , 'serviceEvents' and 'signaling' from the      |
|           |         |       domain enumeration                              |
|           |         |                                                       |
|           |         |    -  commonEventHeader version: incremented the      |
|           |         |       version to 2.0                                  |
|           |         |                                                       |
|           |         |    -  endOfCallVqmSummaries datatype: removed this    |
|           |         |       datatype                                        |
|           |         |                                                       |
|           |         |    -  event: changed the description of the event     |
|           |         |       datatype to: "fields which constitute the ‘root |
|           |         |       level’ of the common event format"              |
|           |         |                                                       |
|           |         |    -  event: removed 'serviceEventFields' and         |
|           |         |       'signalingFields' from the definition           |
|           |         |                                                       |
|           |         |    -  event: fixed a misspelling of                   |
|           |         |       ‘thresholdCrossingAlertFields’, which was only  |
|           |         |       present in the Word document                    |
|           |         |                                                       |
|           |         |    -  eventInstanceIdentifier datatype: removed this  |
|           |         |       datatype                                        |
|           |         |                                                       |
|           |         |    -  internalHeaderFIelds datatype: defined this as  |
|           |         |       follows: "The internalHeaderFields datatype is  |
|           |         |       an undefined object which can contain           |
|           |         |       arbitrarily complex JSON structures. It is      |
|           |         |       intended to be defined separately by each       |
|           |         |       provider implementing the VES Event Listener.   |
|           |         |       The fields in internalHeaderFields are not      |
|           |         |       provided by any event source but instead are    |
|           |         |       added by the VES Event Listener service itself  |
|           |         |       as part of an event enrichment process necessary|
|           |         |       for efficient internal processing of events     |
|           |         |       received by the VES Event Listener"             |
|           |         |                                                       |
|           |         |    -  marker datatype: removed this datatype          |
|           |         |                                                       |
|           |         |    -  measurementsForVfScalingFields datatype:        |
|           |         |       clarified that memoryConfigured and memoryUsed  |
|           |         |       are measured in MB                              |
|           |         |                                                       |
|           |         |    -  midCallRtcp datatype: removed this datatype     |
|           |         |                                                       |
|           |         |    -  mobileFlowFields datatype: added                |
|           |         |       ‘additionalFields’                              |
|           |         |                                                       |
|           |         |    -  mobileFlowFields datatype: incremented the      |
|           |         |       version number for this field block to 1.2      |
|           |         |                                                       |
|           |         |    -  serviceEventsFields datatype: removed this      |
|           |         |       datatype                                        |
|           |         |                                                       |
|           |         |    -  signalingFields datatype: removed this datatype |
|           |         |                                                       |
|           |         |    -  syslogFields: added three fields to the schema  |
|           |         |       that were previously described in the document  |
|           |         |       but not incorporated into the schema: syslogPri,|
|           |         |       syslogSev, syslogSdId                           |
|           |         |                                                       |
|           |         |    -  syslogFields version: incremented the version to|
|           |         |       2.0                                             |
|           |         |                                                       |
|           |         | -  Modified the Common Event Format JSON schema to    |
|           |         |    v27.0 to incorporate the above changes. Also, added|
|           |         |    the AT&T Copyright Notice from the top of the      |
|           |         |    retired CommonEventFormat\_Vendors schema.         |
|           |         |                                                       |
|           |         | -  Section 6 and 2: changed all sample requests to use|
|           |         |    /v4 in the REST Resource URL and call flow diagrams|
|           |         |                                                       |
|           |         | -  Section 6.1.3: added a row to the table in this    |
|           |         |    section describing the ‘heartbeatIntervalChange’   |
|           |         |    command.                                           |
|           |         |                                                       |
|           |         | -  Section 6.1.4: added this new section describing   |
|           |         |    expectations for buffering of events should all    |
|           |         |    REST resource URL FQDNs be unreachable.            |
|           |         |                                                       |
|           |         | -  Section 6 Sample Requests: modified all sample     |
|           |         |    requests showing the return of a commandList toward|
|           |         |    the event source to incorporate a                  |
|           |         |    heartbeatIntervalChange command; also corrected the|
|           |         |    spelling in the samples for the                    |
|           |         |    measurementIntervalChange command.                 |
|           |         |                                                       |
|           |         | -  Section 7: Contributors: removed this section      |
+-----------+---------+-------------------------------------------------------+
| 3/21/2017 | v4.1    | -  JSON Schema changes to produce v27.2 (note: an     |
|           |         |    earlier draft version of v27.1 had been distributed|
|           |         |    to a few individuals):                             |
|           |         |                                                       |
|           |         |    -  To support use of the schema with event batches,|
|           |         |       removed the following statement near the end of |
|           |         |       the schema file:                                |
|           |         |                                                       |
|           |         |     "required": [ "event" ]                           |
|           |         |                                                       |
|           |         | -  Fixed the characters used in some of the quotes    |
|           |         |                                                       |
|           |         | -  Fixed some typos in the descriptions.              |
|           |         |                                                       |
|           |         | -  Removed the booleans, which were non-essential and |
|           |         |    which were causing problems across different       |
|           |         |    implementations.                                   |
|           |         |                                                       |
|           |         | -  Section 4.5.7 measurementsForVfScalingFields:      |
|           |         |                                                       |
|           |         |    -  Fixed the spelling of measurementsForVf\        |
|           |         |       ScalingFields in the Word document              |
|           |         |                                                       |
|           |         | -  Section 2 and 6 sample requests and responses:     |
|           |         |                                                       |
|           |         |    -  Removed quotes from numbers: sequence, and      |
|           |         |       first/lastEpochMicrosec.                        |
|           |         |                                                       |
|           |         |    -  Fixed all quote characters, some of which were  |
|           |         |       using unusual symbols that wouldn’t validate    |
|           |         |       with the json-schema Python package.            |
|           |         |                                                       |
|           |         | -  Section 6.2.6.1, 6.3.6.1, 6.4.6.1 sample requests: |
|           |         |                                                       |
|           |         |    -  Added an alarmAdditionalInformation field array |
|           |         |       to the sample requests.                         |
|           |         |                                                       |
|           |         |    -  Added missing commas.                           |
|           |         |                                                       |
|           |         | -  Section 6.5.6.1 provideThrottlingState sample      |
|           |         |    requests:                                          |
|           |         |                                                       |
|           |         |    -  Fixed the eventDomainThrottleSpecificationList  |
|           |         |       to pass an array of anonymous eventDomain\      |
|           |         |       ThrottleSpecification objects.                  |
|           |         |                                                       |
|           |         |    -  Added missing quotes.                           |
|           |         |                                                       |
|           |         | -  Fixed the suppressedNvPairsList to pass an array of|
|           |         |    anonymous suppressedNvPairs objects.               |
+-----------+---------+-------------------------------------------------------+
| 4/14/2017 | v5.0    | -  Section 1 Introduction:                            |
|           |         |                                                       |
|           |         |    -  Clarified the Introduction (Section 1).         |
|           |         |                                                       |
|           |         |    -  Changed Section 1.1 title from ‘Terminology’ to |
|           |         |       'Event Registration' and referenced the YAML    |
|           |         |       event registration format, defined in a separate|
|           |         |       document.                                       |
|           |         |                                                       |
|           |         |    -  Clarified naming standards for eventName.       |
|           |         |                                                       |
|           |         | -  Section 3: updated the REST resource structure     |
|           |         |                                                       |
|           |         | -  Section 4.1 command list processing datatypes:     |
|           |         |                                                       |
|           |         |    -  Got rid of commandListEntry and returned        |
|           |         |       commandList to a simple array of commands.      |
|           |         |                                                       |
|           |         |    -  Added heartbeatInterval to the command datatype.|
|           |         |                                                       |
|           |         |    -  Changed the datatype of measurementInterval from|
|           |         |       number to integer.                              |
|           |         |                                                       |
|           |         | -  Section 4.2 common event datatypes:                |
|           |         |                                                       |
|           |         |    -  event dataType: Added heartbeatFields,          |
|           |         |       sipSignalingFields and voiceQualityFields to the|
|           |         |       event datatype as optional field blocks         |
|           |         |                                                       |
|           |         |    -  Added jsonObject which provides a json object   |
|           |         |       schema, name and other meta-information along   |
|           |         |       with one or more object instances.              |
|           |         |                                                       |
|           |         |    -  Added jsonObjectInstance which provides         |
|           |         |       meta-information about an instance of a         |
|           |         |       jsonObject along with the actual object instance|
|           |         |                                                       |
|           |         |    -  Added the ‘key’ datatype                        |
|           |         |                                                       |
|           |         |    -  Added the namedArrayOfFields datatype           |
|           |         |                                                       |
|           |         |    -  Added vendorVnfNameFields                       |
|           |         |                                                       |
|           |         | -  Section 4.3 common event header fields:            |
|           |         |                                                       |
|           |         |    -  Add two new enumerations to domain:             |
|           |         |       ‘sipSignaling’ and ‘voiceQuality’               |
|           |         |                                                       |
|           |         |    -  Renamed eventType to eventName. Note that the   |
|           |         |       original usage of eventType was formally        |
|           |         |       described in the Introduction back on 2/11/2016 |
|           |         |       with v1.9.                                      |
|           |         |                                                       |
|           |         |    -  Made eventName a required field                 |
|           |         |                                                       |
|           |         |    -  Created a new field called eventType with a     |
|           |         |       meaning that is different than the old eventType|
|           |         |                                                       |
|           |         |    -  Removed functionalRole, which was replaced by   |
|           |         |       the following two fields.                       |
|           |         |                                                       |
|           |         |    -  Added nfNamingCode                              |
|           |         |                                                       |
|           |         |    -  Added nfcNamingCode                             |
|           |         |                                                       |
|           |         |    -  Changed version to 3.0 (major version change)   |
|           |         |       and made it a required field                    |
|           |         |                                                       |
|           |         | -  Section 4.4: faultFields:                          |
|           |         |                                                       |
|           |         |    -  added one optional field: eventCategory         |
|           |         |                                                       |
|           |         |    -  made faultFieldsVersion a required field        |
|           |         |                                                       |
|           |         |    -  changed faultFieldsVersion to 2.0 (major version|
|           |         |       change)                                         |
|           |         |                                                       |
|           |         |    -  fixed a typo on the spelling of alarmInterfaceA |
|           |         |                                                       |
|           |         |    -  clarified field descriptions                    |
|           |         |                                                       |
|           |         | -  Section 4.5: added heartbeatFields datatype which  |
|           |         |    can be used to communicate heartbeatInterval. Note:|
|           |         |    this change was previously made in v4.2            |
|           |         |                                                       |
|           |         | -  Section 4.6 measurements for vf scaling datatypes: |
|           |         |    changed the following datatypes from number to     |
|           |         |    integer:                                           |
|           |         |                                                       |
|           |         |    -  In measurementsForVfScalingFields:              |
|           |         |       concurrentSessions, configuredEntities,         |
|           |         |       numberOfMediaPortsInUse, vnfcScalingMetric      |
|           |         |                                                       |
|           |         |    -  In codecsInUse: numberInUse                     |
|           |         |                                                       |
|           |         |    -  In featuresInUse: featureUtilization            |
|           |         |                                                       |
|           |         | -  Section 4.6.2 modified cpuUsage                    |
|           |         |                                                       |
|           |         | -  Section 4.6.3 added diskUsage                      |
|           |         |                                                       |
|           |         | -  Section 4.6.7 measurementsForVfScalingFields:      |
|           |         |                                                       |
|           |         |    -  fixed the spelling of the measurementsForVf\    |
|           |         |       ScalingFields in the Word document              |
|           |         |                                                       |
|           |         |    -  added additionalFields, which is an array of    |
|           |         |       fields (i.e., name-value pairs)                 |
|           |         |                                                       |
|           |         |    -  changed additionalMeasurements to reference the |
|           |         |       common datatype namedArrayOfFields (instead of  |
|           |         |       referencing measurementGroup)                   |
|           |         |                                                       |
|           |         |    -  added additionalObjects which is an array of    |
|           |         |       jsonObjects described by name, keys and schema  |
|           |         |                                                       |
|           |         |    -  deleted aggregateCpuUsage                       |
|           |         |                                                       |
|           |         |    -  added diskUsageArray                            |
|           |         |                                                       |
|           |         |    -  deleted measurementGroup (which was replaced by |
|           |         |       the common datatype: namedArrayOfFields         |
|           |         |                                                       |
|           |         |    -  added memoryUsageArray                          |
|           |         |                                                       |
|           |         |    -  deleted memoryConfigured and memoryUsed         |
|           |         |                                                       |
|           |         |    -  deleted errors and vNicUsageArray               |
|           |         |                                                       |
|           |         |    -  added vNicPerformanceArray                      |
|           |         |                                                       |
|           |         |    -  changed the measurementsForVfScalingVersion to  |
|           |         |       2.0 (major version change) and made it a        |
|           |         |       required field. Also changed the name of this   |
|           |         |       version field in the Word document to match that|
|           |         |       in the JSON schema.                             |
|           |         |                                                       |
|           |         | -  Section 4.6.8 added memoryUsage                    |
|           |         |                                                       |
|           |         | -  Section 4.6.9 vNicPerformance: replaced vNicUsage  |
|           |         |    and errors with vNicPerformance                    |
|           |         |                                                       |
|           |         | -  Section 4.7 mobile flow fields changes:            |
|           |         |                                                       |
|           |         |    -  Made mobileFlowFieldsVersion a required field   |
|           |         |       and changed the mobileFlowFieldsVersion to 2.0  |
|           |         |       (major version change).                         |
|           |         |                                                       |
|           |         |    -  Changed the datatype of flowActivationTime and  |
|           |         |       flowDeactivationTime in the Word doc to string. |
|           |         |                                                       |
|           |         |    -  changed the following datatypes from number to  |
|           |         |       integer: otherEndpointPort,                     |
|           |         |       reportingEndpointPort, samplingAlgorithm        |
|           |         |                                                       |
|           |         | -  Section 4.8: otherFields:                          |
|           |         |                                                       |
|           |         |    -  Added otherFieldsVersion (set at 1.1)           |
|           |         |                                                       |
|           |         |    -  Added hashOfNameValuePairArrays                 |
|           |         |                                                       |
|           |         |    -  Added jsonObjects                               |
|           |         |                                                       |
|           |         |    -  Added nameValuePairs                            |
|           |         |                                                       |
|           |         | -  Section 4.9: added sipSignaling domain datatypes   |
|           |         |    with 4.8.1 sipSignalingFields. sipSignalingFields\ |
|           |         |    Version is set at 1.0                              |
|           |         |                                                       |
|           |         | -  Section 4.10 stateChangeFields: made stateChange\  |
|           |         |    FieldsVersion a required field and set it to 2.0   |
|           |         |    (major version change).                            |
|           |         |                                                       |
|           |         | -  Section 4.11 syslogFields:                         |
|           |         |                                                       |
|           |         |    -  Changed the following datatypes from number to  |
|           |         |       integer: syslogFacility, syslogPri              |
|           |         |                                                       |
|           |         |    -  Changed additionalFields from a field [ ] to a  |
|           |         |       string which takes name=value pairs delimited by|
|           |         |       a pipe symbol.                                  |
|           |         |                                                       |
|           |         |    -  Changed syslogFieldsVersion to 3.0 (major       |
|           |         |       version change) and made it a required field    |
|           |         |                                                       |
|           |         |    -  Made syslogSev an enumerated string (previously |
|           |         |       just a string)                                  |
|           |         |                                                       |
|           |         | -  Section 4.12 thresholdCrossingAlertFields: made    |
|           |         |    thresholdCrossingFieldsVersion a required field and|
|           |         |    set it to 2.0 (major version change).              |
|           |         |                                                       |
|           |         | -  Section 4.132: added voice quality domain datatypes|
|           |         |    with 4.13.1 endOfCallVqmSummaries and 4.13.2       |
|           |         |    voiceQualityFields. voiceQualityFieldsVersion is   |
|           |         |    set at 1.0                                         |
|           |         |                                                       |
|           |         | -  JSON Schema: changed the schema to v28.0 and       |
|           |         |    incorporated all of the changes above.             |
|           |         |                                                       |
|           |         | -  Additional JSON Schema changes that are part of    |
|           |         |    v28: Note: The following changes are provided      |
|           |         |    relative to API Spec v4.0 (which embedded JSON     |
|           |         |    schema v27.0), but they were also made in an       |
|           |         |    interim release v4.1 (which embedded JSON schema   |
|           |         |    v27.2):                                            |
|           |         |                                                       |
|           |         |    -  To support use of the schema with event batches,|
|           |         |       removed the following statement near the end of |
|           |         |       the schema file:                                |
|           |         |                                                       |
|           |         |     "required": [ "event" ]                           |
|           |         |                                                       |
|           |         | -  Fixed the characters used in some of the quotes    |
|           |         |                                                       |
|           |         | -  Fixed some typos in the descriptions.              |
|           |         |                                                       |
|           |         | -  Removed the booleans, which were non-essential and |
|           |         |    which were causing problems across different       |
|           |         |    implementations.                                   |
|           |         |                                                       |
|           |         | -  Section 2 and 6 sample requests and responses (also|
|           |         |    incorporated in interim release 4.1):              |
|           |         |                                                       |
|           |         |    -  Removed quotes from numbers: sequence, and      |
|           |         |       first/lastEpochMicrosec.                        |
|           |         |                                                       |
|           |         |    -  Fixed all quote characters, some of which were  |
|           |         |       using unusual symbols that wouldn’t validate    |
|           |         |       with the json-schema Python package.            |
|           |         |                                                       |
|           |         | -  Section 2 and 6 sample requests and responses (only|
|           |         |    in v5.0):                                          |
|           |         |                                                       |
|           |         |    -  Changed the version numbers in the URL string.  |
|           |         |                                                       |
|           |         |    -  Added nfNamingCode and nfcNamingCode and removed|
|           |         |       functionalRole                                  |
|           |         |                                                       |
|           |         | -  Section 6 call flows: updated the version number   |
|           |         |    (only in v5.0).                                    |
|           |         |                                                       |
|           |         | -  Section 6: removed the publishSpecificTopic        |
|           |         |    operation                                          |
|           |         |                                                       |
|           |         | -  Section 6.1.4: Buffering: clarified event source   |
|           |         |    expectations for buffering (only in v5.0).         |
|           |         |                                                       |
|           |         | -  Section 6.2.6.1, 6.3.6.1 sample requests (also     |
|           |         |    incorporated in interim release 4.1):              |
|           |         |                                                       |
|           |         |    -  Added an alarmAdditionalInformation field array |
|           |         |       to the sample requests.                         |
|           |         |                                                       |
|           |         |    -  Added missing commas.                           |
|           |         |                                                       |
|           |         | -  Section 6.2.6.3, 6.3.6.3 commandList sample        |
|           |         |    responses (only in v5.0):                          |
|           |         |                                                       |
|           |         |    -  Fixed the commandList sample responses to pass  |
|           |         |       an array of anonymous command objects (rather   |
|           |         |       than an array of commandListEntry objects).     |
|           |         |                                                       |
|           |         |    -  Fixed the heartbeatIntervalChange commandType to|
|           |         |       pass a heartbeatInterval value instead of a     |
|           |         |       measurementInterval value.                      |
|           |         |                                                       |
|           |         |    -  Removed quotes from the measurementInterval and |
|           |         |       heartbeatInterval values since they are numbers.|
|           |         |                                                       |
|           |         | -  Section 6.4.6.1 provideThrottlingState sample      |
|           |         |    requests(also incorporated in interim release 4.1):|
|           |         |                                                       |
|           |         |    -  Fixed the eventDomainThrottleSpecificationList  |
|           |         |       to pass an array of anonymous                   |
|           |         |       eventDomainThrottleSpecification objects.       |
|           |         |                                                       |
|           |         |    -  Added missing quotes.                           |
|           |         |                                                       |
|           |         |    -  Fixed the suppressedNvPairsList to pass an array|
|           |         |       of anonymous suppressedNvPairs objects (also    |
|           |         |       incorporated in interim release 4.1).           |
+-----------+---------+-------------------------------------------------------+
| 5/22/2017 | v5.1    | -  Footers: removed proprietary markings and updated  |
|           |         |    copyrights to 2017                                 |
|           |         |                                                       |
|           |         | -  Section 4.2.3: field:                              |
|           |         |                                                       |
|           |         |    -  Changed the API spec to make ‘name’ and ‘value’ |
|           |         |       start with lowercase letters. Note: this did not|
|           |         |       affect the schema, which already had them as    |
|           |         |       lowercase.                                      |
|           |         |                                                       |
|           |         | -  JSON Schema:                                       |
|           |         |                                                       |
|           |         |    -  measurementGroup: deleted this object since it  |
|           |         |       was replaced with ‘namedArrayOfFields’ in v28.0 |
|           |         |       and was no longer being used.                   |
|           |         |                                                       |
|           |         |    -  namedArrayOfFields: Fixed an error in the       |
|           |         |       specification of required fields: from          |
|           |         |       ‘measurements’ to ‘arrayOfFields’.              |
|           |         |                                                       |
|           |         | -  Changed the version of the JSON schema to 28.1     |
+-----------+---------+-------------------------------------------------------+
| 6/14/2017 | v5.2    | -  JSON Schema: created v28.2 by changing the field   |
|           |         |    descriptions in the memoryUsage object to refer to |
|           |         |    ‘kibibytes’ instead of ‘kilobytes’. There were no  |
|           |         |    changes to the 28.1 structure.                     |
|           |         |                                                       |
|           |         | -  Word Document: measurementsForVfScaling Domain:    |
|           |         |    memoryUsage object: changed the field descriptions |
|           |         |    in this object to refer to ‘kibibytes’ instead of  |
|           |         |    ‘kilobytes’. There were no changes to the          |
|           |         |    memoryUsage structure.                             |
|           |         |                                                       |
|           |         | -  Reorganized the Word document to group the data    |
|           |         |    structures in Section 4 into three broad categories|
|           |         |    to better align with the VNF Guidelines            |
|           |         |    documentation that has been prepared for vendors:  |
|           |         |                                                       |
|           |         |    -  Common Event Datatypes:                         |
|           |         |                                                       |
|           |         |       - Command List Processing Datatypes             |
|           |         |                                                       |
|           |         |       - Common Event Datatypes                        |
|           |         |                                                       |
|           |         |       - Common Event Header Datatypes                 |
|           |         |                                                       |
|           |         |    -  Technology Independent Datatypes:               |
|           |         |                                                       |
|           |         |       - ‘Fault Domain Datatypes                       |
|           |         |                                                       |
|           |         |       - ‘Heartbeat’ Domain Datatypes                  |
|           |         |                                                       |
|           |         |       - ‘Measurements For Vf Scaling’ Domain Datatypes|
|           |         |                                                       |
|           |         |       - ‘Other’ Domain Datatypes                      |
|           |         |                                                       |
|           |         |       - ‘State Change’ Domain Datatypes               |
|           |         |                                                       |
|           |         |       - ‘Syslog’ Domain Datatypes                     |
|           |         |                                                       |
|           |         |       - ‘Threshold Crossing Alert’ Domain Datatypes   |
|           |         |                                                       |
|           |         |    -  Technology Specify Datatypes:                   |
|           |         |                                                       |
|           |         |       - ‘Mobile Flow’ Domain Datatypes                |
|           |         |                                                       |
|           |         |       - ‘Sip Signaling’ Domain Datatypes              |
|           |         |                                                       |
|           |         |       - ‘Voice Quality’ Domain Datatypes              |
|           |         |                                                       |
|           |         | -  Section 6.1.3: Commands Toward Event Source        |
|           |         |    Clients: Added a statement: "Note: Vendors are not |
|           |         |    currently required to implement support for command|
|           |         |    processing; in addition, command processing may be |
|           |         |    supported by an App-C interface in future."        |
+-----------+---------+-------------------------------------------------------+
| 6/22/2017 | v5.3    | -  JSON Schema: created v28.3 by correcting an error  |
|           |         |    in the sipSignalingFields: changed                 |
|           |         |    vnfVendorNameFields to vendorVnfNameFields.        |
|           |         |    Embedded the new schema at the top of section 4.   |
+-----------+---------+-------------------------------------------------------+
| 9/12/2017 | v5.4    | -  Note: There no changes to any data structures or   |
|           |         |    operations in this version.                        |
|           |         |                                                       |
|           |         | -  JSON Schema: created v28.4 embedded at the top of  |
|           |         |    section 4:                                         |
|           |         |                                                       |
|           |         |    -  Added a reference to eventList in the properties|
|           |         |       defined under the schema title. This enables the|
|           |         |       schema to correctly validate event batches in   |
|           |         |       addition to just events.                        |
|           |         |                                                       |
|           |         |    -  Moved the schema title to the top of the schema |
|           |         |       and changed the text from "Event Listener" to   |
|           |         |       "VES Event Listener"                            |
|           |         |                                                       |
|           |         |    -  Added a schema header block under the title to  |
|           |         |       clearly communicate the schema version,         |
|           |         |       associated API and last-modified information    |
|           |         |                                                       |
|           |         | -  Changed the date in the copyright notice to 2017   |
+-----------+---------+-------------------------------------------------------+
| 9/19/2017 | v5.4.1  | -  Note: There no changes to any data structures or   |
|           |         |    operations in this version.                        |
|           |         |                                                       |
|           |         | -  Back of Cover Page: updated the license and        |
|           |         |    copyright notice to comply with ONAP guidelines    |
|           |         |                                                       |
|           |         | -  JSON Schema: updated the JSON schema to v28.4.1:   |
|           |         |    updated the copyright notice and license to comply |
|           |         |    with ONAP guidelines                               |
+-----------+---------+-------------------------------------------------------+
| 6/28/2018 | v6.0    | -  Added contributors to the title page.              |
|           |         |                                                       |
|           |         | -  Updated references to ‘vnf’ ‘vnfc’ to either ‘nf’  |
|           |         |    and ‘nfc’ or ‘xNf’ and ‘xNfc’ to generalize support|
|           |         |    across both vnfs and pnfs.                         |
|           |         |                                                       |
|           |         | -  Section 1:                                         |
|           |         |                                                       |
|           |         |    -  clarified the meaning of the VES acronym        |
|           |         |                                                       |
|           |         |    -  changed references from ASDC to SDC and from MSO|
|           |         |       to SO                                           |
|           |         |                                                       |
|           |         |    -  clarified the requirements for eventNames.      |
|           |         |                                                       |
|           |         |    -  Added a section of EventId use case examples    |
|           |         |                                                       |
|           |         |    -  Added a new section on measurement expansion    |
|           |         |       fields                                          |
|           |         |                                                       |
|           |         |    -  Added a new section of syslogs                  |
|           |         |                                                       |
|           |         |    -  clarified the versioning section and referenced |
|           |         |       the new API Versioning section in section 6.    |
|           |         |                                                       |
|           |         |    -  Added a list of all the latest field block      |
|           |         |       version numbers in this version of the API spec.|
|           |         |                                                       |
|           |         | -  Section 2: updated the sample to show use of new   |
|           |         |    HTTP versioning headers. Added a note indicating   |
|           |         |    that support for mutual SSL would be provided in   |
|           |         |    future.                                            |
|           |         |                                                       |
|           |         | -  Section 3: updated the resource structure remove   |
|           |         |    the clientThrottlingState resource.                |
|           |         |                                                       |
|           |         | -  Section 4: hashMaps. Changed all name-value pair   |
|           |         |    structures to hashMaps causing the following data  |
|           |         |    model and JSON schema (to v29.0) changes:          |
|           |         |                                                       |
|           |         |    -  4.1.1: Common Event Datatypes:                  |
|           |         |                                                       |
|           |         |       -  removed "field" and added "hashMap"          |
|           |         |                                                       |
|           |         |       -  removed "namedArrayOfFields" and added       |
|           |         |          "namedHashMap"                               |
|           |         |                                                       |
|           |         |       -  added arrayOfNamedHashMap                    |
|           |         |                                                       |
|           |         |       -  added arrayOfJsonObject                      |
|           |         |                                                       |
|           |         |    -  4.2.1: Fault Domain Datatypes:                  |
|           |         |                                                       |
|           |         |       -  changed the faultFields version to 3.0 (major|
|           |         |          change)                                      |
|           |         |                                                       |
|           |         |       -  changed faultFields.alarmAdditional\         |
|           |         |          Information to reference a hashMap           |
|           |         |                                                       |
|           |         |    -  4.2.2: Heartbeat Domain Datatypes:              |
|           |         |                                                       |
|           |         |       -  changed the heartbeatFieldsVersion to 2.0    |
|           |         |          (major change)                               |
|           |         |                                                       |
|           |         |       -  changed heartbeatFields.additionalFields to  |
|           |         |          reference a hashMap                          |
|           |         |                                                       |
|           |         |    -  4.2.3: Measurement Domain Datatypes:            |
|           |         |                                                       |
|           |         |       -  changed the measurementFieldsVersion to 3.0  |
|           |         |          (major change)                               |
|           |         |                                                       |
|           |         |       -  changed measurementFields.additionalFields to|
|           |         |          reference a hashMap                          |
|           |         |                                                       |
|           |         |       -  changed measurement.additionalMesurements to |
|           |         |          reference a namedHashMap [ ]                 |
|           |         |                                                       |
|           |         |       -  modified measurementFields.featureUsageArray |
|           |         |          to reference a hashmap and removed           |
|           |         |          ‘featuresInUse’                              |
|           |         |                                                       |
|           |         |       -  added the following datatypes which are now  |
|           |         |          referenced as items in arrays within         |
|           |         |          measurementFields: hugePages, load,          |
|           |         |          machineCheckException, processStats          |
|           |         |                                                       |
|           |         |    -  4.2.5: Other Domain Datatypes:                  |
|           |         |                                                       |
|           |         |       -  Change the otherFieldsVersion to 2.0 (major  |
|           |         |          change)                                      |
|           |         |                                                       |
|           |         |       -  changed otherFields.nameValuePairs to        |
|           |         |          reference a hashMap and renamed it hashMap   |
|           |         |                                                       |
|           |         |       -  changed otherFields.hashOfNameValuePair\     |
|           |         |          Arrrays to reference a namedHashMap and      |
|           |         |          renamed it arrayOfNamedHashMap               |
|           |         |                                                       |
|           |         |    -  4.2.7: State Change Domain Datatypes:           |
|           |         |                                                       |
|           |         |       -  changed the stateChangeFiledsVersion to 3.0  |
|           |         |          (major change)                               |
|           |         |                                                       |
|           |         |       -  changed stateChangeFields.additionalFields to|
|           |         |          reference a hashMap                          |
|           |         |                                                       |
|           |         |    -  4.2.9: Threshold Crossing Alert Domain          |
|           |         |       Datatypes:                                      |
|           |         |                                                       |
|           |         |       -  changed the thresholdCrossingAlertFields\    |
|           |         |          Version to 3.0 (major change)                |
|           |         |                                                       |
|           |         |       -  changed thresholdCrossingAlert\              |
|           |         |          Fields.additionalFields to reference a       |
|           |         |          hashMap                                      |
|           |         |                                                       |
|           |         |       -  counter: removed name and value elements and |
|           |         |          replaced with a hashMap                      |
|           |         |                                                       |
|           |         |    -  4.3.1: Mobile Flow Domain Datatypes:            |
|           |         |                                                       |
|           |         |       -  changed the mobileFlowFieldsVersion to 3.0   |
|           |         |          (major change)                               |
|           |         |                                                       |
|           |         |       -  changed mobileFlowFields.additionalFields to |
|           |         |          reference a hashMap                          |
|           |         |                                                       |
|           |         |       -  gtpPerFlowMetrics: modified ipTosCountList to|
|           |         |          reference hashmap                            |
|           |         |                                                       |
|           |         |       -  gtpPerFlowMetrics: modified mobileQciCos\    |
|           |         |          CountList to reference hashmap               |
|           |         |                                                       |
|           |         |       -  gtpPerFlowMetrics: modified tcpFlagCountList |
|           |         |          to reference hashmap                         |
|           |         |                                                       |
|           |         |    -  4.3.2: Sip Signaling Domain Datatypes:          |
|           |         |                                                       |
|           |         |       -  changed the sigSignalingFieldsVersion to 2.0 |
|           |         |          (major change)                               |
|           |         |                                                       |
|           |         |       -  changed sipSignalingFields.additional\       |
|           |         |          Information to reference a hashMap           |
|           |         |                                                       |
|           |         |    -  4.3.3: Voice Quality Domain Datatypes:          |
|           |         |                                                       |
|           |         |       -  change the voiceQualityFieldsVersion to 2.0  |
|           |         |          (major change)                               |
|           |         |                                                       |
|           |         |       -  changed voiceQualityFields.additional\       |
|           |         |          Information to reference a hashMap           |
|           |         |                                                       |
|           |         | -  Section 4: added notes at the top of section 4     |
|           |         |    clarifying expectations and requirements for       |
|           |         |    optional fields, extensible fields and keys sent   |
|           |         |    through extensible fields.                         |
|           |         |                                                       |
|           |         | -  Common Event Data Types: Section 4.1.1.9 Changed   |
|           |         |    vendorVnfNameFields to vendorNfNameFields; updated |
|           |         |    Section 4.3.2 SipSignaling and 4.3.3 Voice Quality |
|           |         |    to refer to the renamed object                     |
|           |         |                                                       |
|           |         | -  Common Event Header Section 4.1.2:                 |
|           |         |                                                       |
|           |         |    -  clarified the descriptions of eventId,          |
|           |         |       reportingEntityName, sourceName and             |
|           |         |       startEpochMicroseconds.                         |
|           |         |                                                       |
|           |         |    -  Added ‘notification’ and ‘pngRegistration’ to   |
|           |         |       the domain enumeration.                         |
|           |         |                                                       |
|           |         |    -  added a new timeZoneOffsest field               |
|           |         |                                                       |
|           |         | -  Fault Domain Section 4.2.1: clarified the          |
|           |         |    definitions of alarmCondition, eventSeverity and   |
|           |         |    specificProblem                                    |
|           |         |                                                       |
|           |         | -  Measurements Domain Section 4.2.3: changed the name|
|           |         |    of this domain from ‘measurementsForVfScaling’ to  |
|           |         |    ‘measurement’                                      |
|           |         |                                                       |
|           |         |    -  measurementsForVfScaling measurement            |
|           |         |                                                       |
|           |         |    -  measurementsForVfScalingFields measurementFields|
|           |         |                                                       |
|           |         |    -  measurementsForVfScalingVersion                 |
|           |         |       measurementFieldsVersion                        |
|           |         |                                                       |
|           |         |    -  the ‘mfvs’ abbreviation measurement             |
|           |         |                                                       |
|           |         | -  Measurements Domain Section 4.2.3 cpuUsage: added  |
|           |         |    seven optional fields to this structure:           |
|           |         |    cpuCapacityContention, cpuDemandAvg, cpuDemandMhz, |
|           |         |    cpuDemandPct, cpuLatencyAverage, cpuOverheadAvg,   |
|           |         |    cpuSwapWaitTime                                    |
|           |         |                                                       |
|           |         | -  Measurements Domain Section 4.2.3 diskUsage: added |
|           |         |    ten optional fields to this structure:             |
|           |         |    diskBusResets, diskCommandsAborted, diskCommandsAvg|
|           |         |    , diskFlushRequests, diskFlushTime,                |
|           |         |    diskReadCommandsAvg, diskTime, diskTotalRead\      |
|           |         |    LatencyAvg, diskTotalWriteLatencyAvg, diskWrite\   |
|           |         |    CommandsAvg                                        |
|           |         |                                                       |
|           |         | -  Measurements Domain Section 4.2.3: added a new     |
|           |         |    ‘ipmi’ datatype along with following ‘supporting’  |
|           |         |    datatypes: ipmiBaseboardTemperature, ipmiBaseboard\|
|           |         |    VoltageRegulator, ipmiBattery, ipmiFan, ipmiGlobal\|
|           |         |    AggregateTemperatureMargin, ipmiHsbp, ipmiNic,     |
|           |         |    ipmiPowerSupply, ipmiProcessor, processorDimm\     |
|           |         |    AggregateThermalMargin                             |
|           |         |                                                       |
|           |         | -  Measurements Domain Section 4.2.3: added a new     |
|           |         |    ‘load’ datatype                                    |
|           |         |                                                       |
|           |         | -  Measurements Domain Section 4.2.3 memoryUsage:     |
|           |         |    added eight optional fields to this structure:     |
|           |         |    memoryDemand, memoryLatencyAvg, memorySharedAvg,   |
|           |         |    memorySwapInAvg, memorySwapInRateAvg, memorySwap\  |
|           |         |    OutAvg, memorySwapOutRateAvg, memorySwapUsedAvg    |
|           |         |                                                       |
|           |         | -  Measurements Domain Section 4.2.3: modified        |
|           |         |    measurementFields to include the following new     |
|           |         |    fields: hugePagesArray, ipmi, loadArray, memory\   |
|           |         |    Errors, processStatusArray, rdtArray               |
|           |         |                                                       |
|           |         | -  Measurements Domain Section 4.2.3 renamed vNic\    |
|           |         |    Performance to nicPerformance and changed vNic\    |
|           |         |    Identifer to nicIdentifier                         |
|           |         |                                                       |
|           |         | -  Notification Domain Section 4.2.4: added           |
|           |         |    notificationFields to support a new notification   |
|           |         |    domain.                                            |
|           |         |                                                       |
|           |         | -  pnfRegistration Domain Section 4.2.7: added        |
|           |         |    pnfRegistrationFields to support a new registration|
|           |         |    domain.                                            |
|           |         |                                                       |
|           |         | -  sysLog Domain Section 4.2.8: added two new fields: |
|           |         |    syslogMsgHost and syslogTs. Clarified field        |
|           |         |    descriptions. Clarified syslogSData example.       |
|           |         |                                                       |
|           |         | -  endOfCallVqmSummaries Section 4.3.3.1:             |
|           |         |                                                       |
|           |         |    -  converted endpointJitter into two fields:       |
|           |         |       endpointAverageJitter and endpointMaxJitter     |
|           |         |                                                       |
|           |         |    -  converted localJitter into two fields:          |
|           |         |       localAverageJitter and localMaxJitter           |
|           |         |                                                       |
|           |         |    -  added two fields: localAverageJitterBufferDelay |
|           |         |       and localMaxJitterBufferDelay                   |
|           |         |                                                       |
|           |         |    -  added endpointRtpOctetsLost and                 |
|           |         |       endpointRtpPacketsLost                          |
|           |         |                                                       |
|           |         |    -  added localRtpOctetsLost and localRtpPacketsLost|
|           |         |                                                       |
|           |         |    -  converted packetsLost into oneWayDelay          |
|           |         |                                                       |
|           |         | -  API Versioning:                                    |
|           |         |                                                       |
|           |         |    -  Section 1.4: clarified the versioning section   |
|           |         |       and linked it to the following new section 6.1.2|
|           |         |                                                       |
|           |         |    -  Section 6.1.2: Added requirements for HTTP      |
|           |         |       headers communicating minor, patch and latest   |
|           |         |       version information.                            |
|           |         |                                                       |
|           |         |    -  Section 2 and 6 sample messages: clarified      |
|           |         |       examples to use the new HTTP headers            |
|           |         |                                                       |
|           |         | -  Section 6.1.4: Added a section specifying message  |
|           |         |    size limits.                                       |
|           |         |                                                       |
|           |         | -  Section2 6.2.6.1 and 6.3.6.1: corrected            |
|           |         |    additionalInformation examples to use hashMap      |
|           |         |    instead of name-value pair fields.                 |
|           |         |                                                       |
|           |         | -  Section 7: Added a section on Terminology.         |
|           |         |                                                       |
|           |         | -  Command List Processing: removed command list      |
|           |         |    processing from the document and schema:           |
|           |         |                                                       |
|           |         |    -  Modified the Section 3 resource structure to    |
|           |         |       align with these changes.                       |
|           |         |                                                       |
|           |         |    -  Removed Section 4 Datatypes: command,           |
|           |         |       commandList, eventDomainThrottleSpecification,  |
|           |         |       eventDomainThrottleSpecificationList,           |
|           |         |       eventThrottlingState, suppressedNvPairs         |
|           |         |                                                       |
|           |         |    -  Removed Section 6.1 description of commands     |
|           |         |       toward event source clients                     |
|           |         |                                                       |
|           |         | -  Removed Section 6.4 operation:                     |
|           |         |    provideThrottlingState                             |
+-----------+---------+-------------------------------------------------------+
| 7/30/2018 | v7.0    | -  General:                                           |
|           |         |                                                       |
|           |         |    -  Fixed typos throughout                          |
|           |         |                                                       |
|           |         |    -  Changed example versions to v7                  |
|           |         |                                                       |
|           |         | -  Section1:                                          |
|           |         |                                                       |
|           |         |    -  Clarified casing and use of dashes versus colons|
|           |         |       in eventName examples                           |
|           |         |                                                       |
|           |         |    -  Updated all field block versions                |
|           |         |                                                       |
|           |         | -  Section 2: added a note clarifying that TLS 1.2 or |
|           |         |    higher must be used for HTTPS connections.         |
|           |         |                                                       |
|           |         | -  Section 4 embedded schema changed to v30:          |
|           |         |                                                       |
|           |         |    -  Added " ‘additionalProperties’: false " to      |
|           |         |       objects to reject events that attempt to send   |
|           |         |       properties that are not listed in the           |
|           |         |       ‘properties’ keyword. Note: does not affect     |
|           |         |       hashmap extensible fields.                      |
|           |         |                                                       |
|           |         |    -  Changed all versions in all field blocks from   |
|           |         |       number to string enum with the version number   |
|           |         |       fixed by the enum so the schema can validate    |
|           |         |       events that attempt to send non-standard field  |
|           |         |       blocks.                                         |
|           |         |                                                       |
|           |         |    -  Changed syslog additionalFields to a hashMap    |
|           |         |                                                       |
|           |         | -  Section 4:                                         |
|           |         |                                                       |
|           |         |    -  Fixed section heading numbers that were the same|
|           |         |                                                       |
|           |         |    -  4.1.1: jsonObjectInstance: added an optional    |
|           |         |       recursive jsonObject and removed all required   |
|           |         |       fields from this object                         |
|           |         |                                                       |
|           |         |    -  4.1.2: commonEventHeader:                       |
|           |         |                                                       |
|           |         |       -  nfVendorName: added this optional field      |
|           |         |                                                       |
|           |         |       -  timeZoneOffset: changed from number to string|
|           |         |          with a particular format specified           |
|           |         |                                                       |
|           |         |       -  version was changed from number to string (as|
|           |         |          were all the version fields of all the field |
|           |         |          blocks)                                      |
|           |         |                                                       |
|           |         |       -  vesCommonEventListenerVersion: added this    |
|           |         |          required field as a string enumeration       |
|           |         |                                                       |
|           |         |    -  4.2.3: Measurements Domain:                     |
|           |         |                                                       |
|           |         |       -  Added a note clarifying that NFs are required|
|           |         |          to report exactly one Measurement event per  |
|           |         |          period per sourceName                        |
|           |         |                                                       |
|           |         |       -  diskUsage: added four new optional fields:   |
|           |         |          diskWeightedIoTimeAve, diskWeightedIoTimeLast|
|           |         |          , diskWeightedIoTimeMax,                     |
|           |         |          diskWeightedIoTimeMin                        |
|           |         |                                                       |
|           |         |       -  memoryUsage: add one new optional field:     |
|           |         |          percentMemoryUsage                           |
|           |         |                                                       |
|           |         |       -  nicPerformance: added nine new optional      |
|           |         |          fields: administrativeState, operationalState|
|           |         |          , receivedPercentDiscard,                    |
|           |         |          receivedPercentError, receivedUtilization,   |
|           |         |          speed, transmittedPercentDiscard,            |
|           |         |          transmittedPercentError,                     |
|           |         |          transmittedUtilization                       |
|           |         |                                                       |
|           |         |       -  processorDimmAggregateThermalMargin: make the|
|           |         |          thermalMargin field required                 |
|           |         |                                                       |
|           |         |    -  4.2.8: Syslog Domain:                           |
|           |         |                                                       |
|           |         | -  Corrected the example at the end of the section    |
+-----------+---------+-------------------------------------------------------+
| 7/31/2018 | v7.0.1  | -  Section 4: The schema embedded at the top of       |
|           |         |    section 4 was patched to correct a header field    |
|           |         |    name error—the schema version moves from 30 to     |
|           |         |    30.0.1:                                            |
|           |         |                                                       |
|           |         |    -  Changed commonEventHeader field: ‘vesCommon\    |
|           |         |       EventFormatVersion’ field to ‘vesEventListener\ |
|           |         |       Version’ and set the enum to 7.0.1              |
|           |         |                                                       |
|           |         |    -  Also changed the commonEventHeader ‘required’   |
|           |         |       array to reflect use the corrected field name:  |
|           |         |       ‘vesEventListenerVersion’                       |
|           |         |                                                       |
|           |         |    -  Changed the commonEventHeader ‘version’ field   |
|           |         |       enumeration to 4.0.1                            |
|           |         |                                                       |
|           |         | -  Section1:                                          |
|           |         |                                                       |
|           |         |    -  Changed the field block versions for the common |
|           |         |       header for ‘vesEventListenerVersion’ (to 7.0.1) |
|           |         |       and ‘version’ (to 4.0.1).                       |
|           |         |                                                       |
|           |         | -  Sections 2 and 6:                                  |
|           |         |                                                       |
|           |         |    -  Changed the commonEventHeader version fields    |
|           |         |       above, in the sample message requests and       |
|           |         |       responses; also updated the faultFieldsVersion  |
|           |         |       to 4.0                                          |
|           |         |                                                       |
|           |         | -  Section 6.1.2: Changed the X-LatestVersion to 7.0.1|
|           |         |    and the X-PatchVersion to 1                        |
+-----------+---------+-------------------------------------------------------+
| 12/10/2018| v7.1    | -  Section 1.2: Added Notification domain Perf3gpp    |
|           |         |    domain and changed a reference from ‘measurements  |
|           |         |    domain’ to ‘measurement domain’.                   |
|           |         |                                                       |
|           |         | -  Section 1.7.1: Field Block Versions: added         |
|           |         |    ‘perf3gppFields’ version at 1.0 and changed the    |
|           |         |    following version enumerations so that existing    |
|           |         |    clients of major version 7 would not be broken by  |
|           |         |    this VES minor version change, in accordance with  |
|           |         |    semantic versioning definitions:                   |
|           |         |                                                       |
|           |         |    -  commonEventHeader: changed to                   |
|           |         |       ‘vesEventListenerVersion’ enum to accept either |
|           |         |       7.0 or 7.0.1 or 7.1.                            |
|           |         |                                                       |
|           |         |    -  commonEventHeader: changed ‘version’ enum to    |
|           |         |       accept either 4.0 or 4.0.1 or 4.1               |
|           |         |                                                       |
|           |         | -  Section 2:                                         |
|           |         |                                                       |
|           |         |    -  changed sample request and responses to         |
|           |         |       reference 7.1 instead of 7.0.1 (and version 4.1 |
|           |         |       of the commonEventHeader version, instead of    |
|           |         |       v4.0.1)                                         |
|           |         |                                                       |
|           |         |    -  added a sub section on service provider support |
|           |         |       for mutual ssl certificate authentication       |
|           |         |                                                       |
|           |         | -  Section 4.1.2.1:                                   |
|           |         |                                                       |
|           |         |    -  CommonEventHeader timeZoneOffset changed        |
|           |         |       description from ‘UTC+/-hh.mm’ to ‘UTC+/-hh:mm’ |
|           |         |                                                       |
|           |         |    -  Added ‘perf3gpp’ to the domain enumeration      |
|           |         |                                                       |
|           |         | -  Section 4.2.3: Measurement Domain Datatypes:       |
|           |         |                                                       |
|           |         |    -  In ‘MeasurementFields’: Changed ‘ipmiArray’ to  |
|           |         |       ‘ipmi’ and made the type ‘object’               |
|           |         |                                                       |
|           |         |    -  ‘ipmiProcessor’: changed                        |
|           |         |       ‘pprocessorThermalControl’ to                   |
|           |         |       ‘processorThermalControl’                       |
|           |         |                                                       |
|           |         |    -  ‘machineCheckException’: changed                |
|           |         |       ‘processIdentifier’ to ‘vmIdentifier’           |
|           |         |                                                       |
|           |         | -  Section 4.2.6: added the perf3gpp domain           |
|           |         |                                                       |
|           |         | -  Section 4 embedded schema:                         |
|           |         |                                                       |
|           |         |    -  Changed the schema version from 30.0.1 to 30.1  |
|           |         |       as a result of the changes below:               |
|           |         |                                                       |
|           |         |    -  commonEventHeader: changed to                   |
|           |         |       ‘vesEventListenerVersion’ enum to accept either |
|           |         |       7.0, 7.0.1 or 7.1                               |
|           |         |                                                       |
|           |         |    -  commonEventHeader: changed the ‘version’ field  |
|           |         |       enumeration to accept either 4.0, 4.0.1 or 4.1  |
|           |         |                                                       |
|           |         |    -  commonEventHeader: changed the ‘domain’         |
|           |         |       enumeration to add support for the perf3gpp     |
|           |         |       domain.                                         |
|           |         |                                                       |
|           |         |    -  ‘event’: added a reference to ‘perf3gppFields’  |
|           |         |                                                       |
|           |         |    -  ‘hugePages’: changed the type of                |
|           |         |       hugePagesIdentifier from number to string       |
|           |         |                                                       |
|           |         |    -  ‘ipmiGlobalAggregateTemperatureMargin’: changed |
|           |         |       ‘pmiGlobalAggregateTemperatureMarginIdentifier’ |
|           |         |       to ‘globalAggregateTemperatureMarginIdentifier’ |
|           |         |                                                       |
|           |         |    -  ‘perf3gppFields’: added this object             |
|           |         |                                                       |
|           |         | -  Section 6: changed references throughout from      |
|           |         |    v7.0.1 to v7.1 and v4.0.1 (of the commonEventHeader|
|           |         |    version) to v4.1                                   |
|           |         |                                                       |
|           |         | -  Changed the location of the doc to VNF             |
|           |         |    Requirements and changed the formatting            |
+-----------+---------+-------------------------------------------------------+
| 1/28/2020 | v7.1.1  | -  Changed event sizes from 2Mb to 1Mb                |
|           |         | -  Configuration Requirement comments addressed       |
|           |         | -  Changed DCAE Collector to VES Event Listener       |
|           |         | -  Replaced VNF with NF where appropriate             |
|           |         | -  Updated publishAnyEvent and publishBatchEvent to   |
|           |         |    clarify both one way and mutual TLS are supported  |
|           |         | -  Changed authorization for publishEventBatch        |
|           |         |    because certification authorization is also        |
|           |         |    supported                                          |
|           |         | -  Updated fault use case in EventId Use Case         |
|           |         |    Examples based on Ericsson feedback                |
|           |         | -  Added new Configuration Requirements section       |
|           |         | -  Added new Event Domain Requirements section        |
|           |         | -  Updated security requirements based on agreements  |
|           |         |    in ONAP  Security Committee with details on 2-way  |
|           |         |    certificate support                                |
|           |         | -  Provided clarifications on event buffering         |
|           |         | -  Added Event Handling Requirements for              |
|           |         |    publishEventFlow                                   |
|           |         | -  Updated Field Block Versions to support existing   |
|           |         |    clients of major version 7                         |
|           |         | -  Updated sample request and response schemas        |
|           |         | -  Updated embedded schema as follows:                |
|           |         |                                                       |
|           |         |    * Changed schema version to 30.1.1                 |
|           |         |    * Changed measValues to measValuesList and similar |
|           |         |      changes throughout                               |
|           |         |    * Changed iMeasTypesList to sMeasTypesList         |
|           |         | - Corrected publishEventBatch call flow diagram       |
|           |         | - Changed AuthorizationHeader to Required? = NO for   |
|           |         |   publishAnyEvent operation                           |
|           |         | - Relaxed various requirements related to camel       |
|           |         |   casing of values from 'must' to 'should'            |
+-----------+---------+-------------------------------------------------------+
| 5/27/2020 | v7.2    | -  Re-organized sections to flow more logically       |
|           |         | -  Moved NF requirements to VNF Requirements          |
|           |         | -  Changed DCAE Collector to VES Event Listener       |
|           |         | -  Added StndDefined domain datatypes                 |
|           |         | -  Added eventCommonHeader field stndDefinedNamespace |
|           |         | -  Updated SVC exceptions with SVC2004 and SVC2006    |
|           |         | -  Updated links to OMA                               |
+-----------+---------+-------------------------------------------------------+
| 11/16/2020| v7.2.1  | - updated publishEventBatch to support stndDefined    |
+-----------+---------+-------------------------------------------------------+
| 01/04/2021| v7.2.2  | - added eventId use-case example, where eventID       |
|           |         |   uniqueness cannot be assured                        |
+-----------+---------+-------------------------------------------------------+

.. _time_zone_abbreviations: https://en.wikipedia.org/wiki/List_of_time_zone_abbreviations
.. _Common_definitions: https://www.openmobilealliance.org/release/REST_NetAPI_Common/V1_0-20180116-A/OMA-TS-REST_NetAPI_Common-V1_0-20180116-A.pdf
