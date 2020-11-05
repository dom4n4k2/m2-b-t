from pynput import keyboard

import time

true = True


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    time.sleep(0.5)
    if key == keyboard.Key.esc:
        # Stop listener
        #t1.join()
        keyboard.Listener.stop
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    if (true == True):
        keyboard.Listener.stop
    if (true == False):
        print("dupa")

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

listener.start()




