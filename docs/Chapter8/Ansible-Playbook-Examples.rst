.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

Ansible Playbook Examples
-----------------------------------------------

The following sections contain examples of Ansible playbooks
which follow the guidelines.

Guidelines for Playbooks to properly integrate with APPC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NOTE: To support concurrent requests to multiple VNF instances of same
or different type, VNF hosts and other files with VNF specific default
values are kept or created in separate directories.

Example of an Ansible command (after pwd) to run playbook again
vfdb9904v VNF instance:

.. code-block:: none

 $ pwd
 /storage/vfdb/V16.1/ansible/configure
 $ ansible-playbook -i ../inventory/vfdb9904vhosts site.yml --extra-vars "vnf_instance=vfdb9904v"

 NOTE: To preserve Ansible inventory/group_vars capability, that makes
 group_vars contents global variables available to all playbooks, when they
 reside in the inventory directory, guidelines are being updated to name the
 VNF inventory hosts file as (a flat file) <VNFName>hosts, stored in the
 inventory directory, not a subdirectory under inventory. In the above
 example: vfdb9904vhosts (removed / VNF name and hosts vfdb9904/vhosts)

Example of corresponding APPC API Call from ONAP – Ansible Server
Specifications:

An example of a curl request simulating a Rest API POST requesting execution
of configure Playbook (using playbook relative path):

.. code-block:: none

 curl -u APIUser:APIPassword -H "Content-type:application/json" -X POST
 -d '{"Id": "8412", "PlaybookName": "vfdb/V5.x.x/ansible/configure/site.yml",
 "Timeout":"600", "EnvParameters": { "vnf_instance": "vfdb9904v" }}'
 http://ansible.server.com:5000/Dispatch

Rest API GET request to obtain response/results for prior request
(same Id as POST request above):

.. code-block:: none

 curl -u APIUser:APIPassword -H 'Content-type: application/json' -X GET
 'http://ansible.server.com:5000/Dispatch/?Id=8412&Type=GetResult'

Comments:

-  An ID number is assigned to each request. This ID number is used to
   track request down to completion and provide status to APPC when
   requested.

-  Playbook Name relative path provided in the request as PlaybookName

-  Ansible Server Rest API is aware of playbook’s root directory which may
   vary from instance to instance or Ansible Server cluster to cluster.

Ansible Playbooks will use the VNF instance name (passed using
--extra-vars "vnf\_instance=vfdb9904v") to identify other default values
to run the playbook(s) against the target VNF instance. Same example as
above:

.. code-block:: none

 $ ansible-playbook -i ../inventory/vfdb9904vhosts site.yml --extra-vars "vnf_instance=vfdb9904v"

Each Ansible Server or cluster is assigned its own identification to be used
to authenticate to VNF VMs using Ansible Server or cluster specific set of
SSH keys that may be rotated regularly. Here hosts file, no longer referencing
file with SSH key credentials, to run ansible-playbook listed in this example
above (IP addresses were scrubbed):

.. code-block:: none

 $ more ../inventory/vfdb9904v/hosts
 [host]
 localhost ansible_connection=local

 [oam]
 1xx.2yy.zzz.109
 1xx.2yy.zzz.110

 [rdb]
 1xx.2yy.zzz.105
 1xx.2yy.zzz.106

NOTE: APPC requests to run Playbooks/Cookbooks are specific to a VNF,
but could be more limited to one VM or one type of VM by the request
parameters. Actions that may impact a site (LCP), a service, or an
entire platform must be orchestrated by MSO in order to execute requests
via APPC which then invoke VNF level playbooks. Playbooks that impact
more than a single VNF are not the current focus of these guidelines.

Since last release of these guidelines, based on recent learnings,
moving VNF Type global variables under inventory/group_vars files, this
way variables and respective values are available to all playbooks without
being explicitly referenced though an include statement. Also creating
templates that are VNF Type specific, but moving away from static files
that are VNF instance specific, working to obtain VNF instance specific
from other sources, inventory database, etc.

