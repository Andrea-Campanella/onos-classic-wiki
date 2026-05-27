# OVSDB interaction and ONOS cli example

## Get and Set Controllers with CLI on a device through OVSDB

An example of OVSDB infrastructure usage is getting and setting controllers on a device through CLI commands. The set and get conntrollers operations are defined in an ONOS *Behaviour*, in our case the **OvsdbControllerConfig**.java****, that implements**ControllerConfig** general behaviour. In the behavior to do operations on the devices, you need the **OvsdbController**, which you can obtain through the **DriverHandler**. The OvsdbController instance now gives you access to the database and you can do operations on a specific device through a OvsdbClient specific for that device.

To call the getControllers and setControllers methods you need to obtain the *ControllerConfig Behaviour* and then call on this instance the methods.

## Example

The set and get commands are implemented, as an example, in **DeviceControllersCommand.java** and **DeviceSetControllersCommand.java**that provide, in two CLI commands

```
onos> device-controllers <openflow_device>
```

This command returns the list of controllers for that particular openflow device.

```
onos> device-setcontrollers <openflow_device> <list of controllers>
```

This command puts the given list of controllers as the controllers of the device, removing all the old ones.

## Try it on your machine

Infrastructure Setup:

* start ONOS

  ```
  <your_machine>: $ ok clean
  ```

* ssh into the mininet machine:

  ```
  <your_machine>: $ sshnet
  ```
* tell the ovsdb server to start listening on port 6640:

  ```
  mininet-vm:~$ sudo ovs-vsctl set-manager ptcp:6640
  ```

  if you are running a version of OVSDb older than 2.3.1 and the command before does not work you could try

  ```
  mininet-vm:~$ sudo ovs-vsctl set-manager tcp:127.0.0.1:6640
  ```
* start a sample topology

  ```
  mininet-vm:~$ sudo mn --controller=remote,ip=<ONOS_INSTANCE_IP_ADDRESS> --topo linear,3
  ```

* activate the openflow app :

  ```
  onos> app activate org.onosproject.openflow
  ```

* activate the ovsdb app :

  ```
  onos> app activate org.onosproject.ovsdb
  ```
* activate the ovsdb driver:

  ```
  onos> app activate org.onosproject.drivers.ovsdb
  ```

* run the get command

  ```
  onos> device-controllers of:0000000000000001
  ```

* run the set command

  ```
  onos> device-setcontrollers of:0000000000000001 <protocol>:<ip>:<port> <protocol>:<ip>:<port>
  ```
