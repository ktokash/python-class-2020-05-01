#!/usr/bin/env python

import re
import yaml
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from ciscoconfparse import CiscoConfParse

with open(r'/home/tokash/.netmiko.yml') as f:
    # yaml.safe_load limits this ability to simple Python 
    # objects like integers or lists.
    # https://pyyaml.org/wiki/PyYAMLDocumentation
    devices = yaml.safe_load(f)
    #pprint(devices)

# Assign the dict entry you want to a var by calling 'dict_name["key"]'
cisco4 = devices['cisco4']
# From there just step through it via netconnect like it's your own dict
net_connect = ConnectHandler(**cisco4)

''' Test print, then comment out and store output in list
print()
print(net_connect.send_command('show run'))
print()'''

show_run = net_connect.send_command('show run')
show_run = show_run.splitlines()
# pprint(show_run)

parse = CiscoConfParse(show_run)

# search 'parse' for interfaces, store entire object
has_ip = parse.find_objects_w_child(parentspec=r'^interface', childspec=r"^\s+ip address")

for intf in has_ip:
    print()
    print("Interface Line: ", intf.text)
    # This errors, 'IOSCfgLine' object does not support indexing
    #intf_ip = intf[0].re_search_children(r'^\s+ip address').text
    intf_ip = intf.re_search_children(r'^\s+ip address')[0].text
    print("IP Address Line: ", intf_ip)
    
'''(py3_venv) [tokash@pylab21a python-class-2020-05-01]$ python ex_week3-6.py

Interface Line:  interface Loopback0
IP Address Line:   ip address 1.1.1.1 255.255.255.255

Interface Line:  interface GigabitEthernet0/0/0
IP Address Line:   ip address 10.220.88.23 255.255.255.0
(py3_venv) [tokash@pylab21a python-class-2020-05-01]$ '''
