import random
import numpy

MGRE = 'Magoosh_GRE_word_list.txt'
TOEFL_basic = 'TOEFL_word_basic.txt'
TOEFL_medium = 'TOEFL_word_medium.txt'
TOEFL_advanced = 'TOEFL_word_advanced.txt'

def loadWords():
    Books = [MGRE, TOEFL_basic, TOEFL_medium, TOEFL_advanced]
    print('Books: ')
    print('0: Magoosh_GRE; 1: TOEFL_word_basic; 2: TOEFL_word_medium; 3: TOEFL_word_advanced')
    book = input('Enter a number to select a book to play: ')
    Book_name = Books[int(book)]
    print('Loading word list from file...')
    Book = open(Book_name, 'r')
    wordList = {}
    for line in Book:
        vocab = line.split(None, 1)
        word = vocab[0]
        meaning = vocab[1]
        wordList[word] = meaning
    print(len(wordList))
    return wordList

def chooseWord(wordList):
    word = random.choice(list(wordList))
    return word, wordList[word]

def choices(wordList, answer):
    choice = numpy.random.choice(list(wordList), 3)
    if answer not in choice:
        return choice
    else:
        return choices(wordList)
    
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
    letter2num = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    if options[letter2num[attempt]] == definition:
        return True
    else:
        return False
    
def play(wordList):
    command = input('Press any key to start/e to end the game: ')
    while command != 'e':
        word = chooseWord(wordList)
        answer = word[0]
        definition = word[1]
        options = permu_option(wordList, answer)
        display_options(options, answer)
        attempt = input('Enter A, B, C, D : ')
        if check(options, attempt, definition):
            print('This is correct!')
        elif not check(options, attempt, definition):
            print('This is not correct!')
            print('The correct answer is ', definition)
        command = input('Press any key to continue/e to end the game: ')
    print('Game Over!')
    
# testing    
if __name__ == '__main__':
    wordList = loadWords()
    print(play(wordList))
