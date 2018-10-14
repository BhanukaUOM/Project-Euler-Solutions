def leap(year):
    if year%400 == 0:
        return True;
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False

ms = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def days(y, m):
    if m == 2 and leap(y):
        return 29;
    else:
        return ms[m];

def getDays(y, m):    
    rem = y-1
    yls = rem//400 + rem//4 - rem//100
    ans = yls+rem
    
    p = 1
    while p<m:
        ans += days(y, p)
        p+=1
    return ans%7;

def get(y, m, offset, ys, ms):
    if offset%7 == 6:
        ans = 1
    else:
        ans = 0
    tmp = ms
    while ys<y or tmp<m:
        offset = (offset+days(ys, tmp))%7;
        if offset%7==6:
            ans+=1
        tmp+=1
        if tmp==13:
            tmp=1
            ys+=1
    return ans;

t = int(input())
for _ in range(t):
    y1, m1, d1 = map(int, input().split(' '))
    y2, m2, d2  = map(int, input().split(' '))
    
    if d1!=1:
        m1+=1
        d1 = 1;
        if m1==13:
            y1+=1
            m1=1
    before = (getDays(y1, m1)-getDays(1900, 1)+7)%7
    b = get(y2, m2, before, y1, m1)
    print(b)
