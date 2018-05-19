import shutil
import os

# 1、请将 "1,2,3"，变成 ["1","2","3"]


def str2list(s: str) -> list:
    return s.split(',')


# 使用Python copy一个文件，从a目录,copy文件到b目录


def cpfile(src, dst):
    abs_src = os.path.exists(os.path.abspath(src))
    dst_src = os.path.exists(os.path.abspath(dst))
    if not abs_src:
        raise Exception('{} not extist'.format(src))
    if not dst_src:
        raise Exception('{} not extist'.format(dst))
    shutil.copy2(abs_src, dst_src)


# 3、以下代码输出什么，请解释原因(写到问题下方):
li = [[]] * 5
li[0].append(10)
print(li)
li[1].append(20)
print(li)
li.append(30)
print(li)