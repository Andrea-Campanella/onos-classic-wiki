# onos-1.2-FUNCintent

FUNCintent at 01 Sep 2015 17:10:33
> commit 1fb0578eae4076b206766c59bdf772e4d44a6c1b (HEAD, origin/onos-1.2, onos-1.2)  
> Author: Brian O'Connor [bocon@onlab.us]  
> AuthorDate: Tue Sep 1 15:30:52 2015 -0700  
> Commit: Brian O'Connor [bocon@onlab.us]  
> CommitDate: Tue Sep 1 15:30:52 2015 -0700  
>   
> Starting snapshot 1.2.3-SNAPSHOT

### Case 1: Constructing test variables and building ONOS package - PASS

This test case is mainly for loading from params file, and pull and build the latest ONOS package

* 1.1 Constructing test variables - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2: Starting up 1 node(s) ONOS cluster - PASS

Set up ONOS with 1 node(s) ONOS cluster

* 2.1 Apply cell to environment - PASS ![(tick)](../../../../../assets/check.svg)
* 2.2 Creating ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.4 Installing ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.5 Starting ONOS service - PASS ![(tick)](../../../../../assets/check.svg)
* 2.6 Start ONOS cli - PASS ![(tick)](../../../../../assets/check.svg)

### Case 10: Start Mininet topology with OF 1.0 switches - PASS

Start mininet topology with OF 1.0 switches to test intents, exits out if topology did not start correctly

* 10.1 Starting Mininet topology with OF 1.0 switches - PASS ![(tick)](../../../../../assets/check.svg)

### Case 12: Assign switches to controllers - PASS

Assign OF 1.0 switches to ONOS nodes

* 12.1 Assigning switches to controllers - PASS ![(tick)](../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - PASS

Compare topology elements between Mininet and ONOS

* 8.1 Conmparing MN topology to ONOS topology - PASS ![(tick)](../../../../../assets/check.svg)

### Case 13: Discover all hosts - PASS

* 13.1 Discover all hosts using pingall - PASS ![(tick)](../../../../../assets/check.svg)

### Case 1000: Host Intents Test - 1 NODE(S) - OF 1.0 - PASS

This test case tests Host intents using 1 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.0 OVS running in Mininet

* 1000.1 IPV4: Add host intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.2 DUALSTACK1: Add host intents between h3 and h11 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.3 DUALSTACK2: Add host intents between h1 and h11 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.4 1HOP: Add host intents between h1 and h3 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.5 VLAN1: Add vlan host intents between h4 and h12 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.6 VLAN2: Add inter vlan host intents between h13 and h20 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2000: Point Intents Test - 1 NODE(S) - OF 1.0 - PASS

This test case will test point to point intents using 1 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.0 OVS running in Mininet

* 2000.1 NOOPTION: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.2 IPV4: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.3 IPV4\_2: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.4 SDNIP-ICMP: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.5 SDNIP-TCP: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.6 DUALSTACK1: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.7 VLAN: Add point intents between h5 and h21 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.8 1HOP: Add point intents between h1 and h3 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 3000: Single to Multi Point Intents Test - 1 NODE(S) - OF 1.0 - PASS

This test case will test single point to multi point intents using 1 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.0 OVS running in Mininet

* 3000.1 NOOPTION: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 3000.2 IPV4: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 3000.3 IPV4\_2: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 3000.4 VLAN: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)

### Case 4000: Multi To Single Point Intents Test - 1 NODE(S) - OF 1.0 - FAIL

This test case will test single point to multi point intents using 1 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.0 OVS running in Mininet

* 4000.1 NOOPTION: Add multi point to single point intents - FAIL ![(error)](../../../../../assets/error.svg)

+ NOOPTION: Failed to add multi point to single point intents with no match action

* 4000.2 IPV4: Add multi point to single point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4000.3 IPV4\_2: Add multi point to single point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4000.4 VLAN: Add multi point to single point intents - PASS ![(tick)](../../../../../assets/check.svg)

