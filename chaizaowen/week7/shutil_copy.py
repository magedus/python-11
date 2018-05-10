from pathlib import Path
import shutil

pa = 'e:/homework/python-11/chaizaowen/week7/a/test.txt'
pb = 'e:/homework/python-11/chaizaowen/week7/b/test.txt'

if not Path(pb).parent.exists():
    Path(pb).parent.mkdir(parents=True)

# with open(pa) as fa:
#     with open(pb,'w') as fb:
#         shutil.copyfileobj(fa,fb)   #仅复制内容

shutil.copy(pa,pb)   #复制文件内容、部分元数据
shutil.copy2(pa,pb)   #复制文件内容、除ctime外的全部元数据