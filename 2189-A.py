

t = int(input())
for _ in range(t):
    n, h, l = map(int, input().split())
    arr = list(map(int, input().split()))

    A = B = C = 0  # row-only, col-only, both
    for x in arr:
        if x <= h and x <= l:
            C += 1
        elif x <= h:
            A += 1
        elif x <= l:
            B += 1

    ans = min((A + B + C) // 2, A + C, B + C)
    print(ans)


            
        
            




