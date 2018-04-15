import sys
#task1
str1 = "My Dream Hello! Thank you!"
lst1 = str1.split(' ')
length = len(lst1)
print(str1)
print(lst1)
print(length)

#task2

file1 = open(r'E:\MGEDU\MyPython_Git\python-11\quzhenji\week3_new\004.txt')
file2 = file1.read()
file1.close()
print(file2)
print()
lst1 = file2.split(' ')
print(lst1)
print()
print(len(lst1))