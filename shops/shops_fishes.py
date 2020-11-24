import imutils
import cv2
import numpy as np
import pyautogui
import math
from datetime import datetime
import pydirectinput
import time
from shops.data_struct_shops import  *
import os

up_x = 0
up_y = 0
x_resolution = 1920
y_resolution = 1080

worm_counter = 0

def scale_x(input):
    output = int(up_x + input*x_resolution)
    #print(output)
    return output


def scale_y(input):
    output = int(up_y + input*y_resolution)
    #print(output)
    return output


x_start_1 = scale_x(data_struct['x_start_1'])
y_start_1 = scale_y(data_struct['y_start_1'])
sleep_time = 0.200
jump_pixels = 32
pydirectinput.rightClick(1761,965)
time.sleep(1)
time.sleep(sleep_time)
pydirectinput.press(['s','k','l','e','p'])
time.sleep(sleep_time)
pydirectinput.click(928,558)
time.sleep(sleep_time)


for y in range(8):
    for x in range(5):
        pydirectinput.click(x_start_1 + x * jump_pixels + up_x, y_start_1 + y * jump_pixels + up_y)
        time.sleep(sleep_time)
        pydirectinput.move(-870, -271)
        time.sleep(sleep_time)
        pydirectinput.click()
        time.sleep(sleep_time)
        print('x : ' + str(x))
        print('y : ' + str(y))
        if((y<1) and (y >=0)):
            pydirectinput.press(['3','0','0','0','0','0','0','0',])
        if((y<2) and (y >=1)):
            pydirectinput.press(['6','0','0','0','0','0','0','0',])
        if((y<3) and (y >=2)):
            pydirectinput.press(['9','0','0','0','0','0','0',])
        if((y<4) and (y >=3)):
            pydirectinput.press(['1','1','0','0','0','0','0','0',])
        if((y<5) and (y >=4)):
            pydirectinput.press(['3','0','0','0','0','0','0'])
        if((y<6) and (y >=5)):
            pydirectinput.press(['4','4','0','0','0','0','0'])
        if((y<7) and (y >=6)):
            pydirectinput.press(['1','2','0','0','0','0','0'])
        if((y<8) and (y >=7)):
            pydirectinput.press(['2','4','0','0','0','0','0'])
        time.sleep(sleep_time)
        time.sleep(sleep_time)
        time.sleep(sleep_time)
        pydirectinput.click(927,585)

