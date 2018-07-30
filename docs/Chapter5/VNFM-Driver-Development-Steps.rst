.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

VNFM Driver Development Steps
-----------------------------

Refer to the ONAP documentation for VNF Provider instructions on integrating
vendor-specific VNFM adaptors with VF-C.  The VNF driver development steps are
highlighted below.

1. Use the VNF SDK tools to design the VNF with TOSCA models to output
the VNF TOSCA package.  Using the VNF SDK tools, the VNF package can be
validated and tested.

2. The VNF Provider supplies a vendor-specific VNFM driver in ONAP, which
is a microservice providing a translation interface from VF-C to
the vendor-specific VNFM. The interface definitions of vendor-specific
VNFM adaptors are supplied by the VNF Providers themselves.
