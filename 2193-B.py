def decremental(c):
    values = ""
    for i in range(1,len(c)):
        if c[i] == c[i-1]-1:
            pass
        else:
            values += '1'
    
    if len(values) == 0:
        return 0
    else:
        return 1








t = int(input())
for _ in range(t):
    a = int(input())
    b = list(map(int,input().split()))

    d = decremental(b)
    if d == 0:
        print(b)
    else:
        pass
    