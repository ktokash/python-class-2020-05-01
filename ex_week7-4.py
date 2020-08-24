# 4a. Use the lxml find() method to retrieve the first "zones-security" element. Print out the tag of this element and of all its children elements.
from pprint import pprint
from lxml import etree, objectify

filename = "show_security_zones.xml"
my_xml = etree.parse(filename)
print(type(my_xml))
my_xml = etree.fromstring(filename.read())
print(type(my_xml))

'''print("Find tag of the first zones-security element")
print("-" * 30)
print(my_xml.find(".//zones-security")[0].tag)


print("Find tag of all child elements of the first zones-security element")
print("-" * 30)
my_xml = objectify.parse("show_security_zones.xml")
#my_xml = my_xml.getchildren()
print(type(my_xml))
'''

'''for child in my_xml:
    print(child)
    print(child.tag)
'''

''' turn structured data to string
my_xml = etree.tostring(my_xml)
print(type(my_xml))
#pprint(my_xml)

my_xml = my_xml.decode()
print(type(my_xml))
'''




