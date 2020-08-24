from lxml import etree
'''
x = etree.parse("show_security_zones.xml")
my_xml = x.getroot()
print(my_xml)
'''

# KB does it entirely different
with open("show_security_zones.xml", "r") as infile:
    # parse string using etree.fromstring
    show_security_zones = etree.fromstring(infile.read())

print(show_security_zones)
# Adding this line to print type
print(type(show_security_zones))

# 1b - print out entire xml in unicode string (readable)
# move from byte string
show_security_zones_string = etree.tostring(show_security_zones).decode()
print(25 * '-')
print("1b: print entire xml in unicode string")
print(show_security_zones_string)

# 1c - print root element and number of child elements using len()
print()
print(25 * '-')
print("1c: root element tag and number of child elements")
print(show_security_zones.tag)
# call len() function
print(len(show_security_zones))

# 1d - Using both direct indices and the getchildren() method, obtain the first child element and print its tag name. 
print()
print(25 * '-')
print("1d: print tag name of first child element, direct indice and indirect")
#my_xml_direct = show_security_zones.find("zones-security")
#print(my_xml_direct.tag)
# KB did it via calling the list, didn't realize that's what he meant
print(show_security_zones[0].tag)
my_xml_getchil = show_security_zones.getchildren()
print(my_xml_getchil)
print(my_xml_getchil[0])
print(my_xml_getchil[0].tag)

print()
print(25 * '-')
trust_zone = show_security_zones[0]
print(trust_zone[0].text)

trust_zone_list = []
for xml_tag in trust_zone:
    print(xml_tag.tag)
