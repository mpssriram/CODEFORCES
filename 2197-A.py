def summation(x):
    digits = []
    while x > 0:
        digit = x % 10
        digits.append(digit)
        x //= 10
    return sum(digits[::-1])




t = int(input())
for _ in range(t):
    x = int(input())
    count = 0
    for i in range(x+1,x+82):
        if i - summation(i) == x:
            count += 1
        else:
            pass

    print(count)

        
    
