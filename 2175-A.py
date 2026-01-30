


n = int(input())
for _ in range(n):
    a = int(input())
    b = set(list(map(int,input().split())))
    mex = len(b)
    while mex > 0:
        if mex in b:
            print(mex)
            break
        else:
            mex += 1 
    
    
    

