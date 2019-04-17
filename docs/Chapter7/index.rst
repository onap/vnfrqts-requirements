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

.. _onap_management_requirements:

ONAP Management Requirements
============================

.. toctree::
    :maxdepth: 2

    Service-Design
    VNF-On-boarding-and-package-management
    Configuration-Management
    Monitoring-And-Management
    PNF-Plug-and-Play


The ONAP platform is the part of the larger Network Function
Virtualization/Software Defined Network (NFV/SDN) ecosystem that
is responsible for the efficient control, operation and management
of Virtual Network Function (VNF) capabilities and functions. It
specifies standardized abstractions and interfaces that enable
efficient interoperation of the NVF/SDN ecosystem components. It
enables product/service independent capabilities for design, creation
and runtime lifecycle management (includes all aspects of installation,
change management, assurance, and retirement) of resources in NFV/SDN
environment (see ECOMP white paper ). These capabilities are provided
using two major architectural frameworks: (1) a Design Time Framework
to design, define and program the platform (uniform onboarding), and
(2) a Runtime Execution Framework to execute the logic programmed in
the design environment (uniform delivery and runtime lifecycle
management). The platform delivers an integrated information model
based on the VNF package to express the characteristics and behavior
of these resources in the Design Time Framework. The information model
is utilized by Runtime Execution Framework to manage the runtime
lifecycle of the VNFs. The management processes are orchestrated
across various modules of ONAP to instantiate, configure, scale,
monitor, and reconfigure the VNFs using a set of standard APIs
provided by the VNF developers.

Although the guidelines and requirements specified in this document
were originally driven by the need to standardize and automate the
management of the virtualized environments (with VNFs) operated by
Service Providers, we believe that most of the requirements are equally
applicable to the operation of the physical network functions (PNFs),
those network functions provided by traditional physical network
elements (e.g. whitebox switches) or customized peripherals (e.g. a
video rendering engine for augmented reality). The primary area of
difference will be in how the network function is orchestrated into
place – VNFs can be much more dynamically created & placed by ONAP
to support varying geographic, availability and scalability needs,
whereas the PNFs have to be deployed a priori in specific locations
based on planning and engineering – their availability and scalability
will be determined by the capabilities offered by the PNFs.

**PNF** is a vendor-provided Network Function(s) implemented using a
bundled set of hardware and software while VNFs utilize cloud resources
to provide Network Functions through virtualized software modules.  PNF
can be supplied by a vendor as a Black BOX (provides no knowledge of its
internal characteristics, logic, and software design/architecture) or as
a White Box (provides detailed knowledge and access of its internal
components and logic) or as a Grey Box (provides limited knowledge and
access to its internal components).

* Requirements that equally apply to both VNFs and PNFs are defined as
  "The VNF or PNF MUST/SHOULD/..."
* Requirements that only apply to VNFs are defined as "The VNF MUST/SHOULD/..."
* Requirements that only apply to PNFs are defined as "The PNF MUST/SHOULD/..."
