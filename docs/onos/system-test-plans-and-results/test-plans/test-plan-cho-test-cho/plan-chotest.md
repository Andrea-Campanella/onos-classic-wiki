# Plan - CHOtest

CHO sequence of Tests : All Tests run for N number of iterations

Sample test case sequence: 1,20,3,47,147,[5,60,160,70,80,10,5,90,190,71,81,10]\*10,200,21,3,48,148,[5,61,161,72,82,10,5,91,191,73,83,10]\*10,200,22,3,49,149,[5,62,162,74,84,10,5,92,192,75,85,10]\*10

| Test Case # | Description | Pass/Fail Criteria |
| --- | --- | --- |
| 1 | Start ONOS cluster with 3 nodes | Verify all 5 ONOS instances are up and running with latest build and start ONOS CLI |
| 20 | Start ATT topology, assign controllers and balance mastership | ATT topology starts correctly |
| 21 | Start Chordal topology, assign controllers and balance mastership | Chordal topology starts correctly |
| 22 | Start Spine-leaf topology, assign controllers and balance mastership | Spine-leaf topology starts correctly |
| 3 | Check consistency of ONOS and Mininet topologies | ONOS topology matches Mininet topology |
| 47 | Use fwd app and ping to discover all hosts in ATT topology | fwd app successfully activated and then deactivated |
| 48 | Use fwd app and ping to discover all hosts in Chordal topology | fwd app successfully activated and then deactivated |
| 49 | Use fwd app and ping to discover all hosts in Spine-leaf topology | fwd app successfully activated and then deactivated |
| 147 | Use fwd app and ping6 to discover all ipv6 hosts in ATT topology | fwd app successfully activated and then deactivated |
| 148 | Use fwd app and ping6 to discover all ipv6 hosts in Chordal topology | fwd app successfully activated and then deactivated |
| 149 | Use fwd app and ping6 to discover all ipv6 hosts in Spine-leaf topology | fwd app successfully activated and then deactivated |
| 5 | Compare current ONOS topology with reference data | ONOS topology matches reference data |
| 60 | Install 300 host intents and verify pingall in ATT topology | All intents are installed and pingall passed |
| 61 | Install 300 host intents and verify pingall in Chordal topology | All intents are installed and pingall passed |
| 62 | Install 2278 host intents and verify pingall in spine-leaf topology | All intents are installed and pingall passed |
| 160 | Verify IPv6 pingall across 300 host intents in ATT topology | Pingall passed |
| 161 | Verify IPv6 pingall across 300 host intents in Chordal topology | Pingall passed |
| 162 | Verify IPv6 pingall across 300 host intents in Spine-leaf topology | Pingall passed |
| 70 | Link down and verify pingall across 300 host intents in ATT topology | Link down discovered by ONOS and pingall passed |
| 71 | Link down and verify pingall across 600 point intents in ATT topology | Link down discovered by ONOS and pingall passed |
| 72 | Link down and verify pingall across 300 host intents in Chordal topology | Link down discovered by ONOS and pingall passed |
| 73 | Link down and verify pingall across 600 point intents in Chordal topology | Link down discovered by ONOS and pingall passed |
| 74 | Link down and verify pingall across 2278 host intents in Spine-leaf topology | Link down discovered by ONOS and pingall passed |
| 75 | Link down and verify pingall across 4556 point intents in Spine-leaf topology | Link down discovered by ONOS and pingall passed |
| 80 | Link up and verify pingall across 300 host intents in ATT topology | Link up discovered by ONOS and pingall passed |
| 81 | Link up and verify pingall across 600 point intents in ATT topology | Link up discovered by ONOS and pingall passed |
| 82 | Link up and verify pingall across 300 host intents in Chordal topology | Link up discovered by ONOS and pingall passed |
| 83 | Link up and verify pingall across 600 point intents in Chordal topology | Link up discovered by ONOS and pingall passed |
| 84 | Link up and verify pingall across 2278 host intents in Spine-leaf topology | Link up discovered by ONOS and pingall passed |
| 85 | Link up and verify pingall across 4556 point intents in Spine-leaf topology | Link up discovered by ONOS and pingall passed |
| 90 | Install 600 point intents and verify pingall in ATT topology | All intents are installed and pingall passed |
| 91 | Install 600 point intents and verify pingall in Chordal topology | All intents are installed and pingall passed |
| 92 | Install 4556 point intents and verify pingall in Spine-leaf topology | All intents are installed and pingall passed |
| 190 | Verify IPv6 pingall across 600 point intents in ATT topology | Pingall passed |
| 191 | Verify IPv6 pingall across 600 point intents in Chordal topology | Pingall passed |
| 192 | Verify IPv6 pingall across 4556 point intents in Spine-leaf topology | Pingall passed |
| 200 | Clean up ONOS | Successfully removed devices and hosts |
