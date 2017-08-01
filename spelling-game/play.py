from Main import *

def playGame(wordList):
    command = input('Enter s to start/e to end the game: ')
    score = 0
    correct = 0
    while command != 'e':
        if command == 's' or 'c':
            answer = getWord(wordList)    
            test = deleteLetters(answer)
            attempt = input('Enter your answer: ')
            if isMatch(answer, attempt):
                score += 10
                correct += 1
                print('This is correct! Total number of correct word is', correct)
                print('Your score is', score)
            elif not isMatch(answer, attempt):
                score -= 1
                print('This is incorrect! The correct answer is', answer)
                print('Your score is', score)
        else:
            print('Invalid Command!')
        command = input('Enter c to continue/e to end the game: ')

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
