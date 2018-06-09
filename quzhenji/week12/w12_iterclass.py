
class A:
    def __init__(self):
        self.lst = []

    def append(self,value):
        self.lst.append(value)

    def __getitem__(self, index):
        return self.lst[index]

    def __len__(self):
        return len(self.lst)

    def __iter__(self):
        yield from self.lst
        #return iter(self.lst)

a = A()
for i in range(3,16,2):
    a.append(i)

for x in a:
    print(x)

print(len(a))
print(a[0])
print(a[1])
print(a[6])