And here the scrubbed default arguments for this VNF instance(originated
from previously re-factored playbooks now being phased out):

.. code-block:: none

 vnf_instance=vfdb9904v

 $ more ../vars/vfdb9904v/default_args.yml
 vm_config_oam_vnfc_name: vfdb9904vm001oam001
 vm_config_oam_hostname: vfdb9904vm001
 vm_config_oam_provider_ip_address: 1xx.2yy.zzz.109
 …

IMPORTANT: The APPC and default file attribute name for
vm\_config\_oam\_vnfc\_name, as an example, is derived from vm\_config
array structure (list) in the CSAR package ENV file, with dots replaced
by underscore:

.. code-block:: none

 vm_config:

 oam: {vnfc_name: {{ vm_config_oam_vnfc_name }}, hostname: {{
 vm_config_oam_hostname }}, provider_ip_address: {{
 vm_config_oam_provider_ip_address }
 },
 …

Parameters like VNF names, VNFC names, OA&M IP addresses, after
February, 2018 ONAP release, will be extracted from A&AI by APPC and
then passed down to Ansible Server, as part of APPC request through REST
API. In the meantime, VNF instance specific required values, will
be stored on VNF instance directory, default arguments file and will be
used as defaults. For parameterized playbooks attribute-value pairs
passed down by APPC to Ansible Server always take precedence over
template or VNF instance specific defaults stored in defaults file(s).

.. code-block:: none

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
type generic template, derived from ENV files in CSAR or other files,
with these default values stored on the Ansible Server, together with
the overriding parameters passed down from APPC, to create the VNF
instance specific set of attribute-value pairs to be used for the run, in
INI format. Here is an excerpt from such a file that should look
somewhat similar to ENV files:

.. code-block:: none

 $ more tmp/vfdb9904v/all.yml

 deployment_prefix: vfdb9904v
 …
 timezone: Etc/UTC
 …
 template_version: '2014-10-16'
 stack_name: vfdb9904v
 c3dbtype: OAM
 stackName: vfdb9904v
 juno_base: true
 …

# logins list contain 'login name', 'login group', 'login password'

.. code-block:: none

 logins:
 - { name: 'm99999', group: 'm99999', password: 'abcdefgha' }
 - { name: 'gsuser', group: 'gsuser', password: ' abcdefgha' }
 - { name: 'peruser', group: 'peruser', password: ' abcdefgha' }
 - { name: 'dbuser', group: 'dbuser', password: ' abcdefgha' }

NOTE: Arguments passed by APPC to Ansible Server to run a playbook take
precedence over any defaults stored in Ansible Server.

Ansible Playbooks – Notes On Artifacts Required to Run Playbooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inventory hosts file: should be VNF instance specific.

Default variables: should be VNF instance specific.

NOTE: Some playbooks may rely on inventory directory contents to target
the collection of VNFs in the Services Platform supported through
Ansible.

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

Designing for a shared environment, concurrently running playbooks,
targeting multiple VNF instances – inventory hosts file:

To avoid inventory hosts file overwrites or collisions between multiple
concurrently running VNF instance requests, chosen approach is for each
VNF instance hosts file, to be stored under the Ansible Server Playbooks
root directory, under the inventory subdirectory, and under a directory
for each VNF instance, named after the VNF instance, as follows:

ansible/inventory/<VNF\_instance\_name>/hosts

Example of inventory hosts file path, relative to ansible playbooks root
directory (playbooks\_dir): ansible/inventory/vnfx0001v/hosts

**Designing for a shared environment, concurrently running multiple playbooks,
targeting multiple VNF instances – default argument variables for
specific VNF instances:**

Files containing attribute name value pairs (variable name and default
values), referenced/included by playbooks – Files containing VNF
instance specific default values – in a later APPC release, some or all
the default attribute value pairs contained in the defaults file, may be
passed down by APPC, to the Ansible Server, overriding these defaults:

VNF instance specific files
referenced/included by playbooks, containing default values, example,
default\_args.yml, shall be stored under a directory with VNF instance
name on the path.

Example:

ansible/vars/<VNF\_instance\_name>/default\_args.yml

Example of include statement:

- include_vars: ../vars/{{ vnf_instance }}/default_args.yml

Again, this was originated from previously re-factored playbooks, now being
phased out, to move away from having to create VNF instance specific files
with VNF instance default variables. Moving to extract these values from
inventory databases and provide them to Ansible Server as part of the APPC
request, but may be used in a transition from having everything stored in the
Ansible Server to APPC extracting and providing VNF instance specific
attribute-value pairs to the Ansible Server as part of the request.

Files containing attribute name value pairs (variable name and default
values), referenced/included by playbooks – created dynamically by
playbooks:

To avoid
overwrites or collisions of multiple concurrently running VNF instance
requests, files created dynamically by playbooks, based on VNF generic
templates, combined with default values and arguments passed down by
APPC (as part of the request), shall be stored under a directory with
VNF instance name on the path.

Example:

tmp/<VNF\_instance\_name>/all.yml

Files containing site specific (Openstack location non-instance
specific) attribute name value pairs, like NTP server and DNS server’s
IP addresses and other parameters, referenced/included by playbooks, not
VNF specific – Could/should be stored under inventory/group_vars directory,
in a subdirectory named after the string used to identify the site (nyc1,
lax2,…).

Examples:

ansible/inventory/group_vars/<Site>

ansible/inventory/group_vars/nyc1

ansible/inventory/group_vars/lax2


\ **Ansible Server Design - Directory Structure**

To help understanding the contents of this section, here are few basic
definitions:

**VNF type a.k.a VNF Function Code** - Based on current Services
Platform naming convention, each Virtual Network Function is assigned a
4 character string (example vfdb), these are 4 characters in
the VNF instance name, followed by (4) numbers, ending in a "v", but the
naming convention is evolving. VNF instance name in
some cases corresponds to the stack name for the VNF when VNF instance
is built based on a single module, single stack. Example of VNF instance
name: vfdb9904v. All VNF performing this function, running the same
software, coming from the same VNF provider will have the same 4
characters in the VNF instance name, in this example, vfdb.

NOTE: New naming convention includes a prefix indicating geographical
location where VNF is instantiated.

VNF type, determined through these 4 characters, is also known as VNF
Function Code and is assigned by inventory team. All Services Platform
VNF Function Codes can be found in inventory database and/or A&AI as
well as Services Platform Network Design Documents.

Version – As in VNF software version is the release of the software
running on the VNF for which the playbooks were developed. VNF
configuration steps may change from release to release and this
<Version> in the path will allow the Ansible Server to host playbooks
associated with each software release. And run the playbooks that match
the software release running on each VNF instance. APPC initially will
not support playbook versioning only latest playbook is supported or a hard
coded version that later should become a variable to allow multiple
actively in use playbook versions according to VNF release.

Playbook Function - Is a name associated with a life cycle management
task(s) performed by the playbook(s) stored in this directory. It should
clearly identify the type of action(s) performed by the main playbook
and possibly other playbooks stored in this same directory. Ideally,
playbook function would match APPC corresponding command or function that
is performed by the main playbook in this directory. Following Ansible naming
standards main playbook is usually named site.yml. There can be other
playbooks on the same directory that use a subset of the roles used by the
main playbook site.yml. Examples of Playbook Function directory names:

-  configure – Contains post-instantiation (bulk) configuration
   playbooks, roles,…

-  healthcheck – Contains VNF health check playbook(s), roles,…

-  stop – Contains VNF application stop  (stopApplication) playbook(s),
   roles,…

-  start – Contains VNF application start (startApplication) playbook(s),
   roles,…

Directory structure to allow hosting multiple version sets of playbooks,
for the same VNF type, to be hosted in the runtime environment on the
Ansible Servers. Generic directory structure:

Ansible Playbooks – Function directory and main playbook:

.. code-block:: none

 <VNF type>/<Version>/ansible/<Playbook Function>/site.yml

Example – Post-instantiation (bulk) configuration –APPC Function -
Configure:

.. code-block:: none

 <VNF type>/<Version>/ansible/configure/site.yml

Example – Post-instantiation (bulk) configuration –APPC Function
– Configure – VNF software version 16.1:

.. code-block:: none

 vfdb/V16.1/ansible/configure/site.yml

Example – Health-check –APPC Function - HealthCheck:

.. code-block:: none

 <VNF type>/<Version>/ansible/healthcheck/site.yml

OR (Function directory name does not need to match APPC function name)

.. code-block:: none

 <VNF type>/<Version>/ansible/check/site.yml

Ansible Directories for other artifacts – VNF inventory hosts file -
Required:

.. code-block:: none

 <VNF type>/<Version>/ansible/inventory/<VNF instance name>hosts

Ansible Directories for other artifacts – VNF instance specific default
arguments – Optional:

.. code-block:: none

 <VNF type>/<Version>/ansible/group_vars/<VNF instance name>

NOTE: This requirement is expected to be deprecated all or in part in the
future, for automated actions, once APPC can pass down all VNF specific
arguments for each action. Requirement remains while manual actions are
to be supported. Other automated inventory management mechanisms may be
considered in the future, Ansible supports many automated inventory
management mechanisms/tools/solutions.

Ansible Directories for other artifacts – VNF (special) groups –
Optional:

.. code-block:: none

 <VNF type>/<Version>/ansible/inventory/group_vars/<VNF instance name>

NOTE: Default groups will be created based on VNFC type, 3 characters,
on VNFC name. Example: “oam”, “rdb”, “dbs”, “man”, “iox”, “app”,…

Ansible Directories for other artifacts – VNF (special) other files –
Optional – Example – License file:

.. code-block:: none

 <VNF type>/<Version>/ansible/<Other directory(s)>

CAUTION: On referenced files used/required by playbooks.

-  To avoid missing files, during on-boarding or uploading of Ansible
   Playbooks and related artifacts, all permanent files (not generated
   by playbooks as part of execution), required to run any playbook,
   shall reside under the ansible root directory or below on other
   subdirectories.

-  Any references to files, on includes or other playbook entries, shall
   use relative paths.

-  This is the ansible (root) directory referenced on this
   note (Ansible Server mount point not included):

.. code-block:: none

     <VNF type>/<Version>/ansible/

There will be a soft link to the latest set of Ansible Playbooks for
each VNF type.

VNF type directories use A&AI inventory VNF function code. Ansible
Playbooks will be stored on a Cinder Volume mounted on the Ansible
Servers as /storage. Example:

/storage/vfdb/latest/ansible – This soft link point to the latest set of
playbooks (or the only set)

/storage/vfdb/V16.1/ansible – Root directory for database VNF Ansible
Playbooks for release 16.1

CAUTION: To support this directory structure as the repository to store
Ansible Playbooks run by APPC, APPC API in the Ansible Server side needs
to be configured to run playbooks from directory, not MySQL database.

Ansible Server HTTP will be configured to support APPC REST API requests
to run playbooks as needed, against specific VNF instances, or specific
VM(s) as specified in the request.

ONAP APPC REST API to Ansible Server is documented separately and can be
found under ONAP (onap.org).

**Ansible Server – On-boarding Ansible Playbooks**

Once playbooks are developed following the guidelines listed in prior
section(s), playbooks need to be on-boarded onto Ansible Server(s). In
the future, they’ll be on-boarded and distributed through ONAP, at least
that is the proposed plan, but for now they need to be uploaded
manually. There is work in progress to use a Git as the playbook
repository to store and track playbooks by version, version control.

These are the basic steps to on-board playbooks manually onto the
Ansible Server.

1. Upload CSAR, zip, or tar file containing VNF playbooks and related
   artifacts.

2. Create full directory (using –p option below) to store Ansible
   Playbooks and other artifacts under /storage (or other configured)
   file system.

   a. Includes VNF type using VNF function code 4 characters under
      /storage.

   b. Includes VNF “Version” directory as part of the path to store
      playbooks for this VNF version.

   c. Include generic ansible root directory. Creating full directory
      path as an example:

.. code-block:: none

     $ mkdir –p /storage/vfdb/V16.1/ansible**/**

3. Make this directory (VNF ansible root directory) current directory
   for next few steps:

.. code-block:: none

     cd /storage/vfdb/V16.1/ansible/

4. Extract Ansible Playbooks and other Ansible artifacts associated with
   the playbooks onto the ansible directory. Command depends on the type
   of file uploaded, examples would be:

.. code-block:: none

     tar xvf ..
     unzip …
     bunzip ..

5. Create VNF inventory hosts file with all VMs and
   OA&M IP addresses for all VNF instances with known OA&M IP addresses
   for respective VMs, example:

.. code-block:: none

    $ mkdir inventory

    $ touch inventory/vfdb9904vhosts

    $ cat inventory/vfdb9904vhosts

    [host]
    localhost ansible\_connection=local

    [oam]
    1xx.2yy.zzz.109
    1xx.2yy.zzz.110

    [rdb]
    1xx.2yy.zzz.105
    1xx.2yy.zzz.106

6. (Optional, being deprecated) Create directory to hold default
arguments for each VNF instance,
example:

.. code-block:: none

   $ mkdir –p vars/vfdb9904v
   $ touch vars/vfdb9904v/default\_args.yml
   $ cat vars/vfdb9904v/default\_args.yml
   vm\_config\_oam1\_vnfc\_name: vfdb9904vm001oam001
   vm\_config\_oam1\_hostname: vfdb9904vm001
   vm\_config\_oam1\_provider\_ip\_address: 1xx.2yy.zzz.109

   vm\_config\_oam2\_vnfc\_name: vfdb9904vm002oam001
   vm\_config\_oam2\_hostname: vfdb9904vm002
   vm\_config\_oam2\_provider\_ip\_address: 1xx.2yy.zzz.110

   vm\_config\_rdb1\_vnfc\_name: vfdb9904vm003rdb001
   vm\_config\_rdb1\_hostname: vfdb9904vm003
   vm\_config\_rdb1\_provider\_ip\_address: 1xx.2yy.zzz.105

   vm\_config\_rdb2\_vnfc\_name: vfdb9904vm004rdb001
   vm\_config\_rdb2\_hostname: vfdb9904vm004
   vm\_config\_rdb2\_provider\_ip\_address: 1xx.2yy.zzz.106

   vm\_config\_rdb3\_vnfc\_name: vfdb9904vm005rdb001
   vm\_config\_rdb3\_hostname: vfdb9904vm005
   vm\_config\_rdb3\_provider\_ip\_address: 1xx.2yy.zzz.xxx

   vm\_config\_rdb4\_vnfc\_name: vfdb9904vm006rdb001
   vm\_config\_rdb4\_hostname: vfdb9904vm006
   vm\_config\_rdb4\_provider\_ip\_address: 1xx.2yy.zzz.yyy

NOTE: Please note names in this file shall use underscore “\_” not dots
“.” or dashes “-“.

7. Perform some basic playbook validation running with “--check” option,
   running dummy playbooks or other.

NOTE: Each Ansible Server or cluster of Ansible Server will have its own
credentials to authenticate to VNF VMs. Ansible Server SSH public key(s)
have to be loaded onto VNF VMs during instantiation or other way before
Ansible Server can access VNF VMs and run playbooks. HOT templates used
by heat to instantiate VNFs to be configured by these Ansible Servers running
playbooks shall include the same SSH public key and load them onto VNF VM(s)
as part of instantiation.

Other non-vendor specific playbook tasks need to be incorporated in overall
post-instantiation configuration playbook. Alternative is for company
developed playbooks to be uploaded and executed, after VNF vendor provided
playbooks are run.

**A couple of playbooks used for proof-of-concept testing as examples:**

UpgradePreCheck:

.. code-block:: none

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

.. code-block:: none

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

