import  random


lst = [random.randint(10,100) for _ in range(20)]
print(1,lst)
lst.sort(reverse=True)
print(2,lst)
print('*'*80)
print(3,'Frist_Max={},Second_Max={},Third_Max={}'.format(lst[0],lst[1],lst[2]))
