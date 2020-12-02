import imutils
import cv2
import numpy as np
import pyautogui
import math
from datetime import datetime
import pydirectinput
import time
from motion_detection_1280.data_struct_fishing import *
import os


# =============================================================================
# USER-SET PARAMETERS
# =============================================================================

# Number of frames to pass before changing the frame to compare the current
# frame against
FRAMES_TO_PERSIST = 10

# Minimum boxed area for a detected motion to count as actual motion
# Use to filter out noise or small objects
MIN_SIZE_FOR_MOVEMENT = 2000

# Minimum length of time where no motion is detected it should take
# (in program cycles) for the program to declare that there is no movement
MOVEMENT_DETECTED_PERSISTENCE = 100
x_0_circle = data_struct['circle_center_x']
y_0_circle = data_struct['circle_center_y']

x_start_detection = data_struct['x_start_detection']
y_start_detection = data_struct['y_start_detection']
detection_field = data_struct['detection_field']
resize = data_struct['resize']
previous_x_check = None
previous_y_check = None
dif_x_counter = 0
dif_y_counter = 0
picture_take_counter = 0
image_check_counter = 0
image_log_counter = 0
picture_take_counter = 0
to_do_command = None
item_classify_picture_name = None

file_name = 'final_circle_after_metin_start.png'


worm_counter_fails_count = 0


up_x = 0
up_y = 0
x_resolution = 1280
y_resolution = 1024

worm_counter = 0


# =============================================================================
# CORE PROGRAM
# =============================================================================


# Create capture object
cap = cv2.VideoCapture(5)  # Flush the stream
cap.release()
cap = cv2.VideoCapture(1)  # Then start the webcam


# Init frame variables
first_frame = None
next_frame = None

# Init display font and timeout counters
font = cv2.FONT_HERSHEY_SIMPLEX
delay_counter = 0
movement_persistent_counter = 0


'''
image = pyautogui.screenshot(region=(514, 276, 130, 130))
frame_ever = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("in_memory_to_disk_2.png", frame_ever)
'''

def actual_time():

    current_time = int(round(time.time() * 1000))
    return current_time

def update_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def delete_item(x_start_detection, y_start_detection, detection_field):
    print('delete')
    time.sleep(0.5)
    pydirectinput.click(int(x_start_detection + detection_field/2), int(y_start_detection + detection_field/2))
    time.sleep(0.5)
    pydirectinput.click(630,60)
    time.sleep(0.5)
    pydirectinput.click(601, 526)
    time.sleep(0.5)



