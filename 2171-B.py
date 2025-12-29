n = int(input())
for _ in range(n):
    b = int(input())
    a = list(map(int,input().split()))
    cd = []
    copy = a.copy()
    for i in range(len(a)):
        if a[i] == -1:
            a[i] = 0
    cc = a[len(a)-1]
    dd = a[0]
    g = [a[i+1]-a[i] for i in range(len(a)-1)]
    d = abs(sum(g))

    if copy[len(a)-1] == -1 or copy[0] == -1:
        print(0)
    else:
        print(d)
    
    def list_str():
        for l in range(len(a)):
                e = str(a[l])
                cd.append(e)
        return(" ".join(cd))


    if copy[len(a)-1] == -1:
        if copy[0] == -1:
            print(list_str())
            
        else:
            a[len(a)-1] = a[0]
            print(list_str())
    else:
        if copy[0] == -1:
            a[0] = d
            a[len(a)-1] = d
            print(list_str())
        else:
            print(list_str())

   





    


    