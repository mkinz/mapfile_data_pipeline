#!/bin/bash

echo "start"
expect << 'EOS'
spawn sftp mkinzler@serverA:PycharmProjects/filemover
expect "Password:"
send "*********************"
expect "sftp>"
send "get addendum_file\n"
expect "sftp>"
send "bye\n"
EOS
echo "done"

python3 /path/to/mover.py
