# The Network Configuration Service

The Network Configuration Service provides support for two primary tasks:

* Configuring ONOS applications that provide network services (such as L3 or L2 connectivity, DHCP service, etc.)
* Adding information about devices, links, and device configuration into ONOS's network view

In legacy IP/Ethernet networks, network and connectivity configuration (for example configuring BGP, IP subnets, VLANs, or ACLs) usually requires configuring multiple individual devices. With ONOS, equivalent functionality is usually provided by ONOS *applications* – software packages for a particular task or use case – that usually provide services across multiple devices or the entire network. Some ONOS applications (such as reactive forwarding) either require no configuration or operate perfectly well with a default configuration. However, other applications may require additional specific configuration information that cannot be inferred automatically. These applications can be configured using the Network Configuration Service.

The Network Configuration Service provides configuration services to ONOS applications. ONOS applications such as [SDN-IP](../../../apps-and-use-cases/sdn-ip.md) or [VPLS](../../../apps-and-use-cases/virtual-private-lan-service-vpls/vpls-user-guide.md) accept their own application-specific configuration information from it. Information on application-specific configuration may be found in the individual application sections of [Apps and Use Cases](../../../apps-and-use-cases.md).

The Network Configuration Service also provides the ability to add information into ONOS's network view. This makes it possible to write a program that reads the device and topology inventory, as well as other information, from a site-specific database and then provides it directly to ONOS, without having to rely on dynamic device and topology discovery. Additionally it may be used to add supplemental information that ONOS does not or cannot discover automatically, but may require for correct operation.

Information on configuring *ONOS itself* (such as setting up an ONOS cluster, or activating applications), as well as using ONOS to configure *network devices*, can be found in appropriate sections of [Configuring ONOS](../configuring-onos.md).

## Overview

The network configuration service enables applications and operators to configure ONOS’ network view, and ONOS network applications, using a uniform syntax, currently JSON. Examples include:

* Device and device port types and names
* Device location, owner, hardware and software versions
* Whether components are allowed or denied inclusion in the network model

This service doesn’t limit configuration to the network elements that ONOS has knowledge of - configurations can also refer to yet-discovered elements, or those that cannot be discovered by conventional means.

## Syntax

A *subject key* describes the category of network element, e.g. links, devices, hosts, etc. Each network element is associated with a unique identifier (a *subject*) and one or more attributes, associated with some value, grouped into *configs*. The configs themselves are classified by *config keys*.

The JSON file used with the service then takes on the following format:

```
{
    subject key : {                   # element category, e.g. "devices", "links", etc.
        subject : {                   # unique string, e.g. a device ID
            config key 1 : {          # config class of config, e.g. "basic"
                attr1 : value1,       # attribute : value pairs associated with a config
                attr2 : value2,
                ...
            },
            ...
        },
          ...
    },
    ...
}
```

Sample configuration files may be found in *${ONOS\_ROOT}/tools/test/configs/* .

## Network Configurations for Southbound Providers.

Different southbound providers, namely NETCONF, SNMP, REST and TL1 use net-cfg as the mechanism to inject ip, port, username, password of a device.

You can find information about each of these protocols and json examples in their respecitive wiki pages.

* [NETCONF](southbound-protocols/netconf.md)
* [REST](southbound-protocols/rest.md)
* [SNMP](southbound-protocols/snmp.md)
* [TL1](southbound-protocols/tl1.md)

Sample configuration for these protocols are also stored in *${ONOS\_ROOT}/tools/test/configs/* .

## Loading Network Configurations

### REST API

The `NetworkConfigWebResource` implements the REST calls for the network configuration subsystem. Its functionalities will eventually replace that of `ConfigWebResource`.

The following example uses the REST API to upload a configuration file:

```
curl --user onos:rocks -X POST -H "Content-Type: application/json" http://192.168.56.111:8181/onos/v1/network/configuration/ -d @/tmp/cfg.json
```

The above assumes a running instance at 192.168.56.111, and a configuration file at */tmp/cfg.json*. These should be replaced with appropriate values.

Likewise, the user:password combination might differ with your setup; Other common values are karaf:karaf and onos:onos.

### onos-netcfg shell script

There is a shell script that wraps the REST API to provide a more convenient mechanism to upload configuration from the command line (i.e. from outside ONOS).

For example, the same configuration above can be uploaded using:

```
onos-netcfg 192.168.56.111 /tmp/cfg.json
```

The script also accepts a third argument that allows you to upload smaller chunks of config identified by subject\_key/subject/config\_key:

```
onos-netcfg $OC1 /tmp/basic.json /devices/of:0000000000000001/basic
```

Here the /tmp/basic.json script would just contain the payload of the *basic* config key, for example:

```
{
   "driver" : "softrouter"
}
```

### Network Configuration Loader

The `NetworkConfigLoader` reads JSON files from a known location and attempts to load them as network configurations at system startup.

Currently, a file named *network-cfg.json* is picked up from *${ONOS\_ROOT}/tools/package/config/* and placed in *${KARAF\_ROOT}../config/* at deployment. The filename and paths are currently fixed. When the remote instance boots, its network configuration loader runtime will read this file.

The Network Configuration Loader is implemented as a listener for Network Configuration events (`NetworkConfigEvent`s). It attempts to use the known `Config`s in order to generate or update entities in the network model once it is notified that the `Config`s are available.
