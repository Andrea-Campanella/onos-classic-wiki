# Release Notes - Loon 1.11.0

# **ONOS LOON Release Notes**

# **Summary of Loon Release Content**

* Support for OpenConfig model and Live YANG compiler support in Dynamic Configuration, RESTCONF NB decoupled from YMS and using YANG Runtime, and provided a design for the Config Synchronizer
* Further stabilization of the distributed system with Atomix improvements and Flow Rule store refactor
* Initial work to support In-Service Software Upgrade by enabling multi-version object storage and messaging
* P4Runtime support on BMv2 including a PI framework, gRPC controller that can be leveraged for gNMI, and a General Device Provider
* New performance whitepaper to demonstrate ONOS maintained and improved its leading performance metrics over 12 releases
* Addition of new developer tools in the GUI, improved page loading performance, and initial work to add internationalization support.  The Applications, Cluster, and Topology views have been localized for Spanish, Italian, Korean, Traditional and Simplified Chinese
* Enhancements in Network Virtualization to add Meter Service, revised Intent Service for virtual networks, added Distributed stores for mastership and flow rules, and CLI to balance mastership roles of virtual devices, and LLDP support in OFAgent
* Enabled Eclipse support for BUCK and STC execution on the master branch
* New and improved optical intent compilers, and optical device driver support for Polatis (new), Ciena Waveserver (improved), Lumentum and Fujitsu (fixes)

# **Details of Loon Release Content**

CORE (ONF)

* Re-architected Raft implementation
  + Per-primitive sessions
  + Simplified log compaction
  + Multi-version serialization
* Performance tests added
* Fault injection/linearizability verification tests added
* New flow rule store
  + Backed by partitioned consistent primitives

ISSU (ONF)

* Multi-version object storage
* Multi-version messaging

Dynamic Configuration Brigade (Huawei, NEC, ONF)

* OpenConfig model support
* YANG RPC support
* YANG “uses” augmentation support
* YANG Live compiler
* DynamicConfig event consolidation
* RESTCONF PATCH & RPC support
* Device Synchronizer initial design

P4 Brigade (ONF, POSTECH, NCTU, Barefoot, AT&T)

* PI Framework (beta)

○      Classes to describe protocol-independent pipeline entities (tables, match fields, actions, counters, etc.)

○      Services to aid in the management of PI-enabled devices

○      Extensions to FlowRule to support PI match/actions

* P4Runtime support
* Generic gRPC controller

○      Leveragable for future gNMI service

* General Device Provider
* BMv2 driver

gRPC Brigade (ONF, ZTE, Inspur)

* First services merged
* Structure for gRPC system and naming conventions established
* Translation system improved

GUI Brigade (Villa-Tech, ONF)

* Added new developer tools for GUI development

○      NPM + Gulp

○      Linting

○      Code Coverage

○      Bundled JS and CSS

* Improved load performance by reducing the amount of requests made
* Added a few more GUI diagnostics tools, such as port filtering
* + 19% code coverage from tests
* Ported some Topology functionality to Topology 2
* Updates to the Flow View

○      Enable table column reordering

○      Show Application ID

LION Brigade (University of Alcala, ONF)

* Topology View Localized into Spanish, Italian, Korean, Traditional & Simplified Chinese

Network Virtualization Brigade (Ciena, University of Kyung Hee, POSTECH)

* Virtualization core and SB:

-  Added Meter service (Virtual network meter manager, provider service, simple meter store)

-  Revised Intent service for virtual networks

-  Added Distributed stores - mastership, flow rule

-  Added CLI to balance mastership roles for virtual devices

* OFAgent now handles LLDP and a variety of OF stats requests

Build and Package Infrastructure Brigade (Verizon, Gigamon, ONF)

* Eclipse support for BUCK - Tool to migrate IntelliJ projects to Eclipse and a tutorial to perform manual migration ( under review )
* Survey to understand category of users, gaps in BUCK etc.
* Secondary Jenkins for validation

