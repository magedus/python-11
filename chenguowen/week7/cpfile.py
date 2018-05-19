#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

def copyfile(srcfile,dstfile):
    """

    使用Python copy一个文件，从a目录,copy文件到b目录
    """

    if not os.path.exists(srcfile):
        print('源文件{}不存在!'.format(srcfile))
        return
    elif not os.path.exists(dstfile):
        os.mkdir(dstfile)

    shutil.copy2(srcfile,dstfile)

copyfile('a/a.txt','b/')

