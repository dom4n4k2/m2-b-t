import pyscreenshot as ImageGrab
import numpy as np
import pydirectinput
import time
from datetime import datetime

#metin window
up_x = 1
up_y=  1
down_x = 1920
down_y = 1080
screen_1_click = (950, 15)
screen_2_click = (2870, 15)
hp_count = 0

hp_wp_50_60 = (up_x+126, up_y+1011, up_x+136, up_y+1019)
mp_wp_50_60 = (up_x+106, up_y+1023, up_x+116, up_y+1029)
#intymnis
'''
mulitply = 0.95
f2_cooldown = 175
three_cooldown = 20
four_cooldown = 20
f1_buff_cooldown = 20
f2_buff_cooldown = 20
'''
#bm

f2_cooldown = 161
f1_buff_cooldown = 35
f2_buff_cooldown = 20
'''
#swierzyna
mulitply = 0.8
f2_cooldown = 104*mulitply
three_cooldown = 100*mulitply
four_cooldown = 105*mulitply
'''
def image_colors(x_up,y_up, x_down, y_down):
    im=ImageGrab.grab(bbox=(x_up, y_up, x_down, y_down))
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
        i = i +1
    sum_c1 = sum_c1 / length
    sum_c2 = sum_c2 / length
    sum_c3 = sum_c3 / length

    return sum_c1, sum_c2, sum_c3


def if_statement(c1, c2, c3, c1_min, c1_max, c2_min, c2_max, c3_min, c3_max, function):
    if (c1 > c1_min) & (c1 < c1_max) & (c2 > c2_min) & (c2 < c2_max) & (c3 > c3_min) & (c3 < c3_max):
        #sms("P1 pt dead "+ str(current_time))
        print("if_statement start")
        function()

def if_statement_hp(c1, c2, c3, c1_min, c1_max, c2_min, c2_max, c3_min, c3_max, function, hp_count):
    if (c1 > c1_min) & (c1 < c1_max) & (c2 > c2_min) & (c2 < c2_max) & (c3 > c3_min) & (c3 < c3_max):
        #sms("P1 pt dead "+ str(current_time))
        print("if_statement start")
        function()
        hp_count = hp_count + 1
        if (hp_count > 50):
            pydirectinput.click(93, 97)
            time.sleep(1)
            heal_hp()
            time.sleep(1)
            heal_hp()
            time.sleep(5)
            #autolowy
            pydirectinput.click(1044, 990)
            time.sleep(1)
            #atak
            pydirectinput.click(1053, 627)
            start_skills()

        return hp_count
    else:
        hp_count = 0
        return hp_count



def heal_hp():
    print("heal hp")
    pydirectinput.click(screen_1_click[0], screen_1_click[1])
    time.sleep(0.25)
    pydirectinput.press('1')




def heal_mp():
    print("heal hp")
    pydirectinput.click(screen_1_click[0], screen_1_click[1])
    time.sleep(0.25)
    pydirectinput.press('2')


def start_skills():
    pydirectinput.click(screen_1_click[0], screen_1_click[1])
    time.sleep(0.25)
    pydirectinput.press('f2')
    time.sleep(2)
    #pydirectinput.press('3')
    #time.sleep(2)
    #pydirectinput.press('4')
    #time.sleep(2)
    #menuuu
    pydirectinput.click(1010, 1020)
    time.sleep(1)
    #autohunt
    pydirectinput.click(1044, 990)
    time.sleep(1)
    #start
    pydirectinput.click(963, 760)
    time.sleep(0.25)
    #focus
    pydirectinput.click(1053, 653)
    time.sleep(0.25)
    #atak
    pydirectinput.click(1053, 627)
    time.sleep(0.25)
    #exit
    pydirectinput.click(1074, 307)
    time.sleep(0.25)



def skill_check(current_time, skill_time, cooldown, keybar):

    tt = get_sec(current_time)
    ts = get_sec(skill_time)
    tc = cooldown
    print(tt-ts)
    if ((tt-ts > tc) or(tt-ts < 0)):

        pydirectinput.click(screen_1_click[0], screen_1_click[1])
        time.sleep(0.25)
        pydirectinput.press(keybar)
        print(keybar + " activated")
        pydirectinput.click(2013, 97)
        return actual_time()
    else:
        return skill_time


def skill_check_buff(current_time, skill_time, cooldown, keybar):

    tt = get_sec(current_time)
    ts = get_sec(skill_time)
    tc = cooldown
    print(tt-ts)
    if ((tt-ts > tc) or(tt-ts < 0)):

        pydirectinput.click(screen_2_click[0], screen_2_click[1])
        time.sleep(0.25)
        pydirectinput.press(keybar)
        print(keybar + " activated")
        pydirectinput.click(2013, 97)
        return actual_time()
    else:
        return skill_time


def actual_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)
#init setup
hp_wp_50_60_c1, hp_wp_50_60_c2, hp_wp_50_60_c3 = image_colors(hp_wp_50_60[0], hp_wp_50_60[1], hp_wp_50_60[2], hp_wp_50_60[3])
if_statement_hp(hp_wp_50_60_c1, hp_wp_50_60_c2, hp_wp_50_60_c3, 500, 650, 500, 650, 500, 650, heal_hp, hp_count)
start_skills()
current_time = actual_time()
f2_time = actual_time()
three_time = actual_time()
four_time = actual_time()
f1_buff_time = actual_time()
f2_buff_time = actual_time()

while True:
    current_time = actual_time()

    ####hp and mp heal
    hp_wp_50_60_c1, hp_wp_50_60_c2, hp_wp_50_60_c3 = image_colors(hp_wp_50_60[0], hp_wp_50_60[1], hp_wp_50_60[2], hp_wp_50_60[3])

    print(hp_wp_50_60_c1)
    print(hp_wp_50_60_c2)
    print(hp_wp_50_60_c3)

    hp_count = if_statement_hp(hp_wp_50_60_c1, hp_wp_50_60_c2, hp_wp_50_60_c3, 500, 650, 500, 650, 500, 650, heal_hp, hp_count)
    print("hp_count: " + str(hp_count))

    mp_wp_50_60_c1, mp_wp_50_60_c2, mp_wp_50_60_c3 = image_colors(mp_wp_50_60[0], mp_wp_50_60[1], mp_wp_50_60[2], mp_wp_50_60[3])

    print(mp_wp_50_60_c1)
    print(mp_wp_50_60_c2)
    print(mp_wp_50_60_c3)
    #for wp
    if_statement(mp_wp_50_60_c1, mp_wp_50_60_c2, mp_wp_50_60_c3, 350, 450, 350, 450, 350, 450, heal_mp)

    #####
    f2_time = skill_check(current_time, f2_time, f2_cooldown, 'f2')
    #three_time = skill_check(current_time, three_time, three_cooldown, '3')
    #four_time = skill_check(current_time, four_time, four_cooldown, '4')
    f1_buff_time = skill_check_buff(current_time, f1_buff_time, f1_buff_cooldown, 'f1')
    f2_buff_time = skill_check_buff(current_time, f2_buff_time, f2_buff_cooldown, 'f2')



