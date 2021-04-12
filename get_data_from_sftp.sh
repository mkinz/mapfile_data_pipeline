#!/bin/bash

python print_start.py # dummy call to python script 1

echo "start"
expect << 'EOS'
spawn sftp mkinzler@hostname:PycharmProjects/filemover
expect "Password:"
send "*********************"
expect "sftp>"
send "get add\n"
expect "sftp>"
send "bye\n"
EOS
echo "done"

python print_end.py # dummy call to python script 2
