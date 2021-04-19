#!/bin/bash

# run the unittests and email results

test_results=`python3 -m pytest`
echo -e "Subject: Test \n\n '$test_results'" | sendmail matthew.kinzler@globalfoundries.com

# run the program
/tool/pandora64/bin/python3 /home/mkinzler/PycharmProjects/oasisMapFileTransform/oasis_mapfile_transformer.py
