vowels = 'aeiou'

def vowelfinder():
	vowelnumber = 1
	x = input('Enter your sentence: ')
	for letter in x:
		if letter in vowels:
			vowelnumber += 1
	print (f'Your sentence has {vowelnumber} vowels')


vowelfinder()
