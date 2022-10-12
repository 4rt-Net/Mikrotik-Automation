# Mikrotik-Automation
Small tool to automate checks and changes on Mikrotik routers. 

[Usage]:<br />
python SwissTik.py [-h] HELP<br />
-u | --username USERNAME<br />
-p | --password PASSWORD
-t | --target TARGET
-r | --radioname RADIONAME
-c | --command COMMAND
\n
Available commands: 
check-mac = returns the MAC address of wlan1
check-identity = returns the system identity
check-scanlist = returns the scan-list of wlan1
change-radioname = changes the radioname (needs to be used with [--radioname])

Example:
1.) python SwissTik.py -c check-mac -t 127.0.0.1 -u user -p pass
2.) python SwissTik.py --command change-radioname --target 127.0.0.1 -u user -p pass --radioname newRadioName
