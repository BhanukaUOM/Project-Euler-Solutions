n = int(input())
arr = []

for _ in range(n):
    arr.append(input())
arr.sort()

t = int(input())
for _ in range(t):
    
    s = input()
    sum = 0
    for i in s:
        sum += ord(i)-ord('A')+1
    print((arr.index(s)+1)*sum)
