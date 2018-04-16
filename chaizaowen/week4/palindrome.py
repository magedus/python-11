def pal(num):
    '''
    This function is used to judge whether the number of palindroms is not.

    return 0 is not palindrome
    return 1 is palindrome
    num int

    '''
    num = str(num)
    for i in range(len(num)):
        if num[i] != num[-i-1]:
            return 0
    else:
        return 1

print(pal(12321))
print(pal(1231))
print(pal(111111))


