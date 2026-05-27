# Try fabric.p4 with ONOS and bmv2

Updated Trellis+P4 tutorial material

The content of this page is for users who already have some experience with ONOS and Trellis and wish to learn how to use those with P4 devices.

If you are getting started with ONOS and Trellis we suggest you start with the following slides and exercises:

**Trellis+P4 Tutorial (Presented at ONF Connect, Dec 2018):** <http://bit.ly/trellis-p4-slides>.

## Environment:

### Prerequisites (ONOS, Docker)

Before starting, make sure to have **ONOS v2.2.0 or later** on your physical machine. To download, build and run ONOS, follow this guide: [Developer Quick Start](../../guides/developer-guide/developer-quick-start.md)

Make also sure that Docker is installed and you can run Docker containers in your machine ([Install Docker](https://docs.docker.com/install/)).

In this guide we will refer to `${WORKSPACE}` as the environment variable of your workspace, where we suppose also ONOS has been downloaded. Define it on your `.bashrc` file or make sure that is defined in all your terminal windows.

### P4-Mininet Docker container

We provide a convenient Docker container with Mininet and BMv2 already installed ([P4mn on Docker Hub](https://hub.docker.com/r/opennetworking/p4mn)).

To pull the container, type the following command in a terminal window on your machine:

**pull p4mn container**

```
$ docker pull opennetworking/p4mn
```

### Get Trellis "routing" repository

To try fabric.p4 with BMv2, you will need a custom Mininet script distributed as part of the Trellis "routing" repository:

To clone the repository, type the following commands in a terminal window on your machine:

**Clone Trellis routing repository**

```
cd ${WORKSPACE}
git clone https://github.com/opennetworkinglab/routing/
```

## Network configuration for this mininet topology:

Reference: <https://wiki.opencord.org/pages/viewpage.action?pageId=3014916>

In Trellis, we run every switch as router, each router needs a mac address and multiple interface configurations.

**Interface** config:

**Interface config**

```
"Device-id/port-number" : {
    "interfaces" : [
        {
            "name": "interface name",
            "ips" : [ "10.0.1.254/24" ],
            "vlan-untagged": 10
        }
    ]
}
```

* **Name**: Interface name, can be empty or unset;
* **ips**: List of IP addresses for this interface, it can be the default gateway of the host;
* **VLAN** config, it can be: *vlan-untagged* only, *vlan-tagged* only or *vlan-tagged + vlan-native*.

+ *vlan-untagged* (integer): this interface consumes untagged packet only and it belongs to a specific vlan;
+ *vlan-tagged* (integer array): this interface can consume specific tagged vlans;
+ *vlan-native* (integer): if this is an interface configured as vlan-tagged, the device will associate this vlan ID for untagged packets;

Example of **Segment Routing** device settings:

**device config**

```
"Device-id" : {
    "segmentrouting" : {
        "name" : "Device name",
        "ipv4NodeSid" : 123,
        "ipv4Loopback" : "192.168.0.123",
        "ipv6NodeSid" : 223,
        "ipv6Loopback" : "2000::c0a8:0223",
        "routerMac" : "00:00:00:00:01:23",
        "isEdgeRouter" : true,
        "adjacencySids" : []
     }
}
```

* **Name**: Name for segment routing device;
* **ipv4(6)NodeSid**: Global unique id for IP loopback, it is used as MPLS label in forwarding;
* **ipv4(6)Loopback**: Router loopback IP address, it should not be part of same subnet defined on dataplane interface;
* **routerMac**: Globally unique Mac address. It will be used to reply ARP requests for router IP or interface IP;
* **isEdgeRouter**: *true* if this device is edge/leaf, otherwise *false*;
* **adjacencySids**: **Reserved**, put empty array for now.

## Topology:

![](https://docs.google.com/drawings/u/2/d/s8DqWzX1bA9VtAlYfu47luQ/image?w=624&h=328&rev=278&ac=1)

## Host view:

In the demo Mininet topology, we set the gateway of the hosts to the IP of the interface of the leaf switch. For example, the gateway of Host 1 will be 10.0.2.254.

![](https://docs.google.com/drawings/u/2/d/sJiX_mbAsMGwZRQzwDh3ugQ/image?w=624&h=257&rev=80&ac=1)

## Steps:

In this tutorial, we need 4 terminal windows for:

* ONOS karaf process (from now on it will be called **T1**);
* ONOS shell (**T2**), identified by `onos>` shell;
* Docker P4+Mininet emulator (**T3**), identified by `mininet>` shell;
* Utility (**T4**).

So, first of all, open 4 terminal windows on your machine.

In **T1** run ONOS with the following commands:

```
$ cd ${WORKSPACE}/onos
$ ONOS_APPS=drivers,openflow,netcfghostprovider,segmentrouting,fpm,dhcprelay,routeradvertisement,t3,hostprobingprovider,drivers.bmv2,pipelines.fabric
$ bazel run onos-local -- clean
```

In **T2** connect to the ONOS shell running the following command:

```
$ onos localhost
```

Now check that the apps are correctly active. You should see something similar to the output shown below:

```
onos> apps -a -s
*   9 org.onosproject.drivers              1.13.0.SNAPSHOT Default Drivers
*  35 org.onosproject.generaldeviceprovider 1.13.0.SNAPSHOT General Device Provider
*  36 org.onosproject.protocols.grpc       1.13.0.SNAPSHOT gRPC Protocol Subsystem
*  37 org.onosproject.protocols.p4runtime  1.13.0.SNAPSHOT P4Runtime Protocol Subsystem
*  38 org.onosproject.p4runtime            1.13.0.SNAPSHOT P4Runtime Provider
*  39 org.onosproject.drivers.p4runtime    1.13.0.SNAPSHOT P4Runtime Drivers
*  42 org.onosproject.proxyarp             1.13.0.SNAPSHOT Proxy ARP/NDP
*  44 org.onosproject.hostprovider         1.13.0.SNAPSHOT Host Location Provider
*  45 org.onosproject.lldpprovider         1.13.0.SNAPSHOT LLDP Link Provider
*  73 org.onosproject.pipelines.basic      1.13.0.SNAPSHOT Basic Pipelines
*  84 org.onosproject.route-service        1.13.0.SNAPSHOT Route Service Server
*  95 org.onosproject.protocols.gnmi       1.13.0.SNAPSHOT gNMI Protocol Subsystem
*  96 org.onosproject.drivers.gnmi         1.13.0.SNAPSHOT gNMI Drivers
* 108 org.onosproject.pipelines.fabric     1.13.0.SNAPSHOT Fabric Pipeline
* 120 org.onosproject.segmentrouting       1.13.0.SNAPSHOT Segment Routing
* 121 org.onosproject.drivers.bmv2         1.13.0.SNAPSHOT BMv2 Drivers
```

From **T3**, now push the network configuration:

```
$ cd ${WORKSPACE}/routing/trellis
$ onos-netcfg localhost trellisp4.json
```

Now ONOS is running, the needed apps are correctly running and the network configuration is pushed in ONOS, we are ready to run the emulated Trellis topology on P4+Mininet Docker container.

In **T3** start the previously downloaded Docker container with the topology available in the "routing" repository.

The mininet topology of trellisp4.py python script is the one presented above with:

* 2 by 2 leaf-spine topology using 4 BMv2 devices
* 4 bidirectional links between leaf and spine
* 4 hosts, 2 hosts per leaf device

You can run the topology with the following command on **T3**:

```
$ docker run --rm -it --privileged -v /tmp/p4mn:/tmp \
	-v${WORKSPACE}/routing:/routing -w/routing/trellis \
	--name p4trellis --hostname p4trellis \
	-p 50001-50030:50001-50030 \
	--env PYTHONPATH=/root \
	--entrypoint python opennetworking/p4mn:stable trellisp4.py --onos-ip 127.0.0.1
```

The output should look like something like this:

```
Unable to contact the remote controller at 127.0.0.1:6653
Unable to contact the remote controller at 127.0.0.1:6633
Setting remote controller to 127.0.0.1:6653
*** Error setting resource limits. Mininet's performance may be affected.
*** Creating network
*** Adding hosts:
h1 h2 h3 h4
*** Adding switches:
s204 s205 s226 s227
*** Adding links:
(h1, s204) (h2, s204) (h3, s205) (h4, s205) (s226, s204) (s226, s205) (s227, s204) (s227, s205)
*** Configuring hosts
h1 h2 h3 h4
*** Starting controller	
c0
*** Starting 4 switches
s204 .........⚡️ simple_switch_grpc @ 50001
s205 .........⚡️ simple_switch_grpc @ 50002
s226 ......⚡️ simple_switch_grpc @ 50003
s227 .....⚡️ simple_switch_grpc @ 50004

*** Starting CLI:
mininet>
```

Since the Mininet Python script running inside the Container is not able to contact the ONOS controller (as you can see from the first 2 rows of the output above), we need to submit the Network Configuration on our own using the `onos-netcfg` command as we have done before.

To do so, on **T4**, run the following commands:

```
$ cd /tmp/p4mn
$ onos-netcfg localhost bmv2-s204-netcfg.json
$ onos-netcfg localhost bmv2-s205-netcfg.json
$ onos-netcfg localhost bmv2-s226-netcfg.json
$ onos-netcfg localhost bmv2-s227-netcfg.json
```

On **T1** (Onos Karaf process) you should see that ONOS received the configuration and has configured the device.

To check we can run the following commands on **T2** (onos shell):

```
onos> devices -s
id=device:bmv2:204, available=true, role=MASTER, type=SWITCH, driver=bmv2:org.onosproject.pipelines.fabric
id=device:bmv2:205, available=true, role=MASTER, type=SWITCH, driver=bmv2:org.onosproject.pipelines.fabric
id=device:bmv2:226, available=true, role=MASTER, type=SWITCH, driver=bmv2:org.onosproject.pipelines.fabric
id=device:bmv2:227, available=true, role=MASTER, type=SWITCH, driver=bmv2:org.onosproject.pipelines.fabric
onos> links
src=device:bmv2:204/1, dst=device:bmv2:226/1, type=DIRECT, state=ACTIVE, expected=false
src=device:bmv2:204/2, dst=device:bmv2:227/1, type=DIRECT, state=ACTIVE, expected=false
src=device:bmv2:205/1, dst=device:bmv2:226/2, type=DIRECT, state=ACTIVE, expected=false
src=device:bmv2:205/2, dst=device:bmv2:227/2, type=DIRECT, state=ACTIVE, expected=false
src=device:bmv2:226/1, dst=device:bmv2:204/1, type=DIRECT, state=ACTIVE, expected=false
src=device:bmv2:226/2, dst=device:bmv2:205/1, type=DIRECT, state=ACTIVE, expected=false
src=device:bmv2:227/1, dst=device:bmv2:204/2, type=DIRECT, state=ACTIVE, expected=false
src=device:bmv2:227/2, dst=device:bmv2:205/2, type=DIRECT, state=ACTIVE, expected=false
```

**You should see exactly 4 devices, and 8 links,** each one representing a direction of the 4 bidirectional links of our 2x2 fabric.

Now you should be able to ping the hosts from the Mininet shell (**T3**):

```
mininet> h1 ping h2
PING 10.0.2.2 (10.0.2.2) 56(84) bytes of data.
64 bytes from 10.0.2.2: icmp_seq=1 ttl=63 time=2.90 ms
64 bytes from 10.0.2.2: icmp_seq=2 ttl=63 time=1.86 ms
...
```

`h1` and `h2` are connnected to the same leaf and they belong to the same subnet. For this reason, their packets are bridged. Let's now try to ping hosts on different leaves, to see how packets are routed across the spines. For example, let's ping `h3` from `h1`:

```
mininet> h1 ping h3
```

The **ping should NOT work**, and the reason is that ONOS doesn't know the location of `h3`, and as such it has not installed the necessary rules to forward packets. In a more complicated Trellis setup where the DHCP Relay app is in use, ONOS can learn host information when the host is requesting an IP address using DHCP. However, in our topology IP address are assigned statically, hence ONOS only learns host information from ARP requests/replies. Indeed, while ONOS just learned the location of `h1` and `h2` because of the ARP packets exchanged between these two, `h3` is on a different subnet, hence no ARP exchange happens between `h1` and `h3`.

You can use the ONOS CLI to check which hosts have been discovered so far. In this case, you should see only 2 hosts, h1 and h2:

```
onos> hosts
id=00:AA:00:00:00:01/None, mac=00:AA:00:00:00:01, locations=[device:s204/3], vlan=None, ip(s)=[10.0.2.1], innerVlan=None, outerTPID=unknown, provider=of:org.onosproject.provider.host, configured=false
id=00:AA:00:00:00:02/10,   mac=00:AA:00:00:00:02, locations=[device:s204/4], vlan=10,   ip(s)=[10.0.2.2], innerVlan=None, outerTPID=unknown, provider=of:org.onosproject.provider.host, configured=false
```

To have ONOS discover the hosts, we can generate ARP packets by pinging the fabric interface gateway IP address from each host. For example, let's start a ping from `h3`:

```
mininet> h3 ping 10.0.3.254
PING 10.0.3.254 (10.0.3.254) 56(84) bytes of data.
64 bytes from 10.0.3.254: icmp_seq=1 ttl=64 time=73.0 ms
64 bytes from 10.0.3.254: icmp_seq=2 ttl=64 time=18.4 ms
64 bytes from 10.0.3.254: icmp_seq=3 ttl=64 time=17.7 ms
...
```

10.0.3.254 is the IP address associated with the leaf switch interface attached to `h3`. ICMP Echo Request packets are sent to ONOS as packet-ins, which in turn sends ICMP Echo Replies as packet-out. This is equivalent to pinging the interface of a traditional router but now handled in an SDN way.

In the ONOS log, you should see messages showing that the location of `h3` has been discovered. Let's try again pinging from `h1`:

```
mininet> h1 ping h3
PING 10.0.3.1 (10.0.3.1) 56(84) bytes of data.
64 bytes from 10.0.3.1: icmp_seq=1 ttl=62 time=8.87 ms
64 bytes from 10.0.3.1: icmp_seq=2 ttl=62 time=8.60 ms
64 bytes from 10.0.3.1: icmp_seq=3 ttl=62 time=8.45 ms
...
```

To be able to ping h4, make sure to have it discovered first using the same steps fro h3.

## Congratulations!

You have completed all the steps of this example.
