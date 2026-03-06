import math

def lcm(a,b):
    return a*b//math.gcd(a,b)

def find_values(N):
    ans = 1
    for start in range(1,60):
        val = 1
        for nxt in range(start, start+60):
            val = lcm(val, nxt)
            
            if val > N:
                break
                
            if N % val == 0:
                ans = max(ans, nxt-start+1)

    return ans


t = int(input())
for _ in range(t):
    inn = int(input())
    print(find_values(inn))