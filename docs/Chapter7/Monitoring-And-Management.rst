.. Modifications Copyright © 2017-2018 AT&T Intellectual Property
   Modifications Copyright © 2020 Nokia Solutions and Networks

.. Licensed under the Creative Commons License, Attribution 4.0 Intl.
   (the "License"); you may not use this documentation except in compliance
   with the License. You may obtain a copy of the License at

.. https://creativecommons.org/licenses/by/4.0/

.. Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

Monitoring & Management
-----------------------

In ONAP, DCAE is responsible of collecting, receiving, and analyzing
NF monitoring data. This data serves the basis for tracking the health,
performance, and operational status of the NF. DCAE provides a
number of predefined interfaces based upon accepted, open standards to support
monitoring data ingestion. Some of these interfaces collect data by polling or
pulling data from the NF using standard protocols. Other DCAE interfaces receive
monitoring data (such as VES events) that are pushed from the NFs.

A NF that produces monitoring data and uses protocols that are compatible with
ONAP's predefined monitoring ingestion capabilities can easily be integrated
with ONAP through simple configuration rather than custom development.

This chapter will define the expected requirements for a NF to easily integrate
with an instance of ONAP.

Monitoring and Fault Protocol Selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section provides the proper guidance on how a NF should determine the
protocol and data format for providing a specific types of telemetry data to
ONAP.

.. req::
   :id: R-82909
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   The VNF or PNF **MUST** report faults and alarms using either
   :ref:`Virtual Function Event Streaming (VES) <ves_monitoring_requirements>`
   or :ref:`SNMP <snmp_monitoring_requirements>`. (NOTE: See relevant sections
   for more detailed requirements)

.. req::
   :id: R-554966
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   The VNF or PNF **MUST** report performance metrics using
   :ref:`Virtual Function Event Streaming (VES) <ves_monitoring_requirements>`
   or :ref:`bulk_performance_measurement`.

.. req::
   :id: R-69111
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   The VNF or PNF **MUST** report application logs using either
   :ref:`Virtual Function Event Streaming (VES) <ves_monitoring_requirements>`
   or Syslog in compliance with
   `RFC 5424 <https://tools.ietf.org/html/rfc5424>`__ .


.. req::
   :id: R-209104
   :target: VNF or PNF
   :keyword: SHOULD
   :introduced: guilin

   The VNF or PNF producing VES syslog events **SHOULD** restrict these
   events to those that convey significant errors or warnings needed to support
   the operation or troubleshooting of the VNF or PNF. It is expected the
   volume of such events would be lower (e.g. less than 2000 per day) than
   more detailed events produced in the course of normal operations.

.. req::
   :id: R-332680
   :target: VNF or PNF
   :keyword: SHOULD
   :introduced: casablanca
   :updated: guilin
   :validation_mode: in_service
   :impacts: dcae

   The VNF or PNF producing VES events **SHOULD** deliver syslog messages
   that meet the criteria in R-209104 to the VES Event Listener using the
   ``syslog`` VES domain.

.. req::
   :id: R-935717
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   The VNF or PNF **MUST** report heartbeats using
   :ref:`Virtual Function Event Streaming (VES) <ves_monitoring_requirements>`.

.. req::
   :id: R-697654
   :target: VNF or PNF
   :keyword: MAY
   :introduced: casablanca
   :updated: guilin
   :validation_mode: in_service
   :impacts: DCAE

   The VNF or PNF **MAY** leverage ONAP's High Volume VNF Event Streaming
   (HV-VES) when there is a need to deliver large volumes of real-time
   performance management metrics. See
   `HV-VES Collector <https://onap-doc.readthedocs.io/projects/onap-dcaegen2/en/latest/sections/services/ves-hv/index.html>`__
   service details for more information.

.. req::
   :id: R-857511
   :target: VNF or PNF PROVIDER
   :keyword: MUST
   :introduced: guilin
   :validation_mode: none
   :impacts: DCAE

   VNF or PNF Provider **MUST** have agreement with the Service Provider before
   utilizing the HV-VES option for monitoring as this option does not fully
   integrate with the ONAP's DCAE event processing capabilities.

