#!/bin/bash

# run the unittests and email results

test_results=`python3 -m pytest`
echo -e "Subject: Test \n\n '$test_results'" | sendmail matthew.kinzler@gmail.com

# run the program
/path/to/python3 /home/mkinzler/PycharmProjects/MapFileTransform/transformer.py
