# KB solution

from __future__ import unicode_literals, print_function
from lxml import etree

# This function takes a filename as the sole argument. It opens the file specified
# uses 'infile' as the temporary name, applies the fromstring function from the etree
# module, but only after applying the .read method to read in the file contents
def read_xml(filename):
    # store filename passed in as "infile" for simplicity
    with open(filename) as infile:
    # fromstring - Parses an XML document or fragment from a string. Returns the root node (or the result returned by a parser target).
        return etree.fromstring(infile.read())


if __name__ == "__main__":
    filename = "show_security_zones.xml"
    # print(type(filename))     # Returns string
    # Calling a function and passing the xml file to it
    # receiving a string of output, immediately stored in variable
    show_security_zones = read_xml(filename)
    print(type(show_security_zones))

    print("\n\n")
    print("Find tag of the first zones-security element")
    print("-" * 20)
    # I did "print(my_xml.find(".//zones-security")[0].tag)", worked fine
    # KB called etree's .find function with the argument 'root then zones-security'
    first_zone = show_security_zones.find("./zones-security")
    print(type(show_security_zones))
    print(first_zone.tag)

    print()
    print("Find the tag of all the child elements of the first security-zone")
    print("-" * 20)
    # Because KB stored the results of the .find search on the xml file, we have
    # that element, and can call the .getchildren() function on it, storing the
    # results in a new variable
    children = first_zone.getchildren()
    # print(type(children))   # FINALLY HOW WE GET A LIST
    # Now that we have a list, we can loop through it and print each tag
    for child in children:
        print(child.tag)

    print("\n\n")
    print("Use the find() method to find the first 'zones-security-zonename' element")
    print("-" * 20)
    # Print the text behind the first zones-security-zonename instance found
    print(show_security_zones.find(".//zones-security-zonename").text)

    # use .findall function to find every branch named zones-security under root
    security_zones = show_security_zones.findall(".//zones-security")
    # print(type(security_zones)) # FINDALL ALSO GIVES US BACK A LIST, WOOOO!
    # Loop through security_zones list, use .find to return the .text value behind
    # every instance of the string "zones-security-zonename"
    for zone in security_zones:
        print(zone.find("./zones-security-zonename").text)
    print("\n\n")
