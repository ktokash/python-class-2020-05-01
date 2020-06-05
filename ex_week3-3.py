import json
from pprint import pprint

with open('ex3-3.json') as f:
    nxos_data = json.load(f)

pprint(nxos_data)
print()

# initialize empty lists
ipv4_list = []
ipv6_list = []

# first loop - outer dict of interface + a dict with IP info in it
# "ipaddr_dict" = name of inner dict
for intf, ipaddr_dict in nxos_data.items():
    # second loop - dict with IP info = the v4 or v6 label + a dict with
    # the actual address and another dict. "addr_info" = name of next dict
    for ipv4_or_ipv6, addr_info in ipaddr_dict.items():
        # 3rd loop - actual address, then another dict with 'prefix_length'
        # as key, and a value. "prefix_dict" = next dict
        for ip_addr, prefix_dict in addr_info.items():
            # start peeling it back layer by layer
            # {'prefix_length': 16}
            prefix_length = prefix_dict['prefix_length']
            # you could match on ip_addr here, but you'd need to use a regex
            # to match the formatting. Instead just use the tag they provide
            if ipv4_or_ipv6 == 'ipv4':
                ipv4_list.append("{}/{}".format(ip_addr, prefix_length))
                #ipv4_list.append("".format(ip_addr, prefix_length))
            if ipv4_or_ipv6 == 'ipv6':
                ipv6_list.append("{}/{}".format(ip_addr, prefix_length))

print("\nIPv4 Addresses: {}\n".format(ipv4_list))
print("\nIPv6 Addresses: {}\n".format(ipv6_list))
