# Network Config Link Provider

# 

# Introduction

In a datacenter environment, network administrators may want to lock down the topology of their network and not allow traffic to flow over links that they are not expecting. Also, cabling errors are common, and can lead to a topology being configured that was not intended. The network config link provider allows specifying the link topology via the netcfg mechanism, and disallows any links that are not in the defined configuration.

# How to Use

## Enable Network Config Link Provider

The **openflow**meta application contains **openflow-base**, **hostprovider** and **lldpprovider**.  
You can set the following into ONOS\_APPS environment variable to replace **lldpprovider** with **netcfglinksprovider.**

```
export ONOS_APPS=drivers,openflow-base,hostprovider,netcfglinksprovider
```

Alternatively, since Network Config Link Provider is an application, it can also be enabled/disabled dynamically through ONOS CLI

```
app deactivate org.onosproject.openflow
app activate org.onosproject.openflow-base org.onosproject.hostprovider org.onosproject.netcfglinksprovider
```

## Provide Link Information in Network Config

You can upload **hosts** network config by POSTing a JSON file to:

```
http://<ip>:8181/onos/v1/network/configuration/ 
```

Here is an example of a configuration that defines a set of links in a topology:

**Sample Config**

```
{
    "links" : {
        "of:0000000000000001/1-of:0000000000000191/1" : {
            "basic" : {}
        },
        "of:0000000000000001/3-of:0000000000000192/1" : {
            "basic" : {}
        },
        "of:0000000000000002/1-of:0000000000000191/3" : {
            "basic" : {}
        },
        "of:0000000000000002/3-of:0000000000000192/3" : {
            "basic" : {}
        },
        "of:0000000000000191/1-of:0000000000000001/1" : {
            "basic" : {}
        },
        "of:0000000000000192/1-of:0000000000000001/3" : {
            "basic" : {}
        },
        "of:0000000000000191/3-of:0000000000000002/1" : {
            "basic" : {}
        },
        "of:0000000000000192/3-of:0000000000000002/3" : {
            "basic" : {}
        }
    },
    "apps" : {
        "org.onosproject.core" : {
            "core" : {
                "linkDiscoveryMode" : "STRICT"
            }    
        }
    }
}
```

In the links section of the config, each entry specifies a link that will be allowed in the topology. The format of the link name is devid1/port1-devid2/port2, and this defines the two end points of the link. Setting the link discovery mode to STRICT will prevent unconfigured links from being added to the topology.

# Method of Operation

On startup, the provider reads in the preconfigured links, adds them to the system, and sets their state to INACTIVE. LLDP packets are sent out to determine if the links are active. When an LLDP packet comes back to the controller, if the source and destination match a predefined link, the link is marked ACTIVE and is available for traffic. If the source and destination does not match, a link is created with an error indication, which allows the GUI to display an error indication to the user. These error links are not available for traffic. If the link configuration changes, the provider reads in the changes and adjusts the topology accordingly.
