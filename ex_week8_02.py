# get a running config
from ncclient import manager
from getpass import getpass
from pprint import pprint
#
from ncclient.xml_ import new_ele

# assigning var name more traditionally this time
conn = manager.connect(
    host="srx2.lasthop.io",
    port=830,
    timeout=60,
    username="pyclass",
    password=getpass(),
    device_params={"name": "junos"},
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False,
# Create the variable "netconf_manager" as an object with this dict stuffed in it
)

# Create var, store in it the results of calling the get_config function on "conn",
# which we created above, and pass in the "source" option
config = conn.get_config(source="running")
# Convert the received data to XML via the .data_xml function
config_xml = config.data_xml
pprint(config_xml)
