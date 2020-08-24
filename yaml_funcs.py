import yaml

def yaml_load_devices(filename="ex_6_hosts.yaml"):
    with open(filename, "r") as f:
        return yaml.safe_load(f)
    raise ValueError("Reading YAML file failed")

def yaml_print(arp_output):
    entry_num = 1
    print()
    print('-' * 40)
    for arp_entry in arp_output:
        ip_addy = arp_entry['address']
        mac_addy = arp_entry['hwAddress']
        print("Entry", entry_num, "is", ip_addy, ":", mac_addy)
        entry_num += 1
    print('-' * 40)
    print()

def yaml_print_s_c_routes(route_output):
    print()
    print('-' * 40)
    # create a 'first layer' something (don't know what to call it) in loop
    # with variable 'prefix' because we have to drill inside a nested dict
    # data structure
    for prefix, route_entry in route_output.items():
        print()
        print("Prefix", prefix, "is", route_entry['routeType'])
        if route_entry['routeType'] == 'static':
            print(route_entry['routeType'], 'next hop is', route_entry['vias'][0]['nexthopAddr'])

    print('-' * 40)
    print()
