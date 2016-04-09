#!/usr/bin/env python 

import unittest

try:
    from serial.serialiser import SerialLoader
    from serial.plugins.base import BaseParser
    from serial.exception import SerialException
    from serial.document import Document 
    from serial.xml_layer import XMLWriter
    from serial.xml_layer import XMLReader
except Exception, ex:
    raise Exception("Failed to load modules to be tested. Check your PYTHONPATH: %s" % ex)

################################################################################
class TestXMLLayer(unittest.TestCase):
    def setUp(self):
        pass

    def test_xml_writer(self):
        """ function test xmlwriter """
        sampletext = """<root>\n  <doc><name>test</name></doc>\n</root>\n"""
        xwriter = XMLWriter()
        root    = xwriter.create_element(name="root")
        doc     = xwriter.create_subelement(parent=root, name="doc")
        name    = xwriter.create_subelement(parent=doc, name="name", value="test")
        self.assertEqual(xwriter.to_string(root), sampletext)
        return


    def test_xml_reader(self):
        xreader = XMLReader()

        root  = xreader.get_root_from_file("./test_input.xml")
        docs  = xreader.get_element_children(root)

        self.assertTrue(isinstance(docs, list))
        self.assertEqual(xreader.get_subelement_value(docs[0], "name"), '"Guido Rossum"')
        return

################################################################################
class TestXMLParser(unittest.TestCase):
    def setUp(self):
        self.xmlp = {
                "module"      : "sxml",
                "class"       : "XMLParser"
            }        
        self.xmlo = SerialLoader.create_parser(parser=self.xmlp)

    def test_xmlparser_serialiser(self):
        """ Test xml parser serialise() """

        sampletext = """<root>
  <doc><name>"Guido Rossum"</name><address> "88 Palo Alto"</address><phone> "776985411"</phone></doc>
  <doc><name>"John Smith"</name><address> "38 Driver Avenue"</address><phone> "091234567"</phone></doc>
  <doc><name>"Jane Doe"</name><address> "17 Waine Street"</address><phone> "0494512390"</phone></doc>
</root>
"""     
        self.assertEqual(self.xmlo.serialise("./test_input.txt"), sampletext)

        return 

    def test_xmlparser_deserialiser(self):
        """ Test xml parser deserialise() """
        sampletext = '"Guido Rossum", "88 Palo Alto", "776985411"' 
        self.assertEqual(self.xmlo.deserialise("./test_input.xml")[0].csv(), sampletext)
        return 


################################################################################
class TestDocument(unittest.TestCase):
    def setUp(self):
        pass

    def test_document_basic(self):
        """ Test basic document functionality """   
        d = Document("name", "address", "phone")
        # Check for basic attributes
        self.assertTrue(hasattr(d, 'name'))
        self.assertTrue(hasattr(d, 'address'))
        self.assertTrue(hasattr(d, 'phone'))
        return

    def test_document_display(self):
        """ Test basic document display printout """
        d = Document("name", "address", "phone")
        # check for display print a and b
        self.assertEqual(d.csv(), "name,address,phone")
        self.assertEqual(d.newline(), "Name: name\nAddress:address\nPhone:phone\n")
        return 


################################################################################
class TestSerialLoader(unittest.TestCase):
    def setUp(self):
        pass

    def test_supported_parsers_rtype(self):
        """ Test get_supported_parser() return type """
        supported = SerialLoader.get_supported_parsers()

        # Check return type is a dictionary
        self.assertTrue(isinstance(supported, dict))
        return

    def test_parser_instantiation(self):
        """ Test create_parser() return object """
        parser = {
                "module"      : "spickle",
                "class"       : "PickleParser"
            }        
        o = SerialLoader.create_parser(parser=parser)

        # Check instance base class
        self.assertTrue(isinstance(o, BaseParser))

        # Check instance must have methods
        self.assertTrue(hasattr(o, "serialise"))
        self.assertTrue(hasattr(o, "deserialise"))

        # Check SerialException raise when parser object is empty
        parser = {}
        self.assertRaises(SerialException, SerialLoader.create_parser, parser)       

        return 


################################################################################
if __name__ == '__main__':
    """ test suites execution """
    suite_list = [unittest.TestLoader().loadTestsFromTestCase(TestDocument),
                  unittest.TestLoader().loadTestsFromTestCase(TestSerialLoader),
                  unittest.TestLoader().loadTestsFromTestCase(TestXMLLayer),
                  unittest.TestLoader().loadTestsFromTestCase(TestXMLParser)
                 ]
    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(suite_list))


