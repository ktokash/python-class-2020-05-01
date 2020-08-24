from pprint import pprint
from getpass import getpass
from napalm import get_network_driver
# SSL Warning suppression
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
password = "88newclass"

cisco3 = dict(
    hostname="cisco3.lasthop.io",
    device_type="ios",
    username="pyclass",
    password=password,
    optional_args={},
)
nxos1 = dict(
    hostname="nxos1.lasthop.io",
    device_type="nxos",
    username="pyclass",
    password=password,
    optional_args={'port': 8443},
)
eos1 = dict(
    hostname="arista1.lasthop.io",
    device_type="eos",
    username="pyclass",
    password=password,
)

my_device = eos1
device_type = my_device.pop("device_type")
driver = get_network_driver(device_type)
device = driver(**my_device)

print()
print("\n\n>>>Test device open")
device.open()
print(device)

print()
output1 = device.get_facts()
output2 = device.get_interfaces()
output3 = device.get_lldp_neighbors()
pprint(output1)
pprint(output2)
pprint(output3)
print()
