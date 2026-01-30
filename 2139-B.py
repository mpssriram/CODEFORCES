t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    best = 0
    cur = 0
    k = min(n,m)
    for i in range(n):

        cur += arr[i]*(m-i)
        
        best = max(best,cur)
        

    
    print(best)