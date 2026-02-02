t = int(input())
for _ in range(t):
    inn = int(input())
    arr = list(map(int,input().split()))
    if len(arr)%2 == 0:
        pass
    else:
        arr.append(0)
    
    arr.sort(reverse = True)
    mean_inn = 0
    count = 0


    for ii in range(len(arr)-1):
        int1 = arr[ii]
        int2 = arr[ii+1]
        mean = (int1+int2)/2
        if mean > mean_inn:
            count += max(int1,int2)
            mean_inn += mean
        else:
            pass


    print(count)  