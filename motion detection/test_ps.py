import cv2
import numpy as np
import pyautogui
import time


counter = 0
while True:
    image = pyautogui.screenshot(region=(509, 272, 138, 138))
    frame_ever = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("dupa\\in_memory_to_disk_" + str(counter)+ " .png", frame_ever)
    time.sleep(5)
    counter = counter +1
