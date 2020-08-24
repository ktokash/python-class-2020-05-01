import os
import pyeapi
import yaml
from getpass import getpass
from yaml_funcs import yaml_load_devices, yaml_print_s_c_routes
from pprint import pprint

def main():
    pass_word = '88newclass'
    
    devices = yaml_load_devices()

    for name, device_dict in devices.items():
        device_dict["password"] = pass_word
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip route")
        pprint(output)
        route_output = output[0]['result']['vrfs']['default']['routes']
        yaml_print_s_c_routes(route_output)
        #pprint(route_output)
        #arp_output = output[0]['result']['ipV4Neighbors']
        #yaml_print(arp_output)
    
if __name__ == "__main__":
    main()
