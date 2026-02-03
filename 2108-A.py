def series(n):
    a = [0, 0]
    add = 1
    count = 0   

    for _ in range(n-2):
        a.append(a[-1] + add)
        count += 1

        if add == 1:          
            add += 1
            count = 0
        elif count == 2:      
            add += 1
            count = 0

    return a


t = int(input())
for _ in range(t):
    inn = int(input())
    if inn == 1:
        print(1)
    else:
        b = series(inn)
        print(max(b)+2)
        