import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = 0
    limit = int(n ** 0.5)
    
    for x in range(1, limit + 1):
        for j in range(n):
            aj = arr[j]
            i = j - x * aj
            if i >= 0 and arr[i] == x:
                count += 1
                
        for i in range(n):
            ai = arr[i]
            if ai > limit:
                j = i + ai * x
                if j < n and arr[j] == x:
                    count += 1

    print(count)