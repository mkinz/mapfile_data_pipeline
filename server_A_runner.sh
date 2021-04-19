#!/bin/bash

# check mapfile and addendum path, and if files are missing, email and exist out of runner

mapfile_path='/path/to/mapfile'
addendum_path='/path/to/addendum'

if [[ ! -f $mapfile_path ]] ; then
    echo -e "Subject: WARNING: red_oasis_map NOT FOUND. \n\n Red oasis map file not found in path '$mapfile_path'.
    Please check the paths to see if something has changed." | sendmail matthew.kinzler@globalfoundries.com
    exit
fi

if [[ ! -f $addendum_path ]] ; then
    echo -e "Subject: WARNING: Addendum file NOT FOUND. \n\n Addendum oasis map file not found in path '$addendum_path'.
    Please check the paths to see if something has changed." | sendmail matthew.kinzler@globalfoundries.com
    exit
fi


# otherwise, run the unittests and email results

test_results=`python3 -m pytest`
echo -e "Subject: Test \n\n '$test_results'" | sendmail matthew.kinzler@globalfoundries.com


# run the program
/tool/pandora64/bin/python3 /home/mkinzler/PycharmProjects/oasisMapFileTransform/oasis_mapfile_transformer.py
