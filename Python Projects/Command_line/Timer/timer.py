import time
from playsound import playsound
times = 1

def timer(x):
	stop = False
	if times == 1:
		time.sleep(x)
		for i in range(6):
			playsound('audio.mp3')
		print('Timer Done')


def timer_time():
	SH = input('Timer (S)econds or (M)inutes: ')
	if SH.lower() == 's':
		seconds = int(input("Enter time (S): "))
		times = 1
		timer(seconds)
	elif SH.lower() == 'm':
		minutes = int(input('Enter time (M): '))
		minutes = minutes * 60
		times = 2
		timer(minutes)




timer_time()
