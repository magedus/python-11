f = open('example.txt')
word_lst = f.read().split()
word_dic = {}

print(word_lst)

for i in word_lst:
    word_dic[i] = word_dic.get(i,0) + 1

for k,v in word_dic.items():
    print('the count of "{}" is {}'.format(k,v))

f.close()