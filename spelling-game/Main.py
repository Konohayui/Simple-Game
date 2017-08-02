import random
import numpy

#WordList_File = "GRE_wordlist.txt"
File_name = 'Magoosh_GRE_word_list.txt'

def loadWords():
    print('Loading word list from file...')
    FILE = open(File_name, 'r')
    wordList = {}
    for line in FILE:
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

# texting    
#if __name__ == '__main__':
#    wordList = loadWords()
#    print(len(getWord(wordList)))
