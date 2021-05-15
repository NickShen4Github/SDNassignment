from mininet.topo import Topo 
from mininet.node import Node 
from mininet.net import Mininet 
from mininet.log import setLogLevel, info 
from mininet.cli import CLI 

class NATopo(Topo):
    def __init__(self): 
        Topo.__init__(self)

        info( '***Adding Building 1***')
###################################################
        info( '***Adding Ground Floor***')

        "Create reception topo."
        sw1_1_1 = self.addSwitch('sw1_1_1')#SW4
        h01_1= self.addHost('h01_1',ip='192.168.1.1/24')
        h01_2= self.addHost('h01_2',ip='192.168.1.2/24')
        "Create links."
        self.addLink(h01_1,sw1_1_1,1,1)
        self.addLink(h01_2,sw1_1_1,1,2)

        "Create 5 Offices topo."
        h02_1= self.addHost('h02_1',ip='192.168.2.1/24')
        h02_2= self.addHost('h02_2',ip='192.168.2.2/24')
        h02_3= self.addHost('h02_3',ip='192.168.2.3/24')
        h02_4= self.addHost('h02_4',ip='192.168.2.4/24')
        h02_5= self.addHost('h02_5',ip='192.168.2.5/24')
        "Create links."
        self.addLink(h02_1,sw1_1_1,1,3)
        self.addLink(h02_2,sw1_1_1,1,4)
        self.addLink(h02_3,sw1_1_1,1,5)
        self.addLink(h02_4,sw1_1_1,1,6)
        self.addLink(h02_5,sw1_1_1,1,7)

        "Create SL server."
        sv5= self.addHost('sv5',ip='192.168.100.5/24')
        "Create 4 R&D server."
        sv1= self.addHost('sv1',ip='192.168.100.1/24')
        sv2= self.addHost('sv2',ip='192.168.100.2/24')
        sv3= self.addHost('sv3',ip='192.168.100.3/24')
        sv4= self.addHost('sv4',ip='192.168.100.4/24')
        "Create links."
        self.addLink(sv1,sw1_1_1,1,8)
        self.addLink(sv2,sw1_1_1,1,9)
        self.addLink(sv3,sw1_1_1,1,10)
        self.addLink(sv4,sw1_1_1,1,11)
        self.addLink(sv5,sw1_1_1,1,12)

###################################################
        info( '***Adding First Floor***')

        "Create Lab topo."
        sw1_2_1 = self.addSwitch('sw1_2_1')#SW5
        for i in range(15):
            host = self.addHost('h11_%s' % (i+1), ip='192.168.3.%s/24' % (i+1))
        for l in range(15):
            self.addLink('h11_%s' % (l+1), sw1_2_1, 1, l+2)
 
        "Create 2 letern seminar + 6AP topo."

        sw1_2_2 = self.addSwitch('sw1_2_2')#SW3
        ht1 = self.addHost('ht1', ip='192.168.4.1/24')
        ht2 = self.addHost('ht2', ip='192.168.5.1/24')
        self.addLink('ht1', 'sw1_2_2', 1, 1)
        self.addLink('ht2', 'sw1_2_2', 1, 2)
        #add AP later

        "Create 2 lab seminar topo."
        sw1_2_3 = self.addSwitch('sw1_2_3')#SW6
        sw1_2_4 = self.addSwitch('sw1_2_4')#SW7

        #seminar1 192.168.6.0 seminar2 192.168.7.0
        for lab in range(2):
            for i in range(20):
                host = self.addHost('h1%s_%s' % ((lab+2),(i+1)), ip='192.168.%s.%s/24' % ((lab+6),(i+1)))
            for l in range(20):
                self.addLink('h1%s_%s' % ((lab+2),(l+1)), 'sw1_2_%s' %(lab+3), 1, l+2)

###################################################
        info( '***Adding Second Floor***')
        sw1_3_1 = self.addSwitch('sw1_3_1')#SW8

        "Create Prototyping lab topo."
        for h in range(10):
            host = self.addHost('h21_%s' % (h + 1), ip='192.168.8.%s/24' % (h + 1))
        for l in range(10):
            self.addLink('h21_%s' % (l + 1), sw1_3_1, 1, l+1)

        "Create  6 offices  topo."
        for h in range(6):
            host = self.addHost('h22_%s' % (h + 1), ip='192.168.9.%s/24' % (h + 1))
        for l in range(6):
            self.addLink('h22_%s' % (l + 1), sw1_3_1, 1, l+11)

        "Create Prototyping lab topo."
        host = self.addHost('h23_1',  ip='192.168.10.1/24')
        self.addLink('h23_1', sw1_3_1, 1, 17)

###################################################
        "Create building2 topo."
        sw2_1 = self.addSwitch('sw2_1')#SW9
        sw2_2 = self.addSwitch('sw2_2')#SW10
# no AP yet
        "10 IP cams"
        for c in range(10):
            host = self.addHost('hc%s' % (c + 1), ip='192.168.11.%s/24' % (c + 1))
        for l in range(10):
            self.addLink('hc%s' % (l + 1), sw2_1, 1, l+1)

        "10 IP sensors"
        for s in range(10):
            host = self.addHost('hs%s' % (s + 1), ip='192.168.12.%s/24' % (s + 1))
        for l in range(10):
            self.addLink('hs%s' % (l + 1), sw2_1, 1, l+11)

        "2 HPC"
        hpc1 = self.addHost('hpc1',ip='192.168.13.1/24')
        hpc2 = self.addHost('hpc2',ip='192.168.13.2/24' )
        self.addLink('hpc1', sw2_2, 1, 1)
        self.addLink('hpc2', sw2_2, 1, 2)

###################################################
        "Add internet"
        hi = self.addHost('hi',ip='0.0.0.0')
        sw1 = self.addSwitch('sw1')#SW1
        sw2 = self.addSwitch('sw2')#SW2
        self.addLink('hi', sw1, 1, 1)
        self.addLink('hi', sw2, 2, 1)

        "Create major switch links topo."
        self.addLink(sw1, sw2, 2, 2)
        "SW1 to all other."
        self.addLink(sw1, sw1_1_1, 3, 13)
        self.addLink(sw1, sw1_2_1, 4, 17)
        self.addLink(sw1, sw1_2_2, 5, 3)
        self.addLink(sw1, sw1_2_3, 6, 22)
        self.addLink(sw1, sw1_2_4, 7, 22)
        self.addLink(sw1, sw1_3_1, 8, 18)
        self.addLink(sw1, sw2_1, 9, 21)
        self.addLink(sw1, sw2_2, 10, 3)
        "SW2 to all other."
        self.addLink(sw2, sw1_1_1, 3, 14)
        self.addLink(sw2, sw1_2_1, 4, 18)
        self.addLink(sw2, sw1_2_2, 5, 4)
        self.addLink(sw2, sw1_2_3, 6, 23)
        self.addLink(sw2, sw1_2_4, 7, 23)
        self.addLink(sw2, sw1_3_1, 8, 19)
        self.addLink(sw2, sw2_1, 9, 22)
        self.addLink(sw2, sw2_2, 10, 4)


topos = {'NAT': (lambda:NATopo())}
