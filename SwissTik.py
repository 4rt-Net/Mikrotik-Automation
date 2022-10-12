import argparse
import paramiko
import re

parser = argparse.ArgumentParser()

parser.add_argument(
"--command",
"-c",
default="None",
help=
"List of commands:"
" check-mac | "
"check-identity | "
"check-scanlist | "
"change-radioname | "
)

parser.add_argument(
"--output",
"-o",
default="temp.txt",
help="temporary file for stdout data. Do not change (recommended)"
)

parser.add_argument(
"--target",
"-t",
default="0.0.0.0",
help="specify IP address to target"
	)

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
"--radioname",
"-r",
default="None",
help="specify radio-name for wlan1 interface"
	)

def MacRegex():
	file = open('temp-maccheck.txt', 'r')
	for lines in file:
   	 matches = re.search('(?:[0-9a-fA-F]:?){12}', lines)
   	 if matches != None:
   	   print(matches.group())

def ScanlistRegex():
	file = open('temp-scanlist.txt', 'r')
	for lines in file:
   	 matches = re.search('scan-list=\d{4}-\d{4}', lines)
   	 if matches != None:
   	   print(matches.group())

def main(args):
	#Check mac address of wlan1 interface
	if args.command == "check-mac":
		try:
			client = paramiko.SSHClient()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
			client.connect(hostname = args.target , port='22', username= args.username ,password= args.password ,look_for_keys=False)
			stdin,stdout,stderr = client.exec_command('/interface wireless print')
			output_read = stdout.readlines()
			file=open('temp-maccheck.txt','w')
			file.write(''.join(output_read))
			file.close()
			stdin,stdout,stderr.flush()
		except:
			print("# Connection failed to: ", args.target)
		finally:
			client.close()
			MacRegex()

	#Check scanlist of unit		
	elif args.command == "check-scanlist":
		try:
			client = paramiko.SSHClient()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
			client.connect(hostname = args.target , port='22', username= args.username ,password= args.password ,look_for_keys=False)
			stdin,stdout,stderr = client.exec_command('/interface wireless print')
			output_read = stdout.readlines()
			file=open('temp-scanlist.txt', 'w')
			file.write(''.join(output_read))
			file.close()
			stdin,stdout,stderr.flush()
		except:
			print("# Connection failed to: ", args.target)
		finally:
			client.close()
			ScanlistRegex()

	#Check system identity of unit
	elif args.command == "check-identity":
		try:
			client = paramiko.SSHClient()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
			client.connect(hostname = args.target , port='22', username= args.username ,password= args.password ,look_for_keys=False)
			stdin,stdout,stderr = client.exec_command('/system identity print')
			output_read = stdout.readlines()
			print(output_read)
			stdin,stdout,stderr.flush()
		except:
			print("# Connection failed to: ", args.target)
		finally:
			client.close()

	elif args.command == "change-radioname":
		try:
			client = paramiko.SSHClient()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
			client.connect(hostname = args.target , port='22', username= args.username ,password= args.password ,look_for_keys=False)
			stdin,stdout,stderr = client.exec_command('/interface wireless set wlan1 radio-name='+str(args.radioname))
			output_read = stdout.readlines()
			client.close()
			print("closing ssh connection...")
			stdin,stdout,stderr.flush()
			print("Unit is reconnecting, radio-name changed to:"+str(args.radioname))
		except:
			print("# Connection failed to: ", args.target)

if __name__ == "__main__":
	main(parser.parse_args())