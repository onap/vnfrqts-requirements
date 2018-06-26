.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.


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
