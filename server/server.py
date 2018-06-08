#!/bin/env python2
import sys
import string
import serial
import os
#import numpy
from Xlib import display

# global
running = 1
drift = 2
last_x = 0
last_y = 0
sensibilidade_x = -(3.0)
sensibilidade_y = 3.0


def check_drift():
    if abs(int(x)) - abs(last_x) > drift:
        mouse_x = data_mouse["root_x"] + int(x) * sensibilidade_x

    if abs(int(y)) - abs(last_y) > drift:
        mouse_y = data_mouse["root_y"] + int(y) * sensibilidade_y

print("Iniciando Servidor")
handle_serial = serial.Serial('/dev/ttyUSB1', 115200)
while running:
    data_mouse = display.Display().screen().root.query_pointer()._data
    mouse_x = data_mouse["root_x"]
    mouse_y = data_mouse["root_y"]
    line = handle_serial.readline().replace("\r\n","").replace(" ","")
    data = line.split("|")
    #print data
    x = data[6].split("=")[1].replace(" ","").replace("\r\n","")
    y = data[4].split("=")[1].replace(" ","").replace("\r\n","")
    if y == "-2":# TODO
        y = "0"
    acao_1 = data[7].split("=")[1].replace(" ","").replace("\r\n","")
    print(x+":"+y)

    if acao_1 == "1":
            mouse_x = data_mouse["root_x"] + int(x) * sensibilidade_x
            mouse_y = data_mouse["root_y"] + int(y) * sensibilidade_y
            cmd = "xdotool mousemove {0} {1}".format(mouse_x, mouse_y)
            os.system(cmd)
    last_x = int(x)
    last_y = int(y)
