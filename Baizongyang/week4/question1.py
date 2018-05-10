#判断一个五位数是否为回文数
number = input("Please enter a five-digit number")
len_number = str(number)
if len(len_number) != 5:
    print("The number you have entered is not five digits.")
else:
    flag = False
    for i in range(len(len_number)//2 - 1):
        if len_number[i] == len_number[-(i+1)]:
            flag = True
        else:
            flag = False
    else:
        print(flag)
        print("This number you have entered is a Palindrome number") if flag else print("This number you have entered is not a Palindrome number")