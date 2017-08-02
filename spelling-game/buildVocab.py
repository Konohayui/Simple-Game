import random

File_name = 'Magoosh_GRE_word_list.txt'

file = open(File_name, 'r')
vocab = {}
for line in file:
    w = line.split(None, 1)[0]
    mean = line.split(None, 1)[1:]
    vocab[w] = mean
print(len(vocab))

word = random.choice(list(vocab))
print(word)
