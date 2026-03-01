t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(input())
    if n%2 != 0:
        print('NO')
    else:
        i = 0
        while i < len(arr) - 1:
            if arr[i] == arr[i+1]:
                arr.pop(i)      
                arr.pop(i)      
                i = 0         
            else:
                i += 1

        if len(arr) == 0:
            print('YES')
        else:
            print('NO')
