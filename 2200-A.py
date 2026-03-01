t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    list_arr = [i for i in range(1, n+1)]
    if arr.count(max(arr)) == 1:
        print(1)
    else:
        print( arr.count(max(arr)))