# Controlling P4Runtime-enabled Mellanox Spectrum switch with ONOS

In this tutorial, you will learn how to set up a P4Runtime-enabled Mellanox Spectrum switch, using the ONOS SDN controller. The following set of instructions have been tested using the ONOS fabric.p4 topology.

# Requirements

* 1 or more Spectrum DVS based switches with the following minimum versions:
  + 4.9.30-OpenNetworkLinux
  + SX-SDK Version: 4\_2\_7000X019
  + SX-API Version: 1.0.0
  + SXD Version: 1.00
  + Firmware Version of Device #1: 13.1600.156
  + Custom P4-Runtime gRPC server

* 1 server with the ONOS release 1.13 installed:
  + [https://wiki.onosproject.org/display/ONOS/Downloads](../downloads.md)
  + <https://github.com/opennetworkinglab/onos/releases/tag/1.13.1>

# Prepare the switch

1. Install the Mellanox ethernet switch SDK and all necessary MST tools
2. Install P4Runtime dependencies. You will need to install/build the following packages (make sure you do a "apt-get update")
   * general dev tools
     + apt-get install autoconf automake libtool unzip libtool-bin pkg-config autoconf-archive cmake
   * p4runtime
     + apt-get install libjudy-dev libreadline-dev valgrind libtool-bin libboost-dev libboost-system-dev libmicrohttpd-dev libssl1.0-dev libgc-dev curl
     + [nanomsg 1.0.0](https://github.com/nanomsg/nanomsg/releases/tag/1.0.0)
     + [protobuf v3.2.0](https://github.com/google/protobuf/releases/tag/v3.2.0)
     + git clone <https://github.com/p4lang/PI>
       - cd PI
       - git submodule update --init
       - git checkout a2767fc
       - ./autogen.sh;./configure --with-proto
       - make; make install;
   * [bmv2](https://github.com/p4lang/behavioral-model) (optional)
     + [thrift 0.9.2](https://github.com/apache/thrift/releases/tag/0.9.2)
     + apt-get install libssl-dev g++ pkg-config bison flex libevent-dev libboost-thread-dev libboost-filesystem-dev libgmp-dev libpcap-dev libboost-test-dev libboost-program-options-dev
   * spectrum grpc agent
     + apt-get install libpcap-dev
3. Install the Mellanox gRPC server process. It is critical that the versions of the PI and gRPC libraries are aligned between the server process and the ONOS client.  
   The grpc service can be started manually using:

**Start switchd**

```
spectrum-switch> /usr/bin/dvs_start.sh
spectrum-switch> /usr/local/bin/mlnx_grpc_server
```

Alternatively, you may install the provided init.d scripts that perform the above commands on reboot.

* /etc/init.d/mlnx-dvs.sh
* /etc/init.d/mlnx-grpc.sh

Currently, the mlnx\_grpc\_server starts on the switch **with the fabric.P4 program deployed.** **The program is configured later by ONOS using P4Runtime.**  Please see [Appendix H: ONOS+P4 Development Environment#UpdateP4toolstolatestversion](../guides/developer-guide/appendix-h-onosp4-development-environment.md) for more information. The server uses the standard P4Runtime gRPC port 50051.

# Understanding the pipeconf for the fabric.P4 program

In ONOS the term pipeconf (short of pipeline configuration) is used to describe the ensemble of P4 compiler artifacts and ONOS driver for a specific P4 program. A pipeconf is the entity that allows ONOS to deploy and control a given P4 program. A pipeconf is defined as an ONOS application that can be loaded at runtime. Currently the only pipeline supported for Spectrum is fabric.p4, although support for other pipelines will be forethcoming. You can see the ONOS repository for the fabric.p4 pipeline description. It provides basic MPLS based forwarding capabilities along with packet-in/out support and counters. Among others, this pipeconf defines two important classes, an interpreter implementation, and a pipeconf loader. The fabric pipeline can be found in github [here](https://github.com/opennetworkinglab/onos/blob/onos-1.13/pipelines/fabric/src/main/resources/fabric.p4).

### Interpreter

The interpreter is what enables ONOS to understand the specific constructs of your P4 Program. For example, the Interpreter enables the translation from ONOS traffic treatments to P4-defined actions.

The interpreter implementation for the fabric pipeconf can be found [here](https://github.com/opennetworkinglab/onos/blob/master/pipelines/fabric/src/main/java/org/onosproject/pipelines/fabric/FabricInterpreter.java).

### Pipeconf loader

This class is usually defined as an OSGi runtime component and is used to register the pipeconf at runtime. As part of this operation, this class is responsible for putting together all the pieces of a pipeconf, such as:

* P4Info for your program.
* any binary or target specific configuration files

Binaries and target configurations are generated with the Mellanox P4C backend compiler, which is not open-source. For this reason, ONOS provides the [compiler output of the fabric P4 program for BMv2](https://github.com/opennetworkinglab/onos/tree/master/pipelines/fabric/src/main/resources/p4c-out/bmv2) (generated using the publicly available p4c compiler), but cannot provide the mlnx\_grpc\_server binary and configuration files in the ONOS repository. *For more information on how to obtain the mlnx\_grpc\_server binary,**please reach out to Mellanox.*

Looking at the [pipeconf loader implementation](https://github.com/opennetworkinglab/onos/blob/master/pipelines/fabric/src/main/java/org/onosproject/pipelines/fabric/PipeconfLoader.java), you can see we can also add driver behaviors specific to that P4 program/pipeline, such as the Pipeliner and the PortStatisticsDiscovery. We also need to set a pipeconf ID, which has to be globally unique as it will be used to refer to that pipeconf in the netcfg JSON later.

# Walkthrough

Moving to the ONOS controller on the server, assuming you downloaded it and placed your pipeconf in it.

Run ONOS

**Start ONOS**

```
$ buck run onos-local -- clean debug
```

It's worth noting that this start ONOS in a single instance cluster. The command also build ONOS and purges any previous state. The debug option offers the possibility to attach the debugger on port 5005.

**Login into the ONOS CLI**

Having started ONOS we need to login in its CLI.

```
onos localhost
```

**Start the Mellanox drivers**

**Activate Drivers**

```
onos> app activate org.onosproject.drivers.mellanox
```

This command brings in all the needed applications to interact with the Spectrum-based switch. If running another switch in the topology (e.g. bmv2 as a leaf), also activate it now.

**Load the pipeconf**

**Start ONOS**

```
onos> app activate org.onosproject.pipelines.fabric
onos> app activate lldpprovider hostprovider
```

**Verify the active applications**

```
onos> apps -s -a
```

Verify that these apps at least are active in your ONOS environment:

* org.onosproject.generaldeviceprovider (General Device Provider)
* org.onosproject.drivers (Default Drivers)
* org.onosproject.protocols.grpc (gRPC Protocol Subsystem)
* org.onosproject.protocols.p4runtime (P4Runtime Protocol Subsystem)
* org.onosproject.p4runtime (P4Runtime Provider)
* org.onosproject.drivers.p4runtime (P4Runtime Drivers)
* org.onosproject.drivers.mellanox (Mellanox Drivers)

# Build and push a configuration json

Having all the needed components in ONOS in place we can now tell ONOS about the device(s) and let the interaction begin.

First we need to create a .json file containing all the needed information such as IP/port of the P4Runtime server running on the device, its data plane ports and the pipeconf we want to deploy.

```
{
  "devices": {
    "device:mellanox:spine1": {
      "generalprovider": {
        "p4runtime": {
          "ip": "10.209.80.43",
          "port": 50051,
          "deviceKeyId": "p4runtime:device:mellanox:spine1",
          "deviceId": 0
        }
      },
      "piPipeconf": {
        "piPipeconfId": "org.onosproject.pipelines.fabric"
      },
      "ports": {
        "2/0": {
          "name": "2/0 VM5",
          "speed": 100000,
          "enabled": true,
          "number": 2,
          "removed": false,
          "type": "copper"
        },
        "3/0": {
          "name": "3/0 VM6",
          "speed": 100000,
          "enabled": true,
          "number": 3,
          "removed": false,
          "type": "copper"
        },
        "10/0": {
          "name": "10/0 VM7",
          "speed": 100000,
          "enabled": true,
          "number": 10,
          "removed": false,
          "type": "copper"
        }
      },
      "basic": {
        "driver": "mellanox",
        "name": "spine1"
      }
    }
  }
}
 
```

In this example, we assumed the device has been configured with 3 data plane ports, for each port the "number" value corresponds to the label port value on the Mellanox Spectrum switch (see section below). The port number by default for the gRPC/P4Runtime server is 50051, so unless you made any changes to that leave it as is.

Upload the configuration you just wrote to the instance of ONOS you are running:

```
<your_machine>~$ onos-netcfg localhost <path_to_your_json_configuration_file>
```

Check the ONOS log for possible errors.

To check if the device, links and interfaces have been discovered by ONOS:

```
onos> devices
onos> links
onos> interfaces
```

Configure ports on the device.

The last step to perform is to configure the ports on the switch. This needs to be done after having pushed the pipeline config, hence after having pushed the netcfg JSON to ONOS.

```
spectrum-switch> /usr/bin/sx_api_port_speed_set_100G.py
spectrum-switch> /usr/bin/sx_api_ports_dump.py
```

You should see that the connected label ports are plugged in, administratively and operationally up.

# Use

At this point if everything went well you should be able to push flow rules defined with **PiCriterion** and **PiInstruction**according to the fabric.P4 program deployed on the device.

# Simulation using Mininet and BMV2

This section is based on [https://wiki.onosproject.org/display/ONOS/Try+fabric.p4+with+ONOS+and+bmv2](../apps-and-use-cases/fabric.p4-trellis-support-by-p4-devices/try-fabric.p4-with-onos-and-bmv2.md)

You can simulate a fabric topology using a physical Spectrum switch and virtial software switches (BMV2 under mininet).

1. Setup ONOS 1.13

   See the onos project wiki. Make sure p4tools is installed without errors. Setup the bash environment

   Build onos if necessary.

   Create the Mellanox JSON files (se below)
2. Setup VM environment for ONOS

You can export various environment variables to make it more seemless

export ONOS\_ROOT=/root/onos

source $ONOS\_ROOT/tools/dev/bash\_profile

export ONOS\_IP=10.212.234.6

export ONOS\_APPS="drivers.bmv2,drivers.mellanox,pipelines.fabric,proxyarp,lldpprovider,hostprovider,segmentrouting"

Or you can manually activate on ONOS CLI

 ssh password: rocks

onos localhost

onos> app activate bmv2 mellanox fabric lldpprovider hostprovider

Veriy that only this set of apps is running:

onos> apps -s -a

\*  10 org.onosproject.generaldeviceprovider 1.13.0.SNAPSHOT General Device Provider

\*  11 org.onosproject.protocols.grpc       1.13.0.SNAPSHOT gRPC Protocol Subsystem

\*  12 org.onosproject.protocols.p4runtime  1.13.0.SNAPSHOT P4Runtime Protocol Subsystem

\*  13 org.onosproject.p4runtime            1.13.0.SNAPSHOT P4Runtime Provider

\*  14 org.onosproject.drivers              1.13.0.SNAPSHOT Default Drivers

\*  15 org.onosproject.drivers.p4runtime    1.13.0.SNAPSHOT P4Runtime Drivers

\*  16 org.onosproject.pipelines.basic      1.13.0.SNAPSHOT Basic Pipelines

\*  17 org.onosproject.pipelines.fabric     1.13.0.SNAPSHOT Fabric Pipeline

\*  18 org.onosproject.drivers.mellanox     1.13.0.SNAPSHOT Mellanox Drivers

\*  19 org.onosproject.hostprovider         1.13.0.SNAPSHOT Host Location Provider

\*  20 org.onosproject.lldpprovider         1.13.0.SNAPSHOT LLDP Link Provider

\*  41 org.onosproject.protocols.gnmi       1.13.0.SNAPSHOT gNMI Protocol Subsystem

\*  70 org.onosproject.drivers.gnmi         1.13.0.SNAPSHOT gNMI Drivers

\*  77 org.onosproject.drivers.bmv2         1.13.0.SNAPSHOT BMv2 Drivers

3. Configure the nodes with netcfg. Warning - pause between each netcfg step, to let ONOS to program the flows in sequence.

onos-netcfg localhost bmv2-leafs-mlx.json

**bmv2-leafs-mlnx.json**

```
{
  "devices": {
    "device:bmv2:204": {
      "segmentrouting": {
        "name": "leaf1",
        "ipv4NodeSid": 204,
        "ipv4Loopback": "192.168.0.204",
        "ipv6NodeSid": 214,
        "ipv6Loopback": "2000::c0a8:0204",
        "routerMac": "00:00:00:00:02:04",
        "isEdgeRouter": true,
        "adjacencySids": []
      }
    },
    "device:bmv2:205": {
      "segmentrouting": {
        "name": "leaf2",
        "ipv4NodeSid": 205,
        "ipv4Loopback": "192.168.0.205",
        "ipv6NodeSid": 215,
        "ipv6Loopback": "2000::c0a8:0205",
        "routerMac": "00:00:00:00:02:05",
        "isEdgeRouter": true,
        "adjacencySids": []
      }
    },
    "device:mellanox:spine1": {
      "segmentrouting": {
        "name": "spine1",
        "ipv4NodeSid": 227,
        "ipv4Loopback": "192.168.0.227",
        "ipv6NodeSid": 237,
        "ipv6Loopback": "2000::c0a8:0227",
        "routerMac": "00:00:00:00:02:27",
        "isEdgeRouter": false,
        "adjacencySids": []
      }
    }
  },
  "ports": {
    "device:bmv2:204/1": {
      "interfaces": [
        {
          "name": "leaf1-host",
          "ips": [
            "10.0.2.254/24"
          ],
          "vlan-untagged": 10
        }
      ]
    },
    "device:bmv2:205/1": {
      "interfaces": [
        {
          "name": "leaf2-host",
          "ips": [
            "10.0.3.254/24"
          ],
          "vlan-untagged": 20
        }
      ]
    }
  }
}
```

onos-netcfg localhost mellanox-spine1.json

**mellanox-spine1**

```
{
  "devices": {
    "device:mellanox:spine1": {
      "generalprovider": {
        "p4runtime": {
          "ip": "10.209.80.43",
          "deviceKeyId": "p4runtime:device:mellanox:spine1",
          "port": 50051,
          "deviceId": 0
        }
      },
      "piPipeconf": {
        "piPipeconfId": "org.onosproject.pipelines.fabric"
      },
      "ports": {
        "3/0": {
          "name": "3/0",
          "speed": 10000,
          "enabled": true,
          "number": 3,
          "removed": false,
          "type": "copper"
        },
        "7/0": {
          "name": "7/0",
          "speed": 10000,
          "enabled": true,
          "number": 7,
          "removed": false,
          "type": "copper"
        }
      },
      "basic": {
        "driver": "mellanox",
        "name": "spine1"
      },
      "segmentrouting": {
        "name": "spine1",
        "ipv4NodeSid": 227,
        "ipv4Loopback": "192.168.0.227",
        "ipv6NodeSid": 237,
        "ipv6Loopback": "2000::c0a8:0227",
        "routerMac": "00:00:00:00:02:27",
        "isEdgeRouter": false,
        "adjacencySids": []
      }
    }
  }
}
```

Start mininet with 2 BMV2 leaves (you will need to have simple\_switch\_grpc installed from p4lang/behavioral\_model)

**Mininet**

```
#!/usr/bin/python

import os
import sys
import argparse
sys.path.append('..')

if 'ONOS_ROOT' not in os.environ:
    print "Environment var $ONOS_ROOT not set"
    exit()
else:
    ONOS_ROOT = os.environ["ONOS_ROOT"]
    sys.path.append(ONOS_ROOT + "/tools/dev/mininet")

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import Host, RemoteController
from mininet.link import Intf
from routinglib import RoutedHost
from bmv2 import ONOSBmv2Switch

PIPECONF_ID = 'org.onosproject.pipelines.fabric'

class Trellis( Topo ):
    "Trellis basic topology"

    def __init__( self, *args, **kwargs ):
        Topo.__init__( self, *args, **kwargs )
        s204 = self.addSwitch('s204', cls=ONOSBmv2Switch, deviceId='204', grpcport=55204, pipeconf=PIPECONF_ID, netcfgDelay=0.5)
        s205 = self.addSwitch('s205', cls=ONOSBmv2Switch, deviceId='205', grpcport=55205, pipeconf=PIPECONF_ID, netcfgDelay=0.5)

        h1 = self.addHost('h1', cls=RoutedHost, mac='00:aa:00:00:00:01', ips=['10.0.2.1/24'], gateway='10.0.2.254')
        h2 = self.addHost('h2', cls=RoutedHost, mac='00:aa:00:00:00:02', ips=['10.0.3.1/24'], gateway='10.0.3.254')
        #h1 = self.addHost('h1')
        #h2 = self.addHost('h2')

        self.addLink(s204, h1)
        self.addLink(s205, h2)
        
topos = { 'trellis' : Trellis }

def main():
    topo = Trellis()
    controller = RemoteController('c0', ip='10.212.234.6')
    net = Mininet(topo=topo, controller=None)
    net.addController(controller)

    s204 = net.switches[0]
    s205 = net.switches[1]

    # Replace ens802f0 and ens802f1
    copmute1Intf = Intf('ens6', node=s204)   # port 3
    copmute2Intf = Intf('ens6d1', node=s205)  # port 7

    net.start()
    CLI(net)
    net.stop()

if __name__ == "__main__":
    setLogLevel('debug')

    main()
```

In mininet, check the nodes:

mininet> nodes

available nodes are:

c0 h1 h2 s204 s205

4. Check ONOS status

onos> devices

 id=device:bmv2:204, available=true, local-status=connected 5s ago, role=MASTER, type=SWITCH, mfr=[p4.org](http://p4.org/),

id=device:bmv2:205, available=true, local-status=connected 5s ago, role=MASTER, type=SWITCH, mfr=[p4.org](http://p4.org/), 

id=device:mellanox:spine1, available=true, local-status=connected 16s ago, role=MASTER, type=SWITCH, mfr=

onos> links 

src=device:bmv2:204/2, dst=device:mellanox:spine1/3, type=DIRECT, state=ACTIVE, expected=false

src=device:bmv2:205/2, dst=device:mellanox:spine1/7, type=DIRECT, state=ACTIVE, expected=false

src=device:mellanox:spine1/3, dst=device:bmv2:204/2, type=DIRECT, state=ACTIVE, expected=false

src=device:mellanox:spine1/7, dst=device:bmv2:205/2, type=DIRECT, state=ACTIVE, expected=false

onos> interfaces

leaf1-host: port=device:bmv2:204/1 ips=[10.0.2.254/24] vlanUntagged=10

leaf2-host: port=device:bmv2:205/1 ips=[10.0.3.254/24] vlanUntagged=20

onos> nodes

id=10.212.234.6, address=10.212.234.6:9876, state=READY, version=1.13.0.cc722c0, updated=1d0h ago \*

5. If ONOS does not see any hosts, check ARP on mininet

From mini net CLI, run:

mininet> h1 arping h2

From ONOS CLI, check hosts:

onos> hosts

id=00:AA:00:00:00:01/None, mac=00:AA:00:00:00:01, locations=[device:bmv2:204/1], vlan=None, ip(s)=[10.0.2.1

id=00:AA:00:00:00:02/None, mac=00:AA:00:00:00:02, locations=[device:bmv2:205/1], vlan=None, ip(s)=[10.0.3.1

6. Activate and run segment routing application

onos> app activate segmentrouting

mininet> h1 ping h2

After segment routing is fully loaded, the pings from host to host should start working.

8. Verify counters and flows on ONOS web gui.

[http://ONOS\_IP/onos/ui/index.html#/topo](http://10.212.234.6:8181/onos/ui/index.html#/topo)

name: karaf

password: karaf
