import math as mt

def solve(a, n):
    x, y, z = a 
    if (x * y * z) % n != 0:
        return (-1,)
    p1 = mt.gcd(x, n)
    n //= p1

    p2 = mt.gcd(y, n)
    n //= p2

    p3 = mt.gcd(z, n)
    n //= p3

    if n != 1:
        return (-1,)   
    return (p1 - 1, p2 - 1, p3 - 1)

a = list(map(int, input().split()))
b = int(input())
print(*solve(a, b))
