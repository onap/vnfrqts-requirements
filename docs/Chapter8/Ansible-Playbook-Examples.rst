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


Ansible Playbook Examples
-----------------------------------------------

The following sections contain examples of Ansible playbooks
which follow the guidelines.

To see specific documentation for the Ansible Adapter please refer
to: :doc:`APPC Ansible Adapter <../../../../appc/deployment.git/docs/APPC Ansible Adapter/APPC Ansible Adapter>`


Guidelines for Playbooks to properly integrate with APPC/SDN-C
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**NOTE**: To support concurrent requests to multiple playbooks, targeting VNF
instances of same or different type, VNF files dynamically created by playbooks
with VNF specific default values are kept or created in separate directories.

VNF inventory hosts file names include the VNF instance name and are now
created under base ``inventory`` directory to preserve properties of (global)
``inventory/group_vars`` files with variables, example, site specific
attributes for DNS, NTP, etc.

**Example of an Ansible command (after pwd) to run playbook again
vfdb9904v VNF instance:**

.. code-block:: text

 $ pwd
 /storage/vfdb/V16.1/ansible/configure
 $ ansible-playbook -i ../inventory/vfdb9904vhosts site.yml --extra-vars "vnf_instance=vfdb9904v"

 NOTE: To preserve Ansible inventory/group_vars capability, that makes
 group_vars contents global variables available to all playbooks, when they
 reside in the inventory directory, guidelines were updated to name the
 VNF inventory hosts file as (a flat file) <VNFName>hosts, stored in the
 inventory directory, not a subdirectory under inventory.

**Example of corresponding APPC/SDN-C API Call from ONAP – Ansible Server
Specifications:**

Using a curl request simulating a Rest API POST requesting execution
of configure Playbook (using playbook relative path):

.. code-block:: text

 curl -u APIUser:APIPassword -H "Content-type:application/json" -X POST
 -d '{"Id": "8412", "PlaybookName": "vfdb/V5.x.x/ansible/configure/site.yml",
 "Timeout":"600", "EnvParameters": { "vnf_instance": "vfdb9904v" }}'
 http://ansible.server.com:5000/Dispatch

Rest API GET request to obtain response/results for prior request
(same ID as POST request above):

.. code-block:: text

 curl -u APIUser:APIPassword -H 'Content-type: application/json' -X GET
 'http://ansible.server.com:5000/Dispatch/?Id=8412&Type=GetResult'

Comments:

-  An ID number is assigned to each request. This ID number is used to
   track request down to completion and provide status to APPC/SDN-C
   upon request for status.

-  Playbook Name relative path provided in the request as PlaybookName.

-  Ansible Server Rest API is aware of playbook's root directory which may
   vary from instance to instance or Ansible Server cluster to cluster.

Ansible Playbooks will use the VNF instance name (passed using
--extra-vars "vnf_instance=vfdb9904v") to identify other default values
to run the playbook(s) against the target VNF instance. Same example as
above:

.. code-block:: text

 $ ansible-playbook -i ../inventory/vfdb9904vhosts site.yml --extra-vars "vnf_instance=vfdb9904v"

Each Ansible Server or cluster is assigned its own identification to be used
to authenticate to VNF VMs using Ansible Server or cluster specific set of
SSH keys that may be rotated regularly. Here a hosts file, without any SSH key
credentials, to run ansible-playbook command, listed in example above (NOTE: IP
addresses were scrubbed):

.. code-block:: text

 $ more ../inventory/vfdb9904vhosts
 [host]
 localhost ansible_connection=local

 [oamvip]
 1xx.2yy.zzz.108

 [oam]
 1xx.2yy.zzz.109
 1xx.2yy.zzz.110

 [rdb]
 1xx.2yy.zzz.105
 1xx.2yy.zzz.106

 [wp0ny:children]
 oam
 rdb
 oamvip

Virtual IP addresses that can be used by multiple VMs, usually, used by the
active VM of an active-standby pair, are placed under a group named after the
VNFC (VM) type, plus "vip" string, example of such a group name "oamvip". An
inventory hosts file site also contains a (group) with all groups as children
(see last four lines in above example), to load site specific variables like
NTP, DNS IP addresses, and other site specific variables, making them global
variables to be used by playbooks, namely, configure playbook.

