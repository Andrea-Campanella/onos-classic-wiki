# Interfaces configuration

The interface configuration is part of the network configuration. It allows users to configure information about ports and logical ports of devices connected to the system. The information is used by ONOS and its applications to decide how to select and forward the network traffic. The interface configuration is probably the most similar to the "legacy" network devices configuration. Examples of common patterns are "select traffic tagged with VLAN X on port Y", "Select all the traffic coming with IP A and send it out through port B".

The configuration contains a list of **physical ports**, and **logical interfaces**. A more detailed explanation is reported below.

# Basic definitions

* **Ports** represent physical ports of devices connected to ONOS. They act as containers of one or more interfaces that actually hold the real configuration
* **Interfaces** are logical entities, subset of physical ports, distinguished by different parameters, such as i.e. VLANs, IPs, MAC addresses. Each port can have multiple interfaces.

# Configuration structure

As the rest of the network configuration, also the interface configuration is expressed in JSON format. Below, you can find a the structure of a very generic interface configuration

**Generic configuration structure**

```
{
    "ports" : {
        "of:DPID__WITH_NO_COLUMNS/PORT" : {
            "interfaces" : [
                {
                    "KEY_1" : "VALUE_1",
				    "KEY_2" : [ "VALUE_2A", "VALUE_2B" ],
                    "KEY_3"  : "VALUE_3"
                }
            ]
        },
        "of:ANOTHER_DPID_WITH_NO_COLUMNS/PORT" : {
            "interfaces" : [
                {
                    "KEY_1" : "VALUE_1",
				    "KEY_2" : [ "VALUE_2A", "VALUE_2B" ],
                    "KEY_3"  : "VALUE_3"
                },
				{
                    "KEY_10" : "VALUE_10",
				    "KEY_4" : [ "VALUE_4A", "VALUE_4B" ],
                    "KEY_3"  : "VALUE_3"
                }
            ]
        }
}
```

# Configuration semantic and best-practices:

What's reported above is a sample configuration, used in SDN-IP.

Configuration you may find are usually very specific to the application that parses them.

While the configuration syntax and the general structure is globally enforced by the interface configuration subsystem itself, It's up to each ONOS application how to interpret the values provided. For example, some applications might request just one parameter per interface (it might be the case of some L2 applications with VLAN); some others might reques more (for example IPs for L3 applications). Also, applications might use the values as they like, so giving them any meaning.

Even if different applications might interpret the configuration in different ways, there's an agreement about how parameters should be read. Following is a list of "best-practices" we generally follow:

* **name**: It works as unique interface identifier. One string representing the name per interface. it's enforced to be unique in each port. It would be better to make it globally unique.
* **vlan:** The meaning should be "...select on this interface packets already tagged with the VLAN specified...". One string representing the VLAN Id per interface. It should be unique in each port.
* **ips**: The meaning should be "...select on this interface packets destined to the IP addresses specified...". One comma separated list of strings representing the IP addresses to match against per interface. IP addresses should be unique in each port.
* **mac:** Primarily used for ARP management. The meaning should be "...reply to ARP request with the MAC address specified...". One string representing the MAC address. It should be unique in each port.

# Example: Emulating a router behavior with a combination of IP addresses and MAC address

As an example, the ARP handler of SDN-IP uses the combination of IP addresses and MAC address to emulate routers behavior.

**SDN-IP interface configuration example**

```
{
    "ports" : {
        "of:0000000000000001/1" : {
            "interfaces" : [
                {
                    "name" : "Interface 1 sw 1",
				    "ips"  : [ "1.1.1.1/24", "10.10.10.1/24" ],
                    "mac"  : "00:00:00:00:00:01"
                }
            ]
        }
	}
}
```

The configuration above means "...ARP request packets coming in from DPID 00:00:00:00:00:00:00:01, port 1, having destination IPs 1.1.1.1/24 or 10.10.10.1/24, should be replied with ARP replies with MAC address 00:00:00:00:00:01..."

# Expressing parameters for an entire port (1:1 mapping between a port and an interface)

Sometimes you may want to express parameters related to an entire physical port, rather than an interface. Configurations attributes written directly under a physical port won't be parsed. Anyway, there's a work-around to it: just add one interface to the physical port it and specify inside its parameters.

# Specific configurations

Following is a list of known applications (including the link to their configuration guide) that use the interface configuration. If you like, you may look at their configuration guides and at their code, taking them as example.

* [SDN-IP](../../../../apps-and-use-cases/sdn-ip/sdn-ip-user-guide.md)
* [VPLS](../../../../apps-and-use-cases/virtual-private-lan-service-vpls/vpls-user-guide.md)
