fact = [1, 1]
for i in range(2, 10):
    fact.append(fact[i-1]*i)
    
n = int(input())
ans = 0
for i in range(10, n+1):
    summ = 0
    for j in str(i):
        summ += fact[int(j)]
    if summ%i==0:
        ans += i
        
print(ans)
