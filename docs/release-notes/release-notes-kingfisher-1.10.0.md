# Release Notes - Kingfisher 1.10.0

# High level summary:

 

* **Deployments**

+ ONOS deployed in JGN-X (Japan testbed)
+ New VPLS application deployed in production in NCTU
+ New driver for Corsa DP2100 and fix for Corsa DP6410
+ ONOS + SDX-L2 deployed in GÉANT pilot

* **Tools**

+ YANG Tools 2.0

- All models kept in a single store
- Common ancestor for all models; model-agnostic and model-specific access; friendly API for apps
- YANG models can be introduced and compiled at runtime
- RESTCONF & NETCONF adapters can be maintained separately
- YANG tools, dynamic config manager and store are implemented in a modular fashion; they can be evolved and maintained independently from one another; generated classes are not tied to the dynamic config store

+ Extended ONOS Buck plugin to support embedded dependencies

* **Applications/Use Cases**

+ GUI

- Added packets/second mode to traffic monitoring
- Dark theme reinstated
- Regions/layouts enhancements - layouts can use grid or geo backgrounds for example

+ Packet Optical

- OpenROADM device, network and service support
- Full protection behaviour incl. hardware-based demonstration

+ Datacenter/SONA

- Support for VLAN based virtual network provisioning
- Unit tests and support of OpenStack Tempest API

+ vRouter

- Enable multiple FPM connections for HA
- Added support for multiple control plane redirects for multiple Quagga routers

* **Northbound**

+ RESTCONF adapter for YANG
+ Intent Framework improvements

- Intent framework and VPLS support for OFDPA pipeline (e.g. Accton switches)
- New intent installer to let users create their own intent installer logic and plug them in at run-time
- Domain intents: extension of Intent Framework to generate domain intents

+ Route subsystem enhanced to support multiple routes per prefix

* **Core**

+ Virtualization improvements

- Support of flow objective and mastership services for virtual networks
- Performance improvements

* **Southbound**

+ NETCONF adapter for YANG
+ Apache Mina library for NETCONF
+ OpenFlow 1.4 support
+ LISP subsystem enhancements for mapping services

* **QA Infrastructure**

+ Performance [white paper 2.0](../assets/whitepaper-onos-kingfisher-release-performance.pdf) - first update of performance since Blackbird release
+ New tests on Bandwidth Allocation
+ Tracked down several bugs affecting HA and clustering

# Details:

## Non-brigade contribution

 

* [ONOS-5565]Implementation of QosConfig and QueueConfig(Frank Wang)

## Deployment Brigade (Jimmy Ou, Jordi Ortiz, Luca Prete, Yi Tseng, Yoshihiko Kanaumi, Pier Luigi Ventre, Carolina Fernandez)

 

* New intent installer to let users create their own intent installer logic and plug them in at run-time
* Initial intent framework support for OF groups
* VPLS refactoring: improved code modularity, higher stability, performance improvements, new VPLS status, visible in the VPLS CLI
* Initial support for OF meters
* Intent framework and VPLS support for OFDPA pipeline (i.e. Accton switch)
* PoC: ONOS in a Box - ONOS working as OS directly on top of Accton switches
* ONOS deployed in JGN-X (Japan testbed)
* New VPLS application deployed in production in NCTU
* New driver for Corsa DP2100
* Fix for Corsa DP6410
* ONOS + SDX-L2 deployed in GÉANT pilot

## Network Virtualization Brigade (YoonSeon Han, Claudine Chiu, Harold Huang, Jovana Vuleta)

 

* Support of flow objective and mastership services for virtual networks
* Distributed stores for packet, flow rule, and flow objectives
* Improved the performance for (de)virtualizing and packet and flow rules
* Refactoring of legacy interfaces and logics
* Support REST API for OFagent (the core part of OF is under development)

## Dynamic Configuration Brigade

## 

**Huawei**: Patrick Liu  [patrick.liu@huawei.com](mailto:patrick.liu@huawei.com), Gaurav agrawal [gaurav.agrawal@huawei.com](mailto:gaurav.agrawal@huawei.com), Vinod Kumar S ([vinods.kumar@huawei.com](mailto:vinods.kumar@huawei.com)), Sithara Punnassery [Sithara.Punnassery@huawei.com](mailto:Sithara.Punnassery@huawei.com), Sonu Gupta [sonu.gupta@huawei.com](mailto:sonu.gupta@huawei.com), Henry Yu [henry.yu1@huawei.com](mailto:henry.yu1@huawei.com), Bharat Saraswal [bharat.saraswal@huawei.com](mailto:bharat.saraswal@huawei.com), Janani B [janani.b@huawei.com](mailto:janani.b@huawei.com), Vidyashree Rama [Vidyashree.Rama@huawei.com](mailto:Vidyashree.Rama@huawei.com), Adarsh M [adarsh.m@huawei.com](mailto:adarsh.m@huawei.com), Aruna kumar padhi [aruna.padhi@huawei.com](mailto:aruna.padhi@huawei.com), Shankara ([shankara@huawei.com](mailto:shankara@huawei.com)), Rama Subba Reddy ([Rama.Subba.Reddy.S@huawei.com](mailto:Rama.Subba.Reddy.S@huawei.com)), A U Surya ([a.u.surya@huawei.com](mailto:a.u.surya@huawei.com)), Jin Gan

 

**ON.Lab**: Thomas Vachuska  [tom@onlab.us](mailto:tom@onlab.us), Brian O’Connor [bocon@onlab.us](mailto:bocon@onlab.us), Ray Milkey [ray@onlab.us](mailto:ray@onlab.us), Simon Hunt [simon@onlab.us](mailto:simon@onlab.us)

 

**Fujitsu**: Aaron kruglikov [aaron@onlab.us](mailto:aaron@onlab.us)

 

* YANG Tools 2.0

