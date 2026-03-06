t = int(input())
for _ in range(t):
    inn = int(input())
    arr = list(input())
    i = 0

    while i < len(arr)-1:
        if arr[i] == '(' and arr[i+1] == ')':
            arr.pop(i)
            arr.pop(i)
            i = 0
        else:
            i += 1

    
    print(len(arr)//2)

"""class Stack():
    def __init__(self):
        self.content = []

    def push(self,x):
        return self.content.append(x)

    def pop(self):
        self.element = self.content.pop()
    def is_empty(self):
        length = len(self.content)
        if length == 0:
            return True
        else:
            return False
    def reverse_string(self,x):
        return x[::-1]"""