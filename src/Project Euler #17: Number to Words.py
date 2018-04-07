word1 = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten","Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
word10 = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety", "Hundred"]

def ans(n):
    n = str(int(n))
    if len(n)==1:
        print(word1[int(n)], end=" ")
    elif len(n)==2:
        if int(n)<20:
            print(word1[int(n)], end=" ")
        elif int(n)%10==0:
            print(word10[int(n[0])], end=" ")
        else:
            print(word10[int(n[0])], word1[int(n[1])], end=" ")
    else:
        print(word1[int(n[0])], "Hundred", end=" ")
        if int(n)%100!=0:
            ans(str(int(n)%100))
            

t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    rev = s[::-1]
    
    if int(s)<20:
        print(word1[int(s)])
    else:
        if n==13:
            print(word1[int(s[0])], "Trillion", end=" ")
        if n>=10 and int(rev[11:8:-1])!=0:
            ans(rev[11:8:-1])
            print("Billion", end=" ")
        if n>=7 and int(rev[8:5:-1])!=0:
            ans(rev[8:5:-1])
            print("Million", end=" ")
        if n>=4 and int(rev[5:2:-1])!=0:
            ans(rev[5:2:-1])
            print("Thousand", end=" ")
        if int(s)%1000!=0:
            ans(str(int(s)%1000))
        print()
