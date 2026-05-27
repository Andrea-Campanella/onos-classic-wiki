# Network State Construction

## Overview

A key piece of information maintained by a control plane is the network state. The control plane must aggregate this information, and make it available to its applications. Additionally, in order to maintain extensibility and component reuse, applications should be shielded from protocol-specifics, even if network state information is acquired through protocol-specific means.

ONOS's protocol-agnostic topology is built using two complementary mechanisms - network discovery and configuration. The former takes advantage of network protocols that let ONOS identify the locations and/or properties of network elements, and is proactively carried out by the system if enabled. The latter allows applications and operators to configure the expected topology, or to provide 'hints' about network components that cannot be discovered by typical means, should they be in the network.

This section begins by describing how ONOS represents network topology and state. It then discusses the mechanisms used by ONOS to build the topology.

* [Representing Networks](network-state-construction/representing-networks.md)
* [Network Discovery](network-state-construction/network-discovery.md)
* [Network Configuration Subsystem](network-state-construction/network-configuration-subsystem.md)
