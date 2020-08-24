'''2a. Create a new file named "my_functions.py" that will store a set of reusable functions. Move the "open_napalm_connection" function from exercise1 into this Python file. Import the network devices once again from my_devices.py and create a list of connection objects (once again with connections to both cisco3 and arista1).'''

from my_devices import network_devices
from my_functions import open_napalm_connection
from my_functions import get_my_arp_table
from my_functions import get_my_ntp_peers
from my_functions import create_backup
from pprint import pprint

connections = []

# Use napalm to open connections to a list of devices, one at a time, store result
# in list
for device in network_devices:
    conn = open_napalm_connection(device)
    connections.append(conn)


# Print ARP table for each device in list
'''for device in connections:
    print("\n", "-" * 50, device.hostname)
    arp_table = get_my_arp_table(device)
    pprint(arp_table)


# Try to use get_ntp_peers() for each device in list
for device in connections:
    print("\n", "-" * 50, device.hostname)
    nyp_peer_table = get_my_ntp_peers(device)
    pprint(nyp_peer_table)
'''

# Back running configuration of each device up to a file local to the device

print("\n\n")

# Back running configuration of each device up to a file local to the device
for device in connections:
    print("\n", "-" * 50, device.hostname)
    running_conf = create_backup(device)
    #print(running_conf)
