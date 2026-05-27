# master-SR Dhcp Relay

SRDhcprelay at 29 Sep 2021 19:32:28![SRDhcprelay](https://jenkins.onosproject.org/view/QA/job/postjob-Fabric4/lastSuccessfulBuild/artifact/SRDhcprelay_master_20-builds_graph.jpg)
> commit 581c8407e613a27aaa573a600828b30a37066fb8 (HEAD -] master, origin/master, origin/HEAD)  
> Author: pierventre [pier@opennetworking.org]  
> AuthorDate: Thu Sep 23 19:03:14 2021 +0200  
> Commit: Pier Luigi Ventre [pier@opennetworking.org]  
> CommitDate: Mon Sep 27 19:27:55 2021 +0000  
>   
> [SDFAB-616] Inconsistent format of port number in DhcpRelay  
> --  
> (cherry picked from commit 61bd673eec2282aff175daff141059870db78c7d)

### Case 1: DHCP v4 tests with 4 clients attached to switch directly and 1 server attached to switch directly, with 3 ONOS instances - PASS

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
* 1.16 Verify host IP address assignment in ONOS - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.17 Verify IP address assignment from hosts - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.18 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.19 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 2: DHCP v4 tests with 4 clients attached to switch directly and 1 server attached to switch indirectly (via gateway), with 3 ONOS instances - PASS

* 2.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.4 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.5 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.6 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.7 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.8 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.9 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.10 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.11 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.12 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.13 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.14 Verify host IP address assignment in ONOS - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.15 Verify IP address assignment from hosts - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.16 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 2.17 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 11: DHCP v6 tests with 4 clients attached to switch directly and 1 server attached to switch directly, with 3 ONOS instances - PASS

* 11.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.4 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.5 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.6 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.7 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.8 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.9 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.10 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.11 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.12 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.13 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.14 Verify host IP address assignment in ONOS - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.15 Verify IP address assignment from hosts - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.16 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 11.17 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 12: DHCP v6 tests with 4 clients attached to switch directly and 1 server attached to switch indirectly (via gateway), with 3 ONOS instances - FAIL

* 12.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.4 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.5 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.6 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.7 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.8 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.9 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.10 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.11 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.12 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.13 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.14 Verify host IP address assignment in ONOS - FAIL ![(error)](../../../../../../assets/error.svg)

+ Verify ONOS host IP failed

* 12.15 Verify IP address assignment from hosts - FAIL ![(error)](../../../../../../assets/error.svg)

+ Verify network host IP failed

* 12.16 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 12.17 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 21: DHCP v4 tests with tagged hosts: 4 clients attached to switch directly and 1 server attached to switch directly, with 3 ONOS instances - PASS

* 21.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.4 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.5 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.6 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.7 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.8 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.9 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.10 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.11 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.12 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.13 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.14 Verify host IP address assignment in ONOS - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.15 Verify IP address assignment from hosts - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.16 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 21.17 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 22: DHCP v4 tests with tagged hosts: 4 clients attached to switch directly and 1 server attached to switch indirectly (via gateway), with 3 ONOS instances - PASS

* 22.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.4 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.5 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.6 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.7 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.8 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.9 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.10 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.11 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.12 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.13 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.14 Verify host IP address assignment in ONOS - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.15 Verify IP address assignment from hosts - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.16 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 22.17 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 31: DHCP v6 tests with tagged hosts: 4 clients attached to switch directly and 1 server attached to switch directly, with 3 ONOS instances - PASS

* 31.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.4 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.5 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.6 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.7 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.8 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.9 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.10 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.11 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.12 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.13 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.14 Verify host IP address assignment in ONOS - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.15 Verify IP address assignment from hosts - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.16 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 31.17 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 41: DHCP v4 tests with dual-homed hosts: 4 clients attached to switch directly and 1 server attached to switch directly, with 3 ONOS instances - PASS

* 41.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.4 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.5 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.6 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.7 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.8 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.9 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.10 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.11 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.12 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.13 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.14 Verify host IP address assignment in ONOS - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.15 Verify IP address assignment from hosts - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.16 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 41.17 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 51: DHCP v6 tests with dual-homed hosts: 4 clients attached to switch directly and 1 server attached to switch directly, with 3 ONOS instances - FAIL

* 51.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.4 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.5 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.6 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.7 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.8 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.9 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.10 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.11 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.12 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.13 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.14 Verify host IP address assignment in ONOS - FAIL ![(error)](../../../../../../assets/error.svg)

+ Verify ONOS host IP failed

* 51.15 Verify IP address assignment from hosts - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.16 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 51.17 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 61: DHCP v4 tests with dual-homed tagged hosts: 4 clients attached to switch directly and 1 server attached to switch directly, with 3 ONOS instances - PASS

* 61.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.4 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.5 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.6 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.7 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.8 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.9 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.10 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.11 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.12 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.13 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.14 Verify host IP address assignment in ONOS - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.15 Verify IP address assignment from hosts - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.16 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 61.17 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 71: DHCP v6 tests with dual-homed tagged hosts: 4 clients attached to switch directly and 1 server attached to switch directly, with 3 ONOS instances - FAIL

* 71.1 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.2 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.4 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.5 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.6 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.7 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.8 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.9 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.10 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.11 Set logging levels - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.12 Set ONOS configurations - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.13 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.14 Verify host IP address assignment in ONOS - FAIL ![(error)](../../../../../../assets/error.svg)

+ Verify ONOS host IP failed

* 71.15 Verify IP address assignment from hosts - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.16 Stopping Mininet - PASS ![(tick)](../../../../../../assets/check.svg)
* 71.17 Copying karaf logs - PASS ![(tick)](../../../../../../assets/check.svg)
