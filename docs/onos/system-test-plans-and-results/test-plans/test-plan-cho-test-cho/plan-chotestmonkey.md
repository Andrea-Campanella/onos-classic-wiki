# Plan - CHOTestMonkey

Although CHOTestMonkey still runs based on test cases, we don't explicitly specify pass/fail criteria for each test case, but catch abnormal conditions of ONOS by injecting various checking into each test case.

Sample test case sequence:

0,1,2,3,[10,30,21,31,10,32,21,33,50,10,30,21,31,10,32,21,33,51,40,60,10,30,21,31,10,32,21,33,50,10,30,21,31,10,32,21,33,51,41,60]\*500,100

| Test Case # | Description |
| --- | --- |
| 0 | Initialize CHOTestMonkey |
| 1 | Load topology and balances all switches |
| 2 | Collect and store device and link data from ONOS |
| 3 | Collect and store host data from ONOS |
| 10 | Run all enabled checks |
| 20 | Bring down/up links and check topology and ping |
| 21 | Bring down/up a group of links and check topology and ping |
| 30 | Install host intents and check intent states and ping |
| 31 | Uninstall host intents and check intent states |
| 32 | Install point intents and check intent states and ping |
| 33 | Uninstall point intents and check intent states |
| 40 | Randomly bring down one ONOS node |
| 41 | Randomly bring up one ONOS node that is down |
| 50 | Set FlowObjective to True |
| 51 | Set FlowObjective to False |
| 60 | Rebalance devices across controllers |
| 70 | Run randomly generated events |
| 80 | Replay events from log file |
| 90 | Sleep for some time |
| 100 | Wait until the test stops |

We also list all enabled and planned events in CHOTestMonkey:

| Event Index | Event Name | Description |
| --- | --- | --- |
| 0 | NULL | Do nothing |
| 1 | TEST\_PAUSE | Pause the test |
| 2 | TEST\_RESUME | Resume the test from pausing |
| 3 | TEST\_SLEEP | Make the test sleep for some time |
| 10 | CHECK\_INTENT | Check whether all intents are in expected state |
| 11 | CHECK\_FLOW | Check whether all flows in ONOS are in ADDED state and match those on Mininet |
| 12 | CHECK\_TRAFFIC | Check whether all installed intents work by sending ping traffic |
| 13 | CHECK\_TOPO | Check whether the number of devices, links and hosts are as expected and match those in Mininet |
| 14 | CHECK\_ONOS | Check whether the mastership, leaders and ONOS node states are as expected |
| 20 | NETWORK\_LINK\_DOWN | Bring down a link in Mininet |
| 21 | NETWORK\_LINK\_UP | Bring up a link in Mininet |
| 22 | NETWORK\_DEVICE\_DOWN | Bring down a device in Mininet |
| 23 | NETWORK\_DEVICE\_UP | Bring up a device in Mininet |
| 30 | APP\_INTENT\_HOST\_ADD | Add a host intent via ONOS CLI |
| 31 | APP\_INTENT\_HOST\_DEL | Remove a host intent via ONOS CLI |
| 32 | APP\_INTENT\_POINT\_ADD | Add a point intent via ONOS CLI |
| 33 | APP\_INTENT\_POINT\_DEL | Remove a point intent via ONOS CLI |
| 40 | ONOS\_ONOS\_DOWN | Bring down an ONOS node |
| 41 | ONOS\_ONOS\_UP | Bring up an ONOS node |
| 42 | ONOS\_SET\_CFG | Set a configuration via ONOS CLI |
| 43 | ONOS\_SET\_FLOWOBJ | Set flow objective to True or False via ONOS CLI |
| 44 | ONOS\_BALANCE\_MASTERS | Run balance-masters via ONOS CLI |
| 110 | CHECK\_ALL | Inject all enabled check events into the test |
| 120 | NETWORK\_LINK\_RANDOM\_TOGGLE | Randomly bring down a link in Mininet and then bring it up |
| 121 | NETWORK\_LINK\_GROUP\_RANDOM\_TOGGLE | Randomly bring down a group of links in Mininet and then bring them up |
| 122 | NETWORK\_DEVICE\_RANDOM\_TOGGLE | Randomly bring down a device in Mininet and then bring it up |
| 123 | NETWORK\_DEVICE\_GROUP\_RANDOM\_TOGGLE | Randomly bring down a group of devices in Mininet and then bring them up |
| 130 | APP\_INTENT\_HOST\_ADD\_ALL | Add host intents for all host pairs in the network |
| 131 | APP\_INTENT\_HOST\_DEL\_ALL | Remove host intents for all host pairs in the network |
| 132 | APP\_INTENT\_POINT\_ADD\_ALL | Add point intents for all device pairs in the network |
| 133 | APP\_INTENT\_POINT\_DEL\_ALL | Remove point intents for all device pairs in the network |
| 140 | ONOS\_ONOS\_RANDOM\_TOGGLE | Randomly bring down an ONOS node and then bring it up |
