# Resource Service

WIP

# Overview

Resource Service subsystem provides APIs to manage resource present in the network. It enables us to register/unregister resources and to allocate/release resources. You can find interfaces for this as ResourceService.java and ResourceAdminService.java in org.onosproject.net.resource package. ResourceService interface provides APIs to register/unregister resources and make queries about resources. ResourceAdminService interface provides APIs to register/unregister resource to Resource Service subsystem. It is mainly intended to be used by ONOS core components, not by applications. ResourceService is designed to be used mainly by Intent Framework, but application developers can still use the interface for specific resource handling.

Resource Service subsystem can handle any kinds of resources in a unified way. The types of resources may include, but not limited to devices, ports, VLAN IDs, MPLS labels, wavelengths, and bandwidth. These resources are categorized into two types, which are called discrete type and continuous type. Resource Service subsystem supports resource hierarchy. For example, VLAN IDs are resources of a particular port and the port is a resource of a device. The object representing a resource has this resource hierarchy information.

## Resource types

* Discrete Resource  
  A resource which can be regarded as a discrete unit is categorized as a discrete resource. VLAN ID, MPLS label, and wavelength are examples of this resource type. For example, one VLAN ID is a the smallest unit in its addressing space and it's a discrete instance. A class representing discrete resource is defined in DiscreteResource.java.
* Continuous Resource  
  A resource which contains a continuous value information is categorized as a continuous resource. A typical example of this type is bandwidth. Bandwidth is represented as a continuous value like 1.25Gbps, then bandwidth is categorized as a continuous resource. A class representing continuous resource is defined in ContinuousResource.java. Continuous resource holds a double value to indicate the amount of the resource, but doesn't have knowledge about the unit for the amount. Developers have to keep the consistent meaning of the double value for each continuous type resource.

## Lifecycle

Resource Service subsystem assumes the following phases. A resource has to be registered before being allocated and a resource has to be released before being unregistered.

1. Registration phase  
   A new resource is detected by ONOS, the resource needs to be registered to Resource Service subsystem so that the subsystem can track the resource utilization. This phase is nomally handled by ONOS framework side (ResourceRegistrar), not by application developer, but you can register resources for your specific purpose.
2. Allocation phase  
   Resource Service subsystem can allocate a registered resource to a resource consumer. The allocation method supports multiple resource allocations at a time as a single transaction.
3. Release phase  
   When we don't need to use a resource anymore, we can release the resource allocation. Similar to the allocation method, the release method also supports transaction.
4. Unregistration phase  
   When ONOS detects a registered resource being gone, ResourceRegistrar takes care of the resource unregistration.

# Code examples

```
ResourceService resourceService = ...;

ResourceConsumer consumer = IntentId.valueOf(1);
DeviceId device = DeviceId.deviceId("foo");
PortNumber port = PortNumber.portNumber(1);
VlanId vlan = VlanId.vlanId((short) 100);

// create a VLAN ID resource on port 1 on device "foo"
DiscreteResource vlanRes = Resources.discrete(device, port, vlan).resource();

// create a bandwidth resource representing 1000bps on port 1 on device "foo"
ContinuousResource bandwidthRes = Resources.continuous(device, port, Bandwidth.class).resource(1000);

// allocate the VLAN ID resource, then release it
resourceService.allocate(consumer, vlanRes).ifPresent(alloc -> resourceService.release(alloc));

// allocate the bandwidth resource, then release it
resourceService.allocate(consumer, bandwidthRes).ifPresent(alloc -> resourceService.release(alloc));

// create a discrete resource ID
Resources.discrete(device, port).id();

// create a continuous resource ID
Resources.continuous(device, port, Bandwidth.class).id();
```
