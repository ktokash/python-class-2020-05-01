#! /usr/bin/env python

from netmiko import ConnectHandler, file_transfer
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "session_log": 'my_session_dict.txt',
}
source_file = "mychanges.txt"
# change name slightly to do a 'get' op and pull the file to local machine from router
#dest_file = "mychanges.txt"
dest_file = "mychanges2.txt"
# change direction from put to get
direction = "get"
file_system = "bootflash:"

# Create netmiko SSH session
ssh_conn = ConnectHandler(**device1)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,
)
print(transfer_dict)

# File transfer function has md5 check built in
# also if existing file with that name has same md5, it won't bother transferring
