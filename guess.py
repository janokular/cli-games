#!/bin/env python3


import random


SECRET_NUMBER = random.randint(1, 100)

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")

print('\nPlease select the difficulty level:')
print('1. Easy (10 chances)')
print('2. Medium (5 chances)')
print('3. Hard (3 chances)')

while True:
    try:
        game_mode = int(input('\nEnter your choice: '))
        if game_mode == 1:
            print('\nGreat! You have selected the Easy difficulty level.')
            chances = 10
            break
        elif game_mode == 2:    
            print('\nGreat! You have selected the Medium difficulty level.')
            chances = 5
            break
        elif game_mode == 3:    
            print('\nGreat! You have selected the Hard difficulty level.')
            chances = 3
            break
        else:
            print('Please provide the number in range from 1 to 3.')
    except ValueError:
        print('Please provide the number.')

print(f'You have {chances} chances to guess the correct number.')
print("Let's start the game!")

for guessTaken in range(0, chances):
    while True:
        try:
            guess = int(input('\nEnter your guess: '))
            if guess < 1 or guess > 100:
                print('Please provide the number in range from 1 to 100.')
            else:
                break
        except ValueError:
            print('Please provide the number.')

    if guess < SECRET_NUMBER:
        print(f'Incorrect! The number is greater than {guess}.')
    elif guess > SECRET_NUMBER:
        print(f'Incorrect! The number is less than {guess}.')
    else:
        break

if guess == SECRET_NUMBER:
    if guessTaken == 0:
        print(f'\nCongratulations! You guessed the secret number in {guessTaken + 1} attempt.')
    else:
        print(f'\nCongratulations! You guessed the secret number in {guessTaken + 1} attempts.')
else:
    print(f'\nYou lose! The secret number was {SECRET_NUMBER}.')
