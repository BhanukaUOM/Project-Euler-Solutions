ans = 0
S = [1,2,5,10,20,50,100,200]
m = 8
mod = 1000000007

n = 100000
table = [[0 for x in range(m)] for x in range(n+1)] 
for i in range(m): 
    table[0][i] = 1
for i in range(1, n+1): 
    for j in range(m): 
        x = table[i - S[j]][j] if i-S[j] >= 0 else 0
        y = table[i][j-1] if j >= 1 else 0
        table[i][j] = (x%mod+y%mod)%mod

t = int(input())
for i in range(t):
    n = int(input())
    print(table[n][m-1])
