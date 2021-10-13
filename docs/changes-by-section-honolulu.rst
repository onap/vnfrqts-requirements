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


Requirement Changes Introduced in Honolulu
------------------------------------------

This document summarizes the requirement changes by section that were
introduced between the Guilin release and
Honolulu release. Click on the requirement number to
navigate to the

.. contents::
    :depth: 2

Summary of Changes
^^^^^^^^^^^^^^^^^^

* **Requirements Added:** 0
* **Requirements Changed:** 16
* **Requirements Removed:** 7


Configuration Management > NETCONF Standards and Capabilities > VNF or PNF Configuration via NETCONF Requirements > NETCONF Server Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Requirements Changed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    :need:`R-58358`

    The VNF or PNF **MAY** implement the ``:with-defaults`` capability
    [RFC6243].
    

.. container:: note

    :need:`R-20353`

    The VNF or PNF **MUST** implement at least one of ``:candidate`` and
    ``:writable-running`` capabilities. When both ``:candidate`` and
    ``:writable-running`` are provided then two locks should be supported.
    

.. container:: note

    :need:`R-03465`

    The VNF or PNF **MUST** release locks to prevent permanent lock-outs
    when the corresponding <partial-unlock> operation succeeds if ":partial-lock" is supported.
    

.. container:: note

    :need:`R-83790`

    The VNF or PNF **MAY** implement the ``:validate`` capability.
    

.. container:: note

    :need:`R-01334`

    The VNF or PNF **MAY** conform to the NETCONF RFC 5717,
    "Partial Lock Remote Procedure Call".
    

.. container:: note

    :need:`R-68990`

    The VNF or PNF **MAY** support the ``:startup`` capability. It
    will allow the running configuration to be copied to this special
    database. It can also be locked and unlocked.
    

.. container:: note

    :need:`R-41829`

    The VNF or PNF **MUST** be able to specify the granularity of the
    lock via a restricted or full XPath expression if ":partial-lock" is supported.
    

.. container:: note

    :need:`R-70496`

    The VNF or PNF **MUST** implement the protocol operation:
    ``commit(confirmed, confirm-timeout)`` - Commit candidate
    configuration data store to the running configuration if ":candidate" is supported.
    

.. container:: note

    :need:`R-73468`

    The VNF **MUST** allow the NETCONF server connection
    parameters to be configurable during virtual machine instantiation
    through Heat templates where SSH keys, usernames, passwords, SSH
    service and SSH port numbers are Heat template parameters if VNF is heat based.
    

.. container:: note

    :need:`R-25238`

    The VNF or PNF PACKAGE **MUST** validated YANG code using the open
    source pyang [#7.3.1]_ program using the following commands:

    .. code-block:: text

      $ pyang --verbose --strict <YANG-file-name(s)> $ echo $!

    The VNF or PNF **MUST** have the echo command return a zero value otherwise the validation has failed.
    

.. container:: note

    :need:`R-53317`

    The VNF or PNF **SHOULD** conform its YANG model to RFC 8407,
    "Guidelines for Authors and Reviewers of YANG Data Model specification".
    

.. container:: note

    :need:`R-11499`

    The VNF or PNF **MAY** fully support the XPath 1.0 specification
    for filtered retrieval of configuration and other database contents.
    The 'type' attribute within the <filter> parameter for <get> and
    <get-config> operations may be set to 'xpath'. The 'select' attribute
    (which contains the XPath expression) will also be supported by the
    server. A server may support partial XPath retrieval filtering, but
    it cannot advertise the ``:xpath`` capability unless the entire XPath
    1.0 specification is supported.
    

.. container:: note

    :need:`R-22946`

    The VNF or PNF **SHOULD** conform its YANG model to RFC 8341,
    "NETCONF Access Control Model".
    

.. container:: note

    :need:`R-28756`

    The VNF or PNF **MAY** support ``:partial-lock`` and
    ``:partial-unlock`` capabilities, defined in RFC 5717. This
    allows multiple independent clients to each write to a different
    part of the <running> configuration at the same time.
    

.. container:: note

    :need:`R-68200`

    The VNF or PNF **MAY** support the ``:url`` value to specify
    protocol operation source and target parameters. The capability URI
    for this feature will indicate which schemes (e.g., file, https, sftp)
    that the server supports within a particular URL value. The 'file'
    scheme allows for editable local configuration databases. The other
    schemes allow for remote storage of configuration databases.
    

.. container:: note

    :need:`R-18733`

    The VNF or PNF **MUST** implement the protocol operation:
    ``discard-changes()`` - Revert the candidate configuration
    data store to the running configuration if ":candidate" is supported.
    

Requirements Removed
~~~~~~~~~~~~~~~~~~~~
    

.. container:: note

    R-02616

    The VNF or PNF **MUST** permit locking at the finest granularity
    if a VNF or PNF needs to lock an object for configuration to avoid blocking
    simultaneous configuration operations on unrelated objects (e.g., BGP
    configuration should not be locked out if an interface is being
    configured or entire Interface configuration should not be locked out
    if a non-overlapping parameter on the interface is being configured).
    

.. container:: note

    R-08134

    The VNF or PNF **MUST** conform to the NETCONF RFC 6241,
    "NETCONF Configuration Protocol".
    

.. container:: note

    R-10716

    The VNF or PNF **MUST** support parallel and simultaneous
    configuration of separate objects within itself.
    

.. container:: note

    R-13800

    The VNF or PNF **MUST** conform to the NETCONF RFC 5277,
    "NETCONF Event Notification".
    

.. container:: note

    R-22700

    The VNF or PNF **MUST** conform its YANG model to RFC 6470,
    "NETCONF Base Notifications".
    

.. container:: note

    R-63953

    The VNF or PNF **MUST** have the echo command return a zero value
    otherwise the validation has failed.
    

.. container:: note

    R-88899

    The VNF or PNF **MUST** support simultaneous <commit> operations
    within the context of this locking requirements framework.
    
