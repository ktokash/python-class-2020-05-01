import re
from pprint import pprint

arp_data = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

# read string in, strip the leading whitespace(?) that somehow
# creates an empty list element during conversion from str->list
# pprint won't work on the string
arp_strip = arp_data.strip()
print()
print("arp_strip: ", arp_strip)
arp_strip_type = type(arp_strip)
print(arp_strip_type)
# now have nearly identical string as before

# .splitlines is a method that splits a string into a list, with
# each line as a list item
arp_list = arp_strip.splitlines()
arp_list_type = type(arp_list)
print()
print("arp_list: ")

pprint(arp_list)
print(arp_list_type)

# create an empty list to fill with desired, filtered output
processed_list = []
for arp_entry in arp_list:
    # use the .search primitive operation to make sure you have
    # the top line of output
    if re.search(r"^Protocol.*Interface", arp_entry):
        # This prints just the header line
        # print("arp_entry is ", arp_entry)
        continue
    # Confusing bit, took a while. The underscores are placeholders
    # telling python 'something is there, don't bother naming and
    # storing it.' The named bits become variables.
    _, ip_addr, _, mac_addr, _, intf = arp_entry.split()
    # MUST assign at end, or get SyntaxError: can't assign to function call
    #arp_entry.split() = _, ip_addr, _, mac_addr, _, intf
    #test = arp_entry.split()
    #print(test)
    #arp_entry_len = len(test)
    #print(arp_entry_len)
    # These print statements cycle through each line, printing var
    #print(ip_addr)
    #print(mac_addr)
    #print(intf)
    # Loop through each line in arp_entry, creating a dict with the stored
    # values:
    arp_dict = {"ip_addr":ip_addr, "mac_addr":mac_addr, "interface":intf} 
    # Now stuff the current dict into a list as an element
    processed_list.append(arp_dict)

print()
pprint(processed_list)
print()
