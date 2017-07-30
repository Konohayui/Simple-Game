# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 18:53:04 2017

@author: yu
"""

import random

answer = random.randint(1, 99)
guess = int(input('Enter an integer between 1 and 99: '))


if guess == answer:
    print('You guessed it!')
else:
    while guess != answer:
        if guess < answer:
            print('Your guess is low!')
            guess = int(input('Enter a new guess: '))
        elif guess > answer:
            print('Your guess is high!')
            guess = int(input('Enter a new guess: '))
    print('You guessed it!')
