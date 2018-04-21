def is_or_not(n):
    string = str(n)
    length = len(string)
    for i in range(1,length/2 + 1):
        #print i-1, -1*i
        if not string[i-1] == string[-1*i]:
            return False
    return True

n = input('Enter a number: ')
print is_or_not(n)
