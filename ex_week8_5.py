from jnpr.junos import Device
from pprint import pprint
from jnpr_devices import srx2
from lxml import etree

def get_version(device):
    routes = RouteTable(device)
    routes.get()
    return routes

device = Device(**srx2)
device.open()

'''
https://github.com/Juniper/py-junos-eznc/blob/master/lib/jnpr/junos/facts/get_software_information.py
'''

xml_out = device.rpc.get_software_information()
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))

xml_out_intf = device.rpc.get_interface_information(terse=True, interface_name='fe-0/0/7', normalize=True)
print(etree.tostring(xml_out_intf, pretty_print=True, encoding="unicode"))

