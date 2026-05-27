# SDX-L3 application

This page describes the Software Defined Internet Exchange Point - Layer 3 application (SDX-L3 or *sdx-l3* in ONOS nomenclature). SDX-L3 is an application that extends the existing SDN-IP application of ONOS in order to support software defined Internet Exchange Points (IXP), i.e. an infrastructure where various participating Service Providers (SP) can exchange traffic between their Autonomous Systems (AS).

This description makes use of the SDN-IP application principles and terminology, thus the reader is advised to read the [SDN-IP Architecture](../../apps-and-use-cases/sdn-ip/sdn-ip-architecture.md) and [SDN-IP User Guide](../../apps-and-use-cases/sdn-ip/sdn-ip-user-guide.md) before proceeding to the rest of SDX-L3 application description.

# Description

Although SDN-IP application can be used for the interconnection of different IP networks and for the control of a transit AS, there are some factors that prevent the SDN-IP network from being characterized as an SDX network. The main reasons for that are the following:

* In a typical IXP scenario, the border routers, i.e. BGP peers, of the interconnected ASs have interfaces in the same sub-net, i.e. the sub-net of the IXP. This is not currently supported by SDN-IP since the BGP peers should belong in different networks. Thus, in SDN-IP no explicit association between BGP peers and interfaces of the SDN-IP network is necessary. ONOS is able to find the interface towards a BGP peer automatically by matching the sub-net configured on the interfaces with the BGP peer IP address.
* IXP are typically combined with route servers, which allow the direct, i.e., one hop, connection between peering SPs. This means that the traffic originating from SP1 towards SP2 can be forwarded directly from SP1's border router towards the SP2's border router without the intermediate hop to an internal router of IXP. This is not currently supported by SDN-IP since all traffic between peering ASs should pass through an internal router of the SDN-IP network.

Currently the SDX-L3 application offers the above features. First, with the association of peers with interfaces, which allows BGP peers belonging in the same sub-net and lets the user to explicitly assign the connection point for each BGP peer. Second, by allowing direct traffic between SPs through the SDX-L3 network without the need for the hop towards an internal BGP router. Of course, in order to achieve this type of direct communication, the BGP peers for both the SPs should belong to the same sub-net.

# Application setup

SDX-L3 is implemented as the ONOS's *sdx-l3* or *org.onosproject.sdx-l3* application. SDX-L3 integrates the SDX-related features to the existing SDN-IP functionality thus the *sdnip* application should be deactivated in order to activate *sdx-l3*. Additionally, since SDX-L3 implements a different proxy-ARP handling than the one implemented in the proxy-ARP application, *proxyarp* should be deactivated as well.

```
onos> app deactivate org.onosproject.sdnip org.onosproject.proxyarp
```

```
onos> app activate org.onosproject.sdx-l3
```

SDX-L3 configuration should be placed in the *network-cfg.json* file in the config directory and it will be read in automatically at startup as in the SDN-IP case. The application uses a configuration identical to SDN-IP (using as subject the *"org.onosproject.router"* application) along with additional configuration details that are specific for SDX-L3 and are optional. The new subject is the *"org.onosproject.sdx-l3"* application and the configuration details are explained below in this page.

# Routing policies

In a typical case, routing policies can be applied in the IXP. SDX-L3 system makes use of the same architecture used in SDN-IP, thus iBGP implementation is integrated in ONOS which is used for the communication with the internal BGP speakers. Since, the ONOS BGP implementation is passive, the routing data are set by the internal BGP speaker and they are then communicated to ONOS.

In conclusion, SDX-L3 application is not responsible for setting routing policies in the SDX-L3 network. Instead the routing policies are set on the SDX-L3 internal BGP speakers and the speakers are responsible to communicate them to ONOS through iBGP.

# SDX-L3 features

## Association of peers with interfaces

### Description

There is the case that multiple peers belong to the same AS and are connected through different connection points to the SDX-L3 network controlled by ONOS. In this case, the user should be able to explicitly define the connection points to each peer. This is necessary since the identification of the appropriate interface by the application itself is not enough. Overlapping or identical sub-nets may exist in the *"ports"* section of the network configuration and thus the identification of which connection point should be used for a given peer is not straightforward.

This association is supported by the *sdx-l3* application and is introduced either by appropriate configuration in *network-cfg.json* file or by the command line handlers provided by the *sdx-l3* application during ONOS run-time. Apart from the associated connection point and interface, the user is able to assign an optional name to each BGP peer.

### Specifications

The specifications applying to the above feature are the following:

* Different peering sessions can be maintained for the same AS.
* Interfaces towards overlapping and/or identical sub-nets can be defined in the *"ports"* -> *"interfaces"* section of network configuration. These interfaces can be used for BGP peering sessions and, in order be be referenced to, their *"connectPoint"*, i.e., the corresponding device port, and *"name"* must be specified.
* Optionally, a *"name"*attribute can be assigned to a configured BGP peer.
* In case that a given BGP peer's IP address matches with two or more interfaces, it is recommended that the user should explicitly specify the interface that applies else the system randomly chooses one of them.
* Backwards compatibility is kept with existing configuration structure.
* Backwards compatibility is kept with existing configuration commands.
* New configuration is supported by *peer-add-details and peer-remove-details*command during ONOS run-time.
* The user is able to monitor such BGP peers configurations with appropriate printout command. A new command named *bgp-peers* is introduced for this purpose.
* The service for the connectivity between internal BGP speakers and BGP peers considers the configured association when creating the relevant p-t-p intents.
* The SDX-L3 application FIB component considers the configured association when creating the relevant m-t-p intents.

