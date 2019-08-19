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


Requirement Changes Introduced in El Alto
========================================================

This document summarizes the requirement changes by section that were
introduced between the Dublin release and
El Alto release. Click on the requirement number to
navigate to the

.. contents::
    :depth: 2

Summary of Changes
------------------

* **Requirements Added:** 1
* **Requirements Changed:** 14
* **Requirements Removed:** 2


Monitoring & Management > Data Structure Specification of the Event Record
--------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-520802`

    The VNF or PNF provider **MUST** provide a YAML file formatted in adherence with
    the :ref:`VES Event Registration specification <ves_event_registration_3_2>`
    that defines the following information for each event produced by the VNF:

    * ``eventName``
    * Required fields
    * Optional fields
    * Any special handling to be performed for that event
    

.. container:: note

    :need:`R-570134`

    The events produced by the VNF or PNF **MUST** must be compliant with the common
    event format defined in the
    :ref:`VES Event Listener<ves_event_listener_7_1>`
    specification.
    

.. container:: note

    :need:`R-120182`

    The VNF or PNF provider **MUST** indicate specific conditions that may arise, and
    recommend actions that may be taken at specific thresholds, or if specific
    conditions repeat within a specified time interval, using the semantics and
    syntax described by the :ref:`VES Event Registration specification <ves_event_registration_3_2>`.
    

ONAP Heat Orchestration Template Format > Heat Orchestration Template Structure > resources > properties
--------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-10834`

    A VNF's Heat Orchestration Template resource attribute ``property:``
    **MUST NOT** use more than two levels of nested ``get_param`` intrinsic
    functions when deriving a property value.  SDC does not support nested
    ``get_param`` with recursive lists (i.e., a list inside list).
    The second ``get_param`` in a nested lookup must directly derive its value
    without further calls to ``get_param`` functions.

    * Example of valid nesting:

      * ``name: {get_param: [ {vm-type}_names, {get_param : index } ] }``

    * Examples of invalid nesting.  SDC will not support these examples since
      there is an array inside array.

      * ``name: {get_param: [ {vm-type}_names, { get_param: [ indexlist, 0 ] } ] }``
      * ``name: {get_param: [ {vm-type}_names, { get_param: [ indexlist1, { get_param: indexlist2 } ] } ] }``
    

ONAP Heat Orchestration Templates Overview > ONAP Heat Orchestration Template Filenames > Base Modules
------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-81339`

    A VNF Heat Orchestration Template's Base Module file name **MUST** include
    case insensitive 'base' in the filename and
    **MUST** match one of the following four
    formats:

     1.) ``base_<text>.y[a]ml``

     2.) ``<text>_base.y[a]ml``

     3.) ``base.y[a]ml``

     4.) ``<text>_base_<text>``.y[a]ml

    where ``<text>`` **MUST** contain only alphanumeric characters and
    underscores '_' and **MUST NOT** contain the case insensitive string
    ``base`` or ``volume``.
    

ONAP Heat Orchestration Templates Overview > ONAP Heat Orchestration Template Filenames > Cinder Volume Modules
---------------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-589037`

    A VNF Heat Orchestration Template's Cinder Volume Module ``resources:``
    section
    **MUST** only be defined using one of the following:

    * one of more ``OS::Cinder::Volume`` resources
    * one or more ``OS::Heat::ResourceGroup`` resources that call a nested YAML
      file that contains only ``OS::Cinder::Volume`` resources
    * a resource that calls a nested YAML file (static nesting) that contains
      only ``OS::Cinder::Volume`` resources
    

ONAP Heat Orchestration Templates Overview > ONAP Heat Orchestration Template Filenames > Incremental Modules
-------------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-87247`

    VNF Heat Orchestration Template's Incremental Module file name
    **MUST** contain only alphanumeric characters and underscores
    '_' and **MUST NOT** contain the case insensitive string ``base``.
    

ONAP Heat Orchestration Templates Overview > ONAP Heat Orchestration Template Filenames > Nested Heat file
----------------------------------------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-76057`

    VNF Heat Orchestration Template's Nested YAML file name **MUST** contain
    only alphanumeric characters and underscores '_' and
    **MUST NOT** contain the case insensitive string ``base``.
    

Resource: OS::Nova::Server - Parameters
---------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-304011`

    A VNF's Heat Orchestration Template's ``OS::Nova::Server`` resource's

    * Resource ID (defined in R-29751)
    * property ``image`` parameter name (defined in R-58670)
    * property ``flavor`` parameter name (defined in R-45188)
    * property ``name`` parameter name (defined in R-54171 & R-87817)
    * property ``networks`` map property ``port`` value which is a
      ``OS::Neutron::Port`` Resource ID (defined in R-20453)
      referenced using the intrinsic function ``get_attr``

    **MUST** contain the identical ``{vm-type}``
    and **MUST** follow the naming conventions defined
    in R-58670, R-45188, R-54171, R-87817, and R-29751.  And the ``{index}`` in
    the ``OS::Nova::Server`` Resource ID (defined in R-29751) **MUST** match
    the ``{vm-type_index}`` defined in
    the ``OS::Nova::Server`` property ``networks`` map property ``port``
    referenced ``OS::Neutron::Port`` Resource ID (defined in R-20453).
    

Resource: OS::Nova::Server - Parameters > Property: availability_zone
---------------------------------------------------------------------


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-256790`

    A VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    property ``availability_zone`` parameter name **MAY** change when
    past into a nested YAML file.
    

Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-98450`

    A VNF's Heat Orchestration Template's base module or incremental module
    resource ``OS::Nova::Server``
    property ``availability_zone`` parameter
    **MUST** follow the naming convention

    * ``availability_zone_{index}``

    where ``{index}`` is a numeric value that **MUST** start at zero
    in a VNF's Heat Orchestration Templates and **MUST**
    increment by one.
    

.. container:: note

    :need:`R-23311`

    The VNF's Heat Orchestration Template's base module or incremental module
    resource ``OS::Nova::Server`` property
    ``availability_zone`` parameter **MUST** be declared as type: ``string``.
    

VNF On-boarding and package management > Resource Control Loop
--------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-42018`

    The VNF or PNF Package **MUST** include documentation which must include
    all events (fault, measurement for VNF or PNF Scaling, Syslogs, State Change
    and Mobile Flow), that need to be collected at each VM, VNFC (defined in `VNF Guidelines <https://onap.readthedocs.io/en/latest/submodules/vnfrqts/guidelines.git/docs/vnf_guidelines.html>`__ ) and for the overall VNF or PNF.
    

VNF On-boarding and package management > Resource Description
-------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-22346`

    The VNF or PNF package **MUST** provide :ref:`VES Event Registration <ves_event_registration_3_2>`
    for all VES events provided by that VNF or PNF.
    

VNF Security > VNF General Security Requirements
------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-21819`

    VNFs that are subject to regulatory requirements **MUST** provide
    functionality that enables the Operator to comply with ETSI TC LI
    requirements, and, optionally, other relevant national equivalents.
    

VNF Security > VNF Identity and Access Management Requirements
--------------------------------------------------------------


Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-98391

    The VNF **MUST**, if not integrated with the Operator's Identity and
    Access Management system, support Role-Based Access Control to enforce
    least privilege.
    

VNF Security > VNF Security Analytics Requirements
--------------------------------------------------


Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-22286

    The VNF **MUST** support Integration functionality via
    API/Syslog/SNMP to other functional modules in the network (e.g.,
    PCRF, PCEF) that enable dynamic security control by blocking the
    malicious traffic or malicious end users.
    
