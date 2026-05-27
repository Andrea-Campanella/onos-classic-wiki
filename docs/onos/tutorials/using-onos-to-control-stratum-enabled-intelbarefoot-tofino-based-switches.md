# Using ONOS to control Stratum-enabled Intel/Barefoot Tofino-based switches

This guide does NOT provide detailed instructions, but rather, pointers to existing guides that we hope should give you enough information to set up an ONOS environment capable of controlling Intel/Barefoot Tofino-based switches running Stratum.

[Stratum](https://github.com/stratum/stratum) is a software agent that runs on the switch and exposes gRPC-based interfaces such as P4Runtime, gNMI, and gNOI. These interfaces are used by ONOS to control and configure the switch.

The steps to follow are:

1. Learn the basics of the Stratum-ONOS stack by doing the **Next-Gen SDN Tutorial** (based on Mininet and the BMv2 software switch)
2. Learn to **install and run the Stratum agent on your Tofino-based switch**
3. Learn how to **deploy an existing ONOS pipeconf** to your Tofino switch
4. **Use the acquired knowledge** and code to create a pipeconf and ONOS apps that work with your own P4 program

# 1 - Learn the basics with the Next-Gen SDN Tutorial

Before experimenting with real hardware, and facing all the complexities associated with making things work for the first time, we strongly encourage you to understand the basic concepts of the Stratum-ONOS stack by doing this hands-on tutorial based on Mininet and the BMv2 software switch. Most of the provided code and instructions can be applied to the case of a network comprising real Tofino-based switches.

The tutorial is organized around a sequence of hands-on exercises that show how to build an IPv6-based leaf-spine data center fabric using P4, Stratum, and ONOS. It provides an introduction to concepts such as:

* Data plane programming and control via P4 and P4Runtime
* Device/port configuration via YANG, OpenConfig, and gNMI
* Running and operating ONOS
* Using ONOS to deploy an arbitrary P4 program to the network switches
* Implementing ONOS apps that provide the control plane logic for the data plane P4 programs

**NG-SDN Tutorial repository**

The tutorial instructions, along with slides, are available at this URL:

<https://github.com/opennetworkinglab/ngsdn-tutorial>

# 2 - Install and run Stratum on your Tofino-based switch

Stratum currently supports different Tofino-based switches, from different vendors. **To learn if your switch supports Stratum**, check out the main README of the GitHub Stratum repository:

<https://github.com/stratum/stratum/blob/master/README.md>

**To install and run Stratum** on a Tofino-based switch, use the following instructions:

<https://github.com/stratum/stratum/tree/master/stratum/hal/bin/barefoot>

*Hint: consider using the proposed [Docker-based](https://github.com/stratum/stratum/tree/master/stratum/hal/bin/barefoot/docker)* *approach to install and Stratum with minimal effort*

# 3 - Learn how to deploy a Tofino-enabled pipeconf

From the NG-SDN tutorial, you should have learned that ONOS uses "pipeconfs" to deploy and manage a given P4 program on a device. Pipeconfs are distributed as ONOS applications, hence using the `.oar` packaging.

Most of the pipeconfs already available in ONOS, as well as that provided in the NG-SDN Tutorial, work only with the BMv2 software switch. To learn how to create and deploy pieconfs that can work with real Tofino-enabled switches, you can check out the [fabric-tofino](https://github.com/opencord/fabric-tofino) GitHub repository. [fabric.p4](https://github.com/opennetworkinglab/onos/tree/master/pipelines/fabric/impl/src/main/resources) is an open-source P4 program distributed as part of ONOS, designed to work with [Trellis](https://github.com/opencord/fabric-tofino/blob/master/trellis), a set of SDN applications running on top of ONOS to provide the control plane for an IP fabric based on MPLS segment-routing.

The [fabric-tofino](https://github.com/opencord/fabric-tofino) GitHub repository provides instructions on how to:

* Build a pipeconf .oar package for fabric.p4 that includes the output of the P4 compiler for Tofino (tofino.bin and context.json)
* Install the pipeconf in a running ONOS instance
* Tell ONOS to connect and to deploy the pipeconf to the Stratum agent running on the switch

**fabric-tofino repository**

Detailed Instructions are available in the main README of the fabric-tofino repository:

<https://github.com/opencord/fabric-tofino>

# 4 - Use the acquired knowledge and code

You should now know everything you need to:

* Create a pipeconf package for your own P4 program (check the [PipeconfLoader.java](https://github.com/opencord/fabric-tofino/blob/master/src/main/java/org/opencord/fabric/tofino/PipeconfLoader.java) class from fabric-tofino for an example of how to include the tofino.bin and context.json)
* Load the pipeconf in ONOS and deploy it to your switch (using the [example netcfg.json](https://github.com/opencord/fabric-tofino/blob/master/tofino-netcfg.json) provided in fabric-tofino)
* Implement an ONOS app to manage the tables and other entities of your P4 program (using the [app provided in the ng-sdn tutorial](https://github.com/opennetworkinglab/ngsdn-tutorial/tree/master/app) as an example)

# Get help

If you need help, you can ask questions on the following mailing lists:

* To get help with **ONOS**: [onos-dev mailing list](https://groups.google.com/a/onosproject.org/forum/#!forum/onos-dev)
* To get help with **Stratum**:  [stratum-dev mailing list](https://lists.stratumproject.org/)

For issues concerning Tofino and other Intel/Barefoot products (e.g., P4 compiler errors), please reach out to Barefoot support channels.
