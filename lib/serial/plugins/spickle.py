#!/usr/bin/env python 

import pickle

from serial.document import Document
from serial.plugins.base import BaseParser
from serial.plugins.base import try_except


class PickleParser(BaseParser):
    """ PickleParser object """

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
        return pickle.dumps(self.data)

    @try_except
    def deserialise(self, fileinput):
        """ deserialise 

            :param fileinput: file to be deserialised
            :returns: list of document objects
        """
        self.data = pickle.load(open(fileinput, 'rb'))
        return self.data


if __name__ == '__main__':
    pass