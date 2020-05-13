# Use the extended 'ping' command and Netmiko on the 'cisco4' router.
"""a. Use send_command_timing() to handle the additional prompting from this 'ping' command. Specify a target IP address of '8.8.8.8'

b. Use send_command() and the expect_string argument to handle the additional prompting. Once again specify a target IP address of '8.8.8.8'."""

# find device type syntax:
# >>> from netmiko import ConnectHandler
# >>> net_connect = ConnectHandler(device_type='whatever')

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_xe",
    "session_log": "ex_week2-1.txt"
}

all_devices = [device1]

for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command("ping", expect_string=r'\[ip\]:')
    output += net_connect.send_command("\n", expect_string=r'address:')
    output += net_connect.send_command("8.8.8.8", expect_string=r'\[5\]:')
    output += net_connect.send_command("\n", expect_string=r'\[100\]:')
    output += net_connect.send_command("\n", expect_string=r'\[2\]:')
    output += net_connect.send_command("\n", expect_string=r'\[n\]:')
    output += net_connect.send_command("\n", expect_string=r'\[n\]:')
    output += net_connect.send_command("\n", expect_string=r'Success')
    output += net_connect.send_command("\n")
    print(output)

