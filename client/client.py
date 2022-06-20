import pyautogui
import keyboard
import socket
import json
import os

from PIL import Image
from io import BytesIO

s = socket.socket()

#temp
import pygame




X = 1280
Y = 720


display_surface = pygame.display.set_mode((X, Y ))





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


def client_loop():
    pygame.init()
    while True:
        #receive screen shot
        screen = s.recv(1024)

        #encode screenshot
        stream = BytesIO(screen)

        image = Image.open(stream).convert("RGBA")
        stream.close()
        image.show()

        """
        display_surface.blit(pygame.image.load(screen), (0, 0))
        pygame.display.update()
        """

        #send pressed key
        key = keyboard.read_key()
        s.send(key.encode())

def connect(host, port):
    print(f"  > Connecting to {host}:{port}")
    try:
        s.connect((host, port))
        pass
    except Exception as e:
        print("  > Enter valid hostname and port!")
        print(e)

    client_loop()

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