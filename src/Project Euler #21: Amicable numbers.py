import math
import itertools

n = 100001

div_sum = [1 for i in range(n)]
div_sum[0] = 0
div_sum[1] = 0

for i in range(2, n):
    sq = int(math.sqrt(i))
    for j in range(2, sq+1):        
        if i%j==0:
            p = i//j
            if p!=j:
                div_sum[i] += j + p
            else:
                div_sum[i] += j
            
arr = []

for i in range(2, n):
    if div_sum[i]<n and i == div_sum[div_sum[i]] and div_sum[i]!=i:
        arr.append(i)

t = int(input())

for _ in range(t):
    n = int(input())
    ans = 0
    for i in arr:
        if i>n:
            break
        ans += i

    print(ans)
