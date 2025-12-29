n = int(input())
ab = []
count1 = []
 
for _ in range(n):
    b = list(map(int,input().split()))
    a = list(map(int,input().split()))
    ab.append(a)
    count1.append(b)
i = 0
list1 = []
list2 = []
while i < n:
    list1.append(ab[i].count(-1))
    list2.append(ab[i].count(0))
    list3 = []

    if list1[i] > 0:
        if list1[i]%2 == 0:
            list3.append(0)
        elif list1[i] == 1:
            list3.append(2)
        else:
            list3.append(2)
    if list2[i] >= 0:
        list3.append(list2[i])
    c = sum(list3)
    print(c)
    i += 1
    
