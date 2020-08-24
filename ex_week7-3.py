import xmltodict
from pprint import pprint

def read_xml(filename):
    with open(filename, "r") as infile:
        return xmltodict.parse(infile.read())

def read_xml_forcelist(filename, force_list=None):
    if force_list is None:
        force_list = {}
    with open(filename, "r") as infile:
        return xmltodict.parse(infile.read(), force_list=force_list)

if __name__ == "__main__":

    filename = "show_security_zones.xml"
    show_security_zones = read_xml(filename)
    
    filename = "show_security_zones_single_trust.xml"
    show_security_zones_single_trust = read_xml(filename)

    '''print(type(show_security_zones))
    print(type(show_security_zones_single_trust))
    pprint(show_security_zones)
    pprint(show_security_zones_single_trust)'''

# 3b. Compare the Python "type" of the elements at ['zones-information']['zones-security']. What is the difference between the two data types? Why?

    print(type(show_security_zones['zones-information']))
    print(type(show_security_zones['zones-information']['zones-security']))

# 3c. Create a second function that uses xmltodict to read and parse the "show_security_zones_single_trust.xml". Verify the Python data type is now a list for the ['zones-information']['zones-security'] element.

    filename = "show_security_zones.xml"
    # forcelist requires a second var - the exact spot in the XML tree to turn
    # into a list
    show_security_zones_single_trust = read_xml_forcelist(
        filename, force_list={"zones-information": True})

    print(type(show_security_zones_single_trust['zones-information']))
    print(len(show_security_zones_single_trust))
    print(*show_security_zones_single_trust)
