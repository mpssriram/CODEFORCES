n = int(input())
for _ in range(n):
    t = int(input())
    a = input()
    c = a.count('1')
    
    if c == 0:
        print((t + 2) // 3)
    else:
        string = a.split('1')
        count = 0
        
        for i in range(len(string)):
            segment = string[i]
            length = len(segment)
            
            if i == 0 or i == len(string) - 1:
                count += length // 3
                if length % 3 == 2:
                    count += 1
            else:
                count += length // 3
                
        print(count+c)