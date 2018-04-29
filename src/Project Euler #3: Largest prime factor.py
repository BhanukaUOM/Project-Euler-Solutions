import math

t = int(input())

for _ in range(t):
    n = int(input())
    m = n
    j = 0
    for i in range(2, int(math.sqrt(n))+1):
        while m%i==0:
            m//=i
            j=i
    print(m if m>1 else j)
