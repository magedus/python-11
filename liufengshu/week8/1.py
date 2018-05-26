def test(str1, str2):
    if str2 in str1:
        for i in range(len(str1) - len(str2)+1):
            if str1[i:i+len(str2)] == str2:
                return i
    return None

def test2(str1, str2):
    index = str1.find(str2)
    if index != -1:
        return index
    return None

if __name__ == '__main__':
    lst = ['ab', 'ba', '123', 'asdq', '34fa','ba', 'tfev']
    str2 = 'a'
    for str1 in lst:
        print(test(str1, str2))
    print('--------------')
    for str1 in lst:
        print(test2(str1, str2))


