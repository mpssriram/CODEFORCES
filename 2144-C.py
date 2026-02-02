def dp(a):
    return a+1

t = int(input())
for _ in range(t):
    inn = int(input())
    arr = list(map(int,input().split()))
    count = 0
    last = -10**18
    for ii in range(inn):
        if arr[ii]-last>=2:
            last = arr[ii]
        else:
            count += 1

    print(inn-count)