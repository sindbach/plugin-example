################################################################################
################################################################################

1. Set environment variable:

HOMEP     = "./"  # Update to absolute path of the cwd.
PYTHONPATH="${PYTHONPATH}:${HOMEP}/lib"

2. Running tests:

cd ./tests/
./testmain.sh # This should execute python unittest tests.py and top level tests.

3. exc_main.py script usage example:

./exc_main.py --type xml --serialise --input ./tests/test_input.txt
./exc_main.py --type xml --deserialise --input ./tests/test_input.xml
./exc_main.py --type pickle --serialise --input ./tests/test_input.txt
./exc_main.py --type pickle --deserialise --input ./tests/test_input.pickle --dprint dc

4. xml_layer_alternative.py is an example of swappable xml_layer module.

5. To add a new parser:
5.1. Add a BaseParser inherited class into lib/serial/plugins/
5.2. Update lib/serial/plugins/manifests.json

6. Types of display is assumed to be on the deserialisation, due to on a serialisation process
the output string is already different per parser.

7. ETC:
xml_layer.py  : granular methods. (xml modules) VS high-level (the parser itself)
base_parser.py: providing (de)serialisation for a doc VS a file.


################################################################################




