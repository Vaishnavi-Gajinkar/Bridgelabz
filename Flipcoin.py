import random
h=0
t=0
a="Enter number of times to flip coin"
print(a)
n=int(input())
for i in range (n):
    num = random.randint(1,2)
    if num == 1:
        print("H")
        h+=1
    else:
        print("T")
        t+=1
sum=h+t
hp=float(h/sum*100)
tp=float(t/sum*100)
print("Heads percentage =")
print(hp)
print("Tails percentage =")
print(tp)