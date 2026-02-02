t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr_sorted_new = list(range(1, n+1))

    present = set(arr) - {0}
    missing_num = [x for x in arr_sorted_new if x not in present]

    missing_num.sort(reverse=True)  

    idx = 0
    for i in range(n):
        if arr[i] == 0:
            arr[i] = missing_num[idx]
            idx += 1

    diff = []
    for j in range(n):
        if arr[j] != arr_sorted_new[j]:
            diff.append(j)

    if not diff:
        print(0)
    else:
        print(max(diff) - min(diff) + 1)


            