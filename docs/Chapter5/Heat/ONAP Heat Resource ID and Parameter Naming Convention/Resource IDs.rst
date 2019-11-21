.. Licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

Resource IDs
------------

Requirement R-75141 states a VNF’s Heat Orchestration Template’s resource
name (i.e., <resource ID>) MUST only contain alphanumeric characters and
underscores (‘_’).*

Requirement R-16447 states a VNF’s <resource ID> MUST be unique across
all Heat Orchestration Templates and all HEAT Orchestration Template Nested
YAML files that are used to create the VNF.

As stated previously, OpenStack requires the <resource ID> to be unique
to the Heat Orchestration Template and not unique across all Heat
Orchestration Templates the compose the VNF.

Heat Orchestration Template resources are described in :ref:`resources`.

.. req::
    :id: R-54517
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: casablanca

    When a VNF's Heat Orchestration Template's resource is associated with
    a single ``{vm-type}``, the Resource ID **MUST** contain the
    ``{vm-type}``.

.. req::
    :id: R-96482
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: frankfurt

    When a VNF's Heat Orchestration Template's resource is associated
    with a single ONAP external network, the Resource ID **MUST** contain the
    text ``{network-role}``.

.. req::
    :id: R-98138
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: frankfurt

    When a VNF's Heat Orchestration Template's resource is associated with a
    single ONAP internal network (per the ONAP definition, see
    Requirements R-52425 and R-46461 and R-35666), the Resource ID **MUST**
    contain the text
    ``int_{network-role}``.

.. req::
    :id: R-82115
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: frankfurt

    When a VNF's Heat Orchestration Template's resource is associated with a
    single ``{vm-type}``
    and a single ONAP
    external network, the Resource ID text **MUST** contain both
    the ``{vm-type}``
    and the ``{network-role}``

    - the ``{vm-type}`` **MUST** appear before the ``{network-role}`` and
      **MUST** be separated by an underscore '_'


      - e.g., ``{vm-type}_{network-role}``, ``{vm-type}_{index}_{network-role}``


    - note that an ``{index}`` value **MAY** separate the ``{vm-type}`` and the
      ``{network-role}`` and when this occurs underscores **MUST** separate the
      three values.  (e.g., ``{vm-type}_{index}_{network-role}``).

.. req::
    :id: R-82551
    :target: VNF
    :keyword: MUST
    :validation_mode: none
    :updated: frankfurt

    When a VNF's Heat Orchestration Template's resource is associated with a
    single ``{vm-type}`` and a single ONAP internal network (per the ONAP
    definition, see Requirements R-52425 and R-46461 and R-35666),
    the Resource ID **MUST**
    contain both the ``{vm-type}`` and the ``int_{network-role}`` and

    - the ``{vm-type}`` **MUST** appear before the ``int_{network-role}`` and
      **MUST** be separated by an underscore '_'

      - (e.g., ``{vm-type}_int_{network-role}``,
        ``{vm-type}_{index}_int_{network-role}``)

    - note that an ``{index}`` value **MAY** separate the
      ``{vm-type}`` and the ``int_{network-role}`` and when this occurs
      underscores **MUST** separate the three values.
      (e.g., ``{vm-type}_{index}_int_{network-role}``).

.. req::
    :id: R-67793
    :target: VNF
    :keyword: MUST NOT
    :validation_mode: none
    :updated: frankfurt

    When a VNF's Heat Orchestration Template's resource is associated
    with more than one ``{vm-type}`` and/or more than one ONAP internal network
    (per the ONAP definition, see Requirements R-52425 and R-46461 and R-35666)
    and/or
    ONAP external network (per the ONAP definition, see Requirement R-57424
    and R-16968), the Resource ID **MUST NOT** contain the
    ``{vm-type}`` and/or ``{network-role}``/``int_{network-role}``.
    It also should contain the
    term ``shared`` and/or contain text that identifies the VNF.

.. req::
    :id: R-27970
    :target: VNF
    :keyword: MAY
    :updated: frankfurt

    When a VNF's Heat Orchestration Template's resource is associated with
    more than one ``{vm-type}`` and/or more than one ONAP internal network
    (per the ONAP definition, see Requirements R-52425 and R-46461 and R-35666)
    and/or ONAP external network (per the ONAP definition, see Requirement
    R-57424 and R-16968), the Resource ID **MAY** contain the term
    ``shared`` and/or **MAY**
    contain text that identifies the VNF.

