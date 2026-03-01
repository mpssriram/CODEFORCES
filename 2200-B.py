t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if sorted(arr) == arr:
        print(n)
    else:
        print(1)
        