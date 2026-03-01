a = list("uwuuwu")

changed = True

i = 0
while i < len(a) - 1:
    if a[i] == a[i+1]:
        a.pop(i)      
        a.pop(i)      
        i = 0         
    else:
        i += 1
print(a)
            