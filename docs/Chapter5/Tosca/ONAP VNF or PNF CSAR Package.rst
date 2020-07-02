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


VNF or PNF CSAR Package
-----------------------

CSAR Overview
^^^^^^^^^^^^^

TOSCA YAML CSAR file is an archive file using the ZIP file format whose
structure complies with the TOSCA Simple Profile YAML v1.2 Specification.
The CSAR file may have one of the two following structures:

  - CSAR containing a TOSCA-Metadata directory, which includes the TOSCA.meta
    metadata file providing an entry information for processing a CSAR file.

  - CSAR containing a single yaml (.yml or .yaml) file at the root of the
    archive. The yaml file is a TOSCA definition template that contains a
    metadata section with template_name and template_version metadata. This
    file is the CSAR Entry-Definitions file.

VNF or PNF Package Structure and Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. req::
    :id: R-51347
    :target: VNF or PNF CSAR PACKAGE
    :keyword: MUST
    :introduced: casablanca
    :updated: frankfurt

    The VNF or PNF CSAR package **MUST** be arranged as a CSAR archive as
    specified in TOSCA Simple Profile in YAML 1.2.


.. req::
    :id: R-87234
    :target: VNF or PNF CSAR PACKAGE
    :keyword: MUST
    :introduced: casablanca
    :updated: frankfurt

    The VNF or PNF CSAR package provided by a VNF or PNF vendor **MUST** be with
    TOSCA-Metadata directory (CSAR Option 1) as specified in
    ETSI GS NFV-SOL004.

    **Note:** SDC supports only the CSAR Option 1 in Dublin. The Option 2
    will be considered in future ONAP releases.

.. req::
    :id: R-506221
    :target: VNF or PNF CSAR PACKAGE
    :keyword: MUST
    :introduced: dublin
    :updated: frankfurt

    The VNF or PNF CSAR file **MUST** be a zip file with .csar extension.


VNF or PNF Package Contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. req::
    :id: R-10087
    :target: VNF or PNF CSAR PACKAGE
    :keyword: MUST
    :introduced: casablanca
    :updated: dublin

    The VNF or PNF CSAR package **MUST** include all artifacts required by
    ETSI GS NFV-SOL004 including Manifest file, VNFD or PNFD (or Main
    TOSCA/YAML based Service Template) and other optional artifacts.

.. req::
    :id: R-01123
    :target: VNF or PNF CSAR PACKAGE
    :keyword: MUST
    :introduced: casablanca
    :updated: frankfurt

    The VNF or PNF CSAR package Manifest file **MUST** contain: VNF or PNF
    package meta-data, a list of all artifacts (both internal and
    external) entry's including their respected URI's, as specified
    in ETSI GS NFV-SOL 004

.. req::
    :id: R-21322
    :target: VNF CSAR PACKAGE
    :keyword: MUST
    :introduced: casablanca
    :updated: frankfurt

    The VNF provider **MUST** provide their testing scripts to support
    testing as specified in ETSI NFV-SOL004 - Testing directory in CSAR

.. req::
    :id: R-40820
    :target: VNF CSAR PACKAGE
    :keyword: MUST
    :introduced: casablanca
    :updated: guilin

    The VNF CSAR PACKAGE **MUST** enumerate all of the open source
    licenses their VNF(s) incorporate. CSAR License directory as per ETSI
    SOL004.

    for example ROOT\\Licenses\\ **License_term.txt**

.. req::
    :id: R-293901
    :target: VNF or PNF CSAR PACKAGE
    :keyword: MUST
    :introduced: dublin

    The VNF or PNF CSAR PACKAGE with TOSCA-Metadata **MUST** include following
    additional keywords pointing to TOSCA files:

      - ETSI-Entry-Manifest

      - ETSI-Entry-Change-Log

    Note: For a CSAR containing a TOSCA-Metadata directory, which includes
    the TOSCA.meta metadata file. The TOSCA.meta metadata file includes block_0
    with the Entry-Definitions keyword pointing to a TOSCA definitions YAML
    file used as entry for parsing the contents of the overall CSAR archive.

.. req::
    :id: R-146092
    :target: VNF or PNF CSAR PACKAGE
    :keyword: MUST
    :introduced: dublin
    :updated: frankfurt

    If one or more non-MANO artifact(s) is included in the VNF or PNF CSAR
    package, the Manifest file in this CSAR package **MUST** contain one or more
    of the following ONAP non-MANO artifact set identifier(s):

      - onap_ves_events: contains VES registration files

      - onap_pm_dictionary: contains the PM dictionary files

      - onap_yang_modules: contains Yang module files for configurations

      - onap_ansible_playbooks: contains any ansible_playbooks

      - onap_pnf_sw_information: contains the PNF software information file

      - onap_others: contains any other non_MANO artifacts, e.g. informational
        documents

     *NOTE: According to ETSI SOL004 v.2.6.1, every non-MANO artifact set shall be
     identified by a non-MANO artifact set identifier which shall be registered in
     the ETSI registry. Approved ONAP non-MANO artifact set identifiers are documented
     in the following page* https://wiki.onap.org/display/DW/ONAP+Non-MANO+Artifacts+Set+Identifiers

