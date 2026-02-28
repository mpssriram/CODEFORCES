n,k = map(int,input().split())
W = list(map(int,input().split()))
W.sort()
width = 0
for i in range(n):
    if W[i] > k:
        width += 2
    else:
        width += 1
        
print(width)