.. req::
    :id: R-11690
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: dublin

    When a VNF's Heat Orchestration Template's Resource ID contains an
    ``{index}``, the ``{index}`` is a numeric value that **MUST** start at
    zero and **MUST** increment by one.

    As stated in R-16447,
    *a VNF's <resource ID> MUST be unique across all Heat
    Orchestration Templates and all HEAT Orchestration Template
    Nested YAML files that are used to create the VNF*.  While the ``{index}``
    will start at zero in the VNF, the ``{index}`` may not start at zero
    in a given Heat Orchestration Template or HEAT Orchestration Template
    Nested YAML file.

OpenStack Heat Resources Resource ID Naming Convention
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some OpenStack Heat Resources Resource IDs
have mandatory or suggested naming conventions.  They are provided
in the following sections.

OS::Cinder::Volume
~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-87004
    :target: VNF
    :keyword: SHOULD
    :updated: dublin

    A VNF's Heat Orchestration Template's Resource
    ``OS::Cinder::Volume``
    Resource ID
    **SHOULD**
    use the naming convention

    * ``{vm-type}_volume_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{index}`` starts at zero and increments by one (as described in R-11690)

OS::Cinder::VolumeAttachment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-86497
    :target: VNF
    :keyword: SHOULD
    :updated: dublin

    A VNF's Heat Orchestration Template's Resource
    ``OS::Cinder::VolumeAttachment``
    Resource ID
    **SHOULD**
    use the naming convention

    * ``{vm-type}_volume_attachment_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{index}`` starts at zero and increments by one (as described in R-11690)

OS::Heat::CloudConfig
~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-04747
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource ``OS::Heat::CloudConfig``
    Resource ID **MUST** contain the ``{vm-type}``.

.. req::
    :id: R-20319
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource ``OS::Heat::CloudConfig``
    Resource ID **MAY** use the naming convention

    * ``{vm-type}_RCC``

    where

    * ``{vm-type}`` is the vm-type
    * ``RCC`` signifies that it is the Resource Cloud Config

OS::Heat::MultipartMime
~~~~~~~~~~~~~~~~~~~~~~~


.. req::
    :id: R-30804
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource
    ``OS::Heat::MultipartMime``
    Resource ID
    **MUST**
    contain the ``{vm-type}``.

.. req::
    :id: R-18202
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource
    ``OS::Heat::MultipartMime``
    Resource ID
    **MAY**
    use the naming convention

    * ``{vm-type}_RMM``

    where

    * ``{vm-type}`` is the vm-type
    * ``RMM`` signifies that it is the Resource Multipart Mime

OS::Heat::ResourceGroup
~~~~~~~~~~~~~~~~~~~~~~~~

There is no mandatory naming convention for
the resource 'OS::Heat::ResourceGroup'.


OS::Heat::SoftwareConfig
~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-08975
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource ``OS::Heat::SoftwareConfig``
    Resource ID **MUST** contain the ``{vm-type}``.

.. req::
    :id: R-03656
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource ``OS::Heat::SoftwareConfig``
    Resource ID **MAY** use the naming convention

    * ``{vm-type}_RSC``

    where

    * ``{vm-type}`` is the vm-type
    * ``RSC`` signifies that it is the Resource Software Config

OS::Neutron::Net
~~~~~~~~~~~~~~~~

.. req::
    :id: R-25720
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Net``
    Resource ID **MUST** use the naming convention

    * ``int_{network-role}_network``

    VNF Heat Orchestration Templates can only create ONAP internal networks
    (per the ONAP definition, see Requirements R-52425 and R-46461 and R-35666).
    There is no ``{index}`` after ``{network-role}`` because ``{network-role}``
    **MUST** be unique in the scope of the VNF's
    Heat Orchestration Template.

OS::Neutron::Port
~~~~~~~~~~~~~~~~~~


