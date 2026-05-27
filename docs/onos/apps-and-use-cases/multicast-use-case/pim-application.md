# PIM Application

The PIM application in ONOS provides a minimal implementation of the PIM-SSM protocol.

It supports forming neighbor relationships with other PIM routers, receiving PIM Join/Prune messages and inserting the information into the ONOS multicast route store, and sending PIM Join/Prune messages to upstream routers.

# Usage

## Configuration

The PIM application requires some configuration to enable PIM processing on interfaces. Configuration is required for each interface that will be running PIM.

Please see the [The Network Configuration Service](../../guides/administrator-guide/configuring-onos/the-network-configuration-service.md) wiki page for information on how to manage network configuration in ONOS.

The following is an example PIM configuration:

```
{
    "ports" : {
        "of:0000000000000002/9" : {
            "interfaces" : [
                {
                    "name" : "sw2-9",
                    "ips"  : [ "10.0.1.2/24" ],
                    "mac"  : "90:e2:ba:82:f9:76"
                }
            ],
            "pimInterface" : {
                "interfaceName" : "sw2-9",
                "enabled" : true,
                "helloInterval" : 1,
                "holdTime" : 3,
                "propagationDelay" : 500,
                "overrideInterval" : 2500
            }
        }
    }
}
```

There are two parts to the configuration: **interfaces** and ***pimInterfaces***. Both parts are necessary to enable PIM on an interface.

The **interfaces** section describes IP and MAC address information that is logically assigned to a switch port in the SDN network. The PIM application will make use of this information when sending and receiving messages from this interface. Each interfaces has a 'name' section, which should contain an arbitrary string which can be used to refer to that interface.

The **pimInterfaces** section enables PIM on the interface and configures PIM parameters. It contains a mandatory **interfaceName** field which refers to an interface configuration. The **enabled** flag must be set to true to enable PIM processing on this interface. The remaining fields are optional, and are used to configure the parameters of the interface. If they are omitted, default values are used as defined in RFC 4601.

## Usage

The PIM application can be activated with the following command:

```
onos> app activate org.onosproject.pim
```

The following CLI commands can be used to inspect the state of the running PIM application:

```
onos> pim-interfaces
onos> pim-neighbors
```

## Unicast route information

TBD
