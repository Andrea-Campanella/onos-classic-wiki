# Device Driver Subsystem

## Overview

The primary purpose of this subsystem is to isolate device-specific code so it does not spread-out throughout the rest of the system. Since such code will be necessary for any foreseeable future, this subsystem provides means to contain it and allow applications to interact with it through well-defined device and protocol independent abstractions. Furthermore, since devices are released and upgraded on different cycles than the rest of the network control/management platforms, the mechanism allows for asynchronous delivery and dynamic loading of the device-specific code. The code can be delivered not only by ON.Lab and its partners, but also by other vendors as necessary.

Recognizing that different families of devices may share features, but also support unique ones, the ONOS driver mechanism avoids monolithic driver approach. Instead, it promotes segmenting different facets of behaviour so that support for features can be selective, can potentially come from different sources and can be shared via inheritance within a product family, whose devices may share similar characteristics.

## Definitions

In ONOS, a `Driver` is a representation of a specific family of devices or a specific device. As such, it:

* has a unique name, e.g. `com.ciena.foo`
* supports set of `Behaviour` classes
* may “inherit” behaviours from another `Driver`
* may be “abstract” (?)

`DefaultDriver` is a class provided by ONOS and it implements the `Driver` interface.

## `Delivery Mechanism`

## `DriverProvider` is an entity capable of providing device drivers and their behaviours:

* Set<Driver> getDrivers()

`DriverAdminService` is an ONOS service for tracking and managing device drivers indirectly by managing driver providers as follows:

* Set<DriverProvider> getProviders()
* registerProvider(DriverProvider)
* unregisterProvider(DriverProvider)

Note that different driver providers can contribute behaviours to the same driver. This way, drivers for support of OpenFlow table pipelines can come from one source, while support for the PoE configuration of the device can come from another.

## Lookup Mechanism

`DriverService` is the principal service that apps and other ONOS subsystems can use to locate appropriate drivers for the device via the following:

* by driver name
* by device manufacturer, H/W version & S/W version
* by supported Behaviour
* by device ID

## Modeling

Different facets of behaviour for either talking about a device or for interacting with a device are modeled as derivatives of `Behaviour` and `HandlerBehaviour` interfaces, respectively. The reason for differentiating between the two lies in the slightly different context required. Base implementations of these abstractions are provided as `AbstractBehaviour` and `AbstractHandlerBehaviour` by the driver subsystem. It is the implementation of these abstractions where the device and protocol-specific code resides. 

Definition of a `Behaviour` should be focused on characterization of a specific facet of overall device capabilities, e.g. *VlanConfiguration*, *PoEConfiguration*. The rough guidelines for modeling use a Goldilocks principle. The behaviours should be defined as not to be to broad in that they should not span multiple topics, nor should they be too narrow where they implement a specific bit of a topic. The driver service provides means for apps to see if a device supports a particular behaviour and the agreement is such that the device either supports the entire behaviour or it does not support it. This is to limit the complexity of apps and to make the programming model easier. Properly scoped behaviour abstractions work towards that end.

Please observe that this effectively means that in ONOS, the principal modeling language is Java. This certainly does not preclude from using other modeling languages, e.g. YAML, YANG, SNMP-MIB schema, Loxi Lua to define semantics and syntax for interacting with devices, but such models are to be employed solely by the implementations of the drivers (or of ONOS providers) to guide/implement the interactions with the device. Apps and other ONOS subsystems should be completely independent of such modeling languages and should instead drive their interactions through the prescribed `Behaviour` abstractions.

## Contexts

`DriverData` is a container for data learned about a device in prior interactions. It

* provides `Behaviours` for talking about a device
* has parent `Driver`

In this way, even interrogations about different aspects of a device are channeled through abstractions.

Similarly, `DriverHandler` is a context for interacting with a device.

* provides `Behaviours` for interacting with a device
* has `DriverData`
* has parent `Driver`

So as you can see, in order to talk about a specific aspect of information learned about a device, but in the absence of a connection to the device, one requires access to at least `DriverData`, which represents the data learned in prior interactions with a device, whereas direct interactions with a device require a slightly more comprehensive `DriverHandler` context, which include DriverData for recording learned information, but also additional information required for connecting to the device and/or interacting with other ONOS services on behalf of the device.
