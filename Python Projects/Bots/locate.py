import pyautogui
from pyautogui import click
from time import sleep
import keyboard
def click(x):
    pyautogui.click(x)

keyboard.press_and_release('windows')
sleep(2)
if pyautogui.locateOnScreen('EdgeOpen.png') == None:
    print("Edge is not open")
    keyboard.write('Edge', delay = 0.2)
    sleep(0.5)
    keyboard.press_and_release('enter')
    sleep(4)
    keyboard.press_and_release('shift+ctrl+t')
    sleep(2)
    keyboard.press_and_release('alt+tab')
    sleep(1)

    if pyautogui.locateOnScreen('edge.png', confidence = 0.8) != None:
        maximize = pyautogui.locateOnScreen('edge.png', confidence = 0.8)
        click(maximize)
    elif pyautogui.locateOnScreen('edge2.png', confidence = 0.8) != None:
        pyautogui.moveTo(2498, 23)
        sleep(1)
        print(pyautogui.pixel(2505,20)[0])
        if pyautogui.pixel(2505,20)[0] == 232:
            pyautogui.click(2505, 20)
        pyautogui.moveTo(1300, 852)
        sys.exit()


    pyautogui.moveTo(2498, 23)
    sleep(1)
    print(pyautogui.pixel(2505,20)[0])
    if pyautogui.pixel(2505,20)[0] == 232:
        pyautogui.click(2505, 20)

        pyautogui.moveTo(1300, 852)