### Case 5000: Test host mobility with host intents - PASS

* 5000.1 Testing host mobility by moving h1 from s5 to s6 - PASS ![(tick)](../../../../../assets/check.svg)
* 5000.2 IPV4: Add host intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 14: Stop Mininet topology - PASS

Stopping the current mininet topology to start up fresh

* 14.1 Stopping Mininet Topology - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2: Starting up 3 node(s) ONOS cluster - PASS

Set up ONOS with 3 node(s) ONOS cluster

* 2.1 Apply cell to environment - PASS ![(tick)](../../../../../assets/check.svg)
* 2.2 Creating ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.4 Installing ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.5 Starting ONOS service - PASS ![(tick)](../../../../../assets/check.svg)
* 2.6 Start ONOS cli - PASS ![(tick)](../../../../../assets/check.svg)

### Case 10: Start Mininet topology with OF 1.0 switches - PASS

Start mininet topology with OF 1.0 switches to test intents, exits out if topology did not start correctly

* 10.1 Starting Mininet topology with OF 1.0 switches - PASS ![(tick)](../../../../../assets/check.svg)

### Case 12: Assign switches to controllers - PASS

Assign OF 1.0 switches to ONOS nodes

* 12.1 Assigning switches to controllers - PASS ![(tick)](../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - PASS

Compare topology elements between Mininet and ONOS

* 8.1 Conmparing MN topology to ONOS topology - PASS ![(tick)](../../../../../assets/check.svg)

### Case 13: Discover all hosts - PASS

* 13.1 Discover all hosts using pingall - PASS ![(tick)](../../../../../assets/check.svg)

### Case 1000: Host Intents Test - 3 NODE(S) - OF 1.0 - PASS

This test case tests Host intents using 3 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.0 OVS running in Mininet

* 1000.1 IPV4: Add host intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.2 DUALSTACK1: Add host intents between h3 and h11 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.3 DUALSTACK2: Add host intents between h1 and h11 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.4 1HOP: Add host intents between h1 and h3 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.5 VLAN1: Add vlan host intents between h4 and h12 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.6 VLAN2: Add inter vlan host intents between h13 and h20 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2000: Point Intents Test - 3 NODE(S) - OF 1.0 - PASS

This test case will test point to point intents using 3 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.0 OVS running in Mininet

* 2000.1 NOOPTION: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.2 IPV4: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.3 IPV4\_2: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.4 SDNIP-ICMP: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.5 SDNIP-TCP: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.6 DUALSTACK1: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.7 VLAN: Add point intents between h5 and h21 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.8 1HOP: Add point intents between h1 and h3 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 3000: Single to Multi Point Intents Test - 3 NODE(S) - OF 1.0 - PASS

This test case will test single point to multi point intents using 3 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.0 OVS running in Mininet

* 3000.1 NOOPTION: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 3000.2 IPV4: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 3000.3 IPV4\_2: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 3000.4 VLAN: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)

### Case 4000: Multi To Single Point Intents Test - 3 NODE(S) - OF 1.0 - FAIL

This test case will test single point to multi point intents using 3 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.0 OVS running in Mininet

* 4000.1 NOOPTION: Add multi point to single point intents - FAIL ![(error)](../../../../../assets/error.svg)

+ NOOPTION: Failed to add multi point to single point intents with no match action

* 4000.2 IPV4: Add multi point to single point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4000.3 IPV4\_2: Add multi point to single point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4000.4 VLAN: Add multi point to single point intents - PASS ![(tick)](../../../../../assets/check.svg)

### Case 5000: Test host mobility with host intents - PASS

* 5000.1 Testing host mobility by moving h1 from s5 to s6 - PASS ![(tick)](../../../../../assets/check.svg)
* 5000.2 IPV4: Add host intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 14: Stop Mininet topology - PASS

Stopping the current mininet topology to start up fresh

