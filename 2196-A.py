


t = int(input())
for _ in range(t):
    p,q = map(int,input().split())
    if 2*q <= (3*p) and p < q:
        print('Bob')
    else:
        print('Alice')

