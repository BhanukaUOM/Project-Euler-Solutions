n = int(input())

ans = 0
for i in range(2, 1000000):
    s = str(i)
    summ = 0
    for j in s:
        summ += int(j)**n
    if i == summ:
        ans += i
        
print(ans)
