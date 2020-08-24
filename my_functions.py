from napalm import get_network_driver
from datetime import datetime

def open_napalm_connection(device):
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


def get_my_arp_table(device):
    my_device_arp = device.get_arp_table()
    return my_device_arp


def get_my_ntp_peers(device):
    try:
        my_device_ntp_peers = device.get_ntp_peers()
    except NotImplementedError:
        my_device_ntp_peers = ("get_ntp_peers not implemented in", device.platform)
    return my_device_ntp_peers


def create_backup(device):
    my_config = device.get_config(retrieve='running')
    my_config2 = my_config["running"]
    my_time = datetime.now()
    filename = f"{device.hostname}-{my_time}.txt"
    print("Backing up to:", filename)
    with open(filename, 'w') as f:
        f.write(my_config2)
    return my_config2

def create_candidate_confg(device):
    device.load_merge_candidate(filename="{}-loopbacks".format(device.hostname))
    print("*" * 30)
    print('diff for', device.hostname, 'after change:')
    diff = (device.compare_config())
    print(diff)
    device.discard_config()
    print('diff for', device.hostname, 'after discard:')
    diff = (device.compare_config())
    print(diff)
    if diff:
        device.commit_config()
    else:
        print("No changes committed")
    print('diff for', device.hostname, 'after empty commit:')
    diff = (device.compare_config())
    print(diff)
    device.load_merge_candidate(filename="{}-loopbacks".format(device.hostname))
    print('diff for', device.hostname, 'after change, second round:')
    diff = (device.compare_config())
    print(diff)
    if diff:
        device.commit_config()
    else:
        print("No changes committed")
    print('diff for', device.hostname, 'after commit, second round:')
    diff = (device.compare_config())

def create_checkpoint(device):
    device.open()
    checkpoint = device._get_checkpoint_file()
    #print(checkpoint)
    my_time = datetime.now()
    filename = f"{device.hostname}-checkpoint-{my_time}.txt"
    print("Backing up to:", filename)
    with open(filename, 'w') as f:
        f.write(checkpoint)
    device.close()

def replace_config(device):
    #device.load_replace_candidate(filename="{}-with-loops".format(device.hostname))
    device.load_replace_candidate(filename="nxos1.lasthop.io-with-loops")
    print("*" * 30)
    print('diff for', device.hostname, 'after change:')
    diff = (device.compare_config())
    print(diff)
'''    device.discard_config()
    print('diff for', device.hostname, 'after discard:')
    diff = (device.compare_config())
    print(diff)
'''
