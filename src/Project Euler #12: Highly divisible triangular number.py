import math

a = [0]*200008 
for i in range(2,200000): 
    if (a[i] == 1): 
        continue 
    for j in range(2*i,200000,i): 
        a[j] = 1 
primes = {}
for i in range(2,200000): 
    if a[i] == 0: 
        primes[i] = True 
        
def noofdevisors(N):
    ans = 1
    for p in primes :
        if p*p*p > N:
            break
        count = 1
        #print("p",p)
        while N%p==0:
            N = N//p
            #print("N",N)
            count = count + 1
            #print("count", count)
        ans = ans * count
        #print("ans", ans)

    if N!=1:
        if N in primes:
            ans = ans * 2
        elif math.sqrt(N) in primes:
            ans = ans * 3
        else:
            ans = ans * 4
    return (ans-1)

a = []
a.append(0)
for i in range(1,100000):
    a.append(a[i-1]+i)

t = int(input())
for _ in range(t):
    n = int(input())
    zz = True
    for i in a:
        #print (i, noofdevisors(i))
        if i>=2:
            if noofdevisors(i) >= n:
                print(i)
                break
