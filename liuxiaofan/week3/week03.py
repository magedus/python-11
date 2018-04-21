#给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
import re
ss = 'ABCDEFG'
ls = ['A','b','c']
pattern = re.compile('|'.join(ls))
for x in pattern.findall(ss):
    pri


#任一个英文的纯文本文件，统计其中的单词出现的个数。
import re
def get_word_frequencies(file_name):
    dic = {}
    txt = open(file_name, 'r').read().splitlines()

    n=0
    for line in txt:
        print line
        line = re.sub(r'[.?!,""/]', ' ', line)   
        line = re.sub(r' - ', ' ', line)  
        for word in line.split():

            if word[-1] =='-':
                    m=word[:-1]
                    n=1
                    break
            if n==1:
                word=m+word
                n=0
            print word
            dic.setdefault(word.lower(), 0)  #不区分大小写
            dic[word.lower()] += 1
    #print dic


get_word_frequencies("F:/Export.txt")