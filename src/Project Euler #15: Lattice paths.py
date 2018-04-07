arr = [[1 for i in range(501)] for j in range(501)]
for i in range(1,501):
    for j in range(1,501):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

t = int(input())

for _ in range(t):
    n, m = map(int, input().split(' '))
    print(arr[n][m]%1000000007)
