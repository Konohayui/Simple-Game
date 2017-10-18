# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 17:19:35 2017

@author: yu
"""

import random
import numpy

MGRE = 'Magoosh_GRE_word_list.txt'
Yaoniming = '再要你命3000.txt'
TOEFL_basic = 'TOEFL_word_basic.txt'
TOEFL_medium = 'TOEFL_word_medium.txt'
TOEFL_advanced = 'TOEFL_word_advanced.txt'

def loadWords():
    Books = [MGRE, Yaoniming, TOEFL_basic, TOEFL_medium, TOEFL_advanced]
    print('Books: ')
    print('0: Magoosh_GRE; 1: 再要你命3000; 2: TOEFL_word_basic; 3: TOEFL_word_medium; 4: TOEFL_word_advanced')
    book = input('Enter a number to select a book to play: ')
    Book_name = Books[int(book)]
    print('Loading word list from file...')
    if book == str(1):
        Book = open(Book_name, encoding = 'utf-8')
    else:
        Book = open(Book_name, 'r')
    wordList = {}
    for line in Book:
        vocab = line.split(None, 1)
        word = vocab[0]
        meaning = vocab[1]
        wordList[word] = meaning
    print(len(wordList))
    return wordList

def chooseWord(wordList, correct_choice):
    word = random.choice(list(wordList))
    if word not in correct_choice:
        return word, wordList[word]
    else:
        return chooseWord(wordList, correct_choice)

def choices(wordList, answer):
    choice = numpy.random.choice(list(wordList), 3)
    if answer not in choice:
        return choice
    else:
        return choices(wordList, answer)
    
def permu_option(wordList, answer):
    options = choices(wordList, answer)
    A = options[0]
    B = options[1]
    C = options[2]
    D = answer
    permu_options = numpy.random.permutation([wordList[A], wordList[B], wordList[C], wordList[D]])
    return permu_options
    
def display_options(options, answer):
    print(answer)
    print('A: ', options[0])
    print('B: ', options[1])
    print('C: ', options[2])
    print('D: ', options[3])
    
def check(options, attempt, definition):
    letter2num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'a': 0, 'b': 1, 'c': 2, 'd': 3}
    if options[letter2num[attempt]] == definition:
        return True
    else:
        return False
    
def play(wordList):
    command = input('Press any key to start/e to end the game: ')
    score = 0
    correct_answer = 0
    correct_choice = []
    while command != 'e':
        word = chooseWord(wordList, correct_choice)
        answer = word[0]
        definition = word[1]
        options = permu_option(wordList, answer)
        display_options(options, answer)
        attempt = input('Enter A/a, B/b, C/c, D/d : ')
        if check(options, attempt, definition):
            score += 10
            correct_answer += 1
            correct_choice.append(answer)
            print('This is correct! Total score is ', score)
            print('You got', correct_answer, 'correct answers!')
            if correct_answer == len(wordList):
                print('Well Done!')
                command == 'e'
        elif not check(options, attempt, definition):
            score -= 1
            print('This is not correct! Total score is ', score)
            print('The correct answer is ', definition)
        command = input('Press any key to continue/e to end the game: ')
    print('Game Over!')
    
# testing    
if __name__ == '__main__':
    wordList = loadWords()
    play(wordList)