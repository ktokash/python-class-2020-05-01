'''Use Netmiko and the send_config_set() method to configure the following on the Cisco3 router.

ip name-server 1.1.1.1
ip name-server 1.0.0.1
ip domain-lookup'''

from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

device1 = {
    "host": "cisco3.lasthop.io",
    'username': 'pyclass',
    'password': getpass(),
    "session_log": 'my_session_send.txt',
    'fast_cli': True,
    'device_type': 'cisco_ios'
}

all_devices = [device1]
cmds = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']

for a_device in all_devices:
    start_time = datetime.now()
    net_connect = ConnectHandler(**a_device)
    for cmd in cmds:
        output = net_connect.send_config_set(cmd)
        print(net_connect.find_prompt())
        print(output)
    end_time = datetime.now()
    net_connect.disconnect()
    time_elapsed = end_time - start_time
    print("Time elapsed: ", time_elapsed)




'''cisco3 (Cisco IOS-XE)
    hostname = cisco3.lasthop.io
    snmp_port = 161
    ssh_port = 22
    username = pyclass
    password = 88newclass'''

