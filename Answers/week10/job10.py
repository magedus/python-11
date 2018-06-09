# 1、使用python给自己qq邮箱发送一份邮件

# 参考：https://gist.github.com/binderclip/6d993af3d24edae1cfc4

# 2、实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）

import os


def list_pyfile(directory):
    abs_path = os.path.abspath(directory)
    for f in os.listdir(abs_path):
        abs_f = os.path.abspath(f)
        if os.path.isdir(f):
            list_pyfile(abs_f)
        elif os.path.isfile(abs_f) and abs_f.endswith('.py'):
            yield abs_f

