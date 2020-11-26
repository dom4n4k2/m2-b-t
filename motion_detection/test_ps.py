import cv2
import numpy as np
import pyautogui
import time
from autohuntmt2.data_struct import *

up_x = 1
up_y = 1
x_resolution = 1920
y_resolution = 1080

x_start_detection = 509
y_start_detection = 272
detection_field = 138

def scale_x(input):
    output = int(up_x + input*x_resolution)
    #print(output)
    return output


def scale_y(input):
    output = int(up_y + input*y_resolution)
    #print(output)
    return output

def image_colors(x_up,y_up, width, height):
    im=pyautogui.screenshot(region=(x_up, y_up, width, height))
    #im.show()
    colors = im.convert("RGB")
    na = np.array(colors)
    colours, counts = np.unique(na.reshape(-1, 3), axis=0, return_counts=1)
    length = len(colours)
    i = 0
    sum_c1 = 0
    sum_c2 = 0
    sum_c3 = 0
    while i < length:

        sum_c1 = sum_c1 + counts[i] * colours[i][0]
        sum_c2 = sum_c2 + counts[i] * colours[i][1]
        sum_c3 = sum_c3 + counts[i] * colours[i][2]
        i = i + 1
    sum_c1 = sum_c1 / length
    sum_c2 = sum_c2 / length
    sum_c3 = sum_c3 / length

    return sum_c1, sum_c2, sum_c3
'''
counter = 0
while True:
    #image = pyautogui.screenshot(region=(scale_x(data_struct['logout_v1']), scale_y(data_struct['logout_v2']), 416, 6))
    image = pyautogui.screenshot(region=(x_start_detection, y_start_detection, detection_field, detection_field))
    frame_ever = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    c1,c2,c3 = image_colors(scale_x(data_struct['logout_v1']), scale_y(data_struct['logout_v2']), 416, 6)
    #print(c1, c2, c3)
    cv2.imwrite("test_pictures\\in_memory_to_disk_" + str(counter)+ " .png", frame_ever)
    time.sleep(0.25)
    counter = counter +1
'''

c1, c2, c3 = image_colors(1870, 584, 30, 30)
print( int(c1), int(c2), int(c3))