.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.


**Introduction**
====================
- These requirements are specific to the Amsterdam release of ONAP.
  It is the initial release of requirements based on a merge of the Open-O
  and OpenECOMP requirements.
- Requirements are identified as either MUST, MUST NOT, SHOULD, SHOULD NOT,
  or MAY as defined in RFC 2119.
- Chapter 4 contains the VNF/PNF requirements involving the design and
  development of VNFs/PNFs. These requirements help VNFs/PNFs operate
  efficiently within a cloud environment. Requirements cover design,
  resiliency, security, modularity and DevOps.
- Chapter 5 describes the different data models the VNF/PNF provider
  needs to understand.  There are currently 2 models described in this document:

    - The first model is the onboarding package data model. This is a TOSCA
      model that will describe how all the elements passed from the VNF/PNF
      Provider to the Service provider should be formatted and packaged.
    - The second model is HEAT template used for orchestrating and
      instantiating virtual resources in an OpenStack environment.  At this
      time the HEAT files will be passed to the Service provider as a data
      element within the TOSCA onboarding package.
- Chapter 6 details the requirements specific to an implementation.
  The current implementations documented are OpenStack and Azure.
- Chapter 7 provides the comprehensive set of requirements for VNFs/PNFs to
  be on-boarded, configured and managed by ONAP.
- Chapter 8 is the appendix that provide a number of detailed data record
  formats.

