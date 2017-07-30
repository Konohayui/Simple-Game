import random

answer = random.randint(1, 99)
guess = int(input('Enter an integer between 1 and 99: '))


if guess == answer:
    print('You guessed it with one attempts!')
else:
    attempts = 0
    while guess != answer:
        if guess < answer:
            print('Your guess is low!')
            guess = int(input('Enter a new guess: '))
            attempts += 1
        elif guess > answer:
            print('Your guess is high!')
            guess = int(input('Enter a new guess: '))
            attempts += 1
    print('You guessed it with ' + str(attempts + 1) + ' attempts!')
