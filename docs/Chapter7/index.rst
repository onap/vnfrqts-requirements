.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

ONAP Management Requirements
============================

.. toctree::
    :maxdepth: 2

    Service-Design
    VNF-On-boarding-and-package-management
    Configuration-Management
    Monitoring-And-Management


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
  "The xNF MUST/SHOULD/..."
* Requirements that only apply to VNFs are defined as "The VNF MUST/SHOULD/..."
* Requirements that only apply to PNFs are defined as "The PNF MUST/SHOULD/..."


.. [1]
   https://github.com/mbj4668/pyang

.. [2]
   Recall that the Node Object **is required** to be identical across
   all VMs of a VNF invoked as part of the action except for the “name”.

.. [3]
   Upstream elements must provide the appropriate FQDN in the request to
   ONAP for the desired action.

.. [4]
   Multiple ONAP actions may map to one playbook.

.. [5]
   This option is not currently supported in ONAP and it is currently
   under consideration.

.. |image0| image:: Data_Model_For_Event_Records.png
      :width: 7in
      :height: 8in


.. |image1| image:: VES_JSON_Driven_Model.png
      :width: 5in
      :height: 3in

.. |image2| image:: YANG_Driven_Model.png
      :width: 5in
      :height: 3in

.. |image3| image:: Protocol_Buffers_Driven_Model.png
      :width: 4.74in
      :height: 3.3in
