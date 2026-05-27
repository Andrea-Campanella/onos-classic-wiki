# Segment Routing for ONOS 1.2

# Requirements

The following are missing functionality in onos platform that is needed for Segment Routing use case:

* Multiple table support

+ SPRING-OPEN needs the following pipeline processing

- |- IPv4 unicast table ---|
- vlan table ---> tmac table --->|                                      --->acl table
- |- MPLS unicast table -|

+ The ONOS TrafficSelector has the support for IPv4 destination and MPLS label based match conditions

- MPLS BoS (Bottom of Stack) match condition to be added to Traffic Selector criteria (MplsCriterion class should be modified/extended)

+ DefaultFlowRule class to be extended to include table IDs in the Flow Rule

* Switch specific processing

+ Flow Table IDs for (IPv4, MPLS, VLAN, TMAC, ACL...etc) will differ depending on the underlying switch

* Network Configuration Manager functionality

+ Device type (Switch/Router/Segment Router)
+ Router MAC
+ Router loopback IPv4 address
+ Router/Node Segment Id (SId)
+ Router subnets (if any)
+ IsEdgeRouter
+ Router name
+ Adjancency Segment Ids

* OF1.3 Group support

+ Default groups
+ Group chaining
+ Recovery from failures

* New TrafficTreatment Instructions:

+ OUTGROUP
+ Push MPLS with label and eth type
+ Pop MPLS
+ Decrement IP TTL
+ Decrement MPLS TTL
+ Copy In/Out TTL

Few other questions to keep in mind:

* CLI - we can keep our CLI as a separate project -- need to ensure that the rest API calls we need are implemented in onos-next -

+ probably in the app and in the statistics service
+ also needs to see how Karaf CLI is affected by segment routing

* GUI

+ how can we avoid some of the GUI based intent creation?
+ how can we display tunnels or policies?
+ can we display router config in the GUI?

* Stats

+ must find a way to get port-stats, group-stats and per-table flow stats

* Move from EQUAL to SLAVE

+ need to change OpenFlow Controller to use SLAVE

* State info in controller if doing default routing in Intent Service

+ probably not a good idea
+ can intent service be made stateless?

* Any issues doing policy routing with the Intent Service?

+ Only one instance of controller does policy and policy is implemented in only one switch -- so is there are need to use the intent service? Is there any harm?

* TTP Driver -

+ we need to remove all intelligent group handling from driver -possibly because I think we concluded that app needs to know everything about group - is this still the case?
+ what about the adjacency id stuff?
+ What about the neighborSet stuff - if group handling is in app, do we still need it?

* Multi-instance issues (just need to keep in mind)

+ HA - when master fails

- what happens to policy routing?
- what happens to default routing?

+ Scale -- need to able to work in parallel with multi-masters for default routing

- must ensure that dst-rooted-in-trees is used for default routing

# High Level Architecture Proposal

The below figure depicts the high level architecture of Segment Routing application on ONOS platform (Not all subsystem are shown in the figure).  It uses the following services of ONOS subsystems:

* + Topology service
  + Device service
  + Link service
  + Flow rule service
  + Packet service

![](https://lh5.googleusercontent.com/P1s0LVMC8ZRerDWKsm7opIAfkMzRxARCY4mv5XizZpS0vi8qutnbkhaDZcA4ZyMjjAls0EriLbbqdxC0vhqeIwjI2NH0JuU_srzHFNS8Dfmp4w5IoVypId18hOPxSxH-_A)

New subsystems to be introduced in ONOS-core to be used by applications like Segment Routing application that uses Group constructus in the underlying network elements: 

* Group Subsystem

+ Group store follows the same semantics of Flowrule store. i.e.

- Master instance of device will have ownership over groups with replicas available in Slave instances for fast failover

+ Provides the Group descriptions and Group statistics from devices
+ Creates Group chains
+ Support recovery of groups when ports go UP/DOWN

# Design

* [Multiple Table Support](segment-routing-for-onos-1.2/multi-table-aware-flowruleservice-subsystem.md)
* [Group subsystem](segment-routing-for-onos-1.2/group-subsystem.md)
* [Segment Routing Application Design](segment-routing-for-onos-1.2/segment-routing-application-design.md)
