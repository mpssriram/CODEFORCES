def sol():
    a,b = map(int,input().split())
    if a&1 and b&1: return a*b + 1
    if b&1: return -1
    if a&1 and b&2: return -1
    if a&1: b//=2
    else: a//=2
    b//=2
    return 2*(a*b + 1)
 
for _ in range(int(input())):
    print(sol())








    

    