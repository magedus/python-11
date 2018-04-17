import random

def fil(nums):
    '''
    this is function is used to filter max number.

    num: list
    return the maximum number of three:
    '''
    ret = []
    print(nums)
    for i in range(len(nums)):
        flag = False
        for j in range(len(nums)-i-1):
            if nums[j] < nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                flag = True
        if not flag:
            break
    print(nums)
    ret = nums[0:3]
    return ret

print(*fil([random.randint(1,20) for _ in range(20)]))