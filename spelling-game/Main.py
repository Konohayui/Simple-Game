import random
import numpy

WordList_File = "GRE_wordlist.txt"

def loadWords():
    print('Loading word list from file...')
    FILE = open(WordList_File, 'r')
    wordList = []
    for line in FILE:
        wordList.append(line.strip().lower())
    print(len(wordList))
    return wordList

def getWord(wordList):
    word = random.choice(wordList)
    if len(word) > 0:
        return word
    else:
        return getWord(wordList)

def getSpace(L):
    irange = numpy.random.choice(range(L), random.randint(0, L-1))
    if len(irange) > 0:
        return irange
    else:
        return getSpace(L)
    
def deleteLetters(word):
    w = list(word)
    irange = getSpace(len(w))
    for i in irange:
        w[i] = '_'
    new_word = ''.join(w)
    print(new_word)
    
def isMatch(answer, attempt):
    if answer == attempt:
        return True
    else:
        return False
