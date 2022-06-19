import pyautogui
import keyboard
import socket

s = socket.socket()

v = '0.0.1' #woah

purple = "\033[0;35m"
yellow = "\033[1;33"
green = "\033[1;36"
blank = "\033[0m"


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

def start():
    while True:
        key = keyboard.read_key()
        print(key)
        s.send(key.encode())
        

def connect(host, port):
    print(f"  > Connecting to {host}:{port}")
    try:
        s.connect((host, port))
        pass
    except Exception as e:
        print("  > Enter valid hostname and port!")
        print(e)

    start()

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
