import pyscreenshot as ImageGrab
import numpy as np
import pydirectinput
import time
from datetime import datetime
from autohuntmt2.data_struct import *

empty_var = None
#metin window
up_x = 1
up_y = 1
x_resolution = 1920
y_resolution = 1080


def scale_x(input):
    output = int(up_x + input*x_resolution)
    #print(output)
    return output


def scale_y(input):
    output = int(up_y + input*y_resolution)
    #print(output)
    return output


screen_1_click = (scale_x(data_struct['screen_1_click_x']), scale_y(data_struct['screen_1_click_y']))
screen_2_click = (scale_x(data_struct['screen_1_click_x']) + x_resolution, scale_y(data_struct['screen_1_click_y']))
hp_count = 0
hp_wp_50_60 = (scale_x(data_struct['hp_wp_50_60_v1']), scale_y(data_struct['hp_wp_50_60_v2']),
               scale_x(data_struct['hp_wp_50_60_v3']), scale_y(data_struct['hp_wp_50_60_v4']))
mp_wp_50_60 = (scale_x(data_struct['mp_wp_50_60_v1']), scale_y(data_struct['mp_wp_50_60_v2']),
               scale_x(data_struct['mp_wp_50_60_v3']), scale_y(data_struct['mp_wp_50_60_v4']))


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
'''
f2_cooldown = 161
f1_buff_cooldown = 35
f2_buff_cooldown = 20
'''
#swierzyna
mulitply = 0.8
f2_cooldown = 55
three_cooldown = 100*mulitply
four_cooldown = 105*mulitply




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

'''
def if_statement(c1, c2, c3, c1_min, c1_max, c2_min, c2_max, c3_min, c3_max, function):
    if (c1 > c1_min) & (c1 < c1_max) & (c2 > c2_min) & (c2 < c2_max) & (c3 > c3_min) & (c3 < c3_max):
        #sms("P1 pt dead "+ str(current_time))
        print("if_statement start")
        function()
'''

def if_statement(c1, c2, c3, c1_min, c1_max, c2_min, c2_max, c3_min, c3_max, function, mode, *args):
    if(mode == 'hp'):
        if (c1 > c1_min) & (c1 < c1_max) & (c2 > c2_min) & (c2 < c2_max) & (c3 > c3_min) & (c3 < c3_max):
            #sms("P1 pt dead "+ str(current_time))
            function()
            hp_count = args[0]
            hp_count = hp_count + 1
            if (hp_count > 50):
                #resp_click
                time.sleep(10)
                pydirectinput.click(scale_x(data_struct['resp_click_x']), scale_y(data_struct['resp_click_y']))
                hp_count = 0
                time.sleep(1)
                heal_hp()
                time.sleep(1)
                heal_hp()
                time.sleep(5)
                #autolowy
                pydirectinput.click(scale_x(data_struct['autolowy_autolowy_x']), scale_y(data_struct['autolowy_autolowy_y']))
                time.sleep(1)
                #atak
                pydirectinput.click(scale_x(data_struct['autolowy_atak_x']), scale_y(data_struct['autolowy_atak_y']))
                time.sleep(0.25)
                # exit
                pydirectinput.click(scale_x(data_struct['autolowy_exit_x']), scale_y(data_struct['autolowy_exit_y']))
                time.sleep(0.25)
                start_skills("dupa")

            return hp_count
        else:
            hp_count = 0
            return hp_count
    if (mode == 'mp'):
        if (c1 > c1_min) & (c1 < c1_max) & (c2 > c2_min) & (c2 < c2_max) & (c3 > c3_min) & (c3 < c3_max):
            # sms("P1 pt dead "+ str(current_time))
            function()
    if (mode =='logout'):
        if (c1 > c1_min) & (c1 < c1_max) & (c2 > c2_min) & (c2 < c2_max) & (c3 > c3_min) & (c3 < c3_max):
            function()
    if (mode =='is_logged'):
        if (c1 > c1_min) & (c1 < c1_max) & (c2 > c2_min) & (c2 < c2_max) & (c3 > c3_min) & (c3 < c3_max):
            print(c1, c2, c3)
            return False
        else:
            return True


def heal_hp():
    print("heal hp")
    pydirectinput.click(screen_1_click[0], screen_1_click[1])
    time.sleep(0.25)
    pydirectinput.press('1')
'''
def press_z():
    print("z pressed")
    pydirectinput.click(screen_1_click[0], screen_1_click[1])
    time.sleep(0.25)
    pydirectinput.press('z')
'''

def logged_out():
    check = True
    while check:
        time.sleep(30)
        pydirectinput.click(scale_x(data_struct['log_ok_x']), scale_y(data_struct['log_ok_y']))
        time.sleep(30)
        pydirectinput.click(scale_x(data_struct['log_start_x']), scale_y(data_struct['log_start_y']))
        time.sleep(30)
        check = logout_check('is_logged')
        print(check)
        time.sleep(20)
    print("logged out start skills")
    start_skills()

def heal_mp():
    print("heal mp")
    pydirectinput.click(screen_1_click[0], screen_1_click[1])
    time.sleep(0.25)
    pydirectinput.press('2')


