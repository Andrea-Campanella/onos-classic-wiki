# Multi Instance 1.3

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Jenkins test result for 23:16 on Jun 24, 2015.

## Test MultiProd13

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

### Result summary for Testcase1

This testcase is testing setting up test environment

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Installing ONOS package successful

ONOS instances are up and ready

Result: Pass

### Result summary for Testcase4

This testcase is testing the assignment of all the switches to all controllers and discovering the hosts in reactive mode

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Controller assignment successfull

Pingall Test in reactive mode to discover the hosts successful

Result: Pass

### Result summary for Testcase10

This testcase uninstalls the reactive forwarding app

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Result: Pass

### Result summary for Testcase5

This testcase is testing if all ONOS nodes are in topology sync with mininet and its peer ONOS nodes

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topology Check Test with mininetand ONOS instances successful

Result: Pass

### Result summary for Testcase6

This testcase is testing the addition of host intents and then doing pingall

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Host intents have been installed correctly

Result: Pass

### Result summary for Testcase7

This testscase is killing a link to ensure that link discovery is consistent

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Link Down discovered properly

Link up discovered properly

Result: Pass

### Result summary for Testcase8

This testcase removes any previously added intents

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Intent removal successful

Result: Pass

### Result summary for Testcase6

This testcase is testing the addition of host intents and then doing pingall

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Host intents have been installed correctly

Result: Pass

### Result summary for Testcase8

This testcase removes any previously added intents

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Intent removal successful

Result: Pass

### Result summary for Testcase9

This testcase adds point intents and then does pingall

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Ping all test after Point intents addition successful

Result: Pass

### Result summary for Testcase8

This testcase removes any previously added intents

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Intent removal successful

Result: Pass

### Result summary for Testcase31

This test case adds point intent related to SDN-IP matching on ICMP

Ping all test after Point intents related to SDN-IP matching on ICMP successful

Result: Pass

### Result summary for Testcase32

This test case adds point intent related to SDN-IP matching on TCP

Point intent related to SDN-IP matching on TCP install successful

iperf test successful

Result: Pass

### Result summary for Testcase8

This testcase removes any previously added intents

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Intent removal successful

Result: Pass

### Result summary for Testcase33

This test case adds multipoint to singlepoint intent related to SDN-IP matching on destination ip and rewrite mac address action

Ping between h8 and h10 failed. Making attempt number 2 in 2 seconds

Ping test failed.

Ping all test after multipoint to single point intent addition with rewrite mac address failed

Result: Failed

### Result summary for Testcase8

This testcase removes any previously added intents

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Intent removal successful

Result: Pass

### Result summary for Testcase20

This testcase exits the mininet cli and reinstallsONOS to switch over to Packet Optical topology

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Installing ONOS package successful

ONOS instances are up and ready

ONOS cli starts properly

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

Point intents for packet optical have not ben installed correctly. Cleaning up

Point intents addition for packet optical andPingall Test NOT successful

Result: Failed

### Result summary for Testcase24

This testcase tests rerouting and pings mininet hosts

Links state is inactive as expected due to one of the ports being down

Ping test failed

Packet optical rerouting failed

Result: Failed
