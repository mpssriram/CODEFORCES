
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    surplus = 0
    for i in range(n):
        if a[i] > b[i]:
            surplus += a[i] - b[i]

    print(surplus + 1)
