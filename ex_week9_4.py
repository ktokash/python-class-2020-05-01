from my_devices import network_devices_nxos
from my_functions import open_napalm_connection
from my_functions import create_checkpoint
from my_functions import replace_config

connections = []

for device in network_devices_nxos:
    conn = open_napalm_connection(device)
    connections.append(conn)
    
# for each device, create checkpoint file
for device in connections:
    print("\n", "-" * 50, device.hostname)
    create_checkpoint(device)


# for each device, replace existing config with new one from file
for device in connections:
    print("\n", "-" * 50, device.hostname)
    replace_config(device)

