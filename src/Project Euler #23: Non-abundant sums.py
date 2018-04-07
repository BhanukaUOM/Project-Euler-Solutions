import math

n = 30000

div_sum = [1 for i in range(n)]

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
for i in range(1,n):
    if div_sum[i]>i:
        arr.append(i)
        
all_sums = {}
for i in range(len(arr)):
    for j in range(len(arr)):
        all_sums[arr[i]+arr[j]] = True
    
t = int(input())
for _ in range(t):
    n = int(input())
    if n>28123:
        print("YES")
    else:
        print("YES" if n in all_sums else "NO")
