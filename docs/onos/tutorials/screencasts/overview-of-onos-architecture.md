# Overview of ONOS architecture

## [YouTube Video](https://www.youtube.com/watch?v=60wl-05l7kk)

## Architectural Tenets

ONOS aims to become the SDN system platform for controlling service provider networks. This does not mean that ONOS cannot be used for data center or campus networks. What it does mean, however, is that ONOS had to be built to meet a certain set of stringent requirements.

### High-Availability, Scalability and Performance

First of all, the critical nature and scale of the service provider networks demand that their control platform be built with high-availability, scalability and performance in mind.

### Strong Abstractions

Secondly, to facilitate easy deployment of solutions and applications, the platform must provide a set of robust and simple north-facing abstractions. Similarly, a set of robust south-facing abstractions must be made available to allow control and management of devices using any number of protocols, while at the same time achieving protocol and device behaviour independence.

### Separation of Concerns and Modularity

Furthermore, in order to curb complexity of the platform and to enable stable path for its evolution, ONOS had to be designed with strict adherence for the principle of separation of concerns. For example, care has been taken not to intermingle the north-south workflows with the east-west workflows. This resulted in ONOS being a highly modular platform with crisply defined boundaries between its various subsystems.

## Symmetric Distributed Architecture

In order to be a scalable system and one which is resilient to different types of failures, ONOS is built as a physically distributed system. However, to preserve the simplicity of a centralized control plane, ONOS remains logically centralized. Therefore, ONOS is built as a tightly-coupled, symmetric cluster of individual instances. These instances are software-wise identical to each other, and each is capable to take on work-load of any other instance in case of failure or when balancing work-loads.

### System Tiers

The ONOS system is comprised of several layers which progressively abstract away device and protocol specific aberrations in order to present the applications with a unified and uniform set of abstractions that are free of irrelevant nuances.

### Distributed Core

The pivotal layer is the ONOS core, which while allowing for physical separation of data and control functions, is responsible for presenting a logically centralized view of network state and logically centralized access to network control functions.

### Southbound API & Providers

The core is separated from the other tiers via two logically distinct interface boundaries. The south-facing interface, is a high-level API through which the core interacts with the network environment. Except, rather than interacting with the environment directly, ONOS core relies on protocol-specific adapters to conduct these interactions using the protocol of their choice, whether it is OpenFlow, Netconf, OVSDB, TL1 or even other available means, such as CLIs.

The southbound API then acts as a bridge for core to send edicts to and receive sensory data from the various protocol providers. The protocol-independent nature of this API guarantees that no protocol-specifics leak into the ONOS core and to the applications. Furthermore, its high-level nature avoids merely shrink-wrapping a specific protocol library and at the same time, it allows ample maneuvering room for the protocol providers to translate protocol-specific behaviours into protocol-agnostic ones.

### Northbound API

On the north-facing side, ONOS core exposes a set of abstractions to applications and additional network services via its northbound API. These abstractions provide a range of access to network information starting from the usual low-level topology abstractions, such as devices, links and hosts, to higher-level abstractions, such as the network topology graph. Similarly, they provide a range of abstractions for affecting the network state via flow objective programming and intent-based programming.

## Core Platform Subsystems

Even though the ONOS core is often depicted as a monolithic block, it is in reality an assembly of individual subsystems, each responsible for tracking their own class of network state. This diagram offers a high-level inventory of such subsystems. Most of these provide services which can be utilized by other subsystems and which collectively form the ONOS core northbound API.

Some services are entirely domain agnostic, meaning they have nothing to do with network control, but instead only serve as the distributed infrastructure facilities. These platform subsystems are depicted on the left and in gray, while the rest, which are specific to the domain of network control are depicted on the right and in red.

The intent here is not to dwell on each individual subsystem, but rather to make the point that the ONOS core is not a monolithic entity, but a modular one, designed to be extended and tailored, if required.

## Core Subsystem Structure

To provide a simple and familiar programming model, each core subsystem follows the same high-level pattern of construction and also the same design model for both its northbound, and if applicable, southbound API.

The design revolves around two cooperating components. One is the *Manager* component, which provides the public services, both at the northern and southern sides and is primarily concerned with the north/south workflows. The other is the *Store* component, to which the *Manager* delegates the responsibility to store and distribute state and which hence handles the east/west flows, including all cluster communications. Events that occur elsewhere in the cluster are conveyed by the *Store* to the local *Manager*, which then dispatches them either to its local listeners or takes action on the environment, depending on the nature of the event.

Functionality that is deemed to be reserved for privileged principals, is usually offered through an administrative service, which separate from a service available to all other applications. For example *DeviceAdminService* allows deletion of a device from inventory, whereas *DeviceService* allows all other, generally read-only, interactions with the inventory of network infrastructure devices.

Components which interface with protocol providers structure the south-facing API using a notion of a registry, which acts as a brokerage with which providers can register so that the core can interact with them and in return are issued a provider service through which they can interact with the core.

## Conclusion

I hope you have found this high-level overview of ONOS architecture and its design philosophy helpful. Have a great day… and happy coding.
