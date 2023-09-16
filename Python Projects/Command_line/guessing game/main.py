import random
import math
secret_no = random.randint(0, 30) + 1
guess_count = 0
guess_limit = 5
out_of_guesses = False
won = False
print('I have a number from 1 to 30')
while guess_count < guess_limit and not out_of_guesses:
    guess = int(input('Enter a guess: '))
    if guess > secret_no:
        print('Lower!')
        guess_count += 1
    elif guess < secret_no:
        print("Higher!")
        guess_count += 1
    elif guess == secret_no:
        print("You won")
        print(f"You used {guess_count + 1} guesses :)")
        out_of_guesses = True
        won = True
if not won:
    print(f"The secret number was {secret_no}")
