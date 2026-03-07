import math
def divisors(n):
    
    factors = set()
    if n == 1:
        return {1}
    
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
        i += 1
    
    factors = factors - {1,n}
    return sorted(list(factors))




t = int(input())
for _ in range(t):
    inn = int(input())
    arr = list(map(int,input().split()))
    ans = max(arr)*min(arr)
    if sorted(arr) == divisors(ans):
        print(ans)
    else:
        print(-1)