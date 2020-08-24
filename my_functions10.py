from netmiko import ConnectHandler
from my_devices10 import network_devices
from datetime import datetime

def ssh_conn(device, command):
    if device == 'arista1' or device == 'arista2':
        net_connect = ConnectHandler(**device, global_delay_factor=4)
    else:
        net_connect = ConnectHandler(**device)
    output = net_connect.send_command_expect(command)
    net_connect.disconnect()
    return output

def print_show(device, command):
    for device in network_devices:
        start_time = datetime.now()
        result = ssh_conn(device, command)
        print("\n\n", "-" * 30)
        print(result)
        end_time = datetime.now()
        print("Start time was:", start_time)
        print("End time was:", end_time)
        print("Elapsed time was:", (end_time - start_time))

def print_show_no_loop(device, command):
    start_time = datetime.now()
    result = ssh_conn(device, command)
    print("\n\n", "-" * 30)
    print(result)
    end_time = datetime.now()
    print("Start time was:", start_time)
    print("End time was:", end_time)
    print("Elapsed time was:", (end_time - start_time))

def ssh_conn2(device):
    net_connect = ConnectHandler(**device)
    return net_connect.send_command_expect("show version")

def ssh_show_arp(device):
    net_connect = ConnectHandler(**device)
    if device == 'srx2':
        return net_connect.send_command_expect("show arp")
    else:
        return net_connect.send_command_expect("show ip arp")

def ssh_command2(device, command):
    """Establish an SSH connection. Execute show command, return results."""
    device = ConnectHandler(**device)
    output = device.send_command(command)
    device.disconnect()
    return output