def start_skills(*args):
    pydirectinput.click(screen_1_click[0], screen_1_click[1])
    time.sleep(0.25)
    pydirectinput.press('f2')
    time.sleep(2)
    #pydirectinput.press('3')
    #time.sleep(2)
    #pydirectinput.press('4')
    #time.sleep(2)wa
    #menuuu
    if len(args)== 0:
        pydirectinput.click(scale_x(data_struct['autolowy_menu_x']), scale_y(data_struct['autolowy_menu_y']))
        time.sleep(1)
        #autolowy
        pydirectinput.click(scale_x(data_struct['autolowy_autolowy_x']), scale_y(data_struct['autolowy_autolowy_y']))
        time.sleep(1)
        #start
        pydirectinput.click(scale_x(data_struct['autolowy_start_x']), scale_y(data_struct['autolowy_start_y']))
        time.sleep(0.25)
        #focus
        pydirectinput.click(scale_x(data_struct['autolowy_focus_x']), scale_y(data_struct['autolowy_focus_y']))
        time.sleep(0.25)
        #atak
        pydirectinput.click(scale_x(data_struct['autolowy_atak_x']), scale_y(data_struct['autolowy_atak_y']))
        time.sleep(0.25)
        #exit
        pydirectinput.click(scale_x(data_struct['autolowy_exit_x']), scale_y(data_struct['autolowy_exit_y']))
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
        #mousclick for resurection when second window is in the party
        #pydirectinput.click(2013, 97)
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
        #pydirectinput.click(2013, 97)
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


def healing_hp(hp_count):
    w1, w2, w3 = image_colors(hp_wp_50_60[0], hp_wp_50_60[1], hp_wp_50_60[2],
                                                                  hp_wp_50_60[3])
    print("HP STATUS")
    print(w1)
    print(w2)
    print(w3)
    hp_count = if_statement(w1, w2, w3, data_struct['hp_c1_min'], data_struct['hp_c1_max'], data_struct['hp_c2_min'],
                            data_struct['hp_c2_max'], data_struct['hp_c3_min'], data_struct['hp_c3_max'], heal_hp,
                            'hp', hp_count)

    print("hp_count: " + str(hp_count))
    return hp_count


def healing_mp():
    w1, w2, w3 = image_colors(mp_wp_50_60[0], mp_wp_50_60[1], mp_wp_50_60[2], mp_wp_50_60[3])
    print("MANA STATUS")
    print(w1)
    print(w2)
    print(w3)
    if_statement(w1, w2, w3, data_struct['mp_c1_min'], data_struct['mp_c1_max'], data_struct['mp_c2_min'],
                 data_struct['mp_c2_max'], data_struct['mp_c3_min'], data_struct['mp_c3_max'], heal_mp, 'mp')

def logout_check(mode):

    w1, w2, w3 = image_colors(scale_x(data_struct['logout_v1']), scale_y(data_struct['logout_v2']),
                              scale_x(data_struct['logout_v3']),scale_y(data_struct['logout_v4']))
    if (mode == 'logout'):
        if_statement(w1, w2, w3, data_struct['logout_c1_min'], data_struct['logout_c1_max'], data_struct['logout_c2_min'],
                     data_struct['logout_c2_max'], data_struct['logout_c3_min'], data_struct['logout_c3_max'],  logged_out, 'logout')
    if (mode == 'is_logged'):
       return if_statement(w1, w2, w3, data_struct['login_c1_min'], data_struct['login_c1_max'], data_struct['login_c2_min'],
                     data_struct['login_c2_max'], data_struct['login_c3_min'], data_struct['login_c3_max'],  empty_var, 'is_logged')




###############################################DEBUG#####################################################################

#image_colors(hp_wp_50_60[0], hp_wp_50_60[1], hp_wp_50_60[2], hp_wp_50_60[3])
#image_colors(mp_wp_50_60[0], mp_wp_50_60[1], mp_wp_50_60[2], mp_wp_50_60[3])
''''
w1, w2, w3 = image_colors(scale_x(data_struct['logout_v1']), scale_y(data_struct['logout_v2']), scale_x(data_struct['logout_v3']),
                                                              scale_y(data_struct['logout_v4']))
print(w1)
print(w2)
print(w3)

###############################################DEBUG#####################################################################
'''
#init setup
hp_count = healing_hp(hp_count)
start_skills()
current_time = actual_time()
f2_time = actual_time()
three_time = actual_time()
four_time = actual_time()


f1_buff_time = actual_time()
f2_buff_time = actual_time()

while True:
    current_time = actual_time()
    logout_check('logout')

    ####hp and mp heal

    hp_count = healing_hp(hp_count)
    healing_mp()
    logout_check('logout')


    #####mainw window skills
    f2_time = skill_check(current_time, f2_time, f2_cooldown, 'f2')


    #press_z()
    #three_time = skill_check(current_time, three_time, three_cooldown, '3')
    #four_time = skill_check(current_time, four_time, four_cooldown, '4')

    #sekond window skill
    ##f1_buff_time = skill_check_buff(current_time, f1_buff_time, f1_buff_cooldown, 'f1')
    ##f2_buff_time = skill_check_buff(current_time, f2_buff_time, f2_buff_cooldown, 'f2')



