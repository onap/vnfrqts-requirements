.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

VNF Design
----------

Services are composed of VNFs and common components and are designed to
be agnostic of the location to leverage capacity where it exists in the
Network Cloud. VNFs can be instantiated in any location that meets the
performance and latency requirements of the service.

A key design principle for virtualizing services is decomposition of
network functions using NFV concepts into granular VNFs. This enables
instantiating and customizing only essential functions as needed for the
service, thereby making service delivery more nimble. It provides
flexibility of sizing and scaling and also provides flexibility with
packaging and deploying VNFs as needed for the service. It enables
grouping functions in a common cloud data center to minimize
inter-component latency. The VNFs should be designed with a goal of
being modular and reusable to enable using best-in-breed vendors.

Section 5.a VNF Design in *VNF Guidelines* describes
the overall guidelines for designing VNFs from VNF Components (VNFCs).
Below are more detailed requirements for composing VNFs.

VNF Design Requirements

* R-58421 The VNF **SHOULD** be decomposed into granular re-usable VNFCs.
* R-82223 The VNF **MUST** be decomposed if the functions have
  significantly different scaling characteristics (e.g., signaling
  versus media functions, control versus data plane functions).
* R-16496 The VNF **MUST** enable instantiating only the functionality that
  is needed for the decomposed VNF (e.g., if transcoding is not needed it
  should not be instantiated).
* R-02360 The VNFC **MUST** be designed as a standalone, executable process.
* R-34484 The VNF **SHOULD** create a single component VNF for VNFCs
  that can be used by other VNFs.
* R-23035 The VNF **MUST** be designed to scale horizontally (more
  instances of a VNF or VNFC) and not vertically (moving the existing
  instances to larger VMs or increasing the resources within a VM)
  to achieve effective utilization of cloud resources.
* R-30650 The VNF **MUST** utilize cloud provided infrastructure and
  VNFs (e.g., virtualized Local Load Balancer) as part of the VNF so
  that the cloud can manage and provide a consistent service resiliency
  and methods across all VNF's.
* R-12709 The VNFC **SHOULD** be independently deployed, configured,
  upgraded, scaled, monitored, and administered by ONAP.
* R-37692 The VNFC **MUST** provide API versioning to allow for
  independent upgrades of VNFC.
* R-86585 The VNFC **SHOULD** minimize the use of state within
  a VNFC to facilitate the movement of traffic from one instance
  to another.
* R-65134 The VNF **SHOULD** maintain state in a geographically
  redundant datastore that may, in fact, be its own VNFC.
* R-75850 The VNF **SHOULD** decouple persistent data from the VNFC
  and keep it in its own datastore that can be reached by all instances
  of the VNFC requiring the data.
* R-88199 The VNF **MUST** utilize a persistent datastore service that
  can meet the data performance/latency requirements. (For example:
  Datastore service could be a VNFC in VNF or a DBaaS in the Cloud
  execution environment)
* R-99656 The VNF **MUST** NOT terminate stable sessions if a VNFC
  instance fails.
* R-84473 The VNF **MUST** enable DPDK in the guest OS for VNF’s requiring
  high packets/sec performance.  High packet throughput is defined as greater
  than 500K packets/sec.
* R-54430 The VNF **MUST** use the NCSP’s supported library and compute
  flavor that supports DPDK to optimize network efficiency if using DPDK. [1]_
* R-18864 The VNF **MUST** NOT use technologies that bypass virtualization
  layers (such as SR-IOV) unless approved by the NCSP (e.g., if necessary
  to meet functional or performance requirements).
* R-64768 The VNF **MUST** limit the size of application data packets
  to no larger than 9000 bytes for SDN network-based tunneling when
  guest data packets are transported between tunnel endpoints that
  support guest logical networks.
* R-74481 The VNF **MUST** NOT require the use of a dynamic routing
  protocol unless necessary to meet functional requirements.


.. [1]
   Refer to NCSP’s Network Cloud specification