+ Ability to store data for all and any models in a single store
+ Common ancestor for all models; model-agnostic and model-specific access; friendly API for apps
+ YANG models can be introduced and compiled at runtime (e.g. from a device
+ RESTCONF & NETCONF adapters can be maintained separately
+ Allows use with or without the dynamic configuration store
+ YANG tools, dynamic config manager and store are implemented in a modular fashion; they can be evolved and maintained independently from one another; generated classes are not tied to the dynamic config store

* RESTCONF NB & NETCONF SB Adapter for YANG
* DynamicConfig App and Distributed Store

## GUI Brigade (Simon Hunt, Steven Burrows)

 

* Nodes and links auto-scale with zoom in/out (retrofitted to classic topology view)
* Added packets/second mode to traffic monitoring
* Dark theme reinstated
* Topology 2:

+ Added to navigation menu
+ Regions / Layouts configurable by scripted CLI commands
+ Layouts can use geo backgrounds (latitude/longitude) or grid backgrounds (Y/X) to provide specification of device/host/subregion locations on the view
+ Traffic monitoring augmented to allow aggregation of data over “synthetic” (e.g. region-to-region) links
+ Basic toolbar functionality implemented

* Various bug fixes
* Various extensibility and scalability enhancements applied to client-side code

## gRPC Brigade (Aaron Kruglikov, …)

 

* Brigade planning and organization completed
* Build tools and services created (in master but unlikely to be included in K release)

## Build and Package Infrastructure Brigade (Viswanath KSP)

 

* Extended BUCK to support embedded dependencies - [ONOS-6359](https://jira.onosproject.org/browse/ONOS-6359)
* Experimented code disaggregation with REPO - demo planned with onos-app-samples
* Fixed Gerrit patchset validation pipeline code
* Documented existing Jenkins build process and experimented with Gitbook

## Teaching Brigade (Abdulhalim Dandoush, David Boswell, Lefteris Manassakis, Alexis MUNYANDEKWE, Andrea Campanella, Timon Sloane, Elena Olkhovskaya, David Mahler, sachidananda sahu)

 

* Brigade working days with concrete action points (recordings are available and the action points will be organized in jira tickets)
* Document to reorganize and fill the content for Module 1.4 (intro to SDN)
* Document to reorganize the fill the content for Module 1.5 (intro to ONOS)
* Slides materials for some 1.4 (intro to SDN) sections
* Feedback and broken elements about some wiki sections related to 1.5 (intro to ONOS)

+ Tutorials (i.e. installation, distributed ONOS, etc.)
+ Architecture guide

## Security and Performance Analysis Brigade (Stefano Secci, Kamel Attou, Dung Chi Phung, Jian Li, José Sanchez, David Espinel, Dylan Smith)

 

* Run first complete bundle failure test campaign.
* Run LISP SBI performance tests.
* Identified two security bugs.

## QA (Jon Hall, You Wang, Pratik Parab, and Shreya Chowdhary)

 

* Performance white paper 2.0 - first update of performance since Blackbird release
* Docker test to pull images for released versions of ONOS
* OF 1.5 feature list
* New tests on Bandwidth Allocation
* Improvements in Intent tests, NetConf, NetCfg and BGPLS
* Tracked down several bugs affecting HA and clustering
* Introduced Jenkins Pipeliner job for Scale and Performance tests
* System level tests for the Distributed Work Queue API

## Packet Optical use case (Marc De Leenheer, Yuta Higuchi)

 

* OpenROADM device, network and service support
* Full protection behaviour incl. hardware-based demonstration
* OpenFlow 1.4 support (Murat Parlakisik, Jimmy Jin)
* Improvements to ROADM App (Jimmy Jin, Mao Lu, Jimmy Yan)

## Data center use case/OpenStack integration - SONA Project (Hyunsun Moon)

 

* Added support of VLAN based virtual network provisioning
* Added support of security group to openstack/networking-onos and SONA
* Added methods to recover data plane
* Added support of OVS connection tracking and NAT extension to onos-loxi and ONOS
* Added unit tests and support of OpenStack Tempest API and scenario tests
* Added SONA installed and activated ONOS Docker image to Dockerhub

## LISP Subsystem support (Jian Li)

 

* Implemented mapping management application

+ Implemented distributed and simple MappingStore, and MappingManagers
+ Modeled and implemented several mapping primitives
+ Provided abstractions for LCAF using ExtensionMappingAddress
+ Added CLI, REST, GUI to query mapping information

* Provided a way to assess SBI performance
* Improved the performance of MapServer and MapResolver

# Gory Details

## Sub-task

* [[ONOS-5682](https://jira.onosproject.org/browse/ONOS-5682)] - Implement Virtual network related events
* [[ONOS-5950](https://jira.onosproject.org/browse/ONOS-5950)] - Refactor application structure
* [[ONOS-5951](https://jira.onosproject.org/browse/ONOS-5951)] - Remove security group support
* [[ONOS-5952](https://jira.onosproject.org/browse/ONOS-5952)] - Refactor to cache network states
* [[ONOS-6053](https://jira.onosproject.org/browse/ONOS-6053)] - Implement simple mapping store
* [[ONOS-6054](https://jira.onosproject.org/browse/ONOS-6054)] - Implement distributed mapping store
* [[ONOS-6055](https://jira.onosproject.org/browse/ONOS-6055)] - Define mapping store interface
* [[ONOS-6073](https://jira.onosproject.org/browse/ONOS-6073)] - Implement MappingManager
* [[ONOS-6201](https://jira.onosproject.org/browse/ONOS-6201)] - Add to existing VirtualNetworkFlowObjectiveManager unit tests
* [[ONOS-6423](https://jira.onosproject.org/browse/ONOS-6423)] - Implement missing getOrDefault methods in primitive wrappers
* [[ONOS-6425](https://jira.onosproject.org/browse/ONOS-6425)] - Improve logging for transactions
* [[ONOS-6426](https://jira.onosproject.org/browse/ONOS-6426)] - Include tombstones in null comparisons in AtomixConsistentMapState

## Bug

* [[ONOS-4950](https://jira.onosproject.org/browse/ONOS-4950)] - SONA apps cannot get node COMPLETE event on start-up
* [[ONOS-5683](https://jira.onosproject.org/browse/ONOS-5683)] - Intent throughput test regression
* [[ONOS-5725](https://jira.onosproject.org/browse/ONOS-5725)] - [YMS-Integration] YANG schema registration error using buck-compiled YMS
* [[ONOS-5784](https://jira.onosproject.org/browse/ONOS-5784)] - Empty latitude/longitude in ONOS Web UI
* [[ONOS-5853](https://jira.onosproject.org/browse/ONOS-5853)] - FlowEntry: correctly rebuild permanent entries from devices
* [[ONOS-5902](https://jira.onosproject.org/browse/ONOS-5902)] - Leaders Command Fails with Timeout
* [[ONOS-5911](https://jira.onosproject.org/browse/ONOS-5911)] - Port removal after receiving OFPR\_DELETE port status reason.
* [[ONOS-5971](https://jira.onosproject.org/browse/ONOS-5971)] - [ONOS-YANG]Compilation issue occurred for notification feature.
* [[ONOS-5978](https://jira.onosproject.org/browse/ONOS-5978)] - Set SDN-IP as required application for reactive-routing in BUCK
* [[ONOS-5982](https://jira.onosproject.org/browse/ONOS-5982)] - Bad comparison of signed byte with 240
* [[ONOS-6020](https://jira.onosproject.org/browse/ONOS-6020)] - NETCONF API regression
* [[ONOS-6023](https://jira.onosproject.org/browse/ONOS-6023)] - Existence of BasicLinkConfig result in bogus latency value
* [[ONOS-6031](https://jira.onosproject.org/browse/ONOS-6031)] - Unable to resolve behavior if it is not defined in onos-drivers.xml
* [[ONOS-6041](https://jira.onosproject.org/browse/ONOS-6041)] - Deleting the device from onos making continuous loop of uncaught exceptions for multi-node cluster
* [[ONOS-6047](https://jira.onosproject.org/browse/ONOS-6047)] - VirtualNetworkManager.get does not return existing service class
* [[ONOS-6052](https://jira.onosproject.org/browse/ONOS-6052)] - Exception in DpiStatisticsListener
* [[ONOS-6066](https://jira.onosproject.org/browse/ONOS-6066)] - bug fix for openstack node module
* [[ONOS-6070](https://jira.onosproject.org/browse/ONOS-6070)] - Device which does not support MeterFeatureRequest get stuck during handshake
* [[ONOS-6081](https://jira.onosproject.org/browse/ONOS-6081)] - Resource store throws exception when queried for non-registered continuous resource
* [[ONOS-6098](https://jira.onosproject.org/browse/ONOS-6098)] - Port number used for SNAT does not return to the available port number pool after the SNAT rule expired
* [[ONOS-6106](https://jira.onosproject.org/browse/ONOS-6106)] - Adding Missing Fields in the " get flows and get devices" rest api
* [[ONOS-6114](https://jira.onosproject.org/browse/ONOS-6114)] - [ONOS-YANG-DEMO1]Issue after getting serializer registered
* [[ONOS-6118](https://jira.onosproject.org/browse/ONOS-6118)] - FlowObjective intent throughput regression
* [[ONOS-6120](https://jira.onosproject.org/browse/ONOS-6120)] - Demo1:Integration - node with demo1 namespace not found.
* [[ONOS-6147](https://jira.onosproject.org/browse/ONOS-6147)] - Demo1: Integration - GET throws an exception
* [[ONOS-6155](https://jira.onosproject.org/browse/ONOS-6155)] - issue in JSON parsing when node type is null
* [[ONOS-6156](https://jira.onosproject.org/browse/ONOS-6156)] - Issue in JSON parsing when array size is zero
* [[ONOS-6160](https://jira.onosproject.org/browse/ONOS-6160)] - Possible null pointer reference for Device object
* [[ONOS-6161](https://jira.onosproject.org/browse/ONOS-6161)] - Possible null pointer reference on portchain-list object
* [[ONOS-6172](https://jira.onosproject.org/browse/ONOS-6172)] - [ONOS-YMS-TEST] Ospf yang files is throwing error when space is present in enum.
* [[ONOS-6182](https://jira.onosproject.org/browse/ONOS-6182)] - Demo1 Integration testing: Passive component testing
* [[ONOS-6183](https://jira.onosproject.org/browse/ONOS-6183)] - NET L3VPN structure and store implementation
* [[ONOS-6191](https://jira.onosproject.org/browse/ONOS-6191)] - NET L3VPN create operation support
* [[ONOS-6195](https://jira.onosproject.org/browse/ONOS-6195)] - [ONOS\_YANG\_DEMO2] resource id for create bgp is not correct
* [[ONOS-6196](https://jira.onosproject.org/browse/ONOS-6196)] - [ONOS\_YANG\_DEMO2] Class not registered exception
* [[ONOS-6197](https://jira.onosproject.org/browse/ONOS-6197)] - [ONOS\_YANG\_DEMO2] RT value not correct for any to any
* [[ONOS-6198](https://jira.onosproject.org/browse/ONOS-6198)] - [ONOS\_YANG\_DEMO2] RT value not correct for hub and spoke
* [[ONOS-6199](https://jira.onosproject.org/browse/ONOS-6199)] - Huawei Driver implementation for device and ports discovery and L3VPN create
* [[ONOS-6210](https://jira.onosproject.org/browse/ONOS-6210)] - RemoveDevice throws IllegalStateException if device is not reachable
* [[ONOS-6211](https://jira.onosproject.org/browse/ONOS-6211)] - [ONOS\_L3VPN\_SERVICE] Accumulator and l3VPN svc delete
* [[ONOS-6229](https://jira.onosproject.org/browse/ONOS-6229)] - KShortestPathsSearch cannot find other k-paths when the shortest path is 1 hop
* [[ONOS-6239](https://jira.onosproject.org/browse/ONOS-6239)] - Flows are missing after mastership change if 'backupEnabled' is set to false
* [[ONOS-6243](https://jira.onosproject.org/browse/ONOS-6243)] - [ONOS-YANG-DEMO1]Configurations are getting configured on only one device for multiinstance case.
* [[ONOS-6244](https://jira.onosproject.org/browse/ONOS-6244)] - [ONOS-YANG-DEMO1]Device is getting disconnected and followed by time-out exception for get interface request(queried for updating port statistics)
* [[ONOS-6261](https://jira.onosproject.org/browse/ONOS-6261)] - Topo2 - Node Dragging not always working as expected
* [[ONOS-6265](https://jira.onosproject.org/browse/ONOS-6265)] - IntentManager unregister error
* [[ONOS-6269](https://jira.onosproject.org/browse/ONOS-6269)] - Variable checked for null which is not needed
* [[ONOS-6271](https://jira.onosproject.org/browse/ONOS-6271)] - Variable device dereferenced, it might be null
* [[ONOS-6275](https://jira.onosproject.org/browse/ONOS-6275)] - Topo2 - Host icon needs to be increased to match original topo
* [[ONOS-6276](https://jira.onosproject.org/browse/ONOS-6276)] - Topo2 - Port label and link highlighting not shown as expected
* [[ONOS-6277](https://jira.onosproject.org/browse/ONOS-6277)] - Topo2 - Host label should default to "unknown"
* [[ONOS-6278](https://jira.onosproject.org/browse/ONOS-6278)] - Topo2 - Host "added and updated" events don't contain ip address of the host
* [[ONOS-6279](https://jira.onosproject.org/browse/ONOS-6279)] - Topo2 - Toolbar is creating a duplicated id error
* [[ONOS-6280](https://jira.onosproject.org/browse/ONOS-6280)] - Topo2 - Hosts without lat and long cause error on click events
* [[ONOS-6282](https://jira.onosproject.org/browse/ONOS-6282)] - Topo2 - UiModel backing elements should be retrieved via service
* [[ONOS-6284](https://jira.onosproject.org/browse/ONOS-6284)] - Pointer passed to method where it is dereferened can be null
* [[ONOS-6285](https://jira.onosproject.org/browse/ONOS-6285)] - Unused variable can be deleted
* [[ONOS-6286](https://jira.onosproject.org/browse/ONOS-6286)] - metadata possible be null but not cosider
* [[ONOS-6288](https://jira.onosproject.org/browse/ONOS-6288)] - releasing wrong tunnel id. leads to null pointer exception
* [[ONOS-6291](https://jira.onosproject.org/browse/ONOS-6291)] - Topo2 - theme listener not removed when topo2 view goes out of scope.
* [[ONOS-6292](https://jira.onosproject.org/browse/ONOS-6292)] - Topo2 - Clicking on instance panel - cannot read property 'classed' error
* [[ONOS-6296](https://jira.onosproject.org/browse/ONOS-6296)] - NULL pointer dereference in GroupStore
* [[ONOS-6298](https://jira.onosproject.org/browse/ONOS-6298)] - null pointer derefeference in defaultisisInterface.java
* [[ONOS-6299](https://jira.onosproject.org/browse/ONOS-6299)] - null pointer dereference in linkConverter.java
* [[ONOS-6302](https://jira.onosproject.org/browse/ONOS-6302)] - IntentInstaller did't update flow rule
* [[ONOS-6303](https://jira.onosproject.org/browse/ONOS-6303)] - Incorrect traffic treatment from link collection intent compiler
* [[ONOS-6305](https://jira.onosproject.org/browse/ONOS-6305)] - [ONOS-YANG-DEMO1]Null pointer exception when query for netconf session in multi-instance scenario.
* [[ONOS-6307](https://jira.onosproject.org/browse/ONOS-6307)] - possible null pointer dereference in BandwidthManager
* [[ONOS-6308](https://jira.onosproject.org/browse/ONOS-6308)] - Possible null pointer exception in accessing interfaceclass in yobutils
* [[ONOS-6309](https://jira.onosproject.org/browse/ONOS-6309)] - generating null pointer exception in publish method of MQService
* [[ONOS-6310](https://jira.onosproject.org/browse/ONOS-6310)] - NPE in Protocol TL1Controller disconnectDevice
* [[ONOS-6323](https://jira.onosproject.org/browse/ONOS-6323)] - Juniper driver can generate port numbers, which can overlap
* [[ONOS-6339](https://jira.onosproject.org/browse/ONOS-6339)] - Topo2 - Duplicate region links
* [[ONOS-6347](https://jira.onosproject.org/browse/ONOS-6347)] - Topology scaling test regression
* [[ONOS-6354](https://jira.onosproject.org/browse/ONOS-6354)] - CFG values and applied values are mismatching while trying to set a property with an invalid value
* [[ONOS-6355](https://jira.onosproject.org/browse/ONOS-6355)] - incompatible string object and boolean object comparision
* [[ONOS-6356](https://jira.onosproject.org/browse/ONOS-6356)] - invalid use of bytearray toString
* [[ONOS-6370](https://jira.onosproject.org/browse/ONOS-6370)] - [ONOS\_YANG\_TOOLS]Compilation error in generated code of RPC if namespace is too lengthy
* [[ONOS-6380](https://jira.onosproject.org/browse/ONOS-6380)] - Intent performance regression
* [[ONOS-6397](https://jira.onosproject.org/browse/ONOS-6397)] - Fix incorrect filtering objective condition from Intent copmiler.
* [[ONOS-6401](https://jira.onosproject.org/browse/ONOS-6401)] - ONOS nodes timeout when trying to connect to the cluster in vm test cluster
* [[ONOS-6408](https://jira.onosproject.org/browse/ONOS-6408)] - NetconfAlarmProvider fails to parse eventTime, which contains milliseconds
* [[ONOS-6410](https://jira.onosproject.org/browse/ONOS-6410)] - Transform TargetConfig into a Identifier class, etc.
* [[ONOS-6412](https://jira.onosproject.org/browse/ONOS-6412)] - OpticalCircuitIntent leaves resource allocation behind after withdrawing
* [[ONOS-6414](https://jira.onosproject.org/browse/ONOS-6414)] - LinkManager can throw NPE when BasicLinkConfig is getting updated
* [[ONOS-6415](https://jira.onosproject.org/browse/ONOS-6415)] - NPE in Topo2Jsonifier
* [[ONOS-6421](https://jira.onosproject.org/browse/ONOS-6421)] - invalid equals(), comparing different object types
* [[ONOS-6430](https://jira.onosproject.org/browse/ONOS-6430)] - Topo2 - EdgeLink labels are still visible when hosts are hidden
* [[ONOS-6431](https://jira.onosproject.org/browse/ONOS-6431)] - Suspicious reference comparison
* [[ONOS-6432](https://jira.onosproject.org/browse/ONOS-6432)] - CheckStyle Issue fix
* [[ONOS-6433](https://jira.onosproject.org/browse/ONOS-6433)] - NPE when deactivating org.onosproject.netcfglinksprovider
* [[ONOS-6439](https://jira.onosproject.org/browse/ONOS-6439)] - Floating IP rules are not removed when it is removed without disassociation
* [[ONOS-6444](https://jira.onosproject.org/browse/ONOS-6444)] - Floating IP rules are not set when it created with fixed IP configured and no association step
* [[ONOS-6446](https://jira.onosproject.org/browse/ONOS-6446)] - ObjectiveTrackerService is not a public service
* [[ONOS-6452](https://jira.onosproject.org/browse/ONOS-6452)] - Supplied Eth type value for MPLS\_POP instruction not getting reflected in switch
* [[ONOS-6462](https://jira.onosproject.org/browse/ONOS-6462)] - Intent stuck in WITHDRAWING state with FlowObjective intent compiler
* [[ONOS-6468](https://jira.onosproject.org/browse/ONOS-6468)] - `stc smoke` test fails using updated onos-loxi
* [[ONOS-6476](https://jira.onosproject.org/browse/ONOS-6476)] - It takes 20s to install 1000 FlowObjective intents
* [[ONOS-6481](https://jira.onosproject.org/browse/ONOS-6481)] - Encapsulation intents add bandwidth allocations that don't get removed with the intent
* [[ONOS-6486](https://jira.onosproject.org/browse/ONOS-6486)] - VPLS Configurations are not distributed to the whole cluster
* [[ONOS-6488](https://jira.onosproject.org/browse/ONOS-6488)] - VPLS doesn't reinstall correctly
* [[ONOS-6492](https://jira.onosproject.org/browse/ONOS-6492)] - Consistent Map Timeout in FlowObjective intent throughput test
* [[ONOS-6493](https://jira.onosproject.org/browse/ONOS-6493)] - Any VPLS failure might affect other VPLS
* [[ONOS-6505](https://jira.onosproject.org/browse/ONOS-6505)] - Incorrect Intent id generator from VPLS Intent test
* [[ONOS-6509](https://jira.onosproject.org/browse/ONOS-6509)] - Incorrect VPLS state
* [[ONOS-6510](https://jira.onosproject.org/browse/ONOS-6510)] - In FlowObjective intent test throughput drops to 0 after 20 sec
* [[ONOS-6517](https://jira.onosproject.org/browse/ONOS-6517)] - NPE in network/configuration
* [[ONOS-6528](https://jira.onosproject.org/browse/ONOS-6528)] - VPLS app does not delete a VPLS netowrk
* [[ONOS-6595](https://jira.onosproject.org/browse/ONOS-6595)] - Allow TestON to run with non-default username/passwords

## Story

* [[ONOS-1381](https://jira.onosproject.org/browse/ONOS-1381)] - Visualize more details on optical intents in the CLI
* [[ONOS-2107](https://jira.onosproject.org/browse/ONOS-2107)] - System tests for distributed queue api
* [[ONOS-2451](https://jira.onosproject.org/browse/ONOS-2451)] - System tests for Atomic Value
* [[ONOS-4362](https://jira.onosproject.org/browse/ONOS-4362)] - Alarms for Calient
* [[ONOS-4380](https://jira.onosproject.org/browse/ONOS-4380)] - Refactor AlarmId and Alarm Class
* [[ONOS-4951](https://jira.onosproject.org/browse/ONOS-4951)] - Implement compute node delete
* [[ONOS-5182](https://jira.onosproject.org/browse/ONOS-5182)] - Refactor SONA to cache virtual network states for performance
* [[ONOS-5223](https://jira.onosproject.org/browse/ONOS-5223)] - UI for protection
* [[ONOS-5353](https://jira.onosproject.org/browse/ONOS-5353)] - Test OpenROADM service/network/device methods through RESTCONF.
* [[ONOS-5354](https://jira.onosproject.org/browse/ONOS-5354)] - Import and compile OpenROADM service/network/device models
* [[ONOS-5364](https://jira.onosproject.org/browse/ONOS-5364)] - Separate configurations for netconf and netcfg tests into separate files so they can be easily changed
* [[ONOS-5381](https://jira.onosproject.org/browse/ONOS-5381)] - Topo2 - Keyboard shortcut 'M' toggle offline devices
* [[ONOS-5383](https://jira.onosproject.org/browse/ONOS-5383)] - Topo2 - Implement the Sprite Layer
* [[ONOS-5390](https://jira.onosproject.org/browse/ONOS-5390)] - Topo2 - Implement the toolbar
* [[ONOS-5416](https://jira.onosproject.org/browse/ONOS-5416)] - Restructure onos-sample-apps
* [[ONOS-5450](https://jira.onosproject.org/browse/ONOS-5450)] - (OFAgent) Implement OFAgent manager
* [[ONOS-5451](https://jira.onosproject.org/browse/ONOS-5451)] - (OFAgent) Implement virtual switch and controller connection handler
* [[ONOS-5452](https://jira.onosproject.org/browse/ONOS-5452)] - (OFAgent) Implement OF channel pipeline and handler
* [[ONOS-5453](https://jira.onosproject.org/browse/ONOS-5453)] - (OFAgent) Implement OF message encoder and decoder
* [[ONOS-5503](https://jira.onosproject.org/browse/ONOS-5503)] - (OFAgent) Add CLIs to list, create, and remove OFAgent
* [[ONOS-5504](https://jira.onosproject.org/browse/ONOS-5504)] - (OFAgent) Add REST APIs for OFAgent service
* [[ONOS-5590](https://jira.onosproject.org/browse/ONOS-5590)] - Investigate host add latency test
* [[ONOS-5649](https://jira.onosproject.org/browse/ONOS-5649)] - (vCore) Complete tunnel operations
* [[ONOS-5667](https://jira.onosproject.org/browse/ONOS-5667)] - Device identification in ONOS NBI based on device YANG
* [[ONOS-5668](https://jira.onosproject.org/browse/ONOS-5668)] - Internal application interface definition for interaction with device
* [[ONOS-5828](https://jira.onosproject.org/browse/ONOS-5828)] - TL1 protocol should use DeviceKey service
* [[ONOS-5840](https://jira.onosproject.org/browse/ONOS-5840)] - Docker test should also pull images for released versions of ONOS
* [[ONOS-5841](https://jira.onosproject.org/browse/ONOS-5841)] - Record metrics for decisions made by Reactive Forwarding
* [[ONOS-5881](https://jira.onosproject.org/browse/ONOS-5881)] - Update WIKI about multiple gateway nodes configuration
* [[ONOS-5910](https://jira.onosproject.org/browse/ONOS-5910)] - Studying possible solution for conflicts in resource reservation
* [[ONOS-5916](https://jira.onosproject.org/browse/ONOS-5916)] - Implement mapping management application
* [[ONOS-5919](https://jira.onosproject.org/browse/ONOS-5919)] - (vCore) separate Intent store from virtual network manager
* [[ONOS-5925](https://jira.onosproject.org/browse/ONOS-5925)] - Remove deprecated optical port descriptions from code base
* [[ONOS-5932](https://jira.onosproject.org/browse/ONOS-5932)] - New FlowObjective compiler for LinkCollection Intent
* [[ONOS-5934](https://jira.onosproject.org/browse/ONOS-5934)] - Reuse meterIds
* [[ONOS-5937](https://jira.onosproject.org/browse/ONOS-5937)] - Type of Target Configuration as Enum
* [[ONOS-5957](https://jira.onosproject.org/browse/ONOS-5957)] - Enhance meter commands output
* [[ONOS-5958](https://jira.onosproject.org/browse/ONOS-5958)] - Meter Restoration
* [[ONOS-5962](https://jira.onosproject.org/browse/ONOS-5962)] - YANG Runtime: ModelConverter's createModel implementation
* [[ONOS-5963](https://jira.onosproject.org/browse/ONOS-5963)] - YANG Runtime: ModelConverter createDataNode implementation
* [[ONOS-5966](https://jira.onosproject.org/browse/ONOS-5966)] - YANG Integration: Support for YRT, Model, YC integration related defect fixes
* [[ONOS-5967](https://jira.onosproject.org/browse/ONOS-5967)] - Investigate VLAN mode support
* [[ONOS-5968](https://jira.onosproject.org/browse/ONOS-5968)] - Investigate Kubernetes + Kuryr + SONA
* [[ONOS-5969](https://jira.onosproject.org/browse/ONOS-5969)] - YANG Compiler: Testing of generated code.
* [[ONOS-5970](https://jira.onosproject.org/browse/ONOS-5970)] - Provide a method to actively sync network states with Neutron
* [[ONOS-5976](https://jira.onosproject.org/browse/ONOS-5976)] - Implement UiMessageHandler tailored to use JsonCodecs
* [[ONOS-5977](https://jira.onosproject.org/browse/ONOS-5977)] - YANG Compiler: Optimization of YANG compiler
* [[ONOS-5981](https://jira.onosproject.org/browse/ONOS-5981)] - PoC SNAT support with multiple gateway nodes
* [[ONOS-5983](https://jira.onosproject.org/browse/ONOS-5983)] - Improve gateway node setup
* [[ONOS-5984](https://jira.onosproject.org/browse/ONOS-5984)] - Improve SONA setup with containerized ONOS
* [[ONOS-5986](https://jira.onosproject.org/browse/ONOS-5986)] - Investigate data plane validation tool support
* [[ONOS-5989](https://jira.onosproject.org/browse/ONOS-5989)] - YANG based L3VPN: Provide the skeleton structure with L3SM model
* [[ONOS-5990](https://jira.onosproject.org/browse/ONOS-5990)] - YANG based L3VPN: Internal device model to be added
* [[ONOS-5997](https://jira.onosproject.org/browse/ONOS-5997)] - Select devices for which to develop alarm driver
* [[ONOS-5998](https://jira.onosproject.org/browse/ONOS-5998)] - Decide story from NTT field trial
* [[ONOS-6000](https://jira.onosproject.org/browse/ONOS-6000)] - Decide provisioning mechanism for intents
* [[ONOS-6001](https://jira.onosproject.org/browse/ONOS-6001)] - Decide on additional device drivers for the power behavior
* [[ONOS-6012](https://jira.onosproject.org/browse/ONOS-6012)] - Connect to Netconf Device via SSH Key.
* [[ONOS-6016](https://jira.onosproject.org/browse/ONOS-6016)] - Enhance IntentInstaller for FlowObjective
* [[ONOS-6018](https://jira.onosproject.org/browse/ONOS-6018)] - Netconf : Create Passive Netconf Translator
* [[ONOS-6021](https://jira.onosproject.org/browse/ONOS-6021)] - Some class of Constraints should not be used for link cost evaluation.
* [[ONOS-6022](https://jira.onosproject.org/browse/ONOS-6022)] - CLI to disable LLDP discovery
* [[ONOS-6033](https://jira.onosproject.org/browse/ONOS-6033)] - Corsa pipelines should filter the clear deferred action
* [[ONOS-6034](https://jira.onosproject.org/browse/ONOS-6034)] - Provide a method to purge and resync flow rules for the existing VMs
* [[ONOS-6039](https://jira.onosproject.org/browse/ONOS-6039)] - Remove opesntackinterface application
* [[ONOS-6043](https://jira.onosproject.org/browse/ONOS-6043)] - Allow configuration of MAX\_METERS value within FullMetersAvailable behaviour
* [[ONOS-6057](https://jira.onosproject.org/browse/ONOS-6057)] - Model converter : Object to data node conversion
* [[ONOS-6059](https://jira.onosproject.org/browse/ONOS-6059)] - Enable OpenFlow device to define FlowRuleProgrammable
* [[ONOS-6067](https://jira.onosproject.org/browse/ONOS-6067)] - Mask FlowRule sent to EDFA device
* [[ONOS-6068](https://jira.onosproject.org/browse/ONOS-6068)] - Workaround for detecting packet-layer connectivity
* [[ONOS-6071](https://jira.onosproject.org/browse/ONOS-6071)] - Color change for UI protection
* [[ONOS-6072](https://jira.onosproject.org/browse/ONOS-6072)] - DeviceDescriptionDiscovery for Lumentum ROADM
* [[ONOS-6076](https://jira.onosproject.org/browse/ONOS-6076)] - Move Device configuration portion of NETCONF/TL1 from /apps to /devices
* [[ONOS-6078](https://jira.onosproject.org/browse/ONOS-6078)] - Netconf : Active component
* [[ONOS-6079](https://jira.onosproject.org/browse/ONOS-6079)] - Netconf : Active and passive component integration
* [[ONOS-6082](https://jira.onosproject.org/browse/ONOS-6082)] - Implement missing DistributedFlowRuleStore test
* [[ONOS-6085](https://jira.onosproject.org/browse/ONOS-6085)] - Test Bandwidth allocation with intents
* [[ONOS-6086](https://jira.onosproject.org/browse/ONOS-6086)] - Increase stability in Intent Functionality tests
* [[ONOS-6088](https://jira.onosproject.org/browse/ONOS-6088)] - Investigate OF1.5 features
* [[ONOS-6090](https://jira.onosproject.org/browse/ONOS-6090)] - Investigate on several performance issues related to white paper update
* [[ONOS-6094](https://jira.onosproject.org/browse/ONOS-6094)] - Set out milestones for gRPC brigade and share on the wiki
* [[ONOS-6103](https://jira.onosproject.org/browse/ONOS-6103)] - List up SONA feature test cases
* [[ONOS-6104](https://jira.onosproject.org/browse/ONOS-6104)] - Investigate how to connect Kubernetes pod to SONA controlled OVS
* [[ONOS-6107](https://jira.onosproject.org/browse/ONOS-6107)] - Polish Region Aware Topo to be ready for Demo
* [[ONOS-6109](https://jira.onosproject.org/browse/ONOS-6109)] - Data plane wiring of rack
* [[ONOS-6111](https://jira.onosproject.org/browse/ONOS-6111)] - Investigate Jenkins Pipeliner for ONOS builds
* [[ONOS-6113](https://jira.onosproject.org/browse/ONOS-6113)] - bgp hold time expiry handling
* [[ONOS-6142](https://jira.onosproject.org/browse/ONOS-6142)] - Implement various LISP extension addresses
* [[ONOS-6150](https://jira.onosproject.org/browse/ONOS-6150)] - OpenstackNode application support creation of vlan interface on open vswitch
* [[ONOS-6153](https://jira.onosproject.org/browse/ONOS-6153)] - Refactor intent reroute test
* [[ONOS-6166](https://jira.onosproject.org/browse/ONOS-6166)] - Create SONA project on Github
* [[ONOS-6167](https://jira.onosproject.org/browse/ONOS-6167)] - Move SONA related repositories to SONA project repo
* [[ONOS-6168](https://jira.onosproject.org/browse/ONOS-6168)] - Implement multiple gateway nodes support for VLAN mode
* [[ONOS-6169](https://jira.onosproject.org/browse/ONOS-6169)] - Implement codec for mapping address extension
* [[ONOS-6170](https://jira.onosproject.org/browse/ONOS-6170)] - Implement codec for various mapping primitives
* [[ONOS-6171](https://jira.onosproject.org/browse/ONOS-6171)] - Investigate Jenkins Pipeliner jobs for ONOS system tests
* [[ONOS-6173](https://jira.onosproject.org/browse/ONOS-6173)] - Apparent Infinite loop
* [[ONOS-6179](https://jira.onosproject.org/browse/ONOS-6179)] - Virtual Network Packet Propagate Issue
* [[ONOS-6186](https://jira.onosproject.org/browse/ONOS-6186)] - Implement VLAN based virtual network provisioning and logical switching
* [[ONOS-6187](https://jira.onosproject.org/browse/ONOS-6187)] - Implement logical routing for VLAN mode
* [[ONOS-6208](https://jira.onosproject.org/browse/ONOS-6208)] - Implemention of onos and loxi for OVS NAT and connection tracking support
* [[ONOS-6212](https://jira.onosproject.org/browse/ONOS-6212)] - Packet to optical path correlation for UI
* [[ONOS-6225](https://jira.onosproject.org/browse/ONOS-6225)] - TopologyService should be able to give k-shortest path
* [[ONOS-6231](https://jira.onosproject.org/browse/ONOS-6231)] - Update SONA wiki pages with the latest changes
* [[ONOS-6235](https://jira.onosproject.org/browse/ONOS-6235)] - Implement ExtensionMappingAddressInterpreter
* [[ONOS-6236](https://jira.onosproject.org/browse/ONOS-6236)] - retry to setup connection to device when error appears on socket
* [[ONOS-6241](https://jira.onosproject.org/browse/ONOS-6241)] - (vNet) Can't find a virtual device Id
* [[ONOS-6248](https://jira.onosproject.org/browse/ONOS-6248)] - VPLS application refactoring
* [[ONOS-6253](https://jira.onosproject.org/browse/ONOS-6253)] - Add support for NETCONF device which does not support interleave feature
* [[ONOS-6254](https://jira.onosproject.org/browse/ONOS-6254)] - Submit various bug fixes and patches from ONS
* [[ONOS-6255](https://jira.onosproject.org/browse/ONOS-6255)] - Topo2 - Integrate Topo2 into Nav Menu
* [[ONOS-6263](https://jira.onosproject.org/browse/ONOS-6263)] - Topo2 - Implement link labels
* [[ONOS-6272](https://jira.onosproject.org/browse/ONOS-6272)] - Topo2 - Implement server-side filtering of model data for update events
* [[ONOS-6274](https://jira.onosproject.org/browse/ONOS-6274)] - Topo2 - Host label should be permanently shown
* [[ONOS-6281](https://jira.onosproject.org/browse/ONOS-6281)] - Topo2 - Device detail panel header should navigate to device view
* [[ONOS-6283](https://jira.onosproject.org/browse/ONOS-6283)] - Topo2 - Key command 'H' should toggle hosts and connected links
* [[ONOS-6289](https://jira.onosproject.org/browse/ONOS-6289)] - Revisit path computation in optical path provisioner
* [[ONOS-6290](https://jira.onosproject.org/browse/ONOS-6290)] - Topo2 - with no topology, show "No devices are connected" message
* [[ONOS-6293](https://jira.onosproject.org/browse/ONOS-6293)] - Topo2 - Device detail panel -- suppress blank long/lat properties
* [[ONOS-6294](https://jira.onosproject.org/browse/ONOS-6294)] - Topo2 - Summary panel / Details panel interactions...
* [[ONOS-6306](https://jira.onosproject.org/browse/ONOS-6306)] - Lambda allocation aware path computation
* [[ONOS-6315](https://jira.onosproject.org/browse/ONOS-6315)] - create gRPC northbound Port Service
* [[ONOS-6321](https://jira.onosproject.org/browse/ONOS-6321)] - NETCONF: Discuss about replacing ssh library
* [[ONOS-6328](https://jira.onosproject.org/browse/ONOS-6328)] - Topo view detail panel: suppress empty latitude/longitude
* [[ONOS-6348](https://jira.onosproject.org/browse/ONOS-6348)] - Intent Installer redesign
* [[ONOS-6349](https://jira.onosproject.org/browse/ONOS-6349)] - Add CLI for querying mapping information from MappingService
* [[ONOS-6352](https://jira.onosproject.org/browse/ONOS-6352)] - Add REST API for querying mapping information
* [[ONOS-6358](https://jira.onosproject.org/browse/ONOS-6358)] - Further improve LISP control message processing speed
* [[ONOS-6372](https://jira.onosproject.org/browse/ONOS-6372)] - Topo2 - Refactor "location" data to be consistent
* [[ONOS-6375](https://jira.onosproject.org/browse/ONOS-6375)] - Add Web GUI for mapping subsystem
* [[ONOS-6376](https://jira.onosproject.org/browse/ONOS-6376)] - Change Underlying NETCONF SSH library
* [[ONOS-6377](https://jira.onosproject.org/browse/ONOS-6377)] - Support for chuncked NETCONF 1.1 message termination
* [[ONOS-6382](https://jira.onosproject.org/browse/ONOS-6382)] - (vNet) a problem to remove virtual networks
* [[ONOS-6389](https://jira.onosproject.org/browse/ONOS-6389)] - Topo2 - wiki doc: Using netcfg to configure regions / layouts
* [[ONOS-6393](https://jira.onosproject.org/browse/ONOS-6393)] - Miscellaneous updates for Kingfisher performance white paper
* [[ONOS-6395](https://jira.onosproject.org/browse/ONOS-6395)] - (vNet) Defining mastership service interface
* [[ONOS-6398](https://jira.onosproject.org/browse/ONOS-6398)] - Investigate SDNIP test failures
* [[ONOS-6399](https://jira.onosproject.org/browse/ONOS-6399)] - Investigate VPLS test failures
* [[ONOS-6417](https://jira.onosproject.org/browse/ONOS-6417)] - YANG Tools: Generated code interfaces to be self sufficient and needn't rely on base objects
* [[ONOS-6436](https://jira.onosproject.org/browse/ONOS-6436)] - Implement VLAN based Logical Routing
* [[ONOS-6437](https://jira.onosproject.org/browse/ONOS-6437)] - List up valid Tempest API and scenario test cases for SONA
* [[ONOS-6451](https://jira.onosproject.org/browse/ONOS-6451)] - Datapath type setting function for supporting OVS DPDK addBridge
* [[ONOS-6467](https://jira.onosproject.org/browse/ONOS-6467)] - (vnet) remove tunnel operations
