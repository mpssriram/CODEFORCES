n = int(input())
ab = []
for _ in range(n):
    a = list(map(int,input().split()))
    ab.append(a)
i = 0
while i < n :
    if (ab[i][0])%3 == 0:
        print(0)
    else:
        print(3 - ((ab[i][0])%3))
    i += 1