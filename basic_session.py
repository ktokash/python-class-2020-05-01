#01 Netmiko Overview

from netmiko import ConnectHandler
from getpass import getpass

#In [8]: net_connect = ConnectHandler(host='cisco1.lasthop.io', username='pyclass', password=
#   ...: getpass(), device_type='cisco_ios') 

net_connect = ConnectHandler(
    host='cisco3.lasthop.io',
    username='pyclass',
    password=getpass(),
    device_type='cisco_ios',
    session_log='my_session.txt',
)

print(net_connect.find_prompt())
