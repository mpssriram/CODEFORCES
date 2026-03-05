for _ in range(int(input())):
    n ,x ,y = map(int ,input().split())
    a = list(map(int , input().split()))
    a1 = a[:x]
    a2 = a[x:y]
    a3 = a[y:]
    m = min(a2)
    i1 = a2.index(m)
    A1 = a2[i1:]+a2[:i1]
 
    a5 =a1+a3
    if x==0 and y == n:
        print(*(A1))
    elif m > max(a5):
        print(*(a5+A1))
    else:
        for i in range(len(a5)):
            if a5[i] > m:
                k = i
                break
        b1 = a5[:k]
        b2 = a5[k:]
        c = b1+A1+b2
        print(*c)
                

        
        

    
            