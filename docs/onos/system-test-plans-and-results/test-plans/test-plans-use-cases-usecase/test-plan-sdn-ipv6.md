# Test Plan - SDN-IPv6

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | Verify Modify IPv6 Source Address | Configure and connect the Primary-controller. Create a flow with action OFPAT\_SET\_NW\_SRC and output to an egress port. Send matching packet to ingress port. Verify packet gets output to egress port with correct IPv6 source address as specified in the flow. | 2 | Single node   Multi Node |
| 2 | Verify Modify IPv6 destination address | Configure and connect the Primary-controller. Create a flow with action OFPAT\_SET\_NW\_DST and output to an egress port. Send matching packet to ingress port. Verify packet gets output to egress port with correct IPv6 destination address as specified in the flow. | 3 | Single node   Multi Node |
| 3 | Verify Implement test script for one hop point intent | Form a switch with 2 host Add a one hop between the two hostVerify using "intents" cli where the intents should be removed, Ping between the hosts connected to the devices between whom host intents were added should pass | 2 | Single node   Multi Node |
| 4 | Verify Point intent related SDN-IP matching on ICMPv6 | Check Ping between the hosts connected to the devices between whom point intents were added should pass | 1 | Single node |
| 5 | Verify Multi Point to single point intent related SDN-IP matching on IP prefix and rewriting mac address | Check Ping between the hosts connected to the devices between whom point intents were removed should pass | 1 | Multi Node |
| 6 | Verify add bidirectional point intents between 2 packet layer(mininet) devices | Check Ping between the hosts connected to the devices between whom point intents were added should pass | 1 | Single node   Multi Node |
