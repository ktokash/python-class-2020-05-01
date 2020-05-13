'''Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2. Execute 'show lldp neighbors detail' and print the returned output to standard output. Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8. Print the output of this command to standard output. Use the Python datetime library to record the execution time of both of these commands. Print these execution times to standard output.'''

#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device1 = {
    "host": "nxos2.lasthop.io",
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
    'session_log': 'ex_week2-2.txt',
    'global_delay_factor': 2,
}

all_devices = [device1]

for a_device in all_devices:
    start_time1 = datetime.now()
    net_connect = ConnectHandler(**a_device)
    output1 = net_connect.send_command('show lldp nei det')
    end_time1 = datetime.now()
    print("\n", "-" * 20, "\n", output1)
    start_time2 = datetime.now()
    output2 = net_connect.send_command('show lldp nei det', delay_factor=8)
    end_time2 = datetime.now()
    print("\n", "-" * 20, "\n", output2)

print("global_delay_factor of 2 took this long: ", end_time1 - start_time1)
print("delay_factor of 8 took this long: ", end_time2 - start_time2)

print("global_delay_factor of 2 took this long: {}".format(end_time1 - start_time1))
print("delay_factor of 8 took this long: {}".format(end_time2 - start_time2))



'''nxos2 (NX-OSv Switch)
    hostname = nxos2.lasthop.io
    ssh_port = 22
    nxapi_port = 8443
    username = pyclass
    password = 88newclass'''
