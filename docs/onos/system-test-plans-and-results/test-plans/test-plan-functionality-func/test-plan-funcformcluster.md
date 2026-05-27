# Test Plan - FUNCformCluster

Test suite for the onos-form-cluster

### Purpose

The purpose of this test suite is to verify the functionality of the onos-form-cluster command. We will test the ability to form a cluster from the multiple single node ONOS. The test suite ensures the functionality of the ONOS’s ability to use the onos-form-cluster and comparing a configuration of the ONOS before and after form cluster.

Test Overview

This test uses seven single node at the beginning. It will check the number of the node which all should be 1 at the beginning. Then, it will form the cluster and re-check the number of the node. This case, since seven single node has been formed to one cluster, they all should have 7 nodes. Then, it will start a simple Mininet to test the ping and compare the topology.

| Test Case# | Description | Pass/Fail Criteria |
| --- | --- | --- |
| 0 | Set up test parameters. | pass: If params are set |
| 1 | Install 7 single nodes and start the ONOS. | pass: If sets cells correctly and builds, uninstalls, and installs ONOS correctly |
| 2 | Form a cluster to 7 single nodes. | pass: If successfully formed a cluster. |
| 3 | Checking the ONOS configuration of the single node ONOS. | pass: If each ONOS has one node and only one of them has extra app activated |
| 4 | Checking the ONOS configuration of the cluster formed ONOS. | pass: If each ONOS has 7 nodes, state of the node is in ready, and all of them has extra app activated. |
| 5 | Starting Mininet and verifying Topology. | pass: If successfully verify the topology. |
