#!/usr/bin/python
import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch, OVSBridge
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call


def setTos():
    switch_hub = ['sw1','sw1_1','sw1_2','sw1_3','sw2_1']
#nw_tos0x10 is intranet, nw_tos0x20 is internet, nw_tos0x30 is R&D server access, nw_tos0x40 is other server access
# qos setting is by blacklist the flow that are not allowed
##########not allow for intranet##########
#5 office + 15 SL + 2*20 Lab PC + Proto Lab 10 PC + 6 Office
    for h in range(21,26):
        for switch in switch_hub:
            os.system('sudo ovs-ofctl -O OpenFlow13 add-flow %s ip,nw_src=172.16.1.%d,nw_tos=0x10,action=drop'%(switch,h))

    for h in range(11,26):
        for switch in switch_hub:
            os.system('sudo ovs-ofctl -O OpenFlow13 add-flow %s ip,nw_src=172.16.3.%d,nw_tos=0x10,action=drop'%(switch,h))

    for h in range(11,31):
        for switch in switch_hub:
            os.system('sudo ovs-ofctl -O OpenFlow13 add-flow %s ip,nw_src=172.16.2.%d,nw_tos=0x10,action=drop'%(switch,h))

    for h in range(41,61):
        for switch in switch_hub:
            os.system('sudo ovs-ofctl -O OpenFlow13 add-flow %s ip,nw_src=172.16.2.%d,nw_tos=0x10,action=drop'%(switch,h))

    for h in range(31,41):
        for switch in switch_hub:
            os.system('sudo ovs-ofctl -O OpenFlow13 add-flow %s ip,nw_src=172.16.2.%d,nw_tos=0x10,action=drop'%(switch,h))

    for h in range(41,47):
        for switch in switch_hub:
            os.system('sudo ovs-ofctl -O OpenFlow13 add-flow %s ip,nw_src=172.16.2.%d,nw_tos=0x10,action=drop'%(switch,h))
##########not allow for internet##########
#2 reception + demonstration room + 2 hpc
    for h in range(11,13):
        for switch in switch_hub:
            os.system('sudo ovs-ofctl -O OpenFlow13 add-flow %s ip,nw_src=172.16.1.%d,nw_tos=0x20,action=drop'%(switch,h))

    for switch in switch_hub:
        os.system('sudo ovs-ofctl -O OpenFlow13 add-flow %s ip,nw_src=172.16.3.51,nw_tos=0x20,action=drop'%switch)

    for h in range(31,33):
        for switch in switch_hub:
            os.system('sudo ovs-ofctl -O OpenFlow13 add-flow %s ip,nw_src=172.16.4.%d,nw_tos=0x20,action=drop'%(switch,h))
##########allow for 4 server##########
#10 proto lab + 1 management office + server drop 
    for h in range(31,42):
        os.system('sudo ovs-ofctl -O OpenFlow13 add-flow sw1 ip,nw_src=172.16.3.%d,nw_tos=0x30,action=output=1'%h)

    for h in range(31,42):
        os.system('sudo ovs-ofctl -O OpenFlow13 add-flow sw1 ip,nw_dst=172.16.3.%d,nw_tos=0x30,action=output=3'%h)

    for h in range(11,27):
        for switch in switch_hub:
            os.system('sudo ovs-ofctl -O OpenFlow13 add-flow %s ip,nw_src=172.16.1.%d,nw_tos=0x30,action=drop'%(switch,h))

##########allow for 1 special server##########
#10 proto lab + 1 management office + building2 + server drop
    for h in range(31,42):
        os.system('sudo ovs-ofctl -O OpenFlow13 add-flow sw1 ip,nw_src=172.16.3.%d,nw_tos=0x40,action=output=1'%h)

    for h in range(31,42):
        os.system('sudo ovs-ofctl -O OpenFlow13 add-flow sw1 ip,nw_dst=172.16.3.%d,nw_tos=0x40,action=output=3'%h)

    for h in range(11,33):
        os.system('sudo ovs-ofctl -O OpenFlow13 add-flow sw1 ip,nw_src=172.16.4.%d,nw_tos=0x40,action=output=1'%h)

    for h in range(11,33):
        os.system('sudo ovs-ofctl -O OpenFlow13 add-flow sw1 ip,nw_dst=172.16.4.%d,nw_tos=0x40,action=output=4'%h)

    for h in range(11,27):
        for switch in switch_hub:
            os.system('sudo ovs-ofctl -O OpenFlow13 add-flow %s ip,nw_src=172.16.1.%d,nw_tos=0x40,action=drop'%(switch,h))
if __name__ == '__main__':
    setLogLevel( 'info' )
    setTos()
