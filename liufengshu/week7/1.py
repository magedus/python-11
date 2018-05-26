s = "1,2,3"
lst = (lambda s:[i for i in s.split(',')])(s)
print(lst)
