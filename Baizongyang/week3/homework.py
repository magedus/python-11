#1、给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
lst = [8,6,9,7,1,2,3,4,5]
x = 18
result = 0
for i in range(len(lst)):
    if lst[i] == x:
        result = 1
        break
    else:
        result = 0
print(result)

#2、任一个英文的纯文本文件，统计其中的单词出现的个数。
s = """Christmas or Christmas Day is a holiday celebrating the birth of Jesus, the central figure of Christianity. It is traditionally celebrated on December 25 by most Western Christian churches. Although dating to probably as early as a.d. 200, the feast of Christmas did not become widespread until the Middle Ages. Aspects of celebration may include gift-giving, Christmas trees, display of Nativity sets, church attendance, the Father Christmas/Santa Claus myth, and family gatherings. The word Christmas is derived from Middle English Christemasse. It is a contraction meaning "Christ's mass". The name of the holiday is often shortened to Xmas because Roman letter "X" resembles the Greek letter X, an abbreviation for Christ."""
new_s = s.replace(',','')           #替换掉逗号
new_S = new_s.replace('.','')       #替换掉句号
s1 = new_S.split()
for i in range(len(s1)):
    print(s1[i],s1.count(s1[i]))