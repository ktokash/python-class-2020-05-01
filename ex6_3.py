import pyeapi
from getpass import getpass
from pprint import pprint

connection = pyeapi.client.connect(
    transport="https",
    host="arista8.lasthop.io",
    username="pyclass",
    #88newclass
    password=getpass(),
    port="443",
)

# NEW SECTION HERE
cfg = [
    "vlan 225",
    "name green",
    "vlan 226",
    "name red",
]

# create new object called pyeapi.client.Node, pass in connection
device = pyeapi.client.Node(connection)
# Go from .enable to .config, pass cfg list in
output = device.config(cfg)

pprint(output)
