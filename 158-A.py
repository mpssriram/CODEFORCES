n,k = map(int,input().split())
arr = list(map(int,input().split()))
count = 0
if arr[k-1] == 0 and set(arr) == {0}:
    print(0)
else:
    for i in range(n):
        if arr[i] >= arr[k-1] and arr[i] > 0 :
            count += 1

    print(count)
