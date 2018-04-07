a = [0]*200008
for i in range(2,100000):
    if (a[i] == 1):
        continue
    for j in range(2*i,200000,i):
        a[j] = 1
        
primes = []
for i in range(2,200000):
    if a[i] == 0:
        primes.append(i)
        
        
for _ in range(int(input())):
    print (primes[int(input())-1])
