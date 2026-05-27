# Test Plan - VPLSfailsafe

### Purpose

The purpose of this test is to test Virtual Private Lan Server (VPLS) connectivity in instances of various connectivity failures.  Connectivity between hosts will re-route when a service or link goes down.  This test verifies that the connection is re-routed properly.

### Test Overview

The test uses a configuration similar to the VPLSBasic test configuration: 1 Mininet node, and 3 ONOS nodes.  Each case will stop a specific service and test connectivity, then restart the service and test connectivity again.

| Test Case # | Description | Pass or Fail Criteria |
| --- | --- | --- |
| 1 | Compile ONOS, push ONOS to test machines, set up Mininet, and set up test parameters. | Pass: Mininet, ONOS, and parameters are set up correctly. |
| 2 | Load and test VPLS configurations from .json configuration file located in onos/tools/test/topos. | Pass: Configurations are loaded correctly, connectivity is as expected. |
| 50 | Initial connectivity test. | Pass: Intents are installed and connectivity is as expected. |
| 100 | Bring 1 host down at a time and test connectivity. Then bring the host back up and test connectivity. | Pass: Host is brought down and passes connectivity check. Host is brought up and passes connectivity check. |
| 200 | Bring 1 switch down at a time and test connectivity. Then bring the switch back up and test connectivity. | Pass: Switch is brought down and passes connectivity check. Switch is brought up and passes connectivity check. |
| 300 | Stop 1 ONOS node at a time and test connectivity. Then restart the ONOS node and test connectivity. | Pass: ONOS node stops and passes connectivity check. ONOS node restarts and passes connectivity check. |
| 310 | Kill 1 ONOS node at a time and test connectivity. Wait for the ONOS node to restart, then test connectivity. | Pass: ONOS node is killed and passes connectivity check. ONOS node automatically restarts and passes connectivity check. |
| 400 | Bring 1 link down at a time and test connectivity. Then bring the link back up and test connectivity. | Pass: Link is brought down and passes connectivity check. Link is brought up and passes connectivity check. |
