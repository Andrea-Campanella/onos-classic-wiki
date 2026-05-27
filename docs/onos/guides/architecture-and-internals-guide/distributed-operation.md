# Distributed Operation

This section discusses the design and implementation of the distributed aspects of ONOS.

## Overview

ONOS is built from the ground-up as a distributed SDN operating system. Consequently, ONOS may be deployed as a collection of servers that coordinate with each other to provide capabilities that is greater than the sum of its parts. For example, distribution provides fault-tolerance and resilience even when individual controller instances fail. Additionally, the system as whole can take on workloads that are far greater than what a single instance might be able to handle (scalability).

While distribution has its benefits, it also presents some interesting engineering problems. The following subsections delve into how ONOS identifies, and approaches, a select set of these aspects.

## Remaining Sections

The next section presents an overview of cluster management, and how ONOS instances elect designated *masters* for each device a cluster discovers. The following section describes how network state is distributed across instances.

* [Cluster Coordination](distributed-operation/cluster-coordination.md)
* [Network Topology State](distributed-operation/network-topology-state.md)

 

---

[Previous : The Device Subsystem](https://wiki.onosproject.org/display/ONOS/The+Device+Subsystem)  
 [Next: Cluster Coordination](distributed-operation/cluster-coordination.md)

---
