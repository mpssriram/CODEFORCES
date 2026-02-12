t = int(input())
for _ in range(t):
    p,q = map(int,input().split())
    count = 0
    if p/q == 2/3:
        print('Bob')
    elif p == q:
        print('Alice')
    else:
        if abs(p-q)%6 == 0 or abs(p-q)%4 == 0:
            print('Bob')
        else:
            print('Alice')



