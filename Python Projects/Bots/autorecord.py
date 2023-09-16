from  pyautogui import locateOnScreen, click
from pyautogui import *
from time import sleep
import keyboard
import subprocess
import os
import pyttsx3
obs = 'obs64.exe'


def say(text):
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()

def get_pic():
	recordingPic = locateOnScreen('recording.png', confidence = 0.5)
	if recordingPic != None:
		RunObs()
		
def RunObs():
	print('RunObs started')
	o = subprocess.check_output('tasklist', shell=True)
	if obs.encode() in o:
			print('It is there.')
			startObsRecording = locateOnScreen('obsStartRecording.png', confidence=0.8)
			print(f'Startobsrecording found {startObsRecording}')
			if startObsRecording != None:
				print('i found it first time')
				click(startObsRecording)
			elif startObsRecording == None:
				print('alt tab first time')
				keyboard.press_and_release('alt+tab')
				startObsRecording = locateOnScreen('obsStartRecording.png', confidence=0.8)
				if startObsRecording != None:
					click(startObsRecording)
				elif startObsRecording == None:
					print('started double alt tabbing')
					keyboard.press('alt')
					sleep(0.5)
					keyboard.press_and_release('tab+tab')
					sleep(0.5)
					keyboard.release('alt')
					startObsRecording = locateOnScreen('obsStartRecording.png', confidence=0.8)
					if startObsRecording != None:
						click(startObsRecording)
					elif startObsRecording == None:
						print('alt+tab to OBS in 3 seconds')
						say('alt+tab to OBS in 3 seconds')
						sleep(4)
						startObsRecording = locateOnScreen('obsStartRecording.png', confidence=0.8)
						if startObsRecording != None:
							click(startObsRecording)

	elif obs.encode() not in o:
		print('It is not there')
		os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OBS Studio\\OBS Studio.lnk")
		sleep(5)
		startObsRecording = locateOnScreen('obsStartRecording.png')
		if startObsRecording != None:
			click(startObsRecording)
		print(startObsRecording)

while True:
	get_pic()
	sleep(5)
	if obs.encode() in subprocess.check_output('tasklist', shell=True):
		sleep(2400)
