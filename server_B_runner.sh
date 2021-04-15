#!/bin/bash

echo "start"
expect << 'EOS'
spawn sftp mkinzler@serverA:PycharmProjects/filemover
expect "Password:"
send "*********************"
expect "sftp>"
send "get main_file\n"
expect "sftp>"
send "get log_file\n"
expect "sftp>"
send "bye\n"
EOS
echo "done"

python3 /path/to/mover.py
