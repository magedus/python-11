"""
    Fibonacci
    ---------
    0 1 2 3 5 8 13 21 34 55 89 144
     + + + + + +  +  +  +  +  +
    
    0 + 1 = 2 | 1 + 2 = 3 | 2 + 3 = 5 ... ... 
    
    Math Definiton: Fn = Fn-1 + Fn-2
    
"""

class Fibonacci:
    
    def __init__(self):
        pass
        
       
    def fib1(self, n):
        fib=[0, 1]
        if n >= len(fib):
            for i in range(len(fib), n+1):
                fib.append(fib[i-1] + fib[i-2])
        return fib
    
    def fib2(self, n):
        if n == 0 or n == 1:
            return n
        a, b = 0, 1
        for i in range(2, n+1):
            temp = b
            b = a + b
            a = temp
        return b
    
    def fib3(self, n):
        __result = {0: 0, 1: 1}
        if n in __result:
            return __result[n]
        else:
            r = self.fib3(n -1) + self.fib3(n -2)
            __result[n] = r
            return r
    
    def worsefib(self, n):
        if n == 0 or n == 1:
            return n
        else:
            return self.worsefib(n-1) + self.worsefib(n-2) 
        
        # in class, callback, need add self.
         
    """
    
    Time Complexity: O(f(2^n)).
    
    it take long time while  try worsefib(n >= 40).
    
    Is a bad solution.
    """    
fib = Fibonacci()
fibs = fib.fib1(10)
for i in fibs:
    print(i)    