**NOTE**: APPC/SDN-C requests to run Playbooks/Cookbooks target a specific VNF
instance, but could be limited to one VM or one type of VM by the request
parameters. Actions that may impact a site (LCP), a service, or an
entire platform must be orchestrated by MSO in order to execute requests
via APPC/SDN-C which then invoke VNF level playbooks. Playbooks that
impact more than a single VNF instance are not the current focus of these
guidelines.

Creating group_vars sub-directories in the same directory that contains the
command/action main playbook, while following Ansible standards, to auto load
these variables as global variables is supported as are the majority of
Ansible standard capabilities.

Certain VNF Type global variables, for example site specific variables, were
moved under inventory/group_vars files in the Beijing release. This way those
variables and respective values are available to all playbooks without
being explicitly referenced through an include vars statement. Also creating
templates that are VNF Type specific moving away from static files that
are VNF instance specific.

Any remaining VNF instance specific variables that cannot be obtained from
inventory (A&AI) or other sources, that still need to be created or edited
manually, in advance of VNF instantiation, shall be created under
``ansible/vars`` directory. Recommendation is to use JSON or YAML files,
explicitly referenced by the playbooks, for this purpose, example:
``<VNF_instance_name>.json``.

**Example of playbook task explicitly referencing a VNF instance specific json
file and loading the contents as global variables**:

.. code-block:: text

 $ cat site.yml
 ---

 ...

 - name: get json vars
   hosts: localhost
   gather_facts: False
   tasks:
     - name: json attributes and values
       include_vars: "../vars/{{ vnf_instance }}.json"

 - name: show variables
   hosts: localhost
   gather_facts: False
   roles:
     - debug
 ...

 # Just another example using YAML file
 - name: load vars in a file
  hosts: rdb
 ...
  vars_files:
    - ../vars/{{ vnf_instance }}.yml

 $ ls -1 ../vars
 vfdb9904v.json
 vfdb9905v.json
 vfdb9906v.json
 vfdb9904v.yml
 vfdb9905v.yml
 vfdb9906v.yml



Parameters like VNF names, VNFC names, OA&M IP addresses are extracted
from the inventory database (A&AI) by APPC/SDN-C and then passed down to
Ansible Server in a NodeList attribute, as part of APPC/SDN-C request through
REST API. The Ansible Server Rest API uses the NodeList contents and
InventoryNames parameter to build the inventory hosts file for the request,
according to VNF playbook design needs, with or without VM or VNFC names.
For parameterized playbooks, attribute-value pairs passed down by APPC/SDN-C
to Ansible Server, always takes precedence over template or VNF instance
specific defaults stored in defaults file(s) as they are made part of the
``ansible-playbook`` run command's ``"—extra-vars"`` list.

**Example**:

.. code-block:: text

 $ pwd
 /storage/vfdb/latest/ansible
 Again, originated from previously re-factored playbooks now being phased out:

 $ more vars/vfdb9904v/default_args.yml

 vm_config_oam1_vnfc_name: vfdb9904vm001oam001
 vm_config_oam1_hostname: vfdb9904vm001
 vm_config_oam1_provider_ip_address: 1xx.2yy.zzz.109

 vm_config_oam2_vnfc_name: vfdb9904vm002oam001
 vm_config_oam2_hostname: vfdb9904vm002
 vm_config_oam2_provider_ip_address: 1xx.2yy.zzz.110

 vm_config_rdb1_vnfc_name: vfdb9904vm003rdb001
 vm_config_rdb1_hostname: vfdb9904vm003
 vm_config_rdb1_provider_ip_address: 1xx.2yy.zzz.105

 vm_config_rdb2_vnfc_name: vfdb9904vm004rdb001
 vm_config_rdb2_hostname: vfdb9904vm004
 vm_config_rdb2_provider_ip_address: 1xx.2yy.zzz.106

 vm_config_rdb3_vnfc_name: vfdb9904vm005rdb001
 vm_config_rdb3_hostname: vfdb9904vm005
 vm_config_rdb3_provider_ip_address: 1xx.2yy.zzz.xxx

 vm_config_rdb4_vnfc_name: vfdb9904vm006rdb001
 vm_config_rdb4_hostname: vfdb9904vm006
 vm_config_rdb4_provider_ip_address: 1xx.2yy.zzz.yyy

One of the first tasks on the Ansible Playbooks is to combine the VNF
type generic templates, stored on the Ansible Server with playbooks, with
the overriding parameters passed down from APPC/SDN-C, to create the
VNF instance specific set of attribute-value pairs to be used for the run, in
INI format.

Here is an excerpt from such a file that should look somewhat similar to ENV
files:

