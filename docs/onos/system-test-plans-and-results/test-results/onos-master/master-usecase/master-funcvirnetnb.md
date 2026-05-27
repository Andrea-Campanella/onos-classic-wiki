# Master-FUNCvirNetNB

FUNCvirNetNB at 28 Sep 2021 22:14:22![FUNCvirNetNB](https://jenkins.onosproject.org/view/QA/job/postjob-BM/lastSuccessfulBuild/artifact/FUNCvirNetNB_master_20-builds_graph.jpg)
> commit 581c8407e613a27aaa573a600828b30a37066fb8 (HEAD -] master, origin/master, origin/HEAD)  
> Author: pierventre [pier@opennetworking.org]  
> AuthorDate: Thu Sep 23 19:03:14 2021 +0200  
> Commit: Pier Luigi Ventre [pier@opennetworking.org]  
> CommitDate: Mon Sep 27 19:27:55 2021 +0000  
>   
> [SDFAB-616] Inconsistent format of port number in DhcpRelay  
> --  
> (cherry picked from commit 61bd673eec2282aff175daff141059870db78c7d)

### Case 1: Starting up 3 node(s) ONOS cluster - FAIL

Set up ONOS with 3 node(s) ONOS cluster

* 1.1 Constructing test variables - PASS ![(tick)](../../../../../assets/check.svg)
* 1.2 Apply cell to environment - PASS ![(tick)](../../../../../assets/check.svg)
* 1.3 Uninstalling Atomix - PASS ![(tick)](../../../../../assets/check.svg)
* 1.4 Uninstalling ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 1.5 Creating ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 1.6 Installing Atomix - PASS ![(tick)](../../../../../assets/check.svg)
* 1.7 Installing ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 1.8 Set up ONOS secure SSH - PASS ![(tick)](../../../../../assets/check.svg)
* 1.9 Checking ONOS service - PASS ![(tick)](../../../../../assets/check.svg)
* 1.10 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../assets/check.svg)
* 1.11 Checking ONOS nodes - PASS ![(tick)](../../../../../assets/check.svg)
* 1.12 Checking ONOS applications - PASS ![(tick)](../../../../../assets/check.svg)
* 1.13 App Ids check - PASS ![(tick)](../../../../../assets/check.svg)
* 1.14 Install org.onosproject.vtn app - FAIL ![(error)](../../../../../assets/error.svg)

+ Install org.onosproject.vtn app failed

### Case 2: Virtual Network NBI Test - Network - FAIL
