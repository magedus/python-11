#任一个英文的纯文本文件，统计其中的单词出现的个数。
str1 = "a b c d e f g h i j k l m n a b c d e f g h i j"
lst1 = str1.split()
new_lst = []
num_c = len(lst1) - 1
for i in range(len(lst1)):
    if lst1[i] in new_lst:
        continue
    else:
        new_lst.append(lst1[i])

for j in range(len(new_lst)):
    print("{}:{}".format(new_lst[j],lst1.count(new_lst[j])))
