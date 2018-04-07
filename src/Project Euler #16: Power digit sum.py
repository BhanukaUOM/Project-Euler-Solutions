t = int(input())

for _ in range(t):
    n = int(input())
    n = 1<<n
    ans = 0
    
    for i in str(n):
        ans += int(i)
        
    print(ans)
