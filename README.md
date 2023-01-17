# Mikrotik-Automation
Automate checks and changes on Mikrotik routers.

[Usage]:<br />
python SwissTik.py [-h]<br />
-u | --username<br />
-p | --password<br />
-t | --target<br />
-r | --radioname<br />
-c | --command<br />
-s | --ssl<br />
<br />
<br />
Available commands for -c switch: <br />
check-mac = returns the MAC address of wlan1<br />
check-identity = returns the system identity<br />
check-scanlist = returns the scan-list of wlan1<br />
change-radioname = changes the radioname (needs to be used in conjunction with [--radioname])<br />
create-ssl = create, sign and assign a ssl certificate to api-ssl<br />
<br />
<br />
Example:<br />
1.) python SwissTik.py -c check-mac -t 127.0.0.1 -u user -p pass<br />
2.) python SwissTik.py --command change-radioname --target 127.0.0.1 -u user -p pass --radioname newRadioName<br />
3.) python SwissTik.py -c create-ssl -t 127.0.0.1 -u user -p pass -s certificate1