* 14.1 Stopping Mininet Topology - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2: Starting up 1 node(s) ONOS cluster - PASS

Set up ONOS with 1 node(s) ONOS cluster

* 2.1 Apply cell to environment - PASS ![(tick)](../../../../../assets/check.svg)
* 2.2 Creating ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.4 Installing ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.5 Starting ONOS service - PASS ![(tick)](../../../../../assets/check.svg)
* 2.6 Start ONOS cli - PASS ![(tick)](../../../../../assets/check.svg)

### Case 11: Start Mininet topology with OF 1.3 switches - PASS

Start mininet topology with OF 1.3 switches to test intents, exits out if topology did not start correctly

* 11.1 Starting Mininet topology with OF 1.3 switches - PASS ![(tick)](../../../../../assets/check.svg)

### Case 12: Assign switches to controllers - PASS

Assign OF 1.3 switches to ONOS nodes

* 12.1 Assigning switches to controllers - PASS ![(tick)](../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - PASS

Compare topology elements between Mininet and ONOS

* 8.1 Conmparing MN topology to ONOS topology - PASS ![(tick)](../../../../../assets/check.svg)

### Case 13: Discover all hosts - PASS

* 13.1 Discover all hosts using pingall - PASS ![(tick)](../../../../../assets/check.svg)

### Case 1000: Host Intents Test - 1 NODE(S) - OF 1.3 - PASS

This test case tests Host intents using 1 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.3 OVS running in Mininet

* 1000.1 IPV4: Add host intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.2 DUALSTACK1: Add host intents between h3 and h11 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.3 DUALSTACK2: Add host intents between h1 and h11 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.4 1HOP: Add host intents between h1 and h3 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.5 VLAN1: Add vlan host intents between h4 and h12 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.6 VLAN2: Add inter vlan host intents between h13 and h20 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2000: Point Intents Test - 1 NODE(S) - OF 1.3 - PASS

This test case will test point to point intents using 1 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.3 OVS running in Mininet

* 2000.1 NOOPTION: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.2 IPV4: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.3 IPV4\_2: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.4 SDNIP-ICMP: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.5 SDNIP-TCP: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.6 DUALSTACK1: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.7 VLAN: Add point intents between h5 and h21 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.8 1HOP: Add point intents between h1 and h3 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 3000: Single to Multi Point Intents Test - 1 NODE(S) - OF 1.3 - PASS

This test case will test single point to multi point intents using 1 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.3 OVS running in Mininet

* 3000.1 NOOPTION: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 3000.2 IPV4: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 3000.3 IPV4\_2: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 3000.4 VLAN: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)

### Case 4000: Multi To Single Point Intents Test - 1 NODE(S) - OF 1.3 - FAIL

This test case will test single point to multi point intents using 1 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.3 OVS running in Mininet

* 4000.1 NOOPTION: Add multi point to single point intents - FAIL ![(error)](../../../../../assets/error.svg)

+ NOOPTION: Failed to add multi point to single point intents with no match action

* 4000.2 IPV4: Add multi point to single point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4000.3 IPV4\_2: Add multi point to single point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4000.4 VLAN: Add multi point to single point intents - PASS ![(tick)](../../../../../assets/check.svg)

### Case 5000: Test host mobility with host intents - PASS

* 5000.1 Testing host mobility by moving h1 from s5 to s6 - PASS ![(tick)](../../../../../assets/check.svg)
* 5000.2 IPV4: Add host intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 14: Stop Mininet topology - PASS

Stopping the current mininet topology to start up fresh

* 14.1 Stopping Mininet Topology - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2: Starting up 3 node(s) ONOS cluster - PASS

Set up ONOS with 3 node(s) ONOS cluster

* 2.1 Apply cell to environment - PASS ![(tick)](../../../../../assets/check.svg)
* 2.2 Creating ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.3 Uninstalling ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.4 Installing ONOS package - PASS ![(tick)](../../../../../assets/check.svg)
* 2.5 Starting ONOS service - PASS ![(tick)](../../../../../assets/check.svg)
* 2.6 Start ONOS cli - PASS ![(tick)](../../../../../assets/check.svg)

