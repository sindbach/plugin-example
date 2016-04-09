#!/usr/bin/env python 

import os
import json 
import importlib

from serial.exception import SerialException

PKG_NAME = "serial"
PLUG_DIR = "plugins"

# List of supported deserialiser print types
# FUTURE: give more descriptive name
DE_PRINT = ['csv', 'newline', 'json']


class SerialLoader(object):
    """ SerialLoader 

        Load/instantiate the supported object parsers.
    """

    @staticmethod
    def get_supported_parsers():
        """ Get a list of supported parsers.

            Fetch the list from the 'manifest' (which could be DB, file, env var).
            Raising SerialException on error.

            :return: dictionary of available/supported parsers.
        """
        # FUTURE: scan and read from env path or db.
        MANIFEST = os.path.join(os.path.dirname(__file__), "%s/manifest.json" % PLUG_DIR)

        if not os.path.isfile(MANIFEST):
            raise SerialException("Missing manifest file: %s" % MANIFEST)

        try:
            parsers_dict = json.loads(open(MANIFEST).read())
        except Exception, ex:
            raise SerialException("Failed to parse manifest %s: %s" % (MANIFEST, ex))

        return parsers_dict


    @staticmethod
    def create_parser(parser):
        """ create_parser static method
            Instantiate a serialiser parser object. Given a dict with keys
            'module' and 'class', try import the parser and instantiate it. 

            :param parser: parser dictionary. 
            :return: parser object
        """
        try:
            _module     = parser["module"]
            _classname  = parser["class"]
        except KeyError, ex:
            raise SerialException("Invalid parser object: %s" % ex)
        except Exception, ex:
            raise SerialException("Unknown error reading parser argument: %s" % ex)

        try:
            mod     = importlib.import_module("%s.%s.%s" % (PKG_NAME, PLUG_DIR, _module))
        except Exception, ex:
            raise SerialException("Failed to import parser object %s: %s" % (_module, ex))

        try:
            obj     = getattr(mod, _classname)
        except Exception, ex:
            raise SerialException("Failed to instantiate parser %s: %s" % (_classname, ex))

        return obj()



if __name__ == '__main__':
    pass



