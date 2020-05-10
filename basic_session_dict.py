# 02 Netmiko send commands

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "session_log": 'my_session_dict.txt',
}

# ** Star star arguments pass in every variable
net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

#output = net_connect.send_command("show ip int brief")
output = net_connect.send_command("show ip int brief", use_textfsm=True)
var_type=type(output)
print(var_type)
print(output)

net_connect.disconnect()

# 88newclass

