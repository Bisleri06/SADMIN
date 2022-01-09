from time import sleep

def handle_upload(cli):
 
 name=raw_input("Enter file to upload: ")
 
 try:
  f=open(name,"rb")
 except e:
  print e
  return 1

 try:
  buf=f.read()

  print("Sending file....")
  cli.send(name)
  sleep(1)
  cli.send(str(len(buf)))
  sleep(1)
  cli.send(buf)
  m=cli.recv(5)
  if(m=="Error"):
   print("Error occured")
  cli.close()
  print("Sent!\n\n")
 
 except:
  cli.close()
  return 1
