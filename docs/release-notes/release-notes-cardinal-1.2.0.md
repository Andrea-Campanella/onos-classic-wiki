# Release Notes - Cardinal 1.2.0

# Cardinal Release

Version: 1.2.0

Release Date: 5th June, 2015

Download [here](../onos/downloads.md)

## Code Audit Results (Black Duck)

Below are the compatibility reports (pdf) powered by [Black Duck Software](http://www.blackducksoftware.com/).

 Note: The JAX-RS implementation is from Sun. It is on our class-path but we do not distribute it.

* [Summary Report](../assets/scan-cardinal-summary.pdf)
* [BOM Report](../assets/scan-cardinal-bom.pdf)
* [Legal Report](../assets/scan-cardinal-legal.pdf)
* [All reports](../assets/scan-cardinal-combined.pdf) in one PDF file

## Sub-task

* [[ONOS-268](https://jira.onosproject.org/browse/ONOS-268)] - Implement slide-out toolbar (framework)
* [[ONOS-269](https://jira.onosproject.org/browse/ONOS-269)] - Provide tool registration (icon/tooltip/callback)
* [[ONOS-270](https://jira.onosproject.org/browse/ONOS-270)] - Implement tools for topology view
* [[ONOS-271](https://jira.onosproject.org/browse/ONOS-271)] - Make Links selectable
* [[ONOS-272](https://jira.onosproject.org/browse/ONOS-272)] - Add requestLinkDetails event
* [[ONOS-486](https://jira.onosproject.org/browse/ONOS-486)] - Design and implement a framework for measuring SDN-IP performance
* [[ONOS-576](https://jira.onosproject.org/browse/ONOS-576)] - Assess and publish HA assessment
* [[ONOS-821](https://jira.onosproject.org/browse/ONOS-821)] - Add a new interfance for FlowRuleService
* [[ONOS-823](https://jira.onosproject.org/browse/ONOS-823)] - Implement FlowModBuilderTTP
* [[ONOS-824](https://jira.onosproject.org/browse/ONOS-824)] - Modify the OFSwitchImplOVS10/13
* [[ONOS-894](https://jira.onosproject.org/browse/ONOS-894)] - Implement OFGroupProvider
* [[ONOS-895](https://jira.onosproject.org/browse/ONOS-895)] - Implement GroupManager
* [[ONOS-896](https://jira.onosproject.org/browse/ONOS-896)] - Implement distributed GroupStore
* [[ONOS-928](https://jira.onosproject.org/browse/ONOS-928)] - Implement distributed GroupStore
* [[ONOS-950](https://jira.onosproject.org/browse/ONOS-950)] - Support cross partition transactional updates.
* [[ONOS-969](https://jira.onosproject.org/browse/ONOS-969)] - Extend LINC logic to create new optical port
* [[ONOS-970](https://jira.onosproject.org/browse/ONOS-970)] - Design API for add port in LINC
* [[ONOS-971](https://jira.onosproject.org/browse/ONOS-971)] - Extend LINC CLI with add optical port
* [[ONOS-972](https://jira.onosproject.org/browse/ONOS-972)] - Implement add optical port in Mininet
* [[ONOS-973](https://jira.onosproject.org/browse/ONOS-973)] - Create a UnitTest codes
* [[ONOS-977](https://jira.onosproject.org/browse/ONOS-977)] - Update the actions in TrafficTreatment
* [[ONOS-1053](https://jira.onosproject.org/browse/ONOS-1053)] - Fix Intent REST API and Test
* [[ONOS-1059](https://jira.onosproject.org/browse/ONOS-1059)] - Take a pass on comment/code cleanup
* [[ONOS-1061](https://jira.onosproject.org/browse/ONOS-1061)] - Improve unit test coverage
* [[ONOS-1062](https://jira.onosproject.org/browse/ONOS-1062)] - Harden/Verify "error" code paths
* [[ONOS-1080](https://jira.onosproject.org/browse/ONOS-1080)] - DeviceProvider RPC
* [[ONOS-1082](https://jira.onosproject.org/browse/ONOS-1082)] - Connect to ROADM and add device to core
* [[ONOS-1083](https://jira.onosproject.org/browse/ONOS-1083)] - Connect to ROADM and add device to core
* [[ONOS-1088](https://jira.onosproject.org/browse/ONOS-1088)] - Device vendor annotations & provider selection
* [[ONOS-1098](https://jira.onosproject.org/browse/ONOS-1098)] - Mechanism to point to YANG model
* [[ONOS-1099](https://jira.onosproject.org/browse/ONOS-1099)] - Write or reuse library to parse YANG models
* [[ONOS-1100](https://jira.onosproject.org/browse/ONOS-1100)] - Test YANG parser with ACL model
* [[ONOS-1110](https://jira.onosproject.org/browse/ONOS-1110)] - Verify the feasibility with Internet2
* [[ONOS-1128](https://jira.onosproject.org/browse/ONOS-1128)] - Pull port stats from ROADM and add to core
* [[ONOS-1175](https://jira.onosproject.org/browse/ONOS-1175)] - Downlaod ONOS VM and understand how it works
* [[ONOS-1176](https://jira.onosproject.org/browse/ONOS-1176)] - Download Jono script for mininet from SDN-IP repository and understand how it works
* [[ONOS-1177](https://jira.onosproject.org/browse/ONOS-1177)] - Create a new VM and integrate dockers according to what has been learnt from the downloaded VM
* [[ONOS-1178](https://jira.onosproject.org/browse/ONOS-1178)] - Integrate the Jono script to the newly created VM
* [[ONOS-1236](https://jira.onosproject.org/browse/ONOS-1236)] - Server-side handler registration mechanism
* [[ONOS-1237](https://jira.onosproject.org/browse/ONOS-1237)] - Client-side handler registration mechanism
* [[ONOS-1238](https://jira.onosproject.org/browse/ONOS-1238)] - Implement core handlers for exchange of node information
* [[ONOS-1239](https://jira.onosproject.org/browse/ONOS-1239)] - Implement client-side error handler to fail-over to another node
* [[ONOS-1240](https://jira.onosproject.org/browse/ONOS-1240)] - Implement topology view server-side handler registration
* [[ONOS-1241](https://jira.onosproject.org/browse/ONOS-1241)] - Implement topology view client-side handler registration
* [[ONOS-1268](https://jira.onosproject.org/browse/ONOS-1268)] - Expose IPv6 support at the ONOS CLI level
* [[ONOS-1269](https://jira.onosproject.org/browse/ONOS-1269)] - Expose IPv6 support at the ONOS REST level
* [[ONOS-1303](https://jira.onosproject.org/browse/ONOS-1303)] - Modify existing ONOS code to switch over to the new shared facility as appropriate
* [[ONOS-1330](https://jira.onosproject.org/browse/ONOS-1330)] - Modify multi to single point intent driver function to accept multiple ingress devices instead of just two
* [[ONOS-1345](https://jira.onosproject.org/browse/ONOS-1345)] - Design a new topology (or SB) event test
* [[ONOS-1346](https://jira.onosproject.org/browse/ONOS-1346)] - Test for intent re-route latency
* [[ONOS-1348](https://jira.onosproject.org/browse/ONOS-1348)] - refactor all perf test scripts to adopt new application activation method
* [[ONOS-1349](https://jira.onosproject.org/browse/ONOS-1349)] - refactor switch/link latency test for CI
* [[ONOS-1350](https://jira.onosproject.org/browse/ONOS-1350)] - refactor flow subsystem TP test for CI
* [[ONOS-1351](https://jira.onosproject.org/browse/ONOS-1351)] - refactor Intent TP test for CI
* [[ONOS-1352](https://jira.onosproject.org/browse/ONOS-1352)] - refactor Intent Latency test for CI
* [[ONOS-1353](https://jira.onosproject.org/browse/ONOS-1353)] - Resolve Perf test result discrepancies
* [[ONOS-1361](https://jira.onosproject.org/browse/ONOS-1361)] - document for wiki
* [[ONOS-1362](https://jira.onosproject.org/browse/ONOS-1362)] - Support AsyncConsistentMap for async interaction with Consistent data store
* [[ONOS-1367](https://jira.onosproject.org/browse/ONOS-1367)] - Extend LeadershipService with Administrative interface
* [[ONOS-1368](https://jira.onosproject.org/browse/ONOS-1368)] - Get app status driver function
* [[ONOS-1369](https://jira.onosproject.org/browse/ONOS-1369)] - driver function around onos:apps
* [[ONOS-1370](https://jira.onosproject.org/browse/ONOS-1370)] - driver function around onos:app
* [[ONOS-1371](https://jira.onosproject.org/browse/ONOS-1371)] - driver function to activate an ONOS app
* [[ONOS-1372](https://jira.onosproject.org/browse/ONOS-1372)] - driver function to deactivate an ONOS app
* [[ONOS-1373](https://jira.onosproject.org/browse/ONOS-1373)] - driver function to uninstall an ONOS app
* [[ONOS-1375](https://jira.onosproject.org/browse/ONOS-1375)] - modify create cell driver function to use the new onos app subsystem
* [[ONOS-1394](https://jira.onosproject.org/browse/ONOS-1394)] - Add number of iterations and last modified to IntentData
* [[ONOS-1395](https://jira.onosproject.org/browse/ONOS-1395)] - Recompile/install intents that fail in IntentManager
* [[ONOS-1398](https://jira.onosproject.org/browse/ONOS-1398)] - Add CORRUPT state
* [[ONOS-1402](https://jira.onosproject.org/browse/ONOS-1402)] - Substitute Docker with LXC
* [[ONOS-1405](https://jira.onosproject.org/browse/ONOS-1405)] - Implement persistent store using MapDB
* [[ONOS-1406](https://jira.onosproject.org/browse/ONOS-1406)] - Measure performance of persistence vs no persistence
* [[ONOS-1417](https://jira.onosproject.org/browse/ONOS-1417)] - Driver function to check unique app ids
* [[ONOS-1420](https://jira.onosproject.org/browse/ONOS-1420)] - TestON Drivers: Include support for a list of apps
* [[ONOS-1426](https://jira.onosproject.org/browse/ONOS-1426)] - Configuration subsystem
* [[ONOS-1427](https://jira.onosproject.org/browse/ONOS-1427)] - Application subsystem
* [[ONOS-1428](https://jira.onosproject.org/browse/ONOS-1428)] - Core distribution mechanisms
* [[ONOS-1446](https://jira.onosproject.org/browse/ONOS-1446)] - Site selection
* [[ONOS-1448](https://jira.onosproject.org/browse/ONOS-1448)] - ONOS cluster installation
* [[ONOS-1461](https://jira.onosproject.org/browse/ONOS-1461)] - Create process/object for dealing with CORRUPT
* [[ONOS-1462](https://jira.onosproject.org/browse/ONOS-1462)] - recompute intents from the pending map if they are stuck there
* [[ONOS-1486](https://jira.onosproject.org/browse/ONOS-1486)] - OpenWRT as a residential gateway
* [[ONOS-1487](https://jira.onosproject.org/browse/ONOS-1487)] - ONT + PMC Sierra
* [[ONOS-1489](https://jira.onosproject.org/browse/ONOS-1489)] - Order server
* [[ONOS-1498](https://jira.onosproject.org/browse/ONOS-1498)] - Implement TestON driver function for adding MPLS intent
* [[ONOS-1512](https://jira.onosproject.org/browse/ONOS-1512)] - Pull port stats from ROADM and add to core
* [[ONOS-1532](https://jira.onosproject.org/browse/ONOS-1532)] - Obtain Spirent traffic generators
* [[ONOS-1574](https://jira.onosproject.org/browse/ONOS-1574)] - Add status verification to point to point intent
* [[ONOS-1575](https://jira.onosproject.org/browse/ONOS-1575)] - Add status verification to multi-to-single point intent
* [[ONOS-1576](https://jira.onosproject.org/browse/ONOS-1576)] - Add status verification to single to multi point intents
* [[ONOS-1578](https://jira.onosproject.org/browse/ONOS-1578)] - Update ProdFunc test to use the new ONOS App subsystem
* [[ONOS-1579](https://jira.onosproject.org/browse/ONOS-1579)] - Update MultiProd test to use the new ONOS App subsystem
* [[ONOS-1581](https://jira.onosproject.org/browse/ONOS-1581)] - Add single to multi point intents to Att topology
* [[ONOS-1582](https://jira.onosproject.org/browse/ONOS-1582)] - Add single to multi point intent to Chordal topology
* [[ONOS-1583](https://jira.onosproject.org/browse/ONOS-1583)] - Add single to multi point intent to Spine topology
* [[ONOS-1613](https://jira.onosproject.org/browse/ONOS-1613)] - Investigate how to create vlans with mininet
* [[ONOS-1626](https://jira.onosproject.org/browse/ONOS-1626)] - Implement DNS packet in packet library
* [[ONOS-1640](https://jira.onosproject.org/browse/ONOS-1640)] - Test Application for Atomic Counters
* [[ONOS-1641](https://jira.onosproject.org/browse/ONOS-1641)] - Test Application for Distributed Set
* [[ONOS-1651](https://jira.onosproject.org/browse/ONOS-1651)] - reactive routing design and implementation
* [[ONOS-1652](https://jira.onosproject.org/browse/ONOS-1652)] - Reset the existing OF office access point and install the latest stable OpenWRT fimware (14.07))
* [[ONOS-1658](https://jira.onosproject.org/browse/ONOS-1658)] - The HA design and discussion
* [[ONOS-1659](https://jira.onosproject.org/browse/ONOS-1659)] - HA implementation
* [[ONOS-1660](https://jira.onosproject.org/browse/ONOS-1660)] - virtual gateway design and discussion
* [[ONOS-1661](https://jira.onosproject.org/browse/ONOS-1661)] - virtual gateway implementation
* [[ONOS-1670](https://jira.onosproject.org/browse/ONOS-1670)] - write wiki document for virtual gateway
* [[ONOS-1675](https://jira.onosproject.org/browse/ONOS-1675)] - Add OMS, OCH and ODUCLT port classes and attributes
* [[ONOS-1686](https://jira.onosproject.org/browse/ONOS-1686)] - Implement single to multipoint intent test script in Functionality test
* [[ONOS-1688](https://jira.onosproject.org/browse/ONOS-1688)] - Brainstorm and finalize on new functionality topology
* [[ONOS-1689](https://jira.onosproject.org/browse/ONOS-1689)] - Segregate all test cases/scripts and group them to cover each functionality/feature
* [[ONOS-1691](https://jira.onosproject.org/browse/ONOS-1691)] - Add glyph to the device details panel (topo view)
* [[ONOS-1692](https://jira.onosproject.org/browse/ONOS-1692)] - Add glyph to the device details panel (device table view)
* [[ONOS-1693](https://jira.onosproject.org/browse/ONOS-1693)] - Create the flow table view on the client-side
* [[ONOS-1694](https://jira.onosproject.org/browse/ONOS-1694)] - Generate tabular flow data on the server side
* [[ONOS-1702](https://jira.onosproject.org/browse/ONOS-1702)] - Provision 2 new NETGEAR routers as RGs
* [[ONOS-1712](https://jira.onosproject.org/browse/ONOS-1712)] - Implement cross-connect operation using FlowRule API
* [[ONOS-1713](https://jira.onosproject.org/browse/ONOS-1713)] - Implement cross-connect operation using FlowRule API
* [[ONOS-1730](https://jira.onosproject.org/browse/ONOS-1730)] - Create Mininet config file for new topology
* [[ONOS-1737](https://jira.onosproject.org/browse/ONOS-1737)] - Create a new Jenkins Job Specific for Optical Test
* [[ONOS-1744](https://jira.onosproject.org/browse/ONOS-1744)] - Simplify test results pages on wiki
* [[ONOS-1754](https://jira.onosproject.org/browse/ONOS-1754)] - Install Dell R410 servers as compute nodes
* [[ONOS-1769](https://jira.onosproject.org/browse/ONOS-1769)] - Define a class representing frequency
* [[ONOS-1771](https://jira.onosproject.org/browse/ONOS-1771)] - Create HA Test cases for sets and counters
* [[ONOS-1823](https://jira.onosproject.org/browse/ONOS-1823)] - Basic Multi-instance validation on Dell switches without triggering any control plane failures
* [[ONOS-1825](https://jira.onosproject.org/browse/ONOS-1825)] - Multi-instance test validations on Dell
* [[ONOS-1832](https://jira.onosproject.org/browse/ONOS-1832)] - Verify TestON single-instance test2 is passing with ONOS-1786 changes
* [[ONOS-1833](https://jira.onosproject.org/browse/ONOS-1833)] - Enabling other TestON single-instance tests with different topologies with changes from ONOS-1786 and ONOS-1791
* [[ONOS-1838](https://jira.onosproject.org/browse/ONOS-1838)] - State replication of neighbor-set to next objective in SR group handler to handle multi-instance scenarios
* [[ONOS-1840](https://jira.onosproject.org/browse/ONOS-1840)] - Reorganize functionality tests into new format
* [[ONOS-1869](https://jira.onosproject.org/browse/ONOS-1869)] - Provide CLI support on tunnel subsystem for QA purposes
* [[ONOS-1870](https://jira.onosproject.org/browse/ONOS-1870)] - Provide CLI support on Label subsystem for QA purposes
* [[ONOS-1871](https://jira.onosproject.org/browse/ONOS-1871)] - Provide CLI support on flowrule subsystem extension for QA purposes
* [[ONOS-1873](https://jira.onosproject.org/browse/ONOS-1873)] - Implement Instructions for Packet + Optical
* [[ONOS-1875](https://jira.onosproject.org/browse/ONOS-1875)] - Support new Instructions in InstructionCodec
* [[ONOS-1876](https://jira.onosproject.org/browse/ONOS-1876)] - Add unit tests for ModL0OchSignal
* [[ONOS-1884](https://jira.onosproject.org/browse/ONOS-1884)] - Add REST API
* [[ONOS-1886](https://jira.onosproject.org/browse/ONOS-1886)] - Move wpa\_supplicant to OVS internal interface
* [[ONOS-1942](https://jira.onosproject.org/browse/ONOS-1942)] - HA test on Cardinal RC
* [[ONOS-1953](https://jira.onosproject.org/browse/ONOS-1953)] - Cable up switches and servers
* [[ONOS-1961](https://jira.onosproject.org/browse/ONOS-1961)] - Application Subsystem documentation
* [[ONOS-1964](https://jira.onosproject.org/browse/ONOS-1964)] - Incubator region documentation
* [[ONOS-1971](https://jira.onosproject.org/browse/ONOS-1971)] - Host intents Test
* [[ONOS-1972](https://jira.onosproject.org/browse/ONOS-1972)] - Point Intent Test
* [[ONOS-1973](https://jira.onosproject.org/browse/ONOS-1973)] - Single Point to Multi Point intents
* [[ONOS-1974](https://jira.onosproject.org/browse/ONOS-1974)] - Muti Point to Single Point intents
* [[ONOS-1975](https://jira.onosproject.org/browse/ONOS-1975)] - Update wiki on HA Test plan & results
* [[ONOS-1984](https://jira.onosproject.org/browse/ONOS-1984)] - Add VLAN host intent
* [[ONOS-1985](https://jira.onosproject.org/browse/ONOS-1985)] - Add VLAN point intent
* [[ONOS-2028](https://jira.onosproject.org/browse/ONOS-2028)] - Component Subsystem REST API documentation
* [[ONOS-2039](https://jira.onosproject.org/browse/ONOS-2039)] - Add VLAN point to multi point intent
* [[ONOS-2040](https://jira.onosproject.org/browse/ONOS-2040)] - Add VLAN multi point to point intent
* [[ONOS-2072](https://jira.onosproject.org/browse/ONOS-2072)] - Add option in startNet function in mininet driver to start mininet using sudo mn

## Bug

* [[ONOS-179](https://jira.onosproject.org/browse/ONOS-179)] - Channel in AbstractOpenFlowSwitch should be private
* [[ONOS-180](https://jira.onosproject.org/browse/ONOS-180)] - Make sure shutdown behaviour is clean
* [[ONOS-260](https://jira.onosproject.org/browse/ONOS-260)] - Ping cannot go through when both P2P and H2H intent configured
* [[ONOS-262](https://jira.onosproject.org/browse/ONOS-262)] - Intent stays in INSTALLING state after it is added back from removed list
* [[ONOS-376](https://jira.onosproject.org/browse/ONOS-376)] - Can't handle intents causing exception/error properly
* [[ONOS-428](https://jira.onosproject.org/browse/ONOS-428)] - Implement DistributedLockManager's listener management
* [[ONOS-437](https://jira.onosproject.org/browse/ONOS-437)] - Host intents have no flows after some ONOS nodes restart
* [[ONOS-458](https://jira.onosproject.org/browse/ONOS-458)] - Topology View: host link labels still visible when hosts are hidden
* [[ONOS-459](https://jira.onosproject.org/browse/ONOS-459)] - Topology View: orphaned link labels
* [[ONOS-709](https://jira.onosproject.org/browse/ONOS-709)] - After killing one of the node of ONOS cluster, the node didn't disappear.
* [[ONOS-838](https://jira.onosproject.org/browse/ONOS-838)] - Foo app's pom.xml specifies old version as parent pom
* [[ONOS-905](https://jira.onosproject.org/browse/ONOS-905)] - Intent disappears after 3 of 7 ONOS nodes restart
* [[ONOS-960](https://jira.onosproject.org/browse/ONOS-960)] - Signed/unsigned value mismatch for OpenFlow-related match/action conditions
* [[ONOS-991](https://jira.onosproject.org/browse/ONOS-991)] - Event handling in OpenFlowRuleProvider
* [[ONOS-1012](https://jira.onosproject.org/browse/ONOS-1012)] - TCP checksum error when using with IPv6
* [[ONOS-1013](https://jira.onosproject.org/browse/ONOS-1013)] - UDP checksum error when using with IPv6
* [[ONOS-1142](https://jira.onosproject.org/browse/ONOS-1142)] - LeadershipEvent serialization exception
* [[ONOS-1153](https://jira.onosproject.org/browse/ONOS-1153)] - Switch interfaces appearing as hosts when using IPv6
* [[ONOS-1160](https://jira.onosproject.org/browse/ONOS-1160)] - Sends group stats not only to OF1.3 switch also to OF1.0 switch
* [[ONOS-1167](https://jira.onosproject.org/browse/ONOS-1167)] - NPE in UI Topo view
* [[ONOS-1174](https://jira.onosproject.org/browse/ONOS-1174)] - Mininet start/stop LINC switch should also take care of cross-connects
* [[ONOS-1182](https://jira.onosproject.org/browse/ONOS-1182)] - In multi-instance scenario, random default flows stuck in PENDING\_ADD state even if flows have been installed in the dataplane
* [[ONOS-1183](https://jira.onosproject.org/browse/ONOS-1183)] - Same intent can be installed multiple times when installed through single node
* [[ONOS-1184](https://jira.onosproject.org/browse/ONOS-1184)] - Pre installed host intent does not work if the host entries were not present in ONOS during install
* [[ONOS-1186](https://jira.onosproject.org/browse/ONOS-1186)] - Exception when stoping onos with switches connected
* [[ONOS-1190](https://jira.onosproject.org/browse/ONOS-1190)] - DistributedLeadershipManager exceptions
* [[ONOS-1197](https://jira.onosproject.org/browse/ONOS-1197)] - NPE in EventuallyConsistentMapImpl: Exception thrown handling put
* [[ONOS-1205](https://jira.onosproject.org/browse/ONOS-1205)] - Netty exception while shutting down
* [[ONOS-1215](https://jira.onosproject.org/browse/ONOS-1215)] - Intents sometimes get stuck in INSTALLING phase when recompiled due to switch disconnect
* [[ONOS-1221](https://jira.onosproject.org/browse/ONOS-1221)] - Nodes don't correctly rejoin partitions when restarted
* [[ONOS-1254](https://jira.onosproject.org/browse/ONOS-1254)] - push-test-intents results in flows stuck in PENDING\_ADD state
* [[ONOS-1308](https://jira.onosproject.org/browse/ONOS-1308)] - High topology events latency with multiple ONOS nodes
* [[ONOS-1316](https://jira.onosproject.org/browse/ONOS-1316)] - Kryo buffer underflow
* [[ONOS-1327](https://jira.onosproject.org/browse/ONOS-1327)] - IntentPerfInstaller does not read in numNeighbors from config file
* [[ONOS-1339](https://jira.onosproject.org/browse/ONOS-1339)] - IntentPerfInstaller overall rate decreases during 5min TP test, when in cluster mode
* [[ONOS-1366](https://jira.onosproject.org/browse/ONOS-1366)] - ConsistentMap: Unable to commit writes in a 2node cluster
* [[ONOS-1376](https://jira.onosproject.org/browse/ONOS-1376)] - App command silently handles incorrect commands
* [[ONOS-1383](https://jira.onosproject.org/browse/ONOS-1383)] - When using null link provider sometimes all links do not show up
* [[ONOS-1384](https://jira.onosproject.org/browse/ONOS-1384)] - FlowRuleIntent class not registered with kryo
* [[ONOS-1390](https://jira.onosproject.org/browse/ONOS-1390)] - NettyMessagingService handler exception when running "intent-perf" for about 4~5min
* [[ONOS-1403](https://jira.onosproject.org/browse/ONOS-1403)] - Link reroute broken
* [[ONOS-1409](https://jira.onosproject.org/browse/ONOS-1409)] - Ping through host intent fails and log show PathNotFoundException
* [[ONOS-1414](https://jira.onosproject.org/browse/ONOS-1414)] - Phantom hosts discovered
* [[ONOS-1415](https://jira.onosproject.org/browse/ONOS-1415)] - Device event timestamp mismatch between "topology-events" and "topology-events-metrics"
* [[ONOS-1418](https://jira.onosproject.org/browse/ONOS-1418)] - App command will sometimes not work
* [[ONOS-1429](https://jira.onosproject.org/browse/ONOS-1429)] - metrics app still working after being deactivated
* [[ONOS-1434](https://jira.onosproject.org/browse/ONOS-1434)] - balance-masters command not working in latest master branch
* [[ONOS-1441](https://jira.onosproject.org/browse/ONOS-1441)] - DistributedFlowRuleStore doesn't remove flows for disconnected devices
* [[ONOS-1463](https://jira.onosproject.org/browse/ONOS-1463)] - NPE at Preconditions.checkNotNull & unable to purge intent
* [[ONOS-1471](https://jira.onosproject.org/browse/ONOS-1471)] - Speed up Raft leader election when there is a single node.
* [[ONOS-1480](https://jira.onosproject.org/browse/ONOS-1480)] - Running in to low memory issue on ONOS VMs during CHO test
* [[ONOS-1485](https://jira.onosproject.org/browse/ONOS-1485)] - Gossip Store Exceptions when running onos-null with metrics
* [[ONOS-1506](https://jira.onosproject.org/browse/ONOS-1506)] - Flows are added and hosts can ping each other even when an intent in WITHDRAWN state
* [[ONOS-1520](https://jira.onosproject.org/browse/ONOS-1520)] - Intents View tablebody too short compared to tablehead
* [[ONOS-1539](https://jira.onosproject.org/browse/ONOS-1539)] - "remove-intent" then tab, shows application modules instead of remove options
* [[ONOS-1594](https://jira.onosproject.org/browse/ONOS-1594)] - add-mpls-intent command line autocomplete third option shows wrong value
* [[ONOS-1595](https://jira.onosproject.org/browse/ONOS-1595)] - REST DELETE request to an endpoint that does not support it gives 500 error
* [[ONOS-1598](https://jira.onosproject.org/browse/ONOS-1598)] - NPE in FlowObjectiveManager when a device disconnects
* [[ONOS-1601](https://jira.onosproject.org/browse/ONOS-1601)] - Exception caught when issue "roles" cli command (which takes long time to return)
* [[ONOS-1602](https://jira.onosproject.org/browse/ONOS-1602)] - cfg command does not respect the -j option
* [[ONOS-1604](https://jira.onosproject.org/browse/ONOS-1604)] - Flows are not added/sync'ed across ONOS nodes after topology bringup
* [[ONOS-1609](https://jira.onosproject.org/browse/ONOS-1609)] - IllegalArgumentExceptions at OVSCorsaPipeline and interface
* [[ONOS-1610](https://jira.onosproject.org/browse/ONOS-1610)] - Exception in DefaultDrivers activate method when starting ONOS
* [[ONOS-1628](https://jira.onosproject.org/browse/ONOS-1628)] - NPE in HostLocationProvider
* [[ONOS-1629](https://jira.onosproject.org/browse/ONOS-1629)] - Seeing poor Cbench results due to some regression issue
* [[ONOS-1630](https://jira.onosproject.org/browse/ONOS-1630)] - Candidates list does not sync with two instances
* [[ONOS-1631](https://jira.onosproject.org/browse/ONOS-1631)] - Kryo serialization memory leak
* [[ONOS-1635](https://jira.onosproject.org/browse/ONOS-1635)] - Apps startup fails with Exceptions
* [[ONOS-1647](https://jira.onosproject.org/browse/ONOS-1647)] - onos-app-fwd adding flows after ONOS restart even though it is deactivated
* [[ONOS-1663](https://jira.onosproject.org/browse/ONOS-1663)] - FlowRule subsystem extension refactor
* [[ONOS-1671](https://jira.onosproject.org/browse/ONOS-1671)] - Switch (OVS 2.3) assigned to one instance of ONOS causes 'PORT\_STATS\_UPDATE' DeviceEvent Every 10 seconds, skewing Performance Results
* [[ONOS-1672](https://jira.onosproject.org/browse/ONOS-1672)] - copycat log synchronization issue
* [[ONOS-1673](https://jira.onosproject.org/browse/ONOS-1673)] - Fail fast when DatabaseManager does not start up cleanly
* [[ONOS-1676](https://jira.onosproject.org/browse/ONOS-1676)] - getCounters returns a set containing the counters from both the partitioned database and the in memory map
* [[ONOS-1677](https://jira.onosproject.org/browse/ONOS-1677)] - Restoration of p2p or h2h intents after link failure is not working
* [[ONOS-1678](https://jira.onosproject.org/browse/ONOS-1678)] - TopoView - empty detail panel when navigating away and back
* [[ONOS-1683](https://jira.onosproject.org/browse/ONOS-1683)] - Remove OpenFlow device drivers
* [[ONOS-1715](https://jira.onosproject.org/browse/ONOS-1715)] - NPE in "nodes" command
* [[ONOS-1731](https://jira.onosproject.org/browse/ONOS-1731)] - IllegalStateException: No feature matching for openflow & proxyarp during bootup
* [[ONOS-1736](https://jira.onosproject.org/browse/ONOS-1736)] - Warnings pop up when uninstalling apps
* [[ONOS-1741](https://jira.onosproject.org/browse/ONOS-1741)] - Packet request flows should be handled separately from app flows
* [[ONOS-1746](https://jira.onosproject.org/browse/ONOS-1746)] - Packet request flows stuck in PENDING\_ADD state
* [[ONOS-1751](https://jira.onosproject.org/browse/ONOS-1751)] - Onos karaf clean not compatible with ubuntu onos VM
* [[ONOS-1755](https://jira.onosproject.org/browse/ONOS-1755)] - Topology View -- panel not large enough for data
* [[ONOS-1768](https://jira.onosproject.org/browse/ONOS-1768)] - Tooltip from previous view appears on new view
* [[ONOS-1779](https://jira.onosproject.org/browse/ONOS-1779)] - obs fails sometimes
* [[ONOS-1782](https://jira.onosproject.org/browse/ONOS-1782)] - Switch links are showing up as hosts sometimes after ONOS retarts
* [[ONOS-1784](https://jira.onosproject.org/browse/ONOS-1784)] - onos app cfgs are missing
* [[ONOS-1792](https://jira.onosproject.org/browse/ONOS-1792)] - Missing rules for some subnets attached to Dell leaf segment routers
* [[ONOS-1797](https://jira.onosproject.org/browse/ONOS-1797)] - Flows are not removed on ONOS and Switches after host-intent removal
* [[ONOS-1798](https://jira.onosproject.org/browse/ONOS-1798)] - Can no longer balance masters after the migration to Raft based device mastership
* [[ONOS-1799](https://jira.onosproject.org/browse/ONOS-1799)] - Host intent default treatment is set to DROP after install
* [[ONOS-1802](https://jira.onosproject.org/browse/ONOS-1802)] - The new asynchronous behavior of MastershipService.requestRoleFor(DeviceId) can cause NPEs
* [[ONOS-1874](https://jira.onosproject.org/browse/ONOS-1874)] - mastership "weirdness"
* [[ONOS-1883](https://jira.onosproject.org/browse/ONOS-1883)] - Links disappear when devices change master
* [[ONOS-1890](https://jira.onosproject.org/browse/ONOS-1890)] - low IntentPerf rate when caught ONOS (log) ERROR
* [[ONOS-1893](https://jira.onosproject.org/browse/ONOS-1893)] - Device mastership transfer does not update the switches.
* [[ONOS-1894](https://jira.onosproject.org/browse/ONOS-1894)] - Ping stops after host-intent transitions to INSTALLED state, some flows are missing
* [[ONOS-1895](https://jira.onosproject.org/browse/ONOS-1895)] - Always the first node in 5-node cluster fails to come up after system:shutdown
* [[ONOS-1897](https://jira.onosproject.org/browse/ONOS-1897)] - onos-app-samples/calendar
* [[ONOS-1905](https://jira.onosproject.org/browse/ONOS-1905)] - No leader elected for a device with all nodes in the standby queue
* [[ONOS-1908](https://jira.onosproject.org/browse/ONOS-1908)] - Exception when serializing optical port descriptions
* [[ONOS-1909](https://jira.onosproject.org/browse/ONOS-1909)] - StorageException when activating FlowRuleManager
* [[ONOS-1910](https://jira.onosproject.org/browse/ONOS-1910)] - NPE in DeviceManager when disconnecting from switch
* [[ONOS-1913](https://jira.onosproject.org/browse/ONOS-1913)] - Update tests/drivers to match new json output
* [[ONOS-1917](https://jira.onosproject.org/browse/ONOS-1917)] - Services (Application,hosts, etc.) not working
* [[ONOS-1922](https://jira.onosproject.org/browse/ONOS-1922)] - KryoExceptions at org.onosproject.core.ApplicationRole
* [[ONOS-1926](https://jira.onosproject.org/browse/ONOS-1926)] - Unsupported match field is not handled properly
* [[ONOS-1928](https://jira.onosproject.org/browse/ONOS-1928)] - Topology View Panel resize on window resize
* [[ONOS-1948](https://jira.onosproject.org/browse/ONOS-1948)] - Topology not correctly discovered when restarting ONOS cluster
* [[ONOS-1950](https://jira.onosproject.org/browse/ONOS-1950)] - NPE when calling 'onos:intents -p -j'
* [[ONOS-1951](https://jira.onosproject.org/browse/ONOS-1951)] - Multi-instance instability
* [[ONOS-1958](https://jira.onosproject.org/browse/ONOS-1958)] - fix bug in showing tunnel attributes
* [[ONOS-1959](https://jira.onosproject.org/browse/ONOS-1959)] - fix bug in query subscription command in Tunnel management
* [[ONOS-1965](https://jira.onosproject.org/browse/ONOS-1965)] - Deadlock can occur when a old candidate restarts and does not re-enter ledership race
* [[ONOS-1966](https://jira.onosproject.org/browse/ONOS-1966)] - Links are temporarily lost when restarting ONOS nodes
* [[ONOS-1967](https://jira.onosproject.org/browse/ONOS-1967)] - Missing mastership events on mastership rebalancing
* [[ONOS-1981](https://jira.onosproject.org/browse/ONOS-1981)] - Listeners exceeded execution time limit
* [[ONOS-1986](https://jira.onosproject.org/browse/ONOS-1986)] - Intents update failed after link up/down (re-route case) in CHO
* [[ONOS-2003](https://jira.onosproject.org/browse/ONOS-2003)] - Some intents didn't reroute on link down
* [[ONOS-2011](https://jira.onosproject.org/browse/ONOS-2011)] - store the Path of the tunnel in the store
* [[ONOS-2014](https://jira.onosproject.org/browse/ONOS-2014)] - Compile and install PMC OLT software
* [[ONOS-2015](https://jira.onosproject.org/browse/ONOS-2015)] - Some devices have no ports after ONOS cluster restart
* [[ONOS-2016](https://jira.onosproject.org/browse/ONOS-2016)] - remove to check parameters iif they are null in the construtors of DefaultTunnel.e.g
* [[ONOS-2018](https://jira.onosproject.org/browse/ONOS-2018)] - Fix the bug that the src/dst end point of Vlan-type tunnel is the instance of OpticalTunnelEndPoint
* [[ONOS-2022](https://jira.onosproject.org/browse/ONOS-2022)] - LINC-OE doesn't start up
* [[ONOS-2025](https://jira.onosproject.org/browse/ONOS-2025)] - Host Intents are moving to CORRUPT state after adding (CHO Test)
* [[ONOS-2029](https://jira.onosproject.org/browse/ONOS-2029)] - Optical intents not working ( Optical app issue )
* [[ONOS-2030](https://jira.onosproject.org/browse/ONOS-2030)] - PCEP provider is unable to publish the device to ONOS
* [[ONOS-2031](https://jira.onosproject.org/browse/ONOS-2031)] - Cbench test return "0" and "Received unknown Barrier Reply" msg
* [[ONOS-2032](https://jira.onosproject.org/browse/ONOS-2032)] - Switches disconnected after link up/down in CHO test with handshaker.NiciraSwitchHandshaker broken pipe
* [[ONOS-2033](https://jira.onosproject.org/browse/ONOS-2033)] - Groups view - Buckets need to be one on each line
* [[ONOS-2037](https://jira.onosproject.org/browse/ONOS-2037)] - flows -j breaks after adding point intents (update REST codec)
* [[ONOS-2045](https://jira.onosproject.org/browse/ONOS-2045)] - Adding optical intents via CLI does not work for TL1-based providers
* [[ONOS-2046](https://jira.onosproject.org/browse/ONOS-2046)] - Port class type is incorrect in certain cases
* [[ONOS-2063](https://jira.onosproject.org/browse/ONOS-2063)] - Intent throughput performance drop off
* [[ONOS-2070](https://jira.onosproject.org/browse/ONOS-2070)] - Unable to process port stats due to NPE
* [[ONOS-2088](https://jira.onosproject.org/browse/ONOS-2088)] - java.lang.IllegalStateException: Unable to allocate ID block

## Epic

* [[ONOS-643](https://jira.onosproject.org/browse/ONOS-643)] - We need to complete integration tests for SDN-IP

## Improvement

* [[ONOS-181](https://jira.onosproject.org/browse/ONOS-181)] - Default FlowRules
* [[ONOS-961](https://jira.onosproject.org/browse/ONOS-961)] - Supports Group stats in EventHandler of OpenFlowController
* [[ONOS-1247](https://jira.onosproject.org/browse/ONOS-1247)] - LinkCollectionIntent instances created without using Intent.constraints()
* [[ONOS-1424](https://jira.onosproject.org/browse/ONOS-1424)] - Distributed Default Rule management
* [[ONOS-1433](https://jira.onosproject.org/browse/ONOS-1433)] - Distributed Group Store: Avoid two EC maps for the same data with different keys
* [[ONOS-1593](https://jira.onosproject.org/browse/ONOS-1593)] - Remove Duplicated Interfaces in org.onlab.packet.TCP
* [[ONOS-1650](https://jira.onosproject.org/browse/ONOS-1650)] - Add port names for TL1 providers
* [[ONOS-1674](https://jira.onosproject.org/browse/ONOS-1674)] - Allow full long value to be used as port number
* [[ONOS-1756](https://jira.onosproject.org/browse/ONOS-1756)] - Improve CLI auto completers

## New Feature

* [[ONOS-2007](https://jira.onosproject.org/browse/ONOS-2007)] - add RemoveTunnelByIdCommand
* [[ONOS-2008](https://jira.onosproject.org/browse/ONOS-2008)] - add UpdateTunnelBandWithCommand
* [[ONOS-2009](https://jira.onosproject.org/browse/ONOS-2009)] - add QueryAllTunnelsCommand
* [[ONOS-2010](https://jira.onosproject.org/browse/ONOS-2010)] - add queryAllTunnels api in TunnelService and TunnelStore
* [[ONOS-2017](https://jira.onosproject.org/browse/ONOS-2017)] - add the method of querying in SB

## Story

* [[ONOS-79](https://jira.onosproject.org/browse/ONOS-79)] - Move Distributed Flow Rule Store backups out of Hazelcast
* [[ONOS-86](https://jira.onosproject.org/browse/ONOS-86)] - Topology View details pane for edges (links)
* [[ONOS-100](https://jira.onosproject.org/browse/ONOS-100)] - Topology View toolbar - add first set of toggle buttons
* [[ONOS-406](https://jira.onosproject.org/browse/ONOS-406)] - DistributedIdBlockStore durability
* [[ONOS-453](https://jira.onosproject.org/browse/ONOS-453)] - Topology View: Custom Map
* [[ONOS-454](https://jira.onosproject.org/browse/ONOS-454)] - Topology View: Subnet Sprites
* [[ONOS-533](https://jira.onosproject.org/browse/ONOS-533)] - The ON.Lab Copyright year should be updated to include 2015
* [[ONOS-642](https://jira.onosproject.org/browse/ONOS-642)] - Define a network configuration API for ONOS
* [[ONOS-646](https://jira.onosproject.org/browse/ONOS-646)] - Test IPv6 with SDN-IP
* [[ONOS-660](https://jira.onosproject.org/browse/ONOS-660)] - Design interfaces for multiple table aware FlowRuleService
* [[ONOS-662](https://jira.onosproject.org/browse/ONOS-662)] - Add a virtual gateway for SDN network
* [[ONOS-679](https://jira.onosproject.org/browse/ONOS-679)] - Design interfaces for new Group subsystem
* [[ONOS-682](https://jira.onosproject.org/browse/ONOS-682)] - Implement multiple table features in FlowRule subsystem
* [[ONOS-684](https://jira.onosproject.org/browse/ONOS-684)] - Implement new Match and Actions for FlowRule
* [[ONOS-685](https://jira.onosproject.org/browse/ONOS-685)] - Implement Network Config Manager
* [[ONOS-688](https://jira.onosproject.org/browse/ONOS-688)] - Porting Tunnel policy
* [[ONOS-701](https://jira.onosproject.org/browse/ONOS-701)] - MPLS label manager API
* [[ONOS-743](https://jira.onosproject.org/browse/ONOS-743)] - ONOS CLI JSON generation should use same codecs as REST Apis
* [[ONOS-778](https://jira.onosproject.org/browse/ONOS-778)] - Define Group Subsystem Northbound Interfaces
* [[ONOS-908](https://jira.onosproject.org/browse/ONOS-908)] - Add Single to Multi & multi to single point intents test to CHO on all 3 topologies (ATT, Chordal, Spine)
* [[ONOS-917](https://jira.onosproject.org/browse/ONOS-917)] - Implement a new Group subsystem - provider part
* [[ONOS-920](https://jira.onosproject.org/browse/ONOS-920)] - Test, Profile, Optimization ONOS
* [[ONOS-929](https://jira.onosproject.org/browse/ONOS-929)] - Explicitly check "nodes" when an ONOS node restarts
* [[ONOS-958](https://jira.onosproject.org/browse/ONOS-958)] - Implement a Group action
* [[ONOS-1035](https://jira.onosproject.org/browse/ONOS-1035)] - Intent subsystem cleanup
* [[ONOS-1060](https://jira.onosproject.org/browse/ONOS-1060)] - Introduce "CORRUPT" intent state to represent certain irrecoverable error states
* [[ONOS-1079](https://jira.onosproject.org/browse/ONOS-1079)] - Implement Ciena TL1-based southbound for ROADMs
* [[ONOS-1087](https://jira.onosproject.org/browse/ONOS-1087)] - Implement core extensions
* [[ONOS-1090](https://jira.onosproject.org/browse/ONOS-1090)] - PCE extensions
* [[ONOS-1108](https://jira.onosproject.org/browse/ONOS-1108)] - Create a demo VM to demonstrate easily the features of SDN-IP and packet-optical
* [[ONOS-1109](https://jira.onosproject.org/browse/ONOS-1109)] - Understanding the logistic to connect GEANT network with Internet2 testbed.
* [[ONOS-1143](https://jira.onosproject.org/browse/ONOS-1143)] - Tooltip Service
* [[ONOS-1148](https://jira.onosproject.org/browse/ONOS-1148)] - Improve ONOS application permissions
* [[ONOS-1150](https://jira.onosproject.org/browse/ONOS-1150)] - Security-mode ONOS system design
* [[ONOS-1211](https://jira.onosproject.org/browse/ONOS-1211)] - Refactor CHO code
* [[ONOS-1223](https://jira.onosproject.org/browse/ONOS-1223)] - mpls label new feature
* [[ONOS-1232](https://jira.onosproject.org/browse/ONOS-1232)] - Topology View toolbar - add next set of buttons
* [[ONOS-1233](https://jira.onosproject.org/browse/ONOS-1233)] - Topology View toolbar - add third set of buttons
* [[ONOS-1234](https://jira.onosproject.org/browse/ONOS-1234)] - Topology View toolbar - add layer filter radio button set
* [[ONOS-1235](https://jira.onosproject.org/browse/ONOS-1235)] - Common web-socket for all GUI views
* [[ONOS-1242](https://jira.onosproject.org/browse/ONOS-1242)] - Add the ability to withdraw an intent using the REST API
* [[ONOS-1248](https://jira.onosproject.org/browse/ONOS-1248)] - host inside the SDN network need to be reachable and communicate from/to outside
* [[ONOS-1278](https://jira.onosproject.org/browse/ONOS-1278)] - Create Tabular View of Hosts
* [[ONOS-1279](https://jira.onosproject.org/browse/ONOS-1279)] - Create Tabular View of Cluster Nodes
* [[ONOS-1280](https://jira.onosproject.org/browse/ONOS-1280)] - Create Tabular View of Links
* [[ONOS-1281](https://jira.onosproject.org/browse/ONOS-1281)] - Tabular view of device flows
* [[ONOS-1282](https://jira.onosproject.org/browse/ONOS-1282)] - Create Tabular View of Intents
* [[ONOS-1283](https://jira.onosproject.org/browse/ONOS-1283)] - MPLS Label Manager Framework
* [[ONOS-1284](https://jira.onosproject.org/browse/ONOS-1284)] - Tunnel Manager Framework
* [[ONOS-1301](https://jira.onosproject.org/browse/ONOS-1301)] - Shared system timer and executor services - base
* [[ONOS-1304](https://jira.onosproject.org/browse/ONOS-1304)] - Shared system timer and executor services - configurability
* [[ONOS-1312](https://jira.onosproject.org/browse/ONOS-1312)] - Add single-to-multipoint intent driver function in onosclidriver
* [[ONOS-1314](https://jira.onosproject.org/browse/ONOS-1314)] - Refactor multi-to-single-point intent TestON driver to accept N number of IngressDevices
* [[ONOS-1323](https://jira.onosproject.org/browse/ONOS-1323)] - Upgrade to Apache Karaf 3.0.3
* [[ONOS-1329](https://jira.onosproject.org/browse/ONOS-1329)] - Migrate JSON Codecs to a bundle, which could be used by other apps
* [[ONOS-1337](https://jira.onosproject.org/browse/ONOS-1337)] - Add durability option to EventuallyConsistentMap
* [[ONOS-1341](https://jira.onosproject.org/browse/ONOS-1341)] - TestON driver changes required to support the new ONOS app system
* [[ONOS-1347](https://jira.onosproject.org/browse/ONOS-1347)] - Performance Test Refactoring for CI
* [[ONOS-1354](https://jira.onosproject.org/browse/ONOS-1354)] - Leadership service to support predictable handover of leadership
* [[ONOS-1355](https://jira.onosproject.org/browse/ONOS-1355)] - Intent cleanup for flow-rule system failures
* [[ONOS-1356](https://jira.onosproject.org/browse/ONOS-1356)] - Host Location Tracking for Intents
* [[ONOS-1357](https://jira.onosproject.org/browse/ONOS-1357)] - Provide a builder pattern for EventuallyConsistentMap
* [[ONOS-1358](https://jira.onosproject.org/browse/ONOS-1358)] - Testing Reactive routing in NFV environment
* [[ONOS-1360](https://jira.onosproject.org/browse/ONOS-1360)] - Update tutorial VM for 1.1.0
* [[ONOS-1380](https://jira.onosproject.org/browse/ONOS-1380)] - Enable a user to create and remove optical-intents from CLI
* [[ONOS-1385](https://jira.onosproject.org/browse/ONOS-1385)] - Complete Blackbird Performance & Scalability white paper
* [[ONOS-1386](https://jira.onosproject.org/browse/ONOS-1386)] - Infrastructure setup spring - Setup the development environment as per ONOS Wiki guidelines.
* [[ONOS-1399](https://jira.onosproject.org/browse/ONOS-1399)] - Create presentation for International SDN/OF deployments
* [[ONOS-1411](https://jira.onosproject.org/browse/ONOS-1411)] - As a user, I would like to have consistency between ports reported in the CLI and in the GUI.
* [[ONOS-1416](https://jira.onosproject.org/browse/ONOS-1416)] - Mobile GUI support: Topology View pan and zoom via touch
* [[ONOS-1423](https://jira.onosproject.org/browse/ONOS-1423)] - Better multi table support - FlowObjectiveService
* [[ONOS-1425](https://jira.onosproject.org/browse/ONOS-1425)] - Update Wiki contents for Blackbird functionality
* [[ONOS-1440](https://jira.onosproject.org/browse/ONOS-1440)] - Implement port statistics framework in core
* [[ONOS-1442](https://jira.onosproject.org/browse/ONOS-1442)] - Sortable Tables - Implement Column Comparators and Formatters
* [[ONOS-1443](https://jira.onosproject.org/browse/ONOS-1443)] - Implement group bucket statistics updation
* [[ONOS-1444](https://jira.onosproject.org/browse/ONOS-1444)] - Group handling logic to create groups on-demand when they are not created by default
* [[ONOS-1449](https://jira.onosproject.org/browse/ONOS-1449)] - Rebuild Null Provider for consistent operations
* [[ONOS-1466](https://jira.onosproject.org/browse/ONOS-1466)] - Internet as a service task-add vBNG
* [[ONOS-1467](https://jira.onosproject.org/browse/ONOS-1467)] - First draft of software architecture and components
* [[ONOS-1469](https://jira.onosproject.org/browse/ONOS-1469)] - Device View: include ID of master instances
* [[ONOS-1473](https://jira.onosproject.org/browse/ONOS-1473)] - Add a cli command for inspecting different consistent maps in the cluster
* [[ONOS-1474](https://jira.onosproject.org/browse/ONOS-1474)] - DeviceView: display device details pane on selection
* [[ONOS-1475](https://jira.onosproject.org/browse/ONOS-1475)] - Tabular views adjusted to have no bottom margin
* [[ONOS-1476](https://jira.onosproject.org/browse/ONOS-1476)] - Device View: display columns for count of device ports and egress links
* [[ONOS-1477](https://jira.onosproject.org/browse/ONOS-1477)] - Navigation Menu: glyphs on menu items
* [[ONOS-1478](https://jira.onosproject.org/browse/ONOS-1478)] - Navigation Menu: segmentation into categories
* [[ONOS-1491](https://jira.onosproject.org/browse/ONOS-1491)] - Refactoring of flow rule populator using the new objectives(?) subsystem
* [[ONOS-1492](https://jira.onosproject.org/browse/ONOS-1492)] - Obtain radius configuration from AT&T
* [[ONOS-1494](https://jira.onosproject.org/browse/ONOS-1494)] - ONOS interface to XOS
* [[ONOS-1495](https://jira.onosproject.org/browse/ONOS-1495)] - Implement Functionality test to verify VLAN intents
* [[ONOS-1497](https://jira.onosproject.org/browse/ONOS-1497)] - Add required TestON driver functions for component configuration CLI
* [[ONOS-1505](https://jira.onosproject.org/browse/ONOS-1505)] - Refactoring of default group handler using the new objectives subsystem
* [[ONOS-1513](https://jira.onosproject.org/browse/ONOS-1513)] - Port TestOn automated tests for Segment Routing
* [[ONOS-1515](https://jira.onosproject.org/browse/ONOS-1515)] - Try single instance fabric control on Dell switches
* [[ONOS-1516](https://jira.onosproject.org/browse/ONOS-1516)] - Multi-instance fabric control on Dell switches
* [[ONOS-1517](https://jira.onosproject.org/browse/ONOS-1517)] - Setup Dell switches in leaf-spine topology
* [[ONOS-1521](https://jira.onosproject.org/browse/ONOS-1521)] - Create new TestON tests for leaf-spine topology
* [[ONOS-1522](https://jira.onosproject.org/browse/ONOS-1522)] - Sticky user preferences
* [[ONOS-1526](https://jira.onosproject.org/browse/ONOS-1526)] - Setup VPN connection to Fujitsu lab
* [[ONOS-1530](https://jira.onosproject.org/browse/ONOS-1530)] - Port BGP Router app to use new flow Objectives
* [[ONOS-1531](https://jira.onosproject.org/browse/ONOS-1531)] - Validate Corsa operation with new flow Objectives on TestOn automated test cases
* [[ONOS-1543](https://jira.onosproject.org/browse/ONOS-1543)] - Write wiki page that describes how to install ONOS on CentOS
* [[ONOS-1552](https://jira.onosproject.org/browse/ONOS-1552)] - Create OF-DPA driver for BGP Router flow Objectives
* [[ONOS-1553](https://jira.onosproject.org/browse/ONOS-1553)] - Spec out and purchase servers & optics for BGP Router
* [[ONOS-1557](https://jira.onosproject.org/browse/ONOS-1557)] - Discuss CoVisor integration into ONOS
* [[ONOS-1559](https://jira.onosproject.org/browse/ONOS-1559)] - Create a Performance short test for regression purpose
* [[ONOS-1572](https://jira.onosproject.org/browse/ONOS-1572)] - Test switch with ONOS
* [[ONOS-1573](https://jira.onosproject.org/browse/ONOS-1573)] - Add status verification to CHO test cases
* [[ONOS-1577](https://jira.onosproject.org/browse/ONOS-1577)] - Update Functionality Test (Prod/MultiProd) to use the new app sub-system
* [[ONOS-1580](https://jira.onosproject.org/browse/ONOS-1580)] - Modify pingall function in Mininet driver ( mininetclidriver.py )
* [[ONOS-1590](https://jira.onosproject.org/browse/ONOS-1590)] - Add a config to launch SpringOpenTTP driver for SegmentRoutingApp
* [[ONOS-1591](https://jira.onosproject.org/browse/ONOS-1591)] - Display flash messages for actions in the Topology View toolbar
* [[ONOS-1597](https://jira.onosproject.org/browse/ONOS-1597)] - All add intent type CLI should allow setting the appId option
* [[ONOS-1599](https://jira.onosproject.org/browse/ONOS-1599)] - Implement a LogicalClockService
* [[ONOS-1605](https://jira.onosproject.org/browse/ONOS-1605)] - Investigate and build a simple MPLS Functionality test framework on TestON
* [[ONOS-1612](https://jira.onosproject.org/browse/ONOS-1612)] - Tab completion for component properties with the cfg cli command
* [[ONOS-1615](https://jira.onosproject.org/browse/ONOS-1615)] - Update DB for QA tests on ONOS
* [[ONOS-1616](https://jira.onosproject.org/browse/ONOS-1616)] - Deploy the machine in the server room for CORD
* [[ONOS-1619](https://jira.onosproject.org/browse/ONOS-1619)] - NPE in FlowObjectiveManager when processing DEVICE\_ADDED event
* [[ONOS-1634](https://jira.onosproject.org/browse/ONOS-1634)] - Office network: substitute generic access points with OF (OpenWRT + OVS) access points.
* [[ONOS-1644](https://jira.onosproject.org/browse/ONOS-1644)] - Deploy ONOS and SDN-IP on FIU and AMLight production networks (first two nodes: FIU + Reclara + 2 ONOS instances + SDN-IP)
* [[ONOS-1645](https://jira.onosproject.org/browse/ONOS-1645)] - Migrate Dell - Segment Routing switches to rack 4
* [[ONOS-1656](https://jira.onosproject.org/browse/ONOS-1656)] - Port LinkResourceStore to use LeadershipService
* [[ONOS-1657](https://jira.onosproject.org/browse/ONOS-1657)] - FlowRuleStore using LeadershipService
* [[ONOS-1668](https://jira.onosproject.org/browse/ONOS-1668)] - Migrate Quanta/OF-DPA based BGP Router to Rack 4
* [[ONOS-1669](https://jira.onosproject.org/browse/ONOS-1669)] - Write unit tests for TableBuilder Service
* [[ONOS-1681](https://jira.onosproject.org/browse/ONOS-1681)] - Modify flowrules to accept table ids
* [[ONOS-1685](https://jira.onosproject.org/browse/ONOS-1685)] - Functionality Test Enhancements (new topology)
* [[ONOS-1690](https://jira.onosproject.org/browse/ONOS-1690)] - Topology View details pane buttons
* [[ONOS-1696](https://jira.onosproject.org/browse/ONOS-1696)] - Create XOS UI view for Subscriber
* [[ONOS-1698](https://jira.onosproject.org/browse/ONOS-1698)] - Investigate additional GEO maps
* [[ONOS-1699](https://jira.onosproject.org/browse/ONOS-1699)] - GUI Wiki documentation
* [[ONOS-1700](https://jira.onosproject.org/browse/ONOS-1700)] - Resolve IntentTP drop issue
* [[ONOS-1705](https://jira.onosproject.org/browse/ONOS-1705)] - SDN-IP testing code update
* [[ONOS-1706](https://jira.onosproject.org/browse/ONOS-1706)] - Replicate tests for multi-instance
* [[ONOS-1707](https://jira.onosproject.org/browse/ONOS-1707)] - Automatic reports to IP/optical team of test results
* [[ONOS-1708](https://jira.onosproject.org/browse/ONOS-1708)] - Create simple VLAN forwarding app for fabric
* [[ONOS-1709](https://jira.onosproject.org/browse/ONOS-1709)] - Create DB tables and views for ONOS functional tests
* [[ONOS-1710](https://jira.onosproject.org/browse/ONOS-1710)] - Implement Fujitsu TL1-based southbound for ROADMs
* [[ONOS-1711](https://jira.onosproject.org/browse/ONOS-1711)] - Implement Huawei PCEP-based southbound for ROADMs
* [[ONOS-1734](https://jira.onosproject.org/browse/ONOS-1734)] - FlowObjectiveManager distributes next id
* [[ONOS-1739](https://jira.onosproject.org/browse/ONOS-1739)] - Add host intents in IP/Optical Tests
* [[ONOS-1740](https://jira.onosproject.org/browse/ONOS-1740)] - Make ONOS extraneous flow rule deletion configurable
* [[ONOS-1747](https://jira.onosproject.org/browse/ONOS-1747)] - Update GUI version before Cardinal release
* [[ONOS-1748](https://jira.onosproject.org/browse/ONOS-1748)] - Create workaround to avoid port\_stats\_updated DeviceEvent timestamps
* [[ONOS-1752](https://jira.onosproject.org/browse/ONOS-1752)] - Update container environment for ONOS Cardinal testing
* [[ONOS-1766](https://jira.onosproject.org/browse/ONOS-1766)] - Fix the BgpRouter TestON environment according to the change of application packaging
* [[ONOS-1783](https://jira.onosproject.org/browse/ONOS-1783)] - Refresh button on all GUI tabular views
* [[ONOS-1786](https://jira.onosproject.org/browse/ONOS-1786)] - Supports link failure and recovery using objective subsystem
* [[ONOS-1791](https://jira.onosproject.org/browse/ONOS-1791)] - Push MPLS rules at edge segment routers
* [[ONOS-1794](https://jira.onosproject.org/browse/ONOS-1794)] - Make gossip store aware of port types
* [[ONOS-1796](https://jira.onosproject.org/browse/ONOS-1796)] - Feature Test Improvements using New Topology (Story for Sprint-5)
* [[ONOS-1803](https://jira.onosproject.org/browse/ONOS-1803)] - LINC port descriptions do not carry optical information
* [[ONOS-1810](https://jira.onosproject.org/browse/ONOS-1810)] - Introduce Tunnels & Tunnel-Flow Policy handling
* [[ONOS-1817](https://jira.onosproject.org/browse/ONOS-1817)] - Flow Statistics (Packets and Bytes) to be displayed in Flow table
* [[ONOS-1819](https://jira.onosproject.org/browse/ONOS-1819)] - Display per device Group information (both group description and group statistics)
* [[ONOS-1820](https://jira.onosproject.org/browse/ONOS-1820)] - Display per device port statistics
* [[ONOS-1822](https://jira.onosproject.org/browse/ONOS-1822)] - Display traffic flow visualization using port statistics
* [[ONOS-1831](https://jira.onosproject.org/browse/ONOS-1831)] - TestON: Segment Routing single-instance testcase fixing and validation
* [[ONOS-1834](https://jira.onosproject.org/browse/ONOS-1834)] - Verify Data plane recovery feature on Dell switches with ONOS-1786 changes
* [[ONOS-1839](https://jira.onosproject.org/browse/ONOS-1839)] - SR group handler should avoid creating all default groups again during port down and link up event
* [[ONOS-1842](https://jira.onosproject.org/browse/ONOS-1842)] - Refactor Tabular View to have better table resizing behavior
* [[ONOS-1843](https://jira.onosproject.org/browse/ONOS-1843)] - Clean up HA Tests
* [[ONOS-1847](https://jira.onosproject.org/browse/ONOS-1847)] - Refactor device details panel to be a custom directive
* [[ONOS-1852](https://jira.onosproject.org/browse/ONOS-1852)] - Documentation for writing a new driver
* [[ONOS-1853](https://jira.onosproject.org/browse/ONOS-1853)] - Performing system tests in Deployment VM
* [[ONOS-1861](https://jira.onosproject.org/browse/ONOS-1861)] - enable vBNG to deal with the silent hosts
* [[ONOS-1863](https://jira.onosproject.org/browse/ONOS-1863)] - enable startMonitorHost with configuration file
* [[ONOS-1867](https://jira.onosproject.org/browse/ONOS-1867)] - Implement TrafficTreatments for Packet + Optical
* [[ONOS-1868](https://jira.onosproject.org/browse/ONOS-1868)] - Implement TrafficSelectors for Packet + Optical
* [[ONOS-1877](https://jira.onosproject.org/browse/ONOS-1877)] - Remove user input when starting multi-layer topology
* [[ONOS-1878](https://jira.onosproject.org/browse/ONOS-1878)] - Setup VPN connection to Huawei lab
* [[ONOS-1889](https://jira.onosproject.org/browse/ONOS-1889)] - Driver Inheritance mechanism
* [[ONOS-1892](https://jira.onosproject.org/browse/ONOS-1892)] - wiki of vBNG
* [[ONOS-1915](https://jira.onosproject.org/browse/ONOS-1915)] - Modify point intents in old functionality tests
* [[ONOS-1927](https://jira.onosproject.org/browse/ONOS-1927)] - Run Cbench on a Single node in multi Instance Bare Metal ONOS cluster
* [[ONOS-1929](https://jira.onosproject.org/browse/ONOS-1929)] - Merge all messaging substrates.
* [[ONOS-1933](https://jira.onosproject.org/browse/ONOS-1933)] - CORD Subscriber Login View
* [[ONOS-1934](https://jira.onosproject.org/browse/ONOS-1934)] - CORD Subscriber Dashboard View
* [[ONOS-1936](https://jira.onosproject.org/browse/ONOS-1936)] - CORD Subscriber Edit Bundles - URL filtering
* [[ONOS-1937](https://jira.onosproject.org/browse/ONOS-1937)] - CORD Subscriber Users View
* [[ONOS-1938](https://jira.onosproject.org/browse/ONOS-1938)] - CORD Subscriber Edit User Profile
* [[ONOS-1939](https://jira.onosproject.org/browse/ONOS-1939)] - CORD Subscriber - Proxy to XOS
* [[ONOS-1947](https://jira.onosproject.org/browse/ONOS-1947)] - Tunnel management improvements
* [[ONOS-1949](https://jira.onosproject.org/browse/ONOS-1949)] - Integrate vBNG and test it in demo environment
* [[ONOS-1956](https://jira.onosproject.org/browse/ONOS-1956)] - Ensure incubating features are in onos-incubator
* [[ONOS-1960](https://jira.onosproject.org/browse/ONOS-1960)] - Wiki update for Cardinal
* [[ONOS-1970](https://jira.onosproject.org/browse/ONOS-1970)] - Intent Functionality Test suite
* [[ONOS-1979](https://jira.onosproject.org/browse/ONOS-1979)] - Modify arping in mininet and remote minient drier to add another option for VLAN "-I <node-interface>"
* [[ONOS-1980](https://jira.onosproject.org/browse/ONOS-1980)] - Translation of Lambdas for Linc-OE
* [[ONOS-1990](https://jira.onosproject.org/browse/ONOS-1990)] - Add delete vBNG feature
* [[ONOS-1992](https://jira.onosproject.org/browse/ONOS-1992)] - Make intent clean-up configurable
* [[ONOS-2042](https://jira.onosproject.org/browse/ONOS-2042)] - Adding new function in onosclidriver for summary command
* [[ONOS-2048](https://jira.onosproject.org/browse/ONOS-2048)] - Release resources when removing intents
* [[ONOS-2049](https://jira.onosproject.org/browse/ONOS-2049)] - Allow creation of optical circuit intents via CLI
* [[ONOS-2050](https://jira.onosproject.org/browse/ONOS-2050)] - Merge loxigen patchset by Calient
* [[ONOS-2065](https://jira.onosproject.org/browse/ONOS-2065)] - Intents in FAILED state (Optical Test)
* [[ONOS-2066](https://jira.onosproject.org/browse/ONOS-2066)] - add command line for vBNG
* [[ONOS-2083](https://jira.onosproject.org/browse/ONOS-2083)] - add REST API to vBNG to get the map

## Task

* [[ONOS-1164](https://jira.onosproject.org/browse/ONOS-1164)] - Review available NETCONF client libraries and find out the one that is most suitable
* [[ONOS-1445](https://jira.onosproject.org/browse/ONOS-1445)] - Add new app sub system to CHO
* [[ONOS-1460](https://jira.onosproject.org/browse/ONOS-1460)] - Debug BGP router jenkins job failure
* [[ONOS-1596](https://jira.onosproject.org/browse/ONOS-1596)] - Add driver function in onosclidriver to check intents state
* [[ONOS-1618](https://jira.onosproject.org/browse/ONOS-1618)] - Install OpenStack and XOS
* [[ONOS-1643](https://jira.onosproject.org/browse/ONOS-1643)] - Add driver function in onosclidriver to check flows state
* [[ONOS-1719](https://jira.onosproject.org/browse/ONOS-1719)] - Update runOpticalMnScript function in remote mininet driver
* [[ONOS-1789](https://jira.onosproject.org/browse/ONOS-1789)] - Define Lambda type
* [[ONOS-1790](https://jira.onosproject.org/browse/ONOS-1790)] - Define OchSignal class
* [[ONOS-1844](https://jira.onosproject.org/browse/ONOS-1844)] - Define a Criterion for OchSignal
* [[ONOS-1845](https://jira.onosproject.org/browse/ONOS-1845)] - Define a Criterion for IndexedLambda
* [[ONOS-1846](https://jira.onosproject.org/browse/ONOS-1846)] - Define a Criterion for OchSignalType
