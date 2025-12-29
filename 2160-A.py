n = int(input())
ab = []
count1 = []
 
for _ in range(n):
    b = list(map(int,input().split()))
    a = list(map(int,input().split()))
    ab.append(a)
    count1.append(b)
i = 0

while i < n:
    mex = 0
    while mex >= 0:
        if mex in ab[i]:
            mex += 1
        else:
            print(mex)
            break
    i +=1           
