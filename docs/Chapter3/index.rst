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
  to VNFs or PNFs and within the control of the VNF or PNF provider. The
  current list of VNF or PNF Requirement targets is:

+---------------------+-------------------------------------------------------+
| Target              | When is it used                                       |
+=====================+=======================================================+
| VNF                 | Functional behavior of a VNF                          |
+---------------------+-------------------------------------------------------+
| PNF                 | Functional behavior of a PNF                          |
+---------------------+-------------------------------------------------------+
| VNF or PNF          | Function behavior to both VNFs and PNFs               |
+---------------------+-------------------------------------------------------+
| {VNF|PNF|VNF or PNF}| Something the provider of the VNF, PNF, or VNF/PNF    |
| PROVIDER            | must do. This is often used to describe delivering    |
|                     | artifacts or specific documentation that may not be   |
|                     | part of a standard VNF package format.                |
+---------------------+-------------------------------------------------------+
| VNF HEAT PACKAGE    | The archive/zip file that includes Heat templates. The|
|                     | subject of the requirement my be further refined (Ex: |
|                     | Heat Environment File), but the metadata stay at the  |
|                     | package level.                                        |
+---------------------+-------------------------------------------------------+
| {VNF|PNF|VNF or PNF}| A requirement related to the contents of what should  |
| CSAR PACKAGE        | be in the CSAR package. The subject of the requirement|
|                     | might be further refined (ex: CSAR manifest file, VNF |
|                     | Descriptor, etc.), but the :target: metadata would    |
|                     | stay at the package level.                            |
+---------------------+-------------------------------------------------------+
| {VNF|PNF|VNF or PNF}| VNFs and PNFs are expected to provide human readable  |
| DOCUMENTATION       | documentation. This may come in the form of URLs or   |
| PACKAGE             | pdfs. This documentation may vary by VNF or PNF.      |
|                     | The structure of the documentation is intended for    |
|                     | human consumption and is not highly structured for    |
|                     | machine ingestion. The human readable documentation   |
|                     | may be provided through the RFP/acquisition process.  |
+---------------------+-------------------------------------------------------+

- Chapter 4 contains the VNF or PNF requirements involving the design and
  development of VNFs or PNF. These requirements help VNFs or PNFs operate
  efficiently within a cloud environment. Requirements cover design,
  resiliency, security, modularity and DevOps.
- Chapter 5 describes the different data models the VNF or PNF provider
  needs to understand.  There are currently 2 models described in this
  document:

    - The first model is the onboarding package data model. This is a TOSCA
      model that will describe how all the elements passed from the VNF or PNF
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
