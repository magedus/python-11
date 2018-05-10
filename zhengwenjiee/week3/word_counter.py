file = open('license.txt', 'r')

from collections import Counter
word_counter = Counter(file.read().split())

for item in word_counter.items():
    print("{}\t{}".format(*item))


