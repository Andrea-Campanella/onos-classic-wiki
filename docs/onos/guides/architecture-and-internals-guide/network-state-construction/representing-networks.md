# Representing Networks

This section describes how ONOS internally represents the infrastructure under its control.

## Overview

ONOS maintains protocol-agnostic and protocol-specific network element and state representations that can be translated from one to the other. The former are constructs of the core tier, referred to as ***Model Objects***, and the latter are constructs of the appropriate provider. For example, `DeviceStore` (and consequently the `DeviceManager` and `DeviceListeners`) sees a network device as a `Device`, whereas the `OpenFlowDeviceProvider` will see the device as an `OpenFlowSwitch`. Recall that these two representations are bridged across the provider and core layers by the intermediate transcription into a `DeviceDescription.` Model Objects are what ONOS exposes to its applications.

Additionally, wherever possible, rich data types are used instead of Java primitives for disambiguation and clarity. For example, IP Addresses are described by the `IPAddress` class, as opposed to an `int`, and MAC addresses, with `MACAddress`, rather than a `byte[]` or `long.`These rich data types provide methods to convert the object into analogous primitives where needed.

The rest of this section focuses on the Model Objects.

## Model Object Types

The interface definitions and implementations of these objects can be found across several packages under [org.onosproject.net.\*]. While not formal, implicit object classifications fall out of the organization of these packages.Note that the following list is not comprehensive.

### Network Topology

Many of the model objects have graph analogues, as ONOS represents networks as directed graphs.

* *Device* - A network infrastructure element, e.g. a switch, router, access-point, or middle-box. Devices have a set of interfaces/ports and a `DeviceId`. Devices are interior vertices of the network graph.
* *Port -* A network interface on a Device*.* A Port and `DeviceId` pair forms a `ConnectPoint`, which represents an endpoint of a graph edge.
* *Host* - A network end-station, which has an IP address, MAC address, VLAN ID, and a `ConnectPoint`. Hosts are exterior (leaf) vertices of the network graph.
* *Link* - A directed link between two infrastructure Devices (`ConnectPoints`). Links are interior edges of the network graph.
* *EdgeLink* - A specialized Link connecting a Host to a Device. EdgeLinks are exterior edges of the network graph.
* *Path* - A list of one or more adjacent Links, including EdgeLinks. EdgeLinks, if present in the path, can only be exterior links (beginning and end of the list).
* *Topology* - A Snapshot of a traversable graph representing the network. Path computations against this graph may be done using an arbitrary graph traversal algorithm, e.g. BFS, Dijkstra, or Bellman-Ford.

### Network Control

At the application level, directives for the network are expressed as high-level flow rules given as Criteria (Match) and Treatment (Action) pairs. An ONOS instance will have a role for any given device that either allows or denies it from applying changes to the device.

* *FlowRule* - A high-level flow rule given as a Match and Action pair. An action can be a composite action if needed. This abstraction is distinct from OpenFlow's notions of flow rules, e,g, the number of tables and OF match-action pairs.
* *Intent* - A high-level intent to affect network configuration or connectivity for a subset of network traffic. It allows applications to specify *what* they want to happen, rather than having to specify *how* they want things to happen.
* *RoleValue* - The role of (an) ONOS instance(s) for a device.

Constructs for manipulating network logic, as well as their construction, are discussed further in [Intent Framework](../intent-framework.md). Roles are explained in [Cluster Coordination](../distributed-operation/cluster-coordination.md).

### Network Packets

Packets, such as from network traffic, and those to be injected into the network, have analogues to the OpenFlow PacketIn and PacketOut. 

* *OutboundPacket* - Protocol agnostic representation of a synthetic packet to be emitted on the network. This includes information about where to emit this packet.
* *InboundPacket* - Protocol agnostic representation of a packet sent to the controller by a device. This enables reactive packet processing by making *PacketIn*s available to providers and applications to use as needed, e.g. host tracking, link detection.

### Model Object Dependencies

Some entities rely on the existence of other entities, as in the case of Ports, which cannot exist without a Device. Similarly, Links, and by extension, Topologies, cannot exist without Ports serving as endpoints to the Link. We therefore consider Devices to be a first-class entity in ONOS's network representations.

---

[Previous : System Components](../system-components.md)  
[Next : The Device Subsystem](../device-subsystem.md)

---
