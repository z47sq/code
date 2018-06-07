#!/usr/bin/env python
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):

        # initilaize topology   
        Topo.__init__( self )

        # Add hosts and switches
        leftHost1 = self.addHost( 'h1' )
        rightHost2 = self.addHost( 'h2' )
	leftHost3 = self.addHost( 'h3' )
	rightHost4 = self.addHost( 'h4' )
	leftHost5 = self.addHost( 'h5' )
	rightHost6 = self.addHost( 'h6' )
	leftHost7 = self.addHost( 'h7' )
	rightHost8 = self.addHost( 'h8' )
        Switch1 = self.addSwitch( 's1' )
        leftSwitch2 = self.addSwitch( 's2' )
	rightSwitch3 = self.addSwitch( 's3' )
	leftSwitch4 = self.addSwitch( 's4' )
	rightSwitch5 = self.addSwitch( 's5' )
	leftSwitch6 = self.addSwitch( 's6' )
	rightSwitch7 = self.addSwitch( 's7' )

        # Add links
        self.addLink( Switch1,leftSwitch2 )
        self.addLink( Switch1, rightSwitch3 )
        self.addLink( leftSwitch2, leftSwitch4 )
	self.addLink( leftSwitch2, rightSwitch5 )
	self.addLink( rightSwitch3, leftSwitch6 )
	self.addLink( rightSwitch3, rightSwitch7 )
	self.addLink( leftSwitch4, leftHost1 )
	self.addLink( leftSwitch4, rightHost2 )
	self.addLink( rightSwitch5, leftHost3 )
	self.addLink( rightSwitch5, rightHost4 )
	self.addLink( leftSwitch6, leftHost5 )
	self.addLink( leftSwitch6, rightHost6 )
	self.addLink( rightSwitch7, leftHost7 )
	self.addLink( rightSwitch7, rightHost8 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