.. req::
    :id: R-20453
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    that is attaching to an ONAP external network, the ``OS::Neutron::Port``
    Resource ID
    **MUST** use the naming convention

    * ``{vm-type}_{vm-type_index}_{network-role}_port_{port-index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP external network
      that the port is attached to
    * ``{port_index}`` references the instance of the port on the ``{vm-type}``
      attached to ``{network-role}`` network.  The
      ``{port_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new port is defined on the instance of the ``{vm-type}`` attached to
      ``{network-role}`` network.

.. req::
    :id: R-26351
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    that is attaching to an ONAP internal network
    (per the ONAP definition, see Requirements R-52425 and R-46461 and R-35666),
    the `OS::Neutron::Port`` Resource ID **MUST**
    use the naming convention

    * ``{vm-type}_{vm-type_index}_int_{network-role}_port_{port-index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP internal network
      that the port is attached to
    * ``{port_index}`` references the instance of the port on the ``{vm-type}``
      attached to ``{network-role}`` network.  The
      ``{port_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new port is defined on the instance of the ``{vm-type}`` attached to
      ``{network-role}`` network.

.. req::
    :id: R-27469
    :target: VNF
    :keyword: SHOULD
    :validation_mode: none
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    that is creating a *Reserve Port* with an IPv4 address, the
    `OS::Neutron::Port`` Resource ID
    **SHOULD** use the naming convention

    * ``reserve_port_{vm-type}_{network-role}_floating_ip_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{network-role}`` is the network-role of the ONAP external network
      that the port is attached to
    * ``{index}`` is the instance of the IPv4 *Reserve Port*
      for the vm-type attached to the network of ``{network-role}``.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).


.. req::
    :id: R-68520
    :target: VNF
    :keyword: SHOULD
    :validation_mode: none
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Port``
    that is creating a *Reserve Port* with an IPv6 address, the
    ``OS::Neutron::Port`` Resource ID
    **SHOULD** use the naming convention

    * ``reserve_port_{vm-type}_{network-role}_floating_v6_ip_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{network-role}`` is the network-role of the ONAP external network
      that the port is attached to
    * ``{index}`` is the instance of the IPv6 *Reserve Port*
      for the vm-type attached to the network of ``{network-role}``.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).

OS::Neutron::SecurityGroup
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-08775
    :target: VNF
    :keyword: SHOULD
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::SecurityGroup``
    that is applicable to one ``{vm-type}`` and more than one network (internal
    and/or external), the ``OS::Neutron::SecurityGroup``
    Resource ID **SHOULD** use the naming convention

    * ``{vm-type}_security_group``

    where

    * ``{vm-type}`` is the vm-type

.. req::
    :id: R-03595
    :target: VNF
    :keyword: SHOULD
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::SecurityGroup`` that
    is applicable to more than one ``{vm-type}`` and one ONAP external network,
    the ``OS::Neutron::SecurityGroup`` Resource ID
    **SHOULD** use the naming convention

    * ``{network-role}_security_group``

    where

    * ``{network-role}`` is the network-role of the ONAP external network

.. req::
    :id: R-73213
    :target: VNF
    :keyword: SHOULD
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::SecurityGroup`` that
    is applicable to more than one ``{vm-type}`` and one ONAP internal network,
    the ``OS::Neutron::SecurityGroup`` Resource ID
    **SHOULD** use the naming convention

    * ``int_{network-role}_security_group``

    where

    * ``{network-role}`` is the network-role of the ONAP external network

.. req::
    :id: R-17334
    :target: VNF
    :keyword: SHOULD
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::SecurityGroup``
    that is applicable to one ``{vm-type}`` and one ONAP external network,
    the ``OS::Neutron::SecurityGroup`` Resource ID
    **SHOULD** use the naming convention

    * ``{vm-type}_{network-role}_security_group``

    where

    * ``{vm-type}`` is the vm-type
    * ``{network-role}`` is the network-role of the ONAP external network

.. req::
    :id: R-14198
    :target: VNF
    :keyword: SHOULD
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::SecurityGroup`` that
    is applicable to one {vm-type} and one ONAP internal network, the
    ``OS::Neutron::SecurityGroup`` Resource ID **SHOULD**
    use the naming convention

    * ``{vm-type}_int_{network-role}_security_group``

    where

    * ``{vm-type}`` is the vm-type
    * ``{network-role}`` is the network-role of the INAP internal network

.. req::
    :id: R-30005
    :target: VNF
    :keyword: MAY
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::Neutron::SecurityGroup`` that
    is applicable to more than one ``{vm-type}`` and more than one network
    (internal and/or external), the ``OS::Neutron::SecurityGroup`` Resource ID
    **MAY**
    use the naming convention

    * ``shared_security_group``

    or

    * ``{vnf-type}_security_group``

    where

    * ``{vnf-type}`` describes the VNF

OS::Neutron::Subnet
~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-59434
    :target: VNF
    :keyword: SHOULD
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource ``OS::Neutron::Subnet``
    Resource ID **SHOULD** use the naming convention

    * ``int_{network-role}_subnet_{index}``

    where

    * ``{network-role}`` is the network-role of the ONAP internal network
      (per the ONAP definition, see Requirements R-52425 and R-46461 and
      R-35666).
    * ``{index}`` is the ``{index}`` of the subnet of the ONAP internal network.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).

OS::Nova::Keypair
~~~~~~~~~~~~~~~~~

.. req::
    :id: R-24997
    :target: VNF
    :keyword: SHOULD
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource ``OS::Nova::Keypair``
    applies to one ``{vm-type}``, the ``OS::Nova::Keypair``
    Resource ID **SHOULD** use the naming convention

    * ``{vm-type}_keypair_{index}``

    where

    * ``{network-role}`` is the network-role
    * ``{index}`` is the ``{index}`` of the keypair.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).

