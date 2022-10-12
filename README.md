# Mikrotik-Automation
Small tool to automate checks and changes on Mikrotik routers. 

[Usage]:\n
python SwissTik.py [-h] HELP\n
-u | --username USERNAME\n
-p | --password PASSWORD\n
-t | --target TARGET\n
-r | --radioname RADIONAME\n
-c | --command COMMAND\n
\n
Available commands: \n
check-mac = returns the MAC address of wlan1\n
check-identity = returns the system identity\n
check-scanlist = returns the scan-list of wlan1\n
change-radioname = changes the radioname (needs to be used with [--radioname])\n
\n
Example:\n
1.) python SwissTik.py -c check-mac -t 127.0.0.1 -u user -p pass\n
2.) python SwissTik.py --command change-radioname --target 127.0.0.1 -u user -p pass --radioname newRadioName\n
