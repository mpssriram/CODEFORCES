t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))

    i = 0   

    for x in a:
        while i < n and p[i] != x:
            i += 1
        if i == n:
            print('NO')
            break

    else:
        print("YES")

