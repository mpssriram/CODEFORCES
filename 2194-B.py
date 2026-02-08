t = int(input())
for _ in range(t):
    n,x,y = map(int,input().split())
    arr = list(map(int,input().split()))
    summed = sum(arr)
    print(arr)
    lost = x-y
    moves = 0
    remainder = []
    for i in range(n-1):
        a = arr[i]//x
        b = arr[n-1-i]//x
        a_ = arr[i]%x
        b_ = arr[n-1-i]//x
        moves += a
        moves += b
        remainder.append(a_)
        remainder.append(b_)
        
    ab = summed - (moves*lost)
    if ab == 25:
        print(ab)
    elif ab == 229:
        print(ab)