.. req::
    :id: R-65516
    :target: VNF
    :keyword: SHOULD
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource ``OS::Nova::Keypair``
    applies to all Virtual Machines in the VNF, the
    ``OS::Nova::Keypair`` Resource ID **SHOULD** use the naming
    convention

    * ``{vnf-type}_keypair``

    where

    * ``{vnf-type}`` describes the VNF

OS::Nova::Server
~~~~~~~~~~~~~~~~

.. req::
    :id: R-29751
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: dublin

    A VNF's Heat Orchestration Template's Resource ``OS::Nova::Server``
    Resource ID
    **MUST** use the naming convention

    * ``{vm-type}_server_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{index}`` is the index.
      The ``{index}`` **MUST** starts at zero and increment by one
      as described in R-11690.

OS::Nova::ServerGroup
~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-15189
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource ``OS::Nova::ServerGroup``
    Resource ID **MAY** use the naming convention

    * ``{vm-type}_RSG``

    or

    * ``{vm-type}_Server_Grp``

    or

    * ``{vm-type}_ServerGroup``

    or

    * ``{vm-type}_servergroup``

Contrail Heat Resources Resource ID Naming Convention
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some Contrail Heat Resources Resource IDs
have mandatory or suggested naming conventions. They are provided
in the following sections.


OS::ContrailV2::InstanceIp
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-53310
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: frankfurt


    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` Resource ID
    that is configuring an IPv4 Address on a virtual machine interface
    (i.e., OS::ContrailV2::VirtualMachineInterface)
    attached to an ONAP external network
    **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_{network-role}_vmi_{vmi_index}_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP external
      network that the virtual machine interface is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    * ``IP`` signifies that an IPv4 address is being configured
    * ``{index}`` references the instance of the IPv4 address configured
      on the virtual machine interface.  The ``{index}`` is a numeric value
      that **MUST** start at zero on an
      instance of a virtual machine interface and **MUST** increment by one
      each time a new IPv4 address is configured on the
      virtual machine interface.

.. req::
    :id: R-46128
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` Resource ID
    that is configuring an IPv6 Address on a virtual machine interface
    (i.e., OS::ContrailV2::VirtualMachineInterface)
    attached to an ONAP external network
    **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_{network-role}_vmi_{vmi_index}_v6_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP external network
      that the port is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    * ``v6_IP`` signifies that an IPv6 address is being configured
    * ``{index}`` references the instance of the IPv6 address configured
      on the virtual machine interface.  The ``{index}`` is a numeric value
      that **MUST** start at zero on an
      instance of a virtual machine interface and **MUST** increment by one
      each time a new IPv6 address is configured on the
      virtual machine interface.