○      Pipeline exploration

○      STC execution for master branch

Security and Performance Analysis Brigade (LIP6, Orange, Nokia, Queens University Belfast, CIT, ESME, Politecnico de Milano, ONF)

* hackathon run at RESCOM 2017
* 1st report ready, to be published before ONOS Build

QA (Ciena, ONF)

* Performance White Paper (Business Version)
* New Tests

■      HA Tests for continuous restarts of ONOS nodes

■      Mastership failover latency test

■      VPLS Failure test

■      Flow Objective Throughput test

* Refactor of Tests

○      Functional Optical tests, ONOS startup procedures in Test, VPLS tests

○      Specify number of neighbors in Intent/Flow throughput test , Scale and Performance Flow test

○      Few changes to TEST ON framework (implemented Python Debugger, New startup procedures)

○      Implemented new Cluster Class in tests (ex: FUNC,HA, SCPF, Intent, Flow, BGPLS)

○      Jenkins jobs to use pipeline

* Issues in TestON
* Investigate and fix the issues in the tests (BGPLS, Intents)
* Updated System Test wiki pages - Test Plans, Test Results, Test Guide etc
* Investigation work for implementing of new Graphs for test results

Packet/Optical (NEC, NTT, Fujitsu, Polatis, Lumentum, ONF)

* New and improved optical intent compilers
* Optical device drivers: Polatis (new), Ciena Waveserver (improved), Lumentum & Fujitsu (fixes)
* Help drive dynamic config & YANG tools

Openstack Integration (SK Telecom)

