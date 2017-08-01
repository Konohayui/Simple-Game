vocab = []
print('Loading word list from file...')
FILE = 'GRE_Word_List.txt'
wordList = open(FILE, 'r')

for line in wordList:
    vocab.append(line.split(' ', 1)[0])
    
print(' ', len(vocab))
with open('GRE_wordlist.txt', 'w') as file:
    for v in vocab:
        file.write(v + '\n')
