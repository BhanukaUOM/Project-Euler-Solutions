import fractions 
  
# Returns the lcm of first n numbers 
def lcm(n): 
    ans = 1    
    for i in range(1, n + 1): 
        ans = (ans * i)//fractions.gcd(ans, i)         
    return ans 

t = int(input())
for _ in range(t):
    n = int(input())
    print(lcm(n))
