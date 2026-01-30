t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    string = input()
    count = 0
    awake = 0
    i = 0
    while i < len(string):
        if string[i] == "1":
            awake = k
        else:
            if awake > 0:
                awake -= 1
            else:
                count += 1
        i += 1

    print(count)