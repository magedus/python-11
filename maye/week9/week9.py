'''
    1、请实现函数 new_counter ，使得调用结果如下：
    c1 = new_counter(10)
    c2 = new_counter(20)
    print（c1(), c2(), c1(), c2()）
    
    outputs ：
    11 21 12 22
    
    2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符
    '''


def new_counter(num):
    local_cache={num:num}
    def news_counter():
        local_cache[num]=local_cache.get(num,0)+1
        return local_cache[num]
    return news_counter


c1=new_counter(10)
c2=new_counter(20)
print(c1(),c2(),c1(),c2())

def new_counter(num):
    def news_counter():
        nonlocal num
        while True:
            num+=1
            yield num
    m = news_counter()
    return lambda : next(m)
c1=new_counter(10)
c2=new_counter(20)
print(c1(),c2(),c1(),c2())
#================================
def distinct_str():
    while True:
        a = input('>>>')
        if a.strip() !='':
            break
    set1={x for x in a}
    if len(a)>len(set1):
        return print('{} has repeat string'.format(a))
    return print('{} has no repeat string'.format(a))
distinct_str()
