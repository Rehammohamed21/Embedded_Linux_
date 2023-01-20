#!/bin/bash

grep -r power /sys/ 2> /dev/null >ErrorLog
gedit ErrorLog
mail -s "ErrorLog" -A ErrorLog "e-mail that you send to"


