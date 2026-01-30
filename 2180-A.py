n = int(input())
for _ in range(n):
    a,b,c = map(int,input().split())
    d = set()
    i = 1
    while i > 0:
        e = ((b+(i*c))%a)
        if e in d:
            break
        else:
            d.add(e)
            b = e
        
    print(max(d))
