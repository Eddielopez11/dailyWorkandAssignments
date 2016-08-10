#guessing game
import random

guessing = True
number = random.randint(1, 1000)
print('Welcome to the best guessing game!')
while guessing:
    guesses = int(0)
    print('Try to guess my number, its between 1 and 1000. You will have 5 attempts')
    guess = int(input('What is your guess? '))
    if (guess > 1000 or guess < 1):
        invalid = True
        while(invalid):
            print('Invalid number smarty! guess a number between 1 and 1000')
            guess = int(input('What is your guess? '))
            if(1000 <= guess >= 1):
                invalid = False
    guesses += int(1)
    if (guess == number):
        print('Correct!')
        guessing = True
    elif (guess > number):
        print('your guess is too high, guess lower')
    else (guess < number):
        print('your guess is too low, guess higher')
