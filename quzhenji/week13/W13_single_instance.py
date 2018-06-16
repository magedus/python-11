#method 1:
class SingleInstance:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingleInstance, cls).__new__(cls)

        return cls.instance


print('before', SingleInstance.__dict__)
obj1 = SingleInstance()
obj2 = SingleInstance()
print('after', SingleInstance.__dict__)
obj1.attr1 = 'value1'

print(obj1.__dict__, obj2.__dict__)

print(obj1 is obj2)


#method 2:
def fn(cls):
    d1 = {}

    def wrapper(*args, **kwargs):
        if cls not in d1:
            d1[cls] = cls(*args, **kwargs)

        return d1[cls]

    return wrapper


@fn
class SingleInst:
    x = 5


c1 = SingleInst()
c2 = SingleInst()

print(c1 == c2)
