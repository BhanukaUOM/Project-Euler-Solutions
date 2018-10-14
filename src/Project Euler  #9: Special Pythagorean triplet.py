import math

t = int(input())
dp = {}
ans = [-1 for i in range(3001)]
for i in range(3001):
    dp[i*i] = True
    
for i in range(1, 3001):
    for j in range(1, 3001):
        q = (i*i + j*j)
        if q in dp:
            if (i+j+int(math.sqrt(q))) < 3001:
                if (i*j*int(math.sqrt(q)))>ans[i+j+int(math.sqrt(q))]:
                    ans[i+j+int(math.sqrt(q))] = (i*j*int(math.sqrt(q)))

for _ in range(t):
    n = int(input())
    print(ans[n])
    
