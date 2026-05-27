# SNMP

## Table of Contents

## Contributors

| Name | Organization | Role | Email |
| --- | --- | --- | --- |
| Andrea Campanella | On.Lab | Developer | [andrea@onlab.us](mailto:andrea@onlab.us) |

## Overview

This section provides an overview on the SNMP southbound protocol implementation in ONOS that is used to obtain information and configure devices through interaction with the SNMP protocol that they expose.

![](https://docs.google.com/drawings/d/1IPyXGJWPdpiZ_lUrFVHE7aCAQU-6B33crnmKC9iC4xw/pub?w=1440&h=1080)

## Interfaces and Classes

* **SnmpController.java**, implemented by **DefaultSnmpControllerImpl**.java**:** tracks all the SNMP devices in this instance of ONOS, serves as a one stop for connecting and obtaining a device and it's session.
* ****Snmp**Device**.java**** implemented by **DefaultSnmpDevice.java:**represents a SNMP capable device known to the ONOS core with all the information needed such as Ip, host, username, community, deviceId.
* ****SnmpDevice**Provider**.java**:**manages any SNMP device role and all the interactions with the ONOS core, such as provisioning the ports and the initial device setup. Has his own internalConfigListener from which it gets notified when a configuration is pushed to ONOS via restAPI. When a configuration is pushed and it's relevant to the Snmp device provider, this automatically triggers the connection with the specified devices. The device is added to ONOS if replies on the ip and port that the configuration provides.

## Notify ONOS of your SNMP device

This section specifies how to notify the ONOS core of a device that support REST operations for configuration.

Once you have your device Running on some IP address and some port, in order to make ONOS see it you should follow these steps.

* start ONOS
* activate the SNMP southbound app :

  ```
  onos> app activate org.onosproject.snmp
  ```
* activate the SNMP drivers for your device (i.e. lumentum drivers) :

  ```
  onos> app activate org.onosproject.drivers.lumentum
  ```

  Pay attention: if your drivers already depend upon the snmp app only the second step is needed.
* give ONOS the information regarding the device and which driver to use for your device in a json file. You need to specify username, password, ip and port. If you wrote a specific driver that has also to be changed form the standard "rest" one.

  ```
  {
    "devices": {
      "snmp:<ip>:<port>": {
        "snmp": {
          "ip": <ip>,
          "port": <port>,
          "username": <username>,
          "password": <password>
        },
        "basic": {
          "driver": <driver-name>
        }
      }
    }
  }
  ```

  You can also add other information, more than the driver, to the basic device configuration information: "type": "<device-type>", "manufacturer": "<device-manufacturer>","hwVersion": "<hw-version>","swVersion": "<sw-version>".
* upload the configuration you just wrote to the instance of ONOS you are running, in our case localhost:

  ```
  <your_machine>~$ curl -X POST -H "content-type:application/json" http://localhost:8181/onos/v1/network/configuration -d @<path_to_your_json_configuration_file> --user onos:rocks
  ```

  or

  ```
  <your_machine>~$ onos-netcfg localhost <path_to_your_json_configuration_file>
  ```
* Check if the device is present in ONOS:

  ```
  onos> devices
  ```

  should return, among other devices also something like:

  ```
  onos> id=snmp:127.0.0.1:1, available=true, role=MASTER, type=SWITCH, mfr=unknown, hw=unknown, sw=unknown, serial=unknown, ipaddress=127.0.0.1, driver=lumentum, name=rest:127.0.0.1:1
  ```

  If the device is not present the could have been one or multiple errors and you have to check the logs.

  + for localhost logs

    ```
    <your_machine>~$ tl
    ```

    or for remote logs

    ```
    <your_machine>~$ ol
    ```
  + verify that the logs don't contain SNMP related exceptions. In case error are present in the logs it could mean that the device was not able to reply on the given IP and Port. Verify Ip and Port in the Json file you posted and retry. If any other exception is present, such as no device name, please read the log and react to it accordingly.
* If your driver specifies a PortDiscovery implementation, such as **LumentumRoadmDeviceDescription.java** the Snmp southbound provider also queries the description you provide and the ports that are available on that device and updates the information in the ONOS core.

  So if your run in ONOS the command:

  ```
  onos> ports
  ```

  should return, among other devices also something like:

  ```
  onos> id=snmp:127.0.0.1:1, available=true, role=MASTER, type=SWITCH, mfr=unknown, hw=unknown, sw=unknown, serial=unknown, ipaddress=127.0.0.1, driver=lumentum, name=snmp:127.0.0.1:1
    port=4, state=enabled, type=och, signalType=ODU4, isTunable=yes , name=1.1
    port=5, state=enabled, type=och, signalType=ODU4, isTunable=yes , name=1.2
    port=20, state=enabled, type=oduclt, signalType=CLT_100GBE , name=5
    port=24, state=enabled, type=oduclt, signalType=CLT_100GBE , name=6
    port=28, state=enabled, type=oduclt, signalType=CLT_100GBE , name=7
    port=32, state=enabled, type=oduclt, signalType=CLT_100GBE , name=8
    port=48, state=enabled, type=och, signalType=ODU4, isTunable=yes , name=12.1
    port=49, state=enabled, type=och, signalType=ODU4, isTunable=yes , name=12.2
  ```
* Once the device is present in ONOS you can interact with it via the driver/provider subsystem.
