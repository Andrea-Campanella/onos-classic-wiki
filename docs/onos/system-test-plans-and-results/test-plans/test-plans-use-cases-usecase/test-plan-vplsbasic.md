# Test Plan - VPLSBasic

### Purpose

The purpose of this test is to test various Virtual Private LAN Server (VPLS) CLI commands.

### Test Overview

The test uses the configuration of 1 Mininet node and 3 ONOS nodes.  Mininet topology consists of 6 hosts, 6 switches, and 15 links, which is loaded from onos/tools/test/topos/vpls.py. Hosts 1, 2, 3, and 4 are assigned as VLAN hosts.  After initialization, the test will execute a VPLS CLI command, then check connectivity between hosts.  For the test to pass, all commands must be successfully executed, and connectivity should always be as expected after each command is run.

| Test Case # | Description | Pass/Fail Criteria |
| --- | --- | --- |
| 1 | Compile ONOS, push ONOS to test machines, set up Mininet, and set up test parameters. | Pass: Mininet, ONOS, and parameters are set up correctly. |
| 2 | Load and test VPLS configurations from .json configuration file located in onos/tools/test/topos. | Pass: Configurations are loaded correctly, connectivity is as expected. |
| 10 | Remove an interface from a VPLS network. | Pass: Connectivity tests are as expected. |
| 11 | Clean all VPLS configurations. | Pass: Connectivity tests are as expected. |
| 12 | Create a new VPLS network. | Pass: Connectivity tests are as expected. |
| 13 | Add interfaces to the new VPLS network. | Pass: Connectivity tests are as expected. |
| 14 | Add MPLS encapsulation. | Pass: Connectivity tests are as expected. |
| 15 | Change an encapsulation type. | Pass: Connectivity tests are as expected. |
| 16 | Remove encapsulation. | Pass: Connectivity tests are as expected. |
