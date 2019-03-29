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

VNFRQTS Project Release Notes
==============================

Version: 3.0.1
--------------

:Release Date: 2019-1-30

**New Features**
    - No new features added during Casablanca Maintenance release

**Bug Fixes**
    - Fixed typos
    - Fixed metadata errors

**Known Issues**
    - Links that refer to "latest" version are static.  Please report
      any broken links.

**Security Issues**
    - None

**Upgrade Notes**
    - If you would like to add requirements, you **MUST** follow
      `instructions on Wiki <https://wiki.onap.org/display/DW/VNFRQTS+How+to+Contribute>`__.

**Deprecation Notes**
    - None

**Other**
    - None


Version: 3.0.0
--------------

:Release Date: 2018-11-30

A detailed summary of all requirement changes per section can be found
:doc:`here <changes-by-section-casablanca>`.

A higher level summary of changes as well as non-requirement impacting
changes can be found below.

**New Features**
    - Updated the Security requirements in Chapter 4 (Added, Removed, Reworded,
      or Moved)
    - Created new cybersecurity section in Chapter 4
    - Changed the theme of the documents
    - Moved Requirements list from Chapter 8 to Chapter 9
    - Added a downloadable, dynamic JSON of all requirements, separated by
      versions.  This is available on the Requirements List page.
    - Updated the hierarchy and moved the VNF Requirements to a higher level in
      the doc project
    - Updated and created new wiki material on how to contribute
    - Created enumerated requirements for TOSCA
    - Updated Heat requirements
    - Created new section for PNF Plug-and-Play with associated requirements
    - Updated Management requirements
    - Updated section for VES support
    - Introduced new directive for requirements to use metadata
    - Update test description annex

**Bug Fixes**
    - Fixed typos
    - Fixed broken links
    - Fixing formatting in examples to print properly
    - Fixed formatting of tables

**Known Issues**
    - Links that refer to "latest" version are static.  Please report
      any broken links.

**Security Issues**
    - None

**Upgrade Notes**
    - If you would like to add requirements, you **MUST** follow
      `instructions on Wiki <https://wiki.onap.org/display/DW/VNFRQTS+How+to+Contribute>`__.

**Deprecation Notes**
    - None

**Other**
    - None

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

    - This initial releases is based on seed documents that came from Open-O
      and Open ECOMP. For details, refer
      `Seed Document Mappings to VNFRQTS Deliverable Outlines <https://wiki.onap.org/display/DW/Seed+Document+Mappings+to+VNFRQTS+Deliverable+Outlines>`_.

    - This release provides a consolidated list of requirements as prototype
      text for RFPs to acquire VNFs to run in an ONAP context. The
      requirements are uniquely numbered and in a consistent format.

**Bug Fixes**
    - None

**Known Issues**
    - `VNFRQTS-83 Chapter 5, Section B Requirements <https://jira.onap.org/browse/VNFRQTS-83>`__.

    - Heat requirements have not been formatted into the standard
      format used throughout the document.

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
