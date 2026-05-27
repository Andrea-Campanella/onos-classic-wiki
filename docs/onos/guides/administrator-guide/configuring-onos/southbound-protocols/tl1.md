# TL1

[Transaction Language 1](https://en.wikipedia.org/wiki/Transaction_Language_1) (TL1) is a management protocol that is widely used in the optical networking space. ONOS comes with the needed building blocks to connect and interact with TL1 devices.

# Interfaces

`Tl1Device` is a container that holds the Netty channel and some device attributes such as login and password.

`Tl1Command` represents a command that is sent from the controller to a network element. Its typical structure is as below, and the interface defines various accessor methods as well as a builder.

```
VERB-MODIFIER:<tid>:<aid>:<ctag>::parameter-list;
```

`Tl1Controller` maintains a list of TL1 devices, allows you to connect to them, send and receive messages, and register listeners.

`Tl1Listener` defines the interface for notification of device connect/disconnect events.

Implementations of all these interfaces are prefixed with `Default`, for instance `DefaultTl1Controller` holds the implementation of the `Tl1Controller` interface.

# Tl1Controller

Devices are added to the controller, and then need to be explicitly connected (which leads to a Netty channel being initialized). The controller stores devices using a `ConcurrentMap<DeviceId, Tl1Device>`. For every device, but this time identified by the device's Netty channel, it will also store a `ConcurrentMap<Integer, CompletableFuture<String>>`. This map is keyed on the message ctag (type `Integer`), and stores the future response (type `String`) of the device. An important consequence is that ctag's are assumed to be unique per device, and it is the responsibility of the `sendMsg()` caller to ensure this uniqueness.

# Device Provider

The ONOS TL1 southbound is implemented in the `Tl1DeviceProvider`. This class implements the ONOS SB interface, and most importantly, will connect to the device when it is assigned the master role (in all other cases the instance will disconnect from the device). When a device is connected, the device provider will use the `DeviceDescriptionDiscovery` to fetch and update the device/port description.

Adding devices to ONOS is done by injecting them into the device provider, more specifically Here is an example JSON, that you will inject into ONOS using `onos-netcfg $OC1 tl1.json`.

```
{
  "devices": {
    "tl1:<ip>:<port>": {
      "tl1": {
        "ip": <ip>,
        "port": <port>,
        "username": <username>,
        "password": <password>
      },
      "basic": {
        "driver": <driver-name>
      }
    }
  }
}
```

# Drivers

Adding a new device to ONOS requires implementing a set of behaviors. For instance, to discover devices and their ports, implement the `DeviceDescriptionDiscovery`. If your device supports flow rules, implement the `FlowRuleProgrammable`. And so on. Go here for more information: [Device Driver Subsystem](#).

In the following, let's take `LumentumWaveReadyDiscovery` as an example. Here you can see how the behavior interacts with the TL1 controller. For example, this is how we fetch the device description.

```
// Fetch device description
Tl1Command ddCmd = DefaultTl1Command.builder()
        .withVerb(RTRV)
        .withModifier(NETYPE)
        .withCtag(101)
        .build();
Future<String> dd = ctrl.sendMsg(deviceId, ddCmd);

try {
    String ddResponse = dd.get(TIMEOUT, TimeUnit.MILLISECONDS);

    return new DefaultDeviceDescription(defaultDescription, true, extractAnnotations(ddResponse));
} catch (InterruptedException | ExecutionException | TimeoutException e) {
    log.error("Device description not found", e);
    return defaultDescription;
}
```

We do three things: (1) build a `TL1Command` using a builder pattern, (2) send the message using the controller, and (3) wait for a response to arrive.

After implementing your behaviors, ensure that ONOS knows about them. Here is an example of the `lumentum-drivers.xml`.

```
<driver name="lumentum-waveready" manufacturer="Lumentum" hwVersion="WR*">
    <behaviour api="org.onosproject.net.device.DeviceDescriptionDiscovery"
               impl="org.onosproject.drivers.lumentum.LumentumWaveReadyDiscovery"/>
    <behaviour api="org.onosproject.net.optical.OpticalDevice"
               impl="org.onosproject.net.optical.DefaultOpticalDevice"/>
</driver>
```

To ensure the TL1 provider and protocol are loaded on activation of your driver, you will need to specify this in your driver `BUCK/pom.xml` file as follows (note the `required_apps/onos.app.requires` section):

**BUCK file**

```
onos_app (
    app_name = 'org.onosproject.drivers.lumentum',
    title = 'Lumentum Device Drivers',
    category = 'Drivers',
    url = 'http://onosproject.org',
    description = 'ONOS Lumentum Device Drivers application.',
    required_apps = [ 'org.onosproject.snmp', 'org.onosproject.faultmanagement', 'org.onosproject.optical-model',
     'org.onosproject.tl1'],
)
```

**Maven pom.xml**

```
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
...
    <properties>
        <onos.app.name>org.onosproject.drivers.lumentum</onos.app.name>
        <onos.app.category>Drivers</onos.app.category>
        <onos.app.title>Lumentum Device Drivers</onos.app.title>
        <onos.app.requires>
            org.onosproject.snmp,
            org.onosproject.faultmanagement,
            org.onosproject.optical-model,
            org.onosproject.tl1
        </onos.app.requires>
    </properties>
...
 
```

# Missing features / Help wanted

Here is a list of desirable features that unfortunately are not available in the current code base. Patches and bug reports are very welcome!

* Sending messages using the Tl1Controller uses the following signature. Ideally, we don't want to return a `String` but a `Tl1Message` that can easily be parsed.

  ```
  CompletableFuture<String> sendMsg(DeviceId deviceId, Tl1Command msg);
  ```
* We do not support autonomous messages (alarms, notifications) from the device to the controller. Only request/reply pattern is currently implemented.
* There are no unit tests implemented as of yet.
* The Tl1Listener only has methods to signal device events (device connected and disconnected). Ideally we want to extend this to also cover other events, such as message and alarm notifications.
* We need extensive testing to verify correct behavior in multi-instance ONOS deployments.
* Instead of storing login/password in the `Tl1Device`, use ONOS' `DeviceKeyService` sub-system dedicated to this job.
* Currently, the `Tl1DeviceProvider` will only login to the device when that instance becomes the master. In a multi-instance deployment, it's probably a good idea to have (some of) the standby instances logged in, ready to take over when they becomes master. This requires reworking the `Tl1DeviceProvider`, as well as a way to store multiple accounts per device.
