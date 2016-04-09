#!/usr/bin/env python 


from serial.exception import SerialException
from serial.plugins.base import BaseParser
from serial.plugins.base import try_except
from serial.xml_layer import XMLReader
from serial.xml_layer import XMLWriter
from serial.document import Document
from serial.document import KEY_NAME, KEY_ADDRESS, KEY_PHONE

class XMLParser(BaseParser):
    """ XMLParser

        Given a file path, parse the file for serialisation and deserialisation.
    """

    def __init__(self):
        """ init """
        BaseParser.__init__(self)

    @try_except
    def serialise(self, fileinput):
        """ serialise 

            :param fileinput: file to be serialised
            :returns: serialised string
        """
        self.parse_data(fileinput)
        xwriter = XMLWriter()

        root = xwriter.create_element(name="root")
        for d in self.data:
            doc     = xwriter.create_subelement(parent=root, name="doc")
            name    = xwriter.create_subelement(parent=doc, name=KEY_NAME, value=d.name)
            address = xwriter.create_subelement(parent=doc, name=KEY_ADDRESS, value=d.address)
            phone   = xwriter.create_subelement(parent=doc, name=KEY_PHONE, value=d.phone)

        return xwriter.to_string(root)

    @try_except
    def deserialise(self, fileinput):
        """ deserialise 

            :param fileinput: file to be deserialised
            :returns: list of document objects
        """
        xreader = XMLReader()
        root = xreader.get_root_from_file(fileinput)

        for doc in xreader.get_element_children(root):
            self.data.append(Document(
                                    xreader.get_subelement_value(doc, KEY_NAME),
                                    xreader.get_subelement_value(doc, KEY_ADDRESS),
                                    xreader.get_subelement_value(doc, KEY_PHONE)
                                )
                            )
            
        return self.data



if __name__ == '__main__':
    pass