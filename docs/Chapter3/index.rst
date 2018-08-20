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


Introduction
============

- Requirements are identified as either MUST, MUST NOT, SHOULD, SHOULD NOT,
  or MAY as defined in RFC 2119.
- Requirements should be targeted to a restricted set of nouns related
  to VNFs and within the control of the VNF provider. The current list
  of VNF Requirement targets is:

    - The VNF
    - The VNFC
    - The VNF Provider
    - The VNF Heat Orchestration Template
    - The VNF Package
- Chapter 4 contains the xNF requirements involving the design and
  development of xNFs. These requirements help VNFs/PNFs operate
  efficiently within a cloud environment. Requirements cover design,
  resiliency, security, modularity and DevOps.
- Chapter 5 describes the different data models the xNF provider
  needs to understand.  There are currently 2 models described in this
  document:

    - The first model is the onboarding package data model. This is a TOSCA
      model that will describe how all the elements passed from the VNF/PNF
      Provider to the Service provider should be formatted and packaged.
    - The second model is HEAT template used for orchestrating and
      instantiating virtual resources in an OpenStack environment.  At this
      time the HEAT files will be passed to the Service provider as a data
      element within the TOSCA onboarding package.
- Chapter 6 details the requirements specific to an implementation.
  The current implementations documented are OpenStack and Azure.
- Chapter 7 provides the comprehensive set of requirements for xNFs to
  be on-boarded, configured and managed by ONAP.
- Chapter 8 is the appendix that provide a number of detailed data record
  formats. It also contains a list of the requirements that are listed
  in the other chapters as well as examples and models that are referenced
  throughout the rest of the chapters.
