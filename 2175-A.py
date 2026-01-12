import math as mt
def sequential(b):
    for i in range(len(b)):
        if b[i] != i + 1:
            return "fail"
    return "true"


n = int(input())
for _ in range(n):
    a = int(input())
    b = list(map(int,input().split()))
    b = list(set(b))
    print(b)
    print(b[len(b)-1])
    

