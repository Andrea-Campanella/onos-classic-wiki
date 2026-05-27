# Virtual BNG

The virtual Broadband Network Gateway (vBNG) is a ONOS application for hosts with private IP addresses to access the Internet.

It mainly includes 3 functions:

(1) assigns and replies a public IP address to a REST request with a private IP address.

(2) maintains the mapping from the private IP address to the public IP address.

(3) installs point to point intents for the host configured with private IP address to access Internet.

# Configuration

## vBNG Configuration

To run the vBNG, a new configuration file is needed: onos/tools/package/config/virtualbng.json. The content in this configuration file is:

```
{
    "localPublicIpPrefixes" : [
         "200.0.0.0/32",
         "201.0.0.0/30",
         "202.0.0.0/30"
    ],
    "nextHopIpAddress" : "200.0.0.5",
    "publicFacingMac" : "00:00:00:00:00:66",
    "xosIpAddress" : "10.254.1.22",
    "xosRestPort" : "8000",
    "hosts" : {
        "hostname.onlab.us" : "of:0000000000000001/1"
    }
}
```

The “localPublicIpPrefixes” means the public IP address for vBNG to assign.

The “nextHopIpAddress” means the next hop gateway IP address. The gateway here is the upstream gateway provided by our ISP for us to access the Internet.

The “publicFacingMac” is a MAC address used for ONOS to compose ARP replies to the ARP requests from the upsteam gateway. Before the upstream gateway sends traffic packets to our local public IP addresses, it will send out ARP requests first to get the MAC address of each public IP address. Actually, there are no hosts configured with those public IP addresses in local SDN network, so vBNG will emulate the behavior of the non-existent hosts and return ARP replies with this MAC address. Since we will rewrite the destination MAC address in the switch before traffic packets go to the destination, so the MAC address can be any number. We manually configured a random MAC address for this purpose.

The "xosIpAddress" is the IP address of XOS. The "xosRestPort" is the port of XOS for vBNG to fetch the mapping record. This function is used for vBGN's reboot, we should recovery the vBNG status from the XOS' record.

The "hosts" dictionary contains a map of compute node hostnames to connect point on the vBNG-managed switch.

## Proxy ARP Configuration

When we configure each host with an IP address (the IP address is private IP address), we also configure the gateway IP address on each host. Then the host will send out ARP packets to look for the MAC address of the gateway. Since there is no physical gateway, we will use proxy ARP application to handle those ARP requests.

This configuration (onos/tools/package/config/addresses.json) shown in the table is used for proxy ARP application to reply the ARP requests. The IP addresses “192.0.0.1” and “200.0.0.1” are gateway addresses for subnets“192.0.0.0/24” and “200.0.0.0/24”.

This configuration is also used for proxy ARP application to send out probe packets to check whether a host is present or not. For more detailed introduction of this configuration file, you can refer to this web page: [https://wiki.onosproject.org/display/ONOS/SDN-IP+User+Guide](../../sdn-ip/sdn-ip-user-guide.md).

```
{
    "addresses" : [
                {
                    "dpid" : "00:00:00:00:00:00:00:a1",
                    "port" : "2",
                    "ips" : ["192.0.0.1/24"],
                    "mac" : "00:00:00:00:00:99"
                        
                },
                {
                    "dpid" : "00:00:00:00:00:00:00:a5",
                    "port" : "4",
                    "ips" : ["200.0.0.5/24"],
                    "mac" : "00:00:00:00:00:98"
                }
    ]
}
```

For example, there can be a local host connected to OpenFlow switch “00:00:00:00:00:00:00:a1” and port 2. The switch port is configured with 1 private IP prefix “192.0.0.1/24” and 192.0.0.1 is the gateway IP address. The host can be configured with IP addresses in the subnet of 192.0.0.0/24. The next hop (upstream gateway from ISP) can be connected to switch "00:00:00:00:00:00:00:a5" and port 4. Its address should belong to the subnet of 200.0.0.0/24.

# REST API

| Type | URL | Return |
| --- | --- | --- |
| POST | http://{onosip}:8181/onos/virtualbng/privateip/{privateip}/{mac}/{hostname} | return a public IP string if success, for example "200.0.0.1", otherwise return "0" |
| DELETE | http://{onosip}:8181/onos/virtualbng/privateip/{privateip} | return the public IP address assigned for the private IP address if there is a vBNG for this private IP address and if we delete this vBNG, otherwise return "0" |
| GET | http://{onosip}:8181/onos/virtualbng/privateip/map | return all the mapping entries from private IP address to public IP address in JSON format |

There are some corner cases:

For the POST method, if the public IP address pool is used up, in this case, "0" will be returned. If there is already a vBNG for the requested private IP address, the public IP address already assigned will be returned, and no new vBNG will be created.

For the DELETE method, if there is no vBNG in the system for the requested private IP address, "0" will be returned.

# Application Dependencies

As the description above, to run vBNG, we need to run three applications in total: onos-app-proxyarp, onos-app-virtualbng.

One of the choices to activate them is in the following way:

```
onos> app activate org.onosproject.proxyarp
onos> app activate org.onosproject.virtualbng
```

# CLI Command

```
onos> vbngs
   Private IP - Public IP
   100.0.0.2 - 200.0.0.5
   100.0.0.3 - 202.0.0.1
```

The “vbngs” in ONOS CLI can show all the mapping entries from private IP address to public IP address.

# vBNG Start/Restart

vBNG starts and restarts based on XOS's private IP to public IP mapping record.

After vBNG is started, the first thing vBNG to do is to GET the XOS record based a REST API provided by XOS:

```
http://{xosServerIpAddress}:{xosServerPort}/xoslib/rs/vbng_mapping/
```

Then vBNG will recover its status from the XOS record:

(1) re-set up the mapping from the private IP address to public IP address according to the record;

(2) maintain this mapping;

(3) re-calculate the intents and install them to setup forwarding paths.

Then, it starts to work as normal.

So make sure XOS is running before starting vBNG and make sure the REST API of XOS to get the map record works.
