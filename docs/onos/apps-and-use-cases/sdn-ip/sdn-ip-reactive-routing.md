# SDN-IP Reactive Routing

When ONOS receives an IPv4 or IPv6 packet-in, it will reactively compute and install the routing path for the traffic. We call this function reactive routing. In ONOS we implemented a reactive routing application (name:  "onos-app-reactive-routing") .

The reactive routing application can handle three cases: 2, 3, and 4, while case 1 is controlled by SDN-IP application.

1. transit traffic (traffic from one BGP peer outside local SDN network traverses local SDN network and goes to another BGP peer) are proactively installed by SDN-IP application. You can find the description here[SDN-IP](../sdn-ip.md).
2. one host wants to talk to another host, both two hosts are in SDN network.
3. one host in SDN network wants to talk to another host in Internet.
4. one host from Internet wants to talk to another host in SDN network.

Note: “onos-app-reactive-routing” depends on “onos-app-sdnip”, so if you want to use the reactive routing function, you need to activate “onos-app-sdnip” first, and then active “onos-app-reactive-routing”.

## Virtual Gateway

In legacy IP network, hosts use gateway as the default router to access the Internet. However, an SDN network uses SDN switches to connect a network rather than routers, so there is no physical gateway router in the SDN network. Without a gateway, there is an issue for hosts inside SDN network. When hosts want to communicate with other hosts in different subnetworks, they do not know the next hop where the packets should be sent. Also hosts do not know the MAC address of the next hop and can not compose the entire packet and send it out. To solve this issue, we designed a virtual gateway for SDN network.

After a host gets its gateway address, it will send out ARP packet to look for the MAC address. Since there is no physical gateway in SDN, the virtual gateway module in ONOS will take care all the ARP requests. In detail, virtual gateway module registers from ONOS for all the ARP packet-ins. It will check whether the target address in the ARP request packet is the virtual gateway address. If so, virtual gateway module will composes the ARP reply packet and send it out as packet-out to the host. Currently, we configure each gateway address together with each IP prefix in the configuration file. 

## Configuration

### **BGP Speaker Configuration**

In order to announce the public prefixes to other networks, we should also configure the BGP speaker in local SDN network with all the public prefixes.

### ******ONOS **Configuration********

Usually a network is assigned with several public IP prefixes. Besides those public IP prefixes, the network administrator may also want to use some private IP prefixes locally. For all those IP prefixes, we configure them in configuration file “network-cfg.json” which is located at onos/tools/package/config/network-cfg.json.

******Scenario** 1:****

Even if you only want run reactive routing for local traffic, which means case 2 above. You still need to run SDN-IP APP. But in this case, you do not need to configure the BGP speaker as described in section "**BGP Speaker Configuration**" above.

one example of the configuration file is:

```
{
    "ports" : {
        "of:00000000000000a1/4" : {
            "interfaces" : [
                {
                    "ips"  : [ "201.0.0.254/24" ],
                    "mac"  : "00:00:00:00:00:01"
                }
            ]
        },
        "of:00000000000000a2/3" : {
            "interfaces" : [
                {
                    "ips"  : [ "202.0.0.254/24" ],
                    "mac"  : "00:00:00:00:00:01"
                }
            ]
        },
        "of:00000000000000a6/3" : {
            "interfaces" : [
                {
                    "ips"  : [ "206.0.0.200/24" ],
                    "mac"  : "00:00:00:00:00:01"
                }
            ]
        },
        "of:0000000000000a13/4" : {
            "interfaces" : [
                {
                    "ips"  : [ "213.0.0.200/24" ],
                    "mac"  : "00:00:00:00:00:01"
                }
            ]
        }
    },
    "apps" : {
       "org.onosproject.reactive.routing" : {
            "reactiveRouting" : {
                "ip4LocalPrefixes" : [
                    {
                        "ipPrefix" : "201.0.0.0/24",
                        "type" : "PUBLIC",
                        "gatewayIp" : "201.0.0.254"
                    },
                    {
                        "ipPrefix" : "202.0.0.0/24",
                        "type" : "PUBLIC",
                        "gatewayIp" : "202.0.0.254"
                    },
                    {
                        "ipPrefix" : "206.0.0.0/24",
                        "type" : "PRIVATE",
                        "gatewayIp" : "206.0.0.254"
                    },
                    {
                        "ipPrefix" : "213.0.0.0/24",
                        "type" : "PRIVATE",
                        "gatewayIp" : "213.0.0.254"
                    }
                ],
                "ip6LocalPrefixes" : [
                ],
                "virtualGatewayMacAddress" : "00:00:00:00:00:01"
            }
        }
    }
}
```

