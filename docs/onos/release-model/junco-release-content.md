# Junco Release Content

# **Final**

High level summary:

* Fabric Enhancements

+ IPv6 segment routing
+ Virtual Private Wire Service (VPWS)

* Dataplane Enhancements

+ New TL1 southbound for Lumentum WaveReady

* vRouter

+ IPv6 support

* Framework

+ HA enhancements

- Kafka now uses HA primitives

+ Virtualization support (to virtualize ONOS instances??)

* Northbound Intent Interface Enhancements

+ Optional Guaranteed Bandwidth Allocation
+ Protection Specification
+ Shared resource modeling
+ Hashing support for ECMP traffic distribution

* UI

+ Scalability improvements
+ Regionalization support

* Dynamic Configuration

  + YANG Models.
  + Enhance YANG Compiler for auto-generation of JAVA as per YANG.
  + YANG Runtime for automation of CODEC.
  + XML/JSON Serialializers to adapt Models.

Individuals

* Jordan Halterman

+ Improvements to Atomix for log compaction efficiency/correctness - improving HA characteristics of ONOS
+ Implement Atomix AsyncAtomicCounterMap, AtomicCounterMap and state machine.
+ Update to Atomix version 1.0.3

Calix

* Shravan Ambati

+ Kafka Application - Updated the Application to a Distributed Application

Ciena

* Claudine Chiu

+ Introduced VIRTUAL\_PORT\_\* events for virtual network to virtual port mapping changes.

* Varun Sharma

+ Investigating and identifying several HA issues related node restarts.

* Jon Hall

+ STC Distributed Primitives test now checks all nodes for results
+ Functionality test for VPLS application
+ Investigated several HA bugs
+ Bump karaf from 3.0.5 to 3.0.8

* Kavitha Alagesan

+ Implemented FUNCgroup tests

Create-Net

* Michele Santuari

+ Enable REST to manage devices under a proxy

Criterion Networks

* Vinayak Tejankar

+ Start IPv6 support for vRouter

ETRI

* Sangsik Yoon

+ new Upgraded AFM and FlowStatisticService

GRNET S.A.

* Andreas Papazois

+ Intent installer for Protection

Huawei

* Cheng Fan

+ Implement Partitions View.

* Jin Gan

+ RESTCONF App: App Skeleton creation

* Aihua Guo

+ Utility support for TE attributes defined in the TE topology YANG model:
+ Node connectivity matrix - Local Link Connectivities (LLCL) - Supporting TTP - Path element - Underlay path

* Sithara Punnassery

+ DynamicConfig store and service implementation(create and read supported)
+ Dynamic Config APIs with RPC and Notification support

* Hesam Rahimi

+ Introducing the new YANG model for ietf-te-topology and modifying the converter utility for TE-NBI app to match the latest YANG model.
+ Improving the converter utility for YANG to TE Subsystem and vice versa.

* Yuren You

+ Support TE-link-remove and TE-node-remove event notification

* Henry Yu

+ RESTFul Protocol changes for support YMS and Dynamic configuraiton
+ RESTfule App
+ jSON Serializer/DeSerializer for Dynamic Configuration

* Gaurav Agrawal

+ Handle YANG compiler adaption to YANG architecture with Dynamic Config Store.

- * Enable YANG compiler to be independent of build environment and deployable in a standalone JVM/OSGi environment.
- Design YANG tools generated code to adapt with newer architecture.

+ Handle YANG base Models

- Define YANG models.
- Define model converter for conversion between schema aware and schema agnostic forms.
- Define schema context and schema context provider.-

+ Handle YANG Runtime

- Define and implement YANG runtime services.
- Define YANG serializer and YANG model.
- Define and implement serializer registry.-

+ Handle ONOS YANG App

- Define and implement YANG runtime manager.

* Bharat Saraswal

+ Handle data tree builder implementation

- Provides data node, leaf node and inner node implementation.
- Provides create , delete and update data tree functionality.

+ Model converter implementation for converting model object data to resource data.
+ Implementation of private-package instruction requirement in onos-buck plugin.
+ Handle implementation of yang compiler manager to provide standalone jvm/osgi env
+ Implement Yang model and provide model registry implementation.

* Vidyashree Rama

+ Handle YANG tools generated code to extend Model Object for module, sub-module, container, list and augment.
+ Handle YANG tools generated classes for augmentable node to adopt to augmentation defined in Model Object.
+ Handle YANG tools modification to stop generation of process subtree, select leaf etc.
+ Builder pattern to replace with setters for generated code to provide mutability to the generated code.
+ YANG tools to generate service interface only for RPC and notification.
+ Auto generation of RPC handler, RPC commands and Register RPC class to ease application usage.
+ Implementation of XML serializer to carry out XML to data node/ resource id CODEC
+ Model converter implementation for converting resource data to model object data
+ Implementation of Model Object Id to support schema unaware application to create resource identifier.

* Sonu Gupta

+ Implemented YANG schema provider context.
+ Defined and implemented  YANG serializer helper.
+ Defined YANG data node listener's based walker mechanism.
+ Support for NETCONF active/passive component utility.

IBM

