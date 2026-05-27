# master-SR HA Upgrade Rollback

HAupgradeRollback at 16 Feb 2019 11:20:39![HAupgradeRollback](https://jenkins.onosproject.org/view/QA/job/postjob-Fabric/lastSuccessfulBuild/artifact/HAupgradeRollback_master_20-builds_graph.jpg)
> commit aeabca7c86aca6a76a5debcc84df796d5f0426d3 (HEAD -] master, origin/master, origin/HEAD)  
> Author: Jonghwan Hyun [jonghwan@opennetworking.org]  
> AuthorDate: Thu Feb 14 12:34:47 2019 +0000  
> Commit: Carmelo Cascone [carmelo@opennetworking.org]  
> CommitDate: Sat Feb 16 00:17:26 2019 +0000  
>   
> [ONOS-7931] Add table id mapping for basic pipeline

### Case 1: Constructing test variables and building ONOS package - PASS

For loading from params file, and pull and build the latest ONOS package

* 1.1 Constructing test variables - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.2 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.3 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.4 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.5 Copying backup config files - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.6 Creating ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.7 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.8 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.9 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.10 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.11 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.12 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.13 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.14 Clean up ONOS service changes - No Result ![(warning)](../../../../../../assets/warning.svg)
* 1.15 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.16 Activate apps defined in the params file - No Result ![(warning)](../../../../../../assets/warning.svg)
* 1.17 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.18 Check app ids - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.19 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 102: Starting Mininet Topology - PASS

* 102.1 Pushing Network config - PASS ![(tick)](../../../../../../assets/check.svg)
* 102.2 Check Network config - PASS ![(tick)](../../../../../../assets/check.svg)
* 102.3 Start Mininet topology - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - FAIL
