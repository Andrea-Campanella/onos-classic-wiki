# Release Notes - Blackbird 1.1.0

# Blackbird Release

Version: 1.1.0

Release Date: 17th March, 2015

Download [here](../onos/downloads.md)

## Release Content:

ONOS 1.1.0 release is primarily aimed at improving performance & scale characteristics of ONOS, specifically in the following areas:

* intent operation (submit/withdraw) throughput performance and scalability
* flow operation (add/remove) throughput performance and scalability
* topology change (device/port/link) throughput and latency
* intent reactive repair (path re-routing) latency

The [detailed performance results are available](../onos/system-test-plans-and-results/test-results/onos-v1.1-blackbird/1.1-perf-and-scale-out.md) on the Wiki. While the Blackbird release made a number of significant advancements in these areas, there are a number of remaining optimizations to be made that will further improve the performance and scalability aspects of ONOS in subsequent releases.

In addition to performance improvements, Blackbird release also contains a number of robustness and functionality enhancements:

* cleaner intent subsystem API
* revised flow subsystem API with multi-table support
* application subsystem for cluster-wide app deployment and management
* component configuration subsystem for cluster-wide component configuration
* eventually consistent map mechanism with gossip-based anti-entropy
* strongly consistent map mechanism (based on RAFT)
* device driver framework as a foundation for future device & network configuration
* foundations for modular and dynamically extensible GUI
* IPv6 support
* REST API

## Complete Listing of features and bugs resolved

