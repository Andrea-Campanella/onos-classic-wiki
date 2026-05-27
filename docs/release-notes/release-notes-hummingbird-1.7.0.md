# Release Notes - Hummingbird 1.7.0

# Hummingbird Release

Version: 1.7.0 

Release Date: September 23, 2016

Download [here](../onos/downloads.md)

# Release Content

## Community

* New ONOS collaborators

+ Announced new collaborators: Adtran, Argela, IPT, SDNLAB, Villa-Tech
+ Unannounced new collaborators that have been approved but haven’t been communicated out yet: BII

## Automated testing, Build environment

* Contributions from ON.Lab and Ciena
* Built new ONOS tutorial VM (ON.Lab)
* ONOS Swagger Plugin (ON.Lab)
* Finished moving to BUCK (ON.Lab)
* Stabilized STC, greatly improved coverage (config subsystem, distributed primitives, applications, drivers), added capability to run tests multiple times while unattended (ON.Lab)
* Mininet scripts for testing ONOS network partitions and dynamic scaling (Ciena)

## Applications

* Contributions from Adara, ATTO Research, BUPT, Create-Net, Huawei, NEC, ON.Lab, SK Telecom, SRI, Tata, Tech-Mahindra
* Enhancements to ICONA (controller peering) (Create-Net, Tata)
* SONA and Scaleable gateway improvements (SK Telecom, ATTO Research)
* External event dispatching, standard JSON format for events, event registration, integration of events with packet, link, topology events, integration of RabbitMQ (Adara)
* New subsystem for anomaly detection (ATHENA) (SRI)
* Open Exchange Protocol for inter-controller communication (BUPT)
* Added YANG Management System (YMS) application. (Huawei)
* YANG Tools enhancements to support complete YANG 1.0 (Huawei)
* Added DHCP Relay (Tech-Mahindra)
* Improvements to FIB installer (Tech-Mahindra)
* Dynamic XConnect support (ON.Lab)
* BGP Route policy distribution and flow spec (Huawei)
* Added BMv2 demo apps (P4 support) (ON.Lab)
* VPLS code refactoring (NCTU)
* UI - Separating theme from layout for CSS files, continued work on theming UI (ON.Lab)
* IETF TE Topology Application under ACTN (Huawei)
* Carrier Ethernet application for installing EPL/EP-LAN/EP-Tree and EVPL/EVP-LAN/EVP-Tree services (Huawei)

## Northbound

* Contributions from Calix, Ciena, Fujitsu, Huawei, NEC, ON.Lab, OpLink, Samsung, SK Telecom, Verizon
* Implement PowerConfig for Oplink Devices, Use LambdaQuery in OpenFlowDeviceProvider to get details for optical ports (OpLink)
* Kafka message bus integration (Calix)
* decouple optical-model from CLI (NEC)
* Add basic error handling to gRPC Device SB service, Add link eviction to gRPC Link SB (NEC)
* Initial implementation of Virtual network Intent service (Ciena)
* Improve performance of Resource Reservation Service (Fujitsu)
* YMS to provide automated CODEC for NBI. (Huawei)
* Abstraction and Control of TE Networks (ACTN) implementation (Huawei)
* Refactored tunnel and interface config behavior (SK Telecom)
* sp2mp intents now modify packets at the egress switch (Verizon)
* mp2sp intents now modify packets at the ingress switch (Verizon)
* sp2mp intents support multiple treatments (Università Roma Tor Vergata / ON.Lab)
* mp2sp intents support multiple selectors (Università Roma Tor Vergata / ON.Lab)
* Added back-off mechanism for intent clean-up (ON.Lab)
* Added ARP command (ON.Lab)
* Support for standard IETF TE YANG models under ACTN (Huawei)
* New neighbour message subsystem for handling ARP and NDP (ON.Lab)

## Core

* Contributions from Ciena, Fujitsu, NCTU, NEC, ON.Lab
* Refactoring of optical information model - Move optical Intent compilers out to optical-model (NEC)
* Initial work on virtualization - Virtual Network DeviceService and LinkService to use VirtualNetwork service, virtual network topology provider (Ciena)
* New distributed system primitives (AsyncConsistentTreeMap, DistributedTreeMap) (Fujitsu)
* Distributed work queue primitive (ON.Lab)
* New ApplicationStore that uses a single ConsistentMap to track all app related state (ON.Lab)
* NetconfAlarmProvider alerts core about notifications given subscription (ON.Lab)
* Implementation of Hybrid Logical Clock Service (ON.Lab)
* New ComponentConfigStore that uses a ConsistentMap configured with sequential consistency (ON.Lab)
* Support Cluster restart via stc (NCTU)

## Southbound

* Contributions from Cognizant, Create-Net, Fujitsu, GEANT, Huawei, NEC, ON.Lab, OpLink, POSTECH, SK Telecom, Tata, University of Patras
* LOXI enhancements for optical extensions (OpLink)
* New provider for link discovery
* NETCONF enhancements (Fujitsu)
* YMS to provide automated CODEC for SBI (Huawei)
* YANG Tools enhancements to support auto code generation for drivers/providers. (Huawei)
* Implement the Driver for handling Arista switch (SK Telecom)
* Updated NETCONF for Fujitsu OLT devices, Separate optical driver from "default" driver bundle (NEC)
* Rate limit on port via NetConf (GEANT)
* Cisco IOS PortDiscovery (University of Patras)
* Initial implementation of  LISP control message objects (POSTECH)
* OSPF refactoring to align with ISIS design, ISIS updates (Cognizant)
* Major refactoring of the BMv2 protocol module (P4 support) (ON.Lab)
* Add support for vlan based intents in the Corsa driver (ON.Lab)
* Building alarms from NETCONF notifications (ON.Lab)
* RestConf Client Implementation (Huawei)

