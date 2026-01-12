def recursive(x,y):
    count = 0
    max = x
    min = x
    if x == y:
        return 0
    elif y == 0:
        return -1
    else:
        while count >= 0:
            max1 = max//2 + max%2
            min1 = min//2
            if y == max1 or y == min1:
                return count + 1
            else:
                if y <= max1:
                    max = max1
                    min = min1
                    count += 1
                else:
                    return -1
n = int(input())
for _ in range(n):
     x,y = list(map(int,input().split()))
     print(recursive(x,y))


