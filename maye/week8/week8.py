#1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。
s1='defabcdoabcdeftw'
s2='abcdefg'

def judge_sub(str1,str2):
    matrix=[]
    xmax=0
    xindex=0
    yindex=0


    for i,x in enumerate(str1):
        matrix.append([])
        for j,y in enumerate(str2):
            if x != y:
                matrix[i].append(0)
            else:
                if i==0 or j==0:
                    matrix[i].append(1)
                else:
                    matrix[i].append(matrix[i-1][j-1]+1)

            if matrix[i][j] > xmax:
                xmax=matrix[i][j]
                xindex=j
                xindex+=1
                yindex = i+1-xmax
    if str2[xindex-xmax:xindex]==str2:
        return '{} issubset {}'.format(str2,str1),yindex
    else:
        return


print(judge_sub(s1,s2))

#2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
#如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
lst=[1,5,2,7,4,9]
t1=11
def ret(lst:list,target):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]==target-lst[j]:
                return lst[i],lst[j]
    else:
        return

print(ret(lst,18))
