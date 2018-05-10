t1 = ('a','b')
t2 = ('c','d')
target_lst = []
fn = lambda k,v:{k:v}

target_lst.append(fn(t1[0],t2[0]))
target_lst.append(fn(t2[0],t2[1]))
print(target_lst)

test_lst = [fn(k,v) for k,v in list(zip(t1,t2))]
print(test_lst)