m = 1000000007
t = int(input())

for i in range(t):
    n = (int(input())-1)//2
    print((((16*(n**3)+26*n)//3) + ((10*(n**2))+1))%m)
