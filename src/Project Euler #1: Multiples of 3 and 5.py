t = int(input().strip())
for _ in range(t):
    n = int(input())-1
    print((((n//3*(n//3+1)*3)+(n//5*(n//5+1)*5)-(n//15*(n//15+1)*15))//2))
