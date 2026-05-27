# Network Discovery

## Overview

Given certain types of devices, links, and hosts, the network topology may be discovered by ONOS with little administrator intervention. An example is a device that is configured to connect automatically to a specified controller using a protocol such as OpenFlow. When it establishes a connection with the latter, it will 'see' the device and add it to its view of the network. Depending on the protocol used to establish this connection, further information, such as device capability and number of ports, may also be conveyed to the controller through a series of messages in a *handshake*.

In order to discover links and hosts, ONOS relies on the ability to collect information from, and to configure, network devices. This section focuses on the discovery of those elements, given that ONOS already has control over the devices. The details of how ONOS discovers and interacts with devices are discussed in the [Device Subsystem](../device-subsystem.md).

## Link Discovery

Links are discovered on a hop-by-hop basis using probe frames sent out of all controlled devices on all ports. The device ID of the sending device is added to the probe, to identify one end of a link. The other end is found once a neighboring device receives the probe, sending it back to the controller. For example, given devices A and B which are controlled by the same controller and connected together by a direct link, the link from A to B is found via the following steps:

1. The controller constructs a probe containing A's device ID.
2. The controller sends down a PacketOut directive with the probe as the payload.
3. A receives the directive and sends the probe out on all of its ports.
4. B receives A's probe, and sends it back to the controller.
5. The controller receives the probe that it had sent from A, from B. It has found one network hop.

The same step of events allow the controller to find the reverse link direction, from B to A. Links are found one direction at a time, as links cannot be assumed to be bidirectional.

The Link Subsystem interfaces with the Device subsystem via a **`LLDPLinkProvider`** that subscribes to the `DeviceService` for `DeviceEvents` (i.e. by implementing a DeviceListener), and polling for information about OpenFlow-capable Devices. The `LLDPLinkProvider` allocates a **`LinkDiscovery`** object per discovered Device.

`LinkDiscovery` implements the actual mechanism for link discovery via LLDP and BDDP messages. Every *proberate* milliseconds (default 3000ms), a `LinkDiscovery` instance sends out probe messages containing LLDPs and BDDPs, as *PacketOuts* via the Device that it is paired with. A probe message intercepted at an adjacent switch is passed, as *PacketIns*, to their corresponding `LinkDiscovery` instance, which corresponds the sender and receiver of the probe message as the source and destination endpoints of a directed link.

### SDN islands and legacy networks

SDN *islands* are subsections of networks that are SDN controlled. Each island may have one or more hops through a legacy network in between it and another island.

LLDP probes are dropped after one network hop on both SDN controlled and legacy networks. This may prevent connections between two islands from being discovered, causing a controller to believe that it is managing two disjoint networks. ONOS, like Floodlight, uses BDDP probes to discover paths between islands. While legacy devices do not drop BDDPs, they also do not mark them in any way, i.e., they behave as transparent relays. Therefore, connections across legacy networks will appear as single hops regardless of how many legacy devices may be along that path.

### Control domains

Multiple independent control planes control neighboring sections of network in a *multi-domain* setting. Domains differ from network islands, in that the latter are controlled by one logical control plane. In the former, a controller might receive probes that it (or its cluster, in the case of clustered control planes like ONOS) had not created. These probes mark the location of *network edge links* that demarcatewhere a control plane's influence ends and another's begin. 

A problematic case involves probes from outside devices whose ID(s) are found within the domain (ID aliasing). Other than under special circumstances (e.g. the probe arrives before the domain's own device is discovered, or the recipient of the probe is the one being aliased), ID aliasing is difficult to detect, and leads to wrongly reported links. 

### Probe message fingerprinting

ONOS employs per-logical-control-plane *fingerprints* to identify its own cluster. Since ONOS 1.4, the ability to add fingerprint information to probe messages has been added to the `LLDPLinkProvider`, to aid in the identification of foreign devices and ID aliasing. Specifically, the fingerprint is encoded into the source MAC address of the probe message. The `ProbedLinkProvider` interface allows implementors of providers that probe network links to access a fingerprinted MAC address for use with their probes. The fingerprint is derived from a stable hash of the cluster's name, which is autogenerated at this time. A fixed MAC address (DE:AD:BE:EF:BA:11) is used when the cluster's name cannot be determined (which might be the case if the ClusterMetadata subsystem is unavailable).

In earlier versions of ONOS that implement fingerprinting, a different mechanism, where an extra TLV carrying the fingerprint is added to just the LLDP messages, is used. Although two clusters that use these different mechanisms can control neighboring domains, domain edge detection won't work properly in this case.

## Host Discovery

The Device Subsystem discovers network end-hosts via ARP and DHCP messages detected as PacketIns, and describes their locations in the network in terms of Device-Port pairs referred to as **`ConnectPoints`**. The HostLocationProvider implements this function by implementing a `DeviceListener` in a similar vein as the LLDPLinkProvider.
