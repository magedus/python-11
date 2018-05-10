import sys
num = input("请输入一个数判断是否是回文数:")

if not num.isdigit():
    print("输入的不是数字")
    sys.exit(33)

if num == str(num)[::-1]:
    print("是回文数")
else:
    print("不是回文数")



num = input("请输入一个数判断是否是回文数:")

if not num.isdigit():
    print("输入的不是数字")
    sys.exit(33)
a = num
i = 10
while True:
    if not "c" in dir():
        c = str(int(a)%i)
    else:
        c += str(int(a)%i)
    a = int(a)//i
    if not a:
        break




print("是回文") if c == num else print("不是回文")
