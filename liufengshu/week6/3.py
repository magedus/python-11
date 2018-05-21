text = "He admitted he didn’t shoot people he liked and meant to kill the ones he did target, a probable cause affidavit says."


lst =  text.split()
print(lst)
for i in range(len(lst)//2):
    lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]

print(lst)