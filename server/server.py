import secrets
import pyautogui
import socket
import asyncio
from PIL import Image, ImageFile, ImageTk
from io import BytesIO
import os
import threading
from win32api import GetSystemMetrics, NameDisplay

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


def key_loop_server():
    while True:
        key = c.recv(512).decode()
        print(key)


def server_loop():
    key_loop_server_thread = threading.Thread(target=key_loop_server)
    key_loop_server_thread.start()
    while True:
        #encode
        screen = pyautogui.screenshot()
        screen = screen.resize((res_x, res_y))
        screen.save('img.jpeg', optimize = True, quality = 25)
        screen = open('img.jpeg', 'rb')
        size = os.path.getsize('img.jpeg')
        #print(size)
        #c.send(str(size).encode())
        scren = screen.read()
        bytes = bytearray(scren)

        c.send(bytes)

        #receive pressed key





#start server loop
server_loop()




