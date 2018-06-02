ss = input('please input somthing>>>')
source_string = ss.strip()

#s = 'thisisanexample'
def pick_word(s):
    lst = ['this', 'is', 'an', 'example']
    target_lst = []
    length = len(s)
    start = 0
    for stop in range(start,length):
        if s[start:stop+1] in lst:
            target_lst.append(s[start:stop+1])
            start = stop+1
    return target_lst


print(pick_word(source_string))