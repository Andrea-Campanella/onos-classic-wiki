# [Archived] Software Switch Installation Guide

Deprecated

This page is deprecated and may be removed in a near future.  
The new entry point of Trellis underlay fabric installation guide can be found at [Fabric Installation Guide](https://wiki.opencord.org/display/CORD/Fabric+Installation+Guide).

## Introduction

In this article, we are going to show you how to setup a CORD Fabric environment with Mininet and CpqD software switches.  
This pure software environment allows us to develop and test the control logic (i.e. the Segment Routing app on ONOS) without any hardware switches.

## ONOS

Setup an ONOS cluster with 3 instances. Here we only show brief steps. Please refer to [Installing and running ONOS](../../guides/administrator-guide/installing-and-running-onos.md) for detail.

1. Fetch and compile ONOS
2. Enable Segment Routing applications in your cell configuration:

   ```
   ONOS_APPS=drivers,openflow,segmentrouting
   ```
3. Configure Segment Routing

   You can copy and modify from the following sample json file:

   ```
   $ONOS_ROOT/tools/package/config/samples/network-cfg-fabric-2x2-min.json
   ```

   By default ONOS will use SpringOpen pipeline for CPqD switches. Addition configuration is required if you wish to use OFDPA pipeline. Please refer to [this page](https://github.com/onfsdn/atrium-docs/wiki/Network-Config-Fabric-16A#configuring-devices) for detail.

   1. Running remotely (1, 3+ instances)

      Run *stc setup* to start ONOS.  
      Push the sample json file to the remote machine using *onos-netcfg* command.

      ```
      onos-netcfg <IP> $ONOS_ROOT/tools/package/config/samples/network-cfg-fabric-2x2-min.json
      ```
   2. Running locally (1 instance)  
      Copy the sample json file to the following location and rename it to *network-cfg.json*:

      ```
      ~/Application/config/network-cfg.json
      ```

      Run *ok clean*to start ONOS with the new configuration.

Right now segment routing does not support dynamic configuration. Restarting segment routing app is required after pushing new config

## Mininet and CpqD Software Switch

1. 1. Install Mininet from source code. Please refer to [Install Mininet from source code](http://mininet.org/download/#option-2-native-installation-from-source) for detail.

      **Fetch Mininet**

      ```
      $ git clone git://github.com/mininet/mininet
      $ cd mininet
      $ git checkout -b 2.2.1 2.2.1
      ```
   2. Patch Mininet.

      We will probably commit this back to the Mininet main stream.

      A patch [multi\_controller.patch](../../../assets/multi_controller.patch) is required to allow CpqD software switches to connect to multiple controller instances simultaneously.   
      Apply the patch using:

      **Patch Mininet**

      ```
      # In the Mininet root directory 
      $ git apply multi_controller.patch
      ```
   3. Install Mininet and CpqD Software Switch

      **Install Mininet**

      ```
      $ sudo ./util/install.sh -n3f
      ```

## Start the Fabric

1. 1. Start the Fabric  
      We write a Mininet script [cord\_fabric.py](../../../assets/cord_fabric.py) that can help you easily create a leaf-spine topology with CpqD software switches.

      Check cell configuration

      Since cord\_fabric.py reads controller information from cell configuration, you should check your cell and see if $OC[1-9] is correctly set up before running the script.

      **Start the leaf-spine topology**

      ```
      $ sudo -E ./cord_fabric.py --spine=2 --leaf=2 
      ```
   2. Run pingall

      **Test host connectivity**

      ```
      mininet> pingall
      *** Ping: testing ping reachability
      h1 -> h2 h3 h4
      h2 -> h1 h3 h4
      h3 -> h1 h2 h4
      h4 -> h1 h2 h3
      *** Results: 0% dropped (12/12 received)
      ```

## (Optional) GUI Configuration

1. 1. Configure sprites

      ```
      $ onos-upload-sprites $OC1 onos/web/gui/src/main/webapp/data/sprites/segmentRouting.json
      ```

      and then access the URL: **http://<ONOS\_IP>/onos/ui?sprites=segmentRouting**
   2. Configure topology view

      ```
      $ onos-topo-cfg $OC1 onos/tools/test/topos/cord.json
      ```
