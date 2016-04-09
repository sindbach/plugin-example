#!/usr/bin/env python 

import json

# List of supported keys
KEY_NAME    = "name"
KEY_ADDRESS = "address"
KEY_PHONE   = "phone"


class Document(object):
    """ Document representation """

    def __init__(self, name, address, phone):
        """ init 

            :param name: name
            :param address: person
            :param phone: phone 
        """
        self.name    = name
        self.address = address
        self.phone   = phone

    def csv(self):
        """ print format a, csv """
        return "%s,%s,%s" % (self.name, self.address, self.phone)

    def newline(self):
        """ print format b, newline """
        return "Name: %s\nAddress:%s\nPhone:%s\n" % (self.name, self.address, self.phone)

    def json(self):
        """ print format c, json """
        jdoc = { "Name": self.name, "Address": self.address, "Phone": self.phone}
        return json.dumps(jdoc, indent=4)


if __name__ == '__main__':
    pass
