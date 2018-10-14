maxi = -1

def rec(arr, x, y, su, n):
    global maxi
    if(su>maxi):
        maxi = su
    if(x<n-1):
        if(y<len(arr[x+1])-1):
            rec(arr, x+1, y+1, su+arr[x+1][y+1], n)
        rec(arr, x+1, y, su+arr[x+1][y], n)

t = int(input())
for _ in range(t):
    arr = []
    n = int(input())
    for i in range(n):
        arr.append(list(map(int, input().split(' '))))
    maxi = -1
    rec(arr, 0, 0, arr[0][0], n)
    print(maxi)
