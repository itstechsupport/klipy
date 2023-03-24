import pyautogui
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

#define some useless colors
purple = "\033[0;35m"
yellow = "\033[1;33"
green = "\033[1;36"
blank = "\033[0m"

#set config path
appdata = os.getenv('APPDATA')
config_path = "klipy.json"

#define global config things
res_multiplayer = 0
quality = 0

#config doesn't work

#write and read config from file
def write_config(arg):
    print("  > Writting config")
    config = json.dumps(arg)
    try:
        with open(config_path, "w") as f:
            f.write(str(config))
            print("  > Successfully writted to config")
            pass
    except Exception as e:
        print(f"  > Couldn't write to config! {e}")

def read_config():
    print("  > Reading config")
    try:
        global res_multiplayer
        global quality
        config = json.loads(config_path)
        print("  > Successfully read config")
        res_multiplayer = config["res_multiplier"]
        quality = config["quality"]
        
        return config
    except Exception as e:
        print(f"  > Couldn't read config! {e}")
        pass

#setup config
def config_setup():
    if os.path.exists(config_path) == False:
        print("  > Couldn't find config file, creating config file")
        global config
        config = {"host" : "", "port" : 0, "res_multiplier" : 0.5, "quality" : 25}
        write_config(config)
        read_config()
    else:
        print(f"  > Config found at {config_path}")
        pass

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
        menu()


def menu():
    print(f"  > Select (1-3) <")
    print(f"  1. Connect ")
    print(f"  2. Host ")
    print(f"  3. Settings ")
    x = input("  > ")
    if x == "1":
        print("  > Enter hostname:")
        host = input("  > ")
        print("  > Enter port:")
        port = input("  > ")
        if (port.isdigit() == False):
            print("  > Enter port:")
            port = input("  > ")

        connect(host=host, port=int(port))
    if x == "2":
        print("  > Enter port:")
        port = input("  > ")
        host(port=port)
    if x == "3":
        print(f"  > Select (1-3) <")
        print(f"  1. Delete Config ")
        print(f"  2. Change TPS ")
        print(f"  3. Change FPS ")
        y = input("  > ")
        if y == 1:
            os.remove(config_path)
            print("Config removed!")
            z = input("Do you want to run config setup again? [y/n]")
            if z == "y":
                config_setup()
                menu()
            if z == "n":
                pass
                menu()
            
#init
print("  > Starting client")
config_setup()
read_config()
res_x = int(GetSystemMetrics(0))
res_y = int(GetSystemMetrics(1))
print(f'  > Using display with resolution {res_x} x {res_y}')
stream_res = (res_x * res_multiplayer, res_y * res_multiplayer)
print(f'  > Streaming resolution (for server) {stream_res}, with {quality} quality')

print(
    f"""{purple}
                                                               
            .---.                                          
     .      |   |.--._________   _...._                    
   .'|      |   ||__|\        |.'      '-. .-.          .- 
 .'  |      |   |.--. \        .'```'.    \ \ \        / / 
<    |      |   ||  |  \      |       \    \ \ \      / /  
 |   | ____ |   ||  |   |     |        |    | \ \    / /   
 |   | \ .' |   ||  |   |      \      /    .   \ \  / /    
 |   |/  .  |   ||  |   |     |\`'-.-'   .'     \ `  /     
 |    /\  \ |   ||__|   |     | '-....-'`        \  /      
 |   |  \  \'---'      .'     '.                 / /       
 '    \  \  \        '-----------'           |`-' /        
'------'  '---'                               '..'         
    version: {v}, by tech support#8002
    {blank}
    
    """
)
#run the menu
menu()

input()