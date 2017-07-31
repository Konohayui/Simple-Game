wordList = ['string', 'word', 'list']

for word in wordList:
    w = list(word)
    L = len(w)
    for i in range(L):
        if i % 2 == 0:
            w[i] = '_'
    new_word = ''.join(w)
    print new_word
