"""Custom topology example

8 routers in 3 cities

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class SRTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
        host4 = self.addHost( 'h4' )

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')

        
        # Add links for hosts
        self.addLink( host1, s1)
        self.addLink( host2, s6 )
        self.addLink( host3, s1)
        self.addLink( host4, s7)

        # Add links between switches
        # Only a single link will be added here between any pair of switches
        # Extra links will be added bby the script that imports this topo file
        # See sr_cpqd_full.py
        self.addLink( s1, s2 )
        self.addLink( s1, s3)
        self.addLink( s2, s3)
        self.addLink( s2, s5 )
        self.addLink( s3, s4 )
        self.addLink( s4, s5 )
        self.addLink( s4, s6)
        self.addLink( s5, s6)
        
        self.addLink( s7, s8 )
        self.addLink( s2, s8 )
        self.addLink( s5, s8 )


topos = { 'mytopo': ( lambda: SRTopo() ) }
