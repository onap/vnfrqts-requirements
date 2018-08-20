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
