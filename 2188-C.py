t = int(input())
for _ in range(t):
    inn = int(input())
    arr = list(map(int, input().split()))
    arr_sorted = sorted(arr)
    
    if arr == arr_sorted:
        print(-1)
    else:
        min_val = arr_sorted[0]
        max_val = arr_sorted[-1]
        ans = 10**18 
        
        for i in range(inn):
            if arr[i] != arr_sorted[i]:
                dist_to_min = abs(arr[i] - min_val)
                dist_to_max = abs(arr[i] - max_val)
                
                limit = dist_to_min
                if dist_to_max > limit:
                    limit = dist_to_max
                
                if limit < ans:
                    ans = limit
        
        print(ans)
            
            
