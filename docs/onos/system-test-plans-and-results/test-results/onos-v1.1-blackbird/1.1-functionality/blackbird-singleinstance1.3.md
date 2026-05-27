# Blackbird - SingleInstance1.3

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Jenkins test result for 04:18 on May 16, 2015.

## Test ProdFunc

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

### Result summary for Testcase1

This testcase is testing setting up test environment

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

commit 8d3de3dfacb271516464d0d10dd9f1335ee879a0 (HEAD, origin/master, origin/HEAD, master)

Author: Bri Prebilic Cole [bri@onlab.us]

AuthorDate: Fri May 15 16:02:59 2015 -0700

Commit: Bri Prebilic Cole [bri@onlab.us]

CommitDate: Fri May 15 16:03:06 2015 -0700

GUI -- Titles on topo panels overflow to the next line instead of going off of the screen.

Installing ONOS package successful

ONOS instance is up and ready

Result: Pass

### Result summary for Testcase4

This testcase is testing the assignment of all the switches to all the controllers and discovering the hosts in reactive mode

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Controller assignmnet successful

Pingall Test in reactive mode to discover the hosts successful

Result: Pass

### Result summary for Testcase10

This testcase uninstalls the reactive forwarding app

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Result: Pass

### Result summary for Testcase5

This testcase is testing if all ONOS nodes are in topology sync with mininet

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ONOS Topology matches MN Topology

Result: Pass

### Result summary for Testcase6

This testcase is testing the addition of host intents and then does pingall

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Ping all test after Host intent addition successful

Result: Pass

### Result summary for Testcase7

This testscase is killing a link to ensure that link discovery is consistent

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Killing a link to ensure that link discovery is consistent

Link down was not discovered in 5 seconds

Link up was not discovered in 5 seconds

ONOS Topology matches MN Topology

Result: Failed

### Result summary for Testcase8

This testcase removes any previously added intents before adding any new set of intents

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Intent removal successful

Installed intents have been withdrawn correctly

Intent removal successful

Result: Pass

### Result summary for Testcase9

This test case adds point intents and then does pingall

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Point Intents have been installed correctly

Result: Pass

### Result summary for Testcase8

This testcase removes any previously added intents before adding any new set of intents

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Intent removal successful

Installed intents have been withdrawn correctly

Intent removal successful

Result: Pass

### Result summary for Testcase11

This testcase moves a host from one switch to another to addpoint intents between them and then perform ping

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Point intents for hosts on same devicesinstalled correctly. Cleaning up

Result: Pass

### Result summary for Testcase8

This testcase removes any previously added intents before adding any new set of intents

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Intent removal successful

Installed intents have been withdrawn correctly

Intent removal successful

Result: Pass

### Result summary for Testcase2

This testcase is testing a switch down discovery

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Killing a switch to ensure it is discovered correctly

Deleting s28

Result: Pass

### Result summary for Testcase20

This testcase exits the mininet cli and reinstallsONOS to switch over to Packet Optical topology

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Installing ONOS package successful

ONOS instance is up and ready

Result: Pass

### Result summary for Testcase21

This testcase starts the packet layer topology and REST

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Result: Pass

### Result summary for Testcase22

This testcase compares the optical+packet topology against what is expected

Packet optical topology discovery failed

Result: Failed

### Result summary for Testcase10

This testcase uninstalls the reactive forwarding app

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Result: Pass

### Result summary for Testcase23

This testcase adds bidirectional point intents between 2 packet layer( mininet ) devices and ping mininet hosts

Point Intents for packet optical have been installed correctly

Result: Pass

### Result summary for Testcase24

This testcase tests rerouting and pings mininet hosts

Links state is inactive as expected due to one of the ports being down

Ping test successful

Result: Pass
