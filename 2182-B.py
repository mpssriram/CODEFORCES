t = int(input())
for _ in range(t):
    A, B = map(int,input().split())
    a, b = A, B
    n = 0
    count1 = 0
    while n >= 0:
        if n%2 == 0:
            if a < 2**n: break
            a -= 2**n
        else:
            if b < 2**n: break
            b -= 2**n
        count1 += 1
        n += 1
    a, b = A, B
    n = 0
    count2 = 0
    while n >= 0:
        if n%2 == 0:
            if b < 2**n: break
            b -= 2**n
        else:
            if a < 2**n: break
            a -= 2**n
        count2 += 1
        n += 1

    print(max(count1, count2))


            

