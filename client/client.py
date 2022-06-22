import pyautogui
import keyboard
import socket
import json
import os
import threading

from tkinter import * 


from PIL import Image, ImageFile, ImageTk
from io import BytesIO


ImageFile.LOAD_TRUNCATED_IMAGES = True


s = socket.socket()

v = '0.0.2' #woah



purple = "\033[0;35m"
yellow = "\033[1;33"
green = "\033[1;36"
blank = "\033[0m"

appdata = os.getenv('APPDATA')
config_path = appdata + "\klipy.json"

#write and read config from file
def write_config(arg):
    config = json.dumps(arg)
    try:
        with open(config_path, "w") as f:
            f.write(str(config))
            print("Successfully writted to config")
            pass
    except Exception as e:
        print(f"Couldn't write to config! {e}")

def read_config():
    try:
        config = json.loads(config_path)
        print("Successfully read config")
        
        return config
    except Exception as e:
        print(f"Couldn't read config! {e}")
        pass

#setup config
def config_setup():
    if os.path.exists(config_path) == False:
        print("Config not found, creating config...")
        config = {"host" : "", "port" : 0, "tps" : 60, "fps" : 0}
        write_config(config)
        read_config()
    else:
        print(f"Config found at {config_path}")
        pass

config_setup()
print(
    f"""{purple}
                                                               
            .---.                                          
     .      |   |.--._________   _...._                    
   .'|      |   ||__|\        |.'      '-. .-.          .- 
 .'  |      |   |.--. \        .'```'.    '.\ \        / / 
<    |      |   ||  |  \      |       \     \\ \      / /  
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

def key_loop():
    while True:
        key = keyboard.read_key(suppress=True)
        if key == None:
            key = "none"
        s.send(key.encode())
tk = Tk()


def client_loop(): 
    key_loop_thread = threading.Thread(target=key_loop)
    canvas = Canvas(tk, width = 1280, height = 720)
    canvas.pack() 
    key_loop_thread.start()
    while True:
        try:
            #receive screen shot
            #buffer = s.recv(512).decode()
            #print(str(buffer))a
            screen = s.recv(102400)

            print(screen)
            #encode screenshot
            bytes = bytearray(screen)

            stream = BytesIO(bytes)

            image = Image.open(stream)
            image.save("received.png")
            stream.close()

            #display image  
            img = PhotoImage(file="received.png")
            canvas.create_image(0.01, 0.01, anchor=NW, image=img) 
            canvas.pack()

            buffer = None


            #now the keys

        except:
            screen = None
            bytes = None
            stream = None 
            image = None
            pass

def connect(host, port):
    print(f"  > Connecting to {host}:{port}")
    try:
        s.connect((host, port))
        tk_inter_thread = threading.Thread(target=client_loop)
        tk_inter_thread.start()
        tk.mainloop()
        pass
    except Exception as e:
        print("  > Enter valid hostname and port!")
        print(e)
        menu()



class server():
    def host(port):
        print(f"  > Hosting at {port}")

#ansi colors tui

"""
print(f"{yellow}  > What now? <{blank}")
print(f"{green}  1. Connect {blank}")
print(f"{green}  2. Host {blank}")
print(f"{green}  3. Settings {blank}")
print(f"{yellow}  > {blank}")
"""
#tui

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
            
#run the menu
menu()