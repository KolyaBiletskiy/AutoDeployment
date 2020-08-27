import pynput
from pynput.keyboard import Key, Controller



keyboard = Controller()


keyboard.press(Key.cmd_l)
keyboard.press(Key.space)
keyboard.release(Key.cmd_l)
keyboard.release(Key.space)
