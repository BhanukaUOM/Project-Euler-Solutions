arr = [0 for i in range(5000001)]
max = 0
r = 0
for p in range(2,5000001):
    i = p
    c = 1
    while i!=1:
        c += 1
        if i%2==0:
            i = i//2
        else:
            i = 3*i+1
    if max<=c:
        max = c
        r = p
    arr[p] = r
        
t = int(input())

for _ in range(t):
    n = int(input())
    print(arr[n])
