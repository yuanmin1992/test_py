#coding=utf-8
from pynput import keyboard
from pynput.keyboard import Key, Controller

kb = Controller()

def on_release(key):
    try:
        if key.char == "q":
            kb.type(u'大家好！！！')
            kb.press(Key.enter)
            kb.release(Key.enter)

    except:
        pass

while True:
    with keyboard.Listener(
        on_release = on_release) as listener:
        listener.join()