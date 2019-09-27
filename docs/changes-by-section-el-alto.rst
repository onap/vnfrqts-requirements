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

* **Requirements Added:** 9
* **Requirements Changed:** 21
* **Requirements Removed:** 3


Monitoring & Management > Data Structure Specification of the Event Record
--------------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

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
    

.. container:: note

    :need:`R-520802`

    The VNF or PNF provider **MUST** provide a YAML file formatted in adherence with
    the :ref:`VES Event Registration specification <ves_event_registration_3_2>`
    that defines the following information for each event produced by the VNF:

    * ``eventName``
    * Required fields
    * Optional fields
    * Any special handling to be performed for that event
    

Monitoring & Management > Monitoring & Management Requirements > Security
-------------------------------------------------------------------------


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-55634`

    If VNF or PNF is using Basic Authentication, then the VNF or PNF
    **MUST** be in compliance with
    `RFC7617 <https://tools.ietf.org/html/rfc7617>`_ for authenticating HTTPS
    connections to the DCAE VES Event Listener.
    

.. container:: note

    :need:`R-33878`

    The VNF or PNF **MUST** support one of the following authentication
    methods for authenticating HTTPS connections to the DCAE VES Event
    Listener:

    - The preferred method is Certificate Authentication

    - The non-preferred option is Basic Authentication.
    

.. container:: note

    :need:`R-43387`

    If the VNF or PNF is using Certificate Authentication, the
    VNF or PNF **MUST** support mutual TLS authentication and the Subject
    Name in the end-entity certificate MUST be used according to
    `RFC5280 <https://tools.ietf.org/html/rfc5280>`_.

    Note: In mutual TLS authentication, the client (VNF or PNF) must
    authenticate the server (DCAE) certificate and must provide its own
    X.509v3 end-entity certificate to the server for authentication.
    

Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-894004`

    If the VNF or PNF is using Basic Authentication, then when the VNF
    or PNF sets up a HTTPS connection to the DCAE VES Event Listener,
    the VNF or PNF **MUST** provide a username and password to the
    DCAE VES Event Listener in the Authorization header and the VNF
    or PNF MUST support one-way TLS authentication.

    Note: In one-way TLS authentication, the client (VNF or PNF)
    must authentication the server (DCAE) certificate.
    

.. container:: note

    :need:`R-01427`

    If the VNF or PNF is using Basic Authentication, then the VNF or
    PNF **MUST** support the provisioning of security and authentication
    parameters (HTTP username and password) in order to be able to
    authenticate with DCAE VES Event Listener.

    Note: The configuration management and provisioning software
    are specific to a vendor architecture.
    

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
    

ONAP Heat VNF Modularity
------------------------


Requirements Added
~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-610050`

    The same ``{vm-type}`` for a VNF's Heat Orchestration Template's
    ``OS::Nova::Server`` resource (as defined in R-01455) **MAY** exist in
    the VNF's Heat Orchestration Template's Base Module (or invoked nested yaml
    file) and/or one or more of the VNF's Heat Orchestration Template's
    Incremental Modules (or invoked nested yaml file).
    

.. container:: note

    :need:`R-610010`

    A VNF's Heat Orchestration Template's Base Module **MAY** declare zero, one,
    or more than one ``OS::Nova::Server`` resource.  A ``OS::Nova::Server``
    **MAY** be created in the base module or a nested yaml file invoked by the
    base module.
    

.. container:: note

    :need:`R-610030`

    A VNF's Heat Orchestration Template's Incremental Module **MUST**
    declare one or more ``OS::Nova::Server`` resources.  A ``OS::Nova::Server``
    **MAY** be created in the incremental module or a nested yaml file invoked
    by the incremental module.
    

.. container:: note

    :need:`R-610040`

    If a VNF's Heat Orchestration Template's Incremental Module contains two or
    more ``OS::Nova::Server`` resources, the ``OS::Nova::Server`` resources
    **MAY** define the same ``{vm-type}`` (as defined in R-01455) or **MAY**
    define different ``{vm-type}``.

    Note that

    - there is no constraint on the number of unique ``{vm-type}`` defined in
      the incremental module.
    - there is no constraint on the number of ``OS::Nova::Server`` resources
      that define the same ``{vm-type}`` in the incremental module.
    - if an ``OS::Nova::Server`` is created in a nested yaml file invoked by
      the incremental module, the nested yaml file **MUST NOT** contain more
      than one ``OS::Nova::Server`` resource (as defined in R-17528).
    

.. container:: note

    :need:`R-610020`

    If a VNF's Heat Orchestration Template's Base Module contains two or more
    ``OS::Nova::Server`` resources (created in the base module itself and/or
    in a nested yaml file invoked by the base module), the ``OS::Nova::Server``
    resources **MAY**
    define the same ``{vm-type}`` (as defined in R-01455) or **MAY**
    define different ``{vm-type}``.

    Note that

    - there is no constraint on the number of unique ``{vm-type}`` defined in
      the base module.
    - there is no constraint on the number of ``OS::Nova::Server`` resources
      that define the same ``{vm-type}`` in the base module.
    - if an ``OS::Nova::Server`` is created in a nested yaml file invoked by
      the base module, the nested yaml file **MUST NOT** contain more than one
      ``OS::Nova::Server`` resource (as defined in R-17528).
    

PNF Plug and Play > PNF Plug and Play
-------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-763774`

    The VNF or PNF **MUST** support a HTTPS connection to the DCAE
    VES Event Listener.
    

Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-579051

    The PNF **MAY** support a HTTP connection to the DCAE VES Event Listener.

    Note: HTTP is allowed but not recommended.
    

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

    :need:`R-23311`

    The VNF's Heat Orchestration Template's base module or incremental module
    resource ``OS::Nova::Server`` property
    ``availability_zone`` parameter **MUST** be declared as type: ``string``.
    

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
    

VNF Security > VNF Cryptography Requirements
--------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-49109`

    The VNF or PNF **MUST** support HTTPS using TLS v1.2 or higher
    with strong cryptographic ciphers.
    

VNF Security > VNF General Security Requirements
------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-21819`

    VNFs that are subject to regulatory requirements **MUST** provide
    functionality that enables the Operator to comply with ETSI TC LI
    requirements, and, optionally, other relevant national equivalents.
    

.. container:: note

    :need:`R-258686`

    The VNF application processes **SHOULD NOT** run as root. If a VNF
    application process must run as root, the technical reason must
    be documented.
    

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
    

VNF or PNF CSAR Package > VNF Package Contents
----------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-01123`

    The VNF or PNF package Manifest file **MUST** contain: VNF or PNF
    package meta-data, a list of all artifacts (both internal and
    external) entry's including their respected URI's, as specified
    in ETSI GS NFV-SOL 004
    

VNF or PNF CSAR Package > VNF or PNF Package Authenticity and Integrity
-----------------------------------------------------------------------


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-130206`

    If the VNF or PNF CSAR Package utilizes Option 1 for package security, then
    the complete CSAR file **MUST** contain a Digest (a.k.a. hash) for each of
    the components of the VNF or PNF package. The table of hashes is included
    in the package manifest file, which is signed with the VNF or PNF provider
    private key. In addition, the VNF or PNF provider MUST include a signing
    certificate that includes the VNF or PNF provider public key, following a
    TOSCA pre-defined naming convention and located either at the root of the
    archive or in a predefined location specified by the TOSCA.meta file with
    the corresponding entry named "ETSI-Entry-Certificate".
    
