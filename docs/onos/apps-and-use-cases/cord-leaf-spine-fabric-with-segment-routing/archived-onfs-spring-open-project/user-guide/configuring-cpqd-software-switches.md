# Configuring CPqD Software Switches

This page isn't so much about configuring the software switches – these switches don't need any configuration – it's more about setting up a Mininet network that reflects the [network configuration loaded on the controller](configuring-onos-spring-open.md).

First, create a network topology file the usual way using the Mininet Topology API. See an example here: [srTopo8.py](../../../../../assets/srtopo8.py)

Add hosts and switches

```
host1 = self.addHost( 'h1' )
s1 = self.addSwitch('s1')
```

Add links between switches, and connect hosts to switches

```
 self.addLink( host1, s1)
self.addLink( s1, s2 )
```

Then create another file that loads the Topology file you created above. This file will create the network and connect the switches to the controller.

See an example of such a file here: [sr\_cpqd\_full.py](../../../../../assets/sr_cpqd_full.py)

Load the topo file

```
from srTopo8 import SRTopo
... #omitted lines
topo = SRTopo()
```

Make sure you use the CPqD switch (UserSwitch) and not the default OVS switch, and point the switches to the remote controller (or local controller if you use localhost)

```
net = alterNet(topo=topo, switch=UserSwitch, controller=partial(RemoteController,ip='127.0.0.1'))
```

The Mininet Topology API does not currently allow us to create multiple links between the same pair of switches. Thus we need to use a different API (the Net API) to create extra links.

We do so by loading the switches from the 'net' and adding more links

```
#adding extra links between routers
s1, s2, s3, s4, s5, s6, s7, s8 = net.switches
net.addLink( s7, s8 )
net.addLink( s7, s8 )
net.addLink( s3, s1 )
net.addLink( s2, s5 )
net.addLink( s3, s4 )
net.start()
```

This example shows all the extra links created in the prototype used in the [demo prototype videos](../prototype-demo-videos.md).

Next we need to configure the hosts with the correct IP and Gateway information

```
# host h1 is attached to router s1
h1.setIP("10.200.1.2/24")
h1.setMAC("00:00:00:00:01:02")
setDefaultRoute(h1, "10.200.1.1")
```

The example above, shows that host h1's IP and MAC addresses are set using the setIP and setMAC api calls. It also shows that the default gateway for host h1 is 10.200.1.1. Note that this default gateway has to be configured in the [configuration file loaded on the controller](configuring-onos-spring-open.md) - specifically in the 'subnet' field of the switch configuration.

Finally note that the configuration at the controller currently requires the configuration of the links in the network. This can be useful in scenarios where the network operator wishes to consider the configuration as the 'golden rule' - in such cases, if a network link is wired incorrectly, the the controller will figure out that the discovered link does not match the configuration, and will disallow the link from being used in the network - i.e. no traffic will use the link. On the other hand, it can be cumbersome at times to configure all the network links in the controller config file. It can especially be tricky when using a Mininet based network, because the Mininet APIs used above do not allow the user  to specify the ports when adding a link using addLink. Thus in order to get the controller configuration right, we need to create the network, connect it to the controller, figure out which port-numbers Mininet used to create the links, use those port numbers in the controller config file, and finally reload the controller.

Once the python files are created in mininet/custom directory, use the following command to launch Mininet

```
# sudo ./mininet/custom/sr_cpqd_full.py
```

See [Using the CLI](using-the-cli.md) section to verify that the correct switches and links have been discovered by the controller.
