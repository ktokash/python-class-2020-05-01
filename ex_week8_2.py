'''2b. Create a Python program that creates a PyEZ Device connection to "srx2" (using the previously created Python module). Using this PyEZ connection and the RouteTable and ArpTable views retrieve the routing table and the arp table for srx2.'''

import sys
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable
from lxml import etree
from jnpr.junos import Device
#from getpass import getpass
from pprint import pprint
from jnpr_devices import srx2

def check_connected(device):
    print("\n\n")
    if device.connected:
        print("device is connected")
        print("\n\n")
    else:
        print("device not connected")
        sys.exit(1)

def gather_routes(device):
    routes = RouteTable(device)
    routes.get()
    return routes

def gather_arp_table(device):
    arps = ArpTable(device)
    arps.get()
    return arps

def print_output(device):
    print(connected)

    print("Route table is:")
    pprint(routes.items())

    print("The ARP table is:")
    pprint(arps.items())


device = Device(**srx2)
device.open()

connected = check_connected(device)
routes = gather_routes(device)
arps = gather_arp_table(device)

print_output(device)

device.close()

