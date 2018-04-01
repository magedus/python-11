triangle = [[1],[1,1]]
n = 10
for i in range(2,n):
    pre = triangle[i-1]
    cur = [1]
    for j in range(0,i-1):
        cur.append(pre[j]+pre[j+1])
    cur.append(1)
    triangle.append(cur)
print(triangle)