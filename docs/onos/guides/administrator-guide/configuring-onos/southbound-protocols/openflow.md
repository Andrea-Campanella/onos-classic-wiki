# OpenFlow

OpenFlow is the primary southbound protocol the SDN *control* plane. OpenFlow operates at time scales close to the data network round trip time (RTT), usually milliseconds, and is primarily used to program flow tables that control packet forwarding using the match-action model. ONOS's packet forwarding abstractions primarily use OpenFlow to program switch flow tables.

OpenFlow also provides some limited *configuration* capabilities (such as bringing a port up or down, or configuring meters), but many required configuration operations (such as telling a switch which controllers to connect to, enabling the OpenFlow agent on a switch, or enabling OpenFlow on specific ports) are explicitly out of scope for OpenFlow.

Switches that require configuration beyond what OpenFlow provides may need to use other southbound protocols such as ovsdb, NetConf, SNMP, etc.. ONOS currently provides drivers for several southbound configuration protocols. In the future, ONOS may provide configuration abstractions which enable devices to be configured in a generic manner, without having to worry about specific configuration protocols and their varying semantics across devices.

To enable OpenFlow, the `drivers` and `openflow` apps must be activated, and switches must be configured appropriately to connect to all ONOS instances.
