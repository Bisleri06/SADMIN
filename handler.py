import os
import time

# Function handel shell
def handle_shell(cli):
 while(1):
	 try:
		  cmd=raw_input("> ")
		  
		  if(cmd=="quit"):
		   cli.send("quit")
		   cli.close()
		   print("\n\n")
		   return 0

		  elif(cmd=="clear"):
		  	os.system("clear")
		  	continue



		  elif(cmd=="ss"):

		  	cli.send("ss")
		  	fname="Screenshot_"+str(int(time.time()))+".png"
		  	fp=open(fname,"wb")
		  	
		  	while True:
		  		buff=cli.recv(1000)
		  		if len(buff)<1000:
		  			fp.write(buff)
		  			fp.close()
		  			break
		  		fp.write(buff)

		  	print("Screenshot saved to file "+fname)
		  	


		  else:
		  	cli.send(cmd)
		  	print(cli.recv(5000))
	 
	 except:
		   print "Error occured"
		   return 0
		   raise