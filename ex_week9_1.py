'''1a. Create a Python file named "my_devices.py" that defines the NAPALM connection information for both the 'cisco3' device and the 'arista1' device. Use getpass() for the password handling. This Python module should be used to store the device connection information for all of the exercises in this lesson.

1b. Create a simple function that accepts the NAPALM device information from the my_devices.py file and creates a NAPALM connection object. This function should open the NAPALM connection to the device and should return the NAPALM connection object.'''

# Import list of each device we create a dict for in our file
from my_devices import network_devices
from napalm import get_network_driver
from pprint import pprint

# Create function that opens a device and stores
# 
def open_connect(device):
    # use .copy instead of 'my_device = device' to avoid modifying original
    my_device = device.copy()
    # cut out the specified dict key, placing the value into a variable
    device_type = my_device.pop("device_type")
    # call net_network_driver function, pass in var we just created, store
    # result in a new var
    driver = get_network_driver(device_type)
    # since 'driver' is the result of running get_network_type on the particular
    # machine currently stored in 'my_device' (so the current iteration in a list)
    # we cycle "get_network_driver on ios" through the entire dict that represents
    # the device 'cisco3', storing the resulting dict-like data structure in 'conn'
    conn = driver(**my_device)
    conn.open()
    # return this dict-like data structure so we can append it to a list that we
    # can then plumb at will
    return conn

'''1c. Using your "my_devices.py" file and your NAPALM connection function, create a list of NAPALM connection objects to 'cisco3' and 'arista1'.'''

# Create an empty list to store the return values of the open_connect function
connections = []

'''1d. Iterate through the connection objects, print out the device's connection object itself. Additionally, pretty print the facts for each device and also print out the device's NAPALM platform type (ios, eos, et cetera).'''

# Create a for loop, cycling through each machine in the network_device list
# we imported from the my_devices file
for device in network_devices:
    # can't just call the function because it returns a value - in this case
    # a dict-like data structure for one device at a time
    # open_connect(device)
    #
    # Need to call the function while assigning current iteration to a var
    conn = open_connect(device)
    print(type(conn))
    # stuff that data structure into a list
    connections.append(conn)


print("\n\n>>>Print facts for each device in my_devices.py")
print("-" * 30)

# Another for loop to print out the data we want from every device in the
# 'connections' list
 
for conn in connections:
    print(conn.hostname)
    pprint("{} facts:".format(conn.platform))
    # returns "'eos facts:'"
    #
    # Can finally call .get_facts() on something. Must call it on the entire data
    # structure returned by get_network_driver (<class 'napalm.ios.ios.IOSDriver'>
    # <class 'napalm.eos.eos.EOSDriver'>, etc
    pprint(conn.get_facts())
    print("\n\n")
    conn.close()
