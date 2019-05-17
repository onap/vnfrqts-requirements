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


PNF Plug and Play
------------------------

PNF Plug and Play
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following are the requirements related to PNF Plug and Play.

.. req::
    :id: R-56718
    :target: PNF
    :keyword: MAY
    :introduced: casablanca

    The PNF Vendor **MAY** provide software version(s) to be supported by PNF
    for SDC Design Studio PNF Model. This is set in the PNF Model property
    software_versions.

.. req::
    :id: R-106240
    :target: PNF
    :keyword: SHOULD
    :introduced: casablanca
    :updated: El Alto

    The following VES Events **SHOULD** be supported by the PNF: pnfRegistration
    VES Event, HVol VES Event, and Fault VES Event. These are onboarded via
    he SDC Design Studio.

    Note: these VES Events are emitted from the PNF to support PNF Plug and
    Play, High Volume Measurements, and Fault events respectively.

.. req::
    :id: R-258352
    :target: PNF
    :keyword: MUST
    :introduced: casablanca

    The PNF **MUST** support & accept the provisioning of an ONAP contact IP
    address (in IPv4 or IPv6 format).

    Note: For example, it a possibility is that an external EMS would configure
    & provision the ONAP contact IP address to the PNF (in either IPv4 or
    IPv6 format). For the PNF Plug and Play Use Case, this IP address is the
    service provider's "point of entry" to the DCAE VES Listener.

    Note: different service provider's network architecture may also require
    special setup to allow an external PNF to contact the ONAP installation.
    For example, in the AT&T network, a maintenance tunnel is used to access
    ONAP.

.. req::
    :id: R-793716
    :target: PNF
    :keyword: MUST
    :introduced: casablanca

    The PNF **MUST** have "ONAP Aware" software which is capable of performing
    PNF PnP registration with ONAP. The "ONAP Aware" software is capable of
    performing the PNF PnP Registration with ONAP MUST either be loaded
    separately or integrated into the PNF software upon physical delivery
    and installation of the PNF.

    Note: It is up to the specific vendor to design the software management
    functions.

.. req::
    :id: R-952314
    :target: PNF
    :keyword: MUST
    :introduced: casablanca

    If the PNF set up a TLS connection and mutual (two-way) authentication is
    being used, then the PNF **MUST** provide its own X.509v3 Certificate to
    the DCAE VES Collector for authentication.

    Note: This allows TLS authentication by DCAE VES Collector.

    Note: The PNF got its X.509 certificate through Enrollment with an
    operator certificate authority or a X.509 vendor certificate from the
    vendor factory CA.

    Note: In R3 three authentication options are supported:

    (1) HTTP with Username & Password and no TLS.

    (2) HTTP with Username & Password & TLS with two-way certificate
        authentication.

    (3) HTTP with Username & Password & TLS with server-side
        certificate authentication.

.. req::
    :id: R-809261
    :target: PNF
    :keyword: MUST
    :introduced: casablanca

    The PNF **MUST** use a IP address to contact ONAP.

    Note: it is expected that an ONAP operator can ascertain the ONAP IP
    address or the security gateway to reach ONAP on the VID or ONAP portal
    GUI.

    Note: The ONAP contact IP address has been previously configured and
    provisioned prior to this step.

    Note: The ONAP IP address could be provisioned or resolved through
    FQDN & DNS.

.. req::
    :id: R-763774
    :target: PNF
    :keyword: MUST
    :introduced: casablanca

    The PNF **MUST** support a HTTPS connection to the DCAE VES Event
    Listener.

.. req::
    :id: R-579051
    :target: PNF
    :keyword: MAY
    :introduced: casablanca

    The PNF **MAY** support a HTTP connection to the DCAE VES Event Listener.

    Note: HTTP is allowed but not recommended.

.. req::
    :id: R-686466
    :target: PNF
    :keyword: MUST
    :introduced: casablanca

    The PNF **MUST** support sending a pnfRegistration VES event.

.. req::
    :id: R-980039
    :target: PNF
    :keyword: MUST
    :introduced: casablanca

    The PNF **MUST** send the pnfRegistration VES event periodically.

.. req::
    :id: R-981585
    :target: PNF
    :keyword: MUST
    :introduced: casablanca

    The pnfRegistration VES event periodicity **MUST** be configurable.

    Note: The PNF uses the service configuration request as a semaphore to
    stop sending the pnfRegistration sent. See the requirement PNP-5360
    requirement.

.. req::
    :id: R-284934
    :target: PNF
    :keyword: MUST
    :introduced: casablanca

    If the PNF encounters an error authenticating, reaching the ONAP DCAE VES
    Event listener or recieves an error response from sending the pnfRegistration
    VES Event, it **MAY** log the error, and notify the operator.

    Note: the design of how errors are logged, retrieved and reported
    will be a vendor-specific architecture. Reporting faults and errors
    is also a vendor specific design. It is expected that the PNF shall
    have a means to log an error and notify a user when a fault condition
    occurs in trying to contact ONAP, authenticate or send a pnfRegistration
    event.

.. req::
    :id: R-256347
    :target: PNF
    :keyword: MUST
    :introduced: casablanca
    :updated: dublin

    The PNF **MUST** support one of the protocols for a Service Configuration
    message exchange between the PNF and PNF Controller (in ONAP):
    a) Netconf/YANG, b) Chef, or c) Ansible.

    Note: The PNF Controller may be VF-C, APP-C or SDN-C based on the
    PNF and PNF domain.

.. req::
    :id: R-707977
    :target: PNF
    :keyword: MUST
    :introduced: casablanca

    When the PNF receives a Service configuration from ONAP, the PNF **MUST**
    cease sending the pnfRegistration VES Event.

.. req::
    :id: R-17624
    :target: PNF
    :keyword: MAY
    :introduced: casablanca

    The PNF **MAY** support the optional parameters for Service
    Configuration Parameters.

    Note: These are detailed in the Stage 5 PnP

    Note: These parameters are optional, and not all PNFs will support any
    or all of these parameters, it is up to the vendor and service provider
    to ascertain which ones are supported up to an including all of the ones
    that have been defined. Note: It is expected that there will be a growing
    list of supported configuration parameters in future releases of ONAP.

.. req::
    :id: R-378131
    :target: PNF
    :keyword: MAY
    :introduced: casablanca

    (Error Case) - If an error is encountered by the PNF during a
    Service Configuration exchange with ONAP, the PNF **MAY** log the
    error and notify an operator.

.. req::
    :id: R-638216
    :target: PNF
    :keyword: MUST
    :introduced: casablanca

    (Error Case) - The PNF **MUST** support a configurable timer to stop the
    periodicity sending of the pnfRegistration VES event. If this timer expires
    during a Service Configuration exchange between the PNF and ONAP, it
    MAY log a time-out error and notify an operator.

    Note: It is expected that each vendor will enforce and define a PNF
    service configuration timeout period. This is because the PNF cannot
    wait indefinitely as there may also be a technician on-site trying to
    complete installation & commissioning. The management of the VES event
    exchange is also a requirement on the PNF to be developed by the PNF
    vendor.

