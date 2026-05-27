# Test Plan - FUNCgroup

### Purpose

The purpose of this test is to add flows in differing REST API group types and to test the groups by sending packets using Scapy.

### Test Overview

The test configuration consists of 1 ONOS node and 1 Mininet node.  The Mininet topology contains 4 hosts and 4 switches, and is read from "topo-group.py" located in /mininet/custom/.  After the initialization cases, a group with type "ALL" is tested, then a group with type "INDIRECT" is tested.

| Test Case # | Description | Pass/Fail Criteria |
| --- | --- | --- |
| 1 | Initialize variables. There is an option to pull and build ONOS package. | Variables are copied and environment setup passes. |
| 2 | Install ONOS. | ONOS setup passes. |
| 3 | Start Mininet and verify topology. | Mininet with topology loads, and switch assignment passes. |
| 4 | Test Scapy (currently not run in test). | Send and receive a packet successfully when the filter does and does not match. |
| 5 | Test group with type "ALL". | Group is added, flow is added to group, and Scapy packet is sent and received successfully. |
| 6 | Delete group and flow. | Flow is removed by device ID and flow ID, and group is deleted by device ID and app cookie. |
| 7 | Test group with type "INDIRECT". | Group of type "INDIRECT" is created, flow is added to group, and Scapy packet is sent and received successfully. |
| 100 | Check logs for errors and warnings. | N/A |
