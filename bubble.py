print("enter the no of elements to sort")
num=int(input())
print("Enter the elements")
l=[]
for k in range(num):
    l.append(input())
print(l)
for i in range(num):
    for j in range(i+1,num):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp

print(l)
        