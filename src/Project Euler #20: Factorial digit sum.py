import math

t = int(input())
for _ in range(t):
    n = int(input())
    n = math.factorial(n)
    
    c = 0
    for i in str(n):
        c += int(i)
    
    print(c)
