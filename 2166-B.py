t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    if n * b <= a or a == b:
        print(1)
    else:
        print(2)

