#!/bin/bash


history >> history_file.txt       #get the history

mail --version
sudo apt install mailutils
sudo apt-get install ssmtp
sudo nano /etc/ssmtp/ssmtp.conf

<<comment
# Make this empty to disable rewriting.
SERVER=rehammohamed2155@gmail.com   # mail you send from

# MX records are consulted. Commonly mailhosts are named mail.domain.com
mailhub=smtp.gmail.com:587

AuthUser=rehammohamed2155@gmail.com
Authpass=rurvvceobvynlqnj       #password of app passwaords from google
UseTLS=YES
UseSTARTTLS=YES

#rewriteDomain=
rewriteDomain=gmail.com

# The full hostname
hostname=reham-VirtualBox

#FromLineOverride=YES
FromLineOverride=YES
comment

mail -s "linux_history" -A history_file.txt rehamma215@gmail.com

<<comment2
Cc : (click  ctrl + d to send )
comment2

<<comment3
"linux_history"      ---> mail subject
history_file.txt     ---> file to send
rehamma215@gmail.com ---> mail send the file to
comment3
