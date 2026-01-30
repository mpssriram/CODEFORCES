t = int(input())
for _ in range(t):
    a = int(input())
    b = input()
    c = b[::-1]
    if c == b:
        print(0,"\n","")
    else:
        for i in range(len(b)-1):
            if b[i:i+2] == '01':
                string = list(b)
                string.pop(i)
                string.pop(i)
                d = ''.join(string)
                if d[::-1] != d:
                    pass
                else:
                    print(i+1,i+2)
                    break
            else:
                pass
        
        else:
            for j in range(len(b)):
                print(j+1,end = ' ')
        
        
        
               