* [[ONOS-253](https://jira.onosproject.org/browse/ONOS-253)] - Test for p2p intent in the same switch ports.
* [[ONOS-443](https://jira.onosproject.org/browse/ONOS-443)] - Null FlowProvider
* [[ONOS-444](https://jira.onosproject.org/browse/ONOS-444)] - Null DeviceProvider
* [[ONOS-490](https://jira.onosproject.org/browse/ONOS-490)] - Pushing optical topology fails in multi-instance scenario
* [[ONOS-492](https://jira.onosproject.org/browse/ONOS-492)] - Fix application in multi-instance environment
* [[ONOS-510](https://jira.onosproject.org/browse/ONOS-510)] - Implement IPv6, ICMP6 and NeighborAdvertisement
* [[ONOS-511](https://jira.onosproject.org/browse/ONOS-511)] - Implement NeighborSolicitation, RouterSolicitation, RouterAdvertisement and Redirect
* [[ONOS-512](https://jira.onosproject.org/browse/ONOS-512)] - Implement IPv6 Extension Headers
* [[ONOS-625](https://jira.onosproject.org/browse/ONOS-625)] - Driver Framework API
* [[ONOS-626](https://jira.onosproject.org/browse/ONOS-626)] - Implement driver management component(s)
* [[ONOS-636](https://jira.onosproject.org/browse/ONOS-636)] - Integrate SDN-IP IPv6 support with the Intent Framework
* [[ONOS-637](https://jira.onosproject.org/browse/ONOS-637)] - Integrate SDN-IP IPv6 support with the HostService
* [[ONOS-638](https://jira.onosproject.org/browse/ONOS-638)] - Update BGP to support IPv6
* [[ONOS-639](https://jira.onosproject.org/browse/ONOS-639)] - Update SDN-IP Router and IntentSynchronizer to support IPv6
* [[ONOS-640](https://jira.onosproject.org/browse/ONOS-640)] - Updated the SDN-IP related CLI commands to support IPv6
* [[ONOS-665](https://jira.onosproject.org/browse/ONOS-665)] - Null PacketProvider
* [[ONOS-707](https://jira.onosproject.org/browse/ONOS-707)] - Investigate bug-609 with tshark logic instead of tcpdump
* [[ONOS-714](https://jira.onosproject.org/browse/ONOS-714)] - complete NB latency test script per test plan
* [[ONOS-717](https://jira.onosproject.org/browse/ONOS-717)] - Complete Automated Test Script for SB Latency Tests
* [[ONOS-724](https://jira.onosproject.org/browse/ONOS-724)] - Run test on Baremetal cluster
* [[ONOS-729](https://jira.onosproject.org/browse/ONOS-729)] - Complete test script for SB TP
* [[ONOS-772](https://jira.onosproject.org/browse/ONOS-772)] - Implement a testcase to cover ONOS-151 bug to verify if ONOS outputs exception on installing one-hop intent
* [[ONOS-775](https://jira.onosproject.org/browse/ONOS-775)] - TopoView - Load background Map on Zoomable SVG
* [[ONOS-783](https://jira.onosproject.org/browse/ONOS-783)] - Update PeerConnectivityManager to handle IPv6
* [[ONOS-793](https://jira.onosproject.org/browse/ONOS-793)] - Get up and running with latest Copycat changes
* [[ONOS-794](https://jira.onosproject.org/browse/ONOS-794)] - Fix NettyTcpProtocol
* [[ONOS-795](https://jira.onosproject.org/browse/ONOS-795)] - Fix quorum calculation + single node cluster set up.
* [[ONOS-797](https://jira.onosproject.org/browse/ONOS-797)] - Implement Map spanning multiple RAFT clusters
* [[ONOS-798](https://jira.onosproject.org/browse/ONOS-798)] - Support a forwarding state machine proxy
* [[ONOS-817](https://jira.onosproject.org/browse/ONOS-817)] - Create scrollable table
* [[ONOS-818](https://jira.onosproject.org/browse/ONOS-818)] - Fix header on table
* [[ONOS-870](https://jira.onosproject.org/browse/ONOS-870)] - Optical device annotations not honored in multi-instance scenario
* [[ONOS-919](https://jira.onosproject.org/browse/ONOS-919)] - Profile and Optimize Single-Node ONOS
* [[ONOS-921](https://jira.onosproject.org/browse/ONOS-921)] - Create onos-maven-plugin
* [[ONOS-933](https://jira.onosproject.org/browse/ONOS-933)] - Use RDS db and google chart API to present SB TP data on wiki
* [[ONOS-935](https://jira.onosproject.org/browse/ONOS-935)] - use RDS db and google chart API to post NB latency data on wiki
* [[ONOS-936](https://jira.onosproject.org/browse/ONOS-936)] - use RDS db and google chart API to post NB TP data on wiki
* [[ONOS-945](https://jira.onosproject.org/browse/ONOS-945)] - Stage our copycat fork on nexus maven repo
* [[ONOS-946](https://jira.onosproject.org/browse/ONOS-946)] - ONOS messaging protocol plugin for Copycat.
* [[ONOS-947](https://jira.onosproject.org/browse/ONOS-947)] - Push all copycat fixes upstream in github
* [[ONOS-948](https://jira.onosproject.org/browse/ONOS-948)] - Update ONOS tablet configuration to support mulitple partitions.
* [[ONOS-949](https://jira.onosproject.org/browse/ONOS-949)] - Create a standalone performance test script that can mesure the througput of our partitioned raft solution.
* [[ONOS-951](https://jira.onosproject.org/browse/ONOS-951)] - Clean up prototype code and integrate with ONOS.
* [[ONOS-965](https://jira.onosproject.org/browse/ONOS-965)] - Choose mechanism to connect to LINC CLI
* [[ONOS-966](https://jira.onosproject.org/browse/ONOS-966)] - Deduce mapping between Mininet and LINC
* [[ONOS-967](https://jira.onosproject.org/browse/ONOS-967)] - Start/stop LINC optical port from Mininet
* [[ONOS-968](https://jira.onosproject.org/browse/ONOS-968)] - Start/stop LINC switch from Mininet
* [[ONOS-1070](https://jira.onosproject.org/browse/ONOS-1070)] - Test SB TP with multi-theaded Null Link Flicker to baseline maximum throughput
* [[ONOS-1071](https://jira.onosproject.org/browse/ONOS-1071)] - create Test Script using flow\_test.py to test Flow performance
* [[ONOS-1072](https://jira.onosproject.org/browse/ONOS-1072)] - create wiki presentation page for logging flow test data
* [[ONOS-1122](https://jira.onosproject.org/browse/ONOS-1122)] - Investigate open source NETCONF implementations
* [[ONOS-1127](https://jira.onosproject.org/browse/ONOS-1127)] - Design extended Provider interfaces for L0
* [[ONOS-1128](https://jira.onosproject.org/browse/ONOS-1128)] - Design ROADM specific interface between Provider and vendor plugin
* [[ONOS-1188](https://jira.onosproject.org/browse/ONOS-1188)] - Update SDN-IP Wiki documentation to include IPv6

## Technical task

* [[ONOS-696](https://jira.onosproject.org/browse/ONOS-696)] - Introduce an hack in ONOS to interpret correctly the VLAN value sent by the FSFW
* [[ONOS-697](https://jira.onosproject.org/browse/ONOS-697)] - We need to express flows using specific port numbers, instead of wildcard them

## Bug

* [[ONOS-261](https://jira.onosproject.org/browse/ONOS-261)] - FlowRule entries are not removed accordingly after P2P Intents are removed
* [[ONOS-329](https://jira.onosproject.org/browse/ONOS-329)] - Ping all from Mininet fails intermittently and ONOS reports device does not exist
* [[ONOS-333](https://jira.onosproject.org/browse/ONOS-333)] - FlowEntryBuilder needs to parse 1.3 set-field actions from OpenFlow
* [[ONOS-384](https://jira.onosproject.org/browse/ONOS-384)] - "push-test-intent" test with 3+ nodes return wide-range latency
* [[ONOS-389](https://jira.onosproject.org/browse/ONOS-389)] - ONOS stop working while stressing with push-test-intent
* [[ONOS-393](https://jira.onosproject.org/browse/ONOS-393)] - NullPointerException when bringing down a link between 2 devices
* [[ONOS-423](https://jira.onosproject.org/browse/ONOS-423)] - LinkResourceStore should store should throw appropriate Exceptions
* [[ONOS-426](https://jira.onosproject.org/browse/ONOS-426)] - Definition of org.onosproject.net.resource.Bandwidth value is unclear
* [[ONOS-432](https://jira.onosproject.org/browse/ONOS-432)] - MessageSubject needs a scheme/naming convention to avoid collisions
* [[ONOS-435](https://jira.onosproject.org/browse/ONOS-435)] - GossipDeviceStore: Timeout during executor shutdown
* [[ONOS-436](https://jira.onosproject.org/browse/ONOS-436)] - Hosts learned via Gossip sometimes are missing ips
* [[ONOS-439](https://jira.onosproject.org/browse/ONOS-439)] - OpticalLinkProvider.processLink throws NPE
* [[ONOS-440](https://jira.onosproject.org/browse/ONOS-440)] - OpticalPathProvisioner NPE
* [[ONOS-447](https://jira.onosproject.org/browse/ONOS-447)] - HostLocationProviderTest.java build error in eclipse
* [[ONOS-468](https://jira.onosproject.org/browse/ONOS-468)] - Failed to respond to peer's getFlowEntries request java.io.IOException: io.netty.util.concurrent.BlockingOperationException: DefaultChannelPromise@26bd6338(incomplete)
* [[ONOS-471](https://jira.onosproject.org/browse/ONOS-471)] - Clean up/refactor IntentManager
* [[ONOS-473](https://jira.onosproject.org/browse/ONOS-473)] - GossipLinkStore {src, dst}Links is not concurrent access safe.
* [[ONOS-474](https://jira.onosproject.org/browse/ONOS-474)] - LinkManager logs "link vanished", even if no links vanished
* [[ONOS-477](https://jira.onosproject.org/browse/ONOS-477)] - NPE when restarting an ONOS node with intents installed
* [[ONOS-478](https://jira.onosproject.org/browse/ONOS-478)] - NPE in Mobility app
* [[ONOS-487](https://jira.onosproject.org/browse/ONOS-487)] - onos-install fails when group name differs from user name
* [[ONOS-537](https://jira.onosproject.org/browse/ONOS-537)] - Requesting output to controller results in receiving PacketIn messages with 0-length packet data
* [[ONOS-541](https://jira.onosproject.org/browse/ONOS-541)] - single-inst ONOS VM stuck at high CPU after connecting to 500 switch topo
* [[ONOS-554](https://jira.onosproject.org/browse/ONOS-554)] - Intents-events-metrics counts do not match even when there are no failed/stuck intents in ONOS
* [[ONOS-566](https://jira.onosproject.org/browse/ONOS-566)] - ONOS "stuck" when "push-test-intent" of 100000 intents
* [[ONOS-577](https://jira.onosproject.org/browse/ONOS-577)] - java.lang.ArrayIndexOutOfBoundsException during Hazelcast event processing
* [[ONOS-581](https://jira.onosproject.org/browse/ONOS-581)] - Chordal ring topology does not converge on ONOS until ONOS restart
* [[ONOS-605](https://jira.onosproject.org/browse/ONOS-605)] - Exceptions thrown while deserializing truncated or malformed packets
* [[ONOS-606](https://jira.onosproject.org/browse/ONOS-606)] - ClassNotFound exception when deploying ONOS with onos-test command
* [[ONOS-609](https://jira.onosproject.org/browse/ONOS-609)] - Moderately large numbers of intents do not generate correct number of FlowMods
* [[ONOS-653](https://jira.onosproject.org/browse/ONOS-653)] - Null Device Provider causes exceptions in multi-node configuration
* [[ONOS-654](https://jira.onosproject.org/browse/ONOS-654)] - onos-install show the cksum error: No such file or directory
* [[ONOS-661](https://jira.onosproject.org/browse/ONOS-661)] - ICMP packets are dropped by deafult from OF 1.3 switches even when reactive forwarding is active
* [[ONOS-666](https://jira.onosproject.org/browse/ONOS-666)] - Heap memory stuck at high usage level after long run of "demo installer"
* [[ONOS-675](https://jira.onosproject.org/browse/ONOS-675)] - deleting a device(switch) with flow rule installed cause intent to stuck at WITHDRAW\_REQ state
* [[ONOS-704](https://jira.onosproject.org/browse/ONOS-704)] - onos-install returns an error when trying to deploy on a remote cell after switching branch
* [[ONOS-705](https://jira.onosproject.org/browse/ONOS-705)] - Exception while running ONOS (master) - against Pica8 switch: java.lang.IllegalArgumentException: Device with ID of:5e3e486e73000187 not found
* [[ONOS-706](https://jira.onosproject.org/browse/ONOS-706)] - Wrong log configuration file in CLI
* [[ONOS-711](https://jira.onosproject.org/browse/ONOS-711)] - Intent Stress test (demo-installer) causes intent install drop after ~3min load
* [[ONOS-712](https://jira.onosproject.org/browse/ONOS-712)] - Using demo Installer, intents cannot be installed on instances that has no mastership of switches
* [[ONOS-722](https://jira.onosproject.org/browse/ONOS-722)] - Proxy ARP sometimes floods packets out the port they came in
* [[ONOS-735](https://jira.onosproject.org/browse/ONOS-735)] - Sometimes, SDN-IP can not start together with ONOS as a feature in cell
* [[ONOS-776](https://jira.onosproject.org/browse/ONOS-776)] - ConfigReader gives errors converting port 46864 to short
* [[ONOS-779](https://jira.onosproject.org/browse/ONOS-779)] - NullPointerException thrown while deserializing malformed BDDP packets
* [[ONOS-787](https://jira.onosproject.org/browse/ONOS-787)] - ONOS sends DELETE flow mods containing actions in OF1.0
* [[ONOS-807](https://jira.onosproject.org/browse/ONOS-807)] - Can't install multi-point to single-point intents on the FSFW
* [[ONOS-808](https://jira.onosproject.org/browse/ONOS-808)] - Fix Bug ONOS-807 - use explicit incoming port matching for Multi-point-to-single point Intents
* [[ONOS-832](https://jira.onosproject.org/browse/ONOS-832)] - Null Devices started on one ONOS node can not be re-assigned mastership to another
* [[ONOS-833](https://jira.onosproject.org/browse/ONOS-833)] - uninstall onos-null feature causes Null devices in unexpected states
* [[ONOS-835](https://jira.onosproject.org/browse/ONOS-835)] - can not install and start two null link provider concurrently on two ONOS nodes
* [[ONOS-836](https://jira.onosproject.org/browse/ONOS-836)] - "flicker" does not run, if reinstall "onos-null" after uninstall
* [[ONOS-864](https://jira.onosproject.org/browse/ONOS-864)] - NPE in Hazelcast during backup
* [[ONOS-868](https://jira.onosproject.org/browse/ONOS-868)] - "NoClassDefFound" exception in onos-intent thread
* [[ONOS-871](https://jira.onosproject.org/browse/ONOS-871)] - When running two simultaneous demo installer on two nodes, one of the nodes get extremely low operation rate
* [[ONOS-886](https://jira.onosproject.org/browse/ONOS-886)] - onos-core-net NPE when running demo installer
* [[ONOS-890](https://jira.onosproject.org/browse/ONOS-890)] - Null Link Provider creates extra links when being run on multiple nodes
* [[ONOS-955](https://jira.onosproject.org/browse/ONOS-955)] - Caught "NoSuchElement" exception while installing large-size intents using "push-test-intents"
* [[ONOS-959](https://jira.onosproject.org/browse/ONOS-959)] - BgpSessionManagerTest unit test failure: BGP route entry lookup
* [[ONOS-974](https://jira.onosproject.org/browse/ONOS-974)] - L2/L3 modification instruction equality is checking for wrong class
* [[ONOS-987](https://jira.onosproject.org/browse/ONOS-987)] - PushHeaderInstructions contains incomplete Ethernet object
* [[ONOS-988](https://jira.onosproject.org/browse/ONOS-988)] - With null link flickering test, scaling onos from 5 to 6(7) nodes causes all nodes thrashing and very low topo performance
* [[ONOS-997](https://jira.onosproject.org/browse/ONOS-997)] - onos:cluster-devices argument "id" is incorrectly optional
* [[ONOS-1009](https://jira.onosproject.org/browse/ONOS-1009)] - ICMPv6 class has bad checksum calculation.
* [[ONOS-1010](https://jira.onosproject.org/browse/ONOS-1010)] - ProxyArpManager class has bug with creating IPv6 ND advertisement
* [[ONOS-1021](https://jira.onosproject.org/browse/ONOS-1021)] - Forwarding IPv6 NDP requests on external ports uses incorrect IPv6 source address
* [[ONOS-1112](https://jira.onosproject.org/browse/ONOS-1112)] - when install with large # of flows (flow-test.py), deleting flows takes long time
* [[ONOS-1113](https://jira.onosproject.org/browse/ONOS-1113)] - No links present on ONOS after bring up of att-topo from Mininet
* [[ONOS-1114](https://jira.onosproject.org/browse/ONOS-1114)] - All ONOS instances crashed after restarting mininet (NPE at WAIT\_SWITCH\_DRIVER\_SUB\_HANDSHAKE)
* [[ONOS-1151](https://jira.onosproject.org/browse/ONOS-1151)] - Filtering options in ONOS CLI shell are not working & causing some test scripts to fail
* [[ONOS-1155](https://jira.onosproject.org/browse/ONOS-1155)] - Topology won't converge in multinode cluster (switches and links)
* [[ONOS-1157](https://jira.onosproject.org/browse/ONOS-1157)] - "memory leak" after flow-tester.py test
* [[ONOS-1161](https://jira.onosproject.org/browse/ONOS-1161)] - Kryo exceptions in EventuallyConsistentMap under load
* [[ONOS-1162](https://jira.onosproject.org/browse/ONOS-1162)] - Hazelcast exceptions under load
* [[ONOS-1163](https://jira.onosproject.org/browse/ONOS-1163)] - Hazelcast Exceptions under load
* [[ONOS-1171](https://jira.onosproject.org/browse/ONOS-1171)] - NPE in GossipDeviceStore when disconnecting switches
* [[ONOS-1173](https://jira.onosproject.org/browse/ONOS-1173)] - exception during flow-tester.py testing flow throughput
* [[ONOS-1185](https://jira.onosproject.org/browse/ONOS-1185)] - flow-tester.py timeout/return "elapse" without error in log
* [[ONOS-1187](https://jira.onosproject.org/browse/ONOS-1187)] - flow-tester.py test results with large variance under light load
* [[ONOS-1189](https://jira.onosproject.org/browse/ONOS-1189)] - If a node has device mastership it will be placed in the standby queue when disconnecting from the cluster
* [[ONOS-1193](https://jira.onosproject.org/browse/ONOS-1193)] - ConcurrentModificationException while processing Device Event
* [[ONOS-1198](https://jira.onosproject.org/browse/ONOS-1198)] - Hazelcast exception: Current thread is not owner of the lock!
* [[ONOS-1208](https://jira.onosproject.org/browse/ONOS-1208)] - Gossip Link Store Exception: Requesting link timestamp without mastership
* [[ONOS-1210](https://jira.onosproject.org/browse/ONOS-1210)] - Instability when using demo installer to test intent installation performance
* [[ONOS-1212](https://jira.onosproject.org/browse/ONOS-1212)] - NPE - when running Intent (demo installer) test
* [[ONOS-1214](https://jira.onosproject.org/browse/ONOS-1214)] - Null provider can not form deterministic topology
* [[ONOS-1222](https://jira.onosproject.org/browse/ONOS-1222)] - ONOS takes over 60sec to load Null provider bundle
* [[ONOS-1286](https://jira.onosproject.org/browse/ONOS-1286)] - Links vanish when devices change mastership
* [[ONOS-1313](https://jira.onosproject.org/browse/ONOS-1313)] - Links are not discovered properly in multi-instance scenarios
* [[ONOS-1315](https://jira.onosproject.org/browse/ONOS-1315)] - IntentPerfInstaller does not read in correct config
* [[ONOS-1317](https://jira.onosproject.org/browse/ONOS-1317)] - Intents pending cli command does not support json output

## Epic

* [[ONOS-578](https://jira.onosproject.org/browse/ONOS-578)] - Improve Southbound Performance
* [[ONOS-643](https://jira.onosproject.org/browse/ONOS-643)] - We need to complete integration tests for SDN-IP

## Improvement

* [[ONOS-419](https://jira.onosproject.org/browse/ONOS-419)] - LinkDiscovery: Suppress discovery on ports which have been configured not to be involved in link discovery
* [[ONOS-434](https://jira.onosproject.org/browse/ONOS-434)] - summary command should print # of active nodes instead of all known nodes
* [[ONOS-461](https://jira.onosproject.org/browse/ONOS-461)] - Maven version mismatch in bash\_profile
* [[ONOS-470](https://jira.onosproject.org/browse/ONOS-470)] - Username is statically configured in onos.conf
* [[ONOS-536](https://jira.onosproject.org/browse/ONOS-536)] - `onos-group` for batching commands to all controllers in a cell
* [[ONOS-607](https://jira.onosproject.org/browse/ONOS-607)] - controller port visualized uncorrectly into ONOS CLI
* [[ONOS-852](https://jira.onosproject.org/browse/ONOS-852)] - Intent install concurrency
* [[ONOS-975](https://jira.onosproject.org/browse/ONOS-975)] - equality check for type() in some of Instruction classes are redundant.
* [[ONOS-1003](https://jira.onosproject.org/browse/ONOS-1003)] - Add an option to flows command to print flows added per device

## New Feature

* [[ONOS-451](https://jira.onosproject.org/browse/ONOS-451)] - Augment Glyph library to be extensible
* [[ONOS-506](https://jira.onosproject.org/browse/ONOS-506)] - Handle IPv6 Neighbor Solicitation in ReactiveForwarding
* [[ONOS-507](https://jira.onosproject.org/browse/ONOS-507)] - Trace Neighbor Solicitation/Advertisement and IPv6 Data Packets in HostLocationProvider
* [[ONOS-508](https://jira.onosproject.org/browse/ONOS-508)] - Implement IPv6 related classes in org.onlab.packet
* [[ONOS-535](https://jira.onosproject.org/browse/ONOS-535)] - Show through the CLI the IP of the switches connecting to ONOS
* [[ONOS-539](https://jira.onosproject.org/browse/ONOS-539)] - See port names
* [[ONOS-540](https://jira.onosproject.org/browse/ONOS-540)] - Create a module to install default flows upon switches connection
* [[ONOS-624](https://jira.onosproject.org/browse/ONOS-624)] - Distributed Application Management Framework

## Story

* [[ONOS-9](https://jira.onosproject.org/browse/ONOS-9)] - Define, Document and Automate HA test cases
* [[ONOS-11](https://jira.onosproject.org/browse/ONOS-11)] - Document and Automate OF1.0/1.3 Functionality Tests (Single & Multi Instance)
* [[ONOS-24](https://jira.onosproject.org/browse/ONOS-24)] - BW Calendaring App - Adding latency constaint
* [[ONOS-80](https://jira.onosproject.org/browse/ONOS-80)] - Support sharding (partitioning) for DatabaseManager
* [[ONOS-101](https://jira.onosproject.org/browse/ONOS-101)] - Extensible navigation & view framework
* [[ONOS-214](https://jira.onosproject.org/browse/ONOS-214)] - How to: contribute to testing
* [[ONOS-278](https://jira.onosproject.org/browse/ONOS-278)] - Show ports on links
* [[ONOS-279](https://jira.onosproject.org/browse/ONOS-279)] - Clean up GUI Technical Debt
* [[ONOS-422](https://jira.onosproject.org/browse/ONOS-422)] - Support IPv6 in SDN-IP
* [[ONOS-442](https://jira.onosproject.org/browse/ONOS-442)] - Null Providers
* [[ONOS-450](https://jira.onosproject.org/browse/ONOS-450)] - Implement Dark theme.
* [[ONOS-456](https://jira.onosproject.org/browse/ONOS-456)] - UI Framework: migrate to AngularJS
* [[ONOS-481](https://jira.onosproject.org/browse/ONOS-481)] - Revisit FlowRule equals design
* [[ONOS-483](https://jira.onosproject.org/browse/ONOS-483)] - SDN-IP: support for 4-byte AS in BGP
* [[ONOS-491](https://jira.onosproject.org/browse/ONOS-491)] - Start/stop LINC network elements from Mininet
* [[ONOS-494](https://jira.onosproject.org/browse/ONOS-494)] - Deploy ONOS and SDN-IP on the local Internet2 testlab network
* [[ONOS-495](https://jira.onosproject.org/browse/ONOS-495)] - Deploy ONOS 1.0.0 and SDN-IP on AL2S network
* [[ONOS-509](https://jira.onosproject.org/browse/ONOS-509)] - Extend Selector and Treatment for IPv6-related Criteria
* [[ONOS-542](https://jira.onosproject.org/browse/ONOS-542)] - ONOS Application as a distributed construct & deployable entity
* [[ONOS-561](https://jira.onosproject.org/browse/ONOS-561)] - TestON Framework and Process Improvements
* [[ONOS-562](https://jira.onosproject.org/browse/ONOS-562)] - HA Assessment and Test Enhancements
* [[ONOS-563](https://jira.onosproject.org/browse/ONOS-563)] - Update CHO Test Plan on wiki with new Test cases
* [[ONOS-564](https://jira.onosproject.org/browse/ONOS-564)] - Feature Test Enhancements
* [[ONOS-567](https://jira.onosproject.org/browse/ONOS-567)] - Add a monitoring mechanism based on MadDash to the testlab deployment
* [[ONOS-584](https://jira.onosproject.org/browse/ONOS-584)] - Finalized Network + Intent Performance Testing Methods and Metrics
* [[ONOS-589](https://jira.onosproject.org/browse/ONOS-589)] - TestON Test Script preparation for Network TP Testing
* [[ONOS-593](https://jira.onosproject.org/browse/ONOS-593)] - TestON Script Preparation for Intent TP Tests
* [[ONOS-608](https://jira.onosproject.org/browse/ONOS-608)] - Test Coverage of Release 1.0.1 bug fixes
* [[ONOS-616](https://jira.onosproject.org/browse/ONOS-616)] - FlowRuleService API enhancements
* [[ONOS-617](https://jira.onosproject.org/browse/ONOS-617)] - FlowRuleManager refactoring
* [[ONOS-618](https://jira.onosproject.org/browse/ONOS-618)] - IntentService API enhancements
* [[ONOS-619](https://jira.onosproject.org/browse/ONOS-619)] - IntentStore refactoring
* [[ONOS-621](https://jira.onosproject.org/browse/ONOS-621)] - TopologyManager refactoring
* [[ONOS-622](https://jira.onosproject.org/browse/ONOS-622)] - Integration - Multi-ring RAFT store implementation
* [[ONOS-623](https://jira.onosproject.org/browse/ONOS-623)] - Device Driver Framework
* [[ONOS-629](https://jira.onosproject.org/browse/ONOS-629)] - Server-side processing of index.html
* [[ONOS-630](https://jira.onosproject.org/browse/ONOS-630)] - Understand the behavior of SDN in case of network reset/re-configuration
* [[ONOS-632](https://jira.onosproject.org/browse/ONOS-632)] - Intent dependency tracking
* [[ONOS-635](https://jira.onosproject.org/browse/ONOS-635)] - Add IPv6 support to HostMonitor
* [[ONOS-650](https://jira.onosproject.org/browse/ONOS-650)] - Intent-based Performance Test-Profile-Optimization Iterations
* [[ONOS-658](https://jira.onosproject.org/browse/ONOS-658)] - Create Production testbed for HA and Functional testing
* [[ONOS-678](https://jira.onosproject.org/browse/ONOS-678)] - Develop Intent Latency Test Script
* [[ONOS-693](https://jira.onosproject.org/browse/ONOS-693)] - SDN-IP tutorial script for IPv6
* [[ONOS-698](https://jira.onosproject.org/browse/ONOS-698)] - Write a technical document to describe SDN-IP and ONOS behavior - version 1
* [[ONOS-713](https://jira.onosproject.org/browse/ONOS-713)] - Build a 7-node baremetal server cluster for Perf/Scale tests
* [[ONOS-716](https://jira.onosproject.org/browse/ONOS-716)] - Develop SB Latency Test Script
* [[ONOS-719](https://jira.onosproject.org/browse/ONOS-719)] - Develop SB TP Test Script
* [[ONOS-720](https://jira.onosproject.org/browse/ONOS-720)] - Develop Intent TP Test Script
* [[ONOS-739](https://jira.onosproject.org/browse/ONOS-739)] - SB Performance Test-Profile-Optimization-Retest Optimization
* [[ONOS-740](https://jira.onosproject.org/browse/ONOS-740)] - Distributed Intent processing leveraging new Intent Store
* [[ONOS-742](https://jira.onosproject.org/browse/ONOS-742)] - Multi-ring RAFT store prototype
* [[ONOS-746](https://jira.onosproject.org/browse/ONOS-746)] - Improve intent stability for long-running test
* [[ONOS-747](https://jira.onosproject.org/browse/ONOS-747)] - Repicate and understand ONOS bug ONOS-712
* [[ONOS-748](https://jira.onosproject.org/browse/ONOS-748)] - Fix ONOS-735. Replicate the problem and put the correct dependencies between the modules involved in ONOS-735
* [[ONOS-757](https://jira.onosproject.org/browse/ONOS-757)] - Start re-implementing modular Topology View
* [[ONOS-758](https://jira.onosproject.org/browse/ONOS-758)] - FlashService implementation
* [[ONOS-759](https://jira.onosproject.org/browse/ONOS-759)] - PanelService implementation
* [[ONOS-760](https://jira.onosproject.org/browse/ONOS-760)] - QuickHelpService implementation
* [[ONOS-761](https://jira.onosproject.org/browse/ONOS-761)] - VeilService implementation
* [[ONOS-762](https://jira.onosproject.org/browse/ONOS-762)] - WebSocketService implementation
* [[ONOS-764](https://jira.onosproject.org/browse/ONOS-764)] - Basic DeviceListView implementation
* [[ONOS-769](https://jira.onosproject.org/browse/ONOS-769)] - Complete re-implementation of modular Topology View
* [[ONOS-841](https://jira.onosproject.org/browse/ONOS-841)] - ONOS Thread names
* [[ONOS-855](https://jira.onosproject.org/browse/ONOS-855)] - Improve SB Perf Data Presentation and Logging
* [[ONOS-856](https://jira.onosproject.org/browse/ONOS-856)] - Improve NB+Core Performance Data Presentation and Logging
* [[ONOS-874](https://jira.onosproject.org/browse/ONOS-874)] - Intent subsystem refactoring
* [[ONOS-893](https://jira.onosproject.org/browse/ONOS-893)] - New CHO test scripts to run on 3 different topologies (ATT, Chordal, Spine)
* [[ONOS-907](https://jira.onosproject.org/browse/ONOS-907)] - Add separate jenkins job for running CHO on maintenance branch
* [[ONOS-909](https://jira.onosproject.org/browse/ONOS-909)] - Update and clean up TestON Github Main page and other links
* [[ONOS-910](https://jira.onosproject.org/browse/ONOS-910)] - Write up a beginners tutorial on TestON and publish to onosproject wiki
* [[ONOS-924](https://jira.onosproject.org/browse/ONOS-924)] - Add support for IPv6 Neighbor Discovery Proxy
* [[ONOS-925](https://jira.onosproject.org/browse/ONOS-925)] - Develop Flow Rule Performance Test
* [[ONOS-927](https://jira.onosproject.org/browse/ONOS-927)] - Delete FlowRules from disconnect devices
* [[ONOS-943](https://jira.onosproject.org/browse/ONOS-943)] - Metrics for FlowService
* [[ONOS-957](https://jira.onosproject.org/browse/ONOS-957)] - Add basic onos-app-ifwd test to be verified on all 3 CHO topologies
* [[ONOS-979](https://jira.onosproject.org/browse/ONOS-979)] - Demonstrate scale-out for IP/optical app
* [[ONOS-1005](https://jira.onosproject.org/browse/ONOS-1005)] - Investigate if python threading could be used in test cases to call ONOS driver functions
* [[ONOS-1014](https://jira.onosproject.org/browse/ONOS-1014)] - Modify current Jenkins results script for CHO to include new topology tests
* [[ONOS-1033](https://jira.onosproject.org/browse/ONOS-1033)] - Restructure NullLinkProvider.
* [[ONOS-1054](https://jira.onosproject.org/browse/ONOS-1054)] - IntentStore cleanup for Performance
* [[ONOS-1058](https://jira.onosproject.org/browse/ONOS-1058)] - Intent CLI Command cleanup
* [[ONOS-1067](https://jira.onosproject.org/browse/ONOS-1067)] - SB Performance Test-Profile-Optimization-Retest Optimization
* [[ONOS-1074](https://jira.onosproject.org/browse/ONOS-1074)] - CLI for querying DatabaseManager's state (partition members, leaders, etc)
* [[ONOS-1077](https://jira.onosproject.org/browse/ONOS-1077)] - Develop Intent TP Test Script: Part 2
* [[ONOS-1078](https://jira.onosproject.org/browse/ONOS-1078)] - Propose vendor-neutral ROADM model
* [[ONOS-1118](https://jira.onosproject.org/browse/ONOS-1118)] - Button Factory
* [[ONOS-1119](https://jira.onosproject.org/browse/ONOS-1119)] - Toolbar Service
* [[ONOS-1120](https://jira.onosproject.org/browse/ONOS-1120)] - Toolbar API
* [[ONOS-1145](https://jira.onosproject.org/browse/ONOS-1145)] - Centralized component configuration
* [[ONOS-1180](https://jira.onosproject.org/browse/ONOS-1180)] - MultiThreaded HA Tests
* [[ONOS-1306](https://jira.onosproject.org/browse/ONOS-1306)] - Update the topology CLI driver function in TestON to work with new o/p format

## Task

* [[ONOS-183](https://jira.onosproject.org/browse/ONOS-183)] - Save and load hazelcast.xml from TestON dependencies folder to avoid overwrite
* [[ONOS-368](https://jira.onosproject.org/browse/ONOS-368)] - Sporadic MasterShipStore unittest failure
* [[ONOS-588](https://jira.onosproject.org/browse/ONOS-588)] - Document Final Test Plan on Wiki
* [[ONOS-773](https://jira.onosproject.org/browse/ONOS-773)] - Implement a testcase for ONOS-260 bug to verify :Ping cannot go through when both P2P and H2H intent configured
* [[ONOS-869](https://jira.onosproject.org/browse/ONOS-869)] - ONOS core extended flow rule and store for installing service data to network elements
