#读取一个英文文件，统计单词出现的次数

#读取文件
file = open('C:\\Users\\ockey\\2.txt','r')
contents = file.read().strip().replace(' ','')
file.close()

contents_list = list(contents)           #读取的内容转成列表
words = [chr(i) for i in range(97,123)]  #定义字母列表

for i in words:
    num = contents_list.count(i)
    if num == len(contents_list):        #字符全部相同的情况
        print("the word of {} 's count is {}".format(i,num))
        break
    if num == 0:
        continue
    print("the word of {} 's count is {}".format(i,num))