from pprint import pprint
from ciscoconfparse import CiscoConfParse

with open(r'ex3-6.txt') as f:
    bgp_nei = f.read()

print(bgp_nei)
bgp_nei = bgp_nei.splitlines()
pprint(bgp_nei)

bgp_nei = CiscoConfParse(bgp_nei)

# Result of find_objects_w_parents will be the child objects
# initialize an empty list, will .append neighbor IPs and ASNs
bgp_peers = []

# read in the BGP config that you used .splitlines on and stored in bgp_nei
# use find_objects_w_parents, and define parent as having string 'router bgp'
# then define child as having string 'neighbor'
neighbors = bgp_nei.find_objects_w_parents(
    parentspec=r"router bgp", childspec=r"neighbor"
)

# create FOR loop, looping through 'neighbors,' which is the two neighbors
# in the BGP config snippet, plus all their child lines
for neighbor in neighbors:
    # this lines says (reading right to left): split every word into a separate
    # list item, use .text on it, and 'neighbor' is the iterative keyword in the
    # loop, so do this for every instance in 'neighbors.' Then ignore the first
    # list item (underscore), and store the second list item in var neighbor_ip
    _, neighbor_ip = neighbor.text.split()
    # neighbor.children is defined by the CiscoConfParse module(?) and is populated
    # by every line of configuration under "neighbor x.x.x.x"
    for child in neighbor.children:
        # use .text on the current line for some reason, match on remote-as
        if "remote-as" in child.text:
            # once you find 'remote-as', .split each word into list items
            # ignore the first list item (the word 'remote-as'), and store
            # the ASN in remote_as
            _, remote_as = child.text.split()
    # The only noteworthy thing about this line is its placement
    # inside the 1st for loop, so as the 2nd loop finishes defining
    # neighbor_ip and remote_as, it appends the values to the list, then
    # starts over
    bgp_peers.append((neighbor_ip, remote_as))

print()
print("BGP Peers: ")
pprint(bgp_peers)
print()
