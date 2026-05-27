# REST

## Table of Contents

## Contributors

| Name | Organization | Role | Email |
| --- | --- | --- | --- |
| Andrea Campanella | On.Lab | Developer | [andrea@opennetworking.org](mailto:andrea@opennetworking.org) |

## Overview

This section provides an overview on the REST southbound protocol implementation in ONOS that is used to obtain information and configure devices through interaction with the REST APIs that they expose.

![](https://docs.google.com/drawings/d/1n3xr_lYYGS2b2c7dbbwleRrlQeTbpEC54pnLH6NEgNI/pub?w=1440&h=1080)

## Interfaces and Classes

* **RestSBController.java**, implemented by **RestSB****ControllerImpl**.java**:** tracks all the NETCONF devices, serves as a one stop for connecting and obtaining a device and (un)register listeners on device events. It also exposes interface methods to do REST CRUD operations on a device identified by a DeviceId.
* ****RestSB**Device**.java**** implemented by **DefaultRestSBDevice.java:** represents a REST capable device known to the ONOS core with all the information needed such as Ip,port,name,password,protocol, deviceId.
* ****RestDevice**Provider**.java**:** manages any REST device role and all the interactions with the ONOS core, such as provisioning the ports and the initial device setup. Has his own internalConfigListener from which it gets notified when a configuration is pushed to ONOS via restAPI. The device is added to ONOS if replies on the ip and port that the configuration provides.

## Notify ONOS of your REST device

This section specifies how to notify the ONOS core of a device that support REST operations for configuration.

Once you have your device Running on some IP address and some port, in order to make ONOS see it you should follow these steps.

* start ONOS
* activate the REST southbound app :

  ```
  onos> app activate org.onosproject.restsb
  ```
* activate the REST drivers for your device (i.e. ciena drivers) :

  ```
  onos> app activate org.onosproject.drivers.ciena.waveserver
  ```
* give ONOS the information regarding the device and which driver to use for your device in a json file. You need to specify username, password, ip and port. If you wrote a specific driver that has also to be changed form the standard "rest" one.

  ```
  {
    "devices": {
      "rest:<ip>:<port>": {
        "rest": {
          "username":<username>,
          "password":<password>,
          "ip":<ip in string format>,
          "port":<port in integer formato> 
  		"protocol":<portocol, i.e. http>
  		"url":<url for the base get operation of the device, {optional}>
        },
        "basic": {
          "driver": <driver-name>
        }
      }
    }
  }
  ```

  A working example is in $ONOS\_ROOT/tools/test/configs/restSB-cfg.json. Change the IP both in the DeviceId at the top and in the devices array. This example expects that your are running a REST server locally (127.0.0.1) on port 8080.  
  You can also add other information, more than the driver, to the basic device configuration information: "type": "<device-type>", "manufacturer": "<device-manufacturer>","hwVersion": "<hw-version>","swVersion": "<sw-version>". If added, the url field will be used to contact the device and find it's reachability instead of ip:port. This url will also be used as a base for URL composition to reach other resources.
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
  onos> id=rest:127.0.0.1:8080, available=true, role=MASTER, type=SWITCH, mfr=unknown, hw=unknown, sw=unknown, serial=unknown, ipaddress=127.0.0.1, driver=restCiena, name=rest:127.0.0.1:8080
  ```

  If the device is not present then it could have been an error and you have to check the logs.

  + for localhost logs

    ```
    <your_machine>~$ tl
    ```

    or for remote logs

    ```
    <your_machine>~$ ol
    ```
  + verify that the logs don't contain REST related exceptions and this error does not appear:

    ```
    2016-01-19 15:19:28,102 | ERROR | event-dispatch-0 | RestDeviceProvider | 192 - org.onosproject.onos-restsb-provider-device - 1.5.0.SNAPSHOT | Device <device> not reachable, error creating HTTP connection
    java.net.ConnectException: Connection refused
    ```

    In case the log is present it means that the device was not able to reply on the given IP and Port. Verify Ip and Port in the Json file you posted and retry. If any other exception is present, such as no device name, please read the log and react to it accordingly.
* If your driver specifies a PortDiscovery implementation, such as PortDiscoveryCienaWaveserverImpl.java the Rest southbound provider also queries the ports that are available on that device and updates the information in the ONOS core.   
  So if your run in ONOS the command:

  ```
  onos> ports
  ```

  should return, among other devices also something like:

  ```
  onos> id=rest:127.0.0.1:8080, available=true, role=MASTER, type=SWITCH, mfr=unknown, hw=unknown, sw=unknown, serial=unknown, ipaddress=127.0.0.1, driver=restCiena, name=rest:127.0.0.1:8080
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
