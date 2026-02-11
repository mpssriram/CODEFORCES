arr = input()
listed = arr.split('WUB')
append = []
for i in range(len(listed)):
    if len(listed[i]) > 0:
        append.append(listed[i])


print(' '.join(append))