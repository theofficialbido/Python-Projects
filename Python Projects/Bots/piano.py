from pyautogui import *
import pyautogui
import time
import random
import win32api, win32con
import keyboard
''' 1: X 726 Y 700
    2: X 888 Y 700
    3: X 999 Y 700
    4: X 1128 Y 700'''
def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.05)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:

	if pyautogui.pixel(726,700)[0] == 0:
		click(726, 700)

	if pyautogui.pixel(888,700)[0] == 0:
		click(888, 700)

	if pyautogui.pixel(999,700)[0] == 0:
		click(999, 700)

	if pyautogui.pixel(1128,700)[0] == 0:
		click(1128, 700)
