t = int(input())
for _ in range(t):
    stri = list(input())
    
    count = -1
    for i in range(len(stri)-1):
        if (stri[i] == 'Y' and stri[i+1] == 'Y') or (stri[i] == 'Y' and stri[i+1] == "N") or (stri[i] == 'N' and stri[i+1] == "Y"):
            count = -1
        else:
            count += 1
    if count == -1:
        print('NO')
    else:
        print('yes')


        
