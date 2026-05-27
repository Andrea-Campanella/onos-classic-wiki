# master-SR Switch Failure

SRSwitchFailure at 24 Sep 2021 20:07:21![SRSwitchFailure](https://jenkins.onosproject.org/view/QA/job/postjob-Fabric4/lastSuccessfulBuild/artifact/SRSwitchFailure_master_20-builds_graph.jpg)
> commit b53d626fb03195129c0ec0802e1f953f85dcbef8 (HEAD -] master, origin/master, origin/HEAD)  
> Author: pierventre [pier@opennetworking.org]  
> AuthorDate: Wed Sep 22 11:24:38 2021 +0200  
> Commit: Pier Luigi Ventre [pier@opennetworking.org]  
> CommitDate: Thu Sep 23 07:38:36 2021 +0000  
>   
> [SDFAB-612] Cluster not ready when using recent tost master images  
> --  
> (cherry picked from commit ec0e942320ef27932b4173172055151015261d7c)

### Case 1: Switch Failure test with 2x2 leaf-spine topology and 1 Onos - PASS

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
* 1.13 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.14 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.15 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.16 Check whether the flow count is >= 116 - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.17 Check whether all flow status are ADDED - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.18 Verify full connectivity for [u'h1', u'h2', u'h3', u'h4'] with tag CASE1 - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.19 Verify full connectivity for [u'olt10', u'vsg10'] with tag CASE1 - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.20 Verify full connectivity for [u'olt5', u'vsg5'] with tag CASE1 - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.21 Kill ['spine101'] - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.22 Verify full connectivity for [u'h1', u'h2', u'h3', u'h4'] with tag CASE1\_Failure - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.23 Verify full connectivity for [u'olt10', u'vsg10'] with tag CASE1\_Failure - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.24 Verify full connectivity for [u'olt5', u'vsg5'] with tag CASE1\_Failure - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.25 Recovering ['spine101'] - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.26 Check whether the flow count is >= 116 - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.27 Check whether all flow status are ADDED - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.28 Verify full connectivity for [u'h1', u'h2', u'h3', u'h4'] with tag CASE1\_Recovery - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.29 Verify full connectivity for [u'olt10', u'vsg10'] with tag CASE1\_Recovery - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.30 Verify full connectivity for [u'olt5', u'vsg5'] with tag CASE1\_Recovery - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.31 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.32 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)
