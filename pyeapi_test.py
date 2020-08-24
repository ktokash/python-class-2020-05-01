import pyeapi
from getpass import getpass
# import python debugger with fun happy coloring
import ipdb

ipdb.set_trace()
connection = pyeapi.client.connect(
    transport="https",
    host="arista8.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

#enable = getpass("Enable: ")
#device = pyeapi.client.Node(connection, enablepwd=enable)

# create new object called pyeapi.client.Node, pass in connection
device = pyeapi.client.Node(connection)
