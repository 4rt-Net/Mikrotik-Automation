# Mikrotik-Automation
Small tool to automate checks and changes on Mikrotik routers. 

[Usage]:<br />
python SwissTik.py [-h] HELP<br />
-u | --username USERNAME<br />
-p | --password PASSWORD<br />
-t | --target TARGET<br />
-r | --radioname RADIONAME<br />
-c | --command COMMAND<br />
<br />
<br />
Available commands: <br />
check-mac = returns the MAC address of wlan1<br />
check-identity = returns the system identity<br />
check-scanlist = returns the scan-list of wlan1<br />
change-radioname = changes the radioname (needs to be used with [--radioname])<br />
<br />
<br />
Example:<br />
1.) python SwissTik.py -c check-mac -t 127.0.0.1 -u user -p pass<br />
2.) python SwissTik.py --command change-radioname --target 127.0.0.1 -u user -p pass --radioname newRadioName<br />