.. req::
   :id: R-908291
   :target: VNF or PNF
   :keyword: MAY
   :introduced: casablanca
   :updated: guilin
   :validation_mode: in_service
   :impacts: dcae, dmaap

   The VNF or PNF **MAY** leverage a bulk VNF or PNF telemetry transmission
   mechanism in instances where other transmission
   methods are not practical or advisable.

   NOTE: For additional information and use cases for the Bulk Telemetry
   Transmission Mechanism, please refer to
   the :ref:`bulk_performance_measurement` requirements and the
   `5G - Bulk PM ONAP Development <https://wiki.onap.org/display/DW/5G+-+Bulk+PM>`__
   Wiki page.

.. _snmp_monitoring_requirements:

SNMP Monitoring Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. req::
   :id: R-261501
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   If the VNF or PNF is using SNMP, then the VNF or PNF Provider **MUST**
   provide a Management Information Base (MIB) file that uniquely identifies
   and describes all SNMP events exposed by the network function.

.. req::
   :id: R-233922
   :target: VNF or PNF
   :keyword: SHOULD
   :introduced: guilin

   If the VNF or PNF is using SNMP, then the VNF or PNF Provider **SHOULD**
   provide examples of all SNMP alarms.

.. _ves_monitoring_requirements:

Virtual Function Event Streaming (VES) Client Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The VES protocol enables NFs to transmit telemetry data in a non-proprietary,
extensible format to ONAP using the HTTP protocol. This chapter will define
the requirements for a NF to deliver events to ONAP's VES event listeners in
a manner that conforms with the appropriate VES Event Listener specifications,
and ensures the NF can be configured to maximize the reliability of telemetry
data delivery.


Event Definition and Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
   :id: R-520802
   :target: VNF or PNF PROVIDER
   :keyword: MUST
   :introduced: casablanca
   :updated: guilin
   :validation_mode: static
   :impacts: dcae

   If the VNF or PNF is using VES, then the VNF or PNF Provider **MUST** provide
   a YAML file formatted in adherence with the
   :ref:`VES Event Registration specification <ves_event_registration_3_2>`
   that defines the following information for each event produced by the VNF:

   * ``eventName``
   * Required fields
   * Optional fields
   * Any special handling to be performed for that event

.. req::
   :id: R-120182
   :target: VNF or PNF PROVIDER
   :keyword: MUST
   :introduced: casablanca
   :updated: guilin
   :validation_mode: static
   :impacts: dcae

   A VNF or PNF Provider utilizing VES **MUST** indicate specific conditions
   that may arise, and recommend actions that may be taken at specific
   thresholds, or if specific conditions repeat within a specified time
   interval, using the semantics and syntax described by the
   :ref:`VES Event Registration specification <ves_event_registration_3_2>`.

   **NOTE:** The Service Provider may override VNF or PNF provider Event
   Registrations using the ONAP SDC Design Studio to finalizes Service
   Provider engineering rules for the processing of the VNF or PNF events.
   These changes may modify any of the following:

   * Threshold levels
   * Specified actions related to conditions

.. req::
   :id: R-123044
   :target: VNF or PNF PROVIDER
   :keyword: MAY
   :introduced: casablanca
   :updated: dublin
   :validation_mode: in_service
   :impacts: dcae

   The VNF or PNF Provider **MAY** require that specific events, identified by
   their ``eventName``, require that certain fields, which are optional in the
   common event format, must be present when they are published.

Event Formatting and Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
   :id: R-570134
   :target: VNF or PNF
   :keyword: MUST
   :introduced: casablanca
   :updated: guilin
   :validation_mode: in_service
   :impacts: dcae

   The VES events produced by the VNF or PNF **MUST** be compliant with the
   common event formats defined in one of the following specifications:

   * :ref:`VES Event Listener 5.4.1<ves_event_listener_5_4_1>`
   * :ref:`VES Event Listener 7.1.1<ves_event_listener_7_1>`
   * :ref:`VES Event Listener 7.2<ves_event_listener_7_2>`

   The latest version (7.2) should be preferred. Earlier versions are
   provided for backwards compatibility.

.. req::
   :id: R-528866
   :target: VNF or PNF
   :keyword: MUST
   :introduced: casablanca
   :updated: guilin
   :validation_mode: in_service
   :impacts: dcae

   The VES events produced by the VNF or PNF **MUST** conform to the schema and
   other formatting requirements specified in the relevant VES Event Listener
   specification.

