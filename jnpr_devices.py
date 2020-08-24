'''2a. Create a Python module named jnpr_devices.py. This Python module should contain a dictionary named "srx2". This "srx2" dictionary should contain all of the key-value pairs needed to establish a PyEZ connection. You should use getpass() for the password handling. You should import this "srx2" device definition for all of the remaining exercises in class8.'''

from getpass import getpass

srx2 = {
    'host': 'srx2.lasthop.io',
    'user': "pyclass",
    'password': '88newclass'
}

junos_devices = [srx2]

