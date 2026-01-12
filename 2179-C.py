
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    
    k1 = a[0]           
    k2 = a[1] - a[0]    
    
    print(max(k1, k2))

    
    