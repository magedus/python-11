#统计 x 元素是否在某一列表中
str = input('please input a list:').strip()
lst = list(str)
print(lst)
#统计
num = lst.count('x')
print( 1 if num!=0 else 0)