# onos-1.2-HA Single Instance Restart

HATestSingleInstanceRestart at 30 Jun 2015 02:54:46

> commit fdba99862c594dca7672eb09fea8584a3dd99a87 (HEAD, origin/onos-1.2, onos-1.2)  
> Author: alshabib [alshabibi.ali@[gmail.com](http://gmail.com)]  
> AuthorDate: Fri Jun 26 13:20:54 2015 -0700  
> Commit: alshabib [alshabibi.ali@[gmail.com](http://gmail.com)]  
> CommitDate: Fri Jun 26 15:43:59 2015 -0700  
>   
> adding a dockerfile for onos-1.2

### Case 1: Setting up test environment - PASS

Setup the test environment including installing ONOS, starting Mininet and ONOScli sessions.

* 1.1 Applying cell variable to environment - No Result ![(warning)](../../../../../assets/warning.svg)
* 1.2 Starting Mininet - PASS ![(tick)](../../../../../assets/check.svg)
* 1.3 Git checkout and pull master - No Result ![(warning)](../../../../../assets/warning.svg)
* 1.4 Using mvn clean install - PASS ![(tick)](../../../../../assets/check.svg)
* 1.5 Creating ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 1.6 Installing ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 1.7 Checking if ONOS is up yet - PASS ![(tick)](../../../../../assets/check.svg)
* 1.8 App Ids check - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2: Assigning devices to controllers - PASS

Assign switches to ONOS using 'ovs-vsctl' and check that an ONOS node becomes the master of the device.

* 2.1 Assign switches to controllers - PASS ![(tick)](../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - PASS

Compare topology objects between Mininet and ONOS

* 8.1 Create TestONTopology object - PASS ![(tick)](../../../../../assets/check.svg)
* 8.2 Comparing ONOS topology to MN - No Result ![(warning)](../../../../../assets/warning.svg)
* 8.3 Collecting topology information from ONOS - PASS ![(tick)](../../../../../assets/check.svg)

### Case 3: Adding host Intents - PASS

Discover hosts by using pingall then assign predetermined host-to-host intents. After installation, check that the intent is distributed to all nodes and the state is INSTALLED

* 3.1 Install reactive forwarding app - PASS ![(tick)](../../../../../assets/check.svg)
* 3.2 Check app ids - PASS ![(tick)](../../../../../assets/check.svg)
* 3.3 Discovering Hosts( Via pingall for now ) - PASS ![(tick)](../../../../../assets/check.svg)
* 3.4 Uninstall reactive forwarding app - PASS ![(tick)](../../../../../assets/check.svg)
* 3.5 Check app ids - PASS ![(tick)](../../../../../assets/check.svg)
* 3.6 Add host intents via cli - PASS ![(tick)](../../../../../assets/check.svg)
* 3.7 Intent Anti-Entropy dispersion - PASS ![(tick)](../../../../../assets/check.svg)

### Case 4: Verify connectivity by sendind traffic across Intents - PASS

Ping across added host intents to check functionality and check the state of the intent

* 4.1 Ping across added host intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4.2 Check Intent state - PASS ![(tick)](../../../../../assets/check.svg)
* 4.3 Check leadership of topics - PASS ![(tick)](../../../../../assets/check.svg)
* 4.4 Wait a minute then ping again - PASS ![(tick)](../../../../../assets/check.svg)

### Case 5: Setting up and gathering data for current state - PASS

* 5.1 Check that each switch has a master - PASS ![(tick)](../../../../../assets/check.svg)
* 5.2 Get the Mastership of each switch - No Result ![(warning)](../../../../../assets/warning.svg)
* 5.3 Get the intents from each controller - No Result ![(warning)](../../../../../assets/warning.svg)
* 5.4 Get the flows from each controller - No Result ![(warning)](../../../../../assets/warning.svg)
* 5.5 Get the OF Table entries - No Result ![(warning)](../../../../../assets/warning.svg)
* 5.6 Create TestONTopology object - No Result ![(warning)](../../../../../assets/warning.svg)
* 5.7 Collecting topology information from ONOS - No Result ![(warning)](../../../../../assets/warning.svg)
* 5.8 Each host has an IP address - PASS ![(tick)](../../../../../assets/check.svg)
* 5.9 There is only one dataplane cluster - PASS ![(tick)](../../../../../assets/check.svg)
* 5.10 Comparing ONOS topology to MN - PASS ![(tick)](../../../../../assets/check.svg)

### Case 14: Start Leadership Election app - PASS

* 14.1 Install leadership election app - PASS ![(tick)](../../../../../assets/check.svg)
* 14.2 Run for election on each node - PASS ![(tick)](../../../../../assets/check.svg)

### Case 15: Check that Leadership Election is still functional - PASS

* 15.1 Find current leader and withdraw - PASS ![(tick)](../../../../../assets/check.svg)
* 15.2 Make sure new leader is elected - PASS ![(tick)](../../../../../assets/check.svg)
* 15.3 Run for election on old leader( just so everyone is in the hat ) - PASS ![(tick)](../../../../../assets/check.svg)
* 15.4 Node became leader when it ran for election - PASS ![(tick)](../../../../../assets/check.svg)

### Case 16: Install Primitives app - PASS

* 16.1 Install Primitives app - PASS ![(tick)](../../../../../assets/check.svg)

### Case 17: Check for basic functionality with distributed primitives - PASS

Test the methods of the distributed primitives (counters and sets) throught the cli

* 17.1 Increment and get a default counter on each node - PASS ![(tick)](../../../../../assets/check.svg)
* 17.2 Increment and get an in memory counter on each node - PASS ![(tick)](../../../../../assets/check.svg)
* 17.3 Check counters are consistant across nodes - PASS ![(tick)](../../../../../assets/check.svg)
* 17.4 Counters we added have the correct values - PASS ![(tick)](../../../../../assets/check.svg)
* 17.5 Distributed Set get - PASS ![(tick)](../../../../../assets/check.svg)
* 17.6 Distributed Set size - PASS ![(tick)](../../../../../assets/check.svg)
* 17.7 Distributed Set add() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.8 Distributed Set addAll() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.9 Distributed Set contains() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.10 Distributed Set containsAll() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.11 Distributed Set remove() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.12 Distributed Set removeAll() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.13 Distributed Set addAll() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.14 Distributed Set clear() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.15 Distributed Set addAll() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.16 Distributed Set retain() - PASS ![(tick)](../../../../../assets/check.svg)

### Case 6: Restart ONOS node - PASS

Killing ONOS process and restart cli sessions once onos is up.

* 6.1 Killing ONOS processes - PASS ![(tick)](../../../../../assets/check.svg)
* 6.2 Checking if ONOS is up yet - PASS ![(tick)](../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - PASS

Compare topology objects between Mininet and ONOS

* 8.1 Create TestONTopology object - PASS ![(tick)](../../../../../assets/check.svg)
* 8.2 Comparing ONOS topology to MN - No Result ![(warning)](../../../../../assets/warning.svg)
* 8.3 Collecting topology information from ONOS - PASS ![(tick)](../../../../../assets/check.svg)

### Case 3: Adding host Intents - PASS

Discover hosts by using pingall then assign predetermined host-to-host intents. After installation, check that the intent is distributed to all nodes and the state is INSTALLED

* 3.1 Install reactive forwarding app - PASS ![(tick)](../../../../../assets/check.svg)
* 3.2 Check app ids - PASS ![(tick)](../../../../../assets/check.svg)
* 3.3 Discovering Hosts( Via pingall for now ) - PASS ![(tick)](../../../../../assets/check.svg)
* 3.4 Uninstall reactive forwarding app - PASS ![(tick)](../../../../../assets/check.svg)
* 3.5 Check app ids - PASS ![(tick)](../../../../../assets/check.svg)
* 3.6 Add host intents via cli - PASS ![(tick)](../../../../../assets/check.svg)
* 3.7 Intent Anti-Entropy dispersion - PASS ![(tick)](../../../../../assets/check.svg)

### Case 7: Running ONOS Constant State Tests - PASS

* 7.1 Check that each switch has a master - PASS ![(tick)](../../../../../assets/check.svg)
* 7.2 Check if switch roles are consistent across all nodes - PASS ![(tick)](../../../../../assets/check.svg)
* 7.3 Compare switch roles from before failure - PASS ![(tick)](../../../../../assets/check.svg)
* 7.4 Get the intents and compare across all nodes - PASS ![(tick)](../../../../../assets/check.svg)
* 7.5 Get the OF Table entries and compare to before component failure - PASS ![(tick)](../../../../../assets/check.svg)
* 7.6 Leadership Election is still functional - PASS ![(tick)](../../../../../assets/check.svg)

### Case 4: Verify connectivity by sendind traffic across Intents - PASS

Ping across added host intents to check functionality and check the state of the intent

* 4.1 Ping across added host intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4.2 Check Intent state - PASS ![(tick)](../../../../../assets/check.svg)
* 4.3 Check leadership of topics - PASS ![(tick)](../../../../../assets/check.svg)
* 4.4 Wait a minute then ping again - PASS ![(tick)](../../../../../assets/check.svg)

### Case 15: Check that Leadership Election is still functional - PASS

* 15.1 Find current leader and withdraw - PASS ![(tick)](../../../../../assets/check.svg)
* 15.2 Make sure new leader is elected - PASS ![(tick)](../../../../../assets/check.svg)
* 15.3 Run for election on old leader( just so everyone is in the hat ) - PASS ![(tick)](../../../../../assets/check.svg)
* 15.4 Node became leader when it ran for election - PASS ![(tick)](../../../../../assets/check.svg)

### Case 17: Check for basic functionality with distributed primitives - PASS

Test the methods of the distributed primitives (counters and sets) throught the cli

* 17.1 Increment and get a default counter on each node - PASS ![(tick)](../../../../../assets/check.svg)
* 17.2 Increment and get an in memory counter on each node - PASS ![(tick)](../../../../../assets/check.svg)
* 17.3 Check counters are consistant across nodes - PASS ![(tick)](../../../../../assets/check.svg)
* 17.4 Counters we added have the correct values - PASS ![(tick)](../../../../../assets/check.svg)
* 17.5 Distributed Set get - PASS ![(tick)](../../../../../assets/check.svg)
* 17.6 Distributed Set size - PASS ![(tick)](../../../../../assets/check.svg)
* 17.7 Distributed Set add() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.8 Distributed Set addAll() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.9 Distributed Set contains() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.10 Distributed Set containsAll() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.11 Distributed Set remove() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.12 Distributed Set removeAll() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.13 Distributed Set addAll() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.14 Distributed Set clear() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.15 Distributed Set addAll() - PASS ![(tick)](../../../../../assets/check.svg)
* 17.16 Distributed Set retain() - PASS ![(tick)](../../../../../assets/check.svg)

### Case 9: Turn off a link to ensure that Link Discovery is working properly - PASS

* 9.1 Kill Link between s3 and s28 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - PASS

Compare topology objects between Mininet and ONOS

* 8.1 Create TestONTopology object - PASS ![(tick)](../../../../../assets/check.svg)
* 8.2 Comparing ONOS topology to MN - No Result ![(warning)](../../../../../assets/warning.svg)
* 8.3 Collecting topology information from ONOS - PASS ![(tick)](../../../../../assets/check.svg)

### Case 4: Verify connectivity by sendind traffic across Intents - PASS

Ping across added host intents to check functionality and check the state of the intent

* 4.1 Ping across added host intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4.2 Check Intent state - PASS ![(tick)](../../../../../assets/check.svg)
* 4.3 Check leadership of topics - PASS ![(tick)](../../../../../assets/check.svg)
* 4.4 Wait a minute then ping again - PASS ![(tick)](../../../../../assets/check.svg)

### Case 10: Restore a link to ensure that Link Discovery is working properly - PASS

* 10.1 Bring link between s3 and s28 back up - PASS ![(tick)](../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - PASS

Compare topology objects between Mininet and ONOS

* 8.1 Create TestONTopology object - PASS ![(tick)](../../../../../assets/check.svg)
* 8.2 Comparing ONOS topology to MN - No Result ![(warning)](../../../../../assets/warning.svg)
* 8.3 Collecting topology information from ONOS - PASS ![(tick)](../../../../../assets/check.svg)

### Case 4: Verify connectivity by sendind traffic across Intents - PASS

Ping across added host intents to check functionality and check the state of the intent

* 4.1 Ping across added host intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4.2 Check Intent state - PASS ![(tick)](../../../../../assets/check.svg)
* 4.3 Check leadership of topics - PASS ![(tick)](../../../../../assets/check.svg)
* 4.4 Wait a minute then ping again - PASS ![(tick)](../../../../../assets/check.svg)

### Case 11: Killing a switch to ensure it is discovered correctly - PASS

* 11.1 Kill s5 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - PASS

Compare topology objects between Mininet and ONOS

* 8.1 Create TestONTopology object - PASS ![(tick)](../../../../../assets/check.svg)
* 8.2 Comparing ONOS topology to MN - No Result ![(warning)](../../../../../assets/warning.svg)
* 8.3 Collecting topology information from ONOS - PASS ![(tick)](../../../../../assets/check.svg)

### Case 4: Verify connectivity by sendind traffic across Intents - PASS

Ping across added host intents to check functionality and check the state of the intent

* 4.1 Ping across added host intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4.2 Check Intent state - PASS ![(tick)](../../../../../assets/check.svg)
* 4.3 Check leadership of topics - PASS ![(tick)](../../../../../assets/check.svg)
* 4.4 Wait a minute then ping again - PASS ![(tick)](../../../../../assets/check.svg)

### Case 12: Adding a switch to ensure it is discovered correctly - PASS

* 12.1 Add back s5 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - PASS

Compare topology objects between Mininet and ONOS

* 8.1 Create TestONTopology object - PASS ![(tick)](../../../../../assets/check.svg)
* 8.2 Comparing ONOS topology to MN - No Result ![(warning)](../../../../../assets/warning.svg)
* 8.3 Collecting topology information from ONOS - PASS ![(tick)](../../../../../assets/check.svg)

### Case 4: Verify connectivity by sendind traffic across Intents - PASS

Ping across added host intents to check functionality and check the state of the intent

* 4.1 Ping across added host intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4.2 Check Intent state - PASS ![(tick)](../../../../../assets/check.svg)
* 4.3 Check leadership of topics - PASS ![(tick)](../../../../../assets/check.svg)
* 4.4 Wait a minute then ping again - PASS ![(tick)](../../../../../assets/check.svg)

### Case 13: Test Cleanup - PASS

* 13.1 Killing tcpdumps - No Result ![(warning)](../../../../../assets/warning.svg)
* 13.2 Copying MN pcap and ONOS log files to test station - No Result ![(warning)](../../../../../assets/warning.svg)
* 13.3 Stopping Mininet - PASS ![(tick)](../../../../../assets/check.svg)
* 13.4 Checking ONOS Logs for errors - No Result ![(warning)](../../../../../assets/warning.svg)
* 13.5 Packing and rotating pcap archives - No Result ![(warning)](../../../../../assets/warning.svg)
