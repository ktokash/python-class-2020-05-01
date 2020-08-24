# 2a. Using xmltodict, load the show_security_zones.xml file as a Python dictionary. Print out this new variable and its type

import xmltodict
from pprint import pprint

xmlfile = open("show_security_zones.xml")
xmldata = xmlfile.read().strip()
my_xml = xmltodict.parse(xmldata)
pprint(my_xml)

'''2b. Print the names and an index number of each security zone in the XML data from Exercise 2a. Your output should look similar to the following (tip, enumerate will probably help):
Security Zone #1: trust
Security Zone #2: untrust
Security Zone #3: junos-host'''

print()
print(25 * '-')
print("Print the names and an index number of each security zone")
my_xml = xmltodict.parse(xmldata, force_list={'zones-security': True})
my_xml = xmltodict.parse(xmldata, force_list={'zones-security-zonename': True})
print(type(my_xml["zones-information"]["zones-security"]))

new_list = []
for zones in my_xml:
    zone = my_xml["zones-information"]["zones-security"][0]['zones-security-zonename'][0]
    new_list.append(zone)

print()
print(new_list)
