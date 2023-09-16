import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$*"?'
passlen = int(input("Enter the lenth of your password:"))
password = ''
for le in range(passlen):
	passwordchar = random.choice(chars)
	password = password + passwordchar
print('your password is:', password)
for i in range(3):
	print('hello')
