1.请将 "1,2,3"，变成 ["1","2","3"]
_="1,2,3"
[_[i] for i in range(len(_)) if  i%2==0]
2.使用Python copy一个文件，从a目录,copy文件到b目录
import os
import shutil
os.chdir("/home/python/cxz/project/cmdb")
os.getcwd()
!ls
a="/home/python/cxz/project/cmdb"
b="/home/python/cxz/project/"
print(path1)
shutil.move("234.py",b)
3.以下代码输出什么，请解释原因(写到问题下方):
li = [ [ ] ] * 5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li)
print(id(li[0]),id(li[1]),id(li[2]),id(li[3]),id(li[4]),id(li[5]))
li 前面5个空列表元素的内存地址都是一个，第6个append的元素创建了新的内存地址保存30
