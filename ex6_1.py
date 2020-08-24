import pyeapi
from pprint import pprint

device1 = pyeapi.connect_to("arista7")
device2 = pyeapi.connect_to("arista8")
print(device1)
#api_capabilities = dir(device1)
#pprint(api_capabilities)
print(device2.model)
