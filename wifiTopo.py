#!/usr/bin/python

from mininet.node import Controller, OVSKernelSwitch
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import Station, OVSKernelAP
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd#, mesh
from mn_wifi.wmediumdConnector import interference
from subprocess import call


def myNetwork():

    net = Mininet_wifi(topo=None,
                       build=False,
                       link=wmediumd,
                       wmediumd_mode=interference,
                       ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0 = net.addController(name='c0',
                           controller=Controller,
                           protocol='tcp',
                           port=6633)

    info( '*** Add switches/APs\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid',
                             channel='1', mode='g', passwd = 'SDN123456', encrypt = 'wpa2', position='350.0,150.0,0')
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid',
                             channel='1', mode='g', passwd = 'SDN123456', encrypt = 'wpa2', position='350.0,250.0,0')
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid',
                             channel='1', mode='g', passwd = 'SDN123456', encrypt = 'wpa2', position='350.0,350.0,0')
    ap4 = net.addAccessPoint('ap4', cls=OVSKernelAP, ssid='ap4-ssid',
                             channel='1', mode='g', passwd = 'SDN123456', encrypt = 'wpa2', position='550.0,250.0,0')

    info( '*** Add hosts/stations\n')
    sta2 = net.addStation('sta2', passwd = 'SDN123456', encrypt = 'wpa2', ip='10.0.0.2',
                           position='350.0,50.0,0')
    sta1 = net.addStation('sta1', passwd = 'SDN123456', encrypt = 'wpa2', ip='10.0.0.1',
                           position='320.0,60.0,0')

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info( '*** Add links\n')
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    #net.addLink(ap1, intf='ap1-wlan2', cls=mesh, ssid='mesh-ssid', channel=5)
    #net.addLink(ap2, intf='ap2-wlan2', cls=mesh, ssid='mesh-ssid', channel=5)
    #net.addLink(ap3, intf='ap3-wlan2', cls=mesh, ssid='mesh-ssid', channel=5)
    #net.addLink(ap4, intf='ap4-wlan2', cls=mesh, ssid='mesh-ssid', channel=5)
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    net.addLink(ap1, ap4)
    net.addLink(s1, ap1)

    net.plotGraph(max_x=1000, max_y=1000)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches/APs\n')
    net.get('s1').start([c0])
    net.get('ap3').start([c0])
    net.get('ap2').start([c0])
    net.get('ap1').start([c0])
    net.get('ap4').start([c0])

    info( '*** Post configure nodes\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

