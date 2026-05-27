# CLI and Service Tutorial

## Overview

This tutorial will show you how to create a CLI command to print the endpoints found by the reactive forwarding application from the [Application tutorial](#). After completing this tutorial, you will understand:

* How to extend applications with new services
* How to extend the Karaf-based ONOS CLI with new commands

As a reference, our collection of additions/modifications can be summarized in the following directory layout:

```
${ONOS_ROOT}/apps/pom.xml (apps parent POM)
         |    |  
         |    /ifwd/pom.xml (application POM)
         |         |
         |         /src/main/java/org/onosproject/ifwd/IntentReactiveForwarding.java (the application)
         |             |                              |
         |             |                              /package-info.java (optional documentation/annotations)
         |             |
         |             /test/java/org/onosproject/ifwd/ (Unit tests go here)
         |
         /core/api/src/main/java/org/onosproject/net/apps/ForwardingMapService.java (the service interface)
         |
         /cli/src/main/java/org/onosproject/cli/net/ForwardingMapCommand.java (the command)
                      |
                      /resources/OSGI-INF/blueprint/shell-config.xml (Karaf shell configuration)
```

### Conventions

*${ONOS\_ROOT}* refers to the project root directory for ONOS. For example, if the project directory is *~/onos\_next*,  `cd ${ONOS_ROOT}` is equivalent to `cd ~/onos_next` .

We also assume that the you have a Mininet installation, as we will be testing our work against it.

## Offering services to other modules

If you want your module to be able to provide services to other modules, you should define a service interface and have your module class implement it.

### 1. Define a service interface.

We start by defining a new interface for the service in the onos-api package (*${ONOS\_ROOT}/**core/api/src/main/java/org/onosproject/net/*). We also create a new directory, *apps/*, for our service interface to reside in. The interface is added to this location so that the *cli* package that implements the commands has access to it.

**ForwardingMapService.java** Expand source

```
/*
 * Copyright 2014 Open Networking Laboratory
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
 
package org.onosproject.net.apps;

import java.util.Map;

import org.onosproject.net.HostId;

/**
 * A demonstrative service for the intent reactive forwarding application to
 * export.
 */
public interface ForwardingMapService {

    /**
     * Get the endpoints of the host-to-host intents that were installed.
     *
     * @return maps of source to destination
     */
    public Map<HostId, HostId> getEndPoints();

}
```

### 2. Import the service interface.

Next, we implement our service in `IntentReactiveForwarding`. We also indicate to Karaf that the application exports a service, using the the Felix SCR annotation `@Service`:

**IntentReactiveForwarding.java** Expand source

```
/*
 * Copyright 2014 Open Networking Laboratory
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
package org.onosproject.ifwd;

import java.util.Collections;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

import org.apache.felix.scr.annotations.Activate;
import org.apache.felix.scr.annotations.Component;
import org.apache.felix.scr.annotations.Deactivate;
import org.apache.felix.scr.annotations.Reference;
import org.apache.felix.scr.annotations.ReferenceCardinality;
import org.apache.felix.scr.annotations.Service;
import org.onosproject.core.ApplicationId;
import org.onosproject.core.CoreService;
import org.onosproject.net.Host;
import org.onosproject.net.HostId;
import org.onosproject.net.PortNumber;
import org.onosproject.net.apps.ForwardingMapService;
import org.onosproject.net.flow.DefaultTrafficSelector;
import org.onosproject.net.flow.DefaultTrafficTreatment;
import org.onosproject.net.flow.TrafficSelector;
import org.onosproject.net.flow.TrafficTreatment;
import org.onosproject.net.host.HostService;
import org.onosproject.net.intent.HostToHostIntent;
import org.onosproject.net.intent.IntentService;
import org.onosproject.net.packet.DefaultOutboundPacket;
import org.onosproject.net.packet.InboundPacket;
import org.onosproject.net.packet.OutboundPacket;
import org.onosproject.net.packet.PacketContext;
import org.onosproject.net.packet.PacketProcessor;
import org.onosproject.net.packet.PacketService;
import org.onosproject.net.topology.TopologyService;
import org.onlab.packet.Ethernet;
import org.slf4j.Logger;

import static org.slf4j.LoggerFactory.getLogger;

@Component(immediate = true)
@Service
public class IntentReactiveForwarding implements ForwardingMapService {

	private final Logger log = getLogger(getClass());

    @Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
    protected CoreService coreService;

    // ...<snip>...
 
    // Install a rule forwarding the packet to the specified port.
    private void setUpConnectivity(PacketContext context, HostId srcId, HostId dstId) {
        TrafficSelector selector = DefaultTrafficSelector.builder().build();
        TrafficTreatment treatment = DefaultTrafficTreatment.builder().build();
        HostToHostIntent intent = new HostToHostIntent(appId, srcId, dstId,
                                                       selector, treatment);
        intentService.submit(intent);
    }
 
    // the new service method, to be filled out
    @Override
    public Map<HostId, HostId> getEndPoints() {
        return null;
    }
}
```

Although we won't be using it here in this manner in this tutorial, the `@Service`annotation enables another class to reference the service through the `@Reference` annotation:

**Felix annotation reference**

```
@Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
protected ForwardingMapService fwdMapService;
```

### 3. Implement the service.

We can now define the new method. We add a new Map, `endPoints`, to `IntentReactiveForwarding`. The map is populated when the `ReactivePacketProcessor`'s `process()` method finds endpoints known by the *HostService*.

**IntentReactiveForwarding.java - service** Expand source

```
@Component(immediate = true)
@Service
public class IntentReactiveForwarding implements ForwardingMapService {

    // ...<snip>...
    private ApplicationId appId;

    // Map for storing found endpoints, for our service. It is protected
    // so that process() can access it.
    protected final ConcurrentMap<HostId, HostId> endPoints = new ConcurrentHashMap<>();

    // ...<snip>...
    /**
     * Packet processor responsible for forwarding packets along their paths.
     */
    private class ReactivePacketProcessor implements PacketProcessor {

        @Override
        public void process(PacketContext context) {
            // Stop processing if the packet has been handled, since we
            // can't do any more to it.
            if (context.isHandled()) {
            
            // ...<snip>...
            
            if (dst == null) {
                flood(context);
                return;
            }
            // Add found endpoints to map.
            endPoints.put(srcId, dstId);

            // Otherwise forward and be done with it.
            setUpConnectivity(context, srcId, dstId);
            forwardPacketToDst(context, dst);
        }
    }

    // ...<snip>...

    @Override
    public Map<HostId, HostId> getEndPoints() {
        // Return our map as a read-only structure.
        return Collections.unmodifiableMap(endPoints);
    }
}
```

Now, a module referencing the *ForwardingMapService* may call `getEndPoints()` to get a list of directional endpoints for which intents were installed, and traffic can flow between.

Next, we will create a CLI command to use this new service. This command will list the contents of this map, and also provide the option to take a parameter (a host ID), to filter on that host as a source.

## Creating a command

The CLI commands are defined in the project directory ${ONOS\_ROOT}*/cli/.* There are two types of commands, with their source files located in the following locations:

* ***${ONOS\_ROOT}/cli/src/main/java/org/onosproject/cli -***Commands related to system configuration and monitoring
* ***${ONOS\_ROOT}/cli/src/main/java/org/***onosproject***/cli/net -*** Commands related to network configuration and monitoring

Since our command will display network-related  information, we will add our command to the second *net* directory. 

### 1. Create a command class.

We create the following class skeleton for our new command, tentatively named `ForwardingMapCommand`. Our class is a child of `AbstractShellCommand`, and uses some command-related annotations:

* `@Command` -  used to set a command's name, scope, and description.
* `@Argument` - used to indicate that a variable is set by a command-line argument.

**ForwardingMapCommand.java** Expand source

```
/*
 * Copyright 2014 Open Networking Laboratory
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
 
package org.onosproject.cli.net;

import org.apache.karaf.shell.commands.Argument;
import org.apache.karaf.shell.commands.Command;
import org.onosproject.cli.AbstractShellCommand;
import org.onosproject.net.HostId;
import org.onosproject.net.apps.ForwardingMapService;

/**
 * A demo service that lists the endpoints for which intents are installed.
 */
@Command(scope = "onos", name = "fwdmap",
        description = "Lists the endpoints for which intents are installed")
public class ForwardingMapCommand extends AbstractShellCommand {
 
    @Argument(index = 0, name = "hostId", description = "Host ID of source",
            required = false, multiValued = false)
    private HostId hostId = null;

    @Override
    protected void execute() {
    }
}
```

The annotations enable this particular command to be invoked as `fwdmap` or `onos:fwdmap` at the CLI. In addition, it can also take a host ID as an option, e.g. `fwdmap 06:38:27:D5:68:88/-1`.

### 2. Incorporate the new service.

Next, we implement the command. In our case, it is pretty simple - we ask the service for its endpoint map, and if we were given a host ID, we search for it in the map. The full class definition looks like this:

**ForwardingMapCommand.java** Expand source

```
/*
 * Copyright 2014 Open Networking Laboratory
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

package org.onosproject.cli.net;

import java.util.Map;

import org.apache.karaf.shell.commands.Argument;
import org.apache.karaf.shell.commands.Command;
import org.onosproject.cli.AbstractShellCommand;
import org.onosproject.net.HostId;
import org.onosproject.net.apps.ForwardingMapService;

/**
 * A demo service that lists the endpoints for which intents are installed.
 */
@Command(scope = "onos", name = "fwdmap",
        description = "Lists the endpoints for which intents are installed")
public class ForwardingMapCommand extends AbstractShellCommand {
 
    // formatted string for output to CLI
    private static final String FMT = "src=%s, dst=%s";

    // the String to hold the optional argument
    @Argument(index = 0, name = "hostId", description = "Host ID of source",
            required = false, multiValued = false)
    private String hostId = null;

    // reference to our service
    private ForwardingMapService service;
    // to hold the service's response
    private Map<HostId, HostId> hmap;

    @Override
    protected void execute() {
        // get a reference to our service
        service = get(ForwardingMapService.class);

        /*
         * getEndPoints() returns an empty map even if it contains nothing, so
         * we don't need to check for null hmap here.
         */
        hmap = service.getEndPoints();

        // check for an argument, then display information accordingly
        if (hostId != null) {
            // we were given a hostId to filter on, print only those that match
            HostId host = HostId.hostId(hostId);
            for (Map.Entry<HostId, HostId> el : hmap.entrySet()) {
                if (el.getKey().equals(hostId)) {
                    print(FMT, el.getKey(), el.getValue());
                }
            }
        } else {
            // print everything we have
            for (Map.Entry<HostId, HostId> el : hmap.entrySet()) {
                print(FMT, el.getKey(), el.getValue());
            }
        }
    }
}
```

### 3. Register the command with Karaf CLI.

Next, we need to tell Karaf about our new command by editing ***shell-config.xml,*** located in ***${ONOS\_ROOT}/****cli/src/main/resources/OSGI-INF/blueprint/**.* We add the following to the contents between the `<command-bundle></command-bundle>` clause in the file:

**shell-config.xml**

```
        <command>
            <!--Our command implementation's FQDN-->
            <action class="org.onosproject.cli.net.ForwardingMapCommand"/>
            <!--A command completer for Host IDs-->
            <completers>
                <ref component-id="hostIdCompleter"/>
                <null/>
            </completers>
        </command>
```

## Verification

Once we rebuild ONOS, we can test our command out.

### 1. Rebuild and restart ONOS.

Rebuild and relaunch ONOS.

```
$ cd ${ONOS_ROOT}
$ mvn clean install
$ karaf clean
```

The last command re-launches the CLI. The new command should be available as part of the listing for `help onos`:

```
onos> help onos | grep fwdmap
onos:fwdmap
onos> fwdmap --help
DESCRIPTION
    onos:fwdmap

	Lists the endpoints for which intents are installed

SYNTAX
        onos:fwdmap [options] [hostId] 

ARGUMENTS
        hostId
                Host ID of source

OPTIONS
        -j, --json
                Output JSON
        --help
                Display this help message
```

### 2. Launch a Mininet test network.

Launch a small Mininet network with four hosts, pointing at our ONOS instance (192.168.56.20 in this example):

```
$ sudo mn --topo=tree,2,2 --controller=remote,ip=192.168.56.20 --mac
*** Creating network
...
mininet>
```

Your ONOS instance should see four hosts:

```
onos> hosts
id=00:00:00:00:00:01/-1, mac=00:00:00:00:00:01, location=of:0000000000000002/1, vlan=-1, ip(s)=[]
id=00:00:00:00:00:02/-1, mac=00:00:00:00:00:02, location=of:0000000000000002/2, vlan=-1, ip(s)=[]
id=00:00:00:00:00:03/-1, mac=00:00:00:00:00:03, location=of:0000000000000003/1, vlan=-1, ip(s)=[]
id=00:00:00:00:00:04/-1, mac=00:00:00:00:00:04, location=of:0000000000000003/2, vlan=-1, ip(s)=[]
```

### 3. Test out the command.

Without traffic, the command won't return anything:

```
onos> fwdmap
onos>
```

So, generate traffic on Mininet:

```
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 h4 
h2 -> h1 h3 h4 
h3 -> h1 h2 h4 
h4 -> h1 h2 h3 
*** Results: 0% dropped (12/12 received)
```

And retry the command. You should see four entries:

```
onos> fwdmap
src=00:00:00:00:00:04/-1, dst=00:00:00:00:00:03/-1
src=00:00:00:00:00:03/-1, dst=00:00:00:00:00:04/-1
src=00:00:00:00:00:02/-1, dst=00:00:00:00:00:04/-1
src=00:00:00:00:00:01/-1, dst=00:00:00:00:00:02/-1
```

Since we have specified for an optional argument, we can also filter on source host ID:

```
onos> fwdmap 00:00:00:00:00:04/-1
src=00:00:00:00:00:04/-1, dst=00:00:00:00:00:03/-1
```

We had also configured autocomplete, so we are presented with the available options when we hit **Tab**:

```
onos> fwdmap <tab>
onos> fwdmap 00:00:00:00:00:0
00:00:00:00:00:01/-1   00:00:00:00:00:02/-1   00:00:00:00:00:03/-1   00:00:00:00:00:04/-1
```

## What next?

* Check out the [Documentation Set](https://wiki.onosproject.org/display/ONOS/Documentation+Set) for deep dives into the architecture or the development process.

---

[Return To : Tutorials and Walkthroughs](../tutorials.md)

---
