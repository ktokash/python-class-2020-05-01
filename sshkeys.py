#! /usr/bin/env python
# SSH keys

from netmiko import ConnectHandler

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'student1',
    "use_keys": True,
    "device_type": 'cisco_ios',
    "key_file": "/home/tokash/.ssh/student_key",
#    "session_log": 'my_session_dict.txt',
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
net_connect.disconnect()