* + Himanshu Ranjan
    - Add ability to connect NETCONF devices through ssh

KAIST

* Chanhee Lee

+ Implementing unit test on Security-Mode ONOS

KHU

* Sangyun-Han

+ Implement json cli in PacketProcessors and PacketRequests
+ (SBI) Define VirtualDeviceProvider - add interface virtual port description - add interface virtual device Provider/ProviderService

NEC

* Yuta Higuchi

+ CLI action to pretty print JSON
+ Intent improvements to support protection behaviour

- Ensure all Intents reaches installable state.
- Use marker in ProtectedTransportIntentCompiler
- marker resource for annotating installable intent
- Allow LinkCollectionIntent to accept other types of resources.
- ProtectedTransportIntent, compiler, CLI
- intent-details command

+ Add support for disjoint Paths to paths CLI
+ Sort alarm count by severity
+ Handle Copycat queries in high priority

ON.Lab

* Andrea Campanella

+ Faultmanagment app enhancements in backend, CLI and UI
+ UI to show Protected Intents
+ Introduction of default driver to onboard behaviours otherwise not accessible due to differen package
+ CLI to show hierarchy of drivers and behaviours with their parents

* Charles Chan

+ Segment Routing enhancement

- VLAN support
- Introduce generic routing service in Segment Routing

* + OFDPA driver enhancement

    - OFDPA pipeline for OpenvSwitch
    - Change default OFDPA driver to ofdpa3
  + Implement vlan-untagged, vlan-tagged, vlan-native in interface config
  + Implement distributed route store
  + Allow pre-setting component config via REST API

* Jonathan Hart

+ Config support for multiple routers
+ Add ability to remove patches
+ Added completer for interface names

* Luca Prete

+ Add resource groups to allow sharing of resources between intents
+ New bandwidth allocation and release functionalities for all intent types (also available from command line)
+ Partial failure support for SP2MP intents
+ Enable encapsulation in SDN-IP
+ New SDN-IP STC scenario
+ Implementing new VPLS CLI
+ New ONOS administrative guide documentation

* Marc De Leenheer

+ TL1 device provider with driver for Lumentum WaveReady

* Pier Luigi Ventre

+ Virtual Private Wire Service (VPWS) support in Segment Routing App and OFDPA pipelines
+ Greedy learning of IPv6 hosts
+ IPv6 support for Fabric
+ IPv6 support for vRouter

* Ray Milkey

+ build improvements

* Simon Hunt

+ UI sprite support
+ augmented implementation of "showIntent" overlay support allow overlays to declare which intent types they can display.
+ Skeleton implementation of TableDetailService, to house common code for creating detail panels for table item selection.
+ UI core support for visualizing “Protected Intents” on the Topology view

* Thomas Vachuska

+ Added simulation of GEANT topology using null providers.
+ Added REST API to administratively remove hosts.

* Yi Tseng

+ Multi-buckets add and remove support in the same group for OFDPA pipeline
+ Fix cells command

* You Wang

+ Integrated Security (DELTA) tests into OnosSystemTest
+ ONOS bug fix: Topology updation on sequence of events
+ OnosSystemTest bug fix: Race condition when scaling ONOS cluster size during performance tests

* Pratik Parab

+ Enhancements to BGPLS Tests
+ Run Sanity tests on all Docker images

* Shreya Chowdhary

+ Improve reliability of Intent functionality tests

OPLINK

* Mao Lu

+ Add Oplink protection optical switch handshake driver.

* Jimmy Yan

+ Add ROADM application

POSTECH

* Yoonseon Han

+ Virtualization

- Implement packet and flowrule services for virtual networks including managers and stores
- Define provider interfaces with skeleton codes for packet, flow, group, and meter providers for virtual networks
- Add command for flow lists for virtual networks

* Hwanwook Lee

+ Null-Providers: Implements the mesh topology

* Jian Li

+ Supported various LCAF address types and DDT message types

- LCAF address support: AS, Geo-Coordinate, multicast and nonce
- DDT message type support : LispMapReferral

+ Added skeleton code for mapping mgmt. app, LISP driver & message provider
+ Enhanced MapServer and MapResolver to support router registration and negative forwarding
+ Implemented initial version of LISP device and mapping providers
+ Supported MappingDatabase along with mapping aging mechanism
+ Bumped up various dependencies related to REST API

- Bump up swagger UI from 2.2.5 to 2.2.10
- Bump up jersey from 2.22.2 to 2.25
- Bump up jackson from 2.7.3 to 2.8.6

Radisys

* Amit Ghosh

+ Added changes to OltPipeline to create filtering flows for DHCP packets

Samsung

* Jaegon Kim

+ Add hashing support so intent traffic path load is distributed.

SK Telecom

* Hyunsun Moon

+ Implemented skeleton of OFAgent application

Universidad de Murcia

* Jordi Ortiz

+ Meter support enhancements
+ New meter-remove CLI command
+ Added meter-add command options

Villa-Tech, inc 

* Steven Burrows

+ Migrating “classic” topology functionality to the new (“region aware”) topology view
+ Augmented topology layouts to render sprite layers, and handle “logical” grid mapping
