n = int(input())
for _ in range(n):
    inn = int(input())
    arr = input().split()
    s = ""
    for a in arr:
        back = s + a
        front = a + s
        if front < back:
            s = front
        else:
            s = back
    
    print(s)