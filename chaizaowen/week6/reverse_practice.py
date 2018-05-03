str1 = 'Nothing he did or said was unpremeditated.'

def rev_seq(words):
    src = words.split()
    middle = []
    dest = []
    for w in src:
        middle.append(w.strip(',.?-'))
    # print(middle)
    for i in range(len(middle)-1,-1,-1):
        dest.append(middle[i])
    # print(dest)
    dest = ' '.join(dest)
    return dest

print(rev_seq(str1))

