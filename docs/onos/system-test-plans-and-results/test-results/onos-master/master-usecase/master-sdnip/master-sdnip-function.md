# Master-SDNIP Function

USECASE\_SdnipFunction at 21 Sep 2021 22:27:03

### Case 101: Starting up 3 node(s) ONOS cluster - PASS

Set up ONOS with 3 node(s) ONOS cluster

* 101.1 Constructing test variables - No Result ![(warning)](../../../../../../assets/warning.svg)
* 101.2 Copying config files - PASS ![(tick)](../../../../../../assets/check.svg)
* 101.3 Apply cell to environment - PASS ![(tick)](../../../../../../assets/check.svg)
* 101.4 Uninstalling Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 101.5 Uninstalling ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 101.6 Creating ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 101.7 Installing Atomix - PASS ![(tick)](../../../../../../assets/check.svg)
* 101.8 Installing ONOS package - PASS ![(tick)](../../../../../../assets/check.svg)
* 101.9 Set up ONOS secure SSH - PASS ![(tick)](../../../../../../assets/check.svg)
* 101.10 Checking ONOS service - PASS ![(tick)](../../../../../../assets/check.svg)
* 101.11 Starting ONOS CLI sessions - PASS ![(tick)](../../../../../../assets/check.svg)
* 101.12 Checking ONOS nodes - PASS ![(tick)](../../../../../../assets/check.svg)
* 101.13 Checking ONOS applications - PASS ![(tick)](../../../../../../assets/check.svg)
* 101.14 Checking if ONOS CLI is ready for issuing commands - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 100: Setup the Mininet testbed - PASS

* 100.1 Starting Mininet Topology - PASS ![(tick)](../../../../../../assets/check.svg)
* 100.2 Connect switches to controller - PASS ![(tick)](../../../../../../assets/check.svg)
* 100.3 Set up tunnel from Mininet node to onos node - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 200: Activate sdn-ip application - PASS

* 200.1 Activate sdn-ip application - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 102: Loading methods from other Python file - PASS



### Case 1: Ping tests between BGP peers and speakers - PASS

* 1.1 BGP speakers ping peers, expect all tests to succeed - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.2 BGP speakers ping peers, expect all tests to succeed - PASS ![(tick)](../../../../../../assets/check.svg)
* 1.3 BGP speakers ping peers, expect all tests to succeed - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 2: Check point-to-point intents - PASS

* 2.1 Check P2P intents number from ONOS CLI - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 3: Check routes and M2S intents to all BGP peers - FAIL

* 3.1 Check routes installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ Routes are wrong!

* 3.2 Check M2S intents installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ MultiPointToSinglePoint Intent Num is wrong!

* 3.3 Check whether all flow status are ADDED - FAIL ![(error)](../../../../../../assets/error.svg)

+ Flow status is wrong!

### Case 4: Ping test for each route, all hosts behind BGP peers - FAIL

* 4.1 Check ping between each host pair, expect all to succede=True - FAIL ![(error)](../../../../../../assets/error.svg)

+ Ping test results are Not expected

* 4.2 Check ping between each host pair, expect all to succede=True - FAIL ![(error)](../../../../../../assets/error.svg)

+ Ping test results are Not expected

* 4.3 Check ping between each host pair, expect all to succede=True - FAIL ![(error)](../../../../../../assets/error.svg)

+ Ping test results are Not expected

### Case 5: Bring down links and check routes/intents - FAIL

* 5.1 Bring down the link between sw32 and p64514 - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.2 Check routes installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ Route number is wrong!

* 5.3 Check M2S intents installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ M2S intent number is wrong!

* 5.4 Bring down the link between sw8 and p64515 - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.5 Check routes installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ Route number is wrong!

* 5.6 Check M2S intents installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ M2S intent number is wrong!

* 5.7 Bring down the link between sw28 and p64516 - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.8 Check routes installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ Route number is wrong!

* 5.9 Check M2S intents installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ M2S intent number is wrong!

* 5.10 Check whether all flow status are ADDED - FAIL ![(error)](../../../../../../assets/error.svg)

+ Flow status is wrong!

* 5.11 BGP speakers ping peers, expect all tests to fail - PASS ![(tick)](../../../../../../assets/check.svg)
* 5.12 Check ping between each host pair, expect all to succede=False - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 6: Bring up links and check routes/intents - FAIL

* 6.1 Bring up the link between sw32 and p64514 - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.2 Check routes installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ Route number is wrong!

* 6.3 Check M2S intents installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ M2S intent number is wrong!

* 6.4 Bring up the link between sw8 and p64515 - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.5 Check routes installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ Route number is wrong!

* 6.6 Check M2S intents installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ M2S intent number is wrong!

* 6.7 Bring up the link between sw28 and p64516 - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.8 Check routes installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ Route number is wrong!

* 6.9 Check M2S intents installed - FAIL ![(error)](../../../../../../assets/error.svg)

+ M2S intent number is wrong!

* 6.10 Check whether all flow status are ADDED - FAIL ![(error)](../../../../../../assets/error.svg)

+ Flow status is wrong!

* 6.11 BGP speakers ping peers, expect all tests to fail - PASS ![(tick)](../../../../../../assets/check.svg)
* 6.12 Check ping between each host pair, expect all to succede=False - PASS ![(tick)](../../../../../../assets/check.svg)

### Case 7: Stop edge sw32,check P-2-P and M-2-S intents, ping test - FAIL
