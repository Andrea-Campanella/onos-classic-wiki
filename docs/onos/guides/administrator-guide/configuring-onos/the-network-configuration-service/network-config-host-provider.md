# Network Config Host Provider

# Introduction

Network Config Host Provider is a host provider that learns host information from network config subsystem rather than packet-in.  
There are two main benefit that Network Config Host Provider can offer:

1. Block unexpected hosts  
   In some use cases such as CORD, the network orchestrator (XOS) knows all hosts that suppose to be in the system. We can easily avoid interference from unexpected hosts by explicitly specify which hosts we want to allow in network config.
2. Debugging  
   We can easily mock up and inject a host through network config.

Network config subsystem already provides Java API and REST API. Which makes Network Config Host Provider very easy to use.

# How to Use

## Enable Network Config Host Provider

The **openflow**meta application contains **openflow-base**, **hostprovider** and **lldpprovider**.  
You can set the following into ONOS\_APPS environment variable to replace **hostprovider** with **netcfghostprovider.**

```
export ONOS_APPS=drivers,openflow-base,netcfghostprovider,lldpprovider
```

Alternatively, since Network Config Host Provider is an application, it can also be enabled/disabled dynamically through ONOS CLI

```
app deactivate org.onosproject.openflow
app activate org.onosproject.openflow-base org.onosproject.netcfghostprovider org.onosproject.lldpprovider
```

## Provide Host Information in Network Config

You can upload **hosts** network config by POSTing a JSON file to:

```
http://<ip>:8181/onos/v1/network/configuration/hosts
```

Here is an JSON example:

```
{
  "00:02:c9:1e:b1:20/None": {
    "basic": {
      "ips": ["10.0.1.1", "10.0.1.2"],
      "locations": ["of:0000000000000001/5"]
    }
  },
  "00:02:c9:1e:b1:21/None": {
    "basic": {
      "ips": [],
      "locations": ["of:0000000000000001/13"]
    }
  }
}
```
