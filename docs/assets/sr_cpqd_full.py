#!/usr/bin/env python
'''
Script to connect 8 router & 4 host topo


'''

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import UserSwitch, RemoteController, OVSSwitch
from mininet.topolib import TreeNet
from mininet.topo import SingleSwitchTopo
from mininet.net import Mininet
from functools import partial
from srTopo8 import SRTopo
from alterableNet import alterableCLI
from alterableNet import alterNet

def setDefaultRoute(node, ip, intf=None):
    """Modified node.setDefaultRoute that sets a default gateway IP.

    Example call:
    /sbin/route add -net 0.0.0.0 gw 1.1.1.1 eth0
    
    ip: string
    intf: interface string
    """
    if not intf:
        intf = node.defaultIntf()
    #node.cmd( 'ip route flush root 0/0' )
    #node.cmd( 'route add default %s' % intf )
    node.cmd('route add -net 0.0.0.0 gw %s %s' % (ip, intf))

if __name__ == '__main__':
    setLogLevel( 'info' )
    topo = SRTopo()
    # load the topology, use the cpqd1.3 switch and point to a controller running
    # in the this VM
    net = alterNet(topo=topo, switch=UserSwitch, controller=partial(RemoteController,ip='127.0.0.1'))
    
    #adding extra links between routers
    s1, s2, s3, s4, s5, s6, s7, s8 = net.switches
    net.addLink( s7, s8 )
    net.addLink( s7, s8 )
    net.addLink( s3, s1 )
    net.addLink( s2, s5 )
    net.addLink( s3, s4 )
    net.start()
   
    # end-host configuration
    h1, h2, h3, h4 = net.hosts

    # host h1 is attached to router s1
    h1.setIP("10.200.1.2/24")
    h1.setMAC("00:00:00:00:01:02")
    setDefaultRoute(h1, "10.200.1.1")

    # host h2 is attached to router s6
    h2.setIP("10.200.2.24/24")
    h2.setMAC("00:00:00:00:02:24")
    setDefaultRoute(h2, "10.200.2.1")

    # host h3 is attached to router s1
    h3.setIP("10.200.3.12/24")
    h3.setMAC("00:00:00:00:03:12")
    setDefaultRoute(h3, "10.200.3.1")

    # host h4 is attached to router s7
    h4.setIP("10.200.4.42/24")
    h4.setMAC("00:00:00:00:04:42")
    setDefaultRoute(h4, "10.200.4.1")

    alterableCLI(net)
    net.stop()
