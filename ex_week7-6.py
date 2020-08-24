'''6a. Create an nxapi_plumbing "Device" object for nxos1. The api_format should be "jsonrpc" and the transport should be "https" (port 8443). Use getpass() to capture the device's password. Send the "show interface Ethernet1/1" command to the device, parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500'''

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from getpass import getpass
from nxapi_plumbing import Device
from pprint import pprint

# just to handle self-signed cert warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password='88newclass',
    transport="https",
    port=8443,
    verify=False,
)

cmds = ["show interface Ethernet1/1"]
# call show_list method
output = device.show_list(cmds)
#pprint(output)
output = output[0]
#pprint(type(output_intf))
output_intf = (output["result"]['TABLE_interface']['ROW_interface']['interface'])
output_state = (output["result"]['TABLE_interface']['ROW_interface']
    ['state'])
output_mtu = (output["result"]['TABLE_interface']['ROW_interface']
    ['eth_mtu'])
print()
print("Interface:", output_intf, ';', "State:", output_state, ';', "MTU:", output_mtu)
#pprint(output_intf)
