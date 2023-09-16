from time import sleep
import random
maximum = int(input('Enter max number:'))
num = random.randint(10000, maximum)
fact = 0
print(num)
sleep(5)
while num != 4:
	#sleep(0.2)
	print(num)
	if num == 4:
		break
	elif num % 2 != 0:
		num = num * 3
		num += 1
	elif num % 2 == 0:
		num = num // 2
	fact += 1
print(f'that took {fact + 2} tries')