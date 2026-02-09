t = int(input())
for _ in range(t):
    n,x,y = map(int,input().split())
    arr = list(map(int,input().split()))
    moves = 0
    for i in range(n):
        moves += arr[i]//x
    maxi = 0
    for j in arr:
        amount =  j  + (moves - (j//x))*y
        maxi = max(maxi,amount)
        
    print(maxi)
