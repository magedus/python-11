from pathlib import Path

def get_py_path(p):
    p = Path(p)
    return list(p.glob('**/*.py'))

if __name__ == '__main__':
    p = 'D:\program file\pycahrm\github_py\python-11\liufengshu'
    print(get_py_path(p))