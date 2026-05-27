# Cells and ONOS test scripts

The workflow is recommended for developers who wish to use cells and the [stc / onos-\* utility scripts](#) to manage an ONOS development or testing cluster using multiple VMs or hardware servers.

Before starting

* Make sure you have read the [Abstraction and Definitions](../../../administrator-guide/abstractions-and-definitions.md) section in the Administrator Guide on this wiki
* ONOS, being an SDN controller authored in Java, can run on a variety of platforms. However, in the interest of focus, the ONOS team engages primarily in testing on Ubuntu server distributions, specifically *Ubuntu Server LTS 64-bit*. Commands above are related

This page describes a mechanism for setting up a virtual test environment across *multiple* VMs or hardware servers.

If you simply want to do ONOS development with a virtual multi-node ONOS cluster, check out [Mininet and onos.py workflow](mininet-and-onos.py-workflow.md).

This page assumes that the reader has been able to work through [Installing and running ONOS](../../../administrator-guide/installing-and-running-onos.md).

# Overview

Testing and managing a distributed platform like ONOS can become a cumbersome task.

In order to simplify testing and to make it more repeatable, a number of assets, including the aforementioned ONOS scripts, have been developed to make the developer’s  and tester’s lives easier. These are located under *$ONOS\_ROOT*/tools/test/.** [Appendix A](../../appendix-a-list-of-onos-utility-scripts-onos-scripts.md) of this guide provides a listing of available utilities. From your management (in this case development) machine, with few commands you'll be able to:

* Deploy ONOS as a cluster on one or multiple remote target machines
* Deploy an arbitrary Mininet topology on a remote machine and let its the switches connect to the ONOS machines mentioned above
* Test that the ONOS cluster and the Mininet topology came up correctly (i.e. check automatically ONOS logs, number of switches, links, hosts, ...)

# Test Environment Components

Following the model reported in the [Abstractions and Definitions section](../../../administrator-guide/abstractions-and-definitions.md), an ONOS developer's environment may include the following:

* **Management/**Development/build **machine**: for code development - i.e. running the IDE and building/packaging/deploying ONOS.
* One or more ONOS **target machines:** for running ONOS instances
* A **Mininet target machine**: for emulating networks to test with ONOS

In the above case, the ONOS scripts are run from the management machine, and directed towards the target machines. The target machines (both ONOS and Mininet target machines) can be either local or remote, physical, virtual, ...

# Target machines requirements

The following requirements should be satisfied in order to be able to push software configurations on the remote target machines.

## All target machines:

* Be all-to-all reachable at IP layer (basically all machines -including the management machine- need to be able to ping one each other)
* Have a user *sdn* that can be *sudoer* on the machine, without any need to insert the password for it

**Adding the sdn user as sudoer on Ubuntu**

```
sudo visudo
sdn ALL=(ALL) NOPASSWD:ALL     # Add this line at the bottom of the file
```

* Accessing without password from the management machine to the target machines. To do this the public key of the user on the management machine must be present in the .ssh/authorized\_key file on all your target machines.  
  This can be done in two ways: *manually* or (almost) *automatically* using an ONOS script

**Manually (to be executed on the target machine)**

```
ssh-keygen -t rsa         	        # If an .ssh directory is not present under your user directory, generate new SSH keys
vi ~/.ssh/authorized_keys           # Create the authorized_keys file and copy into it your management machine public key (you can find it on the managemnt machine under .ssh/id_rsa.pub)
chmod 700 ~/.ssh			        # Give the correct permissions to your .ssh directory
chmod 600 ~/.ssh/authorized_keys    # Give the correct permissions to your authorized_keys file
```

**Automatically**

```
ssh-keygen -t rsa         	        # TBD on the management machine. If an .ssh directory is not present under your user directory, generate new SSH keys.
onos-push-keys $TARGET_MACHINE_IP   # TBD on the management machine for each target machine
```

* As a proof that everything works, from your management machine you should be able to login into any target machine doing ssh sdn@TARGET\_MACHINE\_IP and execute *sudo echo hello* (for example) with no passwords required

## ONOS target machines

Additionally, ONOS target machines should have

* Oracle Java (at least JRE) 1.8 installed. The [ONOS installation section](../../../administrator-guide/installing-and-running-onos/requirements.md), under the Administration Guide, provides examples for Ubuntu about how to do that.
* curl installed
* make sure the following ports are open:
  + 8181    for REST API and GUI
  + 8101    to access the ONOS CLI
  + 9876    for intra-cluster communication (communication between target machines)
  + 6653    optional, for OpenFlow
  + 6640    optional, for OVSDB

## Mininet target machine

Additionally, the Mininet target machine should have

* Mininet install. This can be simple as typing *sudo apt-get install* mininet. Anyway, for more, and more detailed instructions, please refer directly to the [Mininet website](http://mininet.org/)

## Management/Development/build machine

Some test scenario, such as *smoke*, require external libraries.  (e.g. [requests](http://docs.python-requests.org/en/latest/user/install/#install))  If you see errors like "ImportError: No module named requests" install them on the management machine.

```
pip install requests
```

# Test Cells

Since a developer may want to test different scenarios against different sets of VMs or servers, ONOS provides the notion of **test cells**.

A *test* *cell* refers to a specific target machines environment designated for testing. *Cell definition files* are bash snippets that simply export few environment variables into the developer’s (or tester’s) shell. These variables are then used by a number of the ONOS test and utility scripts. This allows the scripts and test scenarios to be independent to a specific test bench setup.

The cell and cells commands are available on the management machine, where the ONOS repository has been originally cloned.

## Listing existing cells

Cells configured can be listed using the command *cells*.

**cells command output example**

```
$ cells
beast             # Bare metal cluster (7-node)
beast-1           # Bare metal cluster (1-node)
beast-3           # Bare metal cluster (3-node)
beast-5           # Bare metal cluster (5-node)
demo              # LXC demo environment for oneping tutorial
demo-eu           # For demo with GEANT topology and three ONOS instances using vagrant devmachine
demo-eu-single    # For demo with GEANT topology and three ONOS instances using vagrant devmachine
demo-eu-single-vpls *  # For demo with GEANT topology and three ONOS instances using vagrant devmachine
ec2               # EC2-based cluster (7-node)
i2                # SDN-IP ProxMox cell
i2-centos-single  # SDN-IP ProxMox cell
i2-single         # SDN-IP ProxMox cell
local             # Local VirtualBox-based ONOS instances 1,2 & ONOS mininet box
```

Cell definitions are loaded into the shell environment with the *`cell`* utility. This utility takes the name of a cell definition file as the argument. If the command is invoked without parameters, it will just print out the cell in use.

**Cell command output example**

```
$ cell local               # Instruct ONOS to use cell "local"
ONOS_CELL=local
OCI=192.168.56.101
OC1=192.168.56.101
OC2=192.168.56.102
OCN=192.168.56.103
ONOS_FEATURES=openflow
ONOS_NIC=192.168.56.*

$ cell                     # Print the cell currently in use
ONOS_CELL=local
OCI=192.168.56.101
OC1=192.168.56.101
OC2=192.168.56.102
OCN=192.168.56.103
ONOS_FEATURES=openflow
ONOS_NIC=192.168.56.*
```

## Cell files attributes

Below it's reported a list of the basic attributes you can express and find in a cell file.

* **OCI** : the default target machine node IP. This is an alias for OC1.
* **OC[1-N]** : the IP addresses of the ONOS target machines. You can set as many OC instances as you want (depending on the number of ONOS target machines you want to run)
* **OCN** : the IP address of the Mininet target machine
* **ONOS\_FEATURES** : a comma-separated list of bundle names, loaded at startup by an ONOS instances within this cell
* **ONOS\_NIC** : The address block used amongst ONOS instances for inter-controller (clustering) and OpenFlow communication. In the example above, it's assumed that all ONOS instances have an IP address in the subnet 192.168.56.0/24

Once a cell definition is exported, utilities such as `onos` will fall back to using the value set in `OCI` (192.168.56.101 for above) if not given any parameters.

The utility script `cells` can be used to view all available cell definitions. Without parameters, `cell`will list the values associated with the current cell in us`e.`

## Defining cell files

Cell files can be found on your *management machine*, under *$ONOS\_ROOT/tools/test/cells*, where $ONOS\_ROOT is the onos folder containing the ONOS repository files cloned.

When a file is added to this directory, it automatically enables it to be loaded and liste`d using the cell and cells commands``.`

A cell definition file defines values for the aforementioned environment variables. A cell definition file may look like the following:

```
# Defining a cell composed by 3 ONOS target machines and one Mininet target machine

export OCI="192.168.56.101"     # Default ONOS target machine (ONOS 1)
export OC1="192.168.56.101"     # ONOS target machine 1
export OC2="192.168.56.102"     # ONOS target machine 2
export OC3="192.168.56.103"     # ONOS target machine 1
export OCN="192.168.56.110"     # Mininet target machine
export ONOS_NIC=”192.168.56.*”    

# ONOS features to load
export ONOS_FEATURES="openflow"
```

Using environment variables instead of IPs

Once your cell file is loaded you can use the *OCX* name instead, instead of the IP of a certain machine. So, for example you may want to do *ssh sdn@$OC1* instead of *ssh sdn@192.168.56.101*

vicell command

ONOS 1.1.0 and later comes with *vicell* command to ease editing and applying cell definition files. See *vicell -h* for usage details.

# Mininet topologies

Optionally, ONOS test scripts can automatically deploy also a custom Mininet topology for you on a remote Mininet target machine. Custom topologies should be defined in *$ONOS\_ROOT/tools/test/topos*.

## Listing existing topologies

To view the list of the existing topologies with their descriptions, you can use the command *topos*. An asterisk may indicate what topology is currently in use. An example is reported below.

**Topos output command example**

```
$ topos
default *                  # Default US MPLS topology recipe (currently in use)
geant                      # GEANT & Nordnet topology recipe
sdnip                      # SDN-IP topology recipe
uk                         # Simple UK topology recipe
vpls                       # Default VPLS topology recipe
```

## Loading topologies

Topologies can be load with the command *topo $TOPO\_NAME*. The same command without arguments shows the details about the topology loaded.

**Topos output command example**

```
$ topo default             # Load the topology named default
ONOS_TOPO=default
OTH=25
OTL=140
OTD=25

$ topo                     # Print the details about the topology currently loaded
ONOS_TOPO=default
OTH=25
OTL=140
OTD=25
```

## Creating custom topologies

The folder already contains lots of examples that may help you to start to write your first own topology. A topology may include up to 3 files, by convention called the same way, but using different extensions:

* The **Topology recipe file** (.recipe). The topology recipe file lets you define a new topology. This is mandatory, in order to create a new topology. Optionally, it lets you also automatically check (after the virtual network has been deployed) if the the expected number of devices, links and hosts are set. The structure of this file is very simple. An commented example is reported below.
* The **Mininet Python topology file**, (.py) that expresses how the Mininet topology should look like. The file is mandatory if you want to deploy a Mininet topology as well (to create new topologies look at the existing examples shipped with ONOS and/or go on the [Mininet website](http://mininet.org))
* The **ONOS network configuration file** (.json), that lets you specify an ONOS. You can refer to [this guide](../../../administrator-guide/configuring-onos/the-network-configuration-service.md) to learn more about the [ONOS network configuration](../../../administrator-guide/configuring-onos/the-network-configuration-service.md).

**Receipe file example**

```
ONOS_TOPO=default  # A new topology named "default" is declared
export OTD=6       # 6 devices are expected to be found (optional)
export OTL=18      # 18 links are expected to be found (optional)
export OTH=6       # 6 hosts are expected to be found (optional)
```

# Deploy ONOS and the topology STC

The STC command lets you deploy multiple ONOS instances, the Mininet topology and test the environment.

Once your cell file is loaded:

**STC - deploy bits on the ONOS target machines**

```
$ stc setup
$ stc setup
2017-01-27 15:11:52  Setup started
2017-01-27 15:11:52  Push-Bits-1 started -- onos-push-bits 10.100.198.201
2017-01-27 15:11:52  Uninstall-1 started -- onos-uninstall 10.100.198.201
2017-01-27 15:11:55  Push-Bits-1 completed
2017-01-27 15:12:11  Uninstall-1 completed
2017-01-27 15:12:11  Kill-1 started -- onos-kill 10.100.198.201
2017-01-27 15:12:11  Kill-1 completed
2017-01-27 15:12:11  Install-1 started -- onos-install 10.100.198.201
2017-01-27 15:12:22  Install-1 completed
2017-01-27 15:12:22  Secure-SSH-1 started -- onos-secure-ssh -u onos -p rocks 10.100.198.201
2017-01-27 15:12:38  Secure-SSH-1 completed
2017-01-27 15:12:38  Wait-for-Start-1 started -- onos-wait-for-start 10.100.198.201
2017-01-27 15:12:43  Wait-for-Start-1 completed
2017-01-27 15:12:43  Check-Components-1 started -- onos-check-components 10.100.198.201
2017-01-27 15:12:43  Check-Nodes-1 started -- onos-check-nodes 10.100.198.201
2017-01-27 15:12:46  Check-Nodes-1 completed
2017-01-27 15:12:48  Check-Components-1 completed
2017-01-27 15:12:48  Check-Logs-1 started -- onos-check-logs 10.100.198.201
2017-01-27 15:12:48  Check-Apps-1 started -- onos-check-apps 10.100.198.201 drivers,openflow includes
2017-01-27 15:12:49  Check-Logs-1 completed
2017-01-27 15:12:49  Check-Apps-1 completed
2017-01-27 15:12:49  Setup completed
0:56 Passed! 11 steps succeeded
```

**STC - deploy a Mininet target machine and perform basic tests**

```
$ stc net-setup
2017-01-27 15:13:34  Net-Setup started
2017-01-27 15:13:34  Push-Topos started -- onos-push-topos 10.100.198.200
2017-01-27 15:13:34  Stop-Mininet-If-Needed started -- onos-mininet stop
2017-01-27 15:13:34  Push-Topos completed
2017-01-27 15:13:35  Stop-Mininet-If-Needed completed
2017-01-27 15:13:35  Clean-Mininet-If-Needed started -- onos-mininet cleanup
2017-01-27 15:13:37  Clean-Mininet-If-Needed completed
2017-01-27 15:13:37  Wipe-Out-Data-Before started -- onos-wipe-out
2017-01-27 15:13:37  Wipe-Out-Data-Before completed
2017-01-27 15:13:37  Initial-Summary-Check started -- onos-check-summary 10.100.198.201 [0-9]* 0 0 0
2017-01-27 15:13:37  Initial-Summary-Check completed
2017-01-27 15:13:37  Config-Topo started -- onos-netcfg 10.100.198.201 /Users/luca/onos/tools/test/topos/default.json
2017-01-27 15:13:38  Config-Topo completed
2017-01-27 15:13:38  Start-Mininet started -- onos-mininet start topos/topo default.py 10.100.198.201
2017-01-27 15:13:38  Start-Mininet completed
2017-01-27 15:13:38  Wait-For-Mininet started -- onos-mininet wait 10
2017-01-27 15:13:56  Wait-For-Mininet completed
2017-01-27 15:13:56  ARP-Hosts started -- onos-mininet sendAndExpect gratuitousArp --expect .
2017-01-27 15:13:59  ARP-Hosts completed
2017-01-27 15:13:59  Check-Summary started -- onos-check-summary 10.100.198.201 [0-9]* 25 140 25
2017-01-27 15:13:59  Check-Summary completed
2017-01-27 15:13:59  Check-Flows started -- onos-check-flows 10.100.198.201
2017-01-27 15:14:04  Check-Flows completed
2017-01-27 15:14:04  Net-Setup completed
0:30 Passed! 12 steps succeeded
```

More STC scripts

STC scripts can do really much more than this. If you're interested to know more check out [this page](../../appendix-g-scenario-test-coordinator-stc.md)!

# Putting everything together: using the test environment

Let's wrap up! The beauty of the cell system is that it will give you the flexibility to test different ONOS configurations on different Mininet topologies, on different remote machines (regardless they are physical servers, virtual machines, containers, ...).

A typical workflow may look like the following:

1. Make changes to the code
2. Build ONOS with *onos-buck buld onos* (more details [here](../building-onos-and-executing-unit-tests.md))
3. Load the cell settings with *`cell $YOUR_CELL_NAME`*
4. Load your topology with topo *$YOUR\_TOPO\_NAME*
5. Deploy ONOS target machines with *stc setup*
6. Deploy the Mininet topology with *stc net-setup*

The correspondent one line command and the related output is reported below:

**Deploy ONOS and a Mininet topology in one line command**

```
$ cell $YOUR_CELL_NAME && topo $YOUR_TOPO_NAME && stc setup && stc net-setup
```

# Other useful commands

Attach to the remote ONOS machine OCN

```
$ onos-mininet attach
```

Start/Stop/Restart/Check the status of the ONOS service

```
$ onos-service --cell start/stop/restart/status    # instead of cell you can also specify $OCX
```

Kill the ONOS process

```
$ onos-service --cell start/stop/restart    # instead of cell you can also specify $OCX
```