.. req::
   :id: R-283988
   :target: VNF or PNF
   :keyword: MUST NOT
   :introduced: casablanca
   :updated: guilin
   :validation_mode: in_service
   :impacts: dcae

   A VNF or PNF producing VES events **MUST NOT** send information through
   extensible structures if the event specification has explicitly defined
   fields for that information.

.. req::
   :id: R-470963
   :target: VNF or PNF
   :keyword: SHOULD
   :introduced: casablanca
   :updated: guilin
   :validation_mode: in_service
   :impacts: dcae

   A VNF or PNF producing VES events **SHOULD** leverage camel case to
   separate words and acronyms used as keys that will be sent through extensible
   fields. When an acronym is used as the key, then only the first letter shall
   be capitalized.

.. req::
   :id: R-408813
   :target: VNF or PNF
   :keyword: MUST
   :introduced: casablanca
   :updated: guilin
   :validation_mode: none
   :impacts: dcae

   A VNF or PNF producing VES events **MUST** pass all information it is
   able to collect even if the information field is identified as optional.
   However, if the data cannot be collected, then optional fields can be
   omitted.
 
.. req::
   :id: R-408814
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin
   :validation_mode: none
   :impacts: dcae

   The VNF or a PNF producing VES stndDefined domain events to report
   standards-organization defined events to ONAP, **MUST** set the
   event.stndDefinedNamespace property. By default, ONAP ships with support
   for the following:

   * 3GPP-Provisioning
   * 3GPP-Heartbeat
   * 3GPP-FaultSupervision
   * 3GPP-PerformanceAssurance

   Another namespace, outside of the list provided, needs to registered in ONAP in coordination
   with the operator before it can be used.

.. req::
   :id: R-408815
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin
   :validation_mode: none
   :impacts: dcae
   
   If the VNF or PNF producing VES stndDefined domain events provides
   the event.stndDefinedFields.schemaReference then it **MUST** set its value
   to the publicUrl value in DCAE's VES Collector `etc/externalRepo/schema-map.json <https://github.com/onap/dcaegen2-collectors-ves/blob/guilin/etc/externalRepo/schema-map.json/>`_ 
   that describes the data being sent in event.stndDefinedFields.data.

.. req::
   :id: R-408816
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin
   :validation_mode: none
   :impacts: dcae
   
   If the VNF or PNF producing VES stndDefined domain events provides
   the event.stndDefinedFields.schemaReference then it **MUST** only pass events
   that conform to schema references previously registered with DCAE otherwise
   the event will be rejected. By default, ONAP ships with support for schemas 
   found in DCAE's VES Collector `etc/externalRepo/schema-map.json <https://github.com/onap/dcaegen2-collectors-ves/blob/guilin/etc/externalRepo/schema-map.json/>`_.

.. req::
   :id: R-408817
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin
   :validation_mode: none
   :impacts: dcae
   
   The VNF or PNF Provider producing stndDefined events **MUST** coordinate with
   the operator, willing to validate stndDefined events, to configure DCAE to 
   accept any new event schema prior to sending those events or the events 
   will be rejected.

.. req::
   :id: R-408818
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin
   :validation_mode: none
   :impacts: dcae
      
   If the VNF or PNF producing VES stndDefined domain events provides 
   the event.stndDefinedFields.schemaReference then it **MUST** set the 
   event.stndDefined.schemaReference property to an exact structure, 
   from supported schemaReference, describing the notification within 
   an openAPI specification, using JSON Pointer as URI fragment  e.g.
   “https://forge.3gpp.org/.../faultMnS.yaml#/components/schemas/notifyNewAlarm"

Configuration Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~

This section defines the types the configuration options and defaults a NF
producing VES events should provide to ensure the NF can be configured properly
for the Service Provider's ONAP environment and ensure reliable delivery of
VES events.

There are several methods available to provide configuration settings to a
network function. This document does not specify the exact manner in which
the configuration elements described below must be required. The
configuration can be provided during instantiation (e.g. preload), provided by
an ONAP controller action, or provided manually.

.. req::
   :id: R-460012
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   The VNF or PNF producing VES events **MUST** allow the configuration of
   the attributes defined in Table 1 and utilize the provided default value
   (where applicable) when the configuration value is not provided by the
   Service Provider.

.. req::
   :id: R-940591
   :target: VNF or PNF
   :keyword: SHOULD
   :introduced: guilin

   A VNF or PNF producing VES events **SHOULD** use the recommended parameter
   name for the configurable value from Table 1.

