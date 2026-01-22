t = int(input())
for _ in range(t):
    n = list(map(int , input().split()))
    if (n[1]%2 != 0 and n[2]%2 == 0) or (n[1]%2 == 0 and n[2]%2 != 0):
        print("no")
    else:
        print("YES")
    
