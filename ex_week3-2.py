import re
import yaml
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

user_name = 'pyclass'
pass_word = 'fake_password'

device1 = {
    'device_name': 'cisco3',
    'host': 'cisco3.lasthop.io',
    'username': user_name,
    'password': pass_word,
    'device_type': 'cisco_ios'
}

device2 = {
    'device_name': 'cisco4',
    "host": 'cisco4.lasthop.io',
    'username': user_name,
    'password': pass_word,
    'device_type': 'cisco_ios'
}

device3 = {
    'device_name': 'nxos1',
    "host": 'nxos1.lasthop.io',
    'username': user_name,
    'password': pass_word,
    'device_type': 'cisco_ios'
}

device4 = {
    'device_name': 'nxos2',
    "host": 'nxos2.lasthop.io',
    'username': user_name,
    'password': pass_word,
    'device_type': 'cisco_ios'
}

devices = [device1, device2, device3, device4]

with open(r'yaml_out.yml', 'w') as file:
    documents = yaml.dump(devices, file)

