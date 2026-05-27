# Test Plan - CHO Test (CHO*)

CHO (Continuous Hours of Operation) test is a long-term regression test that is aimed to run for weeks at a time. Its goal is to find memory leaks or other bugs that otherwise cannot be easily seen with short-term tests.

Currently we deploy a 3-node onos cluster for CHO test. CHO tests run on 3 different types of topologies:

* ATT MPLS Topology (25 devices, 112 links)
* Cordal Ring Topology (25 devices, 600 links)
* Spine and Leaf Topology (78 devices, 284 links)
* H-AGG Topology (10 devices, 44 links)

In CHO test, what we basically do is triggering intent installation/withdrawal from ONOS CLI and link/device/onos instance down/up events from Mininet CLI, and checking if everything is still working properly after each event. Currently we have two versions of CHO test: CHOtest and CHOTestMonkey. CHOtest is built within the traditional test case based framework and runs a fixed list of test cases for a large number of iterations, while CHOTestMonkey runs on an experimental framework which randomly generates and triggers all kinds of events in ONOS and Mininet as the test runs.

Please take a look at the subpages for more details:

* [CHOtest Plans](test-plan-cho-test-cho/plan-chotest.md)
* [CHOTestMonkey Plans](test-plan-cho-test-cho/plan-chotestmonkey.md)

Since the framework of CHOTestMonkey is a little different from the other tests, we also provide a [tutorial for CHOTestMonkey](../../guides/system-testing-guide/onossystemtestteston-tutorial/cho-test-tutorial.md).
