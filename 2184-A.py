n = int(input())
for _ in range(n):
    a = int(input())
    if a == 2 or a == 3:
        print(a)
    elif a%2 == 0:
        print(0)
    else:
        print(1)