a = [True]*1000001 
for i in range(2,1000000): 
    if (a[i] == False): 
        continue 
    for j in range(2*i,1000000,i): 
        a[j] = False

res = [0]*1000001
res[0] = 0
res[1] = 0
for i in range(2,1000000): 
    if (a[i] == True):
        res[i] = res[i-1]+i
    else:
        res[i] = res[i-1]
t = int(input())
for _ in range(t):
    n = int(input())
    print(res[n])
