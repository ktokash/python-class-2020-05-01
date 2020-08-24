import os
import pyeapi
import yaml
from getpass import getpass
from pprint import pprint

def yaml_load_devices(filename="ex_6_hosts.yaml"):
    with open(filename, "r") as f:
        return yaml.safe_load(f)
    raise ValueError("Reading YAML file failed")

def yaml_print(arp_output):
    entry_num = 1
    print()
    print('-' * 40)
    for arp_entry in arp_output:
        ip_addy = arp_entry['address']
        mac_addy = arp_entry['hwAddress']
        print("Entry", entry_num, "is", ip_addy, ":", mac_addy)
        entry_num += 1
    print('-' * 40)
    print()

def main():
    pass_word = '88newclass'
    
    devices = yaml_load_devices()

    for name, device_dict in devices.items():
        device_dict["password"] = pass_word
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip arp")
        arp_output = output[0]['result']['ipV4Neighbors']
        yaml_print(arp_output)        

if __name__ == "__main__":
    main()
