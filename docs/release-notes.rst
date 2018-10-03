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


VNF Requirements Release Notes
==============================

Version: 3.0.0
--------------

:Release Date: In Progress (Casablanca Release)

**New Features**
    - Added R-17528 to Heat section regarding Nested YAML requirements

**Bug Fixes**

**Known Issues**

**Security Issues**
    - None

**Upgrade Notes**

**Deprecation Notes**

**Other**

Version: 2.0.0
--------------

:Release Date: 2018-06-07 (Beijing Release)

**New Features**
    - Chapter 5 Requirements changed from test to numbered requirements.

        -https://jira.onap.org/browse/VNFRQTS-83

    - Chapter Header re-structured to help readability of documents.

        - https://jira.onap.org/browse/VNFRQTS-130
        - https://wiki.onap.org/display/DW/VNF+Requirement+Updated+Header+Structure

    - Changed language to take into consider PNF (xNF).

        - https://jira.onap.org/browse/VNFRQTS-188
        - https://jira.onap.org/browse/VNFRQTS-189

    - Added copyright License Header in all source files

        - https://jira.onap.org/browse/VNFRQTS-180

**Bug Fixes**
    - Fixed Chapter Header Structure warnings.

        - https://jira.onap.org/browse/VNFRQTS-193

    - Found table in Chapter 8 section C.2 that was not printing,
      corrected format.

        - https://jira.onap.org/browse/VNFRQTS-192

    - Fixes for language within requirements from clarification/grammar.

        - The full list of changes made to requirements  is available on `JIRA <https://jira.onap.org/projects/VNFRQTS/issues>`_

**Known Issues**
    - Need to review requirements that have bullet points as well as paragraphs to meet guidelines listed on `VNFRQTS <https://wiki.onap.org/display/DW/VNFRQTS+Requirement+Format+discussion>`_

        - https://jira.onap.org/browse/VNFRQTS-195

**Security Issues**
    - None

**Upgrade Notes**
    - Requirements will still need to go and be updated in multiple
      locations, but there is an upgrade proposal to handle this.

**Deprecation Notes**
    - Chapter numbers will no longer be used, numbers for chapters
      will be assigned dynamically based off of the header structure in rst.

        - More information on the new header structure is available on `Headers <https://wiki.onap.org/display/DW/VNF+Requirement+Updated+Header+Structure>`_

**Other**
    NA

Version: 1.0.0
--------------

:Release Date: 2017-11-16 (Amsterdam Release)

**New Features**

    - Initial release of VNF Provider Guidelines and Requirements for
      Open Network Automation Platform (ONAP)

    - This intitial releases is based on seed documents that came from Open-O and Open ECOMP. For details, refer `Seed Document Mappings to VNFRQTS Deliverable Outlines <https://wiki.onap.org/display/DW/Seed+Document+Mappings+to+VNFRQTS+Deliverable+Outlines>`_.

    - This release provides a consolidated list of requirements as prototype
      text for RFPs to acquire VNFs to run in an ONAP context. The
      requirements are uniquely numbered and in a consistent format.

**Bug Fixes**
    - None

**Known Issues**
    - `VNFRQTS-83 Chapter 5, Section B Requirements <https://jira.onap.org/browse/VNFRQTS-83>`_.

    - Heat requirments have not been formatted into the standard
      format used througout the document.

    - Therefore they are not included in the summary of requirements
      listed in Appendix 8.d.

    - These requirements can be found by searching for the keywords must,
      should in the sections of the document that discuss Heat.

**Security Issues**
    - No known security issues.

**Upgrade Notes**
    - Initial release - none

**Deprecation Notes**
    - Initial release - none

**Other**
    NA

===========

End of Release Notes

