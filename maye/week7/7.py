
a='1,2,3'
print(a.split(','))
=========================

import shutil
import os
def transf(a_dir,b_dir):
    if not os.path.isfile(a_dir) and not os.path.isdir(b_dir):
        return False
    file_path=os.path.split(a_dir)
    file=file_path[1]
    shutil.copy(file,b_dir)
    return b_dir
==========================================

li = [ [ ] ] * 5 引用类型返回同一个地址 输出[[],[],[],[],[]] 相当于copy 生成同一个引用

li[0].append(10)  在返回地址里面加10  li里面的所有都指向这个地址 输出[[10],[10],[10],[10],[10]]
print(li)

li[1].append(20) 在这个地址再加20 输出[[10,20],[10,20],[10,20],[10,20],[10,20]]
print(li)
li.append(30) 输出[[10,20],[10,20],[10,20],[10,20],[10,20],30] 正常append一个元素
print(li)
