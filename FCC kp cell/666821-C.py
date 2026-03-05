n = int(input())
for _ in range(n):
    a = list(map(int,input().split()))
    if a[1] > a[0]:
        print(-1)
    else:
        if a[0]%a[1] == 0:
            print(900+ a[0])
        else:
            remainder = a[0]%a[1]
            if remainder == 0:
                print(a[0]*(10**(len(str(a[0])))) + a[0])
            else:
                

