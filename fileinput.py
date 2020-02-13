print("Enter number of Fruits to add")
n=int(input())
l=[]
f= open("List.txt",'w+')
print("Enter names of fruits")
for i in range(n):
    l.append(input())
l.sort()
f= open("List.txt",'a')
for j in range(len(l)-1):
    f.write(l[j])
    f.write(",")
f.write(l[-1])