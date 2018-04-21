sentence = 'hello world nihao world hey hello java world hi python yeoman word'

list1 = sentence.split()
list2 = set(list1)
dir1 = {}

for i in list1:
    if i in list2 and dir1.get(i):
        dir1[i] += 1
    else:
        dir1[i] = 1

print(dir1)