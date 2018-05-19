
a='1,2,3'
print(a.split(','))
=========================

import shutil
from pathlib import Path
p=Path('a/test.txt')
p.touch()
p1=Path('b/').touch()
shutil.copyfile(p,p1)
==========================================

li = [ [ ] ] * 5 引用类型返回同一个地址 输出[[],[],[],[],[]] 相当于copy 生成同一个引用

li[0].append(10)  在返回地址里面加10  li里面的所有都指向这个地址 输出[[10],[10],[10],[10],[10]]
print(li)

li[1].append(20) 在这个地址再加20 输出[[10,20],[10,20],[10,20],[10,20],[10,20]]
print(li)
li.append(30) 输出[[10,20],[10,20],[10,20],[10,20],[10,20],30] 正常append一个元素
print(li)
