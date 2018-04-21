import random
L = []
for i in range(20):
    L.append(random.randint(1,100))
print(L)
for i in range(len(L)):
    maxindex = i
    minindex = len(L)-i-1
    for j in range(i+1, len(L)-i-1):
        if L[minindex] > L[j]:
            minindex = j
        if L[maxindex] < L[j]:
            maxindex = j
    if maxindex != i:
        L[i], L[maxindex] = L[maxindex], L[i]
    if minindex != len(L)-i-1:
        L[len(L)-i-1], L[minindex] = L[minindex], L[len(L)-i-1]
print(L[0],L[1],L[2])