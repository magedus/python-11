from collections import defaultdict

s1 = input('please inpout some words in English>>>')
def check_repeat(s):
    d = defaultdict(lambda :0)
    for x in s:
        d[x] += 1
    if len(s) == len(d):
        print('No repeat')
        return 1
    else:
        print('repeat')
        return 0

check_repeat(s1)