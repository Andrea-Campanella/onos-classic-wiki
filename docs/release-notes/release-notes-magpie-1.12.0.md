# Release Notes - Magpie 1.12.0

# Features List

## CORE

* Improved failure detection for faster mastership election times
* Migration of all distributed primitives to Atomix
* Raft log compaction optimizations
* Offline backup/restore

## ISSU Brigade

* ISSU architecture documentation
* ISSU protocol prototype
* Foundation for in-place rolling upgrades
* Offline backup/restore tooling
* Primitive state isolation
* Communication isolation
* Upgrade lifecycle management commands
* Upgrade failure detection
* Support for rolling back upgrades
* Application store upgrades

## Dynamic Configuration Brigade

* Design/refactoring of the store to address deficiencies discovered from device sync work
* Device Synchronizer design - operational state to app missing, north to south in place

## P4 Brigade

* Demo

+ ONOS controlling a Tofino-based leaf-spine fabric via P4Runtime running Google’s tor.p4 Video: <https://www.youtube.com/watch?v=BE_y-Sz0WnQ>

* Support for P4 action profiles/groups (enables control of ECMP-like forwarding behaviours)
* Support for mastership arbitration
* P4Runtime driver support for ONOS multi-instance
* Added device driver for Barefoot Tofino
* PI framework refactoring

## gRPC Brigade

* Added

+ LinkService
+ HostService
+ MeterService
+ ComponentConfigService
+ RegionService
+ ApplicationService

* Support gRPC service registration with static binding mechanism

## GUI Brigade

* Application View filter
* Added Details Panel for Ports, Meters, and Groups views

## LION Brigade

* Proof-of-concept translations for some core views: Spanish, French, Italian, Korean, Turkish, Simplified and Traditional Chinese. Plus Greek ongoing...

## Network Virtualization Brigade

* Virtualization core - distributed virtual flow rule store added
* OFAgent handles PORT\_MOD, FLOW\_MOD, GROUP\_MOD, METER\_MOD messages
* Log filtering per OFAgent tenant capability is now available
* External Connectivity to allow communications between other networks (I.e., other virtual networks, Internet)
* STC tests for virtual networks added

## Teaching Brigade

* ONOS Build tutorials
* ONOS Build videos being processed to provide easy to use session-based tutorials

## Security and Performance Analysis Brigade

* First report has been published as ONF Informational Report  
  <https://www.opennetworking.org/software-defined-standards/informational/>
* Working on the second report with tests update on latest release + NETCONF SBI tests

## Packet Optical

* Additional device support by Equinix, Polatis, OpLink
* Support for PowerConfig API on Polatis device
* REST API to allow application outside ONOS to access PowerConfig API
* Ciena transponder supports more API/Behaviours & protocol options

## New Use Cases

* Simple Fabric : Intents based leaf-spine fabric application for physical switches.

# Jira Details

Release Notes - ONOS - Version 1.12.0

\*\* Sub-task

   \* [ONOS-6963] - Show Pipeconf name in device detail view

   \* [ONOS-6964] - Create pipeconf information view

   \* [ONOS-6966] - Pipeconf codec

   \* [ONOS-7026] - Show table name if the table id of a flow is PiTableId

   \* [ONOS-7117] - Support configuring LeaderElector primitive's timeouts

