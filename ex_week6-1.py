import pyeapi
from getpass import getpass
from pprint import pprint

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    #88newclass
    password='88newclass',
    port="443",
)

device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")
arp_output = output[0]['result']['ipV4Neighbors']
#pprint(arp_output)
entry_num = 1
print()

for arp_entry in arp_output:
    ip_addy = arp_entry['address']
    mac_addy = arp_entry['hwAddress']
    print("Entry", entry_num, "is", ip_addy, ":", mac_addy)
    entry_num += 1


'''pprint(output)
print()
pprint(output[0])
print()
pprint(output[0]['result']['ipV4Neighbors'][0]['address'])
pprint(output[0]['result']['ipV4Neighbors'][0]['hwAddress'])
'''
