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

"""
screen = pyautogui.screenshot()
screen.save('img.png')
screen = open('img.png', 'rb')
scren = screen.read()
bytes = bytearray(scren)



stream = BytesIO(bytes)

image = Image.open(stream).convert("RGBA")
stream.close()
image.show()
"""


c, addr = s.accept()
while True:

    #encode
    screen = pyautogui.screenshot()
    screen.save('img.png')
    screen = open('img.png', 'rb')
    scren = screen.read()
    bytes = bytearray(scren)

    #send
    c.send(bytes.encode(1024))

    #receive pressed key
    key = c.recv(1024).decode()

    pass