\*\* Bug

   \* [ONOS-4761] - Optical network state

   \* [ONOS-6551] - [ONOS\_L3VPN\_SERVICE] Tunnel creation support for l3vpn service

   \* [ONOS-6897] - Investigate 0 Throughput rate from the intent with 5 nodes.

   \* [ONOS-6899] - Links may vanish durning node failure due to default timeouts

   \* [ONOS-6937] -  Cluster metadata file is not read even after correcting invalid data

   \* [ONOS-6941] - Insert fromStringMethod for derived identities

   \* [ONOS-6979] - YANG Compiler : Binary type handling in data node.

   \* [ONOS-6981] - YANG Runtime : Processing of uses in module node, which becomes model object, has problem in YTB.

   \* [ONOS-6985] - NPE at OltPipeline if IP proto is not specified

   \* [ONOS-6989] - (vCore) VirtualNetworkMeterStore - ServiceNotFoundException thrown in VirtualNetworkMeterManager constructor

   \* [ONOS-7007] - Cannot write device tree elements to Dynamic Config subsystem

   \* [ONOS-7023] - [ONOs-YANG]Error returned after sending json input

   \* [ONOS-7024] - Atomix 2.x timeouts

   \* [ONOS-7025] - Restore old DistributedFlowRuleStore for testing

   \* [ONOS-7048] - Topo 2: Link details panel is not rendering correctly

   \* [ONOS-7078] - Relying on both name and alias for P4Runtime message encoding/decoding produces inconsistencies

   \* [ONOS-7106] - Cannot XML serialize OpenConfig model

   \* [ONOS-7118] - OVSDB Port can not be scan or block in the get() action

   \* [ONOS-7124] - Race condition when trying to remove a disconnected device from ONOS

   \* [ONOS-7136] - Alarms are not removed when device is disconnected

   \* [ONOS-7146] - InterfaceManager fails to load interfaces from storage after ONOS is restarted.

   \* [ONOS-7147] - [ONOS\_YANG\_TOOLS]list inside a config=false container, the key attribute does not seem to be getting recognized properly

   \* [ONOS-7161] - Flows stuck on pending\_add after bring the link down

   \* [ONOS-7163] - ONOS Cluster is not stable yet !

   \* [ONOS-7174] - ONOS 1.12.0-SNAPSHOT HP driver doesn't work with HP3800 in Janet lab

   \* [ONOS-7176] - Driver service not bound errors

   \* [ONOS-7199] - Augmenting Standard YANG models is a problem

   \* [ONOS-7200] - GUI Build rules are not noop causing buck build to take longer than expected

   \* [ONOS-7202] - IntentCleanupTestMock always fail in jenkins test

   \* [ONOS-7206] - PartitionMember can not add dynamically

   \* [ONOS-7207] - Flows exists even if the devices are not available

   \* [ONOS-7209] - Driver for HP3800 doesn't work with ONOS 1.12.0-SNAPSHOT

   \* [ONOS-7210] - UI doesn't show button to create intents

   \* [ONOS-7213] - New cluster configuration cannot be serialized to JSON on configuration change

   \* [ONOS-7214] - Partition data not deleted after cluster reconfiguration

   \* [ONOS-7219] - Single node ONOS from Docker image can't read cluster metadata

   \* [ONOS-7238] - ICMP checksum error of fabric.p4

   \* [ONOS-7244] - Discover the issue with the missing host after arping.

# 

