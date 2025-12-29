t = int(input())
for _ in range(t):
    a = int(input())
    b = input()
    
    count_last_string = b.count(b[len(b)-1])
    if count_last_string == len(b):
        print(0)
    else:
        print(len(b)-count_last_string)
