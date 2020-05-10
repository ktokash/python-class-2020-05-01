# Week 2 - changing configs via netmiko. Use:
# net_connect.send_config_set(VARIABLE)

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

# send string
# cfg = 'logging buffered 20000'

# send list
#cfg = [
#    'logging buffered 10000',
#    'clock timezone PST -7 0'
#]
#output = net_connect.send_config_set(cfg)

# Call bunch of commands in separate file via send_config_from_file
# create mychanges.txt

output = net_connect.send_config_from_file(config_file='mychanges.txt')
print(output)

save_out = net_connect.save_config()

net_connect.disconnect()

# 88newclass



