#若将n的各位数字反向排列所得自然数n1与n相等，则称n为一回文数
while True:
    num = input("please input a five-digit number: ").strip().lstrip('0')
    if len(num) == 5:
        break
    print("the num of {} 'length != 5,pleas input again!".format(num))

nums = list(num)
lst = nums.copy()
nums.reverse()  #列表反转，就地修改
for i in range(len(lst) - 1):
    if lst[i] != nums[i]:
        print("{} is not palindromic number".format(num))
        break
else:
    print("{} is palindromic number".format(num))