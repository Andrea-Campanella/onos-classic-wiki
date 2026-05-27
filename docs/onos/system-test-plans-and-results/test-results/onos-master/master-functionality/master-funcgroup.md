# master-FUNCgroup

FUNCgroup at 29 Sep 2021 22:44:40![FUNCgroup](https://jenkins.onosproject.org/view/QA/job/postjob-VM/lastSuccessfulBuild/artifact/FUNCgroup_master_20-builds_graph.jpg)
> commit 581c8407e613a27aaa573a600828b30a37066fb8 (HEAD, origin/master, origin/HEAD, master)  
> Author: pierventre [pier@opennetworking.org]  
> AuthorDate: Thu Sep 23 19:03:14 2021 +0200  
> Commit: Pier Luigi Ventre [pier@opennetworking.org]  
> CommitDate: Mon Sep 27 19:27:55 2021 +0000  
>   
> [SDFAB-616] Inconsistent format of port number in DhcpRelay  
> --  
> (cherry picked from commit 61bd673eec2282aff175daff141059870db78c7d)

### Case 1: Pull onos branch and build onos on Teststation. - PASS

For loading from params file, and pull and build the latest ONOS package

* 1.1 Constructing test variables - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2: Starting up 5 node(s) ONOS cluster - PASS

Set up ONOS with 5 node(s) ONOS cluster

* 2.1 Apply cell to environment - PASS ![(tick)](../../../../../assets/check.svg)
* 2.2 Uninstalling Atomix - PASS ![(tick)](../../../../../assets/check.svg)
* 2.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.4 Creating ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.5 Installing Atomix - PASS ![(tick)](../../../../../assets/check.svg)
* 2.6 Installing ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.7 Set up ONOS secure SSH - PASS ![(tick)](../../../../../assets/check.svg)
* 2.8 Checking ONOS service - PASS ![(tick)](../../../../../assets/check.svg)
* 2.9 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../assets/check.svg)
* 2.10 Checking ONOS nodes - PASS ![(tick)](../../../../../assets/check.svg)
* 2.11 Checking ONOS applications - PASS ![(tick)](../../../../../assets/check.svg)

### Case 3: Compare ONOS Topology view to Mininet topology - PASS

Compare topology elements between Mininet and ONOS

* 3.1 Copy Mininet topology file - PASS ![(tick)](../../../../../assets/check.svg)
* 3.2 Setup Mininet Topology - PASS ![(tick)](../../../../../assets/check.svg)
* 3.3 Assign switch to controller - PASS ![(tick)](../../../../../assets/check.svg)
* 3.4 Comparing Mininet topology to ONOS topology - PASS ![(tick)](../../../../../assets/check.svg)
* 3.5 Create hosts and start scapy - No Result ![(warning)](../../../../../assets/warning.svg)
* 3.6 Start scapy components - PASS ![(tick)](../../../../../assets/check.svg)

### Case 5: Verify Group of type All are successfully Added - PASS

Install a Group of type ALL Verify the Group is Added Add a flow using the group Send a packet that verifies the action bucket of the group

* 5.1 Add Group using Rest api - PASS ![(tick)](../../../../../assets/check.svg)
* 5.2 Check groups are in ADDED state - PASS ![(tick)](../../../../../assets/check.svg)
* 5.3 Adding flow with Group using rest api - PASS ![(tick)](../../../../../assets/check.svg)
* 5.4 Testing Group by sending packet using Scapy - PASS ![(tick)](../../../../../assets/check.svg)

### Case 6: Delete the Group and Flow added through Rest api - PASS

* 6.1 Deleting Group and Flows - No Result ![(warning)](../../../../../assets/warning.svg)
* 6.2 Deleting the created flow by deviceId and flowId - PASS ![(tick)](../../../../../assets/check.svg)
* 6.3 Deleting the created group by deviceId and appCookie - PASS ![(tick)](../../../../../assets/check.svg)

### Case 7: Verify Group of type INDIRECT are successfully Added - PASS

Install a Group of type INDIRECT Verify the Group is Added Add a flow using the group Send a packet that verifies the action bucket of the group

* 7.1 Add Group using Rest api - PASS ![(tick)](../../../../../assets/check.svg)
* 7.2 Check groups are in ADDED state - PASS ![(tick)](../../../../../assets/check.svg)
* 7.3 Adding flow with Group using rest api - PASS ![(tick)](../../../../../assets/check.svg)
* 7.4 Testing Group by sending packet using Scapy - PASS ![(tick)](../../../../../assets/check.svg)

### Case 6: Delete the Group and Flow added through Rest api - PASS

* 6.1 Deleting Group and Flows - No Result ![(warning)](../../../../../assets/warning.svg)
* 6.2 Deleting the created flow by deviceId and flowId - PASS ![(tick)](../../../../../assets/check.svg)
* 6.3 Deleting the created group by deviceId and appCookie - PASS ![(tick)](../../../../../assets/check.svg)

### Case 10: Stop Mininet and Scapy - PASS

Stopping the current mininet topology to start up fresh

* 10.1 Stopping and Removing Scapy Host Components - PASS ![(tick)](../../../../../assets/check.svg)
* 10.2 Stopping Mininet - PASS ![(tick)](../../../../../assets/check.svg)

### Case 100: - PASS
