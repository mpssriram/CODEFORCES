n = int(input())
for _ in range(n):
    x,y,z = list(map(int,input().split()))
    if x == y:
        if x + y > z:
            print(x+y -z)
        else:
            print(x)
    elif x + y > z:
        if y < z:
            print(z-y)
        elif y == z:
            print(z)
        else:
            print(0)
    else:
        print(0)    

