#!/usr/bin/python 

import paramiko 
import sys 

command = " ".join(sys.argv[1:])
with open('hosts', 'r') as f:
	for line in f.readlines():
		hostname=str(line.split('\t')[0])
		port=int(line.split('\t')[1]) 
		username=str(line.split('\t')[2])
		password=str(line.split('\t')[3]).strip() 
		print ('\033[32m--------------\033[0m'),hostname,('\033[32m--------------\033[0m')
		ssh_client=paramiko.SSHClient() 
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
		ssh_client.connect(hostname,port,username,password) 
		stdin,stdout,sterr=ssh_client.exec_command(command) 
		print stdout.read() 
		ssh_client.close()

print ('\033[35m--------------\033[0m'),'END',('\033[35m--------------\033[0m')
