import json
import re
from pprint import pprint

with open("ex3-4.json", "r") as f:
    arp_data = json.load(f)

pprint(arp_data)

# initialize empty dict, just like you would an empty list
arp_dict = {}
# ipV4Neighbors is a key in the outer dict, the value is other dicts
arp_entries = arp_data["ipV4Neighbors"]

print()
print("arp_entries is: ")
pprint(arp_entries)
print()

# This is how to loop through a dictionary. Use the existing keys that Arista
# assigned. In this case start with "address"
for entry in arp_entries:
    # store the values for Arista's key "address" in variable called ip_addr
    ip_addr = entry['address']
    # repeat for MAC key and value
    mac_addr = entry['hwAddress']
    # store the mac_addr variable as the value, and the ip_addr var as the key
    # then iterate the loop
    arp_dict[ip_addr] = mac_addr

print()
pprint(arp_dict)
print()

