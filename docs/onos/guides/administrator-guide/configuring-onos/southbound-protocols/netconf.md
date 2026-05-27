# NETCONF

## Table of Contents

## Contributors

| Name | Organization | Role | Email |
| --- | --- | --- | --- |
| Andrea Campanella | ONF | Developer | andrea@opennetworking.us |
| Helen Wu |  | Developer |  |

## Overview

This section provides an overview on the NETCONF protocol implementation in ONOS.

![](https://docs.google.com/drawings/d/1_MH8iTJ8Lm6uMcndp2m0AaX8aGaGSUVfqa0vxASsf4Q/pub?w=960&h=720)

## Interfaces and Classes

* **NetconfController.java** implemented by **NetconfControllerImpl**.java**:** tracks all the NETCONF devices, serves as a one stop for connecting and obtaining a device and (un)register listeners on device events.
* **NetconfDevice**.java**** implemented by **NetconfDeviceImpl**.java**:** represents a NETCONF capable device connected to the ONOS core with his own NetconfSession and his informations saved in an instance of NetconfDeviceInfo
* **NetconfSession**.java**:** interface that every type of transport connection to a NETCONF device must implement, represents the *single access point* for any operation on the device. An example is **NetconfSessionImpl:** uses an SSH2 Connection and Session to exchange information and perform operations like get/set-config with the physical NETCONF device. The capability to start a subscription to a device's notifications can be started here.
* **NetconfSessionDelegate.java:**delegate interface implemented by**NetconfSessionDelegateImpl** in **NetconfSessionImpl.** Serves the purpose of completing the future returned by the thread so the session can return the correct reply for the specific request to the caller, effectively making the request call blocking on the Future.
* **NetconfDeviceProvider**.java**:** manages any NETCONF device role and all the interactions with the ONOS core. The provider is responsible for periodically checking for changes in the availability of NETCONF devices, which it does in *checkAndUpdateDevices()*.
* **NetconfDeviceListener**.java**** implemented by **InnerNetconfDeviceListener**.java**** in NetconfDeviceProvider**:** informs the provider in the ONOS core that a NETCONF device is connected/disconnected.
* **NetconfDeviceOutputEvent.java** represent an output event from a device session's stream, it can be a reply, notification, unregistration from the network, error.
* **NetconfDeviceOutputEventListener.java**implemented by **NetconfDeviceOutputEventListenerImpl.java****:** interface and implementation of a listener that receives notifications from the device stream: replies, notifications, disconnections and errors. NetconfSession has method to set them to the underling stream handler class, such as NetconfStreamThread.
* **NetconfDeviceInfo**.java**:** contains ip,port,protocol,username,password and DeviceId of a NETCONF device; it's used to exchange information about a device without having to pass the device instance itself.
* **NetconfAlarmProvider.java**: manages capturing relevant notifications from devices and creating and alerting the core of alarms based on these notifications.
* **NetconfAlarmTranslator.java**: translates the general case of a NETCONF notification to an alarm, defined by **Alarm.java**, with information from the notification message.
* **NetconfException.java** represents an exception happened in the NETCONF protocol implementation.

Through implementing the **NetconfDeviceOutputEventListener.java** and adding the listener to the sessionanybody who needs to obtain device notifications can listen on device generated messages that are picked up by the listeners implementations that is in the set of to be notified listeners in the StreamHandler implementation, right now **NetconfStreamThread.java.**

## Supported NETCONF Operations

* **sendHello**, sends opening hello message which exchanges device capabilities
* **get**, requests information from specified configuration
* **getConfig**, gets specified configuration
* **editConfig**, edits specified configuration
* **copyConfig**, copies specified configuration
* **deleteConfig**, deletes specified configuration (except <running/>)
* **lock**, locks specified configuration
* **unlock**, unlocks specified configuration
* **startSubscription**, starts a subscription to all notifications from specified device with interleave
* **endSubscription**, ends subscription to notifications from specified device – keeps existing SSH session alive
* **closeSession/killSession**, closes/kills SSH session

For more background on NETCONF operations, refer to [this](http://www.netconfcentral.org/netconf_docs#operations) [reference source](http://www.netconfcentral.org/netconf_docs#operations) [about NETCONF protocol operations.](http://www.netconfcentral.org/netconf_docs#operations)

## Device Discovery

Currently, ONOS is made aware of NETCONF devices through the use of a [Network Configuration Service](../the-network-configuration-service.md) JSON file, which represents the configuration of and provides information about devices. An example of such a file is provided [here on GitHub](https://github.com/opennetworkinglab/onos/blob/master/tools/test/configs/netconf-cfg.json) if you don't have the source code checked out or in the ONOS source code in *${ONOS\_ROOT}/tools/test/configs/netconf-cfg.json*. This JSON file informs ONOS of the existence of such devices when it is pushed, but the confirmation of their reachability and availability occurs in the device provider, NetconfDeviceProvider. For more information about the device subsystem, refer to the [Device Subsystem](../../../architecture-and-internals-guide/device-subsystem.md) wiki page. When the NETCONF devices from the JSON files are pushed to ONOS, the devices are created with the default availability set to false, indicating inability to use the device. Shortly after (approximately 3 seconds after devices configuration is pushed to ONOS), and at intervals of 30 seconds afterwards, the reachability of all devices in the configuration is checked, and according to the information collected, the devices are either marked online (available=true), marked offline (available=false), or the availability state is left unchanged.

## Connect your own device to ONOS

If you have your own device that talks NETCONF protocol follow this section. Otherwise, if you want to try ONOS NETCONF implementation out with a test VM proceed to the [Example section](netconf.md).

Once you have your device Running on some IP address and some port, in order to make ONOS see it you should follow these steps.

* start ONOS
* activate the netconf app :

  ```
  onos> app activate org.onosproject.netconf
  ```
* if you wrote your own driver for your device activate that specific driver (i.e.) :

  ```
  onos> app activate org.onosproject.drivers.fujitsu
  ```
* give ONOS the information to connect to the device and which driver to use for you device in a json file. You need to specify username, password, ip and port. If you wrote a specific driver that has also to be changed form the standard "netconf" one.

  ```
  {
    "devices": {
      "netconf:<ip>:<port>": {
        "netconf": {
          "ip": "<ip>",
          "port": <port>,
          "username": "<username>",
          "password": "<password>"
        },
        "basic": {
          "driver": "<driver-name>"
        }
      }
    }
  }
  ```

  A working example is [here on GitHub](https://github.com/opennetworkinglab/onos/blob/master/tools/test/configs/netconf-cfg.json) or in $ONOS\_ROOT/tools/test/configs/netconf-cfg.json if you have the source code. Change the IP both in the DeviceId at the top and in the devices array. The port number by default on NETCONF is 830, so unless you made any changes to that leave it as is. For passwordless ssh, don't provide password field in the netconf-cfg.json and generate ssh keys on onos host machine at path /root/.ssh/ with name id\_rsa using ssh-keygen -m PEM -t rsa -N "" -f /root/.ssh/id\_rsa. ONOS will automatically pick up private key from this path and use it for authenticating ssh session.  
  You can also add other information, more than the driver, to the basic device configuration information: "type": "<device-type>", "manufacturer": "<device-manufacturer>","hwVersion": "<hw-version>","swVersion": "<sw-version>".  
  If you don't specify any driver-name in the basic configuration ONOS will assign the default one. Being the default one very much related to OpenFlow devices. It's suggested to always specify the driver-name  with yours or the "*netconf*" one.
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
  onos> id=netconf:10.1.9.24:830, available=true, role=MASTER, type=SWITCH, mfr=unknown, hw=unknown, sw=unknown, serial=unknown, ipaddress=10.1.9.24, driver=ovs-netconf, name=netconf:10.1.9.24:830
  ```

  If the device is not present then it could have been and error and you have to check the logs.

  + for localhost logs

    ```
    <your_machine>~$ tl
    ```

    or for remote logs

    ```
    <your_machine>~$ ol <IP Address with ONOS instance>
    ```
  + verify that the logs don't contain NETCONF related exceptions and this warning does not appear:

    ```
    WARN  | event-dispatch-0 | ListenerRegistry <.....> org.onosproject.netconf.NetconfException: Can't connect to NETCONF device on 10.1.9.24:830
    ```

    In case the log is present it means that the device was not able to reply on the given IP and Port. Verify Ip and Port in the Json file you posted and retry. If any other exception is present, such as no device name, please read the log and react to it accordingly.
* Once the device is present in ONOS you can interact with it.

## Timeouts

The NETCONF controller has 3 timeout parameters which control how the underlying SSH client connects to the remote NETCONF device

* The **connect** timeout - the length of time in seconds that is allowed for the SSH connection protocol to complete - this is **5 second**s by default
* The **reply** timeout - the length of time in seconds that is allowed for a reply to a NETCONF command to be returned - this is **5 seconds** by default
* The **idle** timeout - the length of time in seconds that the SSH connection will be automatically closed after if no traffic is detected - this is **300 seconds** by default

These 3 parameters are changeable both system wide through the Configuration Service and individually per NETCONF device through the Network Configuration Service.

The system-wide adjustment can be made through the ONOS CLI "cfg get" shows the values and "cfg set" changes the values:

```
onos> cfg get org.onosproject.netconf.ctl.impl.NetconfControllerImpl 
org.onosproject.netconf.ctl.impl.NetconfControllerImpl
    name=sshLibrary, type=string, value=apache-mina, defaultValue=apache-mina, description=Ssh Library instead of apache_mina (i.e. ethz-ssh2
    name=netconfIdleTimeout, type=integer, value=300, defaultValue=300, description=Time (in seconds) SSH session will close if no traffic seen
    name=netconfConnectTimeout, type=integer, value=5, defaultValue=5, description=Time (in seconds) to wait for a NETCONF connect.
    name=netconfReplyTimeout, type=integer, value=5, defaultValue=5, description=Time (in seconds) waiting for a NetConf reply
onos>
```

Values for individual devices are settable through the Network Configuration Service. Under the "netconf" grouping the following additional attributes can be optionally added in any order

* "**connect-timeout**": <int - values below 1 will be ignored>
* "**reply-timeout**": <int - values below 1 will be ignored>
* "**idle-timeout**": <int - values below 1 will be ignored>

If individual device settings exist for a device, they will take priority over system wide settings for that device. It is at the creation of the NETCONF session that the values are taken in to account and changing them after that will have no effect on that session. If the session is closed however, and a new session opened, then any new values are taken in to account.

**for example**

```
 "devices": {
    <device-id>: {
    "netconf": {
          "username": <user>,
          "password": <pw>,
          "ip": <ip>,
          "port": <port>,
          "connect-timeout": 20,
          "reply-timeout": 25
    },
```

## SSH Client

Two different SSH Client libraries are available in ONOS for NETCONF connections - Apache Mina SSH Client and Ganymede SSH Client - Apache Mina is the default library.

Again the client library may be set system wide or individually per device. To set it per device use the following when provisioning the device through the Network Configuration Service.

* "**ssh-client**": <value - either "**ethz-ssh2**" or "**apache-mina**">

**NOTE :** ethz-ssh2 has been removed from ONOS 1.10 onwards.

## Example: Get and Set Controllers.

An example of NETCONF infrastructure usage is getting and setting controllers on a device. These operations are defined in an ONOS *Behaviour*, in our case the **NetconfControllerConfig**.java****, that implements **ControllerConfig** general behaviour. To do in the Behaviour operations on the devices, you need the **NetconfController**, which you can obtain through the **DriverHandler**. The NetconfController instance now gives you access to all the device or a single device. Once you have the device you are interested in based upon the deviceId you can get the **NetconfSession** object to communicate with the device and do operations on the physical devices, like getting the configuration in the get controllers methods or setting a pre-built new one for the setControllers. **XmlConfigParser.java** offers a method to extract the desired information from an devices's XML response and another method to produce the correct XML to set one or more controller on a specific device.

You can take a look at the actual implementation of the get and set controllers operation in the NetconfControllerConfig.java class. For an example of other operations that can be implemented the OVSDB infrastructure provides a good starting point.

To call the getControllers and setControllers methods you need to obtain the *ControllerConfig Behaviour* and then call on this instance the methods. The set and get commands are implemented, as an example, in **DeviceControllersCommand.java** and **DeviceSetControllersCommand.java** that provide, in two CLI commands

```
onos> device-controllers
```

```
onos> device-setcontrollers
```

## Example: Testing infrastructure

To test locally (not on real switches) the NETCONF implementation you need the Mininet machine with *of-config* installed (link to mininet machine).

| VM | Description | Comments |
| --- | --- | --- |
| [onos-ofconfig-mininet.ova](https://drive.google.com/file/d/1YHzZSzrYfr8tTzvpOsCgxKfymIcCZiMU/view?usp=sharing) | Mininet machine with of-config installed | Username / Password: **mininet**/ **mininet** |

**of-config** is wrapper for an openvswitch instance, that uses NETCONF protocol and translates it to OVSDB in order to use that database implementation.

Infrastructure Setup:

* Start the Mininet machine with of-config installed under Virtual-Box
* [Optional] If you are running one ONOS instance outside of localhost (127.0.0.1), set a controller with the set controller command. For example, you will have a different IP for your ONOS instance.

  ```
  mininet-vm:~$ sudo ovs-vsctl set-controller ofc-bridge tcp:10.128.12.1:6653
  ```
* [Optional] If you are running multiple external ONOS instances,

  ```
  mininet-vm:~$ sudo ovs-vsctl set-controller ofc-bridge tcp:10.128.12.1:6653 tcp:10.128.12.2:6653 tcp: 10.128.12.3:6653
  ```
* Start the ofc-server in the Mininet machine

  ```
  mininet-vm:~$ sudo ofc-server -v 3 -f
  ```
* start ONOS
* activate the netconf app :

  ```
  onos> app activate org.onosproject.netconf
  ```
* activate the netconf drivers :

  ```
  onos> app activate org.onosproject.drivers.netconf
  ```
* give ONOS the information to connect to the device and which driver to use for it in the $ONOS\_ROOT/tools/test/configs/netconf-cfg.json file. Change the IP both in the DeviceId at the top and in the devices array. The port number by default on NETCONF is 830, so unless you made any changes to that leave it as is.
* upload the configuration you just modified to the instance of ONOS you are running, in our case localhost:

  ```
  <your_machine>~$ curl -X POST -H "content-type:application/json" http://localhost:8181/onos/v1/network/configuration -d @$ONOS_ROOT/tools/test/configs/netconf-cfg.json --user onos:rocks
  ```

  or

  ```
  <your_machine>~$ onos-netcfg localhost $ONOS_ROOT/tools/test/configs/netconf-cfg.json
  ```
* open the onos logs

  for localhost logs

  ```
  <your_machine>~$ tl
  ```

  or for remote logs

  ```
  <your_machine>~$ ol
  ```
* verify that the logs don't contain NETCONF related exceptions and this warning does not appear:

  ```
  | WARN | event-dispatch-0 | NetconfDeviceProvider | 186 - org.onosproject.onos-netconf-provider-device - 1.4.0.SNAPSHOT | Can't connect to NETCONF device on <ip>:<port>
  ```

  In case the log is preset it means that the device was not able to reply on the given IP and Port. Verify Ip and Port in the Json file you posted and retry. If any other exception is present, such as no device name, please read the log and react to it accordingly.
* Call the command or run the app you have written. For example:

  ```
  onos> device-controllers netconf:@10.1.9.24:830
  ```

## Fault Management

If you start a subscription to a device with createSubscription, ONOS will receive <notification> XML messages from the NETCONF device. **NetconfAlarmProvider** and **NetconfAlarmTranslator** translate these notification messages into alarms, as they are defined in **Alarm.java**, and notifies the core about the new alarms. For more information about fault management, refer to [NETCONF Fault Management](../../../../new-projects/fault-management/netconf-fault-management.md).

## Future Work

There is much room for improvement and testing, this is only a basic skeleton of the infrastructure. The improvement should be focused on extracting the XML that is now encoded in the NetconfSessionImpl's methods and testing each operation. In the future the XML can be generated through YANG models so it can be specific for every type of device we want to connect.
