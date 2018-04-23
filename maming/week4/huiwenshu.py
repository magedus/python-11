# -*- coding:utf-8 -*-
# -*— author: maming -*-

while True:
    number=input("Please input a 5-digit nnumber:").strip()
    if  number.isdigit() and len(number)==5:
        break
    else:
        print("Bad Number,try again!")

palind=number[::-1]

if palind==number:
    print("This is a palindrome number")
else:
    print("it's not.")