.. code-block:: text

 $ more tmp/vfdb9904v/all.yml

 deployment_prefix: vfdb9904v
 ...
 timezone: Etc/UTC
 ...
 template_version: '2014-10-16'
 stack_name: vfdb9904v
 c3dbtype: OAM
 stackName: vfdb9904v
 juno_base: true
 ...

# logins list contains 'login name', 'login group', 'login password'

.. code-block:: text

 logins:
 - { name: 'm99999', group: 'm99999', password: 'abcdefgha' }
 - { name: 'gsuser', group: 'gsuser', password: ' abcdefgha' }
 - { name: 'peruser', group: 'peruser', password: ' abcdefgha' }
 - { name: 'dbuser', group: 'dbuser', password: ' abcdefgha' }

**NOTE**: Arguments passed by APPC/SDN-C to Ansible Server to run a
playbook take precedence over any defaults stored in Ansible Server.

Ansible Playbooks – Notes On Artifacts Required to Run Playbooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inventory hosts file: should be VNF instance specific.

Default variables: should be VNF instance specific.

Playbooks and paths to referenced files: Playbooks shall not use
absolute paths in include or import entries (variables or playbooks) or
other types of references.

For this to work properly, when running playbooks, the directory where
the main playbook resides shall be the current directory.

Playbook imports, when used, shall use paths relative to the main
playbook directory.

Root directory named ansible - Any files provided with playbooks,
included, imported, or referenced by playbooks, shall reside under the ansible
playbooks (root) directory, containing all playbook subdirectories, or
below that ansible root directory, in other subdirectories to support
on-boarding and portability of VNF collection of playbooks and related
artifacts.

**Designing for a shared environment, concurrently running playbooks,
targeting multiple VNF instances – inventory hosts file:**

To avoid inventory hosts file overwrites or collisions between multiple
concurrently running VNF instance requests, chosen approach is for each
VNF instance hosts file, to be stored under the Ansible Server Playbooks
root directory (ansible), under the inventory subdirectory, on an inventory
hosts file named after the VNF instance, as follows:

.. code-block:: text

 ansible/inventory/<VNF_instance_name>hosts

Example of inventory hosts file path, relative to ansible playbooks (ansible)
root directory (playbooks_dir):

.. code-block:: text

 ansible/inventory/vnfx0001vhosts

**Designing for a shared environment, concurrently running multiple playbooks,
targeting multiple VNF instances – default argument variables for
specific VNF instances:**

VNF instance specific files referenced/included by playbooks, containing
default values, example, ``default_args.yml``, shall be stored under a
directory with VNF instance name on the path (backwards compatibility) or
contain VNF instance name as part of the name.

**Example**:

.. code-block:: text

 ansible/vars/<VNF_instance_name>/default_args.yml

**Example of include statement**:

.. code-block:: text

 include_vars: ../vars/{{ vnf_instance }}/default_args.yml

**Example – all in vars directory**:

.. code-block:: text

 ansible/vars/<VNF_instance_name>default_args.yml

**Example of include statement without vars subdirectory**:

.. code-block:: text

 include_vars: ../vars/{{ vnf_instance }}default_args.yml

Above example has originated from previously re-factored playbooks now being
phased out. Direction is to move away from having to create VNF instance
specific files with VNF instance default variables to the extent possible.
Moving to extract these values from inventory databases and provide them to
Ansible Server as part of APPC/SDN-C request, may be used in a transition
from having everything stored in the Ansible Server to APPC/SDN-C
extracting and providing VNF instance specific attribute-value pairs to the
Ansible Server as part of the request.

**Files containing attribute name value pairs (variable name and default
values), referenced/included by playbooks – created dynamically by
playbooks:**

To avoid overwrites or collisions of multiple concurrently running VNF instance
requests, files created dynamically by playbooks, based on VNF generic
templates, combined with default values and arguments passed down by
APPC/SDN-C (as part of the request), shall be stored under a directory
with VNF instance name on the path.

**Example**:

.. code-block:: text

 tmp/<VNF_instance_name>/all.yml

Files containing site specific (Openstack location non-instance specific)
attribute name value pairs, like NTP server and DNS server's IP addresses and
other parameters, referenced/included by playbooks, not VNF specific –
Could/should be stored under inventory/group_vars directory, in a subdirectory
named after the string used to identify the site (nyc1, lax2,...).

**Examples**:


.. code-block:: text

 ansible/inventory/group_vars/<Site>

 ansible/inventory/group_vars/wp0ny

 ansible/inventory/group_vars/la0ca