\*\* Story

   \* [ONOS-5407] - Ports View - add detail panel

   \* [ONOS-5409] - Meters View - add detail panel

   \* [ONOS-5463] - (OFAgent) Handle LLDP

   \* [ONOS-5891] - Design a suitable mechanism for the handling of the Meters

   \* [ONOS-6657] - Topo2: Implement host friendly name

   \* [ONOS-6673] - YANG Runtime: GET API's for YANG Models

   \* [ONOS-6745] - Initial Sketch of DeviceSynchronizer

   \* [ONOS-6748] - Final porting of old ecmp.p4 demo application to new PI APIs

   \* [ONOS-6751] - Implement upgrade service

   \* [ONOS-6810] - Implement State Distribution In PiPipeconf Service

   \* [ONOS-6818] - Rename default.p4 to avoid confusion with DefaultPiPipeconf implementation

   \* [ONOS-6836] - Implement DeviceHandshaker for Tofino Switch

   \* [ONOS-6837] - Implement Flow Rule Programmable for Tofino

   \* [ONOS-6839] - Implement Packet Programmable for Tofino

   \* [ONOS-6855] - Draft implementation of ecmp2.p4 app

   \* [ONOS-6856] - Interpreter implementation for ecmp2.p4

   \* [ONOS-6867] - Update BMv2 model parser tests to work with updated default.json

   \* [ONOS-6877] - Allow filtering ports with heavy traffic

   \* [ONOS-6891] - Fix ResourceIds#relativize when Yang tools 2.2.0-b4 or later is released

   \* [ONOS-6914] - Shim to convert existing DynamicConfigEvent to ideal form

   \* [ONOS-6915] - NETCONF DeviceSynchronizer XML serializer

   \* [ONOS-6935] - ActionProfile supports in P4RuntimeClient

   \* [ONOS-6944] - Restarted dispatch loop become stopped when event sink exceeded execution time limit in CoreEventDispatcher

   \* [ONOS-6962] - UI support for pipeconf programmable device

   \* [ONOS-6978] - Establish a way to create a device yang tree object for testing

   \* [ONOS-6982] - Implement OpenStackNetworking UI Service

   \* [ONOS-6983] - Complete Italian Localization ahead of OB

   \* [ONOS-6984] - Deck of Slides for Berlin DT event

   \* [ONOS-7001] - Support for flow table counters in P4Runtime

   \* [ONOS-7003] - Implement policer abstraction

   \* [ONOS-7006] - Slides for Introduction to ONOS at P4 Brigade

   \* [ONOS-7008] - Migrate ONOS primitives to Atomix

   \* [ONOS-7009] - Document ISSU protocol

   \* [ONOS-7010] - Setup ISSU brigade Google Group

   \* [ONOS-7011] - Setup ISSU brigade wiki

   \* [ONOS-7012] - Setup ISSU brigade Slack channel

   \* [ONOS-7014] - Create backlog of ISSU tasks from protocol documentation

   \* [ONOS-7018] - Presentation for ONOS Build 2017

   \* [ONOS-7020] - fix some of netconf SBI design issues

   \* [ONOS-7028] - Review Security and Performance Brigade Report

   \* [ONOS-7033] - YANG Compiler: Support for Anydata parsing

   \* [ONOS-7039] - Fix PEP8 Warnings in TestON

   \* [ONOS-7042] - Value validation as per defined datatype restriction and pattern

   \* [ONOS-7044] - Create Gerrit triggered Jenkins Job that checks PEP8 formatting in incoming TestON commits

   \* [ONOS-7052] - Debug CHO failures with ONOS up/down events

   \* [ONOS-7053] - Investigate on DELTA test failures

   \* [ONOS-7054] - Upgrade protocol prototype

   \* [ONOS-7055] - Upgrade protocol tests

   \* [ONOS-7056] - Document forwarding behaviour of ecmp2.p4 for 2x2 Clos topo

   \* [ONOS-7057] - Final implementation and testing of app for ecmp2.p4

   \* [ONOS-7058] - Review and clean-up of PI Framework and P4Runtime subsystem

   \* [ONOS-7060] - Document for demo setup at L123

   \* [ONOS-7061] - Investigation work for gNMI support

   \* [ONOS-7062] - Restore testing on old flow rule store

   \* [ONOS-7063] - Validation of modelId for valid syntax

   \* [ONOS-7068] - Upgrade Atomix

   \* [ONOS-7069] - Create Google Doc to help next QA interns get set up efficiently

   \* [ONOS-7074] - Investigate SCPFscaleTopo where it always fails at scale 40

   \* [ONOS-7079] - setup new P4 hardware env in lab

   \* [ONOS-7081] - Modify EventuallyConsistentMap to bootstrap from old nodes during upgrade

   \* [ONOS-7083] - Handle application version changes in upgrades

   \* [ONOS-7085] - Transition upgrade state back to INACTIVE after upgrade

   \* [ONOS-7086] - Upgrade failure detection

   \* [ONOS-7088] - Redistribute partitions after upgrade is complete

   \* [ONOS-7089] - Ensure new Raft nodes are caught up before being added to the quorum

   \* [ONOS-7091] - Investigate OpenConfig model

   \* [ONOS-7092] - Investigate HA Test Failures

   \* [ONOS-7093] - Add ISSU permissions

   \* [ONOS-7094] - Delete old partitions on upgrade commit

   \* [ONOS-7098] - Rebalance masters on upgrade commit/reset

   \* [ONOS-7100] - Improve mastership election times

   \* [ONOS-7101] - Integrate Jenkins to Slack to notify the information.

   \* [ONOS-7102] - Investigate FUNCintent Failure

   \* [ONOS-7104] -  Fix files that were affected by the style check script in TestON

   \* [ONOS-7112] - Investigate SCPFswitchLat failure, fix the issue, and file the bug

   \* [ONOS-7113] - Adding values to the bars on the wiki test result graphs.

   \* [ONOS-7114] - Meter Subsystem Refactoring

   \* [ONOS-7116] - Create MeterProgrammable and MeterDriverProvider

   \* [ONOS-7125] - Add functionality that checks intents withdraw/install successfully for the SCPFintentInstallWithdrawLat

   \* [ONOS-7128] - Putting fabric.p4 to ONOS codebase

   \* [ONOS-7129] - fabric.p4 pipeliner

   \* [ONOS-7131] - Add Interpreter for fabric.p4

   \* [ONOS-7132] - Test basic functionality of segment routing on fabric.p4

   \* [ONOS-7135] - Implement changePortState Netconf Device Provider

   \* [ONOS-7143] - Add arbitrationUpdate method to P4RuntimeClient

   \* [ONOS-7144] - Membership CLI Command

   \* [ONOS-7145] - Remove warnings and fix comments on the R scripts that generate test result wiki graphs

   \* [ONOS-7148] - Video of P4Runtime Demo at NFV/SDN

   \* [ONOS-7158] - Clean up ONOS data directories for simple backup/recovery

   \* [ONOS-7166] - Send the number of the failed case to the slack from Jenkins

   \* [ONOS-7167] - Change all SCPF front page graphs to display 50 builds

   \* [ONOS-7175] - Refractor R Scripts that generate wiki test result graphs in TestON

   \* [ONOS-7196] - Making a separate database, graph and Wiki page for the old flow rules result

   \* [ONOS-7205] - Investigate SCPF Mastership Failover Latency's Timing Issue

   \* [ONOS-7218] - fabric.p4 unit tests

   \* [ONOS-7221] - Upgrade state tests

   \* [ONOS-7225] - Fix/Add graphs on individual test wiki pages (FUNC, HA, USECASE)

   \* [ONOS-7232] - Origin not mentioned in BUCK file of faultmanagement app

   \* [ONOS-7236] - Supports IPv4 routing on fabric.p4

   \* [ONOS-7246] - Create Test Result Wiki Pa
