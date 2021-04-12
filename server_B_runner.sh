#!/bin/bash

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

python /path/to/mover.py