**Ansible Server Design - Directory Structure**

To help understanding the contents of this section, here are few basic
definitions:

**VNF type a.k.a VNF Function Code** - Based on current  naming convention,
each Virtual Network Function is assigned a 4 character string (example vfdb),
these are 4 characters in the VNF instance name, followed by (4) numbers,
ending in a "v". The naming convention has evolved to include geographical
location. VNF instance name in some cases corresponds to the stack name for the
VNF when VNF instance is built based on a single module, single stack. Example
of VNF instance name: vfdb9904v. All VNF performing this function, running the
same software, coming from the same VNF provider will have the same 4
characters in the VNF instance name, in this example, vfdb.

**NOTE**: New naming convention includes a prefix indicating geographical
location where VNF is instantiated.

VNF type, determined through these 4 characters, is also known as VNF
Function Code. All VNF Function Codes can be found in A&AI as well as
other Network Design Documents.

**Version** – VNF software version is the release of the software
running on the VNF for which the playbooks were developed. VNF
configuration steps may change from release to release and this
<Version> in the path will allow the Ansible Server to host playbooks
associated with each software release. And run the playbooks that match
the software release running on each VNF instance. APPC/SDN-C now support
playbook versioning passed as a variable to APP-C to allow multiple
actively, in use, playbook versions to be picked to match VNF release/version.

**Playbook Function** - A name associated with a life cycle management
task(s) performed by the playbook(s) stored in this directory. It should
clearly identify the type of action(s) performed by the main playbook
and possibly other playbooks stored in this same directory. Ideally,
playbook function would match APPC/SDN-C corresponding command or function
that is performed by the main playbook in this directory. Following Ansible
naming standards, main playbook, is named site.yml. There can be other
playbooks on the same directory that use a subset of the roles used by the
main playbook site.yml. Examples of Playbook Function directory names(matching
APPC/SDN-C command name in lowercase):

-  ``configure`` – Contains post-instantiation (bulk) configuration
   playbook(s), roles,...

-  ``healthcheck`` – Contains VNF health check playbook(s), roles,...

-  ``stopapplication`` – Contains VNF application stop (stopApplication)
   playbook(s), roles,...

-  ``startapplication`` – Contains VNF application start (startApplication)
   playbook(s), roles,...

-  ``restartapplication`` – Contains VNF application restart
   (restartApplication) playbook(s), roles,...

-  ``configbackup`` – Contains VNF configuration backup (ConfigBackup)
   playbook(s), roles,...

-  ``configrestore`` – Contains VNF configuration restore (ConfigBackup)
   playbook(s), roles,...

-  ``configmodify`` – Contains VNF configuration modification (ConfigModify)
   playbook(s), roles,...

-  ``configscaleout`` – Contains VNF scale-out configuration/reconfiguration
   (ConfigBackup) playbook(s), roles,...

-  ``quiescetraffic`` – Contains VNF traffic graceful drain/quiesce
   (QuiesceTraffic) playbook(s), roles,...

-  ``resumetraffic`` – Contains VNF resume/restore traffic (ResumeTraffic)
   playbook(s), roles,...

-  ``upgradeprecheck`` – Contains VNF current (old) SW version check
   (UpgradePreCheck) playbook(s), roles,...

-  ``upgradebackup`` – Contains VNF backup prior to SW upgrade (UpgradeBackup)
   playbook(s), roles,...

-  ``upgradesoftware`` – Contains VNF SW upgrade (UpgradeSoftware)
   playbook(s), roles,...

-  ``upgradepostcheck`` – Contains VNF upgraded (new) SW version check
   (UpgradePostCheck) playbook(s), roles,...

-  ``upgradebackout`` – Contains VNF (SoftwareUpgrade) back out
   (UpgradeBackout) playbook(s), roles,...

-  ``license`` – Contains a playbook to manage licenses, add, upgrade,
   delete, renew, etc.

-  ``starttraffic`` – Contains a playbook used for traffic management (start)

-  ``stoptraffic`` – Contains a playbook used for traffic management (stop)

-  ``distributetraffic`` – Contains a playbook used for traffic management
   (distribute/redistribute)

-  ``statustraffic`` – Contains a playbook used to check status of traffic
   (started, stopped, etc.)

-  ``preconfigcheck`` – Contains post-instantiation pre-configuration check
   playbook(s) that makes no configuration changes to the VNF instance, just
   verifies all conditions are met to successfully run preconfig and/or
   configure playbooks

