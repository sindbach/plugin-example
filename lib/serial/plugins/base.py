#!/usr/bin/env python 

import sys

from serial.exception import SerialException
from serial.document import Document


def try_except(fn):
    """ Decorator for serialise/deserialise Parser methods. 
        This should wrapped the method in a custom try/except, 
        print out proper traceback, and providing info on which 
        function does it failed.

    """
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception, e:
            et, ei, tb = sys.exc_info()
            raise SerialException, "Failed to '%s': %s" % (fn.__name__, SerialException(e)), tb
    return wrapped


class BaseParser(object):
    """ BaseParser, the base class for all parser objects """
    
    def __init__(self):
        """ init """
        self.data    = list()

    def parse_data(self, fileinput):
        """ parse_data, given a file parse the data into a list of Document objects.
            At the moment, its behaviour is to stop parsing on an invalid/erronous line.

            :param fileinput: file path.
        """
        with open(fileinput, 'rb') as fh:
            for line in fh:
                try:
                    name, address, phone = line.strip().split(",")
                    self.data.append(Document(name, address, phone))
                except Exception, ex:
                    raise SerialException(": Failed to parse input line %s: %s" % (line, ex))
        return


    @try_except
    def serialise(self, fileinput):
        """ explicit virtual. (stub) 

            :param fileinput: file to be serialised
        """
        pass

    @try_except
    def deserialise(self, fileinput):
        """ explicit virtual. (stub) 

            :param fileinput: file to be deserialised
        """
        pass


if __name__ == '__main__':
    pass