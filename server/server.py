import pyautogui
import socket

s = socket.socket()
print ("Socket successfully created")

port = 22371

s.bind(('', port))
print ("Socket binded to %s" %(port))

s.listen(5)
print ("Socket is listening")

c, addr = s.accept()
while True:
   
   key = c.recv(1024).decode()
   print(key)
   pass