-  ``preconfig`` – Contains post-instantiation pre-configuration playbook(s),
   that is to run before running the configure playbook

-  ``postconfig`` – Contains post-instantiation post-configuration playbook(s),
   that is to run after running the configure playbook, example, to integrate
   VNFs of different types

-  ``provision`` – Contains a playbook to run on demand, as needed, load or
   update provisioning data onto VNF instances

Other playbook actions were added and are supported, example of playbooks
supported to run before and after Openstack nova commands:

-  prerebuild  & postrebuild

-  premigrate  & postmigrate

-  preevacuate  & postevacuate

Other playbook actions in use not yet supported by APP-C:

-  ``postrestart`` – Contains a playbook used to perform tasks after restarting
   VNF application or VNF instance or a single VM

-  ``restartpods`` – Contains a playbook used to perform tasks to restart
   application containers

-  ``user_management`` – Contains a playbook used to manage user accounts on
   demand (add, update, delete) as part of VNF instance life cycle management

-  ``preinstantiate`` – Contains pre-instantiation playbook(s) to perform
   preparation tasks in advance of instantiation of a VNF instance

Directory structure to allow hosting multiple version sets of playbooks,
for the same VNF type, to be hosted in the runtime environment on the
Ansible Servers. Generic directory structure:

**Ansible Playbooks – Function directory and main playbook**:

.. code-block:: text

 <VNF type>/<Version>/ansible/<Playbook Function>/site.yml

**Example – Post-instantiation (bulk) configuration – APPC/SDN-C Function -
Configure**:

.. code-block:: text

 <VNF type>/<Version>/ansible/configure/site.yml

**Example – Post-instantiation (bulk) configuration – APPC/SDN-C Function
– Configure – VNF software version 16.1**:

.. code-block:: text

 vfdb/V16.1/ansible/configure/site.yml

**Example – Health-check - APPC/SDN-C Function - HealthCheck**:

.. code-block:: text

 <VNF type>/<Version>/ansible/healthcheck/site.yml

OR (Function directory name is not required to match APPC/SDN-C function name
exactly)

.. code-block:: text

 <VNF type>/<Version>/ansible/check/site.yml

**Ansible Directories for other artifacts – VNF inventory hosts file -
Required**:

.. code-block:: text

 <VNF type>/<Version>/ansible/inventory/<VNF instance name>hosts

**NOTE**: Default groups, in inventory hosts file, will be created based on
VNFC type (represented by 3 characters) in VNFC name. Example: "oam", "rdb",
"dbs", "man", "iox", "app",...

**Ansible Directories for other artifacts – VNF instance specific default
arguments – Optional**:

.. code-block:: text

 <VNF type>/<Version>/ansible/vars/<VNF instance name>.json (Preferred)

OR

.. code-block:: text

 <VNF type>/<Version>/ansible/vars/<VNF instance name>.yml
 (INI format accepted/supported by Ansible)

**NOTE**: Requirement remains while manual actions to create or edit VNF or PNF
instance specific files are supported all files manually created or edited
should be placed in this one directory (``ansible/vars``).

**Ansible Directory for site specific attribute-value pairs (in INI format)
- VNF Site files:**:

.. code-block:: text

 <VNF type>/<Version>/ansible/inventory/group_vars/<Site name>

**Ansible Directories for other artifacts – VNF (special) other files –
Optional – Example – License file**:

.. code-block:: text

 <VNF type>/<Version>/ansible/<Other directory(s)>

**CAUTION**: On referenced files used/required by playbooks.

-  To avoid missing files, during on-boarding or uploading of Ansible
   Playbooks and related artifacts, all permanent files (not generated
   by playbooks as part of execution), required to run any playbook,
   shall reside under the ansible root directory or below on other
   subdirectories.

-  Any references to files, on includes or other playbook entries, shall
   use relative paths.

-  This is the ansible (root) directory referenced on this
   note (Ansible Server mount point not included):

.. code-block:: text

 <VNF type>/<Version>/ansible/

VNF type directories use A&AI inventory VNF function code. Ansible
Playbooks will be stored on a (Cinder) Volume mounted on the Ansible
Servers as /storage that is used as a local cache for playbooks and other
related artifacts cloned or pulled (updates) from central (git) repository.

Example:

``/storage/vfdb/V16.1/ansible`` – Root directory for database VNF Ansible
Playbooks for release 16.1

