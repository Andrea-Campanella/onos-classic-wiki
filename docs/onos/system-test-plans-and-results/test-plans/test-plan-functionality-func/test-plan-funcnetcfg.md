# Test Plan - FUNCnetCfg

Test suite for the Network Configuration subsystem

### Purpose

The purpose of this test suite is to verify the functionality of the Network Configuration Subsystem. We will test the ability to add and distribute configurations across nodes as well as how other subsystems use these configurations. The test suite ensures the functionality of the ONOS’s ability to use the NETCONF communication protocol to configure switches.

### Test Overview

This test uses a single node which will be emulated via mininet.  It will use a combination of the REST API and the ONOS CLI to connect, configure, and disconnect a device using the NETCONF protocol.  This test does not configure specific devices, but rather demonstrates the ability of ONOS to configure a device using NETCONF assuming the appropriate drivers and variables are set. The specifics of the device to be connected should be set in the .params file.

| Test Case# | Description | Pass/Fail Criteria |
| --- | --- | --- |
| 1 | Set up test parameters | pass: If params are set |
| 2 | Set cells and build, uninstall, and install ONOS | pass: If sets cells correctly and builds, uninstalls, and installs ONOS correctly |
| 8 | Compare MN topology and ONOS topology | pass: If ONOS topology is the same as the Mininet topology |
| 9 | Report logs | pass |
| 10 | Setup Mininet with 1.0 OVS (start mn, assign mastership to switches, and compares topology) | pass: If Mininet, switch assignment and topology comparison all pass |
| 11 | Setup Mininet with 1.3 OVS (start mn, assign mastership to switches, and compares topology) | pass: If Mininet, switch assignment and topology comparison all pass |
| 12 | Assign switch to controller | pass: If assign switch to controller successfully |
| 14 | Stop Mininet | pass: If Mininet stops |
| 20 | Add some device configurations for undiscovered devices and then check they are distributed to all nodes | pass: If the given NetCfgs are added and distributed to all ONOS nodes |
| 21 | Check that devices appear or don't appear in the Network Graph according to the initial NetCfgs | pass: If the allowed devices appear in the network graph and the disallowed devices don't |
| 22 | Add some device configurations for discovered devices and then check they are distributed to all nodes | pass: If the given NetCfgs are added and distributed to all ONOS nodes |
| 23 | Check that only disallowed devices disappear from the Network Graph according to the additional NetCfgs | pass: If only the diallowed devices disappear from the network graph |
| 24 | Remove Network Configurations using different methods. I.E. delete a device, delete multiple devices, delete all configs | pass: If the deleted NetCfgs are deleted from all nodes |
| 25 | Preparing network-cfg.json to load configurations | pass: If successfully copied network-cfg.json to target directory |
| 26 | Check that pre-build configurations are correct | pass: If pre-build configurations were set correctly |
| 27 | Posting network configurations to the top level web resource | pass: If post network configuration successfully |