* Added REST interface for OpenStack node operations
* Added option for selecting reactive or stateful-NAT mode
* Removed use of flow objective from OpenStack networking application
* Added support of virtual network and port admin state up/down
* Added support of[OpenStack-Helm project](https://github.com/openstack/openstack-helm), Kubernetes based automated OpenStack deployment, by implementing[Helm chart for Neutron-SONA driver](https://review.openstack.org/%23/c/489500/)

LISP (POSTECH)

* Added interfaces for IP RadixTree data structure

○      Implement ConcurrentRadixTree stores IP as a key

○      Implement LispRadixTreeDatabase with unit tests

* Improve ExpireMap lookup performance with code refactoring
* Assessed the performance of ExpireMap mapping database
* Further improved the performance of MapServer and MapResolver

○      With 600,000 packets/s speed, less than 5% packet loss

# **Detailed Jira Issues - ONOS - Version 1.11.0**

## **\*\* Sub-task**

   \* [ONOS-4770] - OpenFlow 1.5 - loxigen integration

   \* [ONOS-4771] - Openflow 1.5 SBI enhancement

   \* [ONOS-6135] - Analysis : Manifest "Hello-World"

   \* [ONOS-6560] - Implement table entry handling

   \* [ONOS-6588] - Create Cluster Class

   \* [ONOS-6589] - Prototype cluster usage with HA tests

   \* [ONOS-6590] - Prototpe cluster usage with FUNCintent

   \* [ONOS-6790] - update How to Contribute page

   \* [ONOS-6791] - Update System Testing guide section

   \* [ONOS-6792] - Update CHO test plans

   \* [ONOS-6793] - Update FUNC test plans

   \* [ONOS-6794] - update HA test plans

   \* [ONOS-6795] - update SCPF test plans

   \* [ONOS-6796] - update CHO monkey documentation

   \* [ONOS-6797] - Update SAMP test plans

   \* [ONOS-6798] - Update USECASE test plans

   \* [ONOS-6814] - Prototype cluster usage with Sample test

   \* [ONOS-6843] - Add AtomicValue test commands

   \* [ONOS-6845] - Update Cluster class

   \* [ONOS-6846] - Implement cluster class to CHO tests

   \* [ONOS-6847] - Implement cluster class to FUNC tests

   \* [ONOS-6848] - Implement cluster class to HA tests

   \* [ONOS-6849] - Implement cluster class to SCPF tests

   \* [ONOS-6850] - Implement cluster class to USECASE tests

   \* [ONOS-6851] - Implement cluster class to all the other tests

   \* [ONOS-6869] - Implement blocking DocumentTree

   \* [ONOS-6870] - Refactor FlowRuleStore to use DocumentTree for persistence

   \* [ONOS-6942] - Get rid of Init jobs from Jenkins for the SCPF and let pipeline to handles the init setup.

## **\*\* Bug**

   \* [ONOS-3264] - Topo View - custom summary panel - gap needs closing

   \* [ONOS-4408] - Thrift server doesn't properly stop when Bmv2Controller is deactivated

   \* [ONOS-4446] - Performance regression bugs

   \* [ONOS-5765] - OpticalConnectivityIntentCompiler doesn't search through paths for non tunable ports

   \* [ONOS-5896] - Flow rule store can lose flows, causing links to disappear

   \* [ONOS-6084] - No statistics for flows that were posted when the device is down (or when Master=null)

   \* [ONOS-6151] - DistributedGroupStore Behavior is not inline with DistributedFlowRuleStore behavior when device Master is null

   \* [ONOS-6266] - 'garbageCollect' is not working for groups after ONOS restart

   \* [ONOS-6270] - linkWeightFunction was set as 'geoDistance', it is still using default linkWeightFunction 'hopCount' after restart

   \* [ONOS-6319] - absolute path does not work in .topo <home> for onos driver

   \* [ONOS-6331] - Flows View: expanded rows - only "selectable" from top row

   \* [ONOS-6332] - Flows: bad parsing of EXTENSION:of:0000nnnn identifier

   \* [ONOS-6333] - Missing info in flow details

   \* [ONOS-6397] - Fix incorrect filtering objective condition from Intent copmiler.

   \* [ONOS-6438] - Network creation fails with empty name field

   \* [ONOS-6446] - ObjectiveTrackerService is not a public service

   \* [ONOS-6449] - Fix arista driver and HttpSBControlllerImpl

   \* [ONOS-6468] - `stc smoke` test fails using updated onos-loxi

   \* [ONOS-6475] - DefaultSingleTablePipeline does not handle next objective with multiple treatments.

   \* [ONOS-6476] - It takes 20s to install 1000 FlowObjective intents

   \* [ONOS-6481] - Encapsulation intents add bandwidth allocations that don't get removed with the intent

   \* [ONOS-6482] - Kryo registration warnings

   \* [ONOS-6486] - VPLS Configurations are not distributed to the whole cluster

   \* [ONOS-6488] - VPLS doesn't reinstall correctly

   \* [ONOS-6489] - Per Port Flow rule installation is not happening When IN\_PORT is "ALL"

   \* [ONOS-6493] - Any VPLS failure might affect other VPLS

   \* [ONOS-6503] - Potential null value dereferenced before checking for null

   \* [ONOS-6504] - Cbench test regression

   \* [ONOS-6505] - Incorrect Intent id generator from VPLS Intent test

   \* [ONOS-6509] - Incorrect VPLS state

   \* [ONOS-6510] - In FlowObjective intent test throughput drops to 0 after 20 sec

   \* [ONOS-6516] - NullPointerExceptions during OFDPA driver testing

   \* [ONOS-6517] - NPE in network/configuration

   \* [ONOS-6519] - Supporting OVS DPDK, and PICA8 OVS interface creation & MTU setting

   \* [ONOS-6528] - VPLS app does not delete a VPLS netowrk

   \* [ONOS-6534] - Device Null Point Error is Expected

   \* [ONOS-6546] - (OFAgent) OFSwitchManager throws NullPointerException if VirtualDevice is created before ofagent is created

   \* [ONOS-6576] - Add ports discovery when OVSDB DEVICE\_ADDED event occurs

   \* [ONOS-6609] - OVSDB device is not removed properly

   \* [ONOS-6631] - Fix TestON install script

   \* [ONOS-6637] - topology config containing an array crashes net config REST POST call

   \* [ONOS-6638] - Fix Java version on onos.cshrc

   \* [ONOS-6644] - [Lion] Can't build&test with Chinese character

   \* [ONOS-6655] - [YRT] Exception is thrown when grouping is processed during model to data conversion.

   \* [ONOS-6658] - NPE while posting netcfg after deactivating Segment Routing App

   \* [ONOS-6663] - Shutdown executor in RestDeviceProvider

   \* [ONOS-6664] - NPE occurs while deactivating RestDeviceProvider

   \* [ONOS-6667] - NullPointerException on device-remove

   \* [ONOS-6675] - YANG Compiler: Augment Conflict resolution should consider namespace

   \* [ONOS-6677] - YANG Compiler: Handling of description in Pattern statement.

   \* [ONOS-6691] - YANG Compiler : Error is thrown when type-def name is same as identity-ref.

   \* [ONOS-6692] - YANG Compiler : Not able to find path for leaf-ref.

   \* [ONOS-6693] - YANG Compiler : Failed to prepare generate code for typedef node

   \* [ONOS-6694] - YANG Compiler : OpenConfig - Failing to link in augment and grouping scenario.

   \* [ONOS-6719] - TestON won't run if the test cases parameter begins with a bracket

   \* [ONOS-6768] - hosts not being discovered on ARP without net config pushed

   \* [ONOS-6772] - One of the update from onos changed the format of the getting a json format.

   \* [ONOS-6773] - The location of the onos-netcfg changed and has not been updated.

   \* [ONOS-6775] - Flow rule was not removed when remove an ingress point from MP2SP Intent

   \* [ONOS-6776] - ImmutableMap.of use error

   \* [ONOS-6782] - SDN-IP missing configuration registry

   \* [ONOS-6783] - YANG Runtime: DataTypes handling in YOB & YTB to be corrected

   \* [ONOS-6784] - YANG Runtime: Reffered types under grouping handling

   \* [ONOS-6785] - ServiceNotFoundException in ONOS shutdown

   \* [ONOS-6800] - onosNetCFG driver function should not append ".json" to the file name

   \* [ONOS-6803] - Loading cpman app breaks UI.

   \* [ONOS-6817] - PathService.getPaths() passes wrong edges to LinkWeigher.weight()

   \* [ONOS-6820] - YANG Runtime : Resource id from YTB with processed objects.

   \* [ONOS-6859] - ResourceStore opens new Raft session on each transaction

   \* [ONOS-6871] - Getting java.lang.IllegalArgumentException: Unable to resolve class [org.onosproject.net](http://org.onosproject.net).behaviour.LambdaQuery exception while activating restCiena Driver:

   \* [ONOS-6883] - Investigate FUNCintent results

   \* [ONOS-6890] - Fix the IndexError from the FUNCbgpls test

   \* [ONOS-6892] - Kryo exceptions during deserialization of large objects

   \* [ONOS-6893] - Intents get stuck in withdrawing state after link down

   \* [ONOS-6900] - Getting Java.lang.ClassCastException when injecting topology to onos using onos-netcfg

   \* [ONOS-6901] - Fix how the systemTest does not return any result when it forced to quit the test.

   \* [ONOS-6909] - Name collision with Java built-in method

   \* [ONOS-6910] - Null pointer exception in device store if stale message encountered

   \* [ONOS-6916] - Can't install flows to bmv2 with default bmv2 pipeconf

   \* [ONOS-6932] - Unable to load application org.onosproject.evpnrouteservice from disk

   \* [ONOS-6933] - Support packet request for different device scheme

   \* [ONOS-6938] - null-create-host gives error "Host should have at least one location"

   \* [ONOS-6939] - YANG Compiler : Augment linking, with self file prefix available and not-available combinations are not proper.

   \* [ONOS-6951] - YANG Compiler : Union with two identityref has file generation issue.

   \* [ONOS-6952] - support \*(asterisk) as enum name.

   \* [ONOS-6953] - show-glyphs page broken (missing TP libs)

   \* [ONOS-6954] - onos-wait-for-start wait for timeout instead of wait for START LEVEL 100

   \* [ONOS-6960] - YANG Compiler : Referred node is not searched under the sub module list of the imported/included node.

## **\*\* Story**

   \* [ONOS-2920] - Clean loxi circuit extensions

   \* [ONOS-3559] - Consistent primitive based FlowRuleStore

   \* [ONOS-4456] - BMv2 Buckification

   \* [ONOS-4769] - Openflow 1.5 Integration

   \* [ONOS-4965] - Investigate Jepsen tests for ONOS

   \* [ONOS-5222] - Design Multi-layer resource tracking

   \* [ONOS-6089] - Update ONOS performance white paper for K release

   \* [ONOS-6091] - Review and comment on gRPC design document

   \* [ONOS-6093] - Refactor existing Protocol Buffer models to be more modular

   \* [ONOS-6095] - Integrate gRPC generation and Protocol Buffer compilation with BUCK build

   \* [ONOS-6163] - (vNet) Revise virtual network intent service

   \* [ONOS-6219] - Adding script to handle dynamic cluster

   \* [ONOS-6245] - Implement Intent Mini-Summary Rest API

   \* [ONOS-6312] - create gRPC northbound Device Service

   \* [ONOS-6326] - Add friendly names to Hosts

   \* [ONOS-6327] - Hosts View should have details panel for selected host

   \* [ONOS-6334] - Flow treatments immediate vs deferred, should be clearer

   \* [ONOS-6335] - Flows view: columns should be re-ordered

   \* [ONOS-6336] - Flows View : show app name (not integer ID)

   \* [ONOS-6337] - PortStats non-zero and delta modes

   \* [ONOS-6359] - Support for embedded dependency

   \* [ONOS-6371] - (vCore) mastershipService for virtual devices

   \* [ONOS-6381] - Transactional event listeners

   \* [ONOS-6386] - Implement OF1.4 driver (Polatis)

   \* [ONOS-6390] - Topo2 - src doc: write [README.x.md](http://README.x.md) files for Topo2 (client-side) services.

   \* [ONOS-6396] - Separate per-partition per-primitive Copycat sessions

   \* [ONOS-6400] - Investigate BGP-LS test failures

   \* [ONOS-6409] - Create throughput test for FlowObjective subsystem

   \* [ONOS-6456] - Update onos-p4-dev scripts

   \* [ONOS-6457] - Update bmv2.py custom mininet script

   \* [ONOS-6463] - General Device Provider implementation

   \* [ONOS-6464] - Sketch PI core interfaces and classes

   \* [ONOS-6465] - Implement gRPC transport controller interface

   \* [ONOS-6466] - Hold P4 brigade kick-off meeting

   \* [ONOS-6496] - Implement lambda query for transponders

   \* [ONOS-6501] - WiKi: UI Service - DialogService update dialog.addButton(text, cb) is deprecated

   \* [ONOS-6512] - YANG Tools: Wiki page creation/review

   \* [ONOS-6514] - Yang Compiler/Runtime: Identifty ref support

   \* [ONOS-6521] - Add Javascript Linting tools for Javascript and define the coding standard rules

   \* [ONOS-6523] - Remove vendor packages and use a package manager

   \* [ONOS-6524] - Add code coverage tools for Javascript

   \* [ONOS-6525] - Topo2: Establish an API for overlays

   \* [ONOS-6529] - Cisco REST driver

   \* [ONOS-6531] - YANG Compiler: WebResource to support live compilation in cluster env.

   \* [ONOS-6537] - Implement RadixTree data structure

   \* [ONOS-6545] - HP3800 driver

   \* [ONOS-6552] - Implementation of PiPipelineModel classes

   \* [ONOS-6553] - Implementation of PiTableEntry classes

   \* [ONOS-6554] - Implement BMv2-JSON-to-PiPipelineModel parser

   \* [ONOS-6555] - PiPipeconf default implementation and builder

   \* [ONOS-6556] - Implementation of PiPipeconfService

   \* [ONOS-6557] - Add PiCriterion and PiInstruction builders for flow rules

   \* [ONOS-6559] - Implement P4Runtime protocol library

   \* [ONOS-6561] - Implement BMv2 Handshaker

   \* [ONOS-6562] - Implement P4RuntimePacketProvider

   \* [ONOS-6563] - Draft porting of old ecmp.p4 demo application to use new PI APIs

   \* [ONOS-6564] - Support for pipeline-specific behaviours in drivers

   \* [ONOS-6565] - Add "continuous" node restart test to HA suite

   \* [ONOS-6584] - Introduce retries for NetCfg and VPLS tests

   \* [ONOS-6587] - Introduce cluster class to TestON tests

   \* [ONOS-6591] - Buck build of P4Runtime gRPC stubs

   \* [ONOS-6592] - Implementation of ManagedChannel handling in gRPC controller

   \* [ONOS-6593] - Review and Refactor ONOS startup procedures in TestON

   \* [ONOS-6596] - Port example P4 programs from P4\_14 to P4\_16

   \* [ONOS-6604] - Translation of all criterion types in PiFlowRuleTranslationService

   \* [ONOS-6605] - First implementation of PiFlowRuleTranslationService

   \* [ONOS-6607] - Get active flow entries count in FlowRuleService

   \* [ONOS-6610] - Tests for NetconfDeviceProvider InternalDeviceListener

   \* [ONOS-6618] - Refactor FUNCoptical to use up-to-date topology

   \* [ONOS-6619] - Allow different bash prompts in TestON components

   \* [ONOS-6622] - Remove test steps that try to build using maven

   \* [ONOS-6623] - Fix parsing of hosts json

   \* [ONOS-6625] - ONOS To remove all meters from device not in line with onos view

   \* [ONOS-6626] - (OFAgent) Virtual device disconnects from external controller soon after a connection is established to the external controller.

   \* [ONOS-6628] - YANG JSON Serializer: Encode operation to prefix module name instead of namespace.

   \* [ONOS-6648] - Update p4c build script in onos-setup-p4-dev to use CMake

   \* [ONOS-6652] - Documentation updates on wiki pages for features/tests

   \* [ONOS-6653] - To provide an option in ONOS CLI to configure Group stats collection interval

   \* [ONOS-6654] - ONOS "groups" CLI command enhancement

   \* [ONOS-6656] - Topo2: Navigate to hosts page when clicking host title in details panel

   \* [ONOS-6657] - Topo2: Implement host friendly name

   \* [ONOS-6662] - Port statistics for RestDeviceProvider

   \* [ONOS-6665] - Support for "\*/\*" media type

   \* [ONOS-6670] - Add OchSignal as parameter to OpticalConnectivityIntent

   \* [ONOS-6674] - YANG Compiler: YANG Live compiler to handle JAR/ZIP and change the API.

   \* [ONOS-6681] - Port statistics discovery Cisco REST driver

   \* [ONOS-6685] - ApplicationId Protobuf model

   \* [ONOS-6686] - Version Protobuf model

   \* [ONOS-6687] - ApplicationRole Protobuf model

   \* [ONOS-6688] - Permission Protobuf model

   \* [ONOS-6697] - New HostDiscovery behavior

   \* [ONOS-6699] - ApplicationState Protobuf model

   \* [ONOS-6713] - Path Protobuf model

   \* [ONOS-6714] - DisjointPath Protobuf model

   \* [ONOS-6723] - Lion: I18n for Applications View

   \* [ONOS-6724] - Lion: I18n for Masthead

   \* [ONOS-6725] - Lion: I18n for Navigation Panel

   \* [ONOS-6726] - Lion: I18n for Quick Help panel

   \* [ONOS-6730] - Lion: I18n for Topology View

   \* [ONOS-6741] - Design support for P4 action profiles/groups

   \* [ONOS-6744] - Understand code relevant to Device Synchronizer

   \* [ONOS-6747] - VPLS test with network failures

   \* [ONOS-6750] - Implement BMv2 PacketProgrammable

   \* [ONOS-6752] - Verify FUNCintentREST test results

   \* [ONOS-6756] - Update ClusterStore to track and replicate node version information

   \* [ONOS-6757] - Setup P4 environment at ON.Lab

   \* [ONOS-6758] - Enable TLS by default for intra-cluster communication

   \* [ONOS-6760] - RestConf RPC

   \* [ONOS-6761] - RestConf PATCH support

   \* [ONOS-6764] - YANG Compiler & Runtime: Identification of YANG Model with a name.

   \* [ONOS-6769] - Update P4 demo programs to support Packet I/O via PacketMetadata

   \* [ONOS-6774] - Mechanism to unregister pipeconfs in PiPipeconfService

   \* [ONOS-6806] - Add getAvailableDeviceCount method

   \* [ONOS-6809] - Add support for Packets and Packet Metadata, also in PiPipelineInterpreter

   \* [ONOS-6812] - YANG Compiler: Adaption to new RPC mechanism

   \* [ONOS-6813] - Implement Python Debugger (pdb) in the TestON Framework

   \* [ONOS-6815] - Prepare Performance White Paper (Business version) (use KingFisher Release) , Part-1

   \* [ONOS-6816] - Prepare Business Performance White Paper (KingFisher) Part -2

   \* [ONOS-6819] - Update TestON file headers

   \* [ONOS-6823] - Create performance test to measure control plane failure recovery latency

   \* [ONOS-6824] - Unit tests for Translation of all criterion types in PiFlowRuleTranslationService

   \* [ONOS-6832] - Read from local cache of the ConsistentMap

   \* [ONOS-6833] - UiPreferencesService: augment to include getPreferences(username, prefsKey)

   \* [ONOS-6835] - Dynamic Config: RPC dispatcher implementation

   \* [ONOS-6841] - Distributed primitive throughput tests

   \* [ONOS-6842] - Distributed primitive linearizability verification

   \* [ONOS-6844] - Investigate pushing ports via net-cfg

   \* [ONOS-6853] - Servers for P4 test environment

   \* [ONOS-6854] - Refactor bmv2-demo.py mininet script to work with new P4Runtime-based environment

   \* [ONOS-6857] - Testing of Packet I/O handling via PacketMetadata

   \* [ONOS-6862] - SCPFflowTp1g test refactor

   \* [ONOS-6863] - Flexible way to specify number of neighbors in intent/flow throughput test

   \* [ONOS-6865] - Enforcing same label along a path

   \* [ONOS-6866] - Pipeconf implementation for ecmp.p4

   \* [ONOS-6868] - Netty messaging protocol inefficiencies

   \* [ONOS-6874] - Implement nullable consistent map

   \* [ONOS-6875] - Partitions command is broken

   \* [ONOS-6884] - ResourceId related modification to deal with relative ResourceId

   \* [ONOS-6888] - Move .net.routing from incubator to apps

   \* [ONOS-6894] - ItemNotFoundException when looking up device driver

   \* [ONOS-6895] - Implement min swap behavior

   \* [ONOS-6904] - Add ecmp to default.p4

   \* [ONOS-6905] - Adjust the number of retrying and sleep time to the FUNCintent.

   \* [ONOS-6907] - Enable and debug ONOS up/down events in CHOTestMonkey

   \* [ONOS-6911] - Bring SCPFmastershipFailoverLat test online

   \* [ONOS-6917] - Adding more features to the TestON

   \* [ONOS-6918] - Investigate on unstable results from switch down latency test

   \* [ONOS-6920] - Bring FlowObjective throughput test online

   \* [ONOS-6936] - Create table for the database and connect it to the test/wiki page for SCPFmastershipFailover test.

   \* [ONOS-6947] - Make 1.11 version for the wiki and Jenkins.
