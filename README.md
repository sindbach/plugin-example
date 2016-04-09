
#### Set environment variable:

Update to absolute path of the cwd.

`PYTHONPATH="./lib:${PYTHONPATH}"`

#### Running tests:

```
cd ./tests/
./testmain.sh # This should execute python unittest tests.py and top level tests.
```

#### exc_main.py script usage example:

```
./exc_main.py --type xml --serialise --input ./tests/test_input.txt
./exc_main.py --type xml --deserialise --input ./tests/test_input.xml
./exc_main.py --type pickle --serialise --input ./tests/test_input.txt
./exc_main.py --type pickle --deserialise --input ./tests/test_input.pickle --dprint dc
```

#### xml_layer_alternative.py is an example of swappable xml_layer module.

#### To add a new parser:

* Add a BaseParser inherited class into lib/serial/plugins/
* Update lib/serial/plugins/manifests.json

#### Types of display is assumed to be on the deserialisation, due to on a serialisation process
the output string is already different per parser.

#### misc :
xml_layer.py  : granular methods. (xml modules) VS high-level (the parser itself)
base_parser.py: providing (de)serialisation for a doc VS a file.





