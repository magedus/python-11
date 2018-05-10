# Q1
tups = [(('a'),('b')),(('c'),('d'))]
target = [(lambda x:{x[0]:x[1]})(tup) for tup in tups]
print(target)

# Q2
sentence = 'Be kind, for everyone you meet is fighting a hard battle.'
words = sentence.replace(',', ' ').replace('.', ' ').split()
words_reverse = [0]*len(words)

for i in range(len(words)):
    words_reverse[i]=words[-i-1]

print(words_reverse)