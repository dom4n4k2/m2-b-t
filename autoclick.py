import pyautogui
import pydirectinput
import time



while True:
    pydirectinput.moveTo(93, 97)
    time.sleep(2)
    pydirectinput.click()
    time.sleep(2)
    pydirectinput.moveTo(2880, 17)
    pydirectinput.click()
    time.sleep(120)
    print("click")
    #pydirectinput.press('f2')