def item_classify(c1, c2, c3):

    avg_c1_zr = 309
    avg_c2_zr = 222
    avg_c3_zr = 71

    if((c1 > (avg_c1_zr-4)) and (c1< (avg_c1_zr+4)) and (c2 > (avg_c2_zr-4)) and (c2< (avg_c2_zr+4)) and (c3 > (avg_c3_zr-4)) and (c3< (avg_c3_zr+4))):
        return 'zlota_ruda', None

    avg_c1_bf = 229
    avg_c2_bf = 226
    avg_c3_bf = 218

    if((c1 > (avg_c1_bf-4)) and (c1< (avg_c1_bf+4)) and (c2 > (avg_c2_bf-4)) and (c2< (avg_c2_bf+4)) and (c3 > (avg_c3_bf-4)) and (c3< (avg_c3_bf+4))):
        return 'biala_farba', 'delete'

    avg_c1_jcf = 171
    avg_c2_jcf = 67
    avg_c3_jcf = 62

    if((c1 > (avg_c1_jcf-4)) and (c1< (avg_c1_jcf+4)) and (c2 > (avg_c2_jcf-4)) and (c2< (avg_c2_jcf+4)) and (c3 > (avg_c3_jcf-4)) and (c3< (avg_c3_jcf+4))):
        return 'jasno_czerwona_farba', 'delete'

    avg_c1_zf = 159
    avg_c2_zf = 147
    avg_c3_zf = 66

    if((c1 > (avg_c1_zf-4)) and (c1< (avg_c1_zf+4)) and (c2 > (avg_c2_zf-4)) and (c2< (avg_c2_zf+4)) and (c3 > (avg_c3_zf-4)) and (c3< (avg_c3_zf+4))):
        return 'zolta_farba', 'delete'

    avg_c1_ccf = 154
    avg_c2_ccf = 93
    avg_c3_ccf = 74

    if((c1 > (avg_c1_ccf-4)) and (c1< (avg_c1_ccf+4)) and (c2 > (avg_c2_ccf-4)) and (c2< (avg_c2_ccf+4)) and (c3 > (avg_c3_ccf-4)) and (c3< (avg_c3_ccf+4))):
        return 'ciemno_czerwona_farba', 'delete'

    avg_c1_zk = 147
    avg_c2_zk = 111
    avg_c3_zk = 51

    if((c1 > (avg_c1_zk-4)) and (c1< (avg_c1_zk+4)) and (c2 > (avg_c2_zk-4)) and (c2< (avg_c2_zk+4)) and (c3 > (avg_c3_zk-4)) and (c3< (avg_c3_zk+4))):
        return 'zloty_klucz', 'delete'

    avg_c1_pl = 121
    avg_c2_pl = 117
    avg_c3_pl = 76

    if((c1 > (avg_c1_pl-4)) and (c1< (avg_c1_pl+4)) and (c2 > (avg_c2_pl-4)) and (c2< (avg_c2_pl+4)) and (c3 > (avg_c3_pl-4)) and (c3< (avg_c3_pl+4))):
        return 'pierscien_lucy', 'delete'

    avg_c1_sk = 118
    avg_c2_sk = 92
    avg_c3_sk = 59

    if((c1 > (avg_c1_sk-4)) and (c1< (avg_c1_sk+4)) and (c2 > (avg_c2_sk-4)) and (c2< (avg_c2_sk+4)) and (c3 > (avg_c3_sk-4)) and (c3< (avg_c3_sk+4))):
        return 'symbol_krola', None

    avg_c1_zp = 110
    avg_c2_zp = 89
    avg_c3_zp = 59

    if((c1 > (avg_c1_zp-4)) and (c1< (avg_c1_zp+4)) and (c2 > (avg_c2_zp-4)) and (c2< (avg_c2_zp+4)) and (c3 > (avg_c3_zp-4)) and (c3< (avg_c3_zp+4))):
        return 'zloty_pierscien', None

    avg_c1_cf = 105
    avg_c2_cf = 103
    avg_c3_cf = 95

    if((c1 > (avg_c1_cf-4)) and (c1< (avg_c1_cf+4)) and (c2 > (avg_c2_cf-4)) and (c2< (avg_c2_cf+4)) and (c3 > (avg_c3_cf-4)) and (c3< (avg_c3_cf+4))):
        return 'czarna_farba', 'delete'

    avg_c1_skl = 100
    avg_c2_skl = 99
    avg_c3_skl = 104

    if((c1 > (avg_c1_skl-4)) and (c1< (avg_c1_skl+4)) and (c2 > (avg_c2_skl-4)) and (c2< (avg_c2_skl+4)) and (c3 > (avg_c3_skl-4)) and (c3< (avg_c3_skl+4))):
        return 'srebny_klucz', 'delete'

    avg_c1_pustka = 97
    avg_c2_pustka = 85
    avg_c3_pustka = 67

    if ((c1 > (avg_c1_pustka - 3)) and (c1 < (avg_c1_pustka + 3)) and (c2 > (avg_c2_pustka - 3)) and (
            c2 < (avg_c2_pustka + 3)) and (c3 > (avg_c3_pustka - 3)) and (c3 < (avg_c3_pustka + 3))):
        return 'puste', None

    avg_c1_nimfa = 79
    avg_c2_nimfa = 97
    avg_c3_nimfa = 104

    if ((c1 > (avg_c1_nimfa - 3)) and (c1 < (avg_c1_nimfa + 3)) and (c2 > (avg_c2_nimfa - 3)) and (
            c2 < (avg_c2_nimfa + 3)) and (c3 > (avg_c3_nimfa - 3)) and (c3 < (avg_c3_nimfa + 3))):
        return 'klucz_nimfy', None


    avg_c1_rkr = 76
    avg_c2_rkr = 75
    avg_c3_rkr = 44

    if((c1 > (avg_c1_rkr-4)) and (c1< (avg_c1_rkr+4)) and (c2 > (avg_c2_rkr-4)) and (c2< (avg_c2_rkr+4)) and (c3 > (avg_c3_rkr-4)) and (c3< (avg_c3_rkr+4))):
        return 'rekawica_krola', 'delete'

    avg_c1_wybielacz = 110
    avg_c2_wybielacz = 99
    avg_c3_wybielacz = 72

    if ((c1 > (avg_c1_wybielacz - 4)) and (c1 < (avg_c1_wybielacz + 4)) and (c2 > (avg_c2_wybielacz - 4)) and (
            c2 < (avg_c2_wybielacz + 4)) and (c3 > (avg_c3_wybielacz - 4)) and (c3 < (avg_c3_wybielacz + 4))):
        return 'wybielacz', 'delete'



    avg_c1_peleryna = 61
    avg_c2_peleryna = 60
    avg_c3_peleryna = 59

    if((c1 > (avg_c1_peleryna-4)) and (c1< (avg_c1_peleryna+4)) and (c2 > (avg_c2_peleryna-4)) and (c2< (avg_c2_peleryna+4)) and (c3 > (avg_c3_peleryna-4)) and (c3< (avg_c3_peleryna+4))):
        return 'peleryna', 'delete'

    else:
        return 'not_cassified', None

