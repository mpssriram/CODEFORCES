import math as mt



n = int(input())
for _ in range(n):
    c = int(input())
    d = bin(c)
    count = str(c)
    count_zero = count.count("0")

    output = len(count) - count_zero
    bin_count = str(d)
    
    bin_count_zero = bin_count.count("0")
    bin_output = len(bin_count)- bin_count_zero

    if bin_output > output:
        print(output)
    else:
        print(bin_output)