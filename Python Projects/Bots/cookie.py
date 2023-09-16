import os
import subprocess
from time import sleep
from pyautogui import locateOnScreen, click
import keyboard
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', voices[1].id)	

def say(text):
	engine.say(text)
	engine.runAndWait()

obs = 'obs64'
# def RunObs():
# 	print('RunObs started')
# 	o = subprocess.check_output('tasklist', shell=True)
# 	if obs.encode() in o:
# 		print('It is there.')
# 		startObsRecording = locateOnScreen('obsStartRecording.png')
# 		if startObsRecording != None:
# 			click(startObsRecording)
# 	elif obs.encode() not in o:
# 		print('It is not there')
# 		os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OBS Studio\\OBS Studio.lnk")
# 		sleep(5)
# 		startObsRecording = locateOnScreen('obsStartRecording.png')
# 		if startObsRecording != None:
# 			click(startObsRecording)

# RunObs()
sleep(2)
say(engine.getProperty('rate'))
engine.setProperty('rate', 150)
say(engine.getProperty('rate'))

# keyboard.press('alt')
# sleep(0.5)
# keyboard.press_and_release('tab+tab')
# sleep(0.5)
# keyboard.release('alt')
# keyboard.press('alt')
# sleep(0.5)
# keyboard.press_and_release('tab+tab')
# sleep(0.5)
# keyboard.release('alt')
# print(locateOnScreen('recording.png', confidence=0.8))