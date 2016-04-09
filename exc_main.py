#!/usr/bin/env python

""" Executable for serialiser package. 

    Supporting 3 modes of operation: serialise, deserialise and listtypes.
"""

import sys
import argparse

from serial.serialiser import SerialLoader
from serial.serialiser import DE_PRINT


def main(flags):
    # fetch a list of available plugins.
    try:
        supported = SerialLoader.get_supported_parsers()
    except Exception, ex:
        print "Failed to load supported plugins: %s" % ex
        sys.exit(1)

    # list supported/available plugins and then quit
    if flags.listtypes:
        for k, v in supported.iteritems():
            print "Type: %s" % (k)
            print "Desc: %s" % (v.get("description"))
        sys.exit(1)

    # validate serialiser type
    if not flags.type in supported.keys():
        print "Parser type %s is not supported. Please read --help file" % (flags.type)
        sys.exit(1)

    # instantiate object parser
    s = SerialLoader.create_parser(parser=supported.get(flags.type))   

    # run serialise()
    if flags.serialise:
        print s.serialise(flags.input)

    # run deserialise()
    elif flags.deserialise:
        dprint = flags.dprint
        if not dprint in  DE_PRINT:
            print "Warning: print format is unsupported. reverting to default."
            dprint = DE_PRINT[0]
        
        for d in s.deserialise(flags.input):
            print getattr(d, dprint)()

    return 


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-s", "--serialise", action="store_true", help="Serialise document mode.")
    parser.add_argument("-d", "--deserialise", action="store_true", help="Deserialise document mode.")
    parser.add_argument("-l", "--listtypes", action="store_true", help="List supported types mode.")

    parser.add_argument("-t", "--type", help="Specify parser type. [REQUIRED]")
    parser.add_argument("-i", "--input", help="Specify file input. [REQUIRED]")
    parser.add_argument("--dprint", default="csv", help="Specify format of deserialisation display. %s" % DE_PRINT)

    flags = parser.parse_args()

    if not (flags.serialise or flags.deserialise or flags.listtypes):
        print "Please specify at least one mode of operation. (serialise, deserialise, listtypes)"
        parser.print_help()
        sys.exit(1)

    if (flags.serialise and flags.deserialise) or \
        (flags.serialise and flags.listtypes) or \
        (flags.deserialise and flags.listtypes):

        print "Please choose only one mode of operation"
        parser.print_help()
        sys.exit(1)

    if (flags.serialise or flags.deserialise) and not flags.type:
        print "Please specify serialiser type."
        parser.print_help()
        sys.exit(1)

    if (flags.serialise or flags.deserialise) and not flags.input:
        print "Please specify an input file."
        parser.print_help()
        sys.exit(1)

    main(flags)


