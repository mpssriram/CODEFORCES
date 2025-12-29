n = int(input())
for _ in range(n):
    a = list(map(int,input().split()))
    
    if a[1]%2 == 0:
        print(0)
    else:
        print(a[0])
    