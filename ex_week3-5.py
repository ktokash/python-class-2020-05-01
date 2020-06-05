import re
import yaml
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

with open(r'/home/tokash/.netmiko.yml') as f:
    # yaml.safe_load limits this ability to simple Python 
    # objects like integers or lists.
    # https://pyyaml.org/wiki/PyYAMLDocumentation
    devices = yaml.safe_load(f)
    pprint(devices)

# Assign the dict entry you want to a var by calling 'dict_name["key"]'
cisco3 = devices['cisco3']
# From there just step through it via netconnect like it's your own dict
net_connect = ConnectHandler(**cisco3)

print()
print(net_connect.find_prompt())
print()

