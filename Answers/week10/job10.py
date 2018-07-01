# 1、使用python给自己qq邮箱发送一份邮件

# 参考：https://gist.github.com/binderclip/6d993af3d24edae1cfc4

# 2、实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）

import os


def list_pyfile(directory, lst=None):
    # 对目录进行递归，判断是否是.py后缀文件并加入列表
    if lst is None:
        lst = []
    abs_path = os.path.abspath(directory)

    for f in os.listdir(abs_path):
        abs_f = os.path.abspath(os.path.join(abs_path, f))
        if os.path.isfile(abs_f) and abs_f.endswith('.py'):
            lst.append(abs_f)
        elif os.path.isdir(abs_f):
            list_pyfile(abs_f, lst)

    return lst
