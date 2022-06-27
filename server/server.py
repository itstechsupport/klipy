from ast import excepthandler
from base64 import encode
from inspect import isdatadescriptor
from operator import truediv
import secrets
from sys import byteorder
import pyautogui
import socket
import asyncio
from PIL import Image, ImageFile, ImageTk
from io import BytesIO
import os
import threading
from win32api import GetSystemMetrics, NameDisplay
import struct

s = socket.socket()


print('  > Starting server')
res_x = int(GetSystemMetrics(0) / 2)
res_y = int(GetSystemMetrics(1) / 2)
print(f'  > Using display with resolution {GetSystemMetrics(0)} x {GetSystemMetrics(1)}, and streaming at {res_x} x {res_y}')
port = 22371

s.bind(('', port))
print(f'  > Server running at {port}')
print('  > Listening for connection...')
s.listen(1)

c, addr = s.accept()
print(f'  > Got connection form {addr}')


class server:
    size = 102400
    def key_loop(self):
        while True:
            try:
                key = c.recv(512).decode()
                print(key)
            except Exception as e:
                #print("  > Couldn't receive key, skipping!")
                pass


    def buffer_loop(self):
        while True:
            try:
                size = os.stat('img.jpeg').st_size
                size_str = str(size)
                c.send(size_str.encode())
            except Exception as e:
                print(f"  > Couldn't send dynamic buffer, sending 102400 buffer! {e}")
                c.send(size)

    def screen_loop(self):
        while True:
            #try:
                #take screenshot
                screen = pyautogui.screenshot()
                screen = screen.resize((res_x, res_y))
                screen.save('img.jpeg', optimize = True, quality = 25)

                #encode frame
                screen = open('img.jpeg', 'rb')
                screen_read = screen.read()

                
                bytes = bytearray(screen_read)

                c.send(bytes)
            #except Exception as e:
            #    print(f"  > Something went wrong! {e}")

    def __init__(self):
        print("a")
        threading.Thread(target=self.key_loop).start()
        #threading.Thread(target=self.buffer_loop).start()
        threading.Thread(target=self.screen_loop).start()
    

server()
input()