The type “PUBLIC” means this prefix will be announced by BGP speaker to the outside networks and is reachable from outside, while “PRIVATE” means this prefix will be used only locally, and is not reachable from outside.

We configure a static MAC address as the virtual gateway address. This MAC address can be any MAC address of the BGP speakers’ in the configuration. The “virtualGatewayMacAddress” in configuration file is the MAC address for the virtual gateway.

So each SDN network only needs one virtual gateway, and this virtual gateway only has one mac address and may have several gateway IP addresses.

**Scenario******2:****

If you want to make all the scenarios work, including 1. 2. 3. 4. Then you should config both SDN-IP APP and ReactiveRouting APP. One config example is:

```
{
    "ports" : {
        "of:00000000000000a8/5" : {
            "interfaces" : [
                {
                    "ips"  : [ "10.0.5.101/24" ],
                    "mac"  : "00:00:00:00:00:01"
                }
            ]
        },
        "of:0000000000000a32/4" : {
            "interfaces" : [
                {
                    "ips"  : [ "10.0.4.101/24" ],
                    "mac"  : "00:00:00:00:00:01"
                }
            ]
        },
        "of:0000000000000a28/3" : {
            "interfaces" : [
                {
                    "ips"  : [ "10.0.6.101/24" ],
                    "mac"  : "00:00:00:00:00:01"
                }
            ]
        },
        "of:00000000000000a1/4" : {
            "interfaces" : [
                {
                    "ips"  : [ "201.0.0.200/24" ],
                    "mac"  : "00:00:00:00:00:01"
                }
            ]
        },
        "of:00000000000000a2/3" : {
            "interfaces" : [
                {
                    "ips"  : [ "202.0.0.200/24" ],
                    "mac"  : "00:00:00:00:00:01"
                }
            ]
        },
        "of:00000000000000a6/3" : {
            "interfaces" : [
                {
                    "ips"  : [ "206.0.0.200/24" ],
                    "mac"  : "00:00:00:00:00:01"
                }
            ]
        },
        "of:0000000000000a13/4" : {
            "interfaces" : [
                {
                    "ips"  : [ "213.0.0.200/24" ],
                    "mac"  : "00:00:00:00:00:01"
                }
            ]
        }
    },
    "apps" : {
        "org.onosproject.router" : {
            "bgp" : {
                "bgpSpeakers" : [
                    {
                        "connectPoint" : "of:0000000000000a24/1",
                        "peers" : [
                            "10.0.4.1",
                            "10.0.5.1",
                            "10.0.6.1"
                        ]
                    }
                ]
            }
        },
       "org.onosproject.reactive.routing" : {
            "reactiveRouting" : {
                "ip4LocalPrefixes" : [
                    {
                        "ipPrefix" : "201.0.0.0/24",
                        "type" : "PUBLIC",
                        "gatewayIp" : "201.0.0.254"
                    },
                    {
                        "ipPrefix" : "202.0.0.0/24",
                        "type" : "PUBLIC",
                        "gatewayIp" : "202.0.0.254"
                    },
                    {
                        "ipPrefix" : "206.0.0.0/24",
                        "type" : "PRIVATE",
                        "gatewayIp" : "206.0.0.254"
                    },
                    {
                        "ipPrefix" : "213.0.0.0/24",
                        "type" : "PRIVATE",
                        "gatewayIp" : "213.0.0.254"
                    }
                ],
                "ip6LocalPrefixes" : [
                ],
                "virtualGatewayMacAddress" : "00:00:00:00:00:01"
            }
        }
    }
}
```

Since  "201.0.0.0/24" and  "202.0.0.0/24" are public IP prefixes, you should also config them inside BGP speakers inside SDN network.

## Unknown Traffic Treatment

For a destination IP address, if there is no matchable IP prefix either in sdnip.json or in BGP speaker's route table, we will install rules to drop such packets at the first hop switch where the packets come from.
