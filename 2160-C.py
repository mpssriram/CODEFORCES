import math as mt
import time as t
def brute_force_check(n):
    lower_limit = 2 ** (len(bin(n))-3)
    i = lower_limit
    upper_limit = 2 ** (len(bin(n)))
    while i < upper_limit:
        binary = bin(i)
        reversed_binary = binary[::-1]
        reversed_binary = reversed_binary[:-2]
        if int(reversed_binary,2)^int(binary,2) == n:
            return "yes"
        i += 1
    return "no"
def check_for_odd(n):
    binary = bin(n)
    new_binary = binary[2:]
    reversed_binary = new_binary[::-1]
    if int(reversed_binary,2)^int(binary,2) == 0:
        if len(new_binary)%2 == 0:
            if new_binary[len(new_binary)//2-1:len(new_binary)//2 + 1].count("0") == 2 or new_binary[len(new_binary)//2-1:len(new_binary)//2 + 1].count("1") == 2:
              return "yes"
            else:
                return "no"
        else:
            if new_binary[len(new_binary)//2] == "0":
                return "yes"
            else:
                return "no"
    else:
        return "no"

def even_simplier(n):
    while n > 0:
        if n%2 != 0:
            if mt.log2((n//2)+1).is_integer():
                if mt.log2(n+1)%2 == 0:
                    return "yes"
                else:
                    return "no"
            else:
                return check_for_odd(n)
        n = n//2
        
def finder(n):
    if n == 0:
        return "yes"
    if n > 0:
        a = mt.log2(n)
        if a.is_integer():
            return "no"
        elif n%2 == 0:
            return even_simplier(int(n//2))
        else:
            if mt.log2(n+1).is_integer():
                if mt.log2(n+1)%2 == 0:
                    return "yes"
                else:
                    return "no"
            else:
                return check_for_odd(n)
# t = int(input())
# for _ in range(t):
#      n = int(input())
#      print(finder(n))
start_time = t.time()
for j in range(10000):
    print(finder(j))
end_time = t.time()
print("time required", {end_time - start_time})