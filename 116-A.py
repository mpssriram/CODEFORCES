n= int(input())
onboard = 0
offrolling = 0
y=[]
 
for i in range(n):
   a=0
   b=0
   x = input()
   li = list(map(int,x.split()))
   a += li[0]
   b+= li[1]
   onboard += b
   onboard -= a
   y.append(onboard)
print(max(y))