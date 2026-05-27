# Appendix H: ONOS+P4 Development Environment

DEPRECATED

The content of this page is outdated. Please check the NG-SDN Tutorial for a reference ONOS+P4 development environment:

<https://github.com/opennetworkinglab/ngsdn-tutorial>

[P4](http://www.p4.org/) is a programming language to define the behavior of the data plane, it can be used to program targets such as software switches, reconfigurable ASICs or FPGAs, or it can be used to formally specify the behavior of a fixed-function switch. P4Runtime is a protocol to control at runtime a P4-defined pipeline, for example, to install entries in a match+action table defined in the P4 program. This page provides steps to set up an environment to try ONOS with the[Behavioral Model v2](https://github.com/p4lang/behavioral-model) (BMv2) (the reference P4 software switch). Support for P4Runtime has been included in ONOS starting from the 1.11 (Loon) release.

This document assumes you are already familiar with ONOS, P4, P4Runtime and BMv2. If this is not the case, **here's a list of pointers to get started:**

* [What's ONOS?](#)
* [ONOS Administrator Guide](../administrator-guide.md)
* [ONOS Developer Guide](../developer-guide.md)
* [P4 white paper](http://www.sigcomm.org/sites/default/files/ccr/papers/2014/July/0000000-0000004.pdf)
* [P4 language specification](http://p4.org/spec/)
* [BMv2 slides at 2016 P4 workshop](http://schd.ws/hosted_files/2016p4workshop/9f/Barefoot%2C%20Antonin%2C%20P4%20workshop%202016.pdf)
* [P4Runtime resources](https://p4.org/p4-runtime/)

ONOS+P4 tutorial for beginners

If this is the first time working with ONOS and/or P4, we strongly suggest you start from this tutorial:

**[ONOS+P4 Tutorial for Beginners](../../tutorials/onosp4-tutorial-for-beginners.md)**

## Table of Contents

## Overview

For an overview of how P4 and P4Runtime are supported in ONOS, please refer to this presentation (ONF Connect, December 2018):

**[Click here to open the slides in a new window](https://docs.google.com/presentation/d/1ji2jSlP2FCX89qQsTdRLykg5-GhQ6AYEWrUkpgm9VF8/edit?usp=sharing)**

**[Video recording](https://vimeo.com/307549630/ff38da82dc)**

## Features at a Glance

By using ONOS, you'll be able to program and control a network comprising P4Runtime-enabled devices with all the benefits of a logically centralized SDN platform. The following features are currently supported:

* Device discovery
* P4 pipeline provisioning (at device connection)
* Match-action table operations (via existing ONOS APIs such as FlowRule, FlowObjective, or Intent)
* Action profile group/member operations (via Group ONOS API)
* Controller packet-in and packet-out
* Counter reads

## ONOS+P4 Developer VM

We have created a special VM with all you need to test P4Runtime support in ONOS.

You can use the following link to download an Open Virtual Appliance (OVA) package to be imported using VirtualBox or any other x86 virtualization system that supports this format.

**[Click here to download the ONOS+P4 Developer VM (approx. 2.5 GB)](http://onlab.vicci.org/onos/onos-p4-dev.ova) (last updated 2019-05-16)**

Alternatively, you can use [these instructions](https://github.com/opennetworkinglab/onos/tree/master/tools/dev/p4vm) to build a VM locally using Vagrant.

VM login credentials

The VM comes with one user with sudo privileges. Use these credentials to log in:

Username: `sdn`

Password: `rocks`

### VM Contents

The VM is based on Ubuntu 18.04 (cloud image) and contains the following software pre-installed:

* ONOS
* BMv2 simple\_switch\_grpc (P4 software switch with P4Runtime support)
* p4c (P4 compiler)
* Mininet (network emulator)

### Recommended System Requirements

The VM is configured with 4 GB of RAM and 2 CPU cores, while the disk has size of approx. 8 GB. For a flawless experience, we recommend running the VM on a host system that has at least the double of resources.

These are the recommended minimum requirements to be able to run a Mininet network with 1-10 BMv2 devices controlled by 1 ONOS instance. To emulate larger networks with multiple instances of ONOS (for example using [onos.py](#)), we recommend configuring the VM to use at least 4 CPU cores.

### VM Connectivity

The VM comes with two network interfaces: a NATed interface that provides access to internet (`eth0`), and a host-only one (`eth1`). Once you are able to access the VM, use `ifconfig` (or your command of choice) to get the IP address of the host-only interface. You will need that later to SSH or access the ONOS GUI from your host system. Alternatively, if your host system supports zeroconf networking via mDNS (e.g. Bonjour in OS X, or Avahi in Linux) then you can use the hostname *onos-p4-dev.local* to access the VM. For example, to SSH into the VM's guest system:

```
$ ssh sdn@onos-p4-dev.local
```

**Important**Interface naming inside the VM is not guaranteed, please use your linux/networking/VirtualBox skills to figure out which interface is the host-only one. It should be the one named `eth1`, but that's not guaranteed. Similarly, make sure that VirtualBox is configured correctly such that the host-only interface can ping your host system.

**Important 2**Without trying to tell you how to live your life, we do recommend for your convenience to set up SSH access to the VM (e.g. copying SSH keys for faster access), as you will need to use multiple terminal shells at the same time. The Ubuntu system in the VM comes already equipped with an SSH server on port 22.

### Known issues

* VirtualBox shared folders are not mounted on startup on Ubuntu 18.04 even if "auto-mount" flag is set. To fix it

  ```
  $ sudo systemctl edit --full vboxadd-service
  ```

  and remove systemd`-timesync.service` from the `Conflicts=` line, then reboot ([source](https://superuser.com/questions/1351003/after-upgrade-to-ubuntu-lts-18-virtualbox-shared-folders-marked-auto-mount-do))

## Walkthrough

This walkthrough demonstrates the necessary steps and commands to run a network of BMv2 devices in Mininet, controlled by ONOS using P4Runtime.

In this example, the BMv2 devices will be configured with a sample P4 program that is provided by ONOS, named `basic.p4`.

If not differently specified, *the following commands have to be executed in a terminal shell of the VM.*

1. **Build ONOS master**

   ```
   $ cd ~/onos
   $ git pull origin master
   $ bazel build onos
   ```
2. **Run ONOS**

   ```
   $ export ONOS_APPS=drivers.bmv2,proxyarp,lldpprovider,hostprovider,fwd
   $ bazel run onos-local -- clean
   ```

   The variable `ONOS_APPS` indicates which ONOS applications to execute at ONOS boot. The list includes the BMv2 drivers (based on P4Runtime), the Proxy ARP application, the LLDP Link Provider, the Host Location Provider, and the Reactive Forwarding application. These applications combined together provide ONOS with capabilities to discover the topology (via injection of LLDP packets), the hosts (by intercepting and handling ARP requests) and to provide basic point-to-point connectivity.
3. On a second terminal shell, **access the ONOS command line**:

   ```
   $ onos localhost
   ```
4. **Check that all applications have been loaded successfully**. On the ONOS command line, type:

   ```
   onos> apps -s -a
   ```

   You should see an output similar to this (depending on your startup apps defined in $ONOS\_APPS)

   |  |
   | --- |
   | `* 10 org.onosproject.drivers 1.13.0.SNAPSHOT Default Drivers` `* 35 org.onosproject.generaldeviceprovider 1.13.0.SNAPSHOT General Device Provider` `* 36 org.onosproject.protocols.grpc 1.13.0.SNAPSHOT gRPC Protocol Subsystem` `* 37 org.onosproject.protocols.p4runtime 1.13.0.SNAPSHOT P4Runtime Protocol Subsystem` `* 38 org.onosproject.p4runtime 1.13.0.SNAPSHOT P4Runtime Provider` `* 39 org.onosproject.drivers.p4runtime 1.13.0.SNAPSHOT P4Runtime Drivers` `* 42 org.onosproject.proxyarp 1.13.0.SNAPSHOT Proxy ARP/NDP` `* 44 org.onosproject.hostprovider 1.13.0.SNAPSHOT Host Location Provider` `* 45 org.onosproject.lldpprovider 1.13.0.SNAPSHOT LLDP Link Provider` `* 73 org.onosproject.pipelines.basic 1.13.0.SNAPSHOT Basic Pipelines` `* 119 org.onosproject.drivers.bmv2 1.13.0.SNAPSHOT BMv2 Drivers` `* 146 org.onosproject.fwd 1.13.0.SNAPSHOT Reactive Forwarding` |
5. **Start Mininet.** On third VM terminal shell, type:

   ```
   $ sudo -E mn --custom $BMV2_MN_PY --switch onosbmv2 --controller remote
   ```

   This will run a simple Mininet topology with 2 hosts connected to a BMv2 switch, to use a different topology please refer to the [Mininet guide](http://mininet.org/walkthrough/#changing-topology-size-and-type). The `-E` argument in sudo ensures that all environment variables are exported to the root user. $BMV2\_MN\_PY is used to point to the location of the Mininet custom file [bmv2.py](https://github.com/opennetworkinglab/onos/blob/master/tools/dev/mininet/bmv2.py) provided in ONOS. If successful, the output of the previous command should be similar to this:

   |  |
   | --- |
   | ``` *** Creating network *** Adding controller *** Adding hosts: h1 h2 *** Adding switches: s1 *** Adding links: (h1, s1) (h2, s1) *** Configuring hosts h1 h2 *** Starting controller c0 *** Starting 1 switches s1 Starting BMv2 target: simple_switch_grpc --device-id 0 -i 1@s1-eth1 -i 2@s1-eth2 --log-console -Lwarn --thrift-port 38148 --no-p4 -- --cpu-port 255 --grpc-server-addr 0.0.0.0:37346 [1] 2370 ```  ```  ```  ``` *** Starting CLI: mininet> ``` |

   bmv2.py custom Mininet script

   When using the bmv2.py custom Mininet script, files related to the execution of the BMv2 switch are stored under `/`tmp. The name of these files depends on the switch name used in Mininet, e.g. s1, s2, etc. Example of these files are:

   `bmv2-s1-`grpc`-port`: contains the port used by the P4Runtime server executed by the BMv2 simple\_switch\_grpc instance named 's1'  
   `bmv2-s1-log`: contains the BMv2 log  
   `bmv2-s1-`netcfg`.json`: netcfg blob pushed to ONOS to discover the switch

   bm-\* commands

   The VM comes with a number command aliases to aid in the debugging of BMv2 when executed as part of Mininet. These commands all take one parameter, the switch name used in Mininet, e.g. s1, s2, etc.

   | Command | Description |
   | --- | --- |
   | ``` bm-log ``` | Shows a live scrolling view of the given BMv2 switch instance log |
   | ``` bm-cli ``` | Access the BMv2 CLI, useful to dump table entries, etc. **WARNING**: *this CLI uses the BMv2 Thrift-based APIs which capabilities overlap with P4Runtime (e.g. a table management is provided by both). For this reason, there could be inconsistency issues when using both APIs to write state to the switch. For example, if one tries to insert a table entry using Thrift, the same cannot be read using P4Runtime. In general, to avoid such issues, we suggest using this CLI only to read state, or to write state that is not managed by P4Runtime.* |
   | ``` bm-dbg ``` | Starts the BMv2 debugger |
   | ``` bm-nmsg ``` | Start the BMv2 nanomsg event logger client |
6. **Check that the BMv2 switch has successfully connected to ONOS**. On the ONOS command line, check the output of the following command.

   |  |
   | --- |
   | `onos> devices`  `id=device:bmv2:1, available=false, local-status=connected 9m33s ago, role=NONE, type=SWITCH, mfr=p4.org, hw=master, sw=master, serial=unknown, driver=bmv2:org.onosproject.pipelines.basic, locType=geo, name=device:bmv2:1, protocol=[p4runtime]` |

   From the output, we can see that the BMv2 switch is connected (`available=true`), along with information on the P4 program (pipeconf) deployed (`driver=bmv2:org.onosproject.pipelines.basic`) and on the protocol used to control the switch (`protocol=[p4runtime]`).
7. **Check that the 2 hosts can ping each other**. On the Mininet command line, use the `pingall` command check the output:

   ```
   mininet> pingall
   *** Ping: testing ping reachability
   h1 -> h2
   h2 -> h1
   *** Results: 0% dropped (2/2 received)
   ```

## Update P4 tools to the latest version

Since P4Runtime is a work-in-progress effort, we frequently update ONOS to support the most recent capabilities. Similarly, we update the version of the P4 tools (BMv2, P4Runtime, and p4c) in the VM. Use the following commands to update ONOS and the P4 tools to the latest version:

```
$ cd ~/onos/
$ git pull origin master
$ onos-setup-p4-dev
```

The `onos-setup-p4-dev` command will download and build the most recent version of the P4 tools. In case of errors, please remove any build artifact from previous executions:

```
$ rm -rf ~/p4tools
$ onos-setup-p4-dev
```
