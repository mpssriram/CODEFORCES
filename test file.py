n = int(input())
for _ in range(n):
    b = int(input())
    a = list(map(int,input().split()))

    if b == 1:
        print(1)
    else:
        a = sorted(set(a))
        n,k = a[0],a[1]
        d = [ii - n for ii in a]
        e = [jj - k for jj in a]
        mex = 0
        while mex >= 0:
                if mex in d :
                    mex += 1
                else:
                    f = mex
                    break
        mex1 = 0
        while mex1 >= 0:
            if mex1 in e:
                mex1 += 1
            else:
                g = mex1
                break
        print(max(f,g))







    

    