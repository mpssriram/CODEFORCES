t = int(input())
for _ in range(t):
    string = input()
    values = string.count('?')
    if len(string) == values:
        print(10**(len(string)-1)*9)
    else:
        if string[0] == '0':
            print(0)
        else:
            if string[0] == '?':
                print(9*10**(values-1))
            else:
                print(10**values)

