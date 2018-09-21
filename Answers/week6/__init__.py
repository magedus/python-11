import threading

threading.Condition


origin=[1, 30,20,40,60,50,10,80,70,90]
origin.insert(0,0)
total=len(origin)-1
print(total)


def heap_adjust(n,i,array:list):
    while 2*i<=n:
        lchile_index=2*i
        max_child_index=lchile_index #n=2*i
        if n>lchile_index and array[lchile_index+1]>array[lchile_index]:
            max_child_index=lchile_index+1
        if array[max_child_index]>array[i]:
            array[i],array[max_child_index]=array[max_child_index],array[i]
            i=max_child_index
        else:
            break
    return array

print('origin:', origin, total)
def max_heap(total,array:list):
    for i in range(total//2,0,-1):
        heap_adjust(total,i,array)
        print(i, array, '======', total//2)
    return  array

print(max_heap(total,origin))
