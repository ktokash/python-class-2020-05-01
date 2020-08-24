import os
from getpass import getpass

password = "88newclass"
username = "pyclass"
#password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

arista1 = {
    "host": "arista1.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "arista_eos",
}

arista2 = {
    "host": "arista2.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "arista_eos",
}

srx2 = {
    "host": "srx2.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "juniper_junos",
}

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "cisco_nxos",
    "optional_args": {"port": 8443},
}

# List of devices (only cisco3 and arista1)
network_devices = [cisco3, arista1, arista2, srx2]
network_devices_nxos = [nxos1]
