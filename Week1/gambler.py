import random
print("enter your stake")
s=int(input())
print("Enter your goal")
g=int(input())

count=0
i=0
while s>0 and s<g:
    num = random.randint(1,100)
    print("random ",num)
    flip= random.randint(1,2)
    if flip==1:
        s+=1
        print(s)
        count+=1
    else:
        s-=1
        print(s)
        count+=1
if s<=0:
    print("you lost your stake in ",count," bets")
elif s>=g:
    print("you reached goal in ",count," bets")
else:
    print("max bet limit reached")
