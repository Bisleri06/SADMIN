import os
import pyautogui
import time

def handle_keypresser(cli):
 
 m=cli.recv(20)
 print "Screen size is "+m
 
 while(1):
   try:
      cmd=""
      cmd=raw_input("> ")
      print cmd

      if(cmd=="quit"):
       cli.send("quit")
       cli.close()
       print("Exited\n")
       return 0

      elif(cmd=="listkeys"):
        print pyautogui.KEYBOARD_KEYS
        continue

      elif(cmd=="clear"):
        os.system("clear")
        continue

      elif(cmd=="ss"):

        cli.send("ss")
        fname="Screenshot_"+str(int(time.time()))+".png"
        fp=open(fname,"wb")
        
        while True:
          buff=cli.recv(10000)
          if len(buff)<10000:
            fp.write(buff)
            fp.close()
            break
          fp.write(buff)

        print("Screenshot saved to file "+fname)
        continue

      cli.send(cmd)

      flag=cli.recv(1)
      if flag=="1":
        print "Did not work.."

   except KeyboardInterrupt:
       return 0
   
   except:
       print "Error occured"
       return 0