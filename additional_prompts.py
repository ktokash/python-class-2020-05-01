# Week 2 - more netmiko
# some commands don't terminate gracefully. Deleting commands on flash
# 88newclass

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "session_log": 'log_additional.txt',
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = 'delete flash:/cisco_file.txt'
output = net_connect.send_command(command, expect_string=r'\[cisco_file.txt\]')
output = net_connect.send_command("\n", expect_string=r'\[confirm\]')
output += net_connect.send_command('y', expect_string=r'#')

print(output)

