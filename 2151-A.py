def incremental(a):
    a = a.split(",")
    for i in range(len(a) - 1):
        if int(a[i + 1]) != int(a[i]) + 1:
            return False
    return True

def has_reset(a):
    a = a.split(",")
    for i in range(len(a) - 1):
        if int(a[i + 1]) == 1 and int(a[i + 1]) != int(a[i]) + 1:
            return True
    return False

def is_valid(a):
    a = a.split(",")
    for i in range(len(a) - 1):
        cur = int(a[i])
        nxt = int(a[i+1])
        if nxt != cur + 1 and nxt != 1:
            return False
    return True

def finder(z,y,x):
    if not is_valid(x):
        return 0
    elif z == 1:
        return f"{y-int(x)+1}"
    elif incremental(x) == True :
        m = len(x.split(","))
        last = int(x.split(",")[0]) + m - 1
        return str(y - last + 1)
    else:
        if has_reset(x) == True:
            return "1"
        else:
            return "0"


t = int(input())
for _ in range(t):
     a = list(map(int,input().split()))
     b = ",".join(input().split())
     print(finder(int(a[1]),int(a[0]),b))
