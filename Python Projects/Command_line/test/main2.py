no = int(input('Enter your number: '))
times = int(input('Enter max number: '))
result = 0
for i in range(times + 1):
	result = no * i
	print(f'{no} * {i} is equal to {result}')
