'''问题描述：一个5位数，判断它是不是回文数'''

num = str(input('pls input a num:'))
if len(num) == 5:
    if num[0] == num[-1] and num[1] == num[-2]:
        print('this num is palindrome number')
    else:
        print('this num is not palindrome number')
else:
    print('wrong')