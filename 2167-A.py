n = int(input())
ab = []
for _ in range(n):
    a = list(map(int,input().split()))
    ab.append(a)
i = 0
while i<n:
    if  len(ab[i])== 4 and ab[i][0] ==ab[i][1] == ab[i][2] == ab[i][3]:
        print("YES")
    else:
        print("NO")
    i += 1
