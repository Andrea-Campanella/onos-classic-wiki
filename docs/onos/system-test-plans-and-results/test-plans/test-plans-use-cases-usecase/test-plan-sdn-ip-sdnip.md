# Test Plan - SDN-IP (SDNIP*)

#### TEST METHODOLOGY

We run through a number of different scenarios, where each scenario changes the number of BGP peers, routes, ONOS instances, BGP speakers.

The test script should be able to set up a given number of BGP peers, then it should be able to dynamically add or remove routes into the system (by talking to the external router’s CLI).

The main verification mechanism should be to check that the intent store in ONOS has exactly the intents we expect. This implies that the test verification script should be able to calculate the correct intents based of the inputs that it gives (inputs being the routes and the peer locations).

As a secondary verification mechanism we can ping through the network to ensure the entire system is functional.

#### TEST SCENARIOS (SINGLE INSTANCE OF SDN-IP/ONOS AND BGP SPEAKER)

| ID | **TestON Case** | **Description** | Environment | **Passing Criteria** |
| --- | --- | --- | --- | --- |
| 1 | 1 | Basic test to establish functionality | Using the same mininet script for Dec.5 demo, which includes 4 BGP peers.  All bgp routers/speakers are quagga before Dec.5  (We may also use bird after Dec.5) | Test steps:  Each BGP peer advertises 10 routes  Check the correctness of routes from ONOS CLI  Check the correctness of intents from ONOS CLI  Ping test for each route  (For each route, we will create an relative IP address on the host behind router)   All BGP peers withdraw all routes  Check the correctness of routes from ONOS CLI  Check the correctness of intents from ONOS CLI  Ping test for each route |
| 2 | 2 | Run a test with a highly fluctuating route stream.  Repeat a few times with cycles of intense route fluctuation |  | Repeat Case1 with cycles of 1000 times |
| 3 | 3 | Scaling test with a large number of peers and routes | Using the same mininet script for Dec.5 demo, but add up to 100 peers | Test steps:  Each BGP peer advertises 1000 routes  Check the correctness of routes from ONOS CLI  Check the correctness of intents from ONOS CLI  Ping test for each route   All BGP peers withdraw all routes  Check the correctness of routes from ONOS CLI  Check the correctness of intents from ONOS CLI  Ping test for each route |
| 4 | 4 | Simulate an IXP - one peer is a route server advertising routes to other next hops.  Run the test with route fluctuation | Based on Case3  Add a route server and a new router and a new host to mininet | The route server advertises 10 routes each time as other BGP peers |

#### TEST SCENARIOS (MULTIPLE INSTANCES OF SDN-IP/ONOS AND BGP SPEAKERS)

| ID | **TestON Case** | **Description** | Environment | **Passing Criteria** |
| --- | --- | --- | --- | --- |
| 5 | 5 | Send a stream of route updates into the system, and at some point kill the primary SDN-IP instance.  Stop the route update stream and check that the intents and data plane are correct | Using the same mininet script for Dec.5 demo   Includes 4 external BGP peers  Running 2 ONOS instances and 1 BGP speaker  Some switches connect to ONOS 1, some to ONOS 2 | Test Steps:  Insert routes from BGP peers and do not stop  Kill primary ONOS/SDN-IP instance  List all routes and intents through CLI of the second ONOS instance  Continue inserting the routes from BGP peers  Stop inserting the routes from BGP peers  Check the routes and intents in the second ONOS instance  Ping test for each route |
| 6 | 6 | Send a stream of route updates into the system, and at some point kill the primary SDN-IP instance.  Stop the route update stream and check that the intents and data plane are correct | Using the same mininet script for Dec.5 demo  Running 2 ONOS instances and 2 BGP speaker  Some switches connect to ONOS 1, some to ONOS 2 | Test Steps:  Check BGP/ICMP path intents  Use ping to check the connectivity of BGP peers in dataplane.   Insert routes from BGP peers and do not stop  Kill primary ONOS/SDN-IP instance  Continue inserting routes from BGP peers  Stop inserting the routes from BGP peers  Check the routes and intents in the ONOS instance  Ping test for each route |
| 7 | 7 | Send a stream of route updates into the system, and at some point kill the BGP speaker.  Stop the route update stream and check that the intents and data plane are correct | Same environment with Case 6 | Test Steps:  Insert routes from BGP peers and do not stop  Kill one BGP speaker  Continue inserting routes from BGP peers  Stop inserting the routes from BGP peers  Check the routes and intents in the ONOS instance  Ping test for each route |
| 8 | 8 | Nightly testing to demo on Dec.5, the test steps will totally the same with the demo steps  But the environment is on a single VM. | Using the same mininet script for Dec.5 demo | Test Steps:  Each BGP peer advertise 10 routes  Check the correctness of routes from ONOS CLI  Check the correctness of intents from ONOS CLI  Ping test for each route   Bring down a link  Wait 20 seconds  Check the correctness of routes from ONOS CLI  Ping test for each route   Bring down a router  Wait 20 seconds  Check the correctness of routes from ONOS CLI  Check the correctness of intents from ONOS CLI  Ping test for each route   Bring up the link  Wait 20 seconds  Check the correctness of routes from ONOS CLI  Check the correctness of intents from ONOS CLI  Ping test for each route   Bring up the router  Wait 20 seconds  Check the correctness of routes from ONOS CLI  Check the correctness of intents from ONOS CLI  Ping test for each route   Then do it (bring down link/router, bring up link/router) in a loop for nightly testing. |

#### PERFORMANCE TEST

| ID | **TestON Case** | **Description** | Environment | **Passing Criteria** |
| --- | --- | --- | --- | --- |
| 9 | 9 | The purpose of the performance is to check:  How many routes can SDN-IP handle?  What route update rate can it sustain?  How many peers can we handle? (There’s probably no huge issues for handling more peers apart  from it requires more flow table space. As long as we can handle 100 or so we should be OK)  Where’s the bottleneck in the overall mechanism? (at least, is SDN-IP or the rest of ONOS?) | Using the same mininet script for Dec.5 demo  But add up to 100 peers | Test steps:  Insert 10,000->100,000-> 1000,000 routes from all BGP peers, check what will happen. |
