# master-VPLSBasic

VPLSBasic at 21 Sep 2021 21:22:36![VPLSBasic](https://jenkins.onosproject.org/view/QA/job/postjob-BM/lastSuccessfulBuild/artifact/VPLSBasic_master_20-builds_graph.jpg)
> commit 18fdda8cb850b6e6f22f98180f4e1c35e6267b5e (HEAD -] master, origin/master, origin/HEAD)  
> Author: Andrea Campanella [andrea@opennetworking.org]  
> AuthorDate: Mon Sep 13 12:37:36 2021 +0200  
> Commit: Andrea Campanella [andrea@opennetworking.org]  
> CommitDate: Mon Sep 20 07:18:54 2021 +0000  
>   
> [VOL-4343] Processing status of ports in order with mastership and connection/disconnection to avoid inconsisten state  
> --  
> (cherry picked from commit b0b93ac609e7860d5fd15703a50a0180fbf7a176)  
> (cherry picked from commit 727ed68ed3edc4512e353af814abe327ee25f143)

### Case 1: Starting up 3 node(s) ONOS cluster - PASS

Set up ONOS with 3 node(s) ONOS cluster

* 1.1 Constructing test variables - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.2 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.3 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.4 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.5 Creating ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.6 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.7 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.8 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.9 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.10 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.11 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.12 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.13 Starting Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.14 Activate apps defined in the params file - No Result ![(warning)](../../../../../../assets/warning.svg)
* 1.15 Set ONOS configurations - No Result ![(warning)](../../../../../../assets/warning.svg)
* 1.16 App Ids check - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 2: - PASS

* 2.1 Discover hosts using pings - No Result ![(warning)](../../../../../../assets/warning.svg)
* 2.2 Load VPLS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.3 Check interface configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.4 Check network configurations for vpls application - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.5 Check vpls app configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.6 Check connectivity - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.7 Loading vpls configuration in case any configuration was missed. - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 10: - PASS

* 10.1 Remove an interface from a vpls network - No Result ![(warning)](../../../../../../assets/warning.svg)
* 10.2 Check network configurations for vpls application - PASS ![(tick)](../../../../../../assets/check.svg)
* 10.3 Check vpls app configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 10.4 Check connectivity - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 11: - PASS

* 11.1 Clean all vpls configurations - No Result ![(warning)](../../../../../../assets/warning.svg)
* 11.2 Check network configurations for vpls application - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.3 Check vpls app configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.4 Check connectivity - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 12: - PASS

* 12.1 Create a new vpls network - No Result ![(warning)](../../../../../../assets/warning.svg)
* 12.2 Check network configurations for vpls application - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.3 Check vpls app configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.4 Check connectivity - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 13: - PASS

* 13.1 Add interfaces to the network - No Result ![(warning)](../../../../../../assets/warning.svg)
* 13.2 Check network configurations for vpls application - PASS ![(tick)](../../../../../../assets/check.svg)
* 13.3 Check vpls app configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 13.4 Check connectivity - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 14: - PASS

* 14.1 Add MPLS encapsulation to a vpls network - No Result ![(warning)](../../../../../../assets/warning.svg)
* 14.2 Check network configurations for vpls application - PASS ![(tick)](../../../../../../assets/check.svg)
* 14.3 Check vpls app configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 14.4 Check connectivity - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 15: - PASS

* 15.1 Change an encapsulation type - No Result ![(warning)](../../../../../../assets/warning.svg)
* 15.2 Check network configurations for vpls application - PASS ![(tick)](../../../../../../assets/check.svg)
* 15.3 Check vpls app configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 15.4 Check connectivity - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 16: - PASS

* 16.1 Remove encapsulation - No Result ![(warning)](../../../../../../assets/warning.svg)
* 16.2 Check network configurations for vpls application - PASS ![(tick)](../../../../../../assets/check.svg)
* 16.3 Check vpls app configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 16.4 Check connectivity - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 11: - PASS

* 11.1 Clean all vpls configurations - No Result ![(warning)](../../../../../../assets/warning.svg)
* 11.2 Check network configurations for vpls application - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.3 Check vpls app configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.4 Check connectivity - PASS ![(tick)](../../../../../../assets/check.svg)
