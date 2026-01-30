n = int(input())
for _ in range(n):
    t = int(input())
    if t == 2:
        print(1,2)
    else:
        if t%2 == 0:
            b = []
            i = 1
            while i <= t//2:
                b.append(i)
                b.append(t+1 - i)
                i += 1

            b = b[::-1]
            for i in b:
                print(i,end = " ")
        else:
            b = []
            i = 1
            while i <= (t+1)//2:
                b.append(i)
                b.append(t+1 - i)
                i += 1

            b = b[::-1]
            b.remove(b[0])
            for i in b:
                print(i,end = " ")          