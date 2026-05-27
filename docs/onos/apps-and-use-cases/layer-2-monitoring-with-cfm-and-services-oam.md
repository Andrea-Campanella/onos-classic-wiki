# Layer 2 Monitoring with CFM and Services OAM

[Connectivity Fault Management](https://en.wikipedia.org/wiki/IEEE_802.1ag) (CFM) was first introduced in IEEE 802.1ag, which has been superseded by IEEE 802.1Q-2011 and subsequently by [IEEE 802.1Q-2014](https://en.wikipedia.org/wiki/IEEE_802.1Q) - the IEEE Standard for Local and metropolitan area networks - Bridges and Bridged Networks.

It defines protocols and practices for OAM (Operations, Administration, and Maintenance) for paths through 802.1 bridges and local area networks (LANs).

It is an amendment to IEEE 802.1Q-2005 and was approved in 2007.

IEEE 802.1ag is largely identical with [ITU-T Recommendation Y.1731](https://en.wikipedia.org/wiki/ITU-T_Recommendation_Y.1731), which additionally addresses performance monitoring.

In addition the Metro Ethernet Forum ([MEF](https://mef.net/)) has defined SOAM (Service Operations Administration and Management) in [MEF-17](https://mef.net/resources/technical-specifications/download?id=41&fileid=file1) on top of these standards to build a framework for monitoring in conjunction with MEF services. This and other MEF standards are available in their [technical documentation](https://mef.net/resources/technical-specifications) section.

## Modeling

Working these combined standards into a unified model is a complex task an inevitably requires some compromises. For instance while  802.1Q talks about Maintenance Domains and Maintenance Associations the MEF 17 standard uses the name Maintenance Entity (ME) and Maintenance Entity Group (MEG). MEF 38 and 39 defines a model that encompasses all of the concepts as a set of YANG modules, that separate out the Monitoring aspects of MEF 17 from MEF Carrier Ethernet Services. In this way a loose coupling exists between the CFM and MEF Services linked together only through VLAN ids.

MEF 38 defines a root object mef-cfm which represents 802.1Q and Y.1731 CFM entities, which is augmented by mef-soam-fm which adds on additional attributes and operations from SOAM related to fault management.

MEF 39 augments mef-cfm further with the performance management aspects of SOAM as mef-soam-pm including monitoring of delay, jitter and loss measurements.

![](https://docs.google.com/drawings/d/sjFIVOrJf_8ZwFBe8RYAX_Q/image?w=444&h=111&rev=122&ac=1)

These YANG models act as a unified definition of these standards that it makes practical sense to reuse in ONOS.

## Implementation in ONOS

Direct translation of the MEF 38 and MEF 39 YANG models into ONOS does not provide a completely clean way to define the models in ONOS, because of the complication brought by the augments. Instead the models have been defined independently in ONOS as a new structure under reusing common ONOS classes such as DeviceId, PortNumber, NetworkResource, Identifier, MacAddress etc.

* [onos/incubator/src/main/java/org/onosproject/api/net/l2monitoring/cfm](http://api.onosproject.org/1.10.8/org/onosproject/incubator/net/l2monitoring/cfm/package-summary.html)
* [onos/incubator/src/main/java/org/onosproject/api/net/l2monitoring/soam](http://api.onosproject.org/1.10.8/org/onosproject/incubator/net/l2monitoring/soam/package-summary.html)

## Java Model

These immutable objects are defined as Java POJOs with little dependencies on outside elements, and built the familiar builder pattern.

As with 802.1Q the model’s top level starts with the Maintenance Domain - an abstract reference object defining the span of the domain of activity for maintenance in the network. Maintenance Domains are defined at 8 different levels to indicate the scope of their span.

Beneath the Maintenance Domain is the Maintenance Association, another abstract object specific to a VLAN that contains common parameters for a group of MEPs (Maintenance Association Endpoints). It is these MEPs that are created on devices in the network and can be thought of as monitoring points. Devices must support the CfmMepProgrammable behaviour to support the creation of MEPs.

The MEP is the key item then that allows specific actions to be taken on devices such as

* Continuity Check Messaging (CCM)
* Loopback testing
* Linktrace testing

In addition these MEPs allow the creation of

* Delay Measurement entities (which run tests for Delay and Jitter on a continuous basis)
* Loss Measurement entities (which run tests for Loss Measurement on a continuous basis)

The Java Doc for this model is available at <http://api.onosproject.org/1.10.8/org/onosproject/incubator/net/l2monitoring/cfm/MaintenanceDomain.html> and is summarized in the following L2 Monitoring hierarchy:

```
|-Maintenance-Domain*
```

```
|-MdId (MdIdCharStr or MdIdDomainName or MdIdMacUint or MdIdNone)
```

```
|-Maintenance-Association*
```

```
|-MaIdShort (MaIdCharStr or MaIdPrimaryVid or MaId2Octet or MaIdRfc2685VpnId or MaIdIccY1731)
```

```
|-Component*
```

```
|-Mep* (Maintenance-Association-EndPoint) and MepEntry*
```

```
| |-MepId
```

```
| |-MepLbEntry
```

```
| |-MepLtEntry
```

```
| | |-MepLtTransactionEntry*
```

```
| | |-MepLtReply*
```

```
| | |-SenderIdTlv
```

```
| |-DelayMeasurementCreate (SOAM)* and DelayMeasurementEntry
```

```
| | |-DmId
```

```
| | |-DelayMeasurementStatCurrent
```

```
| | |-DelayMeasurementStatHistory*
```

```
| |-LossMeasurementCreate (SOAM)* and LossMeasurementEntry
```

```
| | |-LmId
```

```
| | |-LossMeasurementStatCurrent
```

```
| | |-LossMeasurementStatHistory*
```

```
| |-RemoteMepEntry*
```

```
| | |-RemoteMepId
```

```
|-RemoteMepId*
```

The classes and interfaces can be broken down into 4 main categories:

* Those used as identifiers
* Those for configuring the object
* Those representing both the status attributes of the object and its configuration (usually ending in Entry)
* Those used in commands called on objects - for Loopback, Linktrace, Delay and Loss Measurement these are not configured - they are called as a method with parameters

# OSGi Services

A set of services are defined for managing the object model

* CFM MD Service
* CFM MEP Service
* SOAM Service

## CFM MD Service

This is an [interface](http://api.onosproject.org/1.10.8/org/onosproject/incubator/net/l2monitoring/cfm/service/CfmMdService.html) that manages only the configuration of Maintenance Domain and Maintenance Association. It acts as a standalone service in ONOS that manages only these 2 levels of the model. The Maintenance Domain contains a list of Maintenance Associations does not contain Meps - these are left to the CfmMepService.

These objects are persisted in ONOS in a distributed data store by this service.

There are CLI commands (when **org.onosproject.cfm** app is activated) for creating, deleting and modifying these objects.

* cfm-md-list - Lists a single CFM Maintenance Domain.
* cfm-md-add - Add a CFM Maintenance Domain.
* cfm-md-delete - Delete a CFM Maintenance Domain and its children.
* cfm-ma-add - Add a CFM Maintenance Association to a Maintenance Domain.
* cfm-ma-delete - Delete a CFM Maintenance Association and its children.

They can also be modified through a REST interface at <http://localhost:8181/onos/cfm/md>

## CFM MEP Service

This is an [interface](http://api.onosproject.org/1.10.8/org/onosproject/incubator/net/l2monitoring/cfm/service/CfmMepService.html) that manages the MEP and objects and commands below it. A MEP managed under this service has a reference to the Maintenance Domain and Maintenance Association above it, and hence depends on the CFM MD Service.

MEPs are identified by a combination of MdId, MaID and MepId.

To create a MEP a device ID must be specified. This device's driver must support the **[CFM Programmable](http://api.onosproject.org/1.10.8/org/onosproject/incubator/net/l2monitoring/cfm/service/CfmMepProgrammable.html)** behavior.

The service has the following actions associated with it

* Create MEP
* Delete MEP
* Get all MEPs (for a particular MD and MA)
* Get individual MEP
* Transmit Loopback
* Abort Loopback
* Transmit Linktrace
* Create Test Signal
* Abort Test Signal

These objects can be modified through a REST interface at **http://localhost:8181/onos/cfm/md/<md-id>/ma/<ma-id>/mep**

At the moment the MEP object is only maintained in memory and not persisted in the ONOS data store. The objects Loopback, Linktrace, Test Signal, Loss Measurement and Delay Measurement are not maintained in ONOS at all as they are not really configuration objects. They are called on the fly and are passed down as a collection of method parameters to the device implementing the MEP. This device will operate on them and their results can be obtained by querying the responsible MEP on the device. For instance the results of LinkTrace, Loopback and Test Signal will appear in the MepLbEntry, MepLbEntry and MepTsEntry under the MepEntry when the “Get Individual Mep” method is called.

See in

* apps/cfm/src/test/resources/examples

for some JSON examples that can be used to activate this functionality.

## SOAM Service

This is an [interface](http://api.onosproject.org/1.10.8/org/onosproject/incubator/net/l2monitoring/soam/SoamService.html) that manages the Delay and Loss Measurement functions of a MEP. It depends on the CFM MEP Service being active.

To create a Delay or Loss Measurement test the driver of the device associated with the MEP must support the **[SOAM Programmable](http://api.onosproject.org/1.10.8/org/onosproject/incubator/net/l2monitoring/soam/SoamDmProgrammable.html)** behavior.

The service has the following actions associated with it:

* Create a Delay Measurement (DM) test on a MEP
* Abort the DM test
* Abort all DM tests on a MEP
* Create a Loss Measurement (LM) test on a MEP
* Abort the LM test
* Abort all LM tests on a MEP
* Get all DM's for a MEP
* Get all LM's for a MEP
* Get a DM by MEP and DM id
* Get only the Current Stats part of a DM by MEP and DM id
* Get only the Historic Stats part of a DM by MEP and DM id
* Get a LM by MEP and DM id
* Get only the Current Stats part of a LM by MEP and LM id
* Get only the Historic Stats part of a LM by MEP and LM id
* Clear the DM History stats on all DM's for a MEP
* Clear the DM History stats of a DM for a MEP
* Clear the LM History stats on all LM's for a MEP
* Clear the LM History stats of a LM for a MEP
* Perform a Test Signal test on a MEP
* Abort a Test Signal test on a MEP

These objects can be modified through a REST interface at **http://localhost:8181/onos/cfm/md/<md-id>/ma/<ma-id>/mep/<med-id>/dm** or **http://localhost:8181/onos/cfm/md/<md-id>/ma/<ma-id>/mep/<med-id>/lm**