### Case 11: Start Mininet topology with OF 1.3 switches - PASS

Start mininet topology with OF 1.3 switches to test intents, exits out if topology did not start correctly

* 11.1 Starting Mininet topology with OF 1.3 switches - PASS ![(tick)](../../../../../assets/check.svg)

### Case 12: Assign switches to controllers - PASS

Assign OF 1.3 switches to ONOS nodes

* 12.1 Assigning switches to controllers - PASS ![(tick)](../../../../../assets/check.svg)

### Case 8: Compare ONOS Topology view to Mininet topology - PASS

Compare topology elements between Mininet and ONOS

* 8.1 Conmparing MN topology to ONOS topology - PASS ![(tick)](../../../../../assets/check.svg)

### Case 13: Discover all hosts - PASS

* 13.1 Discover all hosts using pingall - PASS ![(tick)](../../../../../assets/check.svg)

### Case 1000: Host Intents Test - 3 NODE(S) - OF 1.3 - PASS

This test case tests Host intents using 3 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.3 OVS running in Mininet

* 1000.1 IPV4: Add host intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.2 DUALSTACK1: Add host intents between h3 and h11 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.3 DUALSTACK2: Add host intents between h1 and h11 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.4 1HOP: Add host intents between h1 and h3 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.5 VLAN1: Add vlan host intents between h4 and h12 - PASS ![(tick)](../../../../../assets/check.svg)
* 1000.6 VLAN2: Add inter vlan host intents between h13 and h20 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 2000: Point Intents Test - 3 NODE(S) - OF 1.3 - PASS

This test case will test point to point intents using 3 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.3 OVS running in Mininet

* 2000.1 NOOPTION: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.2 IPV4: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.3 IPV4\_2: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.4 SDNIP-ICMP: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.5 SDNIP-TCP: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.6 DUALSTACK1: Add point intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.7 VLAN: Add point intents between h5 and h21 - PASS ![(tick)](../../../../../assets/check.svg)
* 2000.8 1HOP: Add point intents between h1 and h3 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 3000: Single to Multi Point Intents Test - 3 NODE(S) - OF 1.3 - PASS

This test case will test single point to multi point intents using 3 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.3 OVS running in Mininet

* 3000.1 NOOPTION: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 3000.2 IPV4: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 3000.3 IPV4\_2: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 3000.4 VLAN: Add single point to multi point intents - PASS ![(tick)](../../../../../assets/check.svg)

### Case 4000: Multi To Single Point Intents Test - 3 NODE(S) - OF 1.3 - FAIL

This test case will test single point to multi point intents using 3 node(s) cluster;
Different type of hosts will be tested in each step such as IPV4, Dual stack, VLAN etc;
The test will use OF 1.3 OVS running in Mininet

* 4000.1 NOOPTION: Add multi point to single point intents - FAIL ![(error)](../../../../../assets/error.svg)

+ NOOPTION: Failed to add multi point to single point intents with no match action

* 4000.2 IPV4: Add multi point to single point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4000.3 IPV4\_2: Add multi point to single point intents - PASS ![(tick)](../../../../../assets/check.svg)
* 4000.4 VLAN: Add multi point to single point intents - PASS ![(tick)](../../../../../assets/check.svg)

### Case 5000: Test host mobility with host intents - PASS

* 5000.1 Testing host mobility by moving h1 from s5 to s6 - PASS ![(tick)](../../../../../assets/check.svg)
* 5000.2 IPV4: Add host intents between h1 and h9 - PASS ![(tick)](../../../../../assets/check.svg)

### Case 14: Stop Mininet topology - PASS

Stopping the current mininet topology to start up fresh

* 14.1 Stopping Mininet Topology - PASS ![(tick)](../../../../../assets/check.svg)
