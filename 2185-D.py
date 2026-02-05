import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, h = map(int, input().split())
    original = list(map(int, input().split()))
    a = original[:]

    changed = []

    for _ in range(m):
        b, c = map(int, input().split())
        i = b - 1

        if a[i] + c > h:
            for idx in changed:
                a[idx] = original[idx]
            changed = []
        else:
            if a[i] == original[i]:
                changed.append(i)
            a[i] += c

    print(*a)