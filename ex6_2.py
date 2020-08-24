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

# Don't quite need, enable mode by default
#enable = getpass("Enable: ")
#device = pyeapi.client.Node(connection, enablepwd=enable)

# create new object called pyeapi.client.Node, pass in connection
device = pyeapi.client.Node(connection)
output = device.enable(["show version", "show ip arp"])
pprint(output)
print()
pprint(output[0])
print()

# the dict item we want is key 'result'
pprint(output[0]['result'])
print()
pprint(output[0]['result']['systemMacAddress'])

