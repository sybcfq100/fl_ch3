# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/31
@Author      : sybcf
@File        : secretNumber
@Description : 
"""
# this is a guess the number game
import random

secretNumber = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")

# ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    a = input('enter a number: ')
    while True:
        try:
            a = float(a)
            break
        except:

            a = input('enter a number: ')
    guess = int(a)
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # this condition is the corret guess!

if guess == secretNumber:
    print('Good job! Your guess my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + ' .')
