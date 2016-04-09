#!/usr/bin/env python 

from lxml import etree as ET

class XMLWriter(object):
    def create_element(self, name):
        """ create element

            :param name: name of the element
            :returns: element
        """
        return ET.Element(name)

    def create_subelement(self, parent, name, value=""):
        """ create subelement 

            :param parent: parent element 
            :param name : name of the element 
            :param value : value to be assigned to the element
            :returns: element
        """
        se = ET.SubElement(parent, name)
        se.text = value
        return se

    def to_string(self, element):
        """ Stringity element 

            :param element: element
            :returns: string 
        """
        return ET.tostring(element, pretty_print=True)


class XMLReader(object):

    def get_root_from_file(self, fileinput):
        """ Given a file , read and returns the root document 

            :param fileinput: file path
            :returns: root element
        """
        tree = ET.parse(fileinput)
        return tree.getroot()

    def get_element_children(self, element):
        """ Retrieve all children belonging to an element 

            :param element: element 
            :returns : list of elements
        """
        return [x for x in element]


    def get_subelement_value(self, parent, element):
        """ Retrieve a subelement text value 

            :param parent: parent of the element 
            :param element: element 
            :returns: string
        """
        return parent.find(element).text



if __name__ == '__main__':
    pass

