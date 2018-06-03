from pathlib import Path
import shutil

def load(path:str):
    p = Path(path)
    for file in list(p.glob('**/*.py')):
        shutil.copy(file,'f:/testcopy',follow_symlinks=True)

load('f:/')
