# Configuring Dell Hardware Switches

1. Configure CAM

   ```
   #configure
   (conf)#cam-acl l2acl 2 ipv4acl 2 ipv6acl 0 ipv4qos 0 l2qos 1 l2pt 0 ipmacacl 0 vman-qos 0 ecfmacl 0 openflow 8
   (conf)#cam-acl-vlan vlanopenflow 1 vlaniscsi 1  vlanaclopt 0
   (conf)#exit
   ```
2. Reboot the switch

   ```
   #reload
   System configuration has been modified. Save? [yes/no]: yes
   !

   Proceed with reload [confirm yes/no]: yes
   ```
3. Create openflow instance

   ```
   #configure
   (conf)#openflow of-instance 1
   (conf-of-instance-1)#controller 1 10.11.44.5 tcp [ change to your controller ip ]
   (conf-of-instance-1)#flow-map l2 enable
   (conf-of-instance-1)#flow-map l3 enable
   (conf-of-instance-1)#interface-type any
   (conf-of-instance-1)#multiple-fwd-table enable
   (conf-of-instance-1)#of-version 1.3
   (conf)#exit
   ```
4. Add interfaces to the openflow instance

   ```
   (conf)#interface TenGigabitEthernet 0/0 [ change to your network ports]
   (conf-if-te-0/0)#of-instance 1
   (conf-if-te-0/0)#no switch-port
   (conf-if-te-0/0)#no shutdown
   (conf)#exit
   ```
5. Enable the openflow instance

   ```
   (conf)#openflow of-instance 1
   (conf-of-instance-1)#no shutdown
   (conf-of-instance-1)#exit
   ```
6. Ensure that the [network configuration file loaded on to the controller](configuring-onos-spring-open.md) matches the configuration of the hardware.
