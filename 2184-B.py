import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s, k, m = map(int, input().split())
    
    r1 = m % k
    if s <= k:
        ans = max(0, s - r1)
    else:
        r2 = m % (2 * k)
        if r2 < k:
            ans = s - r1
        else:
            ans = k - r1
    
    print(ans)
