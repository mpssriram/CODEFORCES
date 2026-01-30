n = int(input())
for _ in range(n):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if sum(b) == a[1]:
        print('YES')
    elif sum(b) > a[1]:
        print('NO')
    else:
        c = a[1] - sum(b)
        x = c%a[2]
        if x != 0:
            print('NO')
        else:
            print('YES')    

