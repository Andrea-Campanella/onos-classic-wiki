# Release notes - Falcon 1.5.0

# Falcon Release

Version: 1.5.0 

Release Date: March, 10th, 2016

Download [here](../redirect-pages-not-in-main-menu/download-packages-and-tutorial-vms.md)

---

## Release Content

### Deployments

* ONOS running production traffic in AmLight
* L2/L3 SDX ONOS app and ONOS deployment in AARNET with CSIRO
* ONOS/SDN-IP has been deployed in KREONET with KISTI
* SDN-IP and SDX-L2 deployed in GEANT with CNIT collaboration
* New link between GEANT (Prague - EU) and AmLight (Sao Paulo - BRA)
* Deployed VPLS on AMLight, together with SDN-IP
* New link between AmLight and KREONET
* ONOS deployment in Taiwan - NCTU

+ Connection between AmLight and Taiwan
+ Connection between Taiwan and KREONET

* ONOS deployment in EU with GARR
* Connection between KREONET and AmLight

### Distribution Support

* ONF and ON.Lab have completed the integration of ONOS into the 2nd release of Atrium (<https://github.com/onfsdn/atrium-docs/wiki>).
* Huawei completed the integration of ONOS into OPNFV Brahmaputra

+ Additional OpenStack routing and switching support
+ Extended SFC with load balancing feature and enhancements to SFC bundling within the VTN application
+ to store multiple similar SFs within a SF group and using this information for load balancing within the SFs.

* Installers, testing
* SONA improvements from SK Telecom and ATTO

+ L3 Routing feature  (Router, pNAT, Floating IP, ICMP Handler)
+ SecurityGroup feature of Openstack

### Security Mode ONOS

* KAIST has added automatic application security policy extraction that uses static analysis techniques

### Applications

* VPLS application - allows creation of multi-point broadcast overlay networks based on VLAN. A fundamental need for most research and education networks
* Initial release of Yang to Java translator by Huawei: YANG is a data modeling language used to model configuration & state data. YANG is  a one way to represent the interface and behavior semantics (of device/controller/component). The YANG modeled interfaces need to be implemented by corresponding application / component. There are 2 parts in implementing the interface: a) the syntax/symantics processing of the request/response being exchanged. b) the business logic to compute the request. This feature abstracts the applications from syntatical processing of information encoding with the external world. It provides a framework in which the applications only need to implement the business logic. It seamlessly supports any interface language like REST, NETCONF etc. YANG Utils which is a basic building block to achieve this goal is developed as a part F release. These UTILS provide following:

+ 1) Abstracting Syntax information from model.
+ 2) Translator tool for auto-generation of JAVA corresponding to a given YANG.
+ 3) Metadata Generation (Input for NBI & SBI Automation)

* FNLab/BUPT troubleshooting application

+ Routing Loop Detection
+ Routing Blackhole Tracking

* POSTECH provided

+ RRD based MetricsDatabase. This is a round robin database (RRD) stores various metric values. The database stores daily data points, and granularity is up to 1 minute.
+ Control metrics monitoring service. This service is for monitoring various control metrics that include control message, CPU load, memory usage, disk I/O, etc.

* Huawei contributed a BGP Flowspec implementation: BGP Flow specification specifies procedures for the distribution of flow specification rules via BGP and defines the procedure to encode flow specification rules as BGP NLRI which can be used in any application. BGP flow specification feature is required to handle  scenarios such as

+ Packet filtering in order to mitigate (distributed) denial of service attacks.
+ Network optimization  by applying flow rule with various flow types.

A REST interface is implemented to push flow specification rules to networking devices using the BGP ONOS southbound interface. Flow specification rules support multi-value flow types with logical conditions as specified in RFC 5575.

* Create-Net and TATA collaboration on ONOS peering improvements

### GUI/CLI

* UI introduction video
* Augmented TableModel with annotations
* Secondary sort capability in tables
* Meter table GUI view
* Driver Matrix view (drivers vs. behaviours) to help visualize supported device control capabilities.
* Topology View:

+ “Reset Node Locations” command (‘X’ keystroke) added
+ Topology Overlay selection with F1, F2, F3… keystrokes

* Application View:

+ Confirmation dialog added for application activate/deactivate/uninstall
+ Application Model enhancements supported

- columns added for additional application attributes
- details panel displayed when application row selected

+ applications can now define custom icon and URL for documentation

* Dialog Service:

+ Enter and Escape keys bound to OK and Cancel buttons

* POSTECH provided

+ Extended application properties for supporting customized icon in application view. This feature extends application properties to have URL, category, icon, long description, etc. With this feature, application developers can customize their own application icons.
+ Augmented table model for supporting annotation. This feature augments table model properties, allow web developer to specify various meta information of table model as a form of annotation.

### Northbound Interface

* New REST APIs for GroupTable, MeterTable, FlowObjectives from POSTECH
* Intents: Fujitsu provide Resource reservation support for “continuous” resources (bandwidth)
* Intents subsystem integrated with Flow Objectives (partial, not all intent types)

### Core

* dynamic cluster scaling
* enhancements making it easier to add new distributed primitives
* from Ciena, the device key subsystem, and integration of the device key id into the BasicDeviceConfig
* Added ability to dynamically extend the core data model and allow alternate projections of core topology entities, e.g. devices, ports, links, hosts.
* Support for more context when looking at state change notifications
* From POSTECH: Control message subsystem which provides control message statistics that includes number of control packet, message volume, etc.
* Introduced Regions as a basis for controlling affinity of controller nodes to geographical regions and for upcoming topology view enhancements.
* Introduced device key subsystem to allow coordinated management of keys (SSL, user/password, community-name) required for securing control interactions with network devices.

### Southbound Interface

* Huawei and Cognizant implemented OSPF southbound protocol support. Plug-in collects the topology information of the legacy network. This topology information can be used by other applications like PCE. Major features supported are OSPFv2 specification (RFC 2328),  and the OSPF Traffic Engineering (TE) extension (RFC3630)
* OSPF SBI is also integrated to the IP Topology (same as BGP-LS).
* REST southbound support

+ Protocol and provider to discover and configure devices that provide REST interaction capability
+ Support for REST CRUD operations and non-standard PATCH operation
+ HTTP and HTTPS protocol capabilities, with and without password login

* SNMP provider from BTI
* Drivers folder has been significantly redesigned

+ each driver family has his own module and is treated as an ONOS app.
+ drivers can be dynamically loaded on an as-needed basis. apps="org.onosproject.drivers.netconf" in app.xml
+ default drivers is now the default folder but the module maintains onos-drivers artifact-id for retro-compatibility
+ base for future separation from base-drivers and device-family specific drivers.

* Driver based fallback providers making deployment much easier
* Device provider testing for OPLink (OpenFlow), Ciena (REST), Fujitsu (NETCONF), Lumentum (SNMP)
* Multiple inheritance between drivers
* OVSDB now supports setting and deleting a port on a specific bridge.
* Multicast support for CORD from DirecTV
* NETCONF improvements

