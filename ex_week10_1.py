from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from netmiko import ConnectHandler
from my_devices10 import network_devices
import re

start_time = datetime.now()

cmd = "show version"

def ssh_conn(device, command):
    if device == 'arista1' or device == 'arista2':
        net_connect = ConnectHandler(**device, global_delay_factor=4)
    else:
        net_connect = ConnectHandler(**device)
    output = net_connect.send_command_expect(command)
    net_connect.disconnect()
    return output

connections = []

for device in network_devices:
    result = ssh_conn(device, cmd)
    print("\n\n", "-" * 30)
    print(result)


end_time = datetime.now()
print("Start time was:", start_time)
print("End time was:", end_time)
print("Elapsed time was:", (end_time - start_time))
