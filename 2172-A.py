a = list(map(int,input().split()))

if max(a) - min(a) >= 10 :
    print("check again")
else:
    b = sorted(a)
    print('final',b[1])