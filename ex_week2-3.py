from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device1 = {
    "host": 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': '88newclass',
    'device_type': 'cisco_ios',
}

device2 = {
    "host": 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password':  '88newclass',
    'device_type': 'cisco_ios',
}


all_devices = [device1, device2]

cmds = ["show version", "show lldp neighbors"]

for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    for cmd in cmds:
        output = net_connect.send_command(cmd, use_textfsm=True)
        print("\n", '-' * 80)
        print("Host: ", a_device['host'], "\t\t", "Command - ", cmd)
        print('-' * 80)
        pprint(output)

        if cmd == "show lldp neighbors":
            print("The port on the connected switch is: ", output[0]["neighbor_interface"])

