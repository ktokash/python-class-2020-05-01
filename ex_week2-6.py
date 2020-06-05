from getpass import getpass
from netmiko import ConnectHandler
import time

# Use exact assigned variable and device dictionary:
password = '88newclass'
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

all_devices = [device]
for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    output = net_connect.find_prompt()
    print(output)
    net_connect.config_mode()
    output = net_connect.find_prompt()
    print(output)
    # can alternately skip find_prompt via
    # output = net_connect.config_mode()
    # though that also echoes 'config term'
    net_connect.exit_config_mode()
    output = net_connect.find_prompt()
    print(output)
    net_connect.write_channel('disable\n')
    output = net_connect.find_prompt()
    print(output)
    time.sleep(2)
    output = net_connect.read_channel()
    print(output)
    net_connect.enable()
    net_connect.enable()
    output = net_connect.find_prompt()
    print(output)

    


