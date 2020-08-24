from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

pass_word = getpass()

nxos1 = {
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': pass_word,
    'device_type': 'cisco_ios',
}

nxos2 = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': pass_word,
    'device_type': 'cisco_ios',
}

all_devices = [nxos1, nxos2]
cmds = ["show version", "show lldp neighbors"]

for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    for cmd in cmds:
        output = net_connect.send_command(cmd, use_textfsm=True)
        #print(a_device[cmd])
        pprint(output)
