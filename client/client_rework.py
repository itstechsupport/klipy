import socket
import os
import threading
from win32api import GetSystemMetrics
import sys
from io import BytesIO
import PIL.Image, PIL.ImageFile, PIL.ImageTk
import dearpygui.dearpygui as dpg

PIL.ImageFile.LOAD_TRUNCATED_IMAGES = True

_width = int(GetSystemMetrics(0))
_height = int(GetSystemMetrics(1))

s = socket.socket()

v = '0.1.0'

class client():
    buffer = 102400
    def screen_loop(self): 
        while True:
            try:
                screen = s.recv(102400)
                bytes = bytearray(screen)
                stream = BytesIO(bytes)
                image = PIL.Image.open(stream)
                size = int(sys.getsizeof(stream))
                #display frame
                if size >= 100:
                    tk_image = PIL.ImageTk.PhotoImage(image)
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

def connect():
    try:
        hostname = dpg.get_value("hostname")
        print(hostname)
        hostname = hostname.split(":")
        print(hostname)
        host = hostname[0]
        port = hostname[1]
        s.connect((host, port))
        print(host = hostname[0], port = hostname[1])
        client()
        pass
    except Exception as e:
        print("  > Enter valid hostname and port!")
        print(e)


class interface():
    def __init__(self):
        dpg.create_context()
        dpg.create_viewport(title="Klipy", width=_width, height=_height)
        dpg.setup_dearpygui()
        dpg.maximize_viewport()
        self.menu()
    def menu(self):
        with dpg.window(label="Menu", tag="menu", pos=(_width/2-125, _height/2.5-200), no_title_bar=True, no_resize=True, no_move=True, width=250, height=500):
            dpg.add_text(f"Klipy {v}")
            dpg.add_text("")
            dpg.add_text("Connect")
            dpg.add_input_text(label="Hostname", tag="hostname")
            dpg.add_button(label="Connect", callback=connect())
            dpg.add_slider_float(label="float")
            #dpg.set_primary_window("menu", True)


interface()


def refresh():
    while dpg.is_dearpygui_running():
        print("this will run every frame")
        dpg.render_dearpygui_frame()

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()