+ device’s session stream handling: allows device notification and listeners for events
+ Async communication is supported via usage of Completable Future based on request and reply messageID
+ Abstracted communication with device in separate thread
+ Capability to listen for device generated messages and events ( like alarms, notifications ).
+ Added Capability to provision ports for a device via a behavior in the provider.

* Improved IPv6 test suite from Criterion Networks
* Improved NETCONF test suite from Happiest Minds

### PoC and Field Trial Support

#### Residential CORD

* ONS demo support (infrastructure development, application development, software and hardware integration by AT&T, Ciena, Accton/Edge-Core, Akamai, Broadcom, Celestica, ONF, PMC Sierra, Tech Mahindra) - full details to be announced and demonstrated at ONS

#### Mobile CORD

* ONS demo support (infrastructure development, application development, software and hardware integration by AT&T, SK Telecom, Verizon, Radisys, Cavium, NEC/NetCracker, AirHop, Cobham Wireless) - full details to be announced and demonstrated at ONS

#### Enterprise CORD

* ONS demo support (infrastructure development, application development, software and hardware integration by NTT, Calient, Cavium, Ciena, Fujitsu, Huawei, Lumentum, NEC, Oplink ) - full details to be announced and demonstrated at ONS

#### CORD Analytics

* ONS demo support (infrastructure development, application development, software and hardware integration by AT&T, Ericsson) - full details to be announced and demonstrated at ONS, but here are some highlights

+ Openstack Ceilometer as a scalable, multi-tenant service in XOS
+ Support for Kafka and UDP based Publish/Subscribe interface over Openstack Ceilometer in addition to existing Query based interface
+ "sFlow Collection" as a scalable, multi-tenant service in XOS
+ Service level metrics and event collection for CORD services such as vSG, vOLT and ONOS
+ Analytic applications such as "XOS Monitoring dashboard",  "XOS-service-auto-scale" and “XOS Residential Subscriber Troubleshooting Portal” are implemented on top of this XOS monitoring platform
+ InMon Corp's sFlow analytics applications are verified on top of this platform
+ Integration of XOS monitoring platform with real time analytics applications from 3rd party vendors is targeted for Open Networking Summit 2016

### Other PoCs

* NTT Communications, China Unicom, AT&T, Huawei, Fujitsu NEC, Adara have been contributing toward IP-Optical and transport SDN use cases.

### Test Improvements

* Production testbed: qualified new Karaf and Maven version
* Continuous Hours of Operation: Improvements to robustness of tests
* HA testbed improvements

### Other ONS demos

* China Unicom has been active with preparing with partners and collaborators in several demonstrations for ONS.

## 

---

## Complete Listing of features and bugs resolved

