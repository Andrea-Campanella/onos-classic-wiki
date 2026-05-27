# Single Instance 1.0

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Jenkins test result for 22:46 on Jun 24, 2015.

## Test ProdFunc

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

### Result summary for Testcase1

This testcase is testing setting up test environment

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Uninstalling ONOS package successful

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

Link Down discovered properly

Link up discovered properly

ONOS Topology matches MN Topology

Result: Pass

### Result summary for Testcase8

This testcase removes any previously added intents before adding any new set of intents

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

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

Result: Pass

### Result summary for Testcase20

This testcase exits the mininet cli and reinstallsONOS to switch over to Packet Optical topology

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ONOS instance is up and ready

Result: Pass

### Result summary for Testcase21

This testcase starts the packet layer topology and REST

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Result: Pass

### Result summary for Testcase22

This testcase compares the optical+packet topology against what is expected

Failed to load packet optical topology

Result: Failed

### Result summary for Testcase10

This testcase uninstalls the reactive forwarding app

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Result: Pass

### Result summary for Testcase23

This testcase adds bidirectional point intents between 2 packet layer( mininet ) devices and ping mininet hosts

Failed to add point intents

Failed to ping between h1 and h5

Result: Failed

### Result summary for Testcase24

This testcase tests rerouting and pings mininet hosts

Links state is inactive as expected due to one of the ports being down

Failed to ping between h1 and h5

Failed to bring the port up

Result: Failed
