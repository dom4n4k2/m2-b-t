import imutils
import cv2
import numpy as np
import pyautogui
import math
from datetime import datetime
import pydirectinput
import time
from motion_detection.data_struct_fishing import *
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
image_check_counter = 0
image_log_counter = 0
file_name = 'final_circle_after_metin_start.png'


worm_counter_fails_count = 0


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


def restart_sequence(worm_counter, worm_counter_time):
    print("window center")
    pydirectinput.click(scale_x(data_struct['screen_1_click_x']), scale_y(data_struct['screen_1_click_y']))
    time.sleep(0.25)
    print("worm counter : " + str(worm_counter))

    if ((worm_counter % 200 == 0) & (worm_counter > 1)):

        time.sleep(5)
        pydirectinput.click(scale_x(data_struct['game_menu_x']), scale_y(data_struct['game_menu_y']))
        print('game main menu')
        time.sleep(1)
        pydirectinput.click(scale_x(data_struct['game_menu_relog_x']), scale_y(data_struct['game_menu_relog_y']))
        print("relog")
        time.sleep(10)
        pydirectinput.click(scale_x(data_struct['log_start_x']), scale_y(data_struct['log_start_y']))
        print("log_start")
        time.sleep(30)
        # openinventory
        pydirectinput.click(scale_x(data_struct['open_inventory_x']), scale_y(data_struct['open_inventory_y']))
        print("open_inventory")
        time.sleep(5)




    if((worm_counter % 20 == 0) & (worm_counter > 1)):
    #if (worm_counter % 20 == 0):
        x_start_1 = scale_x(data_struct['x_start_1'])
        y_start_1 = scale_y(data_struct['y_start_1'])

        x_start_2 = scale_x(data_struct['x_start_1'])
        y_start_2 = scale_y(data_struct['y_start_2'])

        jump_pixels = 32

        pydirectinput.click(scale_x(data_struct['open_fish_x']), scale_y(data_struct['open_fish_y']))
        print("OPEN FISH CLICK SECURE")
        picture_take_counter = 0
        for y in range(5):
            for x in range(5):
                #print("x " + str(x) + " y " + str(y))
                pydirectinput.doubleClick(x_start_1 + x * jump_pixels + up_x, y_start_1 + y * jump_pixels + up_y)
                #time.sleep(0.1)
                #save_picture(x_start_1 + x * jump_pixels + up_x - 13,
                #             y_start_1 + y * jump_pixels + up_y - 13, 26, picture_take_counter)
                #picture_take_counter = picture_take_counter + 1
                print("OPEN FISH IN INVENTORY")
                time.sleep(0.25)
        #second page
        pydirectinput.click(scale_x(data_struct['second_page_x']), scale_y(data_struct['second_page_y']))
        print("SECOND PAGE OF INVENTORY")
        time.sleep(0.25)
        for y in range(6):
            for x in range(5):
                #print("x " + str(x) + " y " + str(y))
                pydirectinput.doubleClick(x_start_2 + x * jump_pixels + up_x, y_start_2 + y * jump_pixels + up_y)
                #time.sleep(0.1)
                #save_picture(x_start_2 + x * jump_pixels + up_x - 13,
                #             y_start_2 + y * jump_pixels + up_y - 13, 26, picture_take_counter)
                #picture_take_counter = picture_take_counter + 1
                print("OPEN FISH IN INVENTORY")
                time.sleep(0.25)
        picture_take_counter = 0
        #go back to the first page
        pydirectinput.click(scale_x(data_struct['first_page_x']), scale_y(data_struct['first_page_y']))
        print("FIRST PAGE OF INVENTORY")
        time.sleep(0.25)

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

def save_picture(x_start_detection, y_start_detection, detection_field, picture_take_counter):
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
    sum_c1 = sum_c1 / length
    sum_c2 = sum_c2 / length
    sum_c3 = sum_c3 / length


    #print(c1, c2, c3)
    #print("in_memory_to_disk_" + str(picture_take_counter) + " .png")
    #print(str(picture_take_counter) + "    :" + str(sum_c1) + " " + str(sum_c2) + " " + str(sum_c3) )
    cv2.imwrite("test_pictures\\in_memory_to_disk_" + str(picture_take_counter)+ " .png", frame_ever)
    f.write(str(picture_take_counter) + "    :" + str(sum_c1) + " " + str(sum_c2) + " " + str(sum_c3) + '\n')
    time.sleep(0.5)
    f.close()




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
    if ((worm_counter % 200 == 0) & (worm_counter > 1)):
        fishing_itself_last_recognise = actual_time()
        fishing_itself_last_recognise = actual_time()

    if((fishing_itself_last_recognise - worm_counter_time_after) < -100000):
        print('TASK KILL')
        os.system("taskkill /f /im  metin2client.exe")
        time.sleep(10)
        #gamefroge client
        pydirectinput.click(scale_x(data_struct['gameforge_client_x']), scale_y(data_struct['gameforge_client_y']))
        print("gameforge_client_x")
        #rungame
        time.sleep(2)
        pydirectinput.click(scale_x(data_struct['run_game_x']), scale_y(data_struct['run_game_y']))
        print("run_game_x")
        time.sleep(2)
        #gameforge client hide
        pydirectinput.click(scale_x(data_struct['gameforge_client_x']), scale_y(data_struct['gameforge_client_y']))
        print("gameforge_client_x")
        time.sleep(30)
        #ok
        pydirectinput.click(scale_x(data_struct['log_ok_x']), scale_y(data_struct['log_ok_y']))
        print("log_ok")
        time.sleep(30)
        #start
        pydirectinput.click(scale_x(data_struct['log_start_x']), scale_y(data_struct['log_start_y']))
        print("log_start")
        time.sleep(30)
        #openinventory
        pydirectinput.click(scale_x(data_struct['open_inventory_x']), scale_y(data_struct['open_inventory_y']))
        print("open_inventory")
        time.sleep(5)
        fishing_itself_last_recognise = actual_time()
        fishing_itself_last_recognise = actual_time()



    if(image_log_counter > 10000):
        print("is logedout check")
        c1, c2, c3 = image_colors(scale_x(data_struct['logout_v1']), scale_y(data_struct['logout_v2']), 416, 6)
        if ((c1 < data_struct['login_c1_min']) or (c1 > data_struct['login_c1_max'])) & \
                ((c2 < data_struct['login_c2_min']) or (c2 > data_struct['login_c2_max'])) & \
                ((c3 < data_struct['login_c3_min']) or (c3 > data_struct['login_c3_max'])):
            time.sleep(30)
            pydirectinput.click(scale_x(data_struct['log_ok_x']), scale_y(data_struct['log_ok_y']))
            time.sleep(30)
            pydirectinput.click(scale_x(data_struct['log_start_x']), scale_y(data_struct['log_start_y']))
            time.sleep(30)
            pydirectinput.click(scale_x(data_struct['open_inventory_x']), scale_y(data_struct['open_inventory_y']))
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
    #    cv2.imshow("delta", frame_delta)

    # Convert the frame_delta to color for splicing
    frame_delta = cv2.cvtColor(frame_delta, cv2.COLOR_GRAY2BGR)

    # Splice the two video frames together to make one long horizontal one
    #cv2.imshow("frame", np.hstack((frame_delta, frame)))

    # Interrupt trigger by pressing q to quit the open CV program
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

# Cleanup when closed
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()