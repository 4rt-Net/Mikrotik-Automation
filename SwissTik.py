import argparse
import paramiko
import re
import time
from time import sleep

parser = argparse.ArgumentParser(description='\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Created by Art-Net ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nThe lazy-admin tool to quickly and easily perform functions on RouterOS.\nSpecifically created to save you time and sanity while changing settings remotely.\n\nThis tool uses SSH to open a connection to the target\nDue to SSH being used this tool is sensitive to ssh configuration:\nrequirements: port 22 needs to be open on RouterOS\n\nSpecial thanks to:\nRextended - for his RegEx solution\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument(
"--command",
"-c",
default="None",
help=(
"List of commands:\n"
" check-mac\n"
" check-identity\n"
" check-scanlist\n"
" change-radioname\n"
" create-ssl\n"
))

parser.add_argument(
"--username",
"-u",
default="admin",
help="specify username for login"
	)

parser.add_argument(
"--password",
"-p",
default="None",
help="specify password for login"
	)

parser.add_argument(
"--target",
"-t",
default="0.0.0.0",
help="specify IP address to target"
	)

parser.add_argument(
"--ssl",
"-s",
default="Cert-1",
help="Specify name for ssl certificate"
)

parser.add_argument(
"--radioname",
"-r",
default="None",
help="specify radio-name for wlan1 interface"
	)

def MacRegex():
	macregex = "([0-9a-fA-F]{2}:){5}[1-9a-fA-F]{2}"
	file = open('temp-maccheck.txt', 'r')
	for lines in file:
   	 matches = re.search(macregex, lines)
   	 if matches != None:
   	   print(matches.group())

def ScanlistRegex():
	scanregex = "scan-list=\d{4}-\d{4}"
	file = open('temp-scanlist.txt', 'r')
	for lines in file:
   	 matches = re.search(scanregex, lines)
   	 if matches != None:
   	   print(matches.group())

def main(args):
	#Check mac address of wlan1 interface
	if args.command == "check-mac":
		try:
			client = paramiko.SSHClient()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
			client.connect(hostname = args.target , port='22', username= args.username ,password= args.password ,look_for_keys=False)
			print("Connected to: "+(args.target))
			stdin,stdout,stderr = client.exec_command('/interface wireless print')
			output_read = stdout.readlines()
			file=open('temp-maccheck.txt','w')
			file.write(''.join(output_read))
			file.close()
			stdin,stdout,stderr.flush()
		except:
			print("# Connection failed to: ", args.target)
			print("check that the port 22 is open on the target")
		finally:
			client.close()
			MacRegex()

	#Check scanlist of unit		
	elif args.command == "check-scanlist":
		try:
			client = paramiko.SSHClient()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
			client.connect(hostname = args.target , port='22', username= args.username ,password= args.password ,look_for_keys=False)
			print("Connected to: "+(args.target))
			stdin,stdout,stderr = client.exec_command('/interface wireless print')
			output_read = stdout.readlines()
			file=open('temp-scanlist.txt', 'w')
			file.write(''.join(output_read))
			file.close()
			stdin,stdout,stderr.flush()
		except:
			print("# Connection failed to: ", args.target)
			print("check that the port 22 is open on the target")
		finally:
			client.close()
			ScanlistRegex()

	#Check system identity of unit
	elif args.command == "check-identity":
		try:
			client = paramiko.SSHClient()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
			client.connect(hostname = args.target , port='22', username= args.username ,password= args.password ,look_for_keys=False)
			print("Connected to: "+(args.target))
			stdin,stdout,stderr = client.exec_command('/system identity print')
			output_read = stdout.readlines()
			print(output_read)
			stdin,stdout,stderr.flush()
		except:
			print("# Connection failed to: ", args.target)
			print("check that the port 22 is open on the target")
		finally:
			client.close()
	
	#Change radio-name of wlan1 on unit
	elif args.command == "change-radioname":
		try:
			client = paramiko.SSHClient()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
			client.connect(hostname = args.target , port='22', username= args.username ,password= args.password ,look_for_keys=False)
			print("Connected to: "+(args.target))
			stdin,stdout,stderr = client.exec_command('/interface wireless set wlan1 radio-name='+str(args.radioname))
			print("Unit is reconnecting, radio-name changed to:"+str(args.radioname))
			print("closing ssh connection...")
			client.close()
			stdin,stdout,stderr.flush()
		except:
			print("# Connection failed to: ", args.target)
			print("check that the port 22 is open on the target")

	#Create, sign and assign ssl certificate to api-ssl
	elif args.command == "create-ssl":
		try:
			client = paramiko.SSHClient()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
			client.connect(hostname = args.target , port='22', username= args.username ,password= args.password ,look_for_keys=False)
			print("Connected to: "+(args.target))
			print("Creating SSL Certificate...")
			stdin,stdout,stderr = client.exec_command('/certificate add name='+(args.ssl)+' common-name='+(args.ssl)+' key-usage=key-cert-sign,crl-sign key-size=2048 trusted=yes days-valid=1175')
			print("Done")
			#stdin,stdout,stderr = client.exec_command('/certificate sign # name='+(args.ssl)+' ca-crl-host='+str(args.target))
			#print("Signing certificate, please wait...")
			#time.sleep(20)
			#print("Done")
			#print("Assigning certificate to API-SSL service...")
			#stdin,stdout,stderr = client.exec_command('/ip service set api-ssl certificate='+(args.ssl))
			#print("SSL Certificate completed!")
			client.close()
			stdin,stdout,stderr.flush()
		except:
			print("# Connection failed to: ", args.target)
			print("check that the port 22 is open on the target")

if __name__ == "__main__":
	main(parser.parse_args())
