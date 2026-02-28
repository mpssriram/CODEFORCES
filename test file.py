t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    W = list(map(int,input().split()))
    W.sort()
    k = min(k,n-k)
    ans = 0
    count = 0
    for i in range(n):
        if count > k-1:
            left = sum(W[k:])
            print(left-ans)
            break
        else:
            ans += W[i]
            count += 1






    

    