def restart_sequence(worm_counter, worm_counter_time):
    print("window center")
    pydirectinput.click(data_struct['screen_1_click_x'], data_struct['screen_1_click_y'])
    time.sleep(0.25)
    print("worm counter : " + str(worm_counter))

    if ((worm_counter % 10 == 0) & (worm_counter > 1)):
        time.sleep(0.25)
        pydirectinput.click(data_struct['open_fish_x'], data_struct['open_fish_y'])
        time.sleep(0.25)

    if ((worm_counter % 210 == 0) & (worm_counter > 1)):
    #if ((worm_counter % 210 == 0)):
        time.sleep(2)
        pydirectinput.click(data_struct['game_menu_x'], data_struct['game_menu_y'])
        print('game main menu')
        time.sleep(1)
        pydirectinput.click(data_struct['game_menu_relog_x'], data_struct['game_menu_relog_y'])
        print("relog")
        time.sleep(30)
        pydirectinput.click(data_struct['log_start_x'], data_struct['log_start_y'])
        print("log_start")
        time.sleep(30)
        # openinventory
        pydirectinput.click(data_struct['open_inventory_x'], data_struct['open_inventory_y'])
        print("open_inventory")
        time.sleep(5)

        while True:
            c1, c2, c3 = image_colors(1230, 530, 30, 30)
            print( int(c1), int(c2), int(c3))
            if(c1 > 85 and c1 <95 and c2 > 68 and c2 < 77 and c3 > 58 and c3 < 68):
                print("inventory oppened")
                break
            if (c1 > 251 and c1 < 261 and c2 > 213 and c2 < 223 and c3 > 129 and c3 < 139):
                print("not logged in ")
                pydirectinput.click(data_struct['log_start_x'], data_struct['log_start_y'])
                print("log_start")
                time.sleep(30)
                # openinventory
                pydirectinput.click(data_struct['open_inventory_x'], data_struct['open_inventory_y'])
                print("open_inventory")
                time.sleep(5)
            if (c1 > 630 and c1 < 640 and c2 > 372 and c2 < 382 and c3 > 240 and c3 < 250):
                print("not logged in 2")
                pydirectinput.click(data_struct['log_ok_x'], data_struct['log_ok_y'])
                print("log_ok")
                time.sleep(30)
                pydirectinput.click(data_struct['log_start_x'], data_struct['log_start_y'])
                print("log_start")
                time.sleep(30)
                # openinventory
                pydirectinput.click(data_struct['open_inventory_x'], data_struct['open_inventory_y'])
                print("open_inventory")
                time.sleep(5)
            else:
                print("inventory not oppened else should never ")
                pydirectinput.click(data_struct['log_ok_x'], data_struct['log_ok_y'])
                print("log_ok")
                time.sleep(30)
                pydirectinput.click(data_struct['log_start_x'], data_struct['log_start_y'])
                print("log_start")
                time.sleep(30)
                # openinventory
                pydirectinput.click(data_struct['open_inventory_x'], data_struct['open_inventory_y'])
                print("open_inventory")
                time.sleep(5)


    if((worm_counter % 50 == 0) & (worm_counter > 1)):
    #if (worm_counter % 75 == 0):
        x_start_1 = data_struct['x_start_1']
        y_start_1 = data_struct['y_start_1']
        x_start_2 = data_struct['x_start_1']
        y_start_2 = data_struct['y_start_2']
        jump_pixels = 32
        print("OPEN FISH CLICK SECURE")
        for y in range(5):
            for x in range(5):
                #print("x " + str(x) + " y " + str(y))
                pydirectinput.moveTo(x_start_1 + x * jump_pixels + up_x, y_start_1 + y * jump_pixels + up_y)
                time.sleep(0.5)
                to_open = save_picture(x_start_1 + x * jump_pixels + up_x - 13,
                             y_start_1 + y * jump_pixels + up_y - 13, 26, worm_counter)

                if(to_open != 'delete'):
                    pydirectinput.doubleClick(x_start_1 + x * jump_pixels + up_x, y_start_1 + y * jump_pixels + up_y)
                #time.sleep(0.5)
                #save_picture(x_start_1 + x * jump_pixels + up_x - 13,
                #             y_start_1 + y * jump_pixels + up_y - 13, 26, worm_counter)
                print("OPEN FISH IN INVENTORY")
        #second page
        pydirectinput.click(data_struct['second_page_x'], data_struct['second_page_y'])
        pydirectinput.click(data_struct['second_page_x'], data_struct['second_page_y'])
        pydirectinput.moveTo(x_start_2, y_start_2)
        pydirectinput.moveTo(x_start_2, y_start_2)
        print("SECOND PAGE OF INVENTORY")
        time.sleep(0.25)
        for y in range(6):
            for x in range(5):
                #print("x " + str(x) + " y " + str(y))
                pydirectinput.moveTo(x_start_2 + x * jump_pixels + up_x, y_start_2 + y * jump_pixels + up_y)
                time.sleep(0.5)
                to_open = save_picture(x_start_2 + x * jump_pixels + up_x - 13,
                             y_start_2 + y * jump_pixels + up_y - 13, 26, worm_counter)
                if(to_open != 'delete'):
                    pydirectinput.doubleClick(x_start_2 + x * jump_pixels + up_x, y_start_2 + y * jump_pixels + up_y)
                #time.sleep(0.5)
                #save_picture(x_start_2 + x * jump_pixels + up_x - 13,
                #             y_start_2 + y * jump_pixels + up_y - 13, 26, worm_counter)
                print("OPEN FISH IN INVENTORY")

        #go back to the first page
        pydirectinput.click(data_struct['first_page_x'], data_struct['first_page_y'])
        pydirectinput.click(data_struct['first_page_x'], data_struct['first_page_y'])
        print("FIRST PAGE OF INVENTORY")
        time.sleep(0.25)
        pydirectinput.doubleClick(1210,581)
        time.sleep(0.25)
        pydirectinput.doubleClick(1210, 581)

    if(worm_counter <= 195):
        pydirectinput.press('1')
        time.sleep(1)
        pydirectinput.press('space')
        worm_counter = worm_counter + 1
    if((worm_counter > 195) & (worm_counter <= 395)):
        pydirectinput.press('2')
        time.sleep(1)
        pydirectinput.press('space')
        worm_counter = worm_counter + 1
    if((worm_counter > 395) & (worm_counter <= 595)):
        pydirectinput.press('3')
        time.sleep(1)
        pydirectinput.press('space')
        worm_counter = worm_counter + 1
    if((worm_counter > 595) & (worm_counter <= 795)):
        pydirectinput.press('4')
        time.sleep(1)
        pydirectinput.press('space')
        worm_counter = worm_counter + 1
    if((worm_counter > 795) & (worm_counter <= 995)):
        pydirectinput.press('f1')
        time.sleep(1)
        pydirectinput.press('space')
        worm_counter = worm_counter + 1
    if((worm_counter > 995) & (worm_counter <= 1195)):
        pydirectinput.press('f2')
        time.sleep(1)
        pydirectinput.press('space')
        worm_counter = worm_counter + 1
    if((worm_counter > 1195) & (worm_counter <= 1395)):
        pydirectinput.press('f3')
        time.sleep(1)
        pydirectinput.press('space')
        worm_counter = worm_counter + 1
    if((worm_counter > 1395) & (worm_counter <= 1595)):
        pydirectinput.press('f4')
        time.sleep(1)
        pydirectinput.press('space')
        worm_counter = worm_counter + 1

    worm_counter_time = actual_time()

    return worm_counter, worm_counter_time

