import random
import numpy

#WordList_File = "GRE_wordlist.txt"
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

def getWord(wordList):
    word = random.choice(list(wordList))
    return word, wordList[word]

def getSpace(L):
    if L == 1:
        return [0]
    else:
        irange = numpy.random.choice(range(L), random.randint(1, L//2))
        return irange

def countSpace(word):
    space = 0
    for c in list(word):
        if c == '_':
            space += 1
    return space

def deleteLetters(word):
    w = list(word)
    irange = getSpace(len(w))
    for i in irange:
        w[i] = '_'
    new_word = ''.join(w)
    blanks = countSpace(new_word)
    print(new_word, ',', blanks, 'letters need to enter')
        
def isMatch(answer, attempt):
    if answer == attempt:
        return True
    else:
        return False

def review(incorrect_attempt, wordList):
    answer = random.choice(incorrect_attempt)
    meaning = wordList[answer]
    re_test = deleteLetters(answer)
    print(meaning)
    reattempt = input('Enter your answer: ')
    if isMatch(answer, reattempt):
        print('This is correct!')
        incorrect_attempt.remove(answer)
    return incorrect_attempt

# testing    
#if __name__ == '__main__':
#    wordList = loadWords()
#    print(len(getWord(wordList)))
