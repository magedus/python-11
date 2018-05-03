import shutil

# 请将 "1,2,3"，变成 ["1","2","3"]


def str_to_list(x):
    b = []
    for i in x:
        if i.isdigit():
            b.append(i)
        else:
            continue
    return b


a = "1,2,3"
print(str_to_list(a))

# 2、使用Python copy一个文件，从a目录,copy文件到b目录
shutil.copyfile(a, b)

#  3、以下代码输出什么，请解释原因(写到问题下方):
li = [[]] * 5  # 产生一个列表，里面5个空列表作为元素。
print(li)

li[0].append(10)  # 列表中第一个元素（这个元素也是列表），这个元素追加一外元素：10
print(li) # 由于内存引用地址是同一个，所以打出来是五个同样的元素。

li[1].append(20)  # 列表中第一个元素（这个元素也是列表），这个元素追加一外元素：20
print(li)    # 由于内存引用地址是同一个，所以打出来是五个同样的元素。

li.append(30) # 列表li 添加最一个元素 ：30
print(li)


a = [[], [], [], [], []]
a[0].append(10)
print(a)

a[1].append(20)
print(a)

a.append(30)
print(a)