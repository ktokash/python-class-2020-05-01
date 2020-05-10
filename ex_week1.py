#! /usr/bin/env python

''' Simply print the router prompt back from this device to verify you are connecting to the device properly.

 Add a second NX-OS device to your first exercise. Make sure you are using dictionaries to represent the two NX-OS devices. Additionally, use a for-loop to accomplish the Netmiko connection creation.
 
 retrieve 'show version'. Save this output to a file in the current working directory.'''

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

# Create a dictionary for every device
device1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    "session_log": 'nxos1.txt'
}

device2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_nxos',
    "session_log": 'nxos2.txt'
}

# Create a list that includes every device dictionary
all_devices = [device1, device2]

# Create a for loop that calls the list you just created, and cycles
# through every element (device dictionary) in the list

for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command("show version")
    print("\nDevice: ", net_connect.find_prompt(), "-" * 20)
    print(f"Device Type: {a_device['device_type']}", "-" * 20)
    print(output)




'''nxos1 (NX-OSv Switch)
    hostname = nxos1.lasthop.io
    ssh_port = 22
    nxapi_port = 8443
    username = pyclass
    password = 88newclass

nxos2 (NX-OSv Switch)
    hostname = nxos2.lasthop.io
    ssh_port = 22
    nxapi_port = 8443
    username = pyclass
    password = 88newclass
'''
