def rev(str):
    lst = str.split()
    n = len(lst)
    ret=[]
    for i in range(n):
        ret.append(lst[n-i-1])
    ret = " ".join(ret)
    return  ret

rev("let's try to see whether it works")

###########################################


sen = "let's try to see whether it works"

" ".join(sen.split()[::-1])

