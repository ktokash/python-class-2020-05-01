from my_devices import network_devices
from my_functions import open_napalm_connection
from my_functions import create_candidate_confg

from pprint import pprint

connections = []

for device in network_devices:
    conn = open_napalm_connection(device)
    connections.append(conn)

# for each device, take input file and load into candidate configuration
# print out diff

for device in connections:
    print("\n", "-" * 50, device.hostname)
    candidate_confg = create_candidate_confg(device)
