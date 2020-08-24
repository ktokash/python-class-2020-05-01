import pyeapi
from getpass import getpass
from pprint import pprint

connection = pyeapi.client.connect(
    transport="https",
    host="arista8.lasthop.io",
    username="pyclass",
    #88newclass
    password='88newclass',
    port="443",
)

# NEW SECTION HERE
enable = getpass("Enable: ")
# set up eapi node
device = pyeapi.client.Node(connection, enablepwd=enable)

# take 'device' object, call .api function, pass one of the subsystems available to api
vlan_cfg = device.api("vlans")
print(vlan_cfg)
print()
all_vlans = vlan_cfg.get
print(all_vlans)
