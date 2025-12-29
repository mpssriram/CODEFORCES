n = int(input())
ab = []
count1 = []
 
for _ in range(n):
    b = list(map(int,input().split()))
    a = list(map(str,input().split()))
    ab.append(a)
    count1.append(b)
i = 0
while i < n:
    yes = []
    no = []
    for j in range(count1[i][0]):
        if (ab[i][0][j] in ab[i][1]) and ab[i][0].count(ab[i][0][j]) == ab[i][1].count(ab[i][0][j]):
            yes.append("yes")
        else:
            no.append("no")
            
    if no.count("no") != 0:
        print("no")
    else:
        print("yes")
    i += 1