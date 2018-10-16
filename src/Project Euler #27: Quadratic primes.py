n = 100000
prime = [True for i in range(n+1)] 
p = 2
while (p*p <= n): 
    if (prime[p] == True): 
        for i in range(p*2, n+1, p): 
            prime[i] = False
    p += 1
        
n = int(input())
a = 0
b = 0
maxi = 0
for i in range(-n, n+1):
    for j in range(-n, n+1):
        c = 0
        for k in range(1000000):
            if(prime[k*k+i*k+j]==True):
                c += 1
            else:
                break
        if c>maxi:
            maxi = c
            a = i
            b = j
            
print(a,b)
