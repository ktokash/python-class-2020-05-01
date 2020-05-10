# Add this for python2 to interpret print statements with parenthesis
from __future__ import print_function

ip_addr1 = '8.8.8.8'
print(ip_addr1)

ip_addr2 = input("Enter an IP address: ")
print(ip_addr2)


# To be python2 compatible, use except statements to try old syntax
# p2 has 'input', but almost always use raw_input, while p3 uses input
# no raw_input in p3

try:
    ip_addr3 = raw_input("Enter another IP address: ")
except NameError:
    ip_addr3 = input("Enter another IP address: ")
print(ip_addr3)

