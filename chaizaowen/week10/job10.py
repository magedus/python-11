from pathlib import Path

def findpy(path):
    p = Path(path)
    yield from p.rglob('*.py')

pysuffix = findpy('dir1')
for i in pysuffix:
    print(i)