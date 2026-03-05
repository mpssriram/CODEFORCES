a = [1, 1, 2,3,4,1,1,7,3,9]
count = 0
for i in range(9):
    for j in range(1,10):
        if a[i]*a[j] == j-i:
            count += 1

print(count)



            