.. table:: **Table 1**: VES Configurable Values

   +----------------------+-----------------------------------+----------------+-------------------------------------+
   |Parameter             | Description                       |  Default       | Parameter Name (VES 7.2+)           |
   +======================+===================================+================+=====================================+
   |VES Listener Endpoint | FQDN or IP of the Event Listener  |       n/a      | ves_listener_endpoint               |
   +----------------------+-----------------------------------+----------------+-------------------------------------+
   |Heartbeat Interval    | Frequency in seconds the NF must  |        60      | ves_heartbeat_interval_seconds      |
   |                      | send a heartbeat to the event     |                |                                     |
   |                      | listener                          |                |                                     |
   +----------------------+-----------------------------------+----------------+-------------------------------------+
   |Timeout Value         | Duration in seconds the NF should |         5      | ves_timeout_seconds                 |
   |                      | wait for ACK from the event       |                |                                     |
   |                      | listener before timeout           |                |                                     |
   +----------------------+-----------------------------------+----------------+-------------------------------------+
   |Measurement Interval  | Window size in seconds to use for |        300     | ves_measurement_interval_seconds    |
   |                      | aggregated measurements           |                |                                     |
   +----------------------+-----------------------------------+----------------+-------------------------------------+
   |HTTP Username         | Required if NF supports HTTP      |        n/a     | ves_http_username                   |
   |                      | Basic Authentication with the     |                |                                     |
   |                      | VES Event Listener                |                |                                     |
   +----------------------+-----------------------------------+----------------+-------------------------------------+
   |HTTP Password         | Required if NF supports HTTP      |        n/a     | ves_http_password                   |
   |                      | Basic Authentication with the     |                |                                     |
   |                      | VES Event Listener                |                |                                     |
   +----------------------+-----------------------------------+----------------+-------------------------------------+


VES Listener Endpoint and DNS Resolution
++++++++++++++++++++++++++++++++++++++++

In a high availability deployment of a VES Event Listener, a round-robin DNS or
dynamic DNS may be used to either load balance or provide fault tolerance of
the Event Listener.  Adherence to the following requirements ensure the VNF or
PNF interacts properly with this deployment configuration.

.. req::
   :id: R-70492
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   The VNF or PNF **MUST** support DNS resolution of the VES Listener Endpoint
   if a Fully Qualified Domain Name (FQDN) is provided.

.. req::
   :id: R-130645
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   The VNF or PNF **MUST** respect the Time To Live provided by the DNS for
   the VES Event Listener FQDN.

Event Delivery Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
   :id: R-06924
   :target: VNF or PNF
   :keyword: MUST
   :updated: guilin

   The VNF or PNF producing VES events **MUST** deliver VES events as it
   becomes available or according to the configured measurement interval.

.. req::
    :id: R-655209
    :target: VNF or PNF
    :keyword: MUST
    :introduced: guilin

    The VNF or PNF producing VES events **MUST** respect the configured
    VES Timeout Value when delivering VES events, and abort any call where
    the VES Event Listener does not successfully acknowledge the delivery of
    event(s) within the Timeout Value. These failed transactions should be
    buffered and retried in accordance with the
    :ref:`ves_buffering_requirements` Requirements.

.. req::
   :id: R-176945
   :target: VNF or PNF
   :keyword: SHOULD NOT
   :introduced: guilin

   The VNF or PNF producing VES events **SHOULD NOT** send syslog events to the
   VES Event Listener during debug mode, but rather store syslog events locally
   for access or possible file transfer.

.. _ves_buffering_requirements:

Buffering and Redelivery
~~~~~~~~~~~~~~~~~~~~~~~~

To maximize the reliable delivery of VES events when the VES Listener becomes
unavailable or unhealthy, the NF must adhere to these requirements.

.. req::
   :id: R-658596
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   A VNF or PNF producing VES events **MUST** buffer events that meet the
   following criteria if the VES Event Listener is unreachable or the request
   encounters a timeout.

   * Faults with eventSeverity of ``MINOR``, ``MAJOR``, ``NORMAL``, or
     ``CRITICAL``
   * Syslog with syslogSev of ``Emergency``, ``Alert``, ``Critical``,
     ``Error``, or ``Warning``
   * All measurement events

