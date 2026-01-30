lengths = [4, 3, 2, 6]

a = 29
count = 0
lengths.sort(reverse = True)
for i in lengths:
    if a >= i:
        use = a//i
        count += 1
        a -= use*i

print(count)
