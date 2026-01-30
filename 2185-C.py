t = int(input())

for _ in range(t):
    n = int(input())
    arr = sorted(set(map(int, input().split())))

    best = 1
    cur = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            cur += 1
        else:
            cur = 1
        best = max(best, cur)

    print(best)





        