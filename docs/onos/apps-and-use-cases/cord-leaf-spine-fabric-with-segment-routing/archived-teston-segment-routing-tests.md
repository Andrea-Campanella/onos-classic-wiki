# [Archived] TestON Segment Routing tests

Deprecated

This page is deprecated and may be removed in a near future.  
The new entry point of Trellis underlay fabric installation guide can be found at [Fabric Test Guide](https://wiki.opencord.org/display/CORD/Fabric+Test+Guide).

TestOn is the testing framework used at ONLAB to run nightly test of ONOS. This page describes the tests ran over the Segment Routing application.

To install TestOn follow this [link on the wiki.](../../guides/system-testing-guide/system-test-setup-overview.md)

A connectivity test is currently running nightly. The test consists of 3 Steps:

1. Configure and installs ONOS
2. Start mininet and check flow state
3. Test connectivity

The test runs for the following configurations of apps:

1. drivers,segmentrouting,openflow-base,netcfghostprovider,netcfglinksprovider
2. drivers,segmentrouting,openflow

The test runs for the following topologies:

1. 2x2 Leaf-Spine
2. 4x4 Leaf-Spine

The following tests Should be implemented:

1. [2/2] Full connectivity test (SRSanity)
2. [1/1] VLAN cross-connect configuration (Xconnect)
3. [0/5] Multicast
4. [0/5] vRouter integration
5. [0/4] Dynamic configuration of Xconnect and Hosts
6. [3/6] Control plane resilience
7. [3/6] Data plane resilence

Below we describe these tests in detail

**CASE101: Completed but not being executed**

* Description: Full connectivity test
* Topology: 2x2 Leaf-Spine Fabric
* Configuration: openflow
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, execute pingall twice.
* Expect: All pings succeed

**CASE102: Completed and Running (SRSanity)**

* Description: Full connectivity test
* Topology: 2x2 Leaf-Spine Fabric
* Configuration: openflow-base, etc.
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, execute pingall twice.
* Expect: All pings succeed

**CASE201 : Completed (Xconnect)**

* Description: VLAN crossconnect connectivity
* Topology: Single Switch with qinq hosts
* Configuration: openflow-base, etc
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, execute pingall
* Expect: All pings succeed

**CASE301**

* Description: Multicast connectivity
* Topology: Single Switch with multicast src and dst hosts
* Configuration: openflow-base, etc
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, send multicast traffic, expect traffic at end hosts
* Expect: All pings succeed

**CASE302**

* Description: Multicast connectivity on 2x2 fabric
* Topology: 2x2 Leaf-Spine with src and dst hosts
* Configuration: openflow-base, etc
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, send multicast traffic, expect traffic at end hosts
* Expect: All pings succeed

**CASE401**

* Description: VRouter integration
* Topology: Single Switch chained to quagga and host
* Configuration: default
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, ping 8.8.8.8
* Expect: All pings succeed

**CASE402**

* Description: 2x2 Fabric VRouter integration
* Topology: 2x2 Leaf-spine chained to quagga and host
* Configuration: default
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, ping 8.8.8.8,
* Expect: All pings succeed

**CASE405** - Not implemented yet

* Description: Fabric-VRouter integration + quagga link failover
* Topology: Single switch connected to redundant quaggas
* Configuration: default
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, ping 8.8.8.8, shut down a random quagga link , execute pingall
* Expect: All pings succeed

**CASE401**

* Description: Dynamically add a host that doesn't belong to an existing subnet
* Topology: single switch
* Configuration: default
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, execute pingall, add a host via REST interface, execute pingall
* Expect: All pings succeed

**CASE402**

* Description: Dynamically add a host that belongs to an existing subnet
* Topology: single switch
* Configuration: default
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, execute pingall, add a host via REST interface, execute pingall
* Expect: All pings succeed

**CASE503**

* Description: Dynamically add a host that doesn't belong to an existing subnet
* Topology: 2x2 Leaf-spine
* Configuration: default
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, execute pingall, add a host via REST interface, execute pingall
* Expect: All pings succeed

**CASE504**

* Description: Dynamically add a host that belongs to an existing subnet
* Topology: 2x2 Leaf-spine
* Configuration: default
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, execute pingall, add a host via REST interface, execute pingall
* Expect: All pings succeed

**CASE601 : Completed**(SRCLusterSanity)****

* Description: Bring up LS connected to three controllers
* Topology: 2x2 Leaf-spine
* Configuration: default
* Expect flow count
* Do: Start topology, execute pingall
* Expect:Ping successfull

**CASE602: Completed **(SingleInstanceRestart)****

* Description: Bring up LS connected to three controllers
* Topology: 2x2 Leaf-spine
* Configuration: default
* Expect flow count
* Do: Start topology, execute pingall, bring down a controller, pingall
* Expect:Ping successfull

**CASE603: Completed**

* Description: Bring up LS connected to three controllers
* Topology: 2x2 Leaf-spine
* Configuration: default
* Expect flow count
* Do: Start topology, execute pingall, bring down a controller and a node, pingall
* Expect:Ping successfull

**CASE604:**

* Description: Bring up LS connected to three controllers
* Topology: 2x2 Leaf-spine
* Configuration: default
* Expect flow count
* Do: Start topology, execute pingall, bring down a controller, pingall
* Expect:Ping successfull

**CASE605**

* Description: 2x2 Fabric VRouter integration + ONOS failover
* Topology: 2x2 Leaf-spine chained to quagga and host
* Configuration: default
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, ping 8.8.8.8, shut down a random spine link , execute pingall
* Expect: All pings succeed

**CASE606**

* Description: Fabric-VRouter integration + clyuster restart
* Topology: 2x2 Leaf-spine chained to quagga and host
* Configuration: default
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, ping 8.8.8.8, shut down a random spine , execute pingall
* Expect: All pings succeed

**CASE701: Partially completed (LinkDown)**

* Description: Link failover test on 2x2 fabric
* Topology: 2x2 Leaf-Spine Fabric
* Configuration: openflow-base, etc
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, execute pingall, shut down a random spine link , execute pingall
* Expect: All pings succeed
* **Needs inclusion of xconnect**

**CASE702 : Partially completed (NodeDown)**

* Description: Node failover test on 2x2 fabric
* Topology: 2x2 Leaf-Spine Fabric
* Configuration: openflow-base, etc
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, execute pingall, shutdown a random spine, execute pingall, restart spine execute pingall
* Expect: All pings succeed
* **Needs inclusion of xconnect**

**CASE703:**

* Description: Multicast on fabric + Node failover test
* Topology: 2x2 Leaf-Spine with src and dst hosts
* Configuration: openflow-base, etc
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, send multicast traffic, expect traffic at end hosts, shut down a random spine , execute pingall
* Expect: All pings succeed

**CASE704**

* Description: Multicast on fabric + Link failover test
* Topology: 2x2 Leaf-Spine with src and dst hosts
* Configuration: openflow-base, etc
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, send multicast traffic, expect traffic at end hosts, shut down a random spine link , execute pingall
* Expect: All pings succeed

**CASE705**

* Description: 2x2 Fabric VRouter integration + link failover
* Topology: 2x2 Leaf-spine chained to quagga and host
* Configuration: default
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, ping 8.8.8.8, shut down a random spine link , execute pingall
* Expect: All pings succeed

**CASE706**

* Description: Fabric-VRouter integration + node failover
* Topology: 2x2 Leaf-spine chained to quagga and host
* Configuration: default
* Expect: flow count: undetermined group count: undetermined
* Do: Start topology, ping 8.8.8.8, shut down a random spine , execute pingall
* Expect: All pings succeed
