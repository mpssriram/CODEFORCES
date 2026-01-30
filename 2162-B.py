t = int(input())
for _ in range(t):
    a = int(input())
    b = input()
    if b[::-1] == b:
        print(0)
        print()
    else:
        zeroes = [str(i+1) for i, c in enumerate(b) if c == '0']
        print(len(zeroes))
        print(" ".join(zeroes))

        
               
