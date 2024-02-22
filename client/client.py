import keyboard
import socket
import json
import os
import threading
from win32api import GetSystemMetrics

import sys

from tkinter import Label, Tk, Canvas, NW


from PIL import Image, ImageFile, ImageTk
from io import BytesIO

ImageFile.LOAD_TRUNCATED_IMAGES = True

#define some things
s = socket.socket()

v = '0.0.2' #woah

#define global config things
res_multiplayer = 0
quality = 0

#config doesn't work

class client():
    buffer = 102400
    def key_loop(self):
        while True:
            key = keyboard.read_key(suppress=True)
            #print(key)
            if key == None:
                key = "none"
            s.send(key.encode())
    
    def buffer_loop(self):
        while True:
            global buffer
            buffer = int(s.recv(1024))

    def screen_loop(self): 
        while True:
            try:
                screen = s.recv(102400)
                bytes = bytearray(screen)
                stream = BytesIO(bytes)
                image = Image.open(stream)
                size = int(sys.getsizeof(stream))
                print(image)
                #display frame
                if size >= 100:
                    tk_image = ImageTk.PhotoImage(image)
                    canvas.create_image(1, 1, anchor=NW, image=tk_image)
                    canvas.pack()
                else:
                    pass
                
            except Exception as e:
                print(e)
                pass

    def __init__(self):
        global tk
        tk = Tk()
        #threading.Thread(target=self.key_loop).start()
        #threading.Thread(target=self.buffer_loop).start()
        threading.Thread(target=self.screen_loop).start()
        
        global canvas
        canvas = Canvas(tk, width=1280, height=720)

    def connect(host, port):
        print(f"  > Connecting to {host}:{port}")
        try:
            s.connect((host, port))
            client()
            tk.mainloop()
            pass
        except Exception as e:
            print("  > Enter valid hostname and port!")
            print(e)
