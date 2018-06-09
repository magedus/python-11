import pathlib

def findpy(cudir):
	for i in cudir.iterdir():
		if i.is_file() and str(i).endswith('.py'):
			print(str(i).split('/')[-1])
		if i.is_dir():
			findpy(i)

CuPath = pathlib.Path()
findpy(CuPath)