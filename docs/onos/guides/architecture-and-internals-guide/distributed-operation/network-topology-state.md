# Network Topology State

This section discusses the distributed aspects of ONOS's network topology representation.

## Overview

As part of its northbound API, ONOS provides applications with access to a global network topology view. Applications operate on this view to perform various network functions such as path computation and flow provisioning, among others. 

A primary concern in global network topology state management is the maintaining of the consistency of state deployed across various ONOS instances. Each controller must expose a view of the entire network even though at any given point in time it only has direct visibility over a subset of the network.   
  

## Global Network Topology View

There are some properties that a good network topology state management solution should have in a distributed setting:  
  

1. **Completeness**: Even though each controller only has direct visibility and influence over a subset of the network, they should all work together to ensure each controller’s network topology view reflects the state of the entire network.
2. **Accuracy**: Switches, ports and links go up and down. Each controller’s network view should always expose the correct state for various network elements. This also means that each controller’s network view should quickly change to reflect any changes in the underlying network.
3. **Low latency access:** Network topology view is a heavily consumed piece of state and therefore it is very important that the chosen mechanism provide low latency access to the network view.

## Approach

In ONOS, the entire global network topology state is cached in memory on each instance. This provides applications with low-latency access to topology state. Before we go into the details of how the topology state is kept in sync across instances and with the state of the physical network, it is useful to define a few concepts:  

### Masters and Terms

As discussed in [Device Subsystem](../device-subsystem.md), each network device may have direct TCP connections to one or more ONOS instances, and as described in the [previous section](cluster-coordination.md), ONOS elects one of those controllers to serve as the master for the device. The system invariant is that at any given point in time a device can have one and only one master. If the current master dies, ONOS elects a new master from amongst the controllers that the device can talk to. A ***mastership term*** is a per-device monotonically increasing counter (starting at 0) that is bumped each time a new master is elected. The very first time a switch comes online and a new master is elected, the mastership term value is 1. If that master dies and a new master is elected the term is bumped to 2 and so on. 

The information regarding which controller is the current master for a device and the associated term number is tracked in a strongly consistent data store. 

### Topology Events and Sequence numbers

In a given mastership term, the elected master receives various topology events from the device. These could be events such as *switch connected*, *port online, port offline, link down,* etc. The current master maintains a per-switch counter to tag the various topology events it has received from the device during its term. So the **sequence number** is a monotonically increasing counter that is initialized to 0 at the start of the term and is incremented when a new topology event is detected by the master.

### Logical Timestamps

Now to the important part, given the mastership term and sequence number concepts, it is possible for us to assign a logical timestamp to each topology event emanating from the network that will lets us completely order the topology events originating from a that device. That timestamp is the tuple **(mastership\_term, sequence\_number)**

Take any two events for a device, those events can be ordered by first ordering based on the mastership term and if they both have the same term, by comparing their sequence numbers. It is very important to note that the logical timestamps will only let you order events emanating from one device. Two events emanating from different devices are considered independent of each other. 

### Network Topology State Machine

Each ONOS instance maintains a in-memory representation of the global network view that is updated as follows:

1. The instance receives a topology event from a device that it is managing. The instance first assigns a new logical time stamp for this event. It then applies that event to its local topology state machine, and in parallel, broadcasts the event along with the time stamp to every other controller instance in the cluster.
2. The instance receives a topology event (and time stamp) broadcasted by a peer. The instance first checks to see if it already knows of a more recent update for this device. It does so by comparing the time stamp of the most recent event it knows about for this device with the one it just received. If the just received time stamp is older, it simply discards the event. Otherwise, it updates it local topology state machine by applying the received event.

As should be evident by now, the role played by the event logical timestamps is to ensure the topology state machine evolves in the right direction over time by incorporating newer information. This remains true even when messages get lost, delayed or reordered.

### Failure Handling and Anti-Entropy

In the setup described above, it is possible that a controller that is temporarily partitioned away will stop receiving updates from peers. Even under normal operation, there is no guarantee that each and every message that is broadcasted will be received by all members of the cluster. If left to its own devices :) , a system purely based on an optimistic replication technique like the one described above will get progressively out of sync and that is no good.

Another class of failures pertains to controller crashes that effectively results in a loss of topology updates. Consider a controller that, on receiving a topology event, promptly crashes before it could replicate that event to other controllers in the cluster. While ONOS automatically elects another controller as the new master for the device, the original topology event is still effectively lost. If that event was for a port going offline, the network view in each controller will continue to show the port as up if nothing else happens in the system. This is bad as well.

To detect and fix issues such as a the ones described above, ONOS employs a couple of techniques:

* An anti-entropy mechanism based on Gossip protocol, which works as follows: at fixed intervals (usually 3-5 seconds), a controller randomly picks another controller and they both synchronize their respective topology views. If one controller is aware of more recent information that the other controller does not have, they exchange that information and at the end of that interaction, their respective topology views are mutually consistent. Most of the time the anti-entropy interaction will be uneventful, as each controller already knows about every event that happened in the network. But when a controller state drifts slightly, this mechanism quickly detects that and brings the controllers back in sync. This approach has the added benefit of quickly synchronizing a newly-joining controller with the rest. The first anti-entropy interaction that a newly joining controller has with an existing controller will bring it up to speed, without the need for a separate backup/discovery mechanism.
* For detecting and recovering from complete loss of topology updates, each controller periodically probes the devices for which it is the master. If it detects that the device state is different from the information it has, it promptly updates its local topology state and replicates that update to all other controllers in the cluster.

 

---

[Previous : Cluster Coordination](cluster-coordination.md)  
 [Next : Intent Framework](../intent-framework.md) 

---
