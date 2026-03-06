

t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    for i in range(1 , n+1):
        if n % i == 0:
            c += 1
        else:
            break
    print(c)




            