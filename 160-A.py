inn = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
count = 0
sum1 = 0
for i in arr:
    sum1 += i
    print(sum1)
    if sum1 >  sum(arr)//2:
        print(count)
        break
    else:
        count += 1
else:
    print(count)