**CAUTION**: To support this directory structure as the repository to store
Ansible Playbooks run by APPC/SDN-C, APPC/SDN-C API in the Ansible
Server side needs to be configured to run playbooks from this directory.

Ansible Server HTTP will be configured to support APPC/SDN-C REST API
requests to run playbooks as needed, against specific VNF instances, or
specific VM(s) as specified in the request. When a playbook action is expected
to target a subset of VMs in a VNF instance, VNF instance inventory hosts file
is expected to be used, and an extra-vars parameter, named target_vm_list with
the list of VMs to be targeted by the playbook, is expected to be provided to
run specific actions targeting the VM subset. The attribute target_vm_list may
point to a single name or single IP address or a list of names or IP addresses
in between double-quotes with names or IPs seprated by comma, example,
target_vm_list="name1,name2".

APPC/SDN-C REST API to Ansible Server is documented separately and
can be found under ONAP (onap.org).


Ansible Inventory Hosts File – Supported Formats
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Supported inventory hosts file examples, built from this NodeList model,
extracted from A&AI by APPC/SDN-C and passed to the Ansible
Server via Rest API as part of request:

.. code-block:: json

  {
    "NodeList": [
        {
            "vnfc_type": "oam",
            "ne_id_vip": "vfdb9904vm001oam001",
            "floating_ip_address_vip": "1xx.2yy.zzz.109",
            "site": "wp0ny",
            "vm_info": [
                 {
                     "ne_id": "vfdb9904vm001oam001",
                     "fixed_ip_address": "1xx.2yy.zzz.109"
                 },
                 {
                     "ne_id": "vfdb9904vm002oam001",
                     "fixed_ip_address": "1xx.2yy.zzz.110"
                 }
            ]
        },
        {
            " vnfc_type": "rdb",
            "site": "wp0ny",
            "vm_info": [
                 {
                     "ne_id": "vfdb9904vm003rdb001",
                     "fixed_ip_address": "1xx.2yy.zzz.105"
                 },
                 {
                     "ne_id": "vfdb9904vm004rdb001",
                     "fixed_ip_address": "1xx.2yy.zzz.106"
                 }
            ]
        }
    ]
  }

With no names, only IP addresses, template "InventoryNames": "None" (Default)

.. code-block:: text

 $ more ../inventory/vfdb9904vhosts
 [host]
 localhost ansible_connection=local

 [oamvip]
 1xx.2yy.zzz.108

 [oam]
 1xx.2yy.zzz.109
 1xx.2yy.zzz.110

 [rdb]
 1xx.2yy.zzz.105
 1xx.2yy.zzz.106

 [wp0ny:children]
 oam
 rdb
 oamvip

With VM names and IP addresses, template inventory names setting
"InventoryNames": "VM"

.. code-block:: text

 $ more ../inventory/vfdb9904vhosts
 [host]
 localhost ansible_connection=local

 [oamvip]
 vfdb9904vm001vip ansible_host=1xx.2yy.zzz.108

 [oam]
 vfdb9904vm001 ansible_host=1xx.2yy.zzz.109
 vfdb9904vm002 ansible_host=1xx.2yy.zzz.110

 [rdb]
 vfdb9904vm003 ansible_host=1xx.2yy.zzz.105
 vfdb9904vm004 ansible_host=1xx.2yy.zzz.106

 [wp0ny:children]
 oam
 rdb
 oamvip

With VNFC names and IP addresses, template inventory names setting
"InventoryNames": "VNFC"

.. code-block:: text

 $ more ../inventory/vfdb9904vhosts
 [host]
 localhost ansible_connection=local

 [oamvip]
 vfdb9904vm001oam001vip ansible_host=1xx.2yy.zzz.108

 [oam]
 vfdb9904vm001oam001 ansible_host=1xx.2yy.zzz.109
 vfdb9904vm002oam001 ansible_host=1xx.2yy.zzz.110

 [rdb]
 vfdb9904vm003rdb001 ansible_host=1xx.2yy.zzz.105
 vfdb9904vm004rdb001 ansible_host=1xx.2yy.zzz.106

 [wp0ny:children]
 oam
 rdb
 oamvip



Ansible Server – On-boarding Ansible Playbooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once playbooks are developed following these guidelines, playbooks need to be
on-boarded onto Development Ansible Server(s), and placed under (git) code
control. Once a (git) repository is created for the set of playbooks, playbooks
are then pushed to the central repository. Using mechanized identification that
leverages SSH key based authentication, a mechanism is in place to regularly
clone or pull updates from central repository to runtime Ansible Server
Clusters, to perform an automated controlled distribution of playbooks and
related artifacts to clustered runtime Ansible Servers.

