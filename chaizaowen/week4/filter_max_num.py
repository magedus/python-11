import random

def fil(nums,target=[]):
    '''
    this is function is used to filter max number.

    num: list
    return the maximum number of three:
    '''
    print(nums)
    for i in range(len(nums)):
        flag = False
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                flag = True
        if not flag:
            break
    return nums[-1],nums[-2],nums[-3]

print(*fil([random.randint(1,20) for _ in range(20)]))