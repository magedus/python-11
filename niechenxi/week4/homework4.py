#1、问题描述：一个5位数，判断它是不是回文数。
#、随机生成20个数字，并且筛选出其中最大的3个数.

#第一题：

def  Palindrome_number(x):
    if not isinstance(x, int):
        print('The num must be int')
        return
    else:
        if len(str(x).rstrip('0')) != 5:
            print('please input five numbers.')
            return
        else:
            if str(x)[0] == str(x)[-1] and str(x)[1] == str(x)[-2]:
                print('Yes')
            else:
                print('No')

Palindrome_number(12321)
Palindrome_number(11121)
Palindrome_number(11111)

#第二题:
import random
def foo():
    lst = []
    for _ in range(20):
        lst.append(random.randint(0,1000))   #lst追加0，1000内的一个数字

    #一行打印20个数字
    for i,v in enumerate(lst):
        if i == 0:
            print('20 Numbers: {}'.format(v), end=' ')
        else:
            print(v,end=' ')
    print()

    #一行打印最大的3个数字
    for k,v in enumerate(sorted(lst,reverse=True)[:3]):
        if k == 0:
            print('max: {}'.format(v), end=' ')
        else:
            print(v, end=' ')
    print()

foo()