.. req::
    :id: R-62187
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` Resource ID
    that is configuring an IPv4 Address on a virtual machine interface
    (i.e., OS::ContrailV2::VirtualMachineInterface)
    attached to an ONAP internal network (per the ONAP definition, see
    Requirements R-52425 and R-46461 and R-35666)
    **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_int_{network-role}_vmi_{vmi_index}_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP internal network
      that the port is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    * ``IP`` signifies that an IPv4 address is being configured
    * ``{index}`` references the instance of the IPv4 address configured
      on the virtual machine interface.  The ``{index}`` is a numeric value
      that **MUST** start at zero on an
      instance of a virtual machine interface and **MUST** increment by one
      each time a new IPv4 address is configured on the
      virtual machine interface.

.. req::
    :id: R-87563
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InstanceIp`` Resource ID
    that is configuring an IPv6 Address on a virtual machine interface
    (i.e., OS::ContrailV2::VirtualMachineInterface)
    attached to an ONAP internal network (per the ONAP definition, see
    Requirements R-52425 and R-46461 and R-35666)
    **MUST** use the naming convention

    *  ``{vm-type}_{vm-type_index}_int_{network-role}_vmi_{vmi_index}_v6_IP_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP internal network
      that the port is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.
    * ``v6_IP`` signifies that an IPv6 address is being configured
    * ``{index}`` references the instance of the IPv6 address configured
      on the virtual machine interface.  The ``{index}`` is a numeric value
      that **MUST** start at zero on an
      instance of a virtual machine interface and **MUST** increment by one
      each time a new IPv6 address is configured on the
      virtual machine interface.

OS::ContrailV2::InterfaceRouteTable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-81214
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InterfaceRouteTable``
    Resource ID
    **MUST**
    contain the ``{network-role}``.

.. req::
    :id: R-28189
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::InterfaceRouteTable``
    Resource ID **MAY** use the naming convention

    * ``{network-role}_RIRT``

    where

    * ``{network-role}`` is the network-role
    * ``RIRT`` signifies that it is the Resource Interface Route Table

OS::ContrailV2::NetworkIpam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-30753
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::NetworkIpam``
    Resource ID
    **MUST**
    contain the ``{network-role}`` of the ONAP internal network that the
    resource is associated with.

.. req::
    :id: R-81979
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::NetworkIpam``
    Resource ID **MAY** use the naming convention

    * ``{network-role}_RNI``

    where

    * ``{network-role}`` is the network-role
    * ``RNI`` signifies that it is the Resource Network IPAM

OS::ContrailV2::PortTuple
~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-20065
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::PortTuple``
    Resource ID **MUST** contain the ``{vm-type}``.

.. req::
    :id: R-84457
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource ``OS::ContrailV2::PortTuple``
    Resource ID **MAY** use the naming convention

    * ``{vm-type}_RPT``

    where

    * ``{vm-type}`` is the vm-type
    * ``RPT`` signifies that it is the Resource Port Tuple

OS::ContrailV2::ServiceHealthCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-76014
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::ServiceHealthCheck``
    Resource ID
    **MUST**
    contain the ``{vm-type}``.

.. req::
    :id: R-65618
    :target: VNF
    :keyword: MAY
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::ServiceHealthCheck`` Resource ID **MAY** use the naming convention

    * ``{vm-type}_RSHC_{LEFT|RIGHT}``

    where

    * ``{vm-type}`` is the vm-type
    * ``RSHC`` signifies that it is the Resource Service Health Check
    * ``LEFT`` is used if the Service Health Check is on the left interface
    * ``RIGHT`` is used if the Service Health Check is on the right interface

OS::ContrailV2::ServiceTemplate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-16437
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: casablanca

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::ServiceTemplate``
    Resource ID **MUST** contain the ``{vm-type}``.

.. req::
    :id: R-14447
    :target: VNF
    :keyword: MAY
    :updated: dublin

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::ServiceTemplate``
    Resource ID **MAY** use the naming convention

    * ``{vm-type}_RST_{index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``RST`` signifies that it is the Resource Service Template
    * ``{index}`` is the index.
      The ``{index}`` starts at zero and increments by one
      (as described in R-11690).

OS::ContrailV2::VirtualMachineInterface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-96253
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualMachineInterface`` Resource ID
    that is attaching to an ONAP external network
    **MUST** use the naming convention

    * ``{vm-type}_{vm-type_index}_{network-role}_vmi_{vmi_index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP external network
      that the port (i.e. virtual machine interface) is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.


.. req::
    :id: R-50468
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualMachineInterface`` Resource ID
    that is attaching to an ONAP internal network (per the ONAP definition, see
    Requirements R-52425 and R-46461 and R-35666)
    **MUST** use the naming convention

    * ``{vm-type}_{vm-type_index}_int_{network-role}_vmi_{vmi_index}``

    where

    * ``{vm-type}`` is the vm-type
    * ``{vm-type_index}`` references the instance of the ``{vm-type}`` in
      the VNF.  The
      ``{vm-type_index}`` is a numeric value that **MUST** start at zero
      in the VNF and
      **MUST** increment by one each time a new instance of a ``{vm-type}``
      is referenced.
    * ``{network-role}`` is the network-role of the ONAP internal network
      that the port (i.e. virtual machine interface) is attached to
    * ``{vmi_index}`` references the instance of the virtual machine interface
      on the ``{vm-type}`` attached to ``{network-role}`` network.  The
      ``{vmi_index}`` is a numeric value that **MUST** start at zero on an
      instance of a ``{vm-type}`` and **MUST** increment by one each time a
      new virtual machine interface is defined on the instance of the
      ``{vm-type}`` attached to ``{network-role}`` network.


OS::ContrailV2::VirtualNetwork
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. req::
    :id: R-99110
    :target: VNF
    :keyword: MUST
    :validation_mode: static
    :updated: frankfurt

    A VNF's Heat Orchestration Template's Resource
    ``OS::ContrailV2::VirtualNetwork`` Resource ID **MUST** use the naming
    convention

    * ``int_{network-role}_network``

    VNF Heat Orchestration Templates can only create ONAP internal networks
    (per the ONAP definition, see Requirements R-52425 and R-46461 and R-35666).
    There is no ``{index}`` after ``{network-role}`` because ``{network-role}``
    **MUST** be unique in the scope of the VNF's
    Heat Orchestration Template.
