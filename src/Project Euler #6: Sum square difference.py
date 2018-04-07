dp = {}
dp[0] = 0

def sqofsum(n):
    return (n*(n+1)//2)**2

def sumofsq(n):
    global dp
    if n in dp:
        return dp[n]
    for i in range(n+1):
        if i not in dp:
            dp[i] = dp[i-1]+i**2
    return dp[n]

t =int(input())
for _ in range(t):
    n = int(input())
    print (sqofsum(n) - sumofsq(n))
