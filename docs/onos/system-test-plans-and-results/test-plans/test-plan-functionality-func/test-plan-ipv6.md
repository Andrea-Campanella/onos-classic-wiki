# Test Plan - IPv6

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **#** | **Test Case** | **Pass Criteria** | **Priority** | **SingleNode/ MultiNode** |
| 1 | Starting a single instance ONOS,   ONOS install,   Start onos-service and   Obtain all the component   (ONOS bench,ONOS cli, ONOS instance, Mininet) handle | Check Logs and verify ONOS is started with all Services and Components | 2 | Single Node |
| 2 | Starting Multiple instance ONOS,   Install Multiple ONOS,   Start onos-service and   Obtain all the component | Check Logs and verify ONOS is started with all Services and Components | 2 | Multi Node |
| 3 | Verify assign master-ship to one ONOS instance controller | Check master-ship using CLI "sh ovs-vsctl get-controller { switch name }" | 3 | Single node   Multi Node |
| 4 | Verify IPv6 Host Discovery before adding intents | Check using "hosts" cli command | 2 | Single node   Multi Node |
| 5 | Verify IPv6 Neighbor Advertisement | Check neighbor is Advertise on neighbor | 1 | Single node   Multi Node |
| 6 | Verify IPv6 Neighbor Solicitation | Check neighbor is Advertise on neighbor | 1 | Single node   Multi Node |
| 7 | Verify IPv6 Forwarding/Reactive Forwarding | Check IPv6 traffic should be able to flow | 1 | Single node   Multi Node |
| 8 | Verify ICMP6 Ping | Check ICMPv6 ping should be successful | 1 | Single node   Multi Node |
| 9 | Verify IPv6 Host Intent Addition | Check Ping between the hosts connected to the devices between whom point intents were added | 1 | Single node   Multi Node |
| 10 | Verify Point Intent Addition matching on port numbers | Check Ping between the hosts connected to the devices between whom point intents were added | 1 | Single node   Multi Node |
| 11 | Verify Installing 300 host intents and verify ping all | Check all 300 point intents are successfully installed and runs ping all across all host to verify connectivity | 2 | Single node   Multi Node |
| 12 | Verify Compare ONOS topo & mininet topo | Check if the topology across all nodes is consistent with mininet's view of topology | 1 | Single node   Multi Node |
| 13 | Verify Link discovery and Bring a mininet link down and then up | Check Link discovery is done | 2 | Single node   Multi Node |
| 14 | Randomly bring some core links down and verify ping all | Check even during link down state connectivity still exist via reroutes. | 2 | Single node   Multi Node |
| 15 | Bring core links Up that were down and verify ping all | Check the links are up that were down previously and checks the connectivity across host using ping all. | 2 | Single node   Multi Node |
| 16 | Verify Intents with VLAN-id | Check from "hosts" command if ONOS discover correct VLAN tag  Ping between the hosts connected to the devices between whom intents were added should pass | 3 | Single node   Multi Node |
| 17 | Rewrite mac address action in multi point to single point intent | Check using "intents" cli command where the intent's state should be INSTALLED | 2 | Single node   Multi Node |
| 18 | Verify Removing previously and adding new intents types | Check using "intents" cli command where the intents should be removed  Ping between the hosts connected to the devices between whom point intents were removed should fai | 3 | Single node   Multi Node |
| 19 | Verify Modify IPv6 Source Address | Configure and connect the Primary-controller. Create a flow with action OFPAT\_SET\_NW\_SRC and output to an egress port. Send matching packet to ingress port. Verify packet gets output to egress port with correct IPv6 source address as specified in the flow. | 2 | Single node   Multi Node |
| 20 | Verify Modify IPv6 destination address | Configure and connect the Primary-controller. Create a flow with action OFPAT\_SET\_NW\_DST and output to an egress port. Send matching packet to ingress port. Verify packet gets output to egress port with correct IPv6 destination address as specified in the flow. | 3 | Single node   Multi Node |
| 21 | Verify Implement test script for one hop point intent | Form a switch with 2 host Add a one hop between the two hostVerify using "intents" cli where the intents should be removed, Ping between the hosts connected to the devices between whom host intents were added should pass | 2 | Single node   Multi Node |
| 22 | Verify Point intent related SDN-IP matching on ICMPv6 | Check Ping between the hosts connected to the devices between whom point intents were added should pass | 1 | Single node |
| 23 | Verify Multi Point to single point intent related SDN-IP matching on IP prefix and rewriting mac address | Check Ping between the hosts connected to the devices between whom point intents were removed should pass | 1 | Multi Node |
| 24 | Verify add bidirectional point intents between 2 packet layer(mininet) devices | Check Ping between the hosts connected to the devices between whom point intents were added should pass | 1 | Single node   Multi Node |
|  |  |  |  |  |
