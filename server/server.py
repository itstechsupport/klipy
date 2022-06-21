import pyautogui
import socket
import asyncio
from PIL import Image, ImageFile
from io import BytesIO
import os
from multiprocessing import Process

s = socket.socket()

port = 22371

s.bind(('', port))
print(f'   > Server running at {port}')
print('   > Listening for connection...')
s.listen(1)

c, addr = s.accept()
print(f'   > Got connection form {addr}')

def screen_loop():
    #encode
    screen = pyautogui.screenshot()
    screen.save('img.jpeg', optimize = True, quality = 7)
    screen = open('img.jpeg', 'rb')
    size = os.path.getsize('img.jpeg')
    print(size)
    #c.send(str(size).encode())
    scren = screen.read()
    bytes = bytearray(scren)
    
    #send
    c.send(bytes)

def key_loop():
    #receive pressed key
    key = c.recv(512).decode()
    print(key)


#start loop
l1 = Process(target = screen_loop)
l1.start()
key_loop()




