from pynput.keyboard import Key, Controller
import time

time.sleep(3)

keyboard = Controller()
                       
keyboard.press(Key.ctrl)
keyboard.press('t')

#time.sleep(1)

keyboard.release(Key.ctrl)
keyboard.release('t')