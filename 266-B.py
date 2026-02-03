def loop(a,b):
    string_1 = a
    ii = 0
    while ii < b-1:
        if string_1[ii] == "B" and string_1[ii+1] == "G":
            string_1[ii] = "G"
            string_1[ii+1] = 'B'
            ii += 2
        else:
            ii += 1

length,time = map(int,input().split())
arr = list(input())
t = 0
while t < time:
    loop(arr,length)
    
    t += 1

print(''.join(arr))


 