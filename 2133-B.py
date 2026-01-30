t = int(input())
for _ in range(t):
    inn = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse = True)
    if inn%2 == 0:
        pass
    else:
        arr.append(0)
    emeralds = 0
    ii = 0
    while ii < len(arr):
        maximum = max(arr[ii],arr[ii+1])
        emeralds += maximum
        ii += 2

    print(emeralds)

