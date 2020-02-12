print("enter a power of 2")
num=int(input())
s=set()
a=1
for i in range (num):
    a=a*2
    s.add(a)
print(s)