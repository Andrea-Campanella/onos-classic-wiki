#!/usr/bin/env python

from mininet.net import Mininet 
from mininet.cli import CLI
from mininet.log import setLogLevel, info

class Domain(object):
    """
    A container for switch, host, link, and controller information to be dumped
    into the Mininet mid-level API.
    """

    def __init__ (self, did=0):
        # each Domain has a numeric ID for sanity/convenience
        self.__dId = did

        # information about network elements - for calling the "mid-level" APIs
        self.__ctrls = {}
        self.__switches = {}
        self.__hosts = {}
        self.__links = {}
        # maps of devices, hosts, and controller names to actual objects
        self.__smap = {}
        self.__hmap = {}
        self.__cmap = {}

    def addController(self, name, **args):
        self.__ctrls[name] = args if args else {}
        return name

    # Note: This method will return the name of the swich, not the switch object
    def addSwitch(self, name, **args):
        self.__switches[name] = args if args else {}
        return name

    def addHost(self, name, **args):
        self.__hosts[name] = args if args else {}
        return name

    def addLink(self, src, dst, **args):
        self.__links[(src, dst)] = args if args else {}
        return (src, dst)

    def getId( self):
        return self.__dId

    def getControllers(self, name=None):
        return self.__cmap.values() if not name else self.__cmap.get(name)

    def getSwitches(self, name=None):
        return self.__smap.values() if not name else self.__smap.get(name)

    def getHosts(self, name=None):
        return self.__hmap.values() if not name else self.__hmap.get(name)

    def injectInto(self, net):
        """ Adds available topology info to a supplied Mininet object. """
        # add switches, hosts, then links to mininet object
        for sw, args in self.__switches.iteritems():
            self.__smap[sw] = net.addSwitch(sw, **args)
        for h, args in self.__hosts.iteritems():
            self.__hmap[h] = net.addHost(h, **args)
        for l, args in self.__links.iteritems():
            src = self.__smap.get(l[0])
            dst = self.__smap.get(l[1])
            net.addLink(src if src else self.__hmap.get(l[0]),
                         dst if dst else self.__hmap.get(l[1]), **args)
        # then controllers
        for c, args in self.__ctrls.iteritems():
            self.__cmap[c] = net.addController(c, **args)

    def start(self):
        """ starts the switches with the correct controller. """
        map(lambda c: c.start(), self.__cmap.values())
        map(lambda s: s.start(self.__cmap.values()), self.__smap.values())

    def build(self, *args):
        """ override for custom topology, similar to Topo """
        pass

class TestDomain(Domain):
    """
    A tiny domain of two nodes connected together
    """
    def build(self):
        sw1 = 'sw%s1' % self.getId()
        sw2 = 'sw%s2' % self.getId()
        self.addSwitch(sw1)
        self.addSwitch(sw2)
        
        self.addLink(sw1, sw2)

if __name__ == '__main__':
    setLogLevel('info')
 
    #instantiate and build two TestDomains with Domain IDs '1' and '2'
    domain1 = TestDomain(1)
    domain2 = TestDomain(2)
    domain1.addController('c1')
    domain2.addController('c2')
    domain1.build()
    domain2.build()
 
    # add prepared domains to the network, and initialise
    net = Mininet()
    domain1.injectInto(net)
    domain2.injectInto(net)
    net.build()
 
    # connect the domains together
    net.addLink(domain1.getSwitches('sw11'), domain2.getSwitches('sw21'))
 
    # start()ing the Domains associates the switches in the domains
    # with the controllers that had been added to them
    domain1.start()
    domain2.start()
 
    # start up a CLI, as usual. net.stop() will stop the domains it knows about.
    CLI(net)
    net.stop()
