t = int(input())
for _ in range(t):
    arr = input()  
    i = 0
    count_zero = arr.count('0')
    count_one = arr.count('1')
    
    while i < len(arr):
        if arr[i] == '0':
            if count_one == 0:
                break
            count_one -= 1
        else:
            if count_zero == 0:
                break
            count_zero -= 1
        i += 1
        
    print(len(arr) - i)