# Network Virtualization

[Latest design document](../../../assets/virtualnetworksubsystem.pdf)

# Overview

ONOS allows one to define virtual networks in terms of virtual devices and links. The virtual devices will comprise of virtual ports that map to ports of underlying devices (physical or visual themselves). In this way, the virtual devices become slices & splices of underlying devices. Consequently, virtual links can be defined as pairs of virtual devices ports, where the underlying devices are not necessarily adjoining. Assuring connectivity between the ports of a virtual devices and the connectivity over virtualized links, will be the job of a *VirtualNetworkProvider*, which can chose whatever tunneling mechanism it deems appropriate.

In this way, the ONOS virtual network support will resemble OVX on the northern side in that one can model the virtual network and its mapping to the underlying network arbitrarily. It will be different on the southern side however, as we cannot singly rely on OF 1.0 and partitioning of header space to accomplish this. Instead, we want to allow multiple different ways to accomplish this and we need to do so without relying solely on OF 1.0 support and flat table space.

The virtual networks that one will create in ONOS will be treated using the same abstractions as the underlying networks, albeit using service instances mapped to the context of each virtual network. See *VirtualNetworkService* and *VirtualNetworkAdminService* interfaces in ONOS code-base for the initial sketches of this mechanism.

The lowest form of programming virtual network will be the *FlowObjective*/*FlowRule* and *Intent* abstractions.