.. req::
    :id: R-221914
    :target: VNF or PNF CSAR PACKAGE
    :keyword: MUST
    :introduced: dublin
    :updated: frankfurt

    The VNF or PNF CSAR package **MUST** contain a human-readable change log text
    file. The Change Log file keeps a history describing any changes in the VNF
    or PNF package. The Change Log file is kept up to date continuously from
    the creation of the CSAR package.

.. req::
    :id: R-57019
    :target: PNF CSAR PACKAGE
    :keyword: MUST
    :introduced: dublin
    :updated: frankfurt

    The PNF CSAR PACKAGE Manifest file **MUST** start with the PNF
    package metadata in the form of a name-value pairs. Each pair shall appear
    on a different line. The name is specified as following:

      - pnfd_provider

      - pnfd_name

      - pnfd_release_date_time

      - pnfd_archive_version

.. req::
    :id: R-795126
    :target: VNF CSAR PACKAGE
    :keyword: MUST
    :introduced: dublin
    :updated: frankfurt

    The VNF CSAR package Manifest file **MUST** start with the VNF
    package metadata in the form of a name-value pairs. Each pair shall appear
    on a different line. The name is specified as following:

      - vnf_provider_id

      - vnf_product_name

      - vnf_release_date_time

      - vnf_package_version

.. req::
    :id: R-972082
    :target: PNF CSAR PACKAGE
    :keyword: MUST
    :introduced: frankfurt

    If the Manifest file in the PNF CSAR package includes "onap_pnf_sw_information"
    as a non-MANO artifact set identifiers, then the PNF software information file is
    included in the package and it **MUST** be compliant to:

    - The file extension which contains the PNF software version must be .yaml

    - The PNF software version information must be specified as following:

    .. code-block:: yaml

       pnf_software_information:

        - pnf_software_version:  "<version>"



VNF or PNF Package Authenticity and Integrity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

VNF or PNF CSAR package shall support a method for authenticity and integrity
assurance. According to ETSI SOL004 the onboarding package shall be secured.
ETSI SOL004 provides two options:

Option 1 - One Digest for each components of the VNF or PNF package. The table
of hashes is included in the manifest file, which is signed with the VNF or PNF
provider private key. A signing certificate including the provider’s public key
shall be included in the package.

Option 2 - The complete CSAR file shall be digitally signed with the provider
private key. The provider delivers one zip file consisting of the CSAR file, a
signature file and a certificate file that includes the VNF provider public
key.

*Dublin release note*

    - VNFSDK pre-onboarding validation procedure:
      - Option 1: specified in ETSI SOL004 is supported.
      - Option 2: Will be supported in the future releases.

    - SDC onboarding procedure:
      - Option 1: Will be supported in the future releases.
      - Option 2: specified in ETSI SOL004 is supported.

.. req::
    :id: R-787965
    :target: VNF or PNF CSAR PACKAGE
    :keyword: MUST
    :introduced: dublin

    If the VNF or PNF CSAR Package utilizes Option 2 for package security, then
    the complete CSAR file **MUST** be digitally signed with the VNF or PNF
    provider private key. The VNF or PNF provider delivers one zip file
    consisting of the CSAR file, a signature file and a certificate file that
    includes the VNF or PNF provider public key. The certificate may also be
    included in the signature container, if the signature format allows that.
    The VNF or PNF provider creates a zip file consisting of the CSAR file with
    .csar extension, signature and certificate files. The signature and
    certificate files must be siblings of the CSAR file with extensions .cms
    and .cert respectively.


.. req::
    :id: R-130206
    :target: VNF or PNF CSAR PACKAGE
    :keyword: MUST
    :introduced: dublin
    :updated: el alto

    If the VNF or PNF CSAR Package utilizes Option 1 for package security, then
    the complete CSAR file **MUST** contain a Digest (a.k.a. hash) for each of
    the components of the VNF or PNF package. The table of hashes is included
    in the package manifest file, which is signed with the VNF or PNF provider
    private key. In addition, the VNF or PNF provider MUST include a signing
    certificate that includes the VNF or PNF provider public key, following a
    TOSCA pre-defined naming convention and located either at the root of the
    archive or in a predefined location specified by the TOSCA.meta file with
    the corresponding entry named "ETSI-Entry-Certificate".


VNF Package ONAP Extensions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. TOSCA data type extension tosca.datatypes.nfv.injectFile is used for vCPE
   use case.
2. ONAP extensions for VNF package that is currently proposed for Dublin
   release is VES extension described below.
