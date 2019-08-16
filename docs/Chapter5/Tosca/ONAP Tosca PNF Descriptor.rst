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


TOSCA PNF Descriptor
--------------------


General
^^^^^^^

.. req::
    :id: R-24632
    :target: PNF
    :keyword: MUST
    :introduced: dublin

    The PNF Descriptor (PNFD) provided by PNF vendor **MUST** comply with
    TOSCA/YAML based Service template for PNF descriptor specified in ETSI
    NFV-SOL001.


Data Types
^^^^^^^^^^^^^^

.. req::
    :id: R-484843
    :target: PNF
    :keyword: MUST
    :introduced: dublin

    The PNFD provided by a PNF vendor **MUST** comply with the following Data
    Types as specified in ETSI NFV-SOL001 standard:

      - tosca.datatypes.nfv.CpProtocolData

      - tosca.datatypes.nfv.AddressData

      - tosca.datatypes.nfv.L2AddressData

      - tosca.datatypes.nfv.L3AddressData

      - tosca.datatypes.nfv.LocationInfo

      - tosca.datatypes.nfv.CivicAddressElement


Artifact Types
^^^^^^^^^^^^^^

No artifact type is currently supported in ONAP.


Capability Types
^^^^^^^^^^^^^^^^^^^^^

.. req::
    :id: R-177937
    :target: PNF
    :keyword: MUST
    :introduced: dublin

    The PNFD provided by a PNF vendor **MUST** comply with the following
    Capabilities Types as specified in ETSI NFV-SOL001 standard:

      - tosca.datatypes.nfv.VirtualLinkable


Requirements Types
^^^^^^^^^^^^^^^^^^^^^


Relationship Types
^^^^^^^^^^^^^^^^^^^^^

.. req::
    :id: R-64064
    :target: PNF
    :keyword: MUST
    :introduced: dublin

    The PNFD provided by a PNF vendor **MUST** comply with the following
    Relationship Types as specified in ETSI NFV-SOL001 standard:

      - tosca.datatypes.nfv.VirtualLinksTo


Interface Types
^^^^^^^^^^^^^^^^^^^^^

No interface type is currently supported in ONAP.


Node Types
^^^^^^^^^^^^^^

.. req::
    :id: R-535009
    :target: PNF
    :keyword: MUST
    :introduced: dublin

    The PNFD provided by a PNF vendor **MUST** comply with the following Node
    Types as specified in ETSI NFV-SOL001 standard:

      - tosca.nodes.nfv.PNF

      - tosca.nodes.nfv.PnfExtCp

      - tosca.nodes.nfv.Cp



Group Types
^^^^^^^^^^^^^^

No group type is currently supported in ONAP.


Policy Types
^^^^^^^^^^^^^^

.. req::
    :id: R-596064
    :target: PNF
    :keyword: MUST
    :introduced: dublin

    The PNFD provided by a PNF vendor **MUST** comply with the following Policy
    Types as specified in ETSI NFV-SOL001 standard:

      - tosca.datatypes.nfv.SecurityGroupRule
