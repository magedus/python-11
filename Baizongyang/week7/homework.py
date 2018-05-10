# 请将 "1,2,3"，变成 ["1","2","3"]
def transformation(s=None):
    if s == None:
        s = "1,2,3"
        lst = s.split(sep=',')
        print(lst)
transformation()

#第二题
import os,shutil

def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print "move %s -> %s"%( srcfile,dstfile)

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print "copy %s -> %s"%( srcfile,dstfile)

srcfile='/Users/xxx/git/project1/test.sh'
dstfile='/Users/xxx/tmp/tmp/1/test.sh'

mymovefile(srcfile,dstfile)

#第三题
li = [ [ ] ] * 5
print(li)                 #打印出[[], [], [], [], []]
li[0].append(10)           #由于向列表li索引[0]后追加10，所以li[0]就是[10],li=[[]]*5,li[0]下的所有子索引都是指向同一个内存地址，故显示结果如下：
print(li)                 #打印出[[10], [10], [10], [10], [10]]
li[1].append(20)           #道理同上，显示效果如下：
print(li)                 #打印出[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
li.append(30)              #向列表li的尾部追加30，显示效果如下：
print(li)                 #打印出[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]