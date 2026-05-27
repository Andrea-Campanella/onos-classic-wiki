# Master-FUNCoptical

FUNCoptical at 29 Sep 2021 22:05:02![FUNCoptical](https://jenkins.onosproject.org/view/QA/job/postjob-VM/lastSuccessfulBuild/artifact/FUNCoptical_master_20-builds_graph.jpg)
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

### Case 2: Starting up 1 node(s) ONOS cluster - PASS

Set up ONOS with 1 node(s) ONOS cluster

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

### Case 10: Mininet with Linc-OE startup - PASS

Start opticalTest.py topology included with ONOS

* 10.1 Push TopoDDriver.json to ONOS through onos-netcfg - No Result ![(warning)](../../../../../assets/warning.svg)
* 10.2 Starting mininet and LINC-OE - PASS ![(tick)](../../../../../assets/check.svg)

### Case 22: Discover Hosts with arping - PASS

Send arpings between all the hosts to discover and verify them

* 22.1 Send arping between all hosts - PASS ![(tick)](../../../../../assets/check.svg)

### Case 23: Compare ONOS Topology view to Mininet topology - FAIL

Compare topology elements between Mininet and ONOS

* 23.1 Comparing Mininet topology to ONOS topology - FAIL ![(error)](../../../../../assets/error.svg)

+ ONOS incorrectly discovered the topology

### Case 31: Install point intents between 2 packet layer device and ping the hosts - FAIL

This testcase adds bidirectional point intents between 2 packet layer( mininet ) devices and ping mininet hosts

* 31.1 Adding point intents - FAIL ![(error)](../../../../../assets/error.svg)

+ Failed to ping between h1 and h2

* 31.2 Remove Point to Point intents - FAIL ![(error)](../../../../../assets/error.svg)

+ Failed to remove host intents

### Case 32: Test add host intents between optical layer host - FAIL

Test host intents between 2 optical layer host

* 32.1 Creating list of hosts - No Result ![(warning)](../../../../../assets/warning.svg)
* 32.2 Adding host intents to h1 and h2 - FAIL ![(error)](../../../../../assets/error.svg)

+ Some of the intents are not in INSTALLED state

* 32.3 Removing host intents - FAIL ![(error)](../../../../../assets/error.svg)

+ Failed to remove host intents

### Case 14: Stop Mininet - PASS

Stopping the current mininet to start up fresh

* 14.1 Stopping Mininet - PASS ![(tick)](../../../../../assets/check.svg)

### Case 19: Copy karaf logs - PASS

Copying the karaf logs to preserve them throughreinstalling ONOS

* 19.1 Copying karaf logs - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2: Starting up 3 node(s) ONOS cluster - PASS

Set up ONOS with 3 node(s) ONOS cluster

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

### Case 10: Mininet with Linc-OE startup - PASS

Start opticalTest.py topology included with ONOS

* 10.1 Push TopoDDriver.json to ONOS through onos-netcfg - No Result ![(warning)](../../../../../assets/warning.svg)
* 10.2 Starting mininet and LINC-OE - PASS ![(tick)](../../../../../assets/check.svg)

### Case 16: Balance mastership of switches - PASS

* 16.1 Balancing mastership of switches - PASS ![(tick)](../../../../../assets/check.svg)

### Case 22: Discover Hosts with arping - PASS

Send arpings between all the hosts to discover and verify them

* 22.1 Send arping between all hosts - PASS ![(tick)](../../../../../assets/check.svg)

### Case 23: Compare ONOS Topology view to Mininet topology - FAIL

Compare topology elements between Mininet and ONOS

* 23.1 Comparing Mininet topology to ONOS topology - FAIL ![(error)](../../../../../assets/error.svg)

+ ONOS incorrectly discovered the topology

### Case 31: Install point intents between 2 packet layer device and ping the hosts - FAIL

This testcase adds bidirectional point intents between 2 packet layer( mininet ) devices and ping mininet hosts

* 31.1 Adding point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 31.2 Ping h1 and h2 - PASS ![(tick)](../../../../../assets/check.svg)
* 31.3 Remove Point to Point intents - FAIL ![(error)](../../../../../assets/error.svg)

+ Failed to remove host intents

### Case 32: Test add host intents between optical layer host - FAIL

Test host intents between 2 optical layer host

* 32.1 Creating list of hosts - No Result ![(warning)](../../../../../assets/warning.svg)
* 32.2 Adding host intents to h1 and h2 - PASS ![(tick)](../../../../../assets/check.svg)
* 32.3 Pinging h1 and h2 - FAIL ![(error)](../../../../../assets/error.svg)

+ Pinged failed between h1 and h2

* 32.4 Removing host intents - FAIL ![(error)](../../../../../assets/error.svg)

+ Failed to remove host intents

### Case 14: Stop Mininet - PASS

Stopping the current mininet to start up fresh

* 14.1 Stopping Mininet - PASS ![(tick)](../../../../../assets/check.svg)

### Case 19: Copy karaf logs - PASS

Copying the karaf logs to preserve them throughreinstalling ONOS

* 19.1 Copying karaf logs - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2: Starting up 1 node(s) ONOS cluster - PASS

Set up ONOS with 1 node(s) ONOS cluster

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

### Case 10: Mininet with Linc-OE startup - PASS

Start opticalTest.py topology included with ONOS

* 10.1 Push TopoDDriver.json to ONOS through onos-netcfg - No Result ![(warning)](../../../../../assets/warning.svg)
* 10.2 Starting mininet and LINC-OE - PASS ![(tick)](../../../../../assets/check.svg)

### Case 17: Enable intent compilation using Flow Objectives - PASS

* 17.1 Enabling Flow Objectives - PASS ![(tick)](../../../../../assets/check.svg)

### Case 22: Discover Hosts with arping - PASS

Send arpings between all the hosts to discover and verify them

* 22.1 Send arping between all hosts - PASS ![(tick)](../../../../../assets/check.svg)

### Case 23: Compare ONOS Topology view to Mininet topology - FAIL

Compare topology elements between Mininet and ONOS

* 23.1 Comparing Mininet topology to ONOS topology - FAIL ![(error)](../../../../../assets/error.svg)

+ ONOS incorrectly discovered the topology

### Case 31: Install point intents between 2 packet layer device and ping the hosts - FAIL

This testcase adds bidirectional point intents between 2 packet layer( mininet ) devices and ping mininet hosts

* 31.1 Adding point intents - FAIL ![(error)](../../../../../assets/error.svg)

+ Failed to ping between h1 and h2

* 31.2 Remove Point to Point intents - FAIL ![(error)](../../../../../assets/error.svg)

+ Failed to remove host intents

### Case 32: Test add host intents between optical layer host - FAIL

Test host intents between 2 optical layer host

* 32.1 Creating list of hosts - No Result ![(warning)](../../../../../assets/warning.svg)
* 32.2 Adding host intents to h1 and h2 - FAIL ![(error)](../../../../../assets/error.svg)

+ Some of the intents are not in INSTALLED state

* 32.3 Removing host intents - FAIL ![(error)](../../../../../assets/error.svg)

+ Failed to remove host intents

### Case 14: Stop Mininet - PASS

Stopping the current mininet to start up fresh

* 14.1 Stopping Mininet - PASS ![(tick)](../../../../../assets/check.svg)

### Case 19: Copy karaf logs - PASS

Copying the karaf logs to preserve them throughreinstalling ONOS

* 19.1 Copying karaf logs - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2: Starting up 3 node(s) ONOS cluster - PASS

Set up ONOS with 3 node(s) ONOS cluster

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

### Case 10: Mininet with Linc-OE startup - PASS

Start opticalTest.py topology included with ONOS

* 10.1 Push TopoDDriver.json to ONOS through onos-netcfg - No Result ![(warning)](../../../../../assets/warning.svg)
* 10.2 Starting mininet and LINC-OE - PASS ![(tick)](../../../../../assets/check.svg)

### Case 16: Balance mastership of switches - PASS

* 16.1 Balancing mastership of switches - PASS ![(tick)](../../../../../assets/check.svg)

### Case 17: Enable intent compilation using Flow Objectives - PASS

* 17.1 Enabling Flow Objectives - PASS ![(tick)](../../../../../assets/check.svg)

### Case 22: Discover Hosts with arping - PASS

Send arpings between all the hosts to discover and verify them

* 22.1 Send arping between all hosts - PASS ![(tick)](../../../../../assets/check.svg)

### Case 23: Compare ONOS Topology view to Mininet topology - FAIL

Compare topology elements between Mininet and ONOS

* 23.1 Comparing Mininet topology to ONOS topology - FAIL ![(error)](../../../../../assets/error.svg)

+ ONOS incorrectly discovered the topology

### Case 31: Install point intents between 2 packet layer device and ping the hosts - FAIL

This testcase adds bidirectional point intents between 2 packet layer( mininet ) devices and ping mininet hosts

* 31.1 Adding point intents - FAIL ![(error)](../../../../../assets/error.svg)

+ Failed to ping between h1 and h2

* 31.2 Remove Point to Point intents - FAIL ![(error)](../../../../../assets/error.svg)

+ Failed to remove host intents

### Case 32: Test add host intents between optical layer host - FAIL

Test host intents between 2 optical layer host

* 32.1 Creating list of hosts - No Result ![(warning)](../../../../../assets/warning.svg)
* 32.2 Adding host intents to h1 and h2 - FAIL ![(error)](../../../../../assets/error.svg)

+ Some of the intents are not in INSTALLED state

* 32.3 Removing host intents - FAIL ![(error)](../../../../../assets/error.svg)

+ Failed to remove host intents

### Case 14: Stop Mininet - PASS

Stopping the current mininet to start up fresh

* 14.1 Stopping Mininet - PASS ![(tick)](../../../../../assets/check.svg)

### Case 19: Copy karaf logs - PASS

Copying the karaf logs to preserve them throughreinstalling ONOS

* 19.1 Copying karaf logs - PASS ![(tick)](../../../../../assets/check.svg)
