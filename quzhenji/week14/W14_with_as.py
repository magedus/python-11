class A:
    def __init__(self):
        print('init:'+self.__class__.__name__)

    def __enter__(self):
        print('enter:' + self.__class__.__name__)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit:' + self.__class__.__name__)
        return True

a = A()
with a as f:
    print('Hello')

print('outer')