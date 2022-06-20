from anyio import open_signal_receiver
import pyautogui
import socket
from PIL import Image
from io import BytesIO

s = socket.socket()
print ("Socket successfully created")

port = 22371

s.bind(('', port))
print ("Socket binded to %s" %(port))

s.listen(5)
print ("Socket is listening")


screen = pyautogui.screenshot()
screen.save('img.png')
open_screen = open(screen, 'rb')
bytes = bytearray(screen.read)

stream = BytesIO(bytes)

image = Image.open(stream).convert("RGBA")
stream.close()
image.show()



c, addr = s.accept()
while True:
    screen = open(pyautogui.screenshot(), 'rb')
    bytes = bytearray(screen.read)
    c.sendall(bytes)
    key = c.recv(1024).decode()
    #print(key)
    pass

