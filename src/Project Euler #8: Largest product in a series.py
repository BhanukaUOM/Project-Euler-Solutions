t = int(input())
for _ in range(t):
    n, k = input().split(' ')
    k = int(k)
    n = int(n)
    m = input()
    max = 0
    for i in range(n-k):
        p=1
        for j in range(k):
            p *= int(m[i+j])
        if p>max:
            max=p
    print(max)
