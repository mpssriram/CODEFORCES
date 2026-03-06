def binary_search(arr,low,high,x):
    ans = len(arr)

    while low <= high:
        mid = (low+high)//2

        if arr[mid] >= x:
            ans = mid
            high = mid-1
        else:
            low = mid+1

    return ans


def count(n,b):
    return binary_search(b,0,len(b)-1,n+1)-1


t = int(input())
for _ in range(t):
    inn  = int(input())
    swords = list(map(int,input().split()))
    hits = list(map(int,input().split()))
    
    swords.sort()
    maxi = -1
    prefix = [0]
    for ii in range(inn):
        prefix.append(prefix[ii] + hits[ii])

    for i in range(inn):
        usable_swords = inn - binary_search(swords,0,inn-1,swords[i])
        answer = count(usable_swords,prefix)

        maxi = max(maxi, swords[i]*answer)

    print(maxi)



        