.. req::
   :id: R-636251
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   A VNF or PNF producing VES events **MUST** size the event buffer
   referenced in R-658596 such that it can buffer a minimum of 1 hours of
   events under nominal load.

.. req::
   :id: R-498679
   :target: VNF or PNF
   :keyword: MAY
   :introduced: guilin

   A VNF or PNF producing VES events **MAY** discard buffered events older
   than a maximum retention period, not less than 1 hour, even if the event
   was never successfully delivered to the event listener. While discarding
   based on this retention period is supported for backwards compatibility, it
   is recommended to retain events until the maximum buffer size is reached per
   R-346137 as that will maximize the number of events delivered.

.. req::
   :id: R-346137
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   A VNF or PNF producing VES events that is buffering events per R-658596
   **MUST** store in-scope events even when the maximum capacity of the
   buffer (defined in R-636251) has been reached. To make room for new events
   in this situation, hte oldest event in the buffer shall be removed
   as necessary. (i.e. First In First Out)

.. req::
   :id: R-379523
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   A VNF or PNF producing VES events that is buffering events due to an
   unavailable VES Event Listener **MUST** redeliver all buffered events
   according to the following rules when the VNF or PNF detects the VES Event
   Listener has become available:

   * Deliver all previously buffered events before sending new events
   * Deliver buffered events in the order they were received

.. req::
   :id: R-818859
   :target: VNF or PNF
   :keyword: MUST
   :introduced: guilin

   The VNF or PNF producing VES events **MUST** not allow an unavailable or
   timing out VES Event Listener to impact the performance, stability, or
   correct execution of network function.

.. req::
   :id: R-103464
   :target: VNF or PNF
   :keyword: MAY
   :introduced: guilin

   A VNF or PNF producing VES events that is buffering events due to an
   unavailable VES Event Listener **MAY** leverage to ``publishEventBatch``
   operation to redeliver buffered events. Please note this can only be
   used when all buffered events belong to the same domain due to the
   restrictions in place for the operation.

Security
~~~~~~~~

.. req::
    :id: R-68165
    :target: VNF or PNF
    :keyword: MUST
    :updated: dublin

    The VNF or PNF **MUST** encrypt any content containing Sensitive Personal
    Information (SPI) or certain proprietary data, in addition to applying the
    regular procedures for securing access and delivery.


.. req::
   :id: R-33878
   :target: VNF or PNF
   :keyword: MUST
   :introduced: el alto
   :updated: guilin

   The VNF or PNF **MUST** utilize one of the authentication methods
   prescribed by the relevant VES Event Listener specification.

.. _bulk_performance_measurement:

Bulk Performance Measurement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. req::
    :id: R-841740
    :target: VNF or PNF
    :keyword: SHOULD
    :introduced: casablanca
    :updated: dublin
    :impacts: dcae, dmaap

    The VNF or PNF **SHOULD** support FileReady VES event for event-driven bulk transfer
    of monitoring data.

.. req::
    :id: R-440220
    :target: VNF or PNF
    :keyword: SHOULD
    :introduced: casablanca
    :updated: dublin
    :impacts: dcae, dmaap

    The VNF or PNF **SHOULD** support File transferring protocol, such as FTPES or SFTP,
    when supporting the event-driven bulk transfer of monitoring data.

.. req::
    :id: R-75943
    :target: VNF or PNF
    :keyword: SHOULD
    :introduced: casablanca
    :updated: guilin
    :impacts: dcae, dmaap

    The VNF or PNF **SHOULD** support the data schema defined in 3GPP TS 32.435 or 3GPP TS 28.532, when
    supporting the event-driven bulk transfer of monitoring data.

.. req::
    :id: R-807129
    :target: VNF or PNF
    :keyword: SHOULD
    :introduced: dublin
    :impacts: dcae, dmaap

    The VNF or PNF **SHOULD** report the files in FileReady for as long as they are
    available at VNF or PNF.

    Note: Recommended period is at least 24 hours.


.. |image0| image:: ../Data_Model_For_Event_Records.png

.. |image1| image:: ../VES_JSON_Driven_Model.png
      :width: 5in
      :height: 3in

.. |image2| image:: ../Protocol_Buffers_Driven_Model.png
      :width: 4.74in
      :height: 3.3in

.. |image3| image:: ../Bulk_Data_Transfer_Mechv1.png
      :width: 4.74in
      :height: 3.3in
