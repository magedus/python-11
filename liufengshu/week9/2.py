import copy
def check(s:str):
    s = copy.copy(s)
    for i in s:
        if i in s.replace(i,'',1):
            return True
        s.replace(i,'')
    return False

if __name__ == '__main__':
    for s in ['abcdefg', 'abcda', 'qwert', 'zsdxz']:
        print(check(s))