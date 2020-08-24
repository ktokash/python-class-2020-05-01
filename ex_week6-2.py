#2a. Define an Arista device in an external YAML file (use arista4.lasthop.io for the device). In your YAML file, make sure the key names exactly match the names required for use with pyeapi and the connect() method. In other words, you should be able to execute 'connect(**device_dict)' where device_dict was retrieved from your YAML file. Do not store the lab password in this YAML file, instead set the password using getpass() in your Python program. Using this Arista device information stored in a YAML file, repeat the 'show ip arp' retrieval using pyeapi. Once again, from this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.


import os
import pyeapi
import yaml
from getpass import getpass
from pprint import pprint

pass_word = '88newclass'

# create function to open a specific file, pass filename in as parameter
# The function yaml.safe_load limits the ability to construct objects from
# yaml files to simple Python objects like integers or lists.
def yaml_load_devices(filename="ex_6_hosts.yaml"):
    with open(filename, "r") as f:
        return yaml.safe_load(f)
    raise ValueError("Reading YAML file failed")

'''
This is the way I found online to open a yaml file to work with
with open('ex_6_hosts.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
'''

# wrapping main functionality in a function called main
def main():

    # call yaml_load_devices function to create list
    devices = yaml_load_devices()
    # file_type = type(devices)
    # print("devices var is type ", file_type)
    # devices var is type  <class 'function'>
    
    # if there's a global(?) var named PYNET_PASSWORD, use that, otherwise
    # use getpass
    #password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
    entry_num = 1

    # loop through devices (which is "class 'function'"). The '.items' method
    # is built in, and returns a 'view object,' which is the key-value pair in
    # a dict, as tuples in a list
    # So here we're creating a list of tuples and looping through it
    for name, device_dict in devices.items():
        # since the yaml file is nested, 'name' is the first layer
        # device_dict is the inside dict
        device_dict["password"] = pass_word
        # create a variable holding the result of stepping through the inside dict
        connection = pyeapi.client.connect(**device_dict)
        # create new object called pyeapi.client.Node, pass in connection
        device = pyeapi.client.Node(connection)
        # call the .enable function to execute show cmds on 'device'
        output = device.enable("show ip arp")

        print()
        print('-' * 40)
        arp_output = output[0]['result']['ipV4Neighbors']
        for arp_entry in arp_output:
            ip_addy = arp_entry['address']
            mac_addy = arp_entry['hwAddress']
            print("Entry", entry_num, "is", ip_addy, ":", mac_addy)
            entry_num += 1
        print('-' * 40)
        print()


# actually call main() to execute the program, unless some other program
# has called this one
if __name__ == "__main__":
    main()