def save_picture(x_start_detection, y_start_detection, detection_field, picture_take_counter, *args):
    f = open("test_pictures\\log.txt", "a")
    image = pyautogui.screenshot(region=(x_start_detection, y_start_detection, detection_field, detection_field))
    frame_ever = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    #image.show()
    colors = image.convert("RGB")
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
    sum_c1 = int(sum_c1 / length)
    sum_c2 = int(sum_c2 / length)
    sum_c3 = int(sum_c3 / length)

    item_classify_picture_name, to_do_command = item_classify(sum_c1, sum_c2, sum_c3)

    print("classified as : " + str(item_classify_picture_name) + "     with c1 = " +  str(sum_c1) + " and c2 = " +  str(sum_c2)+ " and c3 = " + str(sum_c3))

    if((item_classify_picture_name != 'puste') and (to_do_command == 'delete')):
        cv2.imwrite("test_pictures\\"+str(item_classify_picture_name)+'_'+ str(picture_take_counter) + "_" + str(sum_c1) + "_" + str(sum_c2) + "_" + str(sum_c3) +" .png", frame_ever)
        f.write(str(picture_take_counter) + "     " + str(item_classify_picture_name)+ " " + str(sum_c1) + " " + str(sum_c2) + " " + str(sum_c3) + '\n')
    to_open = None
    if((to_do_command == 'delete') and (len(args) == 0)) :
        delete_item(x_start_detection, y_start_detection, detection_field)
        to_open = 'delete'
    if((item_classify_picture_name == 'puste') or (item_classify_picture_name == 'symbol_krola')):
        to_open = 'delete'
    #print(c1, c2, c3)
    #print("in_memory_to_disk_" + str(picture_take_counter) + " .png")
    #print(str(picture_take_counter) + "    :" + str(sum_c1) + " " + str(sum_c2) + " " + str(sum_c3) )
    time.sleep(0.5)
    f.close()
    return to_open






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
    return int(sum_c1), int(sum_c2), int(sum_c3)