These are the basic steps to on-board playbooks manually onto the
Ansible Server.

#. Upload CSAR, zip, or tar file containing VNF playbooks and related
   artifacts to Development Ansible Server with connectivity to central
   repository.

#. Unzip packaged playbooks or manually create full directory (using –p
   option below) to store Ansible Playbooks and other artifacts under /storage
   (or other configured) file system.

   Includes VNF type using VNF function code 4 characters under
   /storage.

   Includes VNF "Version" directory as part of the path to store
   playbooks for this VNF version.

   Include generic ansible root directory. Creating full directory
   path as an example:

.. code-block:: text

 $ mkdir –p /storage/vfdb/V16.1/ansible

#. When manually creating directory structure make this directory (VNF
   ansible root directory) current directory for next few steps:

.. code-block:: text

 cd /storage/vfdb/V16.1/ansible/

#. Extract Ansible Playbooks and other Ansible artifacts associated with
   the playbooks onto the ansible directory. Command depends on the type
   of file uploaded, examples would be:

.. code-block:: text

 tar xvf ..
 unzip ... # Usually, unzip creates the entire directory structure

#. Create VNF inventory hosts file with all VMs and OA&M IP addresses, and VM
   or VNFC names as required for the VNF type, grouped by VM/VNFC type. Add
   site with all groups as children. Inventory hosts file are required for all
   VNF instances, to be configured and managed through Ansible. Inventory hosts
   file example:

.. code-block:: text

 $ mkdir inventory

 $ touch inventory/vfdb9904vhosts

 $ cat inventory/vfdb9904vhosts

 [host]
 localhost ansible_connection=local

 [oamvip]
 1xx.2yy.zzz.108

 [oam]
 1xx.2yy.zzz.109
 1xx.2yy.zzz.110

 [rdb]
 1xx.2yy.zzz.105
 1xx.2yy.zzz.106

 [wp0ny:children]
 oam
 rdb
 oamvip


Virtual IP addresses that can be used by multiple VMs, usually, used by the
active VM of an active-standby pair, are placed under a group named after the
VNFC (VM) type, plus "vip" string, example of such a group name "oamvip".

#. (Optional) Create directory to hold default arguments for VNF instance,
   and respective file(s), when required by VNF type, example:

.. code-block:: text

 $ mkdir –p vars/vfdb9904v.json
 $
 $ cat vfdb9904v.json
 ...
 {
   "json_var1": "vfdb9904v_test_var1",
   "json_var2": "vfdb9904v_test_var2",
   "json_var3": "vfdb9904v_test_var3"
 }
 ...


**NOTE**: Please note names in this file shall use underscore "_" not dots
"." or dashes "-".

#. Perform some basic playbook validation running with "--check" option,
   running dummy playbooks or other.

#. Make <VNF version> directory current directory to add playbooks and other
   artifacts under (git) code control:

.. code-block:: text

 cd /storage/vfdb/V16.1

**NOTE**: After creating the repository for the playbooks in the central
repository a list of (git) commands is provided to add playbooks
under (git) code control and push them to the newly created repository. Each
Ansible Server or cluster of Ansible Servers will have its own
credentials to authenticate to VNF VMs. Ansible Server SSH public key(s)
have to be loaded onto VNF VMs during instantiation or another way before
Ansible Server can access VNF VMs and run playbooks. Heat templates used
to instantiate VNFs to be configured by these Ansible Servers running
playbooks shall include the same SSH public key and load them onto VNF VM(s)
as part of instantiation. Same Ansible Server Cluster SSH public keys are to be
added to repositories to provide each authorized cluster access, to clone and
pull updates, to each VNF collection of playbooks, from central repository.

Other non-vendor specific playbook tasks, required by customer, need to be
incorporated in overall post-instantiation configuration playbook. Alternative
is for company developed playbooks to be pushed to a repository, distributed
and executed, after VNF vendor provided playbooks are run.

**A couple of playbooks used for proof-of-concept testing as examples:**

UpgradePreCheck:

