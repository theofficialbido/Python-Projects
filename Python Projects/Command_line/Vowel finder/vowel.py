WELCOME_SCREEN = '''
-------------------------------------------------------------------------------------
|																				    |
|							WELCOME TO THE VOWEL FINDER!						    |
|																			    	|
-------------------------------------------------------------------------------------
'''
print(WELCOME_SCREEN)
anum = 0
unum = 0
enum = 0
inum = 0
onum = 0
choice1 = 'y'
while choice1.lower() == 'yes' or choice1.lower() == 'y':
	sentence = input('Enter sentence: ')
	vowles = 'aeiou'
	nov = 0
	for letter in sentence.lower():
		print(letter)
		if letter in vowles:
			nov += 1
		match letter:
			case 'a':
				anum += 1
			case 'e': 
				enum += 1
			case 'i':
				inum += 1
			case 'o':
				onum += 1
			case 'u':
				unum += 1
			case _:
				print(letter)
	print(f'there were {anum} A and {enum} e and {inum} i and {onum} o and {unum} u, in total there were {nov} vowels')
