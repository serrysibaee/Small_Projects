import time
import keyboard 
from pynput import keyboard as sd
from pynput.keyboard import Controller as con , Key as k

# The event listener will be running in this block
inputs = con()
def prin():
    # tab 1
    inputs.press(k.tab)
    inputs.release(k.tab)
    time.sleep(1.2)
    # tab 2
    inputs.press(k.tab)
    inputs.release(k.tab)
    time.sleep(1.2)
    # space
    inputs.press(k.space)
    inputs.release(k.space)
    time.sleep(1.2)
    # tab 3
    inputs.press(k.tab)
    inputs.release(k.tab)
    time.sleep(1.2)
    # PSU ID writitng
    inputs.type("218110246")
    # tab 4
    inputs.press(k.tab)
    inputs.release(k.tab)
    time.sleep(1.2)
    # Student Name writing
    inputs.type("Serry Sibaee")
    
    
    
    
with sd.Events() as events:
    for event in events:
        if event.key == sd.Key.esc:
            prin()
            break
        else:
            print('nothing wait for the form')