### Configuration

An example of a network configuration supported by the proposed feature is the following: [network-cfg.json](../../../assets/proposal-network-cfg-2.json)

This configuration is based on the one described in the [SDN-IP tutorial](../../apps-and-use-cases/sdn-ip/sdn-ip-tutorial.md). New peers with IP addresses 10.0.1.2 and 10.0.1.129 have been added in the topology, all of them belonging to the same sub-net 10.0.1.0/24 (AS1). Peer 10.0.1.2 is connected through a different connection point than the others to the SDX. Peer 10.0.1.129 is connected through the same connection point as 10.0.1.1 but uses vlan-id 100.

The following part describes the structure of the new attribute proposed for the association between peers and interfaces. It takes as prerequisite that a *"name"* has been added to  *"ports"* -> *"interfaces"* in order for the interfaces to be referenced to.The *"name"*  for "*bgpPeers"* is optional.

```
"apps" : {
```

```
"org.onosproject.sdx-l3": {  
  "participants": {  
    "bgpPeers": [  
      {  
        "name": "AS1-Router1",  
        "ip": "10.0.1.1",  
        "connectPoint": "of:00000000000000a1/1",  
        "intfName": "AS1-conn1"  
  }]}}}
```

### CLI commands

The configuration can be added during run-time with the appropriate CLI commands.

#### Addition of peer-specific details

```
peer-add-details
```

This command adds the details of an external BGP peer, i.e. BGP peer name (optionally), BGP peer IP, connect point of the BGP peer, name of configured interface for the BGP peer.

An example of the command that corresponds to the above scenario is the following:

```
peer-add-details -n=AS1-Router1 10.0.1.1 of:00000000000000a1/1 AS1-conn1
```

After the successful execution of the above command, a new association of specified peer with the named interface on specified port is introduced and activated.

#### Removal of peer-specific details

```
peer-remove-details
```

This command removes the details previously specified for an external BGP peer. Only the IP address of the peer should be given as a command argument.

An example of the command that corresponds to the above scenario is the following:

```
peer-remove-details 10.0.1.1
```

After the execution of the above command, a previous defined association of the specified peer with a configured interface no longer exists.

#### List of peer-specific information

```
bgp-peers
```

This command lists all the BGP peers specified in the system. Depending on whether details have been specified for a given peer or not, it behaves as follows:

* If no details have been previously specified for a given peer, only the peer IP address is listed.
* If details have been previously added, all the specified details will be listed by the command for this peer.

## SDX-L3 and route server

### Description

The association of peers with interfaces allows the SDX-L3 network to support route server functionality. In a typical scenario for SDX-L3 all the BGP routers of SPs as well as the internal BGP speaker(s) belong to the same sub-net. However, contrary to the legacy SDN-IP functionality, when the internal BGP speaker(s) is configured as route server it provides the necessary transparency so that peering SPs still appear to be directly connected through the SDX. Therefore, during route propagation between SPs the mediation of the route server is invisible outside of the SDX.

The association of peers with interfaces allows the support of route server functionality since the peer connectivity and the FIB component consider the peer-to-interface mapping when creating the relevant p-t-p and m-t-p intents, respectively. However, ARP requests for direct traffic between the SPs' routers are not handled by legacy functionality.

### Specifications

The specifications applying to the above feature are the following:

* Internal BGP speakers should support route server functionality (this is not related with ONOS itself).
* The feature for the association of peers with interfaces should be supported.
* Proxy-ARP functionality handles (and not reject) ARP requests between configured border routers of SPs, i.e. external BGP peers.
* Since *sdx-l3* implements its own proxy-ARP handling, when activating *sdx-l3* application, the ONOS *proxyarp* application should be deactivated.

### Configuration

An example of a network configuration for ONOS operating along with a route server is the following: [network-cfg.json](../../../assets/route-server_network-cfg-1.json)

This configuration defines two external peers, namely *"AS65001-R1*" and *"AS65002-R2"*, that belong to the same sub-net 10.0.0.3/24 as the internal BGP speaker. The relevant python creating the mininet topology is the following: [route-server-conf.py](../../../assets/rs-conf.py).The necessary quagga files for "AS65001-R1", "AS65002-R2" and the internal route server are: [quagga1.conf](../../../assets/quagga1.conf), [quagga2.conf](../../../assets/quagga2.conf), and [quagga-sdn.conf](../../../assets/quagga-sdn.conf), respectively.

# Code

Currently the code for *sdx-l3*application can be found in the ONOS sample application repository: <https://gerrit.onosproject.org/onos-app-samples>.

More information about getting and contributing to this repository can be found in ONOS wiki page about [Sample Application Development](#).
