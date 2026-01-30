t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    b = max(a)*len(a)
    print(b)