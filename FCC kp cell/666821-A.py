n = int(input())

for _ in range(n):
    a = int(input())
    if a == 0:
        print(0,0)
    elif a == 1:
        print(1,1)
    else:
        if a%2 == 0:
            print(int(a/2), int(a/2))
        else:
            print(int((a-1)/2), int((a-1)/2) + 1)





