import sys
from jnpr.junos import Device
from pprint import pprint
from jnpr_devices import srx2
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError
from jnpr.junos.op.routes import RouteTable

def gather_routes(device):
    routes = RouteTable(device)
    routes.get()
    return routes

def print_output(device):
    try:
        print()
        print(connected)
    except:
        print("Not connected or not checking")

    try:
        print()
        print("Route table is:")
        pprint(routes.items())
    except:
        print("Not checking route table")
        
    try:
        print()
        print("The ARP table is:")
        pprint(arps.items())
    except:
        print("Not checking ARP")


device = Device(**srx2)
device.open()
cfg = Config(device)
cfg.lock()

routes = gather_routes(device)
print("#" * 40, "\n", "Before changing route table:")
print_output(device)

cfg.load(path="static_routes.conf", format="text", merge=True)
cfg.commit()

routes = gather_routes(device)
print("#" * 40, "\n", "After changing route table:")
print_output(device)

cfg.load(path="delete_static_routes.set", format="set", merge=True)
cfg.commit()

print("#" * 40, "\n", "After rolling back route table change:")
routes = gather_routes(device)
print_output(device)

cfg.unlock()
device.close()
