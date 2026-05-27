# Test Plan - HA (HA*)

# **Test Suite Description**

The goal of the High Availability (HA) test suite is to verify how ONOS performs when there are control plane failures. As HA is a key goal in ONOS, we would like to see ONOS gracefully handle failures and continue to manage the data plane during these failures. In cases where ONOS becomes unavailable, say the entire cluster is rebooted, ONOS should quickly recover any persistent data and get back to running the network.

The general structure of this test suite is to start an ONOS cluster and confirm that it has reached a stable working state. Once this state is reached, we will trigger some failure scenario and verify that ONOS correctly recovers from the failure. Below you will find two tables, the first table describes the failure scenarios and the second table describes the functionality and state tests that are performed in each of the HA tests.

# **High Availability Tests Scenarios**

|  |  |  |
| --- | --- | --- |
| **Test** | **Failure Scenario** | **TestON Test name** |
| [HA Sanity Test](../test-results/onos-master/master-ha/master-ha-sanity.md) | This tests runs through all the [state and functionality checks of the HA Test suite](#TestPlanHA(HA*)-StateandFunctionalityChecksintheHATestSuite) but waits 60 seconds instead of inducing a failure. This is run as a 7 node ONOS cluster. | HAsanity |
| [Minority of ONOS Nodes shutdown](../test-results/onos-master/master-ha/master-ha-stop-nodes.md) | Restart 3 of 7 ONOS nodes by gracefully stopping the process once the system is running and stable. | HAstopNodes |
| Minority of ONOS Nodes continuous shutdown | Continuously (1000 times) restart 1 of 7 ONOS nodes iteratively by gracefully stopping the process once the system is running and stable. Then verify the node correctly restarts and joins the cluster. | HAcontinuousStopNodes |
| [Minority of ONOS Nodes killed](../test-results/onos-master/master-ha/master-ha-kill-nodes.md) | Restart 3 of 7 ONOS nodes by killing the process once the system is running and stable. | HAkillNodes |
| [Entire ONOS cluster restart](../test-results/onos-master/master-ha/master-ha-cluster-restart.md) | Restart 7 of 7 ONOS nodes by killing the process once the system is running and stable. | HAclusterRestart |
| [Single node cluster restart](../test-results/onos-master/master-ha/master-ha-single-instance-restart.md) | Restart 1 of 1 ONOS nodes by killing the process once the system is running and stable. | HAsingleInstanceRestart |
| [Control Network partition](../test-results/onos-master/master-ha/master-ha-full-network-partition.md) | Partition the Control Network by creating IP Table rules once the system is in a stable state.  During Partition:   * ONOS nodes that cannot cluster with a quorum of the cluster will relinquish leadership of any topic and give up any device roles * Nodes in the majority partition should be able to take up all the work of the cluster and continue to function normally   After partition is healed:   * Topology is consistent across all nodes and should reflect the current state of the network(including updates during partition) * Flows view should be consistent across all nodes * Intents should be available on all nodes including any new intents pushed to the majority partition * Mastership should be consistent across all nodes | HAfullNetPartition |
| [Dynamic Clustering: Swap nodes](../test-results/onos-master/master-ha/master-ha-swap-nodes.md) | Change membership of an ONOS cluster at run time   * Start a five node ONOS cluster configured to use a remote metadata file * Run common state and functionality checks * Replace two of the five ONOS nodes in the metadata file with two new ONOS nodes * Check that the two new nodes join the cluster and the two replaced nodes leave * Run common state and functionality checks | HAswapNodes |
| [Dynamic Clustering: Scale up/down](../test-results/onos-master/master-ha/master-ha-scaling.md) | Change the size of an ONOS cluster at run time   * Start a single node ONOS cluster configured to use a remote metadata file * Run common state and functionality checks * Scale the cluster up to seven nodes then back down to one node in increments of two nodes. * After changing cluster size:   + Check that the two new nodes join the cluster or the two old nodes leave   + Run common state and functionality checks | HAscaling |
| Offline Backup Recovery | Take a backup of ONOS data and resore ONOS using the backup   * Take a backup of each ONOS node's data * Uninstall and reinstall ONOS without starting the service * Copy the backed up data over to the new installations * Start ONOS using the backed up data | HAbackupRecover |
| ISSU | Perform an [In-Service Software Upgrade (ISSU)](../../community-information/brigades/issu.md) of ONOS   * Start ONOS * Initiate the upgrade * Restart a minority of nodes with the new ONOS version * Verify the new nodes have come up * Transition the cluster from the old version to the new version * Restart the remaining nodes with the new version one at a time * Commit the upgrade | HAupgrade |
| ISSU - Rollback | Rollback an [In-Service Software Upgrade (ISSU)](../../community-information/brigades/issu.md) of ONOS   * Start ONOS * Initiate the upgrade * Restart a minority of nodes with the new ONOS version * Verify the new nodes have come up * Transition the cluster from the old version to the new version * Rollback the upgrade * Restart the upgraded nodes with the old version one at a time | HAupgradeRollback |

# **State and Functionality Checks in the HA Test Suite**

|  |  |
| --- | --- |
| **Description** | **Passing Criteria** |
| Topology Discovery | * All Switches, Links, and Ports are discovered * All information (DPIDs, MACs, Port numbers) are correct * ONOS correctly discovers any change in dataplane topology * Each node in an ONOS cluster has the same correct view of the topology |
| Device Mastership | * Devices have one and only one ONOS node as master * Mastership correctly changes when device roles are manually changed * Mastership fails over if current master becomes unavailable * Each node in an ONOS cluster has the same view of device mastership |
| Intents | * Intents can be added between hosts * Hosts connected by Intents have dataplane connectivity * Intents remain in the cluster as long as some ONOS nodes are available * Connectivity is preserved during dataplane failures as long as at least one path exists between the hosts |
| Switch Failure | * Topology is updated and intents are recompiled |
| Link Failure | * Topology is updated and intents are recompiled |
| Leadership Election | Applications can run for leadership of topics. This service should be safe, stable and fault tolerant.   * The service is functional before and after failures, nodes can withdraw and run for election * There is always only one leader per topic in an ONOS cluster. |
| Distributed Sets | Call each of the following APIs and make sure they are functional and cluster wide   * get() * size() * add() * addAll() * contains() * containsAll() * remove() * removeAll() * clear() * retain()   In addition, we also check that sets are unaffected by ONOS failures |
| Distributed Atomic Counters | Call each of the following APIs and make sure they are functional and cluster wide   * incrementAndGet()   In addition, we also check that sets are unaffected by ONOS failures.  Note: In-memory counters will not persist across cluster wide restarts |
| Cluster Service | * Every ONOS node should be clustered with every other node in the test (unless we specifically make one unavailable) |
| Application Service | * Application IDs are unique to an application * Application activation * Application deactivation * Active applications reactivate on restart |
