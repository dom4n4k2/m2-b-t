import pyscreenshot as ImageGrab
import numpy as np
import pydirectinput
import time
from datetime import datetime


up_x = 1
up_y=  1
down_x = 1920
down_y = 1080
screen_1_click = (950, 15)
screen_2_click = (2870, 15)
hp_count = 0

hp_wp_50_60 = (up_x+126, up_y+1011, up_x+136, up_y+1019)
mp_wp_50_60 = (up_x+106, up_y+1023, up_x+116, up_y+1029)

def image_colors(x_up,y_up, x_down, y_down):
    im=ImageGrab.grab(bbox=(x_up, y_up, x_down, y_down))
    im.show()
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
        i = i +1
    sum_c1 = sum_c1 / length
    sum_c2 = sum_c2 / length
    sum_c3 = sum_c3 / length
    print(sum_c1)
    print(sum_c2)
    print(sum_c3)

    return

image_colors(mp_wp_50_60[0], mp_wp_50_60[1], mp_wp_50_60[2], mp_wp_50_60[3])
