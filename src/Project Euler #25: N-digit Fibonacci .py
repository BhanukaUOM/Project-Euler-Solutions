arr = [1]

a = 0
b = 1
length = 2
count = 1
while True:
    a, b = b, a+b
    count += 1
    if len(str(b))== length:
        length += 1
        arr.append(count)
    if len(str(b))>=5000:
        break
        
t = int(input())
for _ in range(t):
    n = int(input())
    print(arr[n-1])
