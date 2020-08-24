'''1a. Create a PyEZ Device object from the jnpr.junos Device class. This device object should connect to "srx2.lasthop.io". Use getpass() to enter the device's password. Pretty print all of the device's facts. Additionally, retrieve and print only the "hostname" fact.'''

from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

a_device = Device(host='srx2.lasthop.io', user="pyclass", password='88newclass')
a_device.open
pprint(a_device.facts)
print()
print(type(a_device.facts))
print()
print(a_device.facts['hostname'])
print(a_device.facts['ifd_style'])

