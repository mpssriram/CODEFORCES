
t = int(input())
for _ in range(t):
    inn = int(input())
    arr = list(map(int,input().split()))
    bom = arr
    if arr == sorted(arr,reverse=True):
        for i in arr:
            print(i, end = " ")
    else:
        minimum = min(arr)
        maximum = max(arr)
        arr = list(set(arr) - {maximum,minimum})
        arr = sorted(arr)
        arr.insert(0,maximum)
        arr.insert(1,minimum)
        if arr == bom:
            arr = list(set(arr) - {maximum,minimum})
            arr.insert(0,maximum)
            arr.insert(inn-1,minimum)
            for i in arr:
                print(i, end = " ")
        else:
            for i in arr:
                print(i, end = " ")

            

