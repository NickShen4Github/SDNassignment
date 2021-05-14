from mininet.topo import Topo 
from mininet.node import Node 
from mininet.net import Mininet 
from mininet.log import setLogLevel, info 
from mininet.cli import CLI 

class ATopo(Topo):
    def __init__(self): 
        Topo.__init__(self)

        info( '***Adding Building 1***')
###################################################
        info( '***Adding Ground Floor***')

        "Create reception topo."
        sw1_1 = self.addSwitch('sw1_1')
        h01_1= self.addHost('h01_1',ip='192.168.1.1/24')
        h01_2= self.addHost('h01_2',ip='192.168.1.2/24')
        "Create links."
        self.addLink(h01_1,sw1_1,1,1)
        self.addLink(h01_2,sw1_1,1,2)

        "Create 5 Offices topo."
        h02_1= self.addHost('h02_1',ip='192.168.2.1/24')
        h02_2= self.addHost('h02_2',ip='192.168.2.2/24')
        h02_3= self.addHost('h02_3',ip='192.168.2.3/24')
        h02_4= self.addHost('h02_4',ip='192.168.2.4/24')
        h02_5= self.addHost('h02_5',ip='192.168.2.5/24')
        "Create links."
        self.addLink(h02_1,sw1_1,1,3)
        self.addLink(h02_2,sw1_1,1,4)
        self.addLink(h02_3,sw1_1,1,5)
        self.addLink(h02_4,sw1_1,1,6)
        self.addLink(h02_5,sw1_1,1,7)

        "Create server room topo."
        sw0 = self.addSwitch('sw0')
        "Create simulated internet."
        sv0= self.addHost('sv0',ip='192.168.100.100/24')
        "Create SL server."
        sv5= self.addHost('sv5',ip='192.168.100.5/24')
        "Create 4 R&D server."
        sv1= self.addHost('sv1',ip='192.168.100.1/24')
        sv2= self.addHost('sv2',ip='192.168.100.2/24')
        sv3= self.addHost('sv3',ip='192.168.100.3/24')
        sv4= self.addHost('sv4',ip='192.168.100.4/24')
        "Create links."
        self.addLink(sv0,sw0,1,10)
        self.addLink(sv1,sw0,1,1)
        self.addLink(sv2,sw0,1,2)
        self.addLink(sv3,sw0,1,3)
        self.addLink(sv4,sw0,1,4)
        self.addLink(sv5,sw0,1,5)

###################################################
        info( '***Adding First Floor***')

        sw1_2 = self.addSwitch('sw1_2')

        "Create Lab topo."
        sw1_2_1 = self.addSwitch('sw1_2_1')
        for i in range(15):
            host = self.addHost('h11_%s' % (i+1), ip='192.168.3.%s/24' % (i+1))
        for l in range(15):
            self.addLink('h11_%s' % (l+1), sw1_2_1, 1, l+2)
 
        "Create 2 seminar topo."
        sw1_2_2 = self.addSwitch('sw1_2_2')
        sw1_2_2_1 = self.addSwitch('sw1_2_2_1')
        sw1_2_2_2 = self.addSwitch('sw1_2_2_2')
        self.addLink('sw1_2_2', 'sw1_2_2_1', 2, 1)
        self.addLink('sw1_2_2', 'sw1_2_2_2', 3, 1)

        ht1 = self.addHost('ht1', ip='192.168.4.1/24')
        ht2 = self.addHost('ht2', ip='192.168.5.1/24')
        self.addLink('ht1', 'sw1_2_2_1', 1, 23)
        self.addLink('ht2', 'sw1_2_2_2', 1, 23)

        #seminar1 192.168.6.0 seminar2 192.168.7.0
        for lab in range(2):
            for i in range(20):
                host = self.addHost('h1%s_%s' % ((lab+2),(i+1)), ip='192.168.%s.%s/24' % ((lab+6),(i+1)))
            for l in range(20):
                self.addLink('h1%s_%s' % ((lab+2),(l+1)), 'sw1_2_2_%s' %(lab+1), 1, l+2)

        "Create link for sw"
        self.addLink('sw1_2', 'sw1_2_1', 1, 1)
        self.addLink('sw1_2', 'sw1_2_2', 2, 1)

###################################################
        info( '***Adding Second Floor***')
        sw1_3 = self.addSwitch('sw1_3')

        "Create Prototyping lab topo."
        sw1_3_1 = self.addSwitch('sw1_3_1')
        for h in range(10):
            host = self.addHost('h21_%s' % (h + 1), ip='192.168.8.%s/24' % (h + 1))
        for l in range(10):
            self.addLink('h21_%s' % (l + 1), sw1_3_1, 1, l+2)

        "Create  6 offices  topo."
        sw1_3_2 = self.addSwitch('sw1_3_2')
        for h in range(6):
            host = self.addHost('h22_%s' % (h + 1), ip='192.168.9.%s/24' % (h + 1))
        for l in range(6):
            self.addLink('h22_%s' % (l + 1), sw1_3_2, 1, l+2)

        "Create Prototyping lab topo."
        sw1_3_3 = self.addSwitch('sw1_3_3')
        host = self.addHost('h23_1',  ip='192.168.10.1/24')
        self.addLink('h23_1', sw1_3_3, 1, 2)

        "Create link for sw"
        self.addLink('sw1_3', 'sw1_3_1', 1, 1)
        self.addLink('sw1_3', 'sw1_3_2', 2, 1)
        self.addLink('sw1_3', 'sw1_3_3', 3, 1)

###################################################
        "Create building2 topo."
        sw2_1 = self.addSwitch('sw2_1')
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
        self.addLink('hpc1', sw2_1, 1, 21)
        self.addLink('hpc2', sw2_1, 1, 22)

###################################################
        "Create major switch links topo."
        self.addLink(sw0, sw1_1, 100, 100)
        self.addLink(sw0, sw1_2, 101, 100)
        self.addLink(sw0, sw1_3, 102, 100)
        self.addLink(sw0, sw2_1, 103, 100)


topos = {'AT': (lambda:ATopo())}