frame_ever = cv2.imread(file_name,-1)
frame_ever = imutils.resize(frame_ever, width=750)
frame_ever = cv2.cvtColor(frame_ever, cv2.COLOR_BGR2GRAY)
frame_ever = cv2.GaussianBlur(frame_ever, (21, 21), 0)

current_time = actual_time()
fishing_cooldown_time = actual_time()
fishing_itself_last_recognise = actual_time()

worm_counter_time_after = actual_time()

worm_counter, worm_counter_time_after = restart_sequence(worm_counter, worm_counter_time_after)
# LOOP!
while True:
    current_time = actual_time()
    # Set transient motion detected as false
    transient_movement_flag = False

    #########################################################

    image = pyautogui.screenshot(region=(x_start_detection + up_x, y_start_detection + up_y, detection_field, detection_field))
    frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    #img = ImageGrab.grab(bbox=(514, 276, 645, 406))
    #frame = np.array(img)
    # Read frame

    #########################################################
    # Resize and save a greyscale version of the image
    frame = imutils.resize(frame, width=750)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur it to remove camera noise (reducing false positives)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # If the first frame is nothing, initialise it
    #if first_frame is None : first_frame = gray


    delay_counter += 1

    # Otherwise, set the first frame to compare as the previous frame
    # But only if the counter reaches the appriopriate value
    # The delay is to allow relatively slow motions to be counted as large
    # motions if they're spread out far enough
    #if delay_counter > FRAMES_TO_PERSIST:
    #    delay_counter = 0
    #    first_frame = first_frame

    # Set the next frame to compare (the current frame)
    next_frame = gray

    # Compare the two frames, find the difference
    frame_delta = cv2.absdiff(frame_ever, next_frame)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

    # Fill in holes via dilate(), and find contours of the thesholds
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts , _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # loop over the contours
    for c in cnts:

        # Save the coordinates of all found contours
        (x, y, w, h) = cv2.boundingRect(c)

        # If the contour is too small, ignore it, otherwise, there's transient
        # movement
        if cv2.contourArea(c) > MIN_SIZE_FOR_MOVEMENT:
            transient_movement_flag = True

            # Draw a rectangle around big enough movements
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #compare with resize
            x_check = int(x/resize + x_start_detection + w/2/resize)
            if previous_x_check is None: previous_x_check = x_check
            y_check = int(y/resize + y_start_detection + h/2/resize)
            if previous_y_check is None: previous_y_check = y_check

            points_check_distance = int(math.sqrt((x_check - x_0_circle)**2 + (y_check - y_0_circle)**2))
            diagonal_of_rectangle = int(math.sqrt(w*w+h*h))

            if ((diagonal_of_rectangle > 100) & (diagonal_of_rectangle < 200) & (points_check_distance < 68)):
                fishing_itself_last_recognise = actual_time()
                if (abs(x_check - previous_x_check) <= 5):
                    dif_x_counter = dif_x_counter + 1
                elif (abs(x_check - previous_x_check) > 5):
                    dif_x_counter = 0
                    previous_x_check = x_check
                if (abs(y_check - previous_y_check) <= 5):
                    dif_y_counter = dif_y_counter + 1
                elif (abs(y_check - previous_x_check) > 5):
                    dif_y_counter = 0
                    previous_y_check = y_check
                tt = current_time
                ts = fishing_cooldown_time
                tc = 400
                if (((tt - ts > tc) or (tt - ts < 0))& (dif_x_counter > 1 ) & (dif_y_counter > 1)):
                    pydirectinput.click(int(x_check) + up_x, int(y_check)+up_y)
                    print('hunt')
                    fishing_cooldown_time = actual_time()

            if(diagonal_of_rectangle > 1040): image_check_counter = image_check_counter + 1
            if(image_check_counter > 50):
                time.sleep(2)
                worm_counter, worm_counter_time_after = restart_sequence(worm_counter, worm_counter_time_after)
                time.sleep(1.5)
                image_check_counter = 0
    if ((worm_counter % 210 == 0) & (worm_counter > 1)):
        fishing_itself_last_recognise = actual_time()
        fishing_itself_last_recognise = actual_time()


    if((fishing_itself_last_recognise - worm_counter_time_after) < -300000):
        clock_time = update_time()
        print('TASK KILL :' + str(clock_time))
        os.system("taskkill /f /im  metin2client.exe")
        time.sleep(10)
        #gamefroge client
        pydirectinput.click(data_struct['gameforge_client_x'], data_struct['gameforge_client_y'])
        print("gameforge_client_x")
        #rungame
        time.sleep(2)
        pydirectinput.click(data_struct['run_game_x'], data_struct['run_game_y'])
        print("run_game_x")
        time.sleep(2)
        #gameforge client hide
        pydirectinput.click(data_struct['gameforge_client_x'], data_struct['gameforge_client_y'])
        print("gameforge_client_x")
        time.sleep(30)
        #ok
        pydirectinput.click(data_struct['log_ok_x'], data_struct['log_ok_y'])
        print("log_ok")
        time.sleep(60)
        #start
        pydirectinput.click(data_struct['log_start_x'], data_struct['log_start_y'])
        print("log_start")
        time.sleep(60)
        #openinventory
        pydirectinput.click(data_struct['open_inventory_x'], data_struct['open_inventory_y'])
        print("open_inventory")
        time.sleep(5)
        fishing_itself_last_recognise = actual_time()
        fishing_itself_last_recognise = actual_time()



    if(image_log_counter > 5000):
        print("is logeout check")
        c1, c2, c3 = image_colors(data_struct['logout_v1'], data_struct['logout_v2'], 200, 6)
        if ((c1 < data_struct['login_c1_min']) or (c1 > data_struct['login_c1_max']) & \
                ((c2 < data_struct['login_c2_min']) or (c2 > data_struct['login_c2_max']) & \
                ((c3 < data_struct['login_c3_min']) or (c3 > data_struct['login_c3_max'])))):
            time.sleep(30)
            pydirectinput.click(data_struct['log_ok_x'], data_struct['log_ok_y'])
            time.sleep(30)
            pydirectinput.click(data_struct['log_start_x'], data_struct['log_start_y'])
            time.sleep(30)
            pydirectinput.click(data_struct['open_inventory_x'], data_struct['open_inventory_y'])
            print("open_inventory")
            time.sleep(5)
            print("PASS")
        image_log_counter = 0




    image_log_counter = image_log_counter + 1



    # The moment something moves momentarily, reset the persistent
    # movement timer.
    if transient_movement_flag == True:
        movement_persistent_flag = True
        movement_persistent_counter = MOVEMENT_DETECTED_PERSISTENCE

    # As long as there was a recent transient movement, say a movement
    # was detected
    if movement_persistent_counter > 0:
        text = "Movement Detected " + str(movement_persistent_counter)
        movement_persistent_counter -= 1
    else:
        text = "No Movement Detected"

    # Print the text on the screen, and display the raw and processed video
    # feeds
    cv2.putText(frame, str(text), (10, 35), font, 0.30, (255, 255, 255), 2, cv2.LINE_AA)

    # For if you want to show the individual video frames
    #    cv2.imshow("frame", frame)
    #cv2.imshow("delta", frame_delta)

    # Convert the frame_delta to color for splicing
    frame_delta = cv2.cvtColor(frame_delta, cv2.COLOR_GRAY2BGR)

    # Splice the two video frames together to make one long horizontal one
    cv2.imshow("frame", np.hstack((frame_delta, frame)))

    # Interrupt trigger by pressing q to quit the open CV program
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

# Cleanup when closed
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()