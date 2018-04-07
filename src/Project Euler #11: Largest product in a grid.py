arr = []

for i in range(20):
    arr.append(list(map(int, input().split(' '))))
    
max = 0

for j in range(20):
    for i in range(17):
        a=1
        for k in range(4):
            a *= arr[j][i+k]
        if a>max:
            max = a
            
for j in range(17):
    for i in range(20):
        a=1
        for k in range(4):
            a *= arr[j+k][i]
        if a>max:
            max = a
            
for j in range(17):
    for i in range(17):
        a=1
        for k in range(4):
            a *= arr[j+k][i+k]
        if a>max:
            max = a
            
for j in range(17):
    for i in range(19, 2, -1):
        a=1
        for k in range(4):
            a *= arr[j+k][i-k]
        if a>max:
            max = a
            
print(max)