* [[ONOS-902](https://jira.onosproject.org/browse/ONOS-902)] - Write TestON Test for split brain scenario
* [[ONOS-1302](https://jira.onosproject.org/browse/ONOS-1302)] - Provider a onlab-utils utility class that serves our share java.util.Timer, single Executor or poolExecutor
* [[ONOS-2302](https://jira.onosproject.org/browse/ONOS-2302)] - Bring up SCPFmaxIntent test
* [[ONOS-2496](https://jira.onosproject.org/browse/ONOS-2496)] - FUNCintent test add end point failure "multiple to single intent" case
* [[ONOS-2738](https://jira.onosproject.org/browse/ONOS-2738)] - Basic Framework for OSPF
* [[ONOS-2739](https://jira.onosproject.org/browse/ONOS-2739)] - OSPF Packet Processing
* [[ONOS-2740](https://jira.onosproject.org/browse/ONOS-2740)] - ONOS-OSPF neighbor FSM as defined in RFC2328
* [[ONOS-2741](https://jira.onosproject.org/browse/ONOS-2741)] - ONOS-OSPF interface FSM for point-to-point networks as defined in RFC2328.
* [[ONOS-3030](https://jira.onosproject.org/browse/ONOS-3030)] - Basic Framework - OSPF Device Provider implementation
* [[ONOS-3031](https://jira.onosproject.org/browse/ONOS-3031)] - Basic Framework - OSPF Link Provider implementation
* [[ONOS-3032](https://jira.onosproject.org/browse/ONOS-3032)] - Packet Processing - Sending OSPF Hello Packets in point-to-point networks
* [[ONOS-3033](https://jira.onosproject.org/browse/ONOS-3033)] - Packet Processing - Receiving OSPF Hello Packets in point-to-point networks
* [[ONOS-3034](https://jira.onosproject.org/browse/ONOS-3034)] - Packet Processing - Sending OSPF Hello Packets in broadcast networks
* [[ONOS-3035](https://jira.onosproject.org/browse/ONOS-3035)] - Packet Processing - Receiving OSPF Hello Packets in broadcast networks
* [[ONOS-3036](https://jira.onosproject.org/browse/ONOS-3036)] - Data structure definitions for LSDB, Neighbor and Interface parameters
* [[ONOS-3037](https://jira.onosproject.org/browse/ONOS-3037)] - Storing OSPF Type1 LSA
* [[ONOS-3038](https://jira.onosproject.org/browse/ONOS-3038)] - Storing OSPFType2 LSA
* [[ONOS-3039](https://jira.onosproject.org/browse/ONOS-3039)] - Storing OSPF Type3 LSA
* [[ONOS-3040](https://jira.onosproject.org/browse/ONOS-3040)] - Storing OSPF Type4 LSA
* [[ONOS-3041](https://jira.onosproject.org/browse/ONOS-3041)] - Storing OSPF Type5 LSA
* [[ONOS-3042](https://jira.onosproject.org/browse/ONOS-3042)] - ONOS-OSPF interface FSM for broadcast networks as defined in RFC2328.
* [[ONOS-3043](https://jira.onosproject.org/browse/ONOS-3043)] - OSPF Timers – Single Shot Timers and Interval Timers implementation as per RFC - 2328
* [[ONOS-3044](https://jira.onosproject.org/browse/ONOS-3044)] - Packet Processing - Receiving OSPF DD Packets
* [[ONOS-3045](https://jira.onosproject.org/browse/ONOS-3045)] - Packet Processing - Receiving OSPF LS Request Packet
* [[ONOS-3046](https://jira.onosproject.org/browse/ONOS-3046)] - Packet Processing - Receiving OSPF LS Update Packet
* [[ONOS-3047](https://jira.onosproject.org/browse/ONOS-3047)] - Packet Processing - Receiving OSPF LS Acknowledge Packet
* [[ONOS-3048](https://jira.onosproject.org/browse/ONOS-3048)] - Packet Processing - Sending OSPF DD Packets
* [[ONOS-3049](https://jira.onosproject.org/browse/ONOS-3049)] - Packet Processing - Sending OSPF LS Request Packet
* [[ONOS-3050](https://jira.onosproject.org/browse/ONOS-3050)] - Packet Processing - Sending OSPF LS Update Packet
* [[ONOS-3051](https://jira.onosproject.org/browse/ONOS-3051)] - Packet Processing - Sending OSPF LS Acknowledge Packet
* [[ONOS-3052](https://jira.onosproject.org/browse/ONOS-3052)] - APIs for Config and Display for learning OSPF LSA(All types of LSAs)
* [[ONOS-3053](https://jira.onosproject.org/browse/ONOS-3053)] - Configuration of OSPF Interface parameters
* [[ONOS-3054](https://jira.onosproject.org/browse/ONOS-3054)] - Display APIs for OSPF LSDB
* [[ONOS-3055](https://jira.onosproject.org/browse/ONOS-3055)] - OSPF LSA Generation - Router LSA Generation
* [[ONOS-3056](https://jira.onosproject.org/browse/ONOS-3056)] - OSPF LSA Generation - Network LSA Generation
* [[ONOS-3057](https://jira.onosproject.org/browse/ONOS-3057)] - OSPF DR functionality implementation
* [[ONOS-3058](https://jira.onosproject.org/browse/ONOS-3058)] - OSPF DR/BDR Election process implementation
* [[ONOS-3059](https://jira.onosproject.org/browse/ONOS-3059)] - OSPF LSA Flooding - LSRefresh timer expiry
* [[ONOS-3060](https://jira.onosproject.org/browse/ONOS-3060)] - OSPF LSA Flooding - Update in Link State
* [[ONOS-3061](https://jira.onosproject.org/browse/ONOS-3061)] - OSPF LSA Flooding - MaxAge timer expiry
* [[ONOS-3062](https://jira.onosproject.org/browse/ONOS-3062)] - OSPF LSA Flooding - Receiving of self-originated LSA
* [[ONOS-3063](https://jira.onosproject.org/browse/ONOS-3063)] - API for configuration of OSPF LSA generation
* [[ONOS-3064](https://jira.onosproject.org/browse/ONOS-3064)] - Storing OSPF Type9 Opaque LSA
* [[ONOS-3065](https://jira.onosproject.org/browse/ONOS-3065)] - Storing OSPF Type10 Opaque LSA
* [[ONOS-3066](https://jira.onosproject.org/browse/ONOS-3066)] - Storing OSPF Type11 Opaque LSA
* [[ONOS-3067](https://jira.onosproject.org/browse/ONOS-3067)] - Modification of OSPF Neighbor FSM for Opaque LSA handling
* [[ONOS-3068](https://jira.onosproject.org/browse/ONOS-3068)] - Storing OSPF TEDB information
* [[ONOS-3069](https://jira.onosproject.org/browse/ONOS-3069)] - Modification of OSPF LSDB Display API for including TEDB
* [[ONOS-3070](https://jira.onosproject.org/browse/ONOS-3070)] - Multiple OSPF Area Handling - Listening/storing of LSA information for multiple areas
* [[ONOS-3071](https://jira.onosproject.org/browse/ONOS-3071)] - Configuration support for Multiple OSPF Areas
* [[ONOS-3072](https://jira.onosproject.org/browse/ONOS-3072)] - SIT for OSPF point-to-point network
* [[ONOS-3073](https://jira.onosproject.org/browse/ONOS-3073)] - SIT for OSPF broadcast network
* [[ONOS-3074](https://jira.onosproject.org/browse/ONOS-3074)] - SIT for OSPF LSA generation
* [[ONOS-3075](https://jira.onosproject.org/browse/ONOS-3075)] - SIT for OSPF LSA Flooding
* [[ONOS-3076](https://jira.onosproject.org/browse/ONOS-3076)] - SIT for OSPF DR Functionality
* [[ONOS-3077](https://jira.onosproject.org/browse/ONOS-3077)] - SIT for OSPF Opaque LSA
* [[ONOS-3078](https://jira.onosproject.org/browse/ONOS-3078)] - SIT for Multiple OSPF Area Support
* [[ONOS-3103](https://jira.onosproject.org/browse/ONOS-3103)] - automated balance-masters app
* [[ONOS-3522](https://jira.onosproject.org/browse/ONOS-3522)] - SM-ONOS: Implement cache to store permission checks
* [[ONOS-3536](https://jira.onosproject.org/browse/ONOS-3536)] - Implement back-end metrics saving logic using RRD
* [[ONOS-3648](https://jira.onosproject.org/browse/ONOS-3648)] - Implement REST API for collecting system metrics
* [[ONOS-3657](https://jira.onosproject.org/browse/ONOS-3657)] - Update classes and description for listener patch
* [[ONOS-3663](https://jira.onosproject.org/browse/ONOS-3663)] - Implement REST API for control plane monitor
* [[ONOS-3706](https://jira.onosproject.org/browse/ONOS-3706)] - Install YAML plugin for jenkins
* [[ONOS-3729](https://jira.onosproject.org/browse/ONOS-3729)] - Bring up SCPFscaleTopo test
* [[ONOS-3754](https://jira.onosproject.org/browse/ONOS-3754)] - Create driver/behavior for Ciena waveserver
* [[ONOS-3860](https://jira.onosproject.org/browse/ONOS-3860)] - manual evacuate & rollback command
* [[ONOS-3941](https://jira.onosproject.org/browse/ONOS-3941)] - Test current portDiscovery Behavior with physical device
* [[ONOS-3989](https://jira.onosproject.org/browse/ONOS-3989)] - Simplify SDNIP/FSFW test to 1~2min demo suite
* [[ONOS-3990](https://jira.onosproject.org/browse/ONOS-3990)] - create S3 slidesshow
* [[ONOS-3992](https://jira.onosproject.org/browse/ONOS-3992)] - create TestON architecture poster
* [[ONOS-3993](https://jira.onosproject.org/browse/ONOS-3993)] - create screencast video for the demo

## Bug

* [[ONOS-1632](https://jira.onosproject.org/browse/ONOS-1632)] - Exception creating an optical intent
* [[ONOS-1770](https://jira.onosproject.org/browse/ONOS-1770)] - Distributed set's toArray() does not support resizing to a larger array if the given one is too small
* [[ONOS-1887](https://jira.onosproject.org/browse/ONOS-1887)] - Inconsistent Device view in the ONOS CLI
* [[ONOS-1888](https://jira.onosproject.org/browse/ONOS-1888)] - Inconsistent Device display in ONOS GUI
* [[ONOS-2060](https://jira.onosproject.org/browse/ONOS-2060)] - Web UI - App View should not disable drivers
* [[ONOS-2470](https://jira.onosproject.org/browse/ONOS-2470)] - Moving an host manually in the GUI always has priority on the JSON file pushed
* [[ONOS-2497](https://jira.onosproject.org/browse/ONOS-2497)] - Coordinate between events for the identical failed p2p/h2h intent and optical path setup
* [[ONOS-2517](https://jira.onosproject.org/browse/ONOS-2517)] - Latch was already 0 before counting down?
* [[ONOS-2967](https://jira.onosproject.org/browse/ONOS-2967)] - ONOS jenkins goes intermittently out of disc-space
* [[ONOS-3079](https://jira.onosproject.org/browse/ONOS-3079)] - Link Resource Manager - problems in simultaneous requests for allocate/release of resources
* [[ONOS-3425](https://jira.onosproject.org/browse/ONOS-3425)] - Phantom links get discovered between CPqD switch and OVS using metro.py
* [[ONOS-3519](https://jira.onosproject.org/browse/ONOS-3519)] - ONOS maven doesn't create .OAR file
* [[ONOS-3539](https://jira.onosproject.org/browse/ONOS-3539)] - Topology View Highlighting - failed to correctly highlight incoming link
* [[ONOS-3553](https://jira.onosproject.org/browse/ONOS-3553)] - bin/onos-server does not start ONOS correctly if /opt/onos exists
* [[ONOS-3564](https://jira.onosproject.org/browse/ONOS-3564)] - Cannot ping IPv6 hosts using the fwd app
* [[ONOS-3620](https://jira.onosproject.org/browse/ONOS-3620)] - Current LambdaQuery implementation incorrectly classifies the port type.
* [[ONOS-3630](https://jira.onosproject.org/browse/ONOS-3630)] - Table sorting of packet count and byte count in the flow view does not work
* [[ONOS-3651](https://jira.onosproject.org/browse/ONOS-3651)] - NPEs on node restart
* [[ONOS-3659](https://jira.onosproject.org/browse/ONOS-3659)] - Submit the modified content of onos-1.4 to onos-master.
* [[ONOS-3664](https://jira.onosproject.org/browse/ONOS-3664)] - Update the bug: the ports command for restful can not get external port.
* [[ONOS-3721](https://jira.onosproject.org/browse/ONOS-3721)] - [Not Reproducible] Build Failure for sample application on 1.5.0-SNAPSHOT
* [[ONOS-3724](https://jira.onosproject.org/browse/ONOS-3724)] - Cbench regression, throughput halved
* [[ONOS-3725](https://jira.onosproject.org/browse/ONOS-3725)] - Pushing configuration through REST-API throws an exception if the corresponding application is not loaded
* [[ONOS-3726](https://jira.onosproject.org/browse/ONOS-3726)] - Update L3's bug about deleting router interface and unbind floating ip.
* [[ONOS-3743](https://jira.onosproject.org/browse/ONOS-3743)] - endpattern no added to doRpc in NetconfSessionImpl
* [[ONOS-3752](https://jira.onosproject.org/browse/ONOS-3752)] - configuration JSON is not applied for big switch app
* [[ONOS-3763](https://jira.onosproject.org/browse/ONOS-3763)] - ADDED flows are not changed back to PENDING\_ADD when missing from flow stat
* [[ONOS-3777](https://jira.onosproject.org/browse/ONOS-3777)] - Using "push-test-intents" with large batch may cause flows to not installed correctly
* [[ONOS-3786](https://jira.onosproject.org/browse/ONOS-3786)] - Error while creating port in ovs using ovsdb due to bug in addPort method of OvsdbBridgeConfig
* [[ONOS-3788](https://jira.onosproject.org/browse/ONOS-3788)] - Update floatingip's bug.
* [[ONOS-3792](https://jira.onosproject.org/browse/ONOS-3792)] - onos 1.5.0-SNAPSHOT meter rest api problem
* [[ONOS-3827](https://jira.onosproject.org/browse/ONOS-3827)] - Resource subsystem: Cannot unregister resource
* [[ONOS-3829](https://jira.onosproject.org/browse/ONOS-3829)] - Drivers are not merged correctly
* [[ONOS-3839](https://jira.onosproject.org/browse/ONOS-3839)] - Frozen device-setconfiguration command
* [[ONOS-3841](https://jira.onosproject.org/browse/ONOS-3841)] - ResourceNetworkConfigListener throws ClassCastException
* [[ONOS-3861](https://jira.onosproject.org/browse/ONOS-3861)] - Errors to add connected switch during ONOS restart
* [[ONOS-3862](https://jira.onosproject.org/browse/ONOS-3862)] - NPE on openstackswitching when restart ONOS with existing VMs
* [[ONOS-3865](https://jira.onosproject.org/browse/ONOS-3865)] - ClassCastException on openstackSwitching when new switch added
* [[ONOS-3867](https://jira.onosproject.org/browse/ONOS-3867)] - Switches are often detached due to class casting error
* [[ONOS-3869](https://jira.onosproject.org/browse/ONOS-3869)] - Allocation of resources takes from 2 to 5 minutes
* [[ONOS-3918](https://jira.onosproject.org/browse/ONOS-3918)] - rpc-reply with error fails to complete future when message-di is absent
* [[ONOS-3922](https://jira.onosproject.org/browse/ONOS-3922)] - Topology View: Problem with Host-Links
* [[ONOS-3923](https://jira.onosproject.org/browse/ONOS-3923)] - Intent Event TP test overall rate drop down to 1500, and decreased to 300
* [[ONOS-3996](https://jira.onosproject.org/browse/ONOS-3996)] - I get very long ConsistentResourceStore warning sometimes
* [[ONOS-4000](https://jira.onosproject.org/browse/ONOS-4000)] - Removal of blank spaces from NETCONF replies
* [[ONOS-4001](https://jira.onosproject.org/browse/ONOS-4001)] - GUI not showing links activated by netcfg
* [[ONOS-4006](https://jira.onosproject.org/browse/ONOS-4006)] - Intent State inconsistent among nodes in the cluster
* [[ONOS-4007](https://jira.onosproject.org/browse/ONOS-4007)] - remove-intent does not work with a key
* [[ONOS-4012](https://jira.onosproject.org/browse/ONOS-4012)] - Host discovered on wrong location
* [[ONOS-4032](https://jira.onosproject.org/browse/ONOS-4032)] - Bandwidth registration failed on boot
* [[ONOS-4033](https://jira.onosproject.org/browse/ONOS-4033)] - Criterion decoder codec crashes if ethType not specified
* [[ONOS-4043](https://jira.onosproject.org/browse/ONOS-4043)] - Intent-perf test caught Null pointer exception
* [[ONOS-4114](https://jira.onosproject.org/browse/ONOS-4114)] - Swagger documentation for Flow POST REST API is incorrect.
* [[ONOS-4116](https://jira.onosproject.org/browse/ONOS-4116)] - onos-uninstall causing errors on running cluster
* [[ONOS-4117](https://jira.onosproject.org/browse/ONOS-4117)] - ONOS process will no longer respawn when killed
* [[ONOS-4121](https://jira.onosproject.org/browse/ONOS-4121)] - "hello" causes incorrect message id's
* [[ONOS-4124](https://jira.onosproject.org/browse/ONOS-4124)] - onos-install doesn't start onos properly on upstart-based distributions
* [[ONOS-4129](https://jira.onosproject.org/browse/ONOS-4129)] - Network Config Store does not process pending config properly
* [[ONOS-4144](https://jira.onosproject.org/browse/ONOS-4144)] - Checkstyle error found in generated code for yang file.
* [[ONOS-4145](https://jira.onosproject.org/browse/ONOS-4145)] - For a Yang construct which is not having any other yang construct as sub attributes code was not generated
* [[ONOS-4151](https://jira.onosproject.org/browse/ONOS-4151)] - ONOS has incorrect OVS driver when running on BM
* [[ONOS-4196](https://jira.onosproject.org/browse/ONOS-4196)] - java.lang.illegalArgumentException is thrown when nodes are synchronized.
* [[ONOS-4263](https://jira.onosproject.org/browse/ONOS-4263)] - Java files are not generated when building from higher
* [[ONOS-4269](https://jira.onosproject.org/browse/ONOS-4269)] - Java files are generated when duplicate container exists in same yang.
* [[ONOS-4371](https://jira.onosproject.org/browse/ONOS-4371)] - Netconf client could not resolve notification message with label attributes
* [[ONOS-4492](https://jira.onosproject.org/browse/ONOS-4492)] - vrouter and floatingip can not be synchronized between multiple instances
* [[ONOS-4559](https://jira.onosproject.org/browse/ONOS-4559)] - Linker error: Unable to process the derived type

## Epic

* [[ONOS-2737](https://jira.onosproject.org/browse/ONOS-2737)] - OSPF as SBI in ONOS
* [[ONOS-3665](https://jira.onosproject.org/browse/ONOS-3665)] - Implement YANG Framework in ONOS
* [[ONOS-4190](https://jira.onosproject.org/browse/ONOS-4190)] - Add the gui of service function chain.

## Story

* [[ONOS-401](https://jira.onosproject.org/browse/ONOS-401)] - MetricsListCommand: add parameters
* [[ONOS-418](https://jira.onosproject.org/browse/ONOS-418)] - GossipLinkStore: make configurable
* [[ONOS-420](https://jira.onosproject.org/browse/ONOS-420)] - OpenFlowDeviceProviderTest: Implement trigger probe test.
* [[ONOS-899](https://jira.onosproject.org/browse/ONOS-899)] - HA Test - Split Brain scenario
* [[ONOS-1305](https://jira.onosproject.org/browse/ONOS-1305)] - Shared system timer and executor services - monitoring
* [[ONOS-2059](https://jira.onosproject.org/browse/ONOS-2059)] - OCh port availability is not tracked properly
* [[ONOS-2225](https://jira.onosproject.org/browse/ONOS-2225)] - Implement REST API for Flow Objectives
* [[ONOS-2476](https://jira.onosproject.org/browse/ONOS-2476)] - Circuit intent support for ODU Multiplexing
* [[ONOS-2565](https://jira.onosproject.org/browse/ONOS-2565)] - Log report function in onos driver does not report error properly needs refactor
* [[ONOS-2696](https://jira.onosproject.org/browse/ONOS-2696)] - Support putIfPresent method in ConsistentMap
* [[ONOS-2849](https://jira.onosproject.org/browse/ONOS-2849)] - Web UI - Confirmation dialog for enable/disable/uninstall apps
* [[ONOS-2855](https://jira.onosproject.org/browse/ONOS-2855)] - FUNCintent Test Suite Enhancements for OF selectors and Treatments (Emu#1)
* [[ONOS-2858](https://jira.onosproject.org/browse/ONOS-2858)] - Northbound API abstraction in YANG
* [[ONOS-2859](https://jira.onosproject.org/browse/ONOS-2859)] - Network element abstraction in YANG
* [[ONOS-2863](https://jira.onosproject.org/browse/ONOS-2863)] - Support the notion of Region for grouping network elements.
* [[ONOS-2910](https://jira.onosproject.org/browse/ONOS-2910)] - Replace LinkResourceService with new ResourceService
* [[ONOS-3091](https://jira.onosproject.org/browse/ONOS-3091)] - FUNCintentRest Update
* [[ONOS-3123](https://jira.onosproject.org/browse/ONOS-3123)] - Define a PoC for initial YANG service model support in ONOS
* [[ONOS-3125](https://jira.onosproject.org/browse/ONOS-3125)] - Requirement to YANG Tool
* [[ONOS-3147](https://jira.onosproject.org/browse/ONOS-3147)] - Device drivers subsystem
* [[ONOS-3313](https://jira.onosproject.org/browse/ONOS-3313)] - Update wiki documentation to reflect Emu GUI functionality
* [[ONOS-3332](https://jira.onosproject.org/browse/ONOS-3332)] - sketch out BigSwitch for super Controller based on ONOS
* [[ONOS-3337](https://jira.onosproject.org/browse/ONOS-3337)] - Investigate Docker image/file as OnosSystemTest
* [[ONOS-3372](https://jira.onosproject.org/browse/ONOS-3372)] - Define RPC data model for Link related interfaces
* [[ONOS-3417](https://jira.onosproject.org/browse/ONOS-3417)] - Update System test Documentation
* [[ONOS-3433](https://jira.onosproject.org/browse/ONOS-3433)] - Inject links between CORD edge and ROADM
* [[ONOS-3435](https://jira.onosproject.org/browse/ONOS-3435)] - Analyze XOS requirements for E-CORD
* [[ONOS-3505](https://jira.onosproject.org/browse/ONOS-3505)] - Web UI - Tabular view of drivers and behaviours
* [[ONOS-3528](https://jira.onosproject.org/browse/ONOS-3528)] - Need to catch and print warnings for exceptions in threads
* [[ONOS-3554](https://jira.onosproject.org/browse/ONOS-3554)] - Capture ClusterCommunicationService metrics
* [[ONOS-3555](https://jira.onosproject.org/browse/ONOS-3555)] - DistributedGroupStore must use ConsistentMap
* [[ONOS-3563](https://jira.onosproject.org/browse/ONOS-3563)] - Register TributarySlot resources in resource manager
* [[ONOS-3568](https://jira.onosproject.org/browse/ONOS-3568)] - Modify pingall function in CHO as timeout causes cascade ping failure in subsequent tests
* [[ONOS-3578](https://jira.onosproject.org/browse/ONOS-3578)] - Add mechanism to notify ONOS of downed device
* [[ONOS-3605](https://jira.onosproject.org/browse/ONOS-3605)] - Create Session listener for device notifications
* [[ONOS-3608](https://jira.onosproject.org/browse/ONOS-3608)] - Create a TestON re-try wrapper to wrap other functions in it for all re-try method
* [[ONOS-3609](https://jira.onosproject.org/browse/ONOS-3609)] - fix max intent and topo SCPF tests
* [[ONOS-3614](https://jira.onosproject.org/browse/ONOS-3614)] - Make scheme and remote URI configurable on big switch app
* [[ONOS-3632](https://jira.onosproject.org/browse/ONOS-3632)] - Move to Karaf 4.0 and Maven 3.3.9
* [[ONOS-3634](https://jira.onosproject.org/browse/ONOS-3634)] - Enhance application to have a category, icon, URL and Read-Me fields
* [[ONOS-3635](https://jira.onosproject.org/browse/ONOS-3635)] - Web UI - Enhance Application view with new columns and a details pane
* [[ONOS-3646](https://jira.onosproject.org/browse/ONOS-3646)] - Move SNMP to release artifacts
* [[ONOS-3654](https://jira.onosproject.org/browse/ONOS-3654)] - Update NETCONF wiki
* [[ONOS-3655](https://jira.onosproject.org/browse/ONOS-3655)] - Device key subsystem
* [[ONOS-3658](https://jira.onosproject.org/browse/ONOS-3658)] - Device key administration
* [[ONOS-3666](https://jira.onosproject.org/browse/ONOS-3666)] - Analysis of ONOS Rest NBI Framework
* [[ONOS-3667](https://jira.onosproject.org/browse/ONOS-3667)] - Planning for Modeling and Automation of Rest Resgistration & Codec implementation
* [[ONOS-3668](https://jira.onosproject.org/browse/ONOS-3668)] - YANGtoJAVA Translator Analysis and Planning
* [[ONOS-3669](https://jira.onosproject.org/browse/ONOS-3669)] - YANGtoJAVA Translator Design
* [[ONOS-3671](https://jira.onosproject.org/browse/ONOS-3671)] - Detailed analysis of the requirements
* [[ONOS-3672](https://jira.onosproject.org/browse/ONOS-3672)] - Solution high level design
* [[ONOS-3674](https://jira.onosproject.org/browse/ONOS-3674)] - demo setup and scenarios planning
* [[ONOS-3675](https://jira.onosproject.org/browse/ONOS-3675)] - Create an outline for the ONOS paper
* [[ONOS-3676](https://jira.onosproject.org/browse/ONOS-3676)] - Submit talk proposals for ONS
* [[ONOS-3679](https://jira.onosproject.org/browse/ONOS-3679)] - HA test Stability issues
* [[ONOS-3681](https://jira.onosproject.org/browse/ONOS-3681)] - Fix CHO failures for the spine-leaf topo
* [[ONOS-3688](https://jira.onosproject.org/browse/ONOS-3688)] - Implement application for compute node bootstrapping
* [[ONOS-3690](https://jira.onosproject.org/browse/ONOS-3690)] - Create southbound driver for Lumentum ROADM (SNMP)
* [[ONOS-3691](https://jira.onosproject.org/browse/ONOS-3691)] - Create southbound driver for Fujitsu Transponder (NETCONF)
* [[ONOS-3692](https://jira.onosproject.org/browse/ONOS-3692)] - Create southbound driver for REST devices
* [[ONOS-3694](https://jira.onosproject.org/browse/ONOS-3694)] - Define subset of MEF services and their attributes to support
* [[ONOS-3696](https://jira.onosproject.org/browse/ONOS-3696)] - Remove flow rules when a VM is terminated
* [[ONOS-3704](https://jira.onosproject.org/browse/ONOS-3704)] - pom.xml errors/warnings - mostly for shaded bundles
* [[ONOS-3708](https://jira.onosproject.org/browse/ONOS-3708)] - Enhance the submitter Gerrit plugin to separate module owner reviews from others
* [[ONOS-3709](https://jira.onosproject.org/browse/ONOS-3709)] - Enhance the submitter Gerrit plugin to assign 2 most specific module owners to a review
* [[ONOS-3710](https://jira.onosproject.org/browse/ONOS-3710)] - Enhance the submitter Gerrit plugin to generate an easy to read module owners page
* [[ONOS-3717](https://jira.onosproject.org/browse/ONOS-3717)] - Guard in OchPort constructor for null parameters
* [[ONOS-3722](https://jira.onosproject.org/browse/ONOS-3722)] - Augment TableModel with Annotations Mechanism
* [[ONOS-3730](https://jira.onosproject.org/browse/ONOS-3730)] - Populate portSpeed for ODUCLT and OCH ports
* [[ONOS-3731](https://jira.onosproject.org/browse/ONOS-3731)] - Change key bindings for pathpainter app
* [[ONOS-3733](https://jira.onosproject.org/browse/ONOS-3733)] - Fix Cluster communication issues noted during failure testing on LxC
* [[ONOS-3738](https://jira.onosproject.org/browse/ONOS-3738)] - Topology View: add Function Key bindings to select overlays
* [[ONOS-3739](https://jira.onosproject.org/browse/ONOS-3739)] - Substitute copyright year at runtime
* [[ONOS-3741](https://jira.onosproject.org/browse/ONOS-3741)] - Bind Escape to Cancel and Enter to OK in dialog service
* [[ONOS-3747](https://jira.onosproject.org/browse/ONOS-3747)] - Refactor Loading factory to handle delayed start internally
* [[ONOS-3755](https://jira.onosproject.org/browse/ONOS-3755)] - Clean up formatting on Flow, Port, Group, Meter views
* [[ONOS-3757](https://jira.onosproject.org/browse/ONOS-3757)] - Create REST southbound protocol page
* [[ONOS-3758](https://jira.onosproject.org/browse/ONOS-3758)] - Restructure drivers module structure to separate base drivers from device-family specific drivers
* [[ONOS-3759](https://jira.onosproject.org/browse/ONOS-3759)] - Driver-based fallback providers
* [[ONOS-3760](https://jira.onosproject.org/browse/ONOS-3760)] - Enhance BasicDeviceConfig to allow injection of mfg/hw/sw/serial information
* [[ONOS-3762](https://jira.onosproject.org/browse/ONOS-3762)] - Create an ON.Lab facebook account and link it to our existing social media accounts
* [[ONOS-3764](https://jira.onosproject.org/browse/ONOS-3764)] - Create an ON.Lab linkedin account and link it to our existing social media accounts
* [[ONOS-3765](https://jira.onosproject.org/browse/ONOS-3765)] - Install and configure plugin on wordpress to automatically publish news on twitter
* [[ONOS-3774](https://jira.onosproject.org/browse/ONOS-3774)] - Submit proposal for ONS Tutorial - Extending the ONOS UI
* [[ONOS-3776](https://jira.onosproject.org/browse/ONOS-3776)] - Install PXE server to facilitate installations
* [[ONOS-3778](https://jira.onosproject.org/browse/ONOS-3778)] - ECORD app has incorrect origin string
* [[ONOS-3779](https://jira.onosproject.org/browse/ONOS-3779)] - Create VPN with Huawei
* [[ONOS-3780](https://jira.onosproject.org/browse/ONOS-3780)] - Application Table View - second level sort required
* [[ONOS-3782](https://jira.onosproject.org/browse/ONOS-3782)] - Unable to load apps
* [[ONOS-3783](https://jira.onosproject.org/browse/ONOS-3783)] - Document SSL OF configuration procedure
* [[ONOS-3785](https://jira.onosproject.org/browse/ONOS-3785)] - Install router in E-CORD rack
* [[ONOS-3787](https://jira.onosproject.org/browse/ONOS-3787)] - ONOSFW-TEST
* [[ONOS-3790](https://jira.onosproject.org/browse/ONOS-3790)] - Create deletePort(bridge,port) on OVSDB
* [[ONOS-3791](https://jira.onosproject.org/browse/ONOS-3791)] - NETCONF session factory
* [[ONOS-3793](https://jira.onosproject.org/browse/ONOS-3793)] - Implements security group REST call json parser
* [[ONOS-3795](https://jira.onosproject.org/browse/ONOS-3795)] - PATCH method in REST southbound controller
* [[ONOS-3796](https://jira.onosproject.org/browse/ONOS-3796)] - Update wiki to reflect new Application GUI
* [[ONOS-3797](https://jira.onosproject.org/browse/ONOS-3797)] - Define skeleton for YANG model integration
* [[ONOS-3806](https://jira.onosproject.org/browse/ONOS-3806)] - Create link between AmLight and GEANT
* [[ONOS-3807](https://jira.onosproject.org/browse/ONOS-3807)] - Create link between AmLight and KREONET
* [[ONOS-3808](https://jira.onosproject.org/browse/ONOS-3808)] - Produce "Introduction to the ONOS Web UI" Video
* [[ONOS-3810](https://jira.onosproject.org/browse/ONOS-3810)] - Test rest implementation against CIENA offical WS simulator
* [[ONOS-3814](https://jira.onosproject.org/browse/ONOS-3814)] - Make production network with structured, separated, test, onos and dp networks
* [[ONOS-3815](https://jira.onosproject.org/browse/ONOS-3815)] - ResourceId refactoring
* [[ONOS-3819](https://jira.onosproject.org/browse/ONOS-3819)] - Implement a PartitionService for managing / administering storage partitions
* [[ONOS-3824](https://jira.onosproject.org/browse/ONOS-3824)] - Prepare slide set and notes for ONS tutorial (Extending the ONOS WebUI)
* [[ONOS-3831](https://jira.onosproject.org/browse/ONOS-3831)] - Code the load balancing algorithm at SFC Manager
* [[ONOS-3833](https://jira.onosproject.org/browse/ONOS-3833)] - Update data structures and supply required contents of packet to algorithm at the SFC Manager
* [[ONOS-3834](https://jira.onosproject.org/browse/ONOS-3834)] - Load balance algorithm should output the rules and flows at classifier and SFFs
* [[ONOS-3835](https://jira.onosproject.org/browse/ONOS-3835)] - Download the load balanced rules and flows at classifier and SFFs
* [[ONOS-3836](https://jira.onosproject.org/browse/ONOS-3836)] - After flow rules are active, send the first packet received from classifier back to classifier
* [[ONOS-3837](https://jira.onosproject.org/browse/ONOS-3837)] - unit test all the stories. Commit code along with unit test code
* [[ONOS-3844](https://jira.onosproject.org/browse/ONOS-3844)] - Support 2 additional flow spec types (packet-length & fragment) as per RFC 5577 as part of Extension
* [[ONOS-3845](https://jira.onosproject.org/browse/ONOS-3845)] - BGP FlowSpec capability support
* [[ONOS-3846](https://jira.onosproject.org/browse/ONOS-3846)] - NPE in 'leaders -j' command
* [[ONOS-3854](https://jira.onosproject.org/browse/ONOS-3854)] - Implement BGP flow object
* [[ONOS-3855](https://jira.onosproject.org/browse/ONOS-3855)] - Implement BGP flow spec provider to update BGP flow rules
* [[ONOS-3856](https://jira.onosproject.org/browse/ONOS-3856)] - Implement BGP flow spec RIB out
* [[ONOS-3857](https://jira.onosproject.org/browse/ONOS-3857)] - BGP flow spec NLRI encoding for MP\_REACH and MP\_UNREACH
* [[ONOS-3858](https://jira.onosproject.org/browse/ONOS-3858)] - BGP flow specification system test
* [[ONOS-3859](https://jira.onosproject.org/browse/ONOS-3859)] - App for monitoring and load balancing Control Plane
* [[ONOS-3864](https://jira.onosproject.org/browse/ONOS-3864)] - Create OTN and FIBER\_SWITCH device icons
* [[ONOS-3871](https://jira.onosproject.org/browse/ONOS-3871)] - Implement Yang file-scanner
* [[ONOS-3872](https://jira.onosproject.org/browse/ONOS-3872)] - Implement Java package creation
* [[ONOS-3873](https://jira.onosproject.org/browse/ONOS-3873)] - Implement Java file creation and appending Java content
* [[ONOS-3874](https://jira.onosproject.org/browse/ONOS-3874)] - Implement seek and insert operations for Java file
* [[ONOS-3875](https://jira.onosproject.org/browse/ONOS-3875)] - Implement Maven plugin
* [[ONOS-3876](https://jira.onosproject.org/browse/ONOS-3876)] - Implement Yang grammar for module,sub-module,container,list
* [[ONOS-3877](https://jira.onosproject.org/browse/ONOS-3877)] - Implement Yang grammar for leaf,leaf-list,augment,grouping/uses
* [[ONOS-3878](https://jira.onosproject.org/browse/ONOS-3878)] - Implement parse tree traversal using listener framework
* [[ONOS-3879](https://jira.onosproject.org/browse/ONOS-3879)] - Implement parse stack management
* [[ONOS-3880](https://jira.onosproject.org/browse/ONOS-3880)] - Implement Yang module parsing
* [[ONOS-3881](https://jira.onosproject.org/browse/ONOS-3881)] - Implement Yang sub-module parsing
* [[ONOS-3882](https://jira.onosproject.org/browse/ONOS-3882)] - Implement Yang container parsing
* [[ONOS-3883](https://jira.onosproject.org/browse/ONOS-3883)] - Implement Yang list parsing
* [[ONOS-3884](https://jira.onosproject.org/browse/ONOS-3884)] - Implement Yang module data-model
* [[ONOS-3885](https://jira.onosproject.org/browse/ONOS-3885)] - Implement Yang sub-module data-model
* [[ONOS-3886](https://jira.onosproject.org/browse/ONOS-3886)] - Implement Yang container data-model
* [[ONOS-3887](https://jira.onosproject.org/browse/ONOS-3887)] - Implement Yang list data-model
* [[ONOS-3888](https://jira.onosproject.org/browse/ONOS-3888)] - Create link between AmLight and NCTU (Taiwan)
* [[ONOS-3892](https://jira.onosproject.org/browse/ONOS-3892)] - Implement Yang leaf/leaf-list parsing
* [[ONOS-3896](https://jira.onosproject.org/browse/ONOS-3896)] - Implement Yang string data-types
* [[ONOS-3897](https://jira.onosproject.org/browse/ONOS-3897)] - Implement Yang derived data-types
* [[ONOS-3898](https://jira.onosproject.org/browse/ONOS-3898)] - Implement Yang choice data-type parsing
* [[ONOS-3899](https://jira.onosproject.org/browse/ONOS-3899)] - Implement Yang leaf/leaf-list data-model
* [[ONOS-3900](https://jira.onosproject.org/browse/ONOS-3900)] - Implement Yang augment data-model
* [[ONOS-3901](https://jira.onosproject.org/browse/ONOS-3901)] - Implement Yang grouping/uses data-model
* [[ONOS-3902](https://jira.onosproject.org/browse/ONOS-3902)] - Implement Yang integer data-types data-model
* [[ONOS-3903](https://jira.onosproject.org/browse/ONOS-3903)] - Implement Yang string data-types data-model
* [[ONOS-3905](https://jira.onosproject.org/browse/ONOS-3905)] - Implement Yang choice data-type data-model
* [[ONOS-3906](https://jira.onosproject.org/browse/ONOS-3906)] - Implement Yang module translator
* [[ONOS-3908](https://jira.onosproject.org/browse/ONOS-3908)] - Implement Yang container translator
* [[ONOS-3910](https://jira.onosproject.org/browse/ONOS-3910)] - Implement Yang leaf/leaf-list translator
* [[ONOS-3912](https://jira.onosproject.org/browse/ONOS-3912)] - Implement Yang grouping/uses translator
* [[ONOS-3917](https://jira.onosproject.org/browse/ONOS-3917)] - Implement Yang lexer
* [[ONOS-3926](https://jira.onosproject.org/browse/ONOS-3926)] - Build console ethernet cables
* [[ONOS-3927](https://jira.onosproject.org/browse/ONOS-3927)] - Module Owner Plugin Improvements
* [[ONOS-3929](https://jira.onosproject.org/browse/ONOS-3929)] - Device factory in NetconfController
* [[ONOS-3932](https://jira.onosproject.org/browse/ONOS-3932)] - Monitor correctly router traffic to understand glitch during vc
* [[ONOS-3933](https://jira.onosproject.org/browse/ONOS-3933)] - Review IEEE Communication magazine / GEANT article
* [[ONOS-3937](https://jira.onosproject.org/browse/ONOS-3937)] - Check performances of RDS DB and make the mandatory updates
* [[ONOS-3938](https://jira.onosproject.org/browse/ONOS-3938)] - YANG SB infrastructure and scripts
* [[ONOS-3940](https://jira.onosproject.org/browse/ONOS-3940)] - Ciena Device Integration
* [[ONOS-3951](https://jira.onosproject.org/browse/ONOS-3951)] - Implement FloatingIP Handler for OpenstackRoutingService
* [[ONOS-3953](https://jira.onosproject.org/browse/ONOS-3953)] - Implements Security Group Handler
* [[ONOS-3956](https://jira.onosproject.org/browse/ONOS-3956)] - Create Invariance check for new CHO test
* [[ONOS-3957](https://jira.onosproject.org/browse/ONOS-3957)] - Investigate coordination of events in new CHO test
* [[ONOS-3959](https://jira.onosproject.org/browse/ONOS-3959)] - Create materials for ONS System test talk
* [[ONOS-3960](https://jira.onosproject.org/browse/ONOS-3960)] - Move VPLS app to ONOS master
* [[ONOS-3962](https://jira.onosproject.org/browse/ONOS-3962)] - ONOS System test S3 demo
* [[ONOS-3980](https://jira.onosproject.org/browse/ONOS-3980)] - Remove deprecated code and APIs from Cardinal and Drake
* [[ONOS-3986](https://jira.onosproject.org/browse/ONOS-3986)] - Implement autocompleter for groups CLI command
* [[ONOS-3987](https://jira.onosproject.org/browse/ONOS-3987)] - create ONS ONOS Kiosk demo
* [[ONOS-3999](https://jira.onosproject.org/browse/ONOS-3999)] - Create AbstractDeviceProvider as a base for other providers
* [[ONOS-4004](https://jira.onosproject.org/browse/ONOS-4004)] - DistributedStatisticStore / DistributedFlowStatisticStore / DistributedPacketStore make configurable
* [[ONOS-4014](https://jira.onosproject.org/browse/ONOS-4014)] - Refactor various \*Id classes to extend from Identifier base class
* [[ONOS-4015](https://jira.onosproject.org/browse/ONOS-4015)] - Region administration CLI
* [[ONOS-4016](https://jira.onosproject.org/browse/ONOS-4016)] - Region administration REST API
* [[ONOS-4018](https://jira.onosproject.org/browse/ONOS-4018)] - Enhance DistributedRegionStore
* [[ONOS-4053](https://jira.onosproject.org/browse/ONOS-4053)] - Analyze the SFC proxy requirement
* [[ONOS-4054](https://jira.onosproject.org/browse/ONOS-4054)] - Analyze the SFC tie breaking requirement at the classifier
* [[ONOS-4055](https://jira.onosproject.org/browse/ONOS-4055)] - Analyze the SFC statistics maintenance requirement
* [[ONOS-4056](https://jira.onosproject.org/browse/ONOS-4056)] - Analyze the GUI or REST API for showing SFC statistics
* [[ONOS-4063](https://jira.onosproject.org/browse/ONOS-4063)] - Implement Yang import parsing
* [[ONOS-4065](https://jira.onosproject.org/browse/ONOS-4065)] - Implement Yang import data-model
* [[ONOS-4066](https://jira.onosproject.org/browse/ONOS-4066)] - Implement Yang include parser
* [[ONOS-4068](https://jira.onosproject.org/browse/ONOS-4068)] - Implement Yang include data-model
* [[ONOS-4069](https://jira.onosproject.org/browse/ONOS-4069)] - Implement Yang union parsing
* [[ONOS-4071](https://jira.onosproject.org/browse/ONOS-4071)] - Implement Yang union data-model
* [[ONOS-4115](https://jira.onosproject.org/browse/ONOS-4115)] - Support Table type in InstructionCodec
* [[ONOS-4191](https://jira.onosproject.org/browse/ONOS-4191)] - Add js,css and html for service function chain.
* [[ONOS-4193](https://jira.onosproject.org/browse/ONOS-4193)] - Add handler for sfc gui.
* [[ONOS-4195](https://jira.onosproject.org/browse/ONOS-4195)] - Register sfc gui.
* [[ONOS-4223](https://jira.onosproject.org/browse/ONOS-4223)] - SFC Proxy: Mapping logic between the 5-tuple and the SFC encapsulation inside every packet
* [[ONOS-4225](https://jira.onosproject.org/browse/ONOS-4225)] - SFC statistics: Maintain the SFC resource statisctics. Maintain datastructures to store the mappings between SFPs and SFs, SFPs and SFFs, SFPs and classifier
* [[ONOS-4300](https://jira.onosproject.org/browse/ONOS-4300)] - YANG RPC Parser Implementation
* [[ONOS-4301](https://jira.onosproject.org/browse/ONOS-4301)] - YANG Notification Parser Implementation
* [[ONOS-4316](https://jira.onosproject.org/browse/ONOS-4316)] - IXIA Benchmark Testing support
* [[ONOS-4430](https://jira.onosproject.org/browse/ONOS-4430)] - Move app.png to resources/
