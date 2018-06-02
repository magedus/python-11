#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def find_py(path,suffix):
    """
    实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）
    
    """

    p1 = Path(path)
    lst1 = list(p1.rglob(suffix))

    print('{}目录中所有{}文件如下:'.format(path,suffix))
    for files in lst1:
        print(files)
        
find_py('./','*.py')