.. code-block:: text

 $ pwd
 /storage/comx/V5.3.1.3/ansible/upgradeprecheck

 $ more site.yml
 ---

 - import_playbook: ../common/create_vars.yml
 - import_playbook: ../common/create_hosts.yml

 - name: upgrade software pre check
   hosts: oam,dbs,cpm
   gather_facts: no
   become: true
   become_method: sudo
   become_user: root
   max_fail_percentage: 0
   any_errors_fatal: True
   roles:
     - precheck
   tags: precheck

 $ more roles/precheck/tasks/main.yml
 ---

 - include_vars: /tmp/{{ vnf_instance }}/all.yml

 - name: get software version installed on vnf
   shell: grep "^SW_VERSION =" /vendor/software/config/param_common.cfg | grep -c "{{ existing_software_version }}"
   register: version_line
   ignore_errors: yes

 - name: send msg when matches expected version
   debug:  msg="*** OK *** VNF software release matches (old) release to be upgraded."
    verbosity=1
   when: version_line.stdout.find('1') != -1

 # send warning message and failure when release is not a match
 - fail:
     msg="*** WARNING *** VNF software release does not match expected (pre-upgrade) release."
   when: (version_line | failed) or version_line.stdout.find('1') == -1


UpgradePostCheck:

.. code-block:: text

 $ pwd
 /storage/comx/V5.3.1.3/ansible/upgradepostcheck

 $ more site.yml
 ---

 - import_playbook: ../common/create_vars.yml
 - import_playbook: ../common/create_hosts.yml

 - name: upgrade software post check
   hosts: oam,dbs,cpm
   gather_facts: no
   become: true
   become_method: sudo
   become_user: root
   max_fail_percentage: 0
   any_errors_fatal: True
   roles:
     - postcheck
   tags: postcheck

 $ more roles/postcheck/tasks/main.yml
 ---

 - include_vars: /tmp/{{ vnf_instance }}/all.yml

 - name: get post upgrade software version installed on vnf
   shell: grep "^SW_VERSION =" /vendor/software/config/param_common.cfg | grep -c "{{ new_software_version }}"
   register: version_line
   ignore_errors: yes

 - name: send msg when matches expected version
   debug:  msg="*** OK *** VNF software release matches new release."
     verbosity=1
   when: version_line.stdout.find('1') != -1

 # send warning message and failure when release is not a match
 - fail:
     msg="*** WARNING *** VNF software release does not match expected new (post-upgrade) release."
   when: (version_line | failed) or version_line.stdout.find('1') == -1


Ansible Server – Playbook Example to Discover Ansible Server Mechanized User ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example of playbook role discovering runtime Ansible Server mechanized user ID
and setting it up on target VNF VM(s) with issued and assigned SSH public key
with "from=" clause stored onto xxxxx_id_rsa.frompub file:

.. code-block:: text

 $ cat roles/setup_ansible_mechid/tasks/main.yml
 ---

 - name: set mechid
   set_fact:
     ansible_mechid: "{{lookup('ini', 'remote_user section=defaults file=/etc/ansible/ansible.cfg') }}"

 - name: set mechid uid
   set_fact:
     ansible_mechuid: "{{lookup('ini', 'remote_user section=defaults file=/etc/ansible/ansible.cfg')[1:] }}"

 - debug: msg="mechid {{ ansible_mechid }} ansible_mechuid {{ ansible_mechuid }}"
     verbosity=1

 # Create ansible server Mech ID group
 - group:
     name: "{{ ansible_mechid }}"
     state: present

 # add ansible server mech id user
 - user:
     name: "{{ ansible_mechid }}"
     group: "{{ ansible_mechid }}"
     state: present
     comment: "Ansible Server Mech ID"
     expires: 99999
     groups: 0
     uid: "{{ ansible_mechuid }}"

 - name: create ansible mech id .ssh directory
   file: path=/home/{{ ansible_mechid }}/.ssh owner={{ ansible_mechid }} group={{ ansible_mechid }} mode=0700 state=directory

 - name: touch ansible mech id authorized_keys file
   file: path=/home/{{ ansible_mechid }}/.ssh/authorized_keys owner={{ ansible_mechid }} group={{ ansible_mechid }} mode=0600 state=touch

 - name: get path to mechid id_rsa.pub
   set_fact:
     public_key: "{{lookup('ini', 'private_key_file section=defaults file=/etc/ansible/ansible.cfg') }}.frompub"
 #   public_key: "{{lookup('ini', 'private_key_file section=defaults file=/etc/ansible/ansible.cfg') }}.pub"

 - name: setup authorized_keys file
   authorized_key:
     user: "{{ ansible_mechid }}"
     state: present
     key: "{{ lookup('file', '{{ public_key}}') }}"
 …

