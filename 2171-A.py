n = int(input())

for _ in range(n):
    a = int(input())

    if a%2 != 0:
        print(0)
    else:
        if a%4 == 0:
            print(a//4+1)
        else:
            print((a+a%4)//4)