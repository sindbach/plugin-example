#!/bin/bash

echo -e "\n=TEST="
python ./tests.py

# Top level functioal tests
echo -e "\n=TEST type listing="
../exc_main.py -l

echo -e "\n=TEST xml serialiser="
../exc_main.py -s -t xml -i ./test_input.txt

echo -e "\n=TEST xml deserialiser="
../exc_main.py -d -t xml -i ./test_input.xml

echo -e "\n=TEST pickle deserialiser with different display="
../exc_main.py -d -t pickle -i ./test_input.pickle --dprint json