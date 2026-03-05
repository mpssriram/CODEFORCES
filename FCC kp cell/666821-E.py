n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int,input().split()))
    if sum(b) > a[1]:
        print(0)
    else:
        