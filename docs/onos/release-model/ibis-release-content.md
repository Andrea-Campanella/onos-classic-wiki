# Ibis Release Content

# ONOS Ibis Release Content

**CSIRO / University of New South Wales**

* CaSToR: new application to manage SDX (Himal Kumar, Craig Russel, Vijay Sivaraman)

**ETH Zurich**

* FatTree simulator, extended NullProviders.java and cli null control command (Andreas Pantelopoulos)

**Fujitsu**

* Alarm Consumer for Fujitsu OLT (Liang Xue)

**Huawei**

* ACTN TE Topology APP Implementation (Aihua Guo, Yixiao Chen, Henry Yu, Hesam Rahimi)
  + Receives multiple TE topologies from SB provider, and merge into one native TE topology; stores both original, received TE topologies and the native topology in TE topology data store; provides APIs for NB APP to retrieve and display the TE topologies.
  + IETF TE Topology Provider
  + TE Topology NBI app YANG notification support
* ACTN TE Tunnel Implementation (Aihua Guo, Cheng Fan, Liu Tao, Chen Qinghui)

  + IETF TE Tunnel Manager app, supporting multi-domain tunnel provisioning using the standard IETF YANG TE tunnel model
  + IETF TE Tunnel South-bound Provider app
  + TE Tunnel NBI app and YANG notification support
* Enhanced YANG Management System (YMS) in ONOS (Gaurav, Vinod, Bharat, Vidya, Janani, Sonu, Rama, Shankara, Mahesh)
  + Added support to automate NBI CODEC for CURD operations including advanced YANG constructs.
  + Added support to automate SBI CODEC for CURD operations including advanced YANG constructs.
  + Added support to automate CODEC for RPC and Notification.
  + Added BUCK support.
  + Added support for Inter-JAR.
* Enhanced YANG Tools (Gaurav, Vinod, Bharat, Vidya, Janani, Sonu, Rama, Shankara, Mahesh)
  + Changed code generation under "YANG Grouping" rather then "YANG Uses" for better code re-usability.
  + Added support for BUCK.
  + Refactored to support any build/runtime environment.
  + Enhancements to support improvement of performance of YMS.
* Implement RESTCONF client, server (Hesam Rahimi, Cheng Fan)
* Adding support for VLAN\_PUSH with EtherType (incl. Q-in-Q) (Konstantinos Kanonakis)
* Introduced L2SwitchVlanConfigBehaviour to manage VLANs on legacy L2 switch devices (Konstantinos Kanonakis)
* Introduced BandwidthProfileConfigBehaviour to manage policers/markers (Konstantinos Kanonakis)
  + Created BandwidthProfile class to represent generic policers/markers
  + Created BandwidthProfileAction class to represent color actions (green/yellow/red)
  + Created DscpClass and IPPrecedence Enums
* Added esc key handlers for cluster details panel (Viswanth KSP)
* Dynamic Config Service & store API definitions [Sithara Punnassery]

**I2CAT Foundation**

* Adds loose filtering capability (-f) to cli commands (intents, flows) - Multi-valued filtering - Two search strategies (Carolina Fernandez)

**KISTI/KREONET ?**

* Initial Contribution to New VPLS NeighbourHandler to support multiple VLANs **(Yong-Hwan Kim)**

**NCTU/Inventec**

* Intents w/ FilteredConnectPoint- a new abstraction to model what the traffic should look like at the network edge - MP2SP and SP2MP have moved to this abstraction (Yi Tseng)
* New VPLS NeighbourHandler to support multiple VLANs (Yi Tseng)
* New VPLS application to support VLAN translation (Chun-Ming Ou, Huai-Wen Hsu, Wei-Cheng Wang, Yi Tseng)
* New VPLS CLI (Chun-Ming Ou, Huai-Wen Hsu, Wei-Cheng Wang, Yi Tseng)

**NEC**

* Config utility class for JSON handling (Yuta HIGUCHI)

**Nokia**

* add pipeline for nokia olt device (Han Ke)

**ON.Lab**

* Consistent document tree (Madan Jampani, Aaron Kruglikov)
* Adding serializer for FilteredConnectPoint (Brian O’Connor)
* Completion of Buck Build (Brian O’Connor, Ray Milkey, Thomas Vachuska, others)
* Trellis Fabric enhancements (Saurav Das, Charles Chan, Pier Luigi Ventre, Flavio A. Castro)
  + Test improvement
    - Improved existing tests
    - Implemented new testing scenarios: dynamic config and HA
    - Improved the resiliency of the Fabric
  + Implement OFDPA 3 pipeliner
    - Bumped OpenFlowJ version to 0.9.7
      * Added OFDPA3 oxms (QoS index, MPLS L2 port, OVID, MPLS type)
      * Added OFDPA3 actions (Push/PoP L2 Header, Push/Pop Cw)
    - Implemented MPLS Termination
  + Miscellaneous
    - Blocked ARP request from hosts belong to different subnet
    - CLI command that shows all configured subnets
    - Improved route population
    - MPLS ECMP configurable

* HostLocationProvider enhancement (Charles Chan)
  + Enable host learning from DHCP packets
* RouteService enhancement (Charles Chan)
  + Support static route configuration via REST API
  + Improve the argument description in RouteRemoveCommand
* IGMPv2 support (Brian O’Connor)
* GUI (Simon Hunt, Steven Burrows, Viswa KSP)
  + Changes in support of regions, basic region configuration
  + Resubmit Intent function added to the Intents View
  + GUI new Icons
  + Cluster Details panel showing node properties
* Treemap primitive enhancements (Aaron Kruglikov)
* Creation of unique subsystem for label (MPLS/VLAN) allocation (Pier Luigi Ventre)
* P2P and H2H have moved to the FilteredConnectPoint (Pier Luigi Ventre)
* Creation of LinkCollection compiler a unique compiler for H2H, P2P and MP intents (Pier Luigi Ventre)
* VLAN tagging support for SDN-IP (Luca Prete)
* Improved encapsulation for P2P intents (Pier Luigi Ventre)
* Support for encapsulation in SP2MP and MP2SP intents (Pier Luigi Ventre)
* Support for encapsulation in VPLS (Luca Prete)
* Optimized chain of actions for the MP intents (Pier Luigi Ventre)
* MPLS BoS decoding (Pier Luigi Ventre)
* NeighbourResolutionService improvements (Pier Luigi Ventre)

**POSTECH**

* LISP SBI Support (Jian Li, Yoonseon Han)
  + Add LispDeviceProvider which launches LISP controller
  + Add lisp providers and protocols into modules.defs
  + Support more LCAF addresses
    - Add LISP Traffic Engineering LCAF address with unit tests
    - Add LISP NAT LCAF address with unit tests
  + Add LISP MAC SHA1 and SHA256 authentication mechanisms
  + Implement MapServer and MappingDatabase
    - Handle Map-Register, Info-Request control message
  + Implement MapResolver
    - Handle Map-Request inside Encapsulated Control Message (ECM)
  + Add LISP channel pipeline along with server bootstrap
  + Support CIDR ranged match for LISP EidRlocRecord
  + Add more control message type with serialization capability
    - Encapsulated Control Message (ECM)
    - Info-Request, Info-Reply
  + Make LISP authKey and authKeyId be configurable
  + Improve message processing throughput using Epoll NIO

**Waltz Networks**

* FlowRuleStore: add purgeFlowEntries (Victor Silva)
* MastershipLoadBalancer: listen to RegionEvents
* GroupStore: add purgeGroupEntries

**Wipro Technologies**

* Highlighting intents in ONOS GUI for selected links (Prince Pereira)

**ZNYX Networks**

* Invokes standard Ofdpa3 driver set for ZNYX hardware implementation (Alan Deikman)
