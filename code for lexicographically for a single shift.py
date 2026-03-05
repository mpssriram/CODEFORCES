t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] != i:
            pos = arr.index(i+1)
            arr[i:pos+1] = reversed(arr[i:pos+1])
            break
    
    print(*arr)
            