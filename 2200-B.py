t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if sorted(arr) == arr:
        print(len(arr))
    else:
        sorted_arr = sorted(arr)
        count = 0
        element = 0
        i = 0
        while i < n-1:
            if sorted_arr[i] != arr[i]:
                if count == 0:
                    print(count+1)
                    break
                else:
                    print(count)
                    break
            elif sorted_arr[i] == arr[i] and element != sorted_arr[i]:
                element = sorted_arr[i]
                count += 1
            i += 1
        