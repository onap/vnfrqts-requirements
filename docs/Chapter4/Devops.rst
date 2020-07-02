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


VNF Devops
----------

This section includes guidelines for VNF providers to ensure that a Network
Cloud Service Provider’s operations personnel have a common and
consistent way to support VNFs and VNFCs.

NCSPs may elect to support standard images to enable compliance with
security, audit, regulatory and other needs. As part of the overall VNF
software bundle, VNF suppliers using standard images would typically
provide the NCSP with an install package consistent with the default OS
package manager (e.g. aptitude for Ubuntu, yum for Redhat/CentOS).

Section 4.5 DevOps in *VNF Guidelines* describes
the DevOps guidelines for VNFs.

DevOps Requirements


.. req::
    :id: R-46960
    :target: VNF
    :keyword: MAY

    NCSPs **MAY** operate a limited set of Guest OS and CPU
    architectures and families, virtual machines, etc.

.. req::
    :id: R-23475
    :target: VNF
    :keyword: SHOULD

    VNFCs **SHOULD** be agnostic to the details of the Network Cloud
    (such as hardware, host OS, Hypervisor or container technology) and must run
    on the Network Cloud with acknowledgement to the paradigm that the Network
    Cloud will continue to rapidly evolve and the underlying components of
    the platform will change regularly.

.. req::
    :id: R-33846
    :target: VNF
    :keyword: MUST

    The VNF **MUST** install the NCSP required software on Guest OS
    images when not using the NCSP provided Guest OS images. [#4.5.1]_

.. req::
    :id: R-09467
    :target: VNF
    :keyword: MUST

    The VNF **MUST** utilize only NCSP standard compute flavors. [#4.5.1]_

.. req::
    :id: R-02997
    :target: VNF
    :keyword: MUST

    The VNF **MUST** preserve their persistent data. Running VMs
    will not be backed up in the Network Cloud infrastructure.

.. req::
    :id: R-29760
    :target: VNF
    :keyword: MUST

    The VNFC **MUST** be installed on non-root file systems,
    unless software is specifically included with the operating system
    distribution of the guest image.

.. req::
    :id: R-20860
    :target: VNF
    :keyword: MUST

    The VNF **MUST** be agnostic to the underlying infrastructure
    (such as hardware, host OS, Hypervisor), any requirements should be
    provided as specification to be fulfilled by any hardware.

.. req::
    :id: R-89800
    :target: VNF
    :keyword: MUST NOT

    The VNF **MUST NOT** require Hypervisor-level customization
    from the cloud provider.

.. req::
    :id: R-86758
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** provide an automated test suite to validate
    every new version of the software on the target environment(s). The tests
    should be of sufficient granularity to independently test various
    representative VNF use cases throughout its lifecycle. Operations might
    choose to invoke these tests either on a scheduled basis or on demand to
    support various operations functions including test, turn-up and
    troubleshooting.

.. req::
    :id: R-39650
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** provide the ability to test incremental
    growth of the VNF.

.. req::
    :id: R-14853
    :target: VNF
    :keyword: MUST

    The VNF **MUST** respond to a "move traffic" [#4.5.2]_ command
    against a specific VNFC, moving all existing session elsewhere with
    minimal disruption if a VNF provides a load balancing function across
    multiple instances of its VNFCs.

    Note: Individual VNF performance aspects (e.g., move duration or
    disruption scope) may require further constraints.

.. req::
    :id: R-06327
    :target: VNF
    :keyword: MUST

    The VNF **MUST** respond to a "drain VNFC" [#4.5.2]_ command against
    a specific VNFC, preventing new session from reaching the targeted VNFC,
    with no disruption to active sessions on the impacted VNFC, if a VNF
    provides a load balancing function across multiple instances of its VNFCs.
    This is used to support scenarios such as proactive maintenance with no
    user impact.

.. req::
    :id: R-64713
    :target: VNF
    :keyword: SHOULD

    The VNF **SHOULD** support a software promotion methodology
    from dev/test -> pre-prod -> production in software, development &
    testing and operations.


.. [#4.5.1]
   Refer to NCSP’s Network Cloud specification

.. [#4.5.2]
   Not currently supported in ONAP release 1


