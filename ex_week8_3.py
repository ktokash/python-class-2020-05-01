import sys
from jnpr.junos import Device
#from getpass import getpass
from pprint import pprint
from jnpr_devices import srx2
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError


device = Device(**srx2)
device.open()

cfg = Config(device)
#cfg.lock()

print()
try:
    cfg.lock()
    print("Lock Acquired")
except LockError:
    print("Device is already locked.")


cfg.load("set system host-name python4life", format="set", merge=True)
print(cfg.diff())
cfg.rollback(0)
print(cfg.diff())

device.close()
