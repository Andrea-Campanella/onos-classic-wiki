# Master-HA Full Network Partition

HAfullNetPartition at 29 Sep 2021 21:49:28![HAfullNetPartition](https://jenkins.onosproject.org/view/QA/job/postjob-VM/lastSuccessfulBuild/artifact/HAfullNetPartition_master_20-builds_graph.jpg)
> commit 581c8407e613a27aaa573a600828b30a37066fb8 (HEAD, origin/master, origin/HEAD, master)  
> Author: pierventre [pier@opennetworking.org]  
> AuthorDate: Thu Sep 23 19:03:14 2021 +0200  
> Commit: Pier Luigi Ventre [pier@opennetworking.org]  
> CommitDate: Mon Sep 27 19:27:55 2021 +0000  
>   
> [SDFAB-616] Inconsistent format of port number in DhcpRelay  
> --  
> (cherry picked from commit 61bd673eec2282aff175daff141059870db78c7d)

### Case 1: Constructing test variables and building ONOS package - PASS

For loading from params file, and pull and build the latest ONOS package

* 1.1 Constructing test variables - PASS ![(tick)](../../../../../assets/check.svg)
* 1.2 Apply cell to environment - PASS ![(tick)](../../../../../assets/check.svg)
* 1.3 Uninstalling Atomix - PASS ![(tick)](../../../../../assets/check.svg)
* 1.4 Uninstalling ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 1.5 Starting Mininet - PASS ![(tick)](../../../../../assets/check.svg)
* 1.6 Creating ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 1.7 Installing Atomix - PASS ![(tick)](../../../../../assets/check.svg)
* 1.8 Installing ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 1.9 Set up ONOS secure SSH - PASS ![(tick)](../../../../../assets/check.svg)
* 1.10 Checking ONOS service - PASS ![(tick)](../../../../../assets/check.svg)
* 1.11 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../assets/check.svg)
* 1.12 Checking ONOS nodes - PASS ![(tick)](../../../../../assets/check.svg)
* 1.13 Checking ONOS applications - PASS ![(tick)](../../../../../assets/check.svg)
* 1.14 Checking ONOS nodes - PASS ![(tick)](../../../../../assets/check.svg)
* 1.15 Activate apps defined in the params file - No Result ![(warning)](../../../../../assets/warning.svg)
* 1.16 Set ONOS configurations - PASS ![(tick)](../../../../../assets/check.svg)
* 1.17 Check app ids - PASS ![(tick)](../../../../../assets/check.svg)
* 1.18 Set logging levels - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2: Assigning devices to controllers - PASS

Assign switches to ONOS using 'ovs-vsctl' and check that an ONOS node becomes the master of the device.

* 2.1 Assign switches to controllers - PASS ![(tick)](../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - FAIL

Compare topology objects between Mininet and ONOS

* 8.1 Comparing ONOS topology to MN topology - FAIL ![(error)](../../../../../assets/error.svg)

+ ONOS topology don't match Mininet

* 8.2 Hosts view is consistent across all ONOS nodes - PASS ![(tick)](../../../../../assets/check.svg)
* 8.3 Hosts information is correct - PASS ![(tick)](../../../../../assets/check.svg)
* 8.4 Host attachment points to the network - PASS ![(tick)](../../../../../assets/check.svg)
* 8.5 Clusters view is consistent across all ONOS nodes - FAIL ![(error)](../../../../../assets/error.svg)

+ ONOS nodes have different views of clusters

* 8.6 There is only one SCC - PASS ![(tick)](../../../../../assets/check.svg)
* 8.7 Device information is correct - FAIL ![(error)](../../../../../assets/error.svg)

+ Device information is incorrect

* 8.8 Links are correct - PASS ![(tick)](../../../../../assets/check.svg)
* 8.9 Hosts are correct - PASS ![(tick)](../../../../../assets/check.svg)
* 8.10 Checking ONOS nodes - PASS ![(tick)](../../../../../assets/check.svg)

### Case 21: Assigning Controller roles for switches - PASS

Check that ONOS is connected to each device. Then manually assign mastership to specific ONOS nodes using 'device-role'

* 21.1 Assign mastership of switches to specific controllers - PASS ![(tick)](../../../../../assets/check.svg)
* 21.2 Check mastership was correctly assigned - PASS ![(tick)](../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - FAIL

Compare topology objects between Mininet and ONOS

* 8.1 Comparing ONOS topology to MN topology - FAIL ![(error)](../../../../../assets/error.svg)

+ ONOS topology don't match Mininet

* 8.2 Hosts view is consistent across all ONOS nodes - PASS ![(tick)](../../../../../assets/check.svg)
* 8.3 Hosts information is correct - PASS ![(tick)](../../../../../assets/check.svg)
* 8.4 Host attachment points to the network - PASS ![(tick)](../../../../../assets/check.svg)
* 8.5 Clusters view is consistent across all ONOS nodes - FAIL ![(error)](../../../../../assets/error.svg)

+ ONOS nodes have different views of clusters

* 8.6 There is only one SCC - PASS ![(tick)](../../../../../assets/check.svg)
* 8.7 Device information is correct - FAIL ![(error)](../../../../../assets/error.svg)

+ Device information is incorrect

* 8.8 Links are correct - PASS ![(tick)](../../../../../assets/check.svg)
* 8.9 Hosts are correct - PASS ![(tick)](../../../../../assets/check.svg)
* 8.10 Checking ONOS nodes - PASS ![(tick)](../../../../../assets/check.svg)

### Case 3: Adding host Intents - FAIL
