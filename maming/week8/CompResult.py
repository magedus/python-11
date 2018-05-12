
def getresult(iterable,result):
    seen=set()
    for i  in range(0,len(iterable)):
        for j in  range(i+1,len(iterable)):
            if iterable[i]+iterable[j]==result:
                seen.add((iterable[i],iterable[j] ))
            else:
                continue
    return seen

print(getresult([1,2,3,6,7,11,9,10,0],0))

