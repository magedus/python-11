#2、使用Python copy一个文件，从a目录,copy文件到b目录

from pathlib import Path

a = Path('/tmp/a/test')
b = Path('/tmp/b/test')

with open(str(a),'rb') as file_src:
    tmp = file_src.read()
    with open(str(b),'wb') as file_dst:
        file_dst.write(tmp)



