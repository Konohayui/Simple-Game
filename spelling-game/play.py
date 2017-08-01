from Main import *

def playGame(wordList):
    command = input('Press any key to start/e to end the game: ')
    score = 0
    correct = 0
    while command != 'e':
        answer = getWord(wordList)    
        test = deleteLetters(answer)
        attempt = input('Enter your answer: ')
        if isMatch(answer, attempt):
            score += 10
            correct += 1
            print('This is correct! Total number of correct word is', correct)
            print('Your score is', score)
            wordList.remove(answer)
            if len(wordList) == 0:
                print('You got all words!')
                command = 'e'
        elif not isMatch(answer, attempt):
            score -= 1
            print('This is incorrect! The correct answer is', answer)
            print('Your score is', score)
        command = input('Press any key to continue/e to end the game: ')
    print('Game Over!')
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
