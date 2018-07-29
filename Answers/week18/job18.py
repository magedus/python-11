# 1、使用归并排序、插入排序算法对列表进行排序


def insert_sort(alist):
    length = len(alist)
    for i in range(1, length):
        current_value = alist[i]
        j = i
        while j > 0 and alist[j - 1] > current_value:
            alist[j] = alist[j - 1]
            j = j - 1
        alist[j] = current_value
    return alist


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i = i + 1
            else:
                alist[k] = right_half[j]
                j = j + 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            alist[k] = right_half[j]
            j = j + 1
            k + k + 1
    return alist


# test
l1 = [3, 2, 1, 0, 7, 11, 56, 23]
print(insert_sort(l1))
print(merge_sort(l1))

# 2、实现一个LRU缓存类，至少包含get和put方法
