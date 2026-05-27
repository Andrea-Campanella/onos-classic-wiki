# NETCONF Fault Management

## Overview

[NETCONF](../../guides/administrator-guide/configuring-onos/southbound-protocols/netconf.md) devices send notifications to the network operator when events or faults occur. NETCONF fault management comprises of catching and translating these messages and sending the resultant alarms to the Alarm subsystem.

## Path from NETCONF device notification to alarm

In **NetconfStreamThread**, messages from the device are caught and notification messages are sent to all **NetconfDeviceOutputEventListener** listeners as part of a **NetconfDeviceOutputEvent** with type DEVICE\_NOTIFICATION. **NetconfAlarmProvider** catches these notification events with **InternalNotificationListener**, which implements **NetconfDeviceOutputEventListener**. **NetconfAlarmTranslator** takes the deviceId of the device and the device message from the event and converts them to alarm(s), which are defined by **Alarm.java**. Then, the **AlarmManager** updates the **AlarmStore** with these new alarms through updateAlarmList. Every time an alarm is added to the alarm store, its information is printed to the log.

## Subscriptions to Notifications

In **NetconfSessionImpl**, which implements **NetconfSession**, startSubscription starts a subscription to all notification messages of the specified device. The ability to filter messages is in progress. For more information on notifications, refer to [RFC 5277](https://tools.ietf.org/html/rfc5277).
