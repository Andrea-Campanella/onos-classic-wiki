# SONA Architecture

# Overall Architecture

![](../../../../assets/image2018-6-1_22-42-25-1.png)

# Software Components

SONA is composed of three ONOS applications, OpenstackNode, OpenstackNetworking, and a set of assistant applications.

## OpenstackNode

OpenstackNode application is in charge of managing and bootstrapping compute and gateway nodes. The node bootstrap procedure includes the following steps. It leverages OVSDB to configure OVS on a node. 

* Connect to OVSDB at compute gateway nodes.
* Create an integration bridge, typically "br-int", and set its OpenFlow controller to ONOS cluster.
* Create an tunneling bridge named as "br-tun", if the nodes run in OVS-DPDK mode.
* Add VXLAN, GRE and GENEVE tunneling ports to br-int with "flow" key and "flow" remote IP.
* Add VLAN interface to br-int if specified.
* Add physical interfaces to br-int if specified.

## OpenstackNetworking

OpenstackNetworking application is in charge of managing virtual network states and providing a network connectivity to virtual machines by setting flow rules to compute and gateway node's OVS. As it plays a role of Neutron ML2 mechanism driver and L3 plugin backend, it exposes REST APIs that networking-onos(<https://github.com/openstack/networking-onos>) calls. More specifically, when a user (or Nova agent) requests a virtual network changes to OpenStack, the request is post-committed to OpenstackNetworking app via networking-onos driver. When a port is added or removed to/from OVS, OpenstackNetworking app identifies the port by its port name, which includes port UUID, and then installs or removes flow rules based on the virtual network states related to the port including network, subnet, router and gateways. All kinds of East-West traffic is handled at compute nodes and only North-South traffic is forwarded to gateway nodes, which have an access to both internal and external network, and NATed there to public IP before leaving the virtual world. The application is also in charge of replying to ARP and DHCP requests from virtual machines. For the subnet gateway and DHCP server, it replies with pre-defined fake MAC address.
