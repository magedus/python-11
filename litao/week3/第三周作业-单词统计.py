sentence = 'hello world nihao world hey hello java world hi python yeoman word'
list1 = sentence.split()
list2 = list(set(list1))
dir1 = {}

for x in range(len(list2)):
    dir1[list2[x]] = 0
    for y in range(len(list1)):
        if list2[x] == list1[y]:
            dir1[list2[x]] += 1
print(dir1)