import os
import subprocess
import socket
import sys
import pyautogui

def sender(soc):
   pyautogui.screenshot("tmp.png")
   fp=open("tmp.png","rb")

   while True:
    buff=fp.read(10000)
    if len(buff)<10000:
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
  soc.send("K")
  x=pyautogui.size()
  sz=str(x.width)+"x"+str(x.height)
  soc.send(sz)
 
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

    cmd=cmd.split(" ")

   
    if(cmd[0]=="write"):
      towrite=""      
      for i in cmd[1:]:
        towrite=towrite+" "+i
      pyautogui.write(towrite,interval=0)
      soc.send("0")      
      continue


    elif(cmd[0]=="press"):
      pyautogui.press(cmd[1])
      soc.send("0")      
      continue


    elif(cmd[0]=="hotkey"):
      if len(cmd)==3:
        pyautogui.hotkey(cmd[1],cmd[2],interval=0.1)
      if len(cmd)==4:
        pyautogui.hotkey(cmd[1],cmd[2],cmd[3],interval=0.1)
      soc.send("0")      
      continue
      


    elif(cmd[0]=="move"):
      if(len(cmd)==3):
        cmd.append(0)
      pyautogui.moveTo(int(cmd[1]),int(cmd[2]),int(cmd[3]))
      soc.send("0")
      continue
      


    elif(cmd[0]=="drag"):
      if(len(cmd)==3):
        cmd.append(0)
      pyautogui.dragTo(int(cmd[1]),int(cmd[2]),int(cmd[3]))
      soc.send("0")
      continue
      


    elif(cmd[0]=="lclick"):
      pyautogui.click(button='left')
      soc.send("0")
      continue
      


    elif(cmd[0]=="rclick"):
      pyautogui.click(button='right')
      soc.send("0")
      continue
      



    elif(cmd[0]=="mclick"):
      pyautogui.click(button='middle')
      soc.send("0")
      continue
      

    elif(cmd[0]=="scroll"):
      pyautogui.scroll(cmd[1])
      soc.send("0")      
      continue
      

    else:
      soc.send("1")
      continue
      
  except KeyboardInterrupt:
     return
  
  except:
     soc.send("1")




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