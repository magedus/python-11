import shutil
from pathlib import Path
def copy_file(dir1, file1, dir2, file2=None):
    dir1 = Path(dir1)
    dir1 /= file1
    dir2 = Path(dir2)
    if file2 is None:
        dir2 /= file1
    else:
        dir2 /= file2
    print(dir1)
    print(dir2)
    with open(dir1, 'r+') as f1:
        with open(dir2, 'w+') as f2:
            shutil.copyfileobj(f1, f2)
    print('ok')

if __name__ == '__main__':
    dir1 = "D:\program file\pycahrm\pyfile\decorator_hash\week6"
    file1 = "学习进度.txt"
    dir2 = Path().absolute()
    copy_file(dir1, file1, dir2)
