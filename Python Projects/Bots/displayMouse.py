import keyboard
from time import sleep
sleep(2)
keyboard.press_and_release('windows')
sleep(1)
keyboard.write('python', delay = 0.1)
sleep(1)
keyboard.press_and_release('enter')
sleep(2)
keyboard.write('import pyautogui', delay = 0.1)
sleep(1)
keyboard.press_and_release('enter')
sleep(1)
keyboard.write('pyautogui.displayMousePosition()', delay = 0.1)
sleep(1)
keyboard.press_and_release('enter')