---

## Sub-task

* [[ONOS-4765](https://jira.onosproject.org/browse/ONOS-4765)] - Document features added to TestON
* [[ONOS-4766](https://jira.onosproject.org/browse/ONOS-4766)] - Document CHO Framework
* [[ONOS-4767](https://jira.onosproject.org/browse/ONOS-4767)] - Make sure Github and wiki are in-sync
* [[ONOS-4976](https://jira.onosproject.org/browse/ONOS-4976)] - com.esotericsoftware.kryo.KryoException: Buffer underflow. Exception
* [[ONOS-4977](https://jira.onosproject.org/browse/ONOS-4977)] - java.lang.IndexOutOfBoundsException: toIndex = 20000. Exception
* [[ONOS-5117](https://jira.onosproject.org/browse/ONOS-5117)] - Create network partition test for onos.py
* [[ONOS-5118](https://jira.onosproject.org/browse/ONOS-5118)] - Dynamic clustering test for onos.py
* [[ONOS-5122](https://jira.onosproject.org/browse/ONOS-5122)] - Update CHO Test Plan
* [[ONOS-5123](https://jira.onosproject.org/browse/ONOS-5123)] - Update FUNC Test Plan
* [[ONOS-5124](https://jira.onosproject.org/browse/ONOS-5124)] - Update HA Test Plan
* [[ONOS-5128](https://jira.onosproject.org/browse/ONOS-5128)] - Update Performance Test Plan

## Bug

* [[ONOS-2582](https://jira.onosproject.org/browse/ONOS-2582)] - Topology View - return to same state after visiting other view
* [[ONOS-3652](https://jira.onosproject.org/browse/ONOS-3652)] - Superflous flows after topo is shutdown
* [[ONOS-3968](https://jira.onosproject.org/browse/ONOS-3968)] - ONOS build is really, really slow
* [[ONOS-4399](https://jira.onosproject.org/browse/ONOS-4399)] - Topology crash when using big topology (e.g. 20X20 torus)
* [[ONOS-4504](https://jira.onosproject.org/browse/ONOS-4504)] - Method 'artifactDir' in onos-maven-plugin generates wrong directory
* [[ONOS-4570](https://jira.onosproject.org/browse/ONOS-4570)] - Random selection of VLAN ids in the Intent Framework
* [[ONOS-4583](https://jira.onosproject.org/browse/ONOS-4583)] - in union, if i give int & uint types together causing error for already defined
* [[ONOS-4601](https://jira.onosproject.org/browse/ONOS-4601)] - yang utils error info is not ok. not showing the specific reason. pyang givng the specific reason
* [[ONOS-4613](https://jira.onosproject.org/browse/ONOS-4613)] - Adding flow with priority more than 65535 in ONOS makes the flow in PENDING\_ADD state
* [[ONOS-4615](https://jira.onosproject.org/browse/ONOS-4615)] - listBuilder in DefaultFilteringObjective.Builder is lost when copying from existing FilteringObjective
* [[ONOS-4624](https://jira.onosproject.org/browse/ONOS-4624)] - Topology view - keybindings are not disabled when dialog panel is in use.
* [[ONOS-4653](https://jira.onosproject.org/browse/ONOS-4653)] - wipe-out please" command of ONOS CLI does not remove flows associated with intents or devices
* [[ONOS-4667](https://jira.onosproject.org/browse/ONOS-4667)] - onos-gen-partitions doesn't write its output file if you pass in a list of IP addresses
* [[ONOS-4688](https://jira.onosproject.org/browse/ONOS-4688)] - OpenFlow Error message with type OFPET\_BAD\_ACTION is not handled
* [[ONOS-4689](https://jira.onosproject.org/browse/ONOS-4689)] - [BGP RPD] Default route should be allowed to configure for local/remote IP
* [[ONOS-4728](https://jira.onosproject.org/browse/ONOS-4728)] - [YANG UTILS] Issue in revision
* [[ONOS-4731](https://jira.onosproject.org/browse/ONOS-4731)] - pce web exception occured
* [[ONOS-4732](https://jira.onosproject.org/browse/ONOS-4732)] - Core class SetQueueInstruction is not registered in Kryo
* [[ONOS-4735](https://jira.onosproject.org/browse/ONOS-4735)] - FlowRuleStore out of sync
* [[ONOS-4744](https://jira.onosproject.org/browse/ONOS-4744)] - Leafref implementation in YANG
* [[ONOS-4745](https://jira.onosproject.org/browse/ONOS-4745)] - Devices View - detail panel - name change - Enter/Esc not working.
* [[ONOS-4749](https://jira.onosproject.org/browse/ONOS-4749)] - GroupKey Interpretaion in REST api
* [[ONOS-4754](https://jira.onosproject.org/browse/ONOS-4754)] - Error message OFFlowModFailedErrorMsgVer13 is not working in onos.
* [[ONOS-4755](https://jira.onosproject.org/browse/ONOS-4755)] - Error message OFBadMatchErrorMsgVer13 is not handled in onos
* [[ONOS-4757](https://jira.onosproject.org/browse/ONOS-4757)] - KryoException observed in ResourceRegistrar
* [[ONOS-4763](https://jira.onosproject.org/browse/ONOS-4763)] - KryoException when bringing up links
* [[ONOS-4772](https://jira.onosproject.org/browse/ONOS-4772)] - Optical resource query can throw NPE
* [[ONOS-4789](https://jira.onosproject.org/browse/ONOS-4789)] - some services don't remove listener in deactive function
* [[ONOS-4805](https://jira.onosproject.org/browse/ONOS-4805)] - Choice of Overlay not persisted across view switches or login sessions
* [[ONOS-4811](https://jira.onosproject.org/browse/ONOS-4811)] - [PCE\_WEBUI]For show tunnels its showing “remove path message log”
* [[ONOS-4812](https://jira.onosproject.org/browse/ONOS-4812)] - [PCE\_WEBUI]We are able to select the radio button without checkboxes and functionality is not working
* [[ONOS-4813](https://jira.onosproject.org/browse/ONOS-4813)] - [PCE-WEBUI] Without mandatory option “Create path message log” and no error message in controller side also
* [[ONOS-4814](https://jira.onosproject.org/browse/ONOS-4814)] - [PCE\_WEBUI]Unable to create a LSP with tunnel name more than 252 Characters via WEB-UI but the same was successfull via CL
* [[ONOS-4815](https://jira.onosproject.org/browse/ONOS-4815)] - [PCE\_WEBUI]Unable to delete the tunnels which was failed(inactive/failed) to create via web UI
* [[ONOS-4816](https://jira.onosproject.org/browse/ONOS-4816)] - [PCE\_WEBUI] PCE-UPDATE None is not working for bandwidth option
* [[ONOS-4819](https://jira.onosproject.org/browse/ONOS-4819)] - [PCE\_WEBUI]Exception occurred in PceWebTopovMessageHandler
* [[ONOS-4836](https://jira.onosproject.org/browse/ONOS-4836)] - POST FlowObjectives with INVALID operation/Type/Flag type causes NPE
* [[ONOS-4839](https://jira.onosproject.org/browse/ONOS-4839)] - [YANGUTILS] update file priority for input files
* [[ONOS-4842](https://jira.onosproject.org/browse/ONOS-4842)] - Leafref with augment and uses
* [[ONOS-4847](https://jira.onosproject.org/browse/ONOS-4847)] - [PCE\_WEB] We are not converting properly bandwidth value which is given as Mbps via WEB\_UI.
* [[ONOS-4857](https://jira.onosproject.org/browse/ONOS-4857)] - SP2MP intents sometimes install VLAN treatment flows incorrectly (only with Flow Objectives)
* [[ONOS-4858](https://jira.onosproject.org/browse/ONOS-4858)] - If it takes more than 5 seconds to process intents, another intent installation request is submitted, even if the original intent gets installed.
* [[ONOS-4864](https://jira.onosproject.org/browse/ONOS-4864)] - Resource Manager doesn't give back the same list of VLANs if an intent is reinstalled (without failing)
* [[ONOS-4876](https://jira.onosproject.org/browse/ONOS-4876)] - "Failed to generate code" exception is thrown for a valid YANG file.
* [[ONOS-4881](https://jira.onosproject.org/browse/ONOS-4881)] - Improper error when 2 or more files contain same module name.
* [[ONOS-4882](https://jira.onosproject.org/browse/ONOS-4882)] - Unique is not supported, throwing error.
* [[ONOS-4883](https://jira.onosproject.org/browse/ONOS-4883)] - Invalid holder error is thrown for when statement.
* [[ONOS-4885](https://jira.onosproject.org/browse/ONOS-4885)] - Parser exception for invalid path in leafref.
* [[ONOS-4886](https://jira.onosproject.org/browse/ONOS-4886)] - Build failing without proper error when leafref is refering to union type.
* [[ONOS-4887](https://jira.onosproject.org/browse/ONOS-4887)] - Build failed and error is thrown for yang version 1.0
* [[ONOS-4888](https://jira.onosproject.org/browse/ONOS-4888)] - Cannot find symbol error occurring for grouping and uses feature.
* [[ONOS-4889](https://jira.onosproject.org/browse/ONOS-4889)] - 4 Checkstyle errors occurred for standard ietf files.
* [[ONOS-4890](https://jira.onosproject.org/browse/ONOS-4890)] - Invalid holder error occurring for case in ietf standard files.
* [[ONOS-4891](https://jira.onosproject.org/browse/ONOS-4891)] - Error occurred while building standard yang files.
* [[ONOS-4892](https://jira.onosproject.org/browse/ONOS-4892)] - augment name invalid error is occurring.
* [[ONOS-4893](https://jira.onosproject.org/browse/ONOS-4893)] - Error occurring while concatenating paths for leafref, pyang check has no errors.
* [[ONOS-4896](https://jira.onosproject.org/browse/ONOS-4896)] - EdgeManager may incorrectly compute the edge points based on outdated topology
* [[ONOS-4920](https://jira.onosproject.org/browse/ONOS-4920)] - Fix to router interface refers subnet not network
* [[ONOS-4923](https://jira.onosproject.org/browse/ONOS-4923)] - [YANGUTILS]Uses nodes are not copied when uses is child of grouping's child
* [[ONOS-4924](https://jira.onosproject.org/browse/ONOS-4924)] - Fix import mechanism of the behaviors in ONOS drivers
* [[ONOS-4930](https://jira.onosproject.org/browse/ONOS-4930)] - Fix NPE from ScalableGateway caused by the event triggered before map creation
* [[ONOS-4931](https://jira.onosproject.org/browse/ONOS-4931)] - FlowEntry.life() is in milliseconds but gets created as seconds
* [[ONOS-4934](https://jira.onosproject.org/browse/ONOS-4934)] - Defect : Compilation error occurred for typedef.
* [[ONOS-4935](https://jira.onosproject.org/browse/ONOS-4935)] - Defect : Data type not supported error is thrown without any information on the file and line of error.
* [[ONOS-4936](https://jira.onosproject.org/browse/ONOS-4936)] - Defect : Compilation error occurred.
* [[ONOS-4937](https://jira.onosproject.org/browse/ONOS-4937)] - Compilation error occurred for typedef with union
* [[ONOS-4940](https://jira.onosproject.org/browse/ONOS-4940)] - For non existing devices in the network , GET /topology/infrastructure/{connectPoint} api returns "false" value instead of "404 error"
* [[ONOS-4941](https://jira.onosproject.org/browse/ONOS-4941)] - [YANGUTILS]Grouping and uses interfile linking issue
* [[ONOS-4942](https://jira.onosproject.org/browse/ONOS-4942)] - ONOS seems to have high memory usage when doing a pingall with reactive forwarding
* [[ONOS-4946](https://jira.onosproject.org/browse/ONOS-4946)] - GetTunnelCount cast exception when getting the device property panel details in WEB GUI
* [[ONOS-4952](https://jira.onosproject.org/browse/ONOS-4952)] - Typedef not supported error is thrown for self linking.
* [[ONOS-4953](https://jira.onosproject.org/browse/ONOS-4953)] - Compilation error for file linking type with self module prefix.
* [[ONOS-4954](https://jira.onosproject.org/browse/ONOS-4954)] - Nullpointer exception occurred.
* [[ONOS-4955](https://jira.onosproject.org/browse/ONOS-4955)] - Build failing for augment inside uses.
* [[ONOS-4956](https://jira.onosproject.org/browse/ONOS-4956)] - Typedef package doesn't changes after cloning, still takes groupings package.
* [[ONOS-4957](https://jira.onosproject.org/browse/ONOS-4957)] - TestON SCPFbatchFlowResp test case confirm flow by REST API
* [[ONOS-4975](https://jira.onosproject.org/browse/ONOS-4975)] - Intent-Perf test Bug
* [[ONOS-4978](https://jira.onosproject.org/browse/ONOS-4978)] - Failed to backup device
* [[ONOS-4979](https://jira.onosproject.org/browse/ONOS-4979)] - [YANGUTILS] If identifier name is enum then error is thrown.
* [[ONOS-4983](https://jira.onosproject.org/browse/ONOS-4983)] - Another bucket is added in groups when IP of gateway is modified
* [[ONOS-4991](https://jira.onosproject.org/browse/ONOS-4991)] - Typedef with leafref is not handled
* [[ONOS-5004](https://jira.onosproject.org/browse/ONOS-5004)] - [YANG UTILS] No APIs offered to add/get AugmentedInfo()
* [[ONOS-5005](https://jira.onosproject.org/browse/ONOS-5005)] - [YANG UTILS] Cannot use YO builder API to build YO
* [[ONOS-5027](https://jira.onosproject.org/browse/ONOS-5027)] - [YANG UTILS] some YANG nodes are not translated into Java class
* [[ONOS-5028](https://jira.onosproject.org/browse/ONOS-5028)] - ICMP request rule is not installed for multiple gateways
* [[ONOS-5030](https://jira.onosproject.org/browse/ONOS-5030)] - Fix to gateway ip address in host annotation refers appropriate ip address
* [[ONOS-5036](https://jira.onosproject.org/browse/ONOS-5036)] - Revise Mirror table in OVSDB protocol
* [[ONOS-5038](https://jira.onosproject.org/browse/ONOS-5038)] - PNAT and floating IP incoming flow rules are stuck in PENDING state
* [[ONOS-5060](https://jira.onosproject.org/browse/ONOS-5060)] - External connection of the VM w/o floating IP does not work
* [[ONOS-5069](https://jira.onosproject.org/browse/ONOS-5069)] - openflowcontroller: fails to restart properly
* [[ONOS-5091](https://jira.onosproject.org/browse/ONOS-5091)] - Group Get API returns Application ID as the Object and not as name.
* [[ONOS-5092](https://jira.onosproject.org/browse/ONOS-5092)] - Port Latency Regression
* [[ONOS-5101](https://jira.onosproject.org/browse/ONOS-5101)] - OpenFlow meta app sometimes fails to load with missing requirements
* [[ONOS-5104](https://jira.onosproject.org/browse/ONOS-5104)] - Build failing and throwing error for refine and all unsupported features.
* [[ONOS-5130](https://jira.onosproject.org/browse/ONOS-5130)] - Uncaught exception when push intents
* [[ONOS-5135](https://jira.onosproject.org/browse/ONOS-5135)] - Config value is not correct if config statement is not present in yang file
* [[ONOS-5136](https://jira.onosproject.org/browse/ONOS-5136)] - Linker exception for node datamodel
* [[ONOS-5137](https://jira.onosproject.org/browse/ONOS-5137)] - index out of bound for augment path while inter file linking
* [[ONOS-5138](https://jira.onosproject.org/browse/ONOS-5138)] - error info is not showing line numbers & file name for "Failed to link "
* [[ONOS-5141](https://jira.onosproject.org/browse/ONOS-5141)] - new compilation error for ONOS-4993 issue
* [[ONOS-5142](https://jira.onosproject.org/browse/ONOS-5142)] - Compilation error occurred when int and uint are given together.
* [[ONOS-5154](https://jira.onosproject.org/browse/ONOS-5154)] - Pings fail in sdnip tests
* [[ONOS-5159](https://jira.onosproject.org/browse/ONOS-5159)] - java process CPU utilization very high after link between switches flap
* [[ONOS-5161](https://jira.onosproject.org/browse/ONOS-5161)] - Error is thrown leaf reference reffering to a leaf under list
* [[ONOS-5162](https://jira.onosproject.org/browse/ONOS-5162)] - Unable to find base typedef for given type error is thrown while building
* [[ONOS-5163](https://jira.onosproject.org/browse/ONOS-5163)] - Error information is not showing proper file name and line of error in yang file.
* [[ONOS-5165](https://jira.onosproject.org/browse/ONOS-5165)] - Failed to link to types
* [[ONOS-5177](https://jira.onosproject.org/browse/ONOS-5177)] - tools/dev/bin/onos-app doesn't work for 'localhost' when proxy is configured in the OS
* [[ONOS-5178](https://jira.onosproject.org/browse/ONOS-5178)] - No get/set for root node in generated service
* [[ONOS-5183](https://jira.onosproject.org/browse/ONOS-5183)] - Protected intents can not be created on a cluster setup
* [[ONOS-5186](https://jira.onosproject.org/browse/ONOS-5186)] - Handle augment scenario in delete request
* [[ONOS-5189](https://jira.onosproject.org/browse/ONOS-5189)] - [ONOS-YMS-TEST] Null pointer check missing for Document
* [[ONOS-5196](https://jira.onosproject.org/browse/ONOS-5196)] - Packet request flows aren't removed when openflow app is deactivated
* [[ONOS-5207](https://jira.onosproject.org/browse/ONOS-5207)] - [ONOS-YMS-TEST] Unable to send notification event to YANG notification listeners
* [[ONOS-5216](https://jira.onosproject.org/browse/ONOS-5216)] - FUNCintent fails on adding point intent
* [[ONOS-5220](https://jira.onosproject.org/browse/ONOS-5220)] - FlowTest not found when using package from BUCK build
* [[ONOS-5259](https://jira.onosproject.org/browse/ONOS-5259)] - ClassCastException in OFChannelHandler
* [[ONOS-5260](https://jira.onosproject.org/browse/ONOS-5260)] - Issue With Meters REST API-GET APPID is printed as object and not the name, Prec level for REMARK BAND is 8 bits but is allowed as INT causing wrap round in the wireshark frame
* [[ONOS-5268](https://jira.onosproject.org/browse/ONOS-5268)] - Failed intents don't get recompiled to flows
* [[ONOS-5271](https://jira.onosproject.org/browse/ONOS-5271)] - Intent stuck in installing and withdrawing states
* [[ONOS-5277](https://jira.onosproject.org/browse/ONOS-5277)] - Devices get default flows for ARP even if proxyarp is not activated
* [[ONOS-5296](https://jira.onosproject.org/browse/ONOS-5296)] - metrics REST API (GET /metrics/{metricName}) results in NPE when the metric name is given wrong
* [[ONOS-5309](https://jira.onosproject.org/browse/ONOS-5309)] - Failed intents bounce between FAILED and WITHDRAWING states
* [[ONOS-5317](https://jira.onosproject.org/browse/ONOS-5317)] - ONOS probes hosts with ARP packets with broadcast source address.

## Story

* [[ONOS-1481](https://jira.onosproject.org/browse/ONOS-1481)] - Add exception handling to mininet driver functions
* [[ONOS-2810](https://jira.onosproject.org/browse/ONOS-2810)] - Support a distributed variant of java.util.TreeMap
* [[ONOS-2902](https://jira.onosproject.org/browse/ONOS-2902)] - SM-ONOS testing
* [[ONOS-3315](https://jira.onosproject.org/browse/ONOS-3315)] - Clean up TestON declaration comments
* [[ONOS-3428](https://jira.onosproject.org/browse/ONOS-3428)] - Implement "Brief" mode for Intent view.
* [[ONOS-3582](https://jira.onosproject.org/browse/ONOS-3582)] - Web UI - Persist last topology overlay
* [[ONOS-3677](https://jira.onosproject.org/browse/ONOS-3677)] - Implement "Brief" mode for Group view.
* [[ONOS-3678](https://jira.onosproject.org/browse/ONOS-3678)] - Implement "Brief" mode for Flow view.
* [[ONOS-3775](https://jira.onosproject.org/browse/ONOS-3775)] - Implement Netconf Alarms.
* [[ONOS-3852](https://jira.onosproject.org/browse/ONOS-3852)] - Discuss & decide how to move packet requests to FilteringObjectives
* [[ONOS-4059](https://jira.onosproject.org/browse/ONOS-4059)] - Analyze the REST framework requirement
* [[ONOS-4060](https://jira.onosproject.org/browse/ONOS-4060)] - Analyze the existing ONOS NBI framework
* [[ONOS-4150](https://jira.onosproject.org/browse/ONOS-4150)] - Use new topology for FUNCoptical
* [[ONOS-4159](https://jira.onosproject.org/browse/ONOS-4159)] - Implement Web user interface to accept path requirements and show output/query result
* [[ONOS-4304](https://jira.onosproject.org/browse/ONOS-4304)] - Analysis for YANG SBI Framework
* [[ONOS-4305](https://jira.onosproject.org/browse/ONOS-4305)] - Design for REST NBI Framework
* [[ONOS-4319](https://jira.onosproject.org/browse/ONOS-4319)] - Help GEANT testing ONOS with CORSA switches
* [[ONOS-4343](https://jira.onosproject.org/browse/ONOS-4343)] - Add Buck swagger target
* [[ONOS-4348](https://jira.onosproject.org/browse/ONOS-4348)] - Binary and bit array data type support
* [[ONOS-4350](https://jira.onosproject.org/browse/ONOS-4350)] - Inter Jar dependency
* [[ONOS-4351](https://jira.onosproject.org/browse/ONOS-4351)] - Augment Intra file linking
* [[ONOS-4353](https://jira.onosproject.org/browse/ONOS-4353)] - NBI REST mechanism (Restful/Restconf)
* [[ONOS-4383](https://jira.onosproject.org/browse/ONOS-4383)] - On mp2sp, treatment should be applied at the ingress of the network.
* [[ONOS-4386](https://jira.onosproject.org/browse/ONOS-4386)] - Add plugin framework to Buck
* [[ONOS-4387](https://jira.onosproject.org/browse/ONOS-4387)] - mp2sp intents should be able to support per connection point homogeneous selectors at the ingress
* [[ONOS-4457](https://jira.onosproject.org/browse/ONOS-4457)] - BGP Buckification
* [[ONOS-4459](https://jira.onosproject.org/browse/ONOS-4459)] - PCEP buckification
* [[ONOS-4460](https://jira.onosproject.org/browse/ONOS-4460)] - An instance that is partitioned away should cease to be MASTER for any device.
* [[ONOS-4481](https://jira.onosproject.org/browse/ONOS-4481)] - Integrate scalable gateway to openstackRouting
* [[ONOS-4482](https://jira.onosproject.org/browse/ONOS-4482)] - Implement dynamic add or remove of a gateway node
* [[ONOS-4501](https://jira.onosproject.org/browse/ONOS-4501)] - NPE in Partitions -c command when dynamically swapping nodes
* [[ONOS-4513](https://jira.onosproject.org/browse/ONOS-4513)] - Separate optical models into separate bundle/app
* [[ONOS-4519](https://jira.onosproject.org/browse/ONOS-4519)] - Build apidocs (per module) in buck build
* [[ONOS-4593](https://jira.onosproject.org/browse/ONOS-4593)] - sp2mp intents should be able to suport per connection treatments at the egress
* [[ONOS-4594](https://jira.onosproject.org/browse/ONOS-4594)] - On a single switch, I should be able to perform different treatments, depending on the egress port
* [[ONOS-4596](https://jira.onosproject.org/browse/ONOS-4596)] - Wrong error is thrown for missing semi colon for key inside a list.
* [[ONOS-4603](https://jira.onosproject.org/browse/ONOS-4603)] - Move BUCK global variables to single file
* [[ONOS-4636](https://jira.onosproject.org/browse/ONOS-4636)] - CLONE - 3894 [Defect of uses linking]
* [[ONOS-4645](https://jira.onosproject.org/browse/ONOS-4645)] - Implement the Kafka Module in Kafka Integration Application
* [[ONOS-4650](https://jira.onosproject.org/browse/ONOS-4650)] - [YANGUTILS] Implement must parser
* [[ONOS-4654](https://jira.onosproject.org/browse/ONOS-4654)] - NETCONF function for FUJITSU OLT #1
* [[ONOS-4666](https://jira.onosproject.org/browse/ONOS-4666)] - Make resource retrieval more efficient by specifying resource type
* [[ONOS-4668](https://jira.onosproject.org/browse/ONOS-4668)] - Refactoring port statistic collector using ScheduledExecutorService
* [[ONOS-4670](https://jira.onosproject.org/browse/ONOS-4670)] - Serialization of YANG Utils Metadata
* [[ONOS-4684](https://jira.onosproject.org/browse/ONOS-4684)] - Avoid extracting resource set from backing range set
* [[ONOS-4690](https://jira.onosproject.org/browse/ONOS-4690)] - containsKey in TransactionalMap
* [[ONOS-4691](https://jira.onosproject.org/browse/ONOS-4691)] - Pluggable ConfigOperator for Ports
* [[ONOS-4694](https://jira.onosproject.org/browse/ONOS-4694)] - YANG data tree interface development
* [[ONOS-4698](https://jira.onosproject.org/browse/ONOS-4698)] - Inefficient deserialization of EncodableDiscreteResources
* [[ONOS-4701](https://jira.onosproject.org/browse/ONOS-4701)] - YANG utils extension to auto-generate device schema
* [[ONOS-4710](https://jira.onosproject.org/browse/ONOS-4710)] - Kryo Exception: Class not registered
* [[ONOS-4711](https://jira.onosproject.org/browse/ONOS-4711)] - Cyclic dependencies removal
* [[ONOS-4712](https://jira.onosproject.org/browse/ONOS-4712)] - Inter jar linker unit test case
* [[ONOS-4719](https://jira.onosproject.org/browse/ONOS-4719)] - Environmental dependency removed from UT
* [[ONOS-4726](https://jira.onosproject.org/browse/ONOS-4726)] - [YANGUTILS] Implement when parser
* [[ONOS-4727](https://jira.onosproject.org/browse/ONOS-4727)] - [YANGUTILS] Implement feature and if-feature
* [[ONOS-4733](https://jira.onosproject.org/browse/ONOS-4733)] - Web UI: Settings Table - remove redundant information
* [[ONOS-4739](https://jira.onosproject.org/browse/ONOS-4739)] - Create a testcase for posting network configurations to the top level web resource
* [[ONOS-4746](https://jira.onosproject.org/browse/ONOS-4746)] - Add params option for TestON CLI
* [[ONOS-4747](https://jira.onosproject.org/browse/ONOS-4747)] - NETCONF function for FUJITSU OLT #2
* [[ONOS-4751](https://jira.onosproject.org/browse/ONOS-4751)] - Issue with creating Group(Type INDIRECT) with multiple bucket through REST API: REST API is successful
* [[ONOS-4759](https://jira.onosproject.org/browse/ONOS-4759)] - personal cell files should not be part of the ONOS repo.
* [[ONOS-4762](https://jira.onosproject.org/browse/ONOS-4762)] - [YANGUTILS] Grammar for meta data
* [[ONOS-4764](https://jira.onosproject.org/browse/ONOS-4764)] - Update TestON Documentation
* [[ONOS-4773](https://jira.onosproject.org/browse/ONOS-4773)] - Randomize app events in CHO test
* [[ONOS-4784](https://jira.onosproject.org/browse/ONOS-4784)] - MVN to make IDEA IDE automatically add generate-sources in target to sources.
* [[ONOS-4787](https://jira.onosproject.org/browse/ONOS-4787)] - Design review session for Virtual Network subsystem
* [[ONOS-4791](https://jira.onosproject.org/browse/ONOS-4791)] - Investigate STC intermittent failures
* [[ONOS-4795](https://jira.onosproject.org/browse/ONOS-4795)] - NETCONF function for FUJITSU OLT #3
* [[ONOS-4796](https://jira.onosproject.org/browse/ONOS-4796)] - Line number not shown in error info
* [[ONOS-4799](https://jira.onosproject.org/browse/ONOS-4799)] - Refactoring of code for java code generation in new package structure
* [[ONOS-4800](https://jira.onosproject.org/browse/ONOS-4800)] - Create testcases for testing openflow 1.3 features
* [[ONOS-4801](https://jira.onosproject.org/browse/ONOS-4801)] - Apply Device subsystem API change to gRPC service
* [[ONOS-4802](https://jira.onosproject.org/browse/ONOS-4802)] - On sp2mp, treatment should be applied at the egress of the network.
* [[ONOS-4806](https://jira.onosproject.org/browse/ONOS-4806)] - Refactor and debug IntentEventTp test
* [[ONOS-4829](https://jira.onosproject.org/browse/ONOS-4829)] - Augmented data method generator implmentation
* [[ONOS-4835](https://jira.onosproject.org/browse/ONOS-4835)] - Delete Group API doesnt work after new interpretation of GroupKey in REST interface
* [[ONOS-4837](https://jira.onosproject.org/browse/ONOS-4837)] - NETCONF function for FUJITSU OLT #4 and #5
* [[ONOS-4849](https://jira.onosproject.org/browse/ONOS-4849)] - NETCONF function for FUJITSU OLT #6
* [[ONOS-4850](https://jira.onosproject.org/browse/ONOS-4850)] - Enhance reproducibility of CHO test by recording and rerunning a list of CHO events
* [[ONOS-4856](https://jira.onosproject.org/browse/ONOS-4856)] - Rename PNAT to PAT
* [[ONOS-4870](https://jira.onosproject.org/browse/ONOS-4870)] - Cleanup onos-package Buck target
* [[ONOS-4871](https://jira.onosproject.org/browse/ONOS-4871)] - Fix gateway external port from list to single port
* [[ONOS-4875](https://jira.onosproject.org/browse/ONOS-4875)] - Recompute the default broadcast address from the subnet
* [[ONOS-4877](https://jira.onosproject.org/browse/ONOS-4877)] - Null pointer exception in FlowStatsCollector when device is connected and disconnected frequently from the controller
* [[ONOS-4894](https://jira.onosproject.org/browse/ONOS-4894)] - [YANGUTILS] Implement extension and argument datamodel and parser
* [[ONOS-4895](https://jira.onosproject.org/browse/ONOS-4895)] - Add a method in VirutalPortService to get virtual port based on mac address
* [[ONOS-4897](https://jira.onosproject.org/browse/ONOS-4897)] - Add flow duration check to functionality tests
* [[ONOS-4898](https://jira.onosproject.org/browse/ONOS-4898)] - Add VLAN encapsulation intents to Functionality tests
* [[ONOS-4899](https://jira.onosproject.org/browse/ONOS-4899)] - Documentation: How to deploy and walk through openstackSwitching
* [[ONOS-4900](https://jira.onosproject.org/browse/ONOS-4900)] - Documentation: How to deploy and walk through OpenstackRouting
* [[ONOS-4903](https://jira.onosproject.org/browse/ONOS-4903)] - Fix to load network-cfg.json on start-up for SONA apps
* [[ONOS-4925](https://jira.onosproject.org/browse/ONOS-4925)] - Debug SCPFscalingMaxIntents Test
* [[ONOS-4929](https://jira.onosproject.org/browse/ONOS-4929)] - Improvement: fix to not to create jersey client for every rest call
* [[ONOS-4939](https://jira.onosproject.org/browse/ONOS-4939)] - NETCONF function for FUJITSU OLT #7
* [[ONOS-4947](https://jira.onosproject.org/browse/ONOS-4947)] - Invalid name in case of qualified info for child nodes
* [[ONOS-4958](https://jira.onosproject.org/browse/ONOS-4958)] - Create simplified HA tests for ONOS.py
* [[ONOS-4959](https://jira.onosproject.org/browse/ONOS-4959)] - Improve SCPFscaleTopo Test
* [[ONOS-4961](https://jira.onosproject.org/browse/ONOS-4961)] - Improve SCPFswitchLat test
* [[ONOS-4962](https://jira.onosproject.org/browse/ONOS-4962)] - Improve SCPFportLat test
* [[ONOS-4964](https://jira.onosproject.org/browse/ONOS-4964)] - Investigate controller benchmarking methodologies from ONF and IETF
* [[ONOS-4973](https://jira.onosproject.org/browse/ONOS-4973)] - Handle pending SB & NB fix reviews
* [[ONOS-4990](https://jira.onosproject.org/browse/ONOS-4990)] - NETCONF function for FUJITSU OLT #8
* [[ONOS-4993](https://jira.onosproject.org/browse/ONOS-4993)] - Compilation error occurred for self resolution grouping with multiple uses.
* [[ONOS-4994](https://jira.onosproject.org/browse/ONOS-4994)] - Defect : compilation error occurs when namspace contains keyword.
* [[ONOS-5003](https://jira.onosproject.org/browse/ONOS-5003)] - Generated Code modification for YangUtils
* [[ONOS-5032](https://jira.onosproject.org/browse/ONOS-5032)] - Record a 'last seen' timestamp for hosts in the host store
* [[ONOS-5034](https://jira.onosproject.org/browse/ONOS-5034)] - Probe host before removing an IP address from it
* [[ONOS-5037](https://jira.onosproject.org/browse/ONOS-5037)] - Modify FUNCintentRest to test SinglePointToMultiPointIntent
* [[ONOS-5058](https://jira.onosproject.org/browse/ONOS-5058)] - Implement compiler annotations
* [[ONOS-5070](https://jira.onosproject.org/browse/ONOS-5070)] - Implement mirroring functionality
* [[ONOS-5071](https://jira.onosproject.org/browse/ONOS-5071)] - To add "remove-intent" feature in ONOS UI
* [[ONOS-5083](https://jira.onosproject.org/browse/ONOS-5083)] - YANG schema registry design
* [[ONOS-5095](https://jira.onosproject.org/browse/ONOS-5095)] - RPC's substatements java code is generating in src/main/java folder rather than target.
* [[ONOS-5109](https://jira.onosproject.org/browse/ONOS-5109)] - Update ONOS System Test Plans on Wiki
* [[ONOS-5111](https://jira.onosproject.org/browse/ONOS-5111)] - Calculate Standard Deviation in Switch/Port Latency Test
* [[ONOS-5112](https://jira.onosproject.org/browse/ONOS-5112)] - Leafref not able to find path in standard yang file.
* [[ONOS-5115](https://jira.onosproject.org/browse/ONOS-5115)] - Design protected path modelling
* [[ONOS-5119](https://jira.onosproject.org/browse/ONOS-5119)] - Clean up code style in Functionality Tests
* [[ONOS-5121](https://jira.onosproject.org/browse/ONOS-5121)] - Update FUNCovsdbtest
* [[ONOS-5127](https://jira.onosproject.org/browse/ONOS-5127)] - Solve wireless AP issues
* [[ONOS-5139](https://jira.onosproject.org/browse/ONOS-5139)] - Invalid holder error occurred for must.
* [[ONOS-5143](https://jira.onosproject.org/browse/ONOS-5143)] - LinkCollection redesign
* [[ONOS-5152](https://jira.onosproject.org/browse/ONOS-5152)] - Encoder for Disjoint Rest API in ONOS is not implemented- ONOS-1.7
* [[ONOS-5155](https://jira.onosproject.org/browse/ONOS-5155)] - To expose port delta statistics via Device REST service
* [[ONOS-5158](https://jira.onosproject.org/browse/ONOS-5158)] - Allow to remove gateway nodes using network config.
* [[ONOS-5184](https://jira.onosproject.org/browse/ONOS-5184)] - New parameter for onos-form-cluster to specify partition size
* [[ONOS-5237](https://jira.onosproject.org/browse/ONOS-5237)] - Write the new ProxyARP module for SDN-IP
* [[ONOS-5238](https://jira.onosproject.org/browse/ONOS-5238)] - Write the new ProxyARP module for VPLS
* [[ONOS-5254](https://jira.onosproject.org/browse/ONOS-5254)] - JUNIT mocks for FUJITSU NETCONF
* [[ONOS-5269](https://jira.onosproject.org/browse/ONOS-5269)] - JUNIT for FUJITSU NETCONF (ponlink)
* [[ONOS-5281](https://jira.onosproject.org/browse/ONOS-5281)] - JUNIT for FUJITSU NETCONF (device-controllers)
* [[ONOS-5299](https://jira.onosproject.org/browse/ONOS-5299)] - Need to be able to get the GIT commit ID used for an onos build
