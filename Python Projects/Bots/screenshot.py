import pyautogui
import keyboard
from time import sleep
'''
X: 55  Y: 105
'''
sleep(2)
p = pyautogui.screenshot('recording.png', region=(30, 80, 60, 60))
