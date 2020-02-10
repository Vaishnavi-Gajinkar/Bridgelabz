print('enter number of elements')
num=int(input())
l=[]
count=0
s=0
print("enter the elements")
for a in range(num):
    a=int(input())
    l.append(a)
for i in range(len(l)):
    for j in range(1,len(l)):
        for k in range(2,len(l)):
            s=(l[i]+l[j]+l[k])
            if s==0:
                count+=1
                print(l[i],l[j],l[k])
print(count,"triplet exists")