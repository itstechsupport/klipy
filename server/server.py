import pyautogui
import socket
import asyncio
from PIL import Image, ImageFile
from io import BytesIO


s = socket.socket()
print ("Socket successfully created")

port = 22371

s.bind(('', port))
print ("Socket binded to %s" %(port))

s.listen(5)
print ("Socket is listening")

c, addr = s.accept()
while True:
    #encode
    screen = pyautogui.screenshot()
    screen.save("img.jpeg", optimize = True, quality = 5)
    screen = open('img.jpeg', 'rb')
    scren = screen.read()
    bytes = bytearray(scren)

    #send
    c.send(bytes)

    #receive pressed key
    key = c.recv(1024).decode()
    print(key)



