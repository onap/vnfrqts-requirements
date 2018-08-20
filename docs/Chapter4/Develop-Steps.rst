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


VNF Develop Steps
-----------------

Aid to help the VNF provider to fasten the integration with the GVNFM, the
ONAP provides the VNF SDK tools, and the documents. In this charter,
the develop steps for VNF providers will be introduced.

First, using the VNF SDK tools to design the VNF with TOSCA model and
output the VNF TOSCA package. The VNF package can be validated, and
tested.

Second, the VNF provider should provide the VNF Rest API to integrate with
the GVNFM if needed. The VNF Rest API is aligned to the ETSI IFA
document.

Third, the TOSCA model supports the HPA feature.

Note:

1. The scripts to extend capacity to satisfy some special requirements.
   In the R2, the scripts is not implemented fully, and will be provided
   in the next release.

2. The monitoring and scale policy also be provide the next release.
