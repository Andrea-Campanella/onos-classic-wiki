# master-SR Dynamic

SRDynamic at 25 Sep 2021 11:59:52![SRDynamic](https://jenkins.onosproject.org/view/QA/job/postjob-Fabric4/lastSuccessfulBuild/artifact/SRDynamic_master_20-builds_graph.jpg)
> commit 7d13b59ecf0968dae20a3ccee7c59cad3f21f66d (HEAD -] master, origin/master, origin/HEAD)  
> Author: Jian Li [pyguni@gmail.com]  
> AuthorDate: Fri Sep 24 15:08:53 2021 +0900  
> Commit: Jian Li [pyguni@gmail.com]  
> CommitDate: Fri Sep 24 06:51:38 2021 +0000  
>   
> Fix: make protocol field optional in kubevirt load balancer  
> --  
> (cherry picked from commit 70d491cba5689d69708568f693b92432ebe52ba5)

### Case 1: Bridging and Routing sanity test with 2x2 leaf-spine topologyand 1 nodes. - FAIL

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
* 1.19 Verify full connectivity for [u'olt10', u'vsg10'] with tag CASE1 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 1.20 Verify full connectivity for [u'olt5', u'vsg5'] with tag CASE1 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 1.21 Pushing new configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 1.22 Pushing new configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 1.23 Check whether the flow count is >= 140 - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.24 Check whether all flow status are ADDED - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.25 Verify full connectivity for [u'h1', u'h2', u'h3', u'h4', 'in1', 'out1'] with tag CASE1 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 1.26 Verify full connectivity for [u'olt10', u'vsg10'] with tag CASE1 - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.27 Verify full connectivity for [u'olt5', u'vsg5'] with tag CASE1 - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.28 Verify full connectivity for ['olt1', 'vsg1'] with tag CASE1 - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.29 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.30 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 2: Bridging and Routing sanity test with 4x4 dual-homed leaf-spine topologyand 1 nodes. - FAIL

* 2.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.4 Creating ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.5 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.6 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.7 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.8 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.9 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.10 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.11 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.12 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.13 Set ONOS configurations - No Result ![(warning)](../../../../../../assets/warning.svg)
* 2.14 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.15 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

+ Skipping the rest of this case. 'mininetArgs'

### Case 3: Bridging and Routing sanity test with single ToRand 1 nodes. - FAIL

* 3.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.4 Creating ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.5 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.6 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.7 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.8 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.9 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.10 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.11 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.12 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.13 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.14 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.15 Check whether the flow count is >= 15 - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.16 Check whether all flow status are ADDED - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.17 Verify full connectivity for [u'h1', u'h2'] with tag CASE3 - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.18 Verify full connectivity for [u'olt10', u'vsg10'] with tag CASE3 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 3.19 Verify full connectivity for [u'olt5', u'vsg5'] with tag CASE3 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 3.20 Verify full connectivity for [u'olt1', u'vsg1'] with tag CASE3 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 3.21 Pushing new configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 3.22 Pushing new configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 3.23 Check whether the flow count is >= 18 - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.24 Check whether all flow status are ADDED - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.25 Verify full connectivity for [u'h1', u'h2', 'in1', 'out1'] with tag CASE3 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 3.26 Verify full connectivity for [u'olt10', u'vsg10'] with tag CASE3 - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.27 Verify full connectivity for [u'olt5', u'vsg5'] with tag CASE3 - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.28 Verify full connectivity for ['olt1', 'vsg1'] with tag CASE3 - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.29 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 3.30 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 4: Bridging and Routing sanity test with 2x2 leaf-spine topologyand 3 nodes. Also, killing the first Onos and removing the host cfg. - FAIL

* 4.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.4 Creating ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.5 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.6 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.7 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.8 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.9 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.10 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.11 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.12 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.13 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.14 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.15 Check whether the flow count is >= 116 - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.16 Check whether all flow status are ADDED - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.17 Verify full connectivity for [u'h1', u'h2', u'h3', u'h4'] with tag CASE4 - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.18 Verify full connectivity for [u'olt10', u'vsg10'] with tag CASE4 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 4.19 Verify full connectivity for [u'olt5', u'vsg5'] with tag CASE4 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 4.20 Pushing new configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 4.21 Pushing new configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 4.22 Check whether the flow count is >= 140 - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.23 Check whether all flow status are ADDED - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.24 Verify full connectivity for [u'h1', u'h2', u'h3', u'h4', 'in1', 'out1'] with tag CASE4 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 4.25 Verify full connectivity for [u'olt10', u'vsg10'] with tag CASE4 - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.26 Verify full connectivity for [u'olt5', u'vsg5'] with tag CASE4 - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.27 Verify full connectivity for ['olt1', 'vsg1'] with tag CASE4 - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.28 Killing ONOS instances with index(es): [0] - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.29 Check number of topology elements - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.30 Removing host configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 4.31 Removing configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 4.32 Removing vlan configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 4.33 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 4.34 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

+ Skipping the rest of this case. deleteXconnect() got an unexpected keyword argument 'vlanId'

### Case 5: Bridging and Routing sanity test with 4x4 dual-homed leaf-spine topologyand 3 nodes. Also, killing the first Onos and removing the host cfg. - FAIL

* 5.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.4 Creating ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.5 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.6 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.7 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.8 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.9 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.10 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.11 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.12 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.13 Set ONOS configurations - No Result ![(warning)](../../../../../../assets/warning.svg)
* 5.14 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.15 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

+ Skipping the rest of this case. 'mininetArgs'

### Case 6: Bridging and Routing sanity test with single ToRand 3 nodes. Also, killing the first Onos and removing the host cfg. - FAIL

* 6.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.4 Creating ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.5 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.6 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.7 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.8 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.9 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.10 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.11 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.12 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.13 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.14 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.15 Check whether the flow count is >= 15 - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.16 Check whether all flow status are ADDED - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.17 Verify full connectivity for [u'h1', u'h2'] with tag CASE6 - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.18 Verify full connectivity for [u'olt10', u'vsg10'] with tag CASE6 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 6.19 Verify full connectivity for [u'olt5', u'vsg5'] with tag CASE6 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 6.20 Verify full connectivity for [u'olt1', u'vsg1'] with tag CASE6 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 6.21 Pushing new configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 6.22 Pushing new configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 6.23 Check whether the flow count is >= 20 - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.24 Check whether all flow status are ADDED - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.25 Verify full connectivity for [u'h1', u'h2', 'in1', 'out1'] with tag CASE6 - FAIL ![(error)](../../../../../../assets/error.svg)

+ IP connectivity failed

* 6.26 Verify full connectivity for [u'olt10', u'vsg10'] with tag CASE6 - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.27 Verify full connectivity for [u'olt5', u'vsg5'] with tag CASE6 - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.28 Verify full connectivity for ['olt1', 'vsg1'] with tag CASE6 - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.29 Killing ONOS instances with index(es): [0] - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.30 Check number of topology elements - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.31 Removing host configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 6.32 Removing configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 6.33 Removing vlan configuration - No Result ![(warning)](../../../../../../assets/warning.svg)
* 6.34 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.35 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

+ Skipping the rest of this case. deleteXconnect() got an unexpected keyword argument 'vlanId'
