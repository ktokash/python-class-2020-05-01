'''5a. Load the show_version.xml file (originally from a Cisco NX-OS device) using the etree.fromstring() method. Note this XML document, unlike the previous documents, contains the document encoding information. Because the document encoding is at the top of the file, you will need to read the file using "rb" mode (the "b" signifies binary mode). Print out the the namespace map of this XML object. You can accomplish this by using the .nsmap attribute of your XML object.'''

from lxml import etree

def read_xml(filename):
    # Open file with "rb" instead of "r" because it's encoded (not sure how the
    # encoding used ("ISO-8859-1") matters since it's human readable) so we'll
    # read it in as binary
    with open(filename, 'rb') as infile:
        return etree.fromstring(infile.read())

if __name__ == "__main__":
    filename = "show_version.xml"
    show_version = read_xml(filename)
    #print(type(show_version))
    #my_xml = show_version.getroot()
    #print(show_version)
    #print(len(show_version))
    #print(show_version[0])
    #print(len(show_version[0]))
    #print(etree.iselement(show_version))
    #for child in show_version:
    #    print(child.tag)
    print(show_version.nsmap)
    print("\n\n")
    print("Print default document namespace mapping")
    print("-" * 20)
    print("Document default Namespace:\n {}".format(show_version.nsmap))

    print("\n\n")
    print("Print the proc_board_id element using namespace wildcard")
    print("-" * 20)
    # Just use the .find function, then put the search pattern in ()
    # The leading .// means start at root of xml tree, and the .text means
    # print out the text between the xmls tags
    serial_number = show_version.find(".//{*}proc_board_id").text
    print(serial_number)
    serial_number = show_version.find(".//{*}proc_board_id").tag
    print(serial_number)
