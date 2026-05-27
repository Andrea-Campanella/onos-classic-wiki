# Provider Tutorial

This tutorial is outdated and should either be updated or the removed.

The [Application tutorial](#) covers more basic aspects of ONOS modules so it's helpful to complete those first. Taking a look at [System Components](../guides/architecture-and-internals-guide/system-components.md) may also help make sense of the terminology here.

## Overview

ONOS interacts with the underlying network with the help of its [Providers](../guides/architecture-and-internals-guide/system-components.md). Since the southbound is modular, new Providers may be loaded to enhance ONOS's ability to interact with networks. This tutorial illustrates how to create a new Provider, using the null link test Provider (`NullLinkProvider`) as an example. This provider generates *LinkDescription*s to stress-test the ONOS core. The `OpenFlowDeviceProvider` is also referenced to supplement this tutorial with key Provider features not implemented by NullLinkProvider.

Providers should be delivered as ONOS applications. In this way, they can be easily deployed across the entire ONOS cluster.

By completing this tutorial, you will understand:

* The organization and structure of a Provider
* How to load a Provider

## Project skeleton setup

Provider implementations are placed under *${ONOS\_ROOT}/providers/*. The layout of the Provider is summarized below:

```
${ONOS_ROOT}/providers/pom.xml (provider parent POM file)
                      |  
                      /null/pom.xml (null providers POM)
                           |
                           /link/pom.xml (provider-specific POM)
                                |
                                /src/main/java/org/onosproject/provider/nil/link/impl/NullLinkProvider.java (the provider)
                                    |                                                |
                                    |                                                /package-info.java (optional package-wide documentation/annotations)
                                    |
                                    /test/java/org/onosproject/providers/null/link/impl/ (Unit tests should go here)
```

If you have completed the [Application tutorial](#), you will notice that the following steps are very similar.

### Set up a directory layout

We first build a directory tree following Maven conventions.

```
$ cd ${ONOS_ROOT}/providers/
$ mkdir -p null/link/src/main/java/org/onosproject/provider/nil/link/impl/
$ mkdir -p null/link/src/test/java/org/onosproject/provider/nil/link/impl/
```

### Add and edit POM files

There are three key POM files to keep in mind for Providers:

* *Provider-specific* : the Provider you are writing
* *Providers* : the set of Providers associated with a mechanism for interacting with the network, e.g. a certain protocol
* *Provider root* : all Providers

We take a look at each below.

#### Provider-specific POM

A Provider tends to have a relatively simple provider-specific POM file. For the NullLinkProvider:

**Provider-specific pom.xml** Expand source

```
<?xml version="1.0" encoding="UTF-8"?>
<!--
  ~ Copyright 2014 Open Networking Laboratory
  ~
  ~ Licensed under the Apache License, Version 2.0 (the "License");
  ~ you may not use this file except in compliance with the License.
  ~ You may obtain a copy of the License at
  ~
  ~     http://www.apache.org/licenses/LICENSE-2.0
  ~
  ~ Unless required by applicable law or agreed to in writing, software
  ~ distributed under the License is distributed on an "AS IS" BASIS,
  ~ WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  ~ See the License for the specific language governing permissions and
  ~ limitations under the License.
  -->
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.onosproject</groupId>
        <artifactId>onos-null-providers</artifactId>
        <version>1.1.0-SNAPSHOT</version>
        <relativePath>../pom.xml</relativePath>
    </parent>

    <artifactId>onos-null-provider-link</artifactId>
    <packaging>bundle</packaging>

    <description>ONOS Null link provider</description>
</project>
```

#### Providers POM

Conventionally, a single Provider is associated with one subsystem, such as Device, Packet, or Link. A protocol supported by the southbound will have a Provider for each subsystem it interacts with. The Providers-level POM describes the group of Providers required to support a protocol. This POM is the parent POM to the Provider-specific file, and is in *${ONOS\_ROOT}/providers/null/* .

**Providers pom.xml** Expand source

```
<?xml version="1.0" encoding="UTF-8"?>
<!--
  ~ Copyright 2014 Open Networking Laboratory
  ~
  ~ Licensed under the Apache License, Version 2.0 (the "License");
  ~ you may not use this file except in compliance with the License.
  ~ You may obtain a copy of the License at
  ~
  ~     http://www.apache.org/licenses/LICENSE-2.0
  ~
  ~ Unless required by applicable law or agreed to in writing, software
  ~ distributed under the License is distributed on an "AS IS" BASIS,
  ~ WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  ~ See the License for the specific language governing permissions and
  ~ limitations under the License.
  -->
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.onosproject</groupId>
        <artifactId>onos-providers</artifactId>
        <version>1.1.0-SNAPSHOT</version>
        <relativePath>../pom.xml</relativePath>
    </parent>

    <artifactId>onos-null-providers</artifactId>
    <packaging>pom</packaging>

    <description>ONOS null protocol adapters</description>

    <modules>
        <module>device</module>
        <module>link</module>       <-----here
        <module>host</module>
        <module>packet</module>
        <module>flow</module>
        <module>app</module>
    </modules>

    <dependencies>

        <dependency>
            <groupId>org.onosproject</groupId>
            <artifactId>onos-api</artifactId>
            <classifier>tests</classifier>
            <scope>test</scope>
        </dependency>
    </dependencies>

</project>
```

As seen in the *modules* section of the above *pom.xml*, the `NullLinkProvider` is part of a set of five Providers associated with different aspects of the Null southbound.

#### Provider root POM

This POM file is used to build all available Providers in *${ONOS\_ROOT}/providers*. Therefore, it must include all Provider sets in its *modules* section, including our set of null Providers:

**Provider root pom.xml**

```
    <description>ONOS information providers &amp; control/management protocol adapter</description>

    <modules>
        <module>openflow</module>
        <module>lldp</module>
        <module>host</module>
        <module>null</module>       <-----here
    </modules>
```

## Creating the Provider

### Create a minimal skeleton.

A Provider is a derived class of `AbstractProvider` that implements some Provider API, and an OSGi bundle. The class `NullLinkProvider` deals with Links, so will implement the `LinkProvider` interface. We begin with the following skeleton.

**NullLinkProvider.java** Expand source

```
/*
 * Copyright 2015 Open Networking Laboratory
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.onosproject.provider.nil.link.impl;

import static org.slf4j.LoggerFactory.getLogger;

import org.apache.felix.scr.annotations.Activate;
import org.apache.felix.scr.annotations.Component;
import org.apache.felix.scr.annotations.Deactivate;
import org.apache.felix.scr.annotations.Reference;
import org.apache.felix.scr.annotations.ReferenceCardinality;
import org.onosproject.net.link.LinkProvider;
import org.onosproject.net.link.LinkProviderRegistry;
import org.onosproject.net.link.LinkProviderService;
import org.onosproject.net.provider.AbstractProvider;
import org.onosproject.net.provider.ProviderId;
import org.slf4j.Logger;

/**
 * Provider which advertises fake/nonexistent links to the core. To be used for
 * benchmarking only.
 */
@Component(immediate = true)
public class NullLinkProvider extends AbstractProvider implements LinkProvider {

    private final Logger log = getLogger(getClass());   

    // The Manager serving as communication point between the ONOS core and this Provider
    @Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
    protected LinkProviderRegistry providerRegistry;

    // The interface that defines how this Provider can interact with the core
    private LinkProviderService providerService;

    public NullLinkProvider() {
        // ProviderId is used by the core to identify this Provider
        // The schema "null" and FQDN of the Null southbound comprise this ID
        super(new ProviderId("null", "org.onosproject.provider.nil"));
    }

    @Activate
    public void activate() {
        // Request interface from Manager
        providerService = providerRegistry.register(this); 
        log.info("started");
    }

    @Deactivate
    public void deactivate() {
        providerRegistry.unregister(this);
        log.info("stopped");
    }
	
 }
```

### Register with Services.

Our Provider is part of the Link subsystem, but needs two pieces of information from other subsystems: available devices and mastership (write permissions) for each device. We register as a listener to the *DeviceService*, and make the *MastershipService* a dependency.

**NullLinkProvider.java** Expand source

```
// new imports - service dependencies
import org.onosproject.mastership.MastershipService;
import org.onosproject.net.device.DeviceService;
import org.onosproject.net.device.DeviceListener;
import org.onosproject.net.device.DeviceEvent;

// ...<snip>...

public class NullLinkProvider extends AbstractProvider implements LinkProvider {

    private final Logger log = getLogger(getClass());   

    // For subscribing to device-related events
    @Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
    protected DeviceService deviceService;

    // For checking write permissions for devices
    @Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
    protected MastershipService roleService;

    // For handling DeviceEvents that we've subscribed to
    private final InternalLinkProvider linkProvider = new InternalLinkProvider();

    // ...<snip>...

    @Activate
    public void activate() {
        providerService = providerRegistry.register(this); 
        deviceService.addListener(linkProvider);
        log.info("started");
    }

    @Deactivate
    public void deactivate() {
        deviceService.removeListener(linkProvider);
        providerRegistry.unregister(this);
        log.info("stopped");
    }

    /**
     * Listener as an inner class 
     * Listens for devices being added/removed, and generates LinkDescriptions.
     */
    private class InternalLinkProvider implements DeviceListener {
        @Override
        public void event(DeviceEvent event) {
        }
    }
 }
```

### Notify Core about links.

We now have a *providerService* for notifying the Core about links and their states, and a *linkProvider* for learning about available devices that can be interconnected by links. The method `event()` in the latter intercepts `DeviceEvent`s from the *DeviceService*. We can implement how this Provider "creates" links between devices that it finds in this method. To keep things organized, we break up event detection and link creation/destruction into multiple methods within the `InternalLinkProvider`:

**NullLinkProvider.java - class InternalLinkProvider** Expand source

```
// more new imports
import java.util.List;
import java.util.concurrent.ConcurrentMap;
import com.google.common.collect.Lists;
import com.google.common.collect.Maps;

import org.onosproject.net.ConnectPoint;
import org.onosproject.net.Device;
import org.onosproject.net.DeviceId;
import org.onosproject.net.Link;
import org.onosproject.net.PortNumber;
import org.onosproject.net.link.DefaultLinkDescription;
import org.onosproject.net.link.LinkDescription;

import static org.onosproject.net.MastershipRole.MASTER;

// ...<snip>...

public class NullLinkProvider extends AbstractProvider implements LinkProvider {

    // ...<snip>...

    private final InternalLinkProvider linkProvider = new InternalLinkProvider();

    // LinkDescriptions for Links that this Provider generates
    private final ConcurrentMap<ConnectPoint, LinkDescription> descriptions = Maps
            .newConcurrentMap();

    // Device IDs that have been seen so far
    private final List<DeviceId> devices = Lists.newArrayList();

    // Switch port values used as Link endpoints
    private static final PortNumber SRCPORT = PortNumber.portNumber(5);
    private static final PortNumber DSTPORT = PortNumber.portNumber(6);

    // ...<snip>...

    /**
     * Listens for devices being added/removed, and generates LinkDescriptions.
     */
    private class InternalLinkProvider implements DeviceListener {

        @Override
        public void event(DeviceEvent event) {
            // extract the device that the event is associated with
            Device dev = event.subject();

            // check if our ONOS instance has permission to configure this 
            // device - if not, ignore the event
            if (!MASTER.equals(roleService.getLocalRole(dev.id()))) {
                return;
            }

            // extract the event type, act accordingly 
            switch (event.type()) {
            case DEVICE_ADDED:
                addLink(dev);
                break;
            case DEVICE_REMOVED:
                removeLink(dev);
                break;
            default:
                break;
            }
        }

        /**
         * "create" links by passing LinkDescriptors to the Core with
         * "link found" context, via the linkDetected() method
         */
        private void addLink(Device current) {
            // update our list of configurable devices
            devices.add(current.id());
            // No link if only one device
            if (devices.size() == 1) {
                return;
            }

            // Connect new device to the last-seen device with a link
            DeviceId prev = devices.get(devices.size() - 2);
            // Create endpoints (ConnectPoints) on each device
            ConnectPoint src = new ConnectPoint(prev, SRCPORT);
            ConnectPoint dst = new ConnectPoint(current.id(), DSTPORT);

            // Create LinkDescriptions for the two 'halves' of the duplex
            // Link: src --> dst and dst --> src 
            LinkDescription fdesc = new DefaultLinkDescription(src, dst,
                    Link.Type.DIRECT);
            LinkDescription rdesc = new DefaultLinkDescription(dst, src,
                    Link.Type.DIRECT);

            // Save created Description for later use (for flickering, step 4)
            descriptions.put(src, fdesc);
            descriptions.put(dst, rdesc);

            // Tell the Core that we have detected a link
            providerService.linkDetected(fdesc);
            providerService.linkDetected(rdesc);
        }

        /*
         * "remove" a link by passing a LinkDescriptor to the Core with
         * "link removed" context, via the linkVanished() method
         */
        private void removeLink(Device device) {
            providerService.linksVanished(device.id());
            devices.remove(device.id());
        }
    }
 }
```

Several things to note here are:

* *A `LinkDescription` is a summary of a network link that the Provider has discovered.* While this Provider fakes the discovery of a link, a proper Provider would also implement some mechanism to communicate with the network. For example, the `LLDPLinkProvider` maintains a `LinkDiscovery` object per known device. `LinkDiscovery` sends and receives LLDPs to and from its network device via its reference to the PacketService.
* *The Mastership check is needed for function in a cluster*.The Provider cannot create a link between devices that the ONOS instance it runs on isn't master for, or if the instance isn't master for one endpoint.

### Add the LinkDriver.

In addition to creating the illusion of a topology, our Provider generates a steady stream of *LinkDescription*s for the core to handle during a stress test. We add this function as a internal `LinkDriver` class that sends previously-created *LinkDescription*s to the core with the premise that the links that they describe are flapping.

**NullLinkProvider.java - class LinkDriver** Expand source

```
// more new imports
import static org.onlab.util.Tools.delay;

// ...<snip>...

public class NullLinkProvider extends AbstractProvider implements LinkProvider { 

    // ...<snip>...

    private static final PortNumber DSTPORT = PortNumber.portNumber(6);

    // Default values for tunable parameters
    private static final boolean FLICKER = true;
    private static final int DEFAULT_RATE = 3000;

    // true: cause links to appear to flap
    private boolean flicker = FLICKER;
    // cause link to flap every specified number of milliseconds
    private int eventRate = DEFAULT_RATE;

    // ...<snip>...

    /**
     * Generate Descriptions to make Links appear to be flapping
     */
    private class LinkDriver implements Runnable {

        @Override
        public void run() {
            log.info("LinkDriver started");

            // continue generating Descriptions until thread is torn down
            while (!linkDriver.isShutdown()) {
                for (LinkDescription desc : descriptions.values()) {
                    // link went down
                    providerService.linkVanished(desc);
                    delay(eventRate);
                    // link came back
                    providerService.linkDetected(desc);
                    delay(eventRate);
                }
            }
        }
    }

}
```

The *LinkDriver* is launched as a task in a separate thread, so we must wire it into the Provider so that it is started and stopped with the Provider.

**NullLinkProvider.java - class LinkDriver** Expand source

```
// more new imports
import static org.onlab.util.Tools.namedThreads;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

// ...<snip>...

public class NullLinkProvider extends AbstractProvider implements LinkProvider { 

    // ...<snip>...

    private int eventRate = DEFAULT_RATE;
    
    // Single-threaded executor. Thread is named to make it easier to  
    // find in logs.
    private ExecutorService linkDriver = Executors.newFixedThreadPool(1,
            namedThreads("null-link-driver"));

    // ...<snip>...

    @Activate
    public void activate() {
        providerService = providerRegistry.register(this);
        deviceService.addListener(linkProvider);
        linkDriver.submit(new LinkDriver());
        log.info("started");
    }

    @Deactivate
    public void deactivate() {
        if (flicker) {
            try {
                linkDriver.awaitTermination(1000, TimeUnit.MILLISECONDS);
            } catch (InterruptedException e) {
                log.error("LinkBuilder did not terminate");
            }
            linkDriver.shutdownNow();
        }
        deviceService.removeListener(linkProvider);
        providerRegistry.unregister(this);
        deviceService = null;

        log.info("stopped");
    }   

    // ...<rest of class>...
}
```

### Prepare for packaging as an ONOS application

Since our provider comprises of multiple OSGi bundles, we need to package it as a multi-bundle application. To do this, we should create a separate module as a peer to the other bundle projects. This module will be responsible for producing the ONOS application archive (`.oar`) file. The convention is to call such modules `app`.  This base directory if this module should contain an `app.xml` and a `features.xml` files.

The `app.xml` defines the application name, version and origin and specifies that the application is backed by the given Apache Karaf feature(s). It is also used as a packaging manifest to instruct the `onos-maven-plugin` about which bundles to include into to the resulting `.oar` file. In our case, the file should look as follows:

**app.xml** Expand source

```
<app name="org.onosproject.null" origin="ON.Lab" version="${project.version}"
     featuresRepo="mvn:${project.groupId}/${project.artifactId}/${project.version}/xml/features"
     features="${project.artifactId}">
    <description>${project.description}</description>
    <artifact>mvn:${project.groupId}/onos-null-device/${project.version}</artifact>
    <artifact>mvn:${project.groupId}/onos-null-link/${project.version}</artifact>
    <artifact>mvn:${project.groupId}/onos-null-host/${project.version}</artifact>
    ...
</app>
```

The `features.xml` defines the bundles that comprise the Apache Karaf feature(s) and therefore which bundles should be installed and activated when the features is installed by Apache Karaf.

![](../../assets/error.png)

ONOS OpenFlow providers and NetConf providers can be used as reference points for the module organization.

### Build the Provider application

Since we have modified several POM files up to the Provider root *pom.xml*, we build the project from *${ONOS\_ROOT}/providers/* .

```
$ cd ${ONOS_ROOT}/providers && mvn clean install
```

Once the build process finishes, we can test out our new provider.

## Loading the Provider(s)

Since the protocol-specific southbound module is just another application, it can be loaded in the same way as any other application using the `onos-app` utility or ONOS REST API.

## What next?

* Try extending this Provider to make its link flapping features configurable in the [Configurability Tutorial](configurability-tutorial.md).
* Check out the [Documentation Set](https://wiki.onosproject.org/display/ONOS/Documentation+Set) for deep dives into the architecture or the development process.
