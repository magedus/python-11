with open('e:\MGEDU\he.txt',encoding='utf-8') as f1:
    with open('d:\des.txt','w',encoding='utf-8') as f2:
        s = f1.read()
        f2.write(s)
