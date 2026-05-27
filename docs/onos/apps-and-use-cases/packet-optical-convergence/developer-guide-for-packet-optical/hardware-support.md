# Hardware Support

This page details how to add support for optical hardware and protocols.

# Device Centric

ONOS assumes it has direct control over network devices. 

Here is the current list of device types.

```
public interface Device extends Element {

    /**
     * Coarse classification of the type of the infrastructure device.
     */
    enum Type {
        SWITCH, ROUTER, ROADM, OTN, ROADM_OTN, FIREWALL, BALANCER, IPS, IDS, CONTROLLER,
        VIRTUAL, FIBER_SWITCH, MICROWAVE, OLT, ONU, OTHER
    }
```

# Network Management System (NMS)

Optical networks are most commonly controlled using an NMS. This is a software layer that directly controls all the hardware, and typically exposes some API upwards for service provisioning, topology discovery, etc. ONOS assumes it has direct control over the devices, and thus supporting the NMS-model requires a slightly different approach than before.

You can easily implement own device and link providers for your NMS and protocol

The most straightforward way is writing your own `OpticalPathIntentCompiler`; instead of generating flow rules, you want to generate API commands 

instructions here assume single vendor environment for the optical layer

1. direct control over device -> use flow rules to drive it, implement devicedescriptiondiscovery, flowruleprogrammable,
2. go through NMS: write your own intent compiler -> instead of generating flow rules, you can make calls to your NMS
3. making an application to bundle support for single vendor env: point to app dev guide
4. open flow extensions: standard and vendor extensions

Vendor Applications

# OpenFlow Extensions for Optical Networks

The Optical Transport Working Group in [ONF](http://opennetworking.org/) has been instrumental in adding support for optical devices in OpenFlow. Their work covers both Layer 0 (WDM) and Layer 1 (OTN). Version 1.0 (ONF TS-022) was publicly released on March 15, 2015. We are slowly adding support for this spec through integration and testing with the following devices:

1. [LINC switch](https://github.com/FlowForwarding/LINC-Switch) is an optical ROADM emulator that supports OpenFlow 1.3 with the extensions defined by the ONF. If you are interested in how LINC implements the optical extensions, go [here](https://github.com/FlowForwarding/LINC-Switch/blob/internals-oe-doc/docs/LINC_internals.md#linc-oe-openflow-13-with-oe).
2. [Calient](http://www.calient.net/) offers a fiber switch with an OpenFlow 1.3 interface; it requires custom Circuit Extensions as developed by Calient.
3. [Oplink](http://www.oplink.com/) has a 8D SDN ROADM that uses OpenFlow 1.3 with vendor-specific extensions.

[LoxiGen](https://github.com/floodlight/loxigen) is a tool that generates OpenFlow bindings for a number of programming languages. It offers a production quality implementation of OpenFlow 1.0 and 1.3. The ONOS project relies on it to generate the OpenFlowJ library, which is used extensively by the OpenFlow subsystem.

This is a short guide on how to add OpenFlow extensions in Loxi, and how to use them in ONOS.

### Setup your build environment

The ONOS project has forked LoxiGen (which will eventually be submitted upstream) to implement some of the optical extensions; start by cloning this.

```
$ git clone https://gerrit.onosproject.org/onos-loxi
```

### Add extensions to Loxi

Add/edit the files under `onos-loxi/openflow_input`. There are a few examples you can look at, such as `circuit`, `nicira` and `bsn`.

For instance, the `circuit` file defines an `of_action_circuit`, which will lead to the creation of a circuit() method in the OFActions class. This method takes in an OXM object, which in this particular example will be of type `of_oxm_och_sigid`. This is a struct that has a field of type `of_sig_id_t`.

The mapping between OpenFlow message types and java types is defined in `java_gen/java_type.py`. Here, we see that `sig_id_t` is mapped to the `CircuitSignalID` class in Java. You will find the definition of this class under `java_gen/onos-loxi/pre-written/src/main/java/org/projectfloodlight/openflow/types`, and its declaration as an OpenFlow match under `java_gen/``onos-loxi/pre-written/src/main/java/org/projectfloodlight/openflow/protocol/match`.

### Generate openflowj

The following command will create the actual openflowj library and make it available to other projects. Run this inside the loxi source directory.

```
onos-loxi$ make install-java
```

The new library will be installed into your local repository, typically under `~/.m2`.

### Support extensions in ONOS

You can now refer to the new openflowj library from ONOS. Basically, you want to:

1. define a new `Criterion` type
2. handle the new type in the `Criteria`
3. create a new handler in the `Instructions`
4. map the `Criteria` and `Instructions` to the `DefaultTrafficSelector` and `DefaultTrafficTreatment` respectively

From then on, you can do things like

```
DefaultTrafficSelector.builder().add(Criteria.yourCustomSelector())
DefaultTrafficTreatment.builder().add(Instructions.yourCustomTreatment()) 
```

You will also want to handle the extensions in the `FlowModBuilder` and the `FlowEntryBuilder`. Note that for the former, version-specific implementations are available in, e.g., `FlowModBuilderVer13`. ONOS currently supports OpenFlow 1.0 and 1.3, so you want to handle these cases appropriately.

### Upgrade version

If you are ready with your work, you should upgrade the openflowj version number.

First, open `onos-loxi/java_gen/pre-written/pom.xml` and find the following section. Bump up the version number.

```
<groupId>org.onosproject</groupId>
<artifactId>openflowj</artifactId>
<version>0.4.1.onos-SNAPSHOT</version>
<packaging>jar</packaging>
```

Then, generate and install the new openflowj library using `make install-java`, after which you should upgrade the version ONOS uses. Open `onos/pom.xml` and search for the following line; make sure the version matches the new version you created.

```
<openflowj.version>0.4.1.onos-SNAPSHOT</openflowj.version>
```

Finally, if you want to submit your changes to the `onos-loxi` repo, you'll need to get in touch with the core dev team via the [onos-dev](../../../community-information/mailing-lists.md) mailing list. Again note that, over time, we will be phasing out our forked loxi repo by submitting all changes upstream.
