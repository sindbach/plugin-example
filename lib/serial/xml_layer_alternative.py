#!/usr/bin/env python 
""" An alternative of XMLWriter and XMLReader

    Utilising xml module instead of lxml.
"""

import xml.etree.ElementTree as ET


class XMLWriter(object):

    def create_element(self, name):
        return ET.Element(name)

    def create_subelement(self, parent, name, value=""):
        se = ET.SubElement(parent, name)
        se.text = value
        return se

    def to_string(self, element):
        return ET.tostring(element, 'utf-8')


class XMLReader(object):

    def get_root_from_file(self, fileinput):
        return ET.parse(fileinput).getroot()


    def get_element_children(self, element):
        return  element.getchildren()


    def get_subelement_value(self, parent, element):
        return parent.find(element).text






if __name__ == '__main__':
    pass

