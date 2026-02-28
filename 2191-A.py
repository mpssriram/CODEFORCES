t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    blue = []
    red = []
    i = 0
    while i < n:
        if i%2 == 0:
            blue.append(arr[i])
        else:
            red.append(arr[i])
        i += 1
    
    j = 1
    while j <= n-1:
        if j in blue and j+1 in red or j in red and j+1 in blue:
            pass
        else:
            print('NO')
            break
        j += 1
    else:
        print('YES')
